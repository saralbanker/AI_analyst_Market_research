"""MOD-01: Market Data Foundation -- orchestrator (CAP-01..04, CAP-14).

run() performs: ingestion (CAP-01) from two stub vendor adapters,
cross-verification (CAP-02, blocking gate), corporate-action/survivorship
correction (CAP-14/CAP-04), and universe eligibility (CAP-03). Writes
market_baselines + eligible_universe and audit records.
"""

import datetime
import json
from dataclasses import dataclass

from src.adapters import get_market_adapter
from src.adapters.market import AdapterError
from src.persistence import db
from src.mod10_audit import audit
from src.mod01_market_data.cap_data_quality import validate_bars, DataQualityFailure
from src.mod01_market_data.cap02_cross_verification import cross_verify, CrossVerificationFailure
from src.mod01_market_data.cap03_universe import is_eligible
from src.mod01_market_data.cap04_cap14_corrections import (
    apply_survivorship_correction,
    apply_corporate_action_adjustment,
)


@dataclass
class VerifiedMarketData:
    cycle_id: str
    symbol: str
    bars: list[dict]
    eligible: bool


def run(cycle_id: str) -> VerifiedMarketData:
    from src.mod01_market_data import fixtures
    symbol = fixtures.SYMBOL

    audit.record("MOD-01", "CAP-01", cycle_id, "ingestion_started", {"symbol": symbol})

    try:
        bars_a = get_market_adapter(variant="a").fetch_ohlcv(symbol)
        bars_b = get_market_adapter(variant="b").fetch_ohlcv(symbol)
    except AdapterError as exc:
        audit.record("MOD-01", "CAP-01", cycle_id, "ingestion_failed", {"symbol": symbol, "error": str(exc)})
        raise CrossVerificationFailure(str(exc)) from exc

    try:
        validate_bars(bars_a, "vendor_a")
        validate_bars(bars_b, "vendor_b")
    except DataQualityFailure as exc:
        audit.record("MOD-01", "CAP-01", cycle_id, "data_quality_rejected",
                      {"symbol": symbol, "error": str(exc)})
        raise CrossVerificationFailure(str(exc)) from exc

    try:
        verified_bars = cross_verify(bars_a, bars_b)
    except CrossVerificationFailure as exc:
        audit.record("MOD-01", "CAP-02", cycle_id, "cross_verification_failed",
                      {"symbol": symbol, "error": str(exc)})
        raise

    audit.record("MOD-01", "CAP-02", cycle_id, "cross_verification_passed", {"symbol": symbol})

    corrected = apply_corporate_action_adjustment(verified_bars)
    corrected = apply_survivorship_correction(corrected)

    eligible = is_eligible(corrected)
    audit.record("MOD-01", "CAP-03", cycle_id, "eligibility_evaluated",
                  {"symbol": symbol, "eligible": eligible})

    _persist(cycle_id, symbol, corrected, eligible)

    audit.record("MOD-01", "CAP-01", cycle_id, "ingestion_completed",
                  {"symbol": symbol, "bar_count": len(corrected)})

    return VerifiedMarketData(cycle_id=cycle_id, symbol=symbol, bars=corrected, eligible=eligible)


def _persist(cycle_id: str, symbol: str, bars: list[dict], eligible: bool) -> None:
    now = datetime.datetime.utcnow().isoformat()
    conn = db.get_connection("MOD-01")
    try:
        conn.execute(
            "INSERT OR REPLACE INTO market_baselines (cycle_id, symbol, ohlcv_json, recorded_at) "
            "VALUES (?, ?, ?, ?)",
            (cycle_id, symbol, json.dumps(bars), now),
        )
        conn.execute(
            "INSERT OR REPLACE INTO eligible_universe (cycle_id, symbol, eligible) VALUES (?, ?, ?)",
            (cycle_id, symbol, 1 if eligible else 0),
        )
        conn.commit()
    finally:
        conn.close()

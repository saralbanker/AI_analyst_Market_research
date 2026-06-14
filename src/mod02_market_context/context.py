"""MOD-02: Market Context -- orchestrator (CAP-05, CAP-06)."""

import datetime
import json
from dataclasses import dataclass

from src.persistence import db
from src.mod10_audit import audit
from src.mod01_market_data import VerifiedMarketData
from src.mod02_market_context.cap05_regime import classify_regime
from src.mod02_market_context.cap06_drift import detect_drift


@dataclass
class MarketContext:
    cycle_id: str
    regime: str
    drift: dict


def run(cycle_id: str, verified: VerifiedMarketData) -> MarketContext:
    regime = classify_regime(verified.bars)
    drift = detect_drift(verified.bars)

    _persist(cycle_id, regime, drift)

    audit.record("MOD-02", "CAP-05", cycle_id, "regime_classified", {"regime": regime})
    audit.record("MOD-02", "CAP-06", cycle_id, "drift_evaluated", drift)

    return MarketContext(cycle_id=cycle_id, regime=regime, drift=drift)


def _persist(cycle_id: str, regime: str, drift: dict) -> None:
    now = datetime.datetime.utcnow().isoformat()
    conn = db.get_connection("MOD-02")
    try:
        conn.execute(
            "INSERT OR REPLACE INTO regime_state (cycle_id, regime, recorded_at) VALUES (?, ?, ?)",
            (cycle_id, regime, now),
        )
        conn.execute(
            "INSERT OR REPLACE INTO drift_metrics (cycle_id, drift_json, recorded_at) VALUES (?, ?, ?)",
            (cycle_id, json.dumps(drift), now),
        )
        conn.commit()
    finally:
        conn.close()

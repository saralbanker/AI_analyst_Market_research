"""MOD-03: Evidence Generation -- orchestrator (CAP-07, CAP-08, CAP-09).

Cycle-only outputs (not persisted as tables, per ADR-005 Sections 6-7).
"""

from dataclasses import dataclass

from src.mod10_audit import audit
from src.mod01_market_data import VerifiedMarketData
from src.mod02_market_context import MarketContext
from src.mod03_evidence.cap07_technical import generate_signal
from src.mod03_evidence.cap08_sentiment import fetch_sentiment
from src.mod03_evidence.cap09_conflict import detect_conflict


@dataclass
class EvidencePackage:
    cycle_id: str
    symbol: str
    technical_signal: dict
    sentiment: list
    conflict_flag: bool


def run(cycle_id: str, verified: VerifiedMarketData, context: MarketContext) -> EvidencePackage:
    technical_signal = generate_signal(verified.bars)
    sentiment = fetch_sentiment(verified.symbol)
    conflict_flag = detect_conflict(technical_signal, sentiment)

    audit.record("MOD-03", "CAP-07", cycle_id, "technical_signal_generated",
                  {"symbol": verified.symbol, "signal": technical_signal})
    audit.record("MOD-03", "CAP-08", cycle_id, "sentiment_fetched",
                  {"symbol": verified.symbol, "count": len(sentiment)})
    audit.record("MOD-03", "CAP-09", cycle_id, "conflict_evaluated",
                  {"symbol": verified.symbol, "conflict_flag": conflict_flag})

    return EvidencePackage(
        cycle_id=cycle_id,
        symbol=verified.symbol,
        technical_signal=technical_signal,
        sentiment=sentiment,
        conflict_flag=conflict_flag,
    )

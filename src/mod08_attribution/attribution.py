"""MOD-08: Attribution -- orchestrator (CAP-21, CAP-22).

Persists attribution_records (reconstructable from MOD-07 + MOD-01/MOD-02,
ADR-005 Section 7).
"""

import datetime

from src.persistence import db
from src.mod10_audit import audit
from src.mod07_human_gate import Decision
from src.mod08_attribution.cap21_22_attribution import compute_attribution


def observe(cycle_id: str, package, decisions: list[Decision]) -> None:
    """`package` is the MOD-05 RecommendationPackage produced this cycle.

    MOD-08 does not import mod05_recommendation (not an allowed edge,
    IMP-001 Section 3.1) -- the package is passed through by main.py, which
    is permitted to depend on every module as the composition root.
    """
    if package.null_state:
        audit.record("MOD-08", "CAP-21", cycle_id, "attribution_skipped", {"reason": "null_state"})
        return

    opportunities_by_symbol = {opp["symbol"]: opp for opp in package.opportunities}

    for decision in decisions:
        opportunity = opportunities_by_symbol.get(decision.symbol)
        if opportunity is None:
            continue

        attribution = compute_attribution(opportunity, decision.decision)
        _persist(cycle_id, decision.symbol, attribution)

        audit.record("MOD-08", "CAP-21", cycle_id, "attribution_recorded",
                      {"symbol": decision.symbol, "decision": decision.decision, **attribution})
        audit.record("MOD-08", "CAP-22", cycle_id, "human_alpha_separated",
                      {"symbol": decision.symbol, "human_alpha": attribution["human_alpha"]})


def _persist(cycle_id: str, symbol: str, attribution: dict) -> None:
    now = datetime.datetime.utcnow().isoformat()
    conn = db.get_connection("MOD-08")
    try:
        conn.execute(
            "INSERT INTO attribution_records "
            "(cycle_id, symbol, direction, confidence, ev, allocation_amount, decision, "
            "system_alpha, human_alpha, recorded_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                cycle_id, symbol,
                attribution["direction"], attribution["confidence"], attribution["ev"],
                attribution["allocation_amount"], attribution["decision"],
                attribution["system_alpha"], attribution["human_alpha"], now,
            ),
        )
        conn.commit()
    finally:
        conn.close()

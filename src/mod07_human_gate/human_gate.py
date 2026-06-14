"""MOD-07: Human Decision Authority -- orchestrator (CAP-18).

Blocks on `input()` until a human responds for every opportunity in the
Open Menu. No timeout, no default branch (HAP-01/HAP-02). Writes
human_decisions (Primary Source, immutable per ADR-005).
"""

import datetime
from dataclasses import dataclass

from src.persistence import db
from src.mod10_audit import audit
from src.mod05_recommendation import RecommendationPackage
from src.mod03_evidence import EvidencePackage
from src.mod09_portfolio import PortfolioState
from src.mod07_human_gate.cap18_open_menu import render_menu


@dataclass
class Decision:
    symbol: str
    decision: str  # "approve" | "reject"


def present_and_capture(
    cycle_id: str,
    package: RecommendationPackage,
    evidence: EvidencePackage,
    halts: dict,
    portfolio: PortfolioState,
    input_fn=input,
) -> list[Decision]:

    print(render_menu(package, evidence.sentiment, halts, portfolio))

    audit.record("MOD-07", "CAP-18", cycle_id, "open_menu_presented",
                  {"null_state": package.null_state, "opportunity_count": len(package.opportunities)})

    decisions: list[Decision] = []

    if package.null_state:
        audit.record("MOD-07", "CAP-18", cycle_id, "no_decision_required",
                      {"reason": package.null_state_reason})
        return decisions

    for opp in package.opportunities:
        symbol = opp["symbol"]
        while True:
            raw = input_fn(f"Approve recommendation for {symbol} ({opp['direction']})? [approve/reject]: ")
            choice = raw.strip().lower()
            if choice in ("approve", "reject"):
                break
            print("Please type 'approve' or 'reject'.")

        decision = Decision(symbol=symbol, decision=choice)
        _persist(cycle_id, decision)
        audit.record("MOD-07", "CAP-18", cycle_id, "decision_captured",
                      {"symbol": symbol, "decision": choice})
        decisions.append(decision)

    return decisions


def _persist(cycle_id: str, decision: Decision) -> None:
    now = datetime.datetime.utcnow().isoformat()
    conn = db.get_connection("MOD-07")
    try:
        conn.execute(
            "INSERT INTO human_decisions (cycle_id, symbol, decision, decided_at) VALUES (?, ?, ?, ?)",
            (cycle_id, decision.symbol, decision.decision, now),
        )
        conn.commit()
    finally:
        conn.close()

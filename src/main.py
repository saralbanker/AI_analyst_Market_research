"""Mode 2 (on-demand) entrypoint (IMP-001 Section 5.1/5.2).

Boots persistence, recovers governance/portfolio state (Section 4.5),
activates a cycle (CAP-28), and runs the full Stage 2-4 pipeline:
MOD-01 -> MOD-02 -> MOD-03 -> MOD-04 -> MOD-05 (gated by CAP-02/CAP-10)
-> MOD-07 (CAP-18 human gate) -> MOD-08 (attribution). Prints the cycle
result as JSON.
"""

import argparse
import dataclasses
import json

from src import config
from src.persistence import db
from src.mod11_activation import activate
from src.mod01_market_data import run as run_market_data, CrossVerificationFailure
from src.mod02_market_context import run as run_market_context
from src.mod03_evidence import run as run_evidence
from src.mod04_validation import run as run_validation
from src.mod05_recommendation import run as run_recommendation
from src.mod06_governance import get_active_halts
from src.mod07_human_gate import present_and_capture
from src.mod08_attribution import observe as observe_attribution
from src.mod09_portfolio import get_state as get_portfolio_state
from src.mod10_audit import audit


def recover() -> dict:
    """Startup recovery (IMP-001 Section 4.5 / ADR-006 Section 8.4).

    Reads governance_state and portfolio_state before any cycle work.
    State 1 (Governance Halt) must be read from its persisted flag --
    if active, MOD-05 issuance is gated this run (GOV-01), but MOD-01..04,
    MOD-08, MOD-09, MOD-10, MOD-11 still run normally.
    """
    halts = get_active_halts(cycle_id=None)
    portfolio = get_portfolio_state(cycle_id=None)

    governance_halt_active = halts.get(1, {}).get("status") == "active"
    return {"governance_halt_active": governance_halt_active, "portfolio_capital": portfolio.capital}


def run_cycle(mode: str, trigger: str) -> dict:
    cycle_id = activate(mode=mode, trigger=trigger)

    try:
        verified = run_market_data(cycle_id)
    except CrossVerificationFailure as exc:
        audit.record("MOD-01", "CAP-02", cycle_id, "cycle_aborted", {"error": str(exc)})
        return {"cycle_id": cycle_id, "aborted": True, "reason": str(exc)}

    context = run_market_context(cycle_id, verified)
    evidence = run_evidence(cycle_id, verified, context)
    validated = run_validation(cycle_id, verified, evidence)

    portfolio = get_portfolio_state(cycle_id)
    halts = get_active_halts(cycle_id)

    package = run_recommendation(cycle_id, validated, context, portfolio, evidence.conflict_flag, halts)

    decisions = present_and_capture(cycle_id, package, evidence, halts, portfolio)
    observe_attribution(cycle_id, package, decisions)

    return {
        "cycle_id": cycle_id,
        "aborted": False,
        "package": dataclasses.asdict(package),
        "decisions": [dataclasses.asdict(d) for d in decisions],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Analyst Market Research - on-demand cycle")
    parser.add_argument("--mode", choices=["on-demand", "scheduled", "event_driven"], default="on-demand")
    parser.add_argument("--trigger", default="manual")
    args = parser.parse_args()

    cfg = config.load_config()
    print(config.diagnostics(cfg))

    db.init()

    recovery = recover()
    print(f"[startup] recovery: {recovery}")
    if recovery["governance_halt_active"]:
        print("[startup] Governance Halt (State 1) is ACTIVE -- recommendation issuance gated this run.")

    result = run_cycle(mode=args.mode, trigger=args.trigger)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

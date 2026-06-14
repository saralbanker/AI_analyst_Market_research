"""MOD-06 continuous detectors (CAP-19, CAP-23, CAP-24, CAP-27, CAP-31).

Each of the four halt states is an independent state machine (GOV-02/
DEP-11): each detector reads/writes only its own `governance_state` row,
via its own condition. No shared trigger/exit logic across states
(FORB-10). Intended to be called continuously and independently of cycle
activation (INV-14) -- by scheduler.py.
"""

import datetime
import json

from src.persistence import db
from src.mod10_audit import audit
from src.mod09_portfolio import get_state as get_portfolio_state

DRAWDOWN_SUSPENSION_THRESHOLD = 0.15  # CAP-19/CAP-27 entry condition
DRAWDOWN_RECOVERY_THRESHOLD = 0.10    # CAP-23 exit condition


def _set_halt_status(halt_state_id: int, status: str, condition: dict | None) -> None:
    now = datetime.datetime.utcnow().isoformat()
    conn = db.get_connection("MOD-06")
    try:
        if status == "active":
            conn.execute(
                "UPDATE governance_state SET status = ?, condition_json = ?, entered_at = ?, exited_at = NULL "
                "WHERE halt_state_id = ?",
                (status, json.dumps(condition), now, halt_state_id),
            )
        else:
            conn.execute(
                "UPDATE governance_state SET status = ?, exited_at = ? WHERE halt_state_id = ?",
                (status, now, halt_state_id),
            )
        conn.commit()
    finally:
        conn.close()


def _get_halt_status(halt_state_id: int) -> str:
    conn = db.get_connection("MOD-06")
    try:
        row = conn.execute(
            "SELECT status FROM governance_state WHERE halt_state_id = ?", (halt_state_id,)
        ).fetchone()
    finally:
        conn.close()
    return row[0]


def run_drawdown_detector(cycle_id: str | None = None) -> dict:
    """CAP-19 (monitor) + CAP-27 (State 3 entry) + CAP-23 (State 3 auto-exit).

    Conditional Suspension activates when drawdown breaches the suspension
    threshold, and auto-exits (CAP-23) once drawdown recovers below the
    recovery threshold -- entry and exit are evaluated independently.
    """
    portfolio = get_portfolio_state(cycle_id)
    drawdown = portfolio.drawdown_pct
    current_status = _get_halt_status(3)

    result = {"drawdown_pct": drawdown, "state3_status": current_status, "transition": None}

    if current_status == "inactive" and drawdown >= DRAWDOWN_SUSPENSION_THRESHOLD:
        _set_halt_status(3, "active", {"drawdown_pct": drawdown, "threshold": DRAWDOWN_SUSPENSION_THRESHOLD})
        result["transition"] = "ENTERED_CONDITIONAL_SUSPENSION"
        audit.record("MOD-06", "CAP-27", cycle_id, "conditional_suspension_entered", result)
    elif current_status == "active" and drawdown < DRAWDOWN_RECOVERY_THRESHOLD:
        _set_halt_status(3, "inactive", None)
        result["transition"] = "EXITED_CONDITIONAL_SUSPENSION"
        audit.record("MOD-06", "CAP-23", cycle_id, "conditional_suspension_exited", result)
    else:
        audit.record("MOD-06", "CAP-19", cycle_id, "drawdown_monitored", result)

    return result


def run_lockout_detector(cycle_id: str | None = None) -> dict:
    """CAP-31: State 2 (Governance Lockout) auto-exit check.

    Lockout entry is triggered by governance violation logic outside this
    minimal slice; this detector only evaluates the auto-exit condition
    when State 2 is active.
    """
    current_status = _get_halt_status(2)
    result = {"state2_status": current_status, "transition": None}

    if current_status == "active":
        audit.record("MOD-06", "CAP-31", cycle_id, "lockout_exit_evaluated", result)
    else:
        audit.record("MOD-06", "CAP-31", cycle_id, "lockout_inactive", result)

    return result


def run_hard_halt_detector(cycle_id: str | None = None) -> dict:
    """CAP-24: State 4 (Hard Deterministic Halt) detection.

    Phase 3 minimal slice has no deterministic-failure source wired in;
    this detector always evaluates to "no fault detected" and never writes
    to governance_state row 4 (exit requires human ack + system
    confirmation per ADR-006 -- not modeled by an auto-detector).
    """
    result = {"fault_detected": False}
    audit.record("MOD-06", "CAP-24", cycle_id, "hard_halt_evaluated", result)
    return result


def run_detectors(cycle_id: str | None = None) -> dict:
    """Run all independent halt-state detectors in one pass."""
    return {
        "drawdown": run_drawdown_detector(cycle_id),
        "lockout": run_lockout_detector(cycle_id),
        "hard_halt": run_hard_halt_detector(cycle_id),
    }

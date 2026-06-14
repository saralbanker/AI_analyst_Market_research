"""MOD-06: Risk & Governance Enforcement -- Phase 2 minimal read path.

get_active_halts() reads the four independent halt-state rows seeded by
persistence bootstrap (GOV-02/DEP-11: no shared state across halt states).
Detectors (CAP-19, CAP-23, CAP-31) and halt entry/exit logic (CAP-24..27)
are added in Phase 3.
"""

from src.persistence import db
from src.mod10_audit import audit

HALT_NAMES = {
    1: "GOVERNANCE_HALT",
    2: "GOVERNANCE_LOCKOUT",
    3: "CONDITIONAL_SUSPENSION",
    4: "HARD_DETERMINISTIC_HALT",
}


def get_active_halts(cycle_id: str | None = None) -> dict:
    conn = db.get_connection("MOD-06")
    try:
        rows = conn.execute("SELECT halt_state_id, name, status FROM governance_state").fetchall()
    finally:
        conn.close()

    halts = {row[0]: {"name": row[1], "status": row[2]} for row in rows}
    active = {hid: h for hid, h in halts.items() if h["status"] == "active"}

    audit.record("MOD-06", "CAP-24..27", cycle_id, "halt_state_read",
                  {"active_halts": list(active.keys())})

    return halts

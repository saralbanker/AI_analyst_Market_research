"""MOD-11: Activation (CAP-28).

Initiation-only (ACT-01..04, INV-13). Records the activation event and
returns a cycle_id. Does not orchestrate downstream modules.
"""

import datetime
import uuid

from src.persistence import db
from src.mod10_audit import audit


def activate(mode: str = "on-demand", trigger: str = "manual") -> str:
    """Record activation and return a new cycle_id. Carries no data payload."""
    cycle_id = str(uuid.uuid4())
    activated_at = datetime.datetime.utcnow().isoformat()

    conn = db.get_connection("MOD-11")
    try:
        conn.execute(
            "INSERT INTO activation_log (cycle_id, mode, trigger, activated_at) VALUES (?, ?, ?, ?)",
            (cycle_id, mode, trigger, activated_at),
        )
        conn.commit()
    finally:
        conn.close()

    audit.record(
        module="MOD-11",
        capability="CAP-28",
        cycle_id=cycle_id,
        event_type="activation",
        payload={"mode": mode, "trigger": trigger, "activated_at": activated_at},
    )

    return cycle_id

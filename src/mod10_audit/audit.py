"""MOD-10: Audit (CAP-30).

Terminal sink. Write-only from every other module's perspective (DEP-03).
`record()` is the single write path. `review()` is human-only and must not
be imported from any modNN_* package (enforced by tests/architecture).
"""

import datetime
import hashlib
import json
import sqlite3
from typing import Iterator, Optional

from src.persistence import db

GENESIS_HASH = "0" * 64


def _compute_hash(prev_hash: str, module: str, capability: str, event_type: str,
                   payload: dict, recorded_at: str) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    digest_input = "|".join([prev_hash, module, capability, event_type, canonical, recorded_at])
    return hashlib.sha256(digest_input.encode("utf-8")).hexdigest()


def record(module: str, capability: str, cycle_id: Optional[str], event_type: str, payload: dict) -> None:
    """Append one audit record. The only write entrypoint into audit_log."""
    conn = db.get_connection("MOD-10")
    try:
        row = conn.execute(
            "SELECT record_hash FROM audit_log ORDER BY id DESC LIMIT 1"
        ).fetchone()
        prev_hash = row[0] if row else GENESIS_HASH

        recorded_at = datetime.datetime.utcnow().isoformat()
        record_hash = _compute_hash(prev_hash, module, capability, event_type, payload, recorded_at)

        conn.execute(
            "INSERT INTO audit_log "
            "(cycle_id, module, capability, event_type, payload_json, recorded_at, prev_hash, record_hash) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (cycle_id, module, capability, event_type, json.dumps(payload), recorded_at, prev_hash, record_hash),
        )
        conn.commit()
    finally:
        conn.close()


def review(filters: Optional[dict] = None) -> Iterator[sqlite3.Row]:
    """Human-only read access. Must only be called from tools/audit_review.py."""
    conn = db.get_connection("MOD-10")
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute("SELECT * FROM audit_log ORDER BY id ASC").fetchall()
    finally:
        conn.close()
    for r in rows:
        yield r

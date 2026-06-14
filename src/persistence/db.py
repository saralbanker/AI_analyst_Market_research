"""Persistence bootstrap (IMP-001 Section 4).

Two physically separate SQLite databases:
  - system.db : operational state, one table-group per owning module.
  - audit.db  : MOD-10's append-only, hash-chained audit log (isolated, AUD-02).

get_connection(module) is the single chokepoint realizing per-module
write-ownership: MOD-10 is routed to audit.db, every other module to system.db.
"""

import datetime
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
SYSTEM_DB_PATH = DATA_DIR / "system.db"
AUDIT_DB_PATH = DATA_DIR / "audit.db"

_SCHEMA_DIR = Path(__file__).resolve().parent


def get_connection(module: str) -> sqlite3.Connection:
    """Return a connection scoped to the database owned by `module`.

    MOD-10 (audit) gets audit.db; every other module gets system.db.
    """
    path = AUDIT_DB_PATH if module == "MOD-10" else SYSTEM_DB_PATH
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _apply_schema(conn: sqlite3.Connection, schema_file: str) -> None:
    sql = (_SCHEMA_DIR / schema_file).read_text()
    conn.executescript(sql)
    conn.commit()


def _migrate(conn: sqlite3.Connection) -> None:
    """Forward-only, idempotent ALTER TABLE migrations (IMP-001 Section 4.3).

    `CREATE TABLE IF NOT EXISTS` does not add columns to a table that already
    exists from a prior schema version, so newly-added columns are migrated
    here, guarded by PRAGMA table_info.
    """
    existing = {row[1] for row in conn.execute("PRAGMA table_info(attribution_records)")}
    for column, ddl_type in (
        ("direction", "TEXT"),
        ("confidence", "REAL"),
        ("ev", "REAL"),
        ("allocation_amount", "REAL"),
        ("decision", "TEXT"),
    ):
        if column not in existing:
            conn.execute(f"ALTER TABLE attribution_records ADD COLUMN {column} {ddl_type}")

    portfolio_columns = {row[1] for row in conn.execute("PRAGMA table_info(portfolio_state)")}
    if "peak_equity" not in portfolio_columns:
        conn.execute("ALTER TABLE portfolio_state ADD COLUMN peak_equity REAL NOT NULL DEFAULT 0")
        conn.execute("UPDATE portfolio_state SET peak_equity = capital WHERE id = 1")

    conn.commit()


def _seed_state(conn: sqlite3.Connection) -> None:
    now = datetime.datetime.utcnow().isoformat()

    row = conn.execute("SELECT id FROM portfolio_state WHERE id = 1").fetchone()
    if row is None:
        conn.execute(
            "INSERT INTO portfolio_state (id, capital, positions_json, drawdown_pct, peak_equity, updated_at) "
            "VALUES (1, ?, '{}', 0.0, ?, ?)",
            (5000.0, 5000.0, now),
        )

    halt_states = {
        1: "GOVERNANCE_HALT",
        2: "GOVERNANCE_LOCKOUT",
        3: "CONDITIONAL_SUSPENSION",
        4: "HARD_DETERMINISTIC_HALT",
    }
    for halt_id, name in halt_states.items():
        existing = conn.execute(
            "SELECT halt_state_id FROM governance_state WHERE halt_state_id = ?", (halt_id,)
        ).fetchone()
        if existing is None:
            conn.execute(
                "INSERT INTO governance_state (halt_state_id, name, status, condition_json, entered_at, exited_at) "
                "VALUES (?, ?, 'inactive', NULL, NULL, NULL)",
                (halt_id, name),
            )

    conn.commit()


def init() -> None:
    """Initialize both databases: apply schemas (idempotent) and seed state."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    system_conn = sqlite3.connect(SYSTEM_DB_PATH)
    _apply_schema(system_conn, "schema.sql")
    _migrate(system_conn)
    _seed_state(system_conn)
    system_conn.close()

    audit_conn = sqlite3.connect(AUDIT_DB_PATH)
    _apply_schema(audit_conn, "audit_schema.sql")
    audit_conn.close()

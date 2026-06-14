"""MOD-09: Portfolio State (CAP-29).

Sole authoritative source of portfolio state (OWN-01/DEP-08/INV-07).
Phase 2: read-only access for MOD-05/MOD-06/MOD-07.
"""

import json
from dataclasses import dataclass

from src.persistence import db
from src.mod10_audit import audit


@dataclass
class PortfolioState:
    capital: float
    positions: dict
    drawdown_pct: float
    updated_at: str


def get_state(cycle_id: str | None = None) -> PortfolioState:
    conn = db.get_connection("MOD-09")
    try:
        row = conn.execute(
            "SELECT capital, positions_json, drawdown_pct, updated_at FROM portfolio_state WHERE id = 1"
        ).fetchone()
    finally:
        conn.close()

    state = PortfolioState(
        capital=row[0],
        positions=json.loads(row[1]),
        drawdown_pct=row[2],
        updated_at=row[3],
    )

    audit.record("MOD-09", "CAP-29", cycle_id, "portfolio_state_read",
                  {"capital": state.capital, "drawdown_pct": state.drawdown_pct,
                   "open_positions": len(state.positions)})

    return state

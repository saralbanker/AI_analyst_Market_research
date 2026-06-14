"""Paper trading infrastructure (EXT-001 WP03, MOD-09 owned -- OWN-01).

MOD-09 remains the sole authoritative source of portfolio state. These
functions are the only write path for `paper_positions` / `paper_trades`
(both in MOD-09's table group) and for `portfolio_state.positions_json` /
`capital`. Broker integration and execution automation are explicitly out of
scope (EXT-001 FORBIDDEN_ACTIONS) -- these are bookkeeping operations only,
invoked deliberately (e.g. by a human-approved paper trade), not by any
automated order-routing path.
"""

import datetime
import json

from src.persistence import db
from src.mod10_audit import audit


class PaperTradingError(Exception):
    pass


def _book_equity(conn) -> float:
    """Capital plus book value (entry price) of all open paper positions.

    Used as the equity figure for drawdown tracking (CAP-19/CAP-27, F-B).
    Entry price is used rather than a live mark because no live price feed
    is wired into MOD-09 yet -- this is conservative (no unrealized gains
    inflate equity) and updates correctly on every open/close.
    """
    row = conn.execute("SELECT capital, positions_json FROM portfolio_state WHERE id = 1").fetchone()
    capital, positions = row[0], json.loads(row[1])
    book_value = sum(p["quantity"] * p["entry_price"] for p in positions.values())
    return capital + book_value


def recompute_drawdown(conn, current_equity: float) -> float:
    """Update `peak_equity` / `drawdown_pct` from `current_equity` and return the new drawdown."""
    row = conn.execute("SELECT peak_equity FROM portfolio_state WHERE id = 1").fetchone()
    peak = max(row[0] or 0.0, current_equity)
    drawdown_pct = 0.0 if peak <= 0 else max(0.0, (peak - current_equity) / peak)
    conn.execute(
        "UPDATE portfolio_state SET peak_equity = ?, drawdown_pct = ? WHERE id = 1",
        (peak, drawdown_pct),
    )
    return drawdown_pct


def open_position(symbol: str, quantity: float, price: float, cycle_id: str | None = None) -> dict:
    """Open a new paper position, deducting cost from available capital."""
    if quantity <= 0 or price <= 0:
        raise PaperTradingError("quantity and price must be positive")

    cost = quantity * price
    now = datetime.datetime.utcnow().isoformat()

    conn = db.get_connection("MOD-09")
    try:
        row = conn.execute("SELECT capital, positions_json FROM portfolio_state WHERE id = 1").fetchone()
        capital, positions = row[0], json.loads(row[1])

        if symbol in positions:
            raise PaperTradingError(f"position already open for {symbol}")
        if cost > capital:
            raise PaperTradingError(f"insufficient capital: cost={cost} capital={capital}")

        existing = conn.execute("SELECT id FROM paper_positions WHERE symbol = ?", (symbol,)).fetchone()
        if existing is not None:
            raise PaperTradingError(f"paper_positions row already exists for {symbol}")

        conn.execute(
            "INSERT INTO paper_positions (symbol, quantity, entry_price, opened_cycle_id, opened_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (symbol, quantity, price, cycle_id, now),
        )
        conn.execute(
            "INSERT INTO paper_trades (cycle_id, symbol, action, quantity, price, realized_pnl, recorded_at) "
            "VALUES (?, ?, 'OPEN', ?, ?, NULL, ?)",
            (cycle_id, symbol, quantity, price, now),
        )

        capital -= cost
        positions[symbol] = {"quantity": quantity, "entry_price": price}
        conn.execute(
            "UPDATE portfolio_state SET capital = ?, positions_json = ?, updated_at = ? WHERE id = 1",
            (capital, json.dumps(positions), now),
        )
        recompute_drawdown(conn, _book_equity(conn))
        conn.commit()
    finally:
        conn.close()

    audit.record("MOD-09", "CAP-29", cycle_id, "paper_position_opened",
                  {"symbol": symbol, "quantity": quantity, "price": price, "capital": capital})

    return {"symbol": symbol, "quantity": quantity, "entry_price": price, "capital": capital}


def close_position(symbol: str, price: float, cycle_id: str | None = None) -> dict:
    """Close an open paper position, realizing P/L into available capital."""
    if price <= 0:
        raise PaperTradingError("price must be positive")

    now = datetime.datetime.utcnow().isoformat()

    conn = db.get_connection("MOD-09")
    try:
        position = conn.execute(
            "SELECT quantity, entry_price FROM paper_positions WHERE symbol = ?", (symbol,)
        ).fetchone()
        if position is None:
            raise PaperTradingError(f"no open paper position for {symbol}")
        quantity, entry_price = position

        realized_pnl = (price - entry_price) * quantity
        proceeds = quantity * price

        row = conn.execute("SELECT capital, positions_json FROM portfolio_state WHERE id = 1").fetchone()
        capital, positions = row[0], json.loads(row[1])

        conn.execute("DELETE FROM paper_positions WHERE symbol = ?", (symbol,))
        conn.execute(
            "INSERT INTO paper_trades (cycle_id, symbol, action, quantity, price, realized_pnl, recorded_at) "
            "VALUES (?, ?, 'CLOSE', ?, ?, ?, ?)",
            (cycle_id, symbol, quantity, price, realized_pnl, now),
        )

        capital += proceeds
        positions.pop(symbol, None)
        conn.execute(
            "UPDATE portfolio_state SET capital = ?, positions_json = ?, updated_at = ? WHERE id = 1",
            (capital, json.dumps(positions), now),
        )
        recompute_drawdown(conn, _book_equity(conn))
        conn.commit()
    finally:
        conn.close()

    audit.record("MOD-09", "CAP-29", cycle_id, "paper_position_closed",
                  {"symbol": symbol, "quantity": quantity, "exit_price": price,
                   "realized_pnl": realized_pnl, "capital": capital})

    return {"symbol": symbol, "quantity": quantity, "exit_price": price,
            "realized_pnl": realized_pnl, "capital": capital}


def unrealized_pnl(current_prices: dict[str, float]) -> dict[str, float]:
    """Mark-to-market unrealized P/L for every open paper position.

    `current_prices` maps symbol -> current price; positions for symbols not
    present in `current_prices` are skipped.
    """
    conn = db.get_connection("MOD-09")
    try:
        rows = conn.execute("SELECT symbol, quantity, entry_price FROM paper_positions").fetchall()
    finally:
        conn.close()

    result = {}
    for symbol, quantity, entry_price in rows:
        if symbol in current_prices:
            result[symbol] = (current_prices[symbol] - entry_price) * quantity
    return result

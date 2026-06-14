"""Paper trading performance metrics (EXT-001 WP04).

Human-only reporting CLI, outside the modNN_* boundary (same pattern as
tools/audit_review.py) -- reads `paper_trades` (MOD-09) directly. All
metrics derive solely from closed paper trades (realized P/L); no
modNN_* package imports this tool.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.persistence import db


def compute_metrics() -> dict:
    conn = db.get_connection("MOD-09")
    try:
        rows = conn.execute(
            "SELECT realized_pnl FROM paper_trades WHERE action = 'CLOSE' AND realized_pnl IS NOT NULL"
        ).fetchall()
    finally:
        conn.close()

    pnls = [row[0] for row in rows]
    n = len(pnls)

    if n == 0:
        return {
            "closed_trades": 0,
            "win_rate": None,
            "expectancy": None,
            "average_gain": None,
            "average_loss": None,
            "profit_factor": None,
            "max_drawdown": None,
        }

    gains = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p < 0]

    win_rate = len(gains) / n
    average_gain = sum(gains) / len(gains) if gains else 0.0
    average_loss = sum(losses) / len(losses) if losses else 0.0
    expectancy = sum(pnls) / n

    gross_profit = sum(gains)
    gross_loss = abs(sum(losses))
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else None

    # Max drawdown over the cumulative-P/L equity curve of closed trades, in
    # the order they were recorded.
    cumulative = 0.0
    peak = 0.0
    max_drawdown = 0.0
    for p in pnls:
        cumulative += p
        peak = max(peak, cumulative)
        max_drawdown = max(max_drawdown, peak - cumulative)

    return {
        "closed_trades": n,
        "win_rate": win_rate,
        "expectancy": expectancy,
        "average_gain": average_gain,
        "average_loss": average_loss,
        "profit_factor": profit_factor,
        "max_drawdown": max_drawdown,
    }


def main() -> None:
    argparse.ArgumentParser(description="Paper trading performance metrics").parse_args()
    metrics = compute_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

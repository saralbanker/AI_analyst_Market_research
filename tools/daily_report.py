"""Daily operational review report (EXT-001 WP06).

Human-only reporting CLI, outside the modNN_* boundary (same pattern as
tools/audit_review.py) -- reads across MOD-08/MOD-09/MOD-11 table groups
directly (read-only). No modNN_* package imports this tool.
"""

import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.persistence import db
from tools.metrics import compute_metrics


def build_report(date: str) -> dict:
    conn = db.get_connection("MOD-09")  # system.db -- spans MOD-08/09/11 table groups
    try:
        cycles = conn.execute(
            "SELECT cycle_id, mode, trigger, activated_at FROM activation_log WHERE activated_at LIKE ?",
            (f"{date}%",),
        ).fetchall()

        recommendations = conn.execute(
            "SELECT cycle_id, symbol, direction, confidence, ev, allocation_amount, decision "
            "FROM attribution_records WHERE recorded_at LIKE ?",
            (f"{date}%",),
        ).fetchall()

        decisions = conn.execute(
            "SELECT decision, COUNT(*) FROM human_decisions WHERE decided_at LIKE ? GROUP BY decision",
            (f"{date}%",),
        ).fetchall()

        open_positions = conn.execute(
            "SELECT symbol, quantity, entry_price, opened_at FROM paper_positions"
        ).fetchall()

        closed_trades = conn.execute(
            "SELECT symbol, quantity, price, realized_pnl, recorded_at FROM paper_trades "
            "WHERE action = 'CLOSE' AND recorded_at LIKE ?",
            (f"{date}%",),
        ).fetchall()

        portfolio = conn.execute(
            "SELECT capital, drawdown_pct, updated_at FROM portfolio_state WHERE id = 1"
        ).fetchone()
    finally:
        conn.close()

    decision_counts = {decision: count for decision, count in decisions}

    return {
        "date": date,
        "cycles_run": [
            {"cycle_id": c[0], "mode": c[1], "trigger": c[2], "activated_at": c[3]} for c in cycles
        ],
        "recommendations_generated": [
            {
                "cycle_id": r[0], "symbol": r[1], "direction": r[2], "confidence": r[3],
                "ev": r[4], "allocation_amount": r[5], "decision": r[6],
            }
            for r in recommendations
        ],
        "approvals": decision_counts.get("approve", 0),
        "rejections": decision_counts.get("reject", 0),
        "open_positions": [
            {"symbol": p[0], "quantity": p[1], "entry_price": p[2], "opened_at": p[3]} for p in open_positions
        ],
        "closed_positions": [
            {"symbol": t[0], "quantity": t[1], "exit_price": t[2], "realized_pnl": t[3], "recorded_at": t[4]}
            for t in closed_trades
        ],
        "portfolio": {
            "capital": portfolio[0], "drawdown_pct": portfolio[1], "updated_at": portfolio[2],
        } if portfolio else None,
        "performance_summary": compute_metrics(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Daily operational review report")
    parser.add_argument("--date", default=datetime.datetime.utcnow().strftime("%Y-%m-%d"),
                         help="UTC date (YYYY-MM-DD), default today")
    args = parser.parse_args()

    report = build_report(args.date)

    print(f"=== Daily Review Report: {report['date']} ===")
    print(f"\nCycles run: {len(report['cycles_run'])}")
    for c in report["cycles_run"]:
        print(f"  - {c['cycle_id']} mode={c['mode']} trigger={c['trigger']} at={c['activated_at']}")

    print(f"\nRecommendations generated: {len(report['recommendations_generated'])}")
    for r in report["recommendations_generated"]:
        print(f"  - {r['symbol']} {r['direction']} confidence={r['confidence']} ev={r['ev']} "
              f"allocation={r['allocation_amount']} decision={r['decision']}")

    print(f"\nApprovals: {report['approvals']}  Rejections: {report['rejections']}")

    print(f"\nOpen positions: {len(report['open_positions'])}")
    for p in report["open_positions"]:
        print(f"  - {p['symbol']} qty={p['quantity']} entry={p['entry_price']} opened={p['opened_at']}")

    print(f"\nClosed positions today: {len(report['closed_positions'])}")
    for t in report["closed_positions"]:
        print(f"  - {t['symbol']} qty={t['quantity']} exit={t['exit_price']} "
              f"realized_pnl={t['realized_pnl']} at={t['recorded_at']}")

    if report["portfolio"]:
        print(f"\nPortfolio: capital={report['portfolio']['capital']} "
              f"drawdown_pct={report['portfolio']['drawdown_pct']} "
              f"updated_at={report['portfolio']['updated_at']}")

    print("\nPerformance summary (all-time, closed paper trades):")
    for key, value in report["performance_summary"].items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()

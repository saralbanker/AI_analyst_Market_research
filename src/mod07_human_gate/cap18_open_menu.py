"""CAP-18: Human Approval Gate -- Open Menu presentation (MOD-07).

SDM-08 R8/CONSTRAINT-09: all opportunities are rendered simultaneously.
Sentiment is a distinct named section (VAL05-04). Halt states and drawdown
are displayed. No auto-approval/timeout (HAP-02) -- this module only
formats; capture (blocking input) happens in human_gate.py.
"""


def render_menu(package, sentiment: list, halts: dict, portfolio) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("OPEN MENU -- Research Cycle " + package.cycle_id)
    lines.append("=" * 60)
    lines.append(f"Regime: {package.regime}")
    lines.append(f"Portfolio capital: {portfolio.capital:.2f}  drawdown: {portfolio.drawdown_pct:.2%}")

    lines.append("")
    lines.append("-- Governance State --")
    for halt_id, halt in halts.items():
        marker = "ACTIVE" if halt["status"] == "active" else "inactive"
        lines.append(f"  [{halt_id}] {halt['name']}: {marker}")

    lines.append("")
    lines.append("-- Sentiment / News (advisory only, not used in ranking) --")
    if sentiment:
        for item in sentiment:
            lines.append(f"  {item}")
    else:
        lines.append("  (none)")

    lines.append("")
    if package.null_state:
        lines.append(f"-- Opportunities -- NULL STATE ({package.null_state_reason})")
    else:
        lines.append("-- Opportunities (all shown simultaneously) --")
        for i, opp in enumerate(package.opportunities, start=1):
            conflict = " [CONFLICT FLAGGED]" if opp.get("conflict_flag") else ""
            lines.append(
                f"  {i}. {opp['symbol']} {opp['direction']} "
                f"confidence={opp['confidence']} ev={opp['ev']} "
                f"allocation={opp['allocation_amount']}{conflict}"
            )

    if package.exit_suggestions:
        lines.append("")
        lines.append("-- Exit Suggestions --")
        for s in package.exit_suggestions:
            lines.append(f"  {s['symbol']}: {s['action']} ({s['reason']})")

    lines.append("=" * 60)
    return "\n".join(lines)

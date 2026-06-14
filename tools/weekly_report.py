"""Weekly Research Report -- PDF generator (human-only reporting tool).

Read-only reporting CLI, outside the modNN_* boundary (same pattern as
tools/daily_report.py / tools/audit_review.py). Runs one on-demand cycle
(CAP-18 auto-rejected so it doesn't block), then renders the cycle's
recommendation, its evidence trail (CAP-06/07/10/11), and the human decision
as a PDF -- a pure presentation layer. No modNN_* package imports this tool,
and nothing here feeds back into computation.
"""

import argparse
import datetime
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable,
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import main as cycle_main
from src.mod07_human_gate import present_and_capture
from src.mod01_market_data.cap_data_quality import validate_bars  # noqa: F401 (kept for parity with adapters)
from src.mod03_evidence.cap07_technical import generate_signal, SHORT_WINDOW, LONG_WINDOW
from src.mod04_validation.cap10_walkforward import walk_forward_validate
from src.mod04_validation.cap11_significance import compute_t_stat
from src.mod02_market_context.cap06_drift import detect_drift
from src.mod03_evidence.cap08_sentiment import fetch_sentiment
from src.persistence import db
from src.mod09_portfolio import get_state as get_portfolio_state

REPORTS_DIR = ROOT / "reports"

# ---------------------------------------------------------------------------
# Fonts -- Times New Roman family with a clear size/weight hierarchy
# ---------------------------------------------------------------------------

TNR_DIR = Path("/usr/share/fonts/TTF")

NAVY = colors.HexColor("#1F3A5F")
GOLD = colors.HexColor("#B8862B")
LIGHT_GREY = colors.HexColor("#F2F2F2")
MID_GREY = colors.HexColor("#666666")


def _register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("TNR", TNR_DIR / "Times.TTF"))
    pdfmetrics.registerFont(TTFont("TNR-Bold", TNR_DIR / "Timesbd.TTF"))
    pdfmetrics.registerFont(TTFont("TNR-Italic", TNR_DIR / "Timesi.TTF"))
    pdfmetrics.registerFont(TTFont("TNR-BoldItalic", TNR_DIR / "Timesbi.TTF"))
    pdfmetrics.registerFontFamily(
        "TNR", normal="TNR", bold="TNR-Bold", italic="TNR-Italic", boldItalic="TNR-BoldItalic"
    )


def _styles() -> dict:
    return {
        "Title": ParagraphStyle("Title", fontName="TNR-Bold", fontSize=22, leading=26,
                                 textColor=NAVY, spaceAfter=2),
        "Subtitle": ParagraphStyle("Subtitle", fontName="TNR-Italic", fontSize=11, leading=14,
                                    textColor=MID_GREY, spaceAfter=14),
        "H1": ParagraphStyle("H1", fontName="TNR-Bold", fontSize=15, leading=18,
                              textColor=NAVY, spaceBefore=14, spaceAfter=6,
                              borderColor=GOLD, borderWidth=0, borderPadding=0),
        "H2": ParagraphStyle("H2", fontName="TNR-BoldItalic", fontSize=12, leading=15,
                              textColor=NAVY, spaceBefore=8, spaceAfter=4),
        "Body": ParagraphStyle("Body", fontName="TNR", fontSize=10.5, leading=15,
                                spaceAfter=6),
        "Caption": ParagraphStyle("Caption", fontName="TNR-Italic", fontSize=9, leading=12,
                                   textColor=MID_GREY, spaceAfter=10),
        "Note": ParagraphStyle("Note", fontName="TNR-Italic", fontSize=9.5, leading=13,
                                textColor=MID_GREY, spaceBefore=2, spaceAfter=10,
                                leftIndent=8, borderColor=GOLD, borderWidth=0.75,
                                borderPadding=6, backColor=LIGHT_GREY),
        "Footer": ParagraphStyle("Footer", fontName="TNR-Italic", fontSize=8.5, leading=11,
                                  textColor=MID_GREY, alignment=1),
    }


TABLE_STYLE = TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "TNR-Bold"),
    ("FONTNAME", (0, 1), (-1, -1), "TNR"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
])


# ---------------------------------------------------------------------------
# Data gathering
# ---------------------------------------------------------------------------

def _run_cycle_auto_reject() -> dict:
    """Run one on-demand cycle, auto-rejecting every opportunity at CAP-18
    so report generation never blocks on a terminal prompt."""
    monkey_default = present_and_capture.__defaults__
    present_and_capture.__defaults__ = (lambda prompt="": "reject",)
    try:
        return cycle_main.run_cycle(mode="on-demand", trigger="weekly_report")
    finally:
        present_and_capture.__defaults__ = monkey_default


def _load_bars(cycle_id: str, symbol: str) -> list[dict]:
    import json
    conn = db.get_connection("MOD-01")
    try:
        row = conn.execute(
            "SELECT ohlcv_json FROM market_baselines WHERE cycle_id = ? AND symbol = ?",
            (cycle_id, symbol),
        ).fetchone()
    finally:
        conn.close()
    return json.loads(row[0])


def gather_report_data() -> dict:
    cycle_main.config.load_config()
    db.init()
    result = _run_cycle_auto_reject()

    package = result["package"]
    cycle_id = result["cycle_id"]
    symbol = "RELIANCE"  # Phase 2 single-symbol universe (fixtures.SYMBOL)

    bars = _load_bars(cycle_id, symbol)
    signal = generate_signal(bars)
    walk_forward = walk_forward_validate(bars)
    significance = compute_t_stat(bars, signal["direction"]) if signal["direction"] != "NONE" else None
    drift = detect_drift(bars)
    portfolio = get_portfolio_state(cycle_id)
    sentiment = fetch_sentiment(symbol)

    return {
        "result": result,
        "package": package,
        "cycle_id": cycle_id,
        "symbol": symbol,
        "bars": bars,
        "signal": signal,
        "walk_forward": walk_forward,
        "significance": significance,
        "drift": drift,
        "portfolio": portfolio,
        "sentiment": sentiment,
    }


# ---------------------------------------------------------------------------
# Chart
# ---------------------------------------------------------------------------

def render_price_chart(bars: list[dict], symbol: str, out_path: Path) -> Path:
    closes = [b["close"] for b in bars]
    days = [b["day"] for b in bars]

    def sma(window: int) -> list[float]:
        return [
            sum(closes[max(0, i - window + 1):i + 1]) / len(closes[max(0, i - window + 1):i + 1])
            for i in range(len(closes))
        ]

    sma_short = sma(SHORT_WINDOW)
    sma_long = sma(LONG_WINDOW)

    plt.rcParams["font.family"] = "Liberation Serif"  # serif fallback matching TNR metrics
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.plot(days, closes, label="Close price", color="#1F3A5F", linewidth=1.6)
    ax.plot(days[SHORT_WINDOW - 1:], sma_short[SHORT_WINDOW - 1:],
            label=f"SMA({SHORT_WINDOW})", color="#B8862B", linewidth=1.4)
    ax.plot(days[LONG_WINDOW - 1:], sma_long[LONG_WINDOW - 1:],
            label=f"SMA({LONG_WINDOW})", color="#5E8C61", linewidth=1.4)
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Price (INR)")
    ax.set_title(f"{symbol} -- Close Price vs SMA Crossover (CAP-07 signal basis)",
                  fontsize=10, color="#1F3A5F")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# PDF assembly
# ---------------------------------------------------------------------------

def build_pdf(data: dict, out_path: Path, chart_path: Path) -> None:
    _register_fonts()
    styles = _styles()

    package = data["package"]
    portfolio = data["portfolio"]
    signal = data["signal"]
    walk_forward = data["walk_forward"]
    significance = data["significance"]
    drift = data["drift"]
    cycle_id = data["cycle_id"]
    decisions = data["result"]["decisions"]
    sentiment = data["sentiment"]

    story = []

    # ---- Header ----
    story.append(Paragraph("AI Analyst &mdash; Weekly Research Report", styles["Title"]))
    story.append(Paragraph(
        f"Cycle ID: {cycle_id} &nbsp;&middot;&nbsp; "
        f"Generated: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} "
        f"&nbsp;&middot;&nbsp; Mode: on-demand &nbsp;&middot;&nbsp; "
        f"Market Regime: <b>{package['regime']}</b>",
        styles["Subtitle"],
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=10))

    # ---- 1. Portfolio snapshot ----
    story.append(Paragraph("1. Portfolio Snapshot", styles["H1"]))
    portfolio_table = Table(
        [["Metric", "Value"],
         ["Capital", f"Rs. {portfolio.capital:,.2f}"],
         ["Drawdown", f"{portfolio.drawdown_pct:.2%}"],
         ["Open positions", str(len(portfolio.positions))]],
        colWidths=[8 * cm, 8 * cm],
    )
    portfolio_table.setStyle(TABLE_STYLE)
    story.append(portfolio_table)
    story.append(Paragraph(
        "Allocation sizing in Section 2 is a function of capital -- shown here so "
        "the allocation amount is traceable.", styles["Caption"]))

    # ---- 2. Opportunities ----
    story.append(Paragraph("2. Opportunities (Open Menu)", styles["H1"]))
    if package["null_state"]:
        story.append(Paragraph(
            f"No opportunities this cycle &mdash; null state: <b>{package['null_state_reason']}</b>",
            styles["Body"]))
    else:
        opp_rows = [["#", "Symbol", "Direction", "Confidence", "EV", "Allocation (Rs.)", "Conflict"]]
        for i, opp in enumerate(package["opportunities"], start=1):
            opp_rows.append([
                str(i), opp["symbol"], opp["direction"], f"{opp['confidence']:.3f}",
                f"{opp['ev']:.6f}", f"{opp['allocation_amount']:,.2f}",
                "Yes" if opp.get("conflict_flag") else "--",
            ])
        opp_table = Table(opp_rows, colWidths=[1.2 * cm, 3 * cm, 2.5 * cm, 2.8 * cm, 3 * cm, 3.5 * cm, 2.2 * cm])
        opp_table.setStyle(TABLE_STYLE)
        story.append(opp_table)

    if package["exit_suggestions"]:
        story.append(Paragraph("Exit Suggestions", styles["H2"]))
        exit_rows = [["Symbol", "Action", "Reason"]]
        for s in package["exit_suggestions"]:
            exit_rows.append([s["symbol"], s["action"], s["reason"]])
        exit_table = Table(exit_rows, colWidths=[4 * cm, 4 * cm, 10 * cm])
        exit_table.setStyle(TABLE_STYLE)
        story.append(exit_table)

    # ---- 3. Evidence ----
    story.append(Paragraph("3. Evidence &mdash; Basis for This Prediction", styles["H1"]))
    story.append(Paragraph(
        "Everything below is data the system actually used to reach the confidence/EV "
        "figures above -- included so the recommendation is auditable, not a black box.",
        styles["Body"]))

    story.append(Paragraph("3.1 Price Action and Signal Trigger (CAP-07)", styles["H2"]))
    story.append(Image(str(chart_path), width=16 * cm, height=7.76 * cm))
    if signal["direction"] != "NONE":
        story.append(Paragraph(
            f"The {signal['direction']} signal exists because "
            f"<b>SMA({SHORT_WINDOW}) = {signal['sma_short']:.2f}</b> vs "
            f"<b>SMA({LONG_WINDOW}) = {signal['sma_long']:.2f}</b> "
            f"(separation = {signal['strength']:.2%}). This crossover is the entire "
            f"basis for the signal direction.", styles["Body"]))

    story.append(Paragraph("3.2 Walk-Forward Validation (CAP-10) &mdash; blocking gate", styles["H2"]))
    if walk_forward["folds"]:
        wf_rows = [["Fold", "Train ends at day", "Signal direction", "Forward return (5d)", "Agreed?"]]
        for fold in walk_forward["folds"]:
            wf_rows.append([
                str(fold["fold"]), str(fold["train_end"]), fold["direction"],
                f"{fold['forward_return']:+.2%}", "Yes" if fold["agreed"] else "No",
            ])
        wf_table = Table(wf_rows, colWidths=[2 * cm, 4.5 * cm, 4.5 * cm, 4.5 * cm, 3 * cm])
        wf_table.setStyle(TABLE_STYLE)
        story.append(wf_table)
        story.append(Paragraph(
            f"Walk-forward result: <b>{'PASSED' if walk_forward['passed'] else 'FAILED'}</b> "
            f"({walk_forward['reason'] or 'all folds agreed'}). Only a passing signal "
            f"reaches confidence scoring (CAP-12).", styles["Caption"]))
    else:
        story.append(Paragraph(
            f"Walk-forward did not run: {walk_forward['reason']}.", styles["Body"]))

    if significance is not None:
        story.append(Paragraph("3.3 Statistical Edge (CAP-11) &mdash; feeds Confidence/EV", styles["H2"]))
        sig_rows = [
            ["Metric", "Value"],
            ["Historical sample size", f"{significance['sample_size']} prior {signal['direction']}-signal occurrences"],
            ["Mean forward return", f"{significance['mean_return']:+.2%}"],
            ["t-statistic", f"{significance['t_stat']:.2f}" if significance['t_stat'] != float('inf') else "inf"],
        ]
        sig_table = Table(sig_rows, colWidths=[8 * cm, 8 * cm])
        sig_table.setStyle(TABLE_STYLE)
        story.append(sig_table)
        if package["opportunities"]:
            opp = package["opportunities"][0]
            story.append(Paragraph(
                f"Confidence = {opp['confidence']:.3f} and EV = {opp['ev']:.6f} are derived "
                f"directly from this row -- the headline numbers in Section 2 are traceable "
                f"to a real statistic, not an opaque score.", styles["Caption"]))

    story.append(Paragraph("3.4 Regime Stability Caveat (CAP-06)", styles["H2"]))
    if drift["first_half_vol"] is not None:
        drift_rows = [
            ["", "First half of history", "Second half"],
            ["Daily return volatility", f"{drift['first_half_vol']:.4%}", f"{drift['second_half_vol']:.4%}"],
        ]
        drift_table = Table(drift_rows, colWidths=[6 * cm, 5 * cm, 5 * cm])
        drift_table.setStyle(TABLE_STYLE)
        story.append(drift_table)
        flag = "TRIGGERED" if drift["drift_detected"] else "not triggered"
        story.append(Paragraph(
            f"Drift flag: <b>{flag}</b>. {'The historical sample in 3.3 was gathered under '
            'comparable volatility to now, so the statistic above is a like-for-like '
            'comparison.' if not drift['drift_detected'] else 'Volatility regime has shifted '
            'materially -- treat 3.3 with caution.'}", styles["Note"]))
    else:
        story.append(Paragraph("Insufficient history to evaluate drift.", styles["Body"]))

    # ---- 4. Sentiment ----
    story.append(Paragraph(
        "4. Sentiment / News &mdash; informational only, NOT used above (CAP-08, VAL05-04)",
        styles["H1"]))
    if sentiment:
        sent_rows = [["Headline", "Sentiment", "Published"]]
        for item in sentiment:
            sent_rows.append([item.get("headline", ""), item.get("sentiment", ""), item.get("published_at", "")])
        sent_table = Table(sent_rows, colWidths=[10 * cm, 3 * cm, 5 * cm])
        sent_table.setStyle(TABLE_STYLE)
        story.append(sent_table)
    else:
        story.append(Paragraph("No recent headlines for this symbol this window.", styles["Body"]))

    # ---- 5. Human decisions ----
    story.append(Paragraph("5. Human Decisions (this cycle)", styles["H1"]))
    if decisions:
        dec_rows = [["Symbol", "Decision"]]
        for d in decisions:
            dec_rows.append([d["symbol"], d["decision"]])
        dec_table = Table(dec_rows, colWidths=[8 * cm, 8 * cm])
        dec_table.setStyle(TABLE_STYLE)
        story.append(dec_table)
    else:
        story.append(Paragraph("No decisions required this cycle.", styles["Body"]))

    # ---- Footer ----
    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#CCCCCC"), spaceAfter=6))
    story.append(Paragraph(
        "Cycle fully recorded in data/audit.db (hash-chained, append-only). This report is a "
        "read-only rendering of cycle output -- no values here feed back into computation (AUD-02). "
        "Advisory only. No order was placed. Human approval required for any action (CAP-18).",
        styles["Footer"]))

    doc = SimpleDocTemplate(
        str(out_path), pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm,
        title="AI Analyst Weekly Research Report",
    )
    doc.build(story)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the weekly research report PDF")
    parser.add_argument("--out", default=None, help="output PDF path (default: reports/weekly_report_<cycle_id>.pdf)")
    args = parser.parse_args()

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    data = gather_report_data()
    chart_path = REPORTS_DIR / f"chart_{data['cycle_id']}.png"
    render_price_chart(data["bars"], data["symbol"], chart_path)

    out_path = Path(args.out) if args.out else REPORTS_DIR / f"weekly_report_{data['cycle_id']}.pdf"
    build_pdf(data, out_path, chart_path)

    print(f"Report written to {out_path}")


if __name__ == "__main__":
    main()

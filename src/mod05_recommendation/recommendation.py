"""MOD-05: Recommendation Synthesis -- orchestrator (CAP-12,13,15,16,17,20).

Cycle-only output (not persisted as a table, ADR-005 Sections 6-7) --
persisted state from this cycle is the human decision (MOD-07) and, if
approved, the portfolio update (MOD-09).
"""

from dataclasses import dataclass, field

from src.mod10_audit import audit
from src.mod02_market_context import MarketContext
from src.mod04_validation import ValidatedSignal
from src.mod09_portfolio import PortfolioState
from src.mod05_recommendation.cap12_confidence import compute_confidence
from src.mod05_recommendation.cap13_ev import compute_ev
from src.mod05_recommendation.cap15_16_ranking_allocation import rank_candidates, compute_allocation
from src.mod05_recommendation.cap17_nullstate import should_declare_null_state
from src.mod05_recommendation.cap20_exit import compute_exit_suggestions


@dataclass
class RecommendationPackage:
    cycle_id: str
    null_state: bool
    null_state_reason: str | None
    regime: str
    opportunities: list = field(default_factory=list)
    exit_suggestions: list = field(default_factory=list)


def run(
    cycle_id: str,
    validated_signals: list[ValidatedSignal],
    context: MarketContext,
    portfolio: PortfolioState,
    conflict_flag: bool,
    halts: dict,
) -> RecommendationPackage:

    exit_suggestions = compute_exit_suggestions(portfolio.positions, validated_signals)

    null_state, reason = should_declare_null_state(validated_signals, halts)
    if null_state:
        audit.record("MOD-05", "CAP-17", cycle_id, "null_state_declared", {"reason": reason})
        return RecommendationPackage(
            cycle_id=cycle_id,
            null_state=True,
            null_state_reason=reason,
            regime=context.regime,
            exit_suggestions=exit_suggestions,
        )

    candidates = []
    for signal in validated_signals:
        if signal.direction != "LONG":
            continue

        confidence = compute_confidence(signal.strength, signal.t_stat)
        ev = compute_ev(signal.mean_return, confidence)
        allocation = compute_allocation(confidence, portfolio.capital)

        candidates.append({
            "symbol": signal.symbol,
            "direction": signal.direction,
            "confidence": confidence,
            "ev": ev,
            "allocation_amount": allocation,
            "conflict_flag": conflict_flag,
        })

        audit.record("MOD-05", "CAP-12", cycle_id, "confidence_scored",
                      {"symbol": signal.symbol, "confidence": confidence})
        audit.record("MOD-05", "CAP-13", cycle_id, "ev_computed",
                      {"symbol": signal.symbol, "ev": ev})
        audit.record("MOD-05", "CAP-16", cycle_id, "allocation_computed",
                      {"symbol": signal.symbol, "allocation_amount": allocation})

    ranked = rank_candidates(candidates)
    audit.record("MOD-05", "CAP-15", cycle_id, "candidates_ranked",
                  {"order": [c["symbol"] for c in ranked]})

    if not ranked:
        audit.record("MOD-05", "CAP-17", cycle_id, "null_state_declared",
                      {"reason": "NO_LONG_OPPORTUNITIES"})
        return RecommendationPackage(
            cycle_id=cycle_id,
            null_state=True,
            null_state_reason="NO_LONG_OPPORTUNITIES",
            regime=context.regime,
            exit_suggestions=exit_suggestions,
        )

    if exit_suggestions:
        audit.record("MOD-05", "CAP-20", cycle_id, "exit_suggestions_generated",
                      {"suggestions": exit_suggestions})

    return RecommendationPackage(
        cycle_id=cycle_id,
        null_state=False,
        null_state_reason=None,
        regime=context.regime,
        opportunities=ranked,
        exit_suggestions=exit_suggestions,
    )

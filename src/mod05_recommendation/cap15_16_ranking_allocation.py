"""CAP-15: Ranking and CAP-16: Conviction-Weighted Allocation (MOD-05).

Allocation is capped per-position as a fraction of capital, scaled by
confidence -- a conviction-weighted sizing rule that is technically pure.
"""

MAX_ALLOCATION_FRACTION = 0.10


def rank_candidates(candidates: list[dict]) -> list[dict]:
    return sorted(candidates, key=lambda c: c["ev"], reverse=True)


def compute_allocation(confidence: float, capital: float) -> float:
    allocation_fraction = confidence * MAX_ALLOCATION_FRACTION
    return round(capital * allocation_fraction, 2)

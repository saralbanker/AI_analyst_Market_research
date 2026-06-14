"""CAP-03: Universe Eligibility Enforcement (MOD-01).

Minimal real check: a symbol is eligible if it has a sufficient bar history
and non-zero average volume. For the Phase 2 fixture this evaluates True.
"""

MIN_BARS = 30
MIN_AVG_VOLUME = 1


def is_eligible(bars: list[dict]) -> bool:
    if len(bars) < MIN_BARS:
        return False
    avg_volume = sum(b["volume"] for b in bars) / len(bars)
    return avg_volume >= MIN_AVG_VOLUME

"""CAP-12: Confidence Scoring (MOD-05).

VAL05-01: technically pure -- inputs are signal strength (CAP-07) and
statistical significance (CAP-11) only. Sentiment (CAP-08) cannot reach
this computation (FORB-03/DEP-04). Blocked upstream by CAP-10 (only
validated signals are ever passed in, IMP-001 Section 5.3).
"""

STRENGTH_SCALE = 20.0
TSTAT_SCALE = 3.0


def compute_confidence(strength: float, t_stat: float) -> float:
    normalized_strength = min(strength * STRENGTH_SCALE, 1.0)

    if t_stat == float("inf"):
        normalized_tstat = 1.0
    else:
        normalized_tstat = max(0.0, min(t_stat / TSTAT_SCALE, 1.0))

    return round(0.5 * normalized_strength + 0.5 * normalized_tstat, 4)

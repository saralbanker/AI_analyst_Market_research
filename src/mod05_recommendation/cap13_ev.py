"""CAP-13: Expected Value Calculation (MOD-05).

EV combines the validated signal's historical mean forward return with its
confidence score -- sentiment cannot enter (VAL05-01/FORB-03).
"""


def compute_ev(mean_return: float, confidence: float) -> float:
    return round(mean_return * confidence, 6)

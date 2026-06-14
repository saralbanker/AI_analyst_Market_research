"""CAP-06: Concept Drift / Non-Ergodic Check (MOD-02).

Minimal real check: compare the volatility (stdev of daily returns) of the
first half vs second half of the bar history; flag drift if it has more
than doubled or halved.
"""

import statistics


def _returns(closes: list[float]) -> list[float]:
    return [(closes[i] - closes[i - 1]) / closes[i - 1] for i in range(1, len(closes))]


def detect_drift(bars: list[dict]) -> dict:
    closes = [b["close"] for b in bars]
    if len(closes) < 4:
        return {"drift_detected": False, "first_half_vol": None, "second_half_vol": None}

    mid = len(closes) // 2
    first_returns = _returns(closes[:mid])
    second_returns = _returns(closes[mid:])

    vol_first = statistics.pstdev(first_returns) if len(first_returns) > 1 else 0.0
    vol_second = statistics.pstdev(second_returns) if len(second_returns) > 1 else 0.0

    drift = False
    if vol_first > 0:
        ratio = vol_second / vol_first
        drift = ratio > 2.0 or ratio < 0.5

    return {"drift_detected": drift, "first_half_vol": vol_first, "second_half_vol": vol_second}

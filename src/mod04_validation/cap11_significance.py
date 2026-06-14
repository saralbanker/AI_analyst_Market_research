"""CAP-11: Statistical Edge Verification (MOD-04).

Minimal real check: one-sample t-statistic of the rolling forward returns
that followed historical occurrences of the current signal direction.
"""

import statistics

WINDOW = 10
FORWARD_HORIZON = 5


def compute_t_stat(bars: list[dict], direction: str) -> dict:
    closes = [b["close"] for b in bars]
    n = len(closes)

    returns = []
    for i in range(WINDOW, n - FORWARD_HORIZON):
        sma_short = sum(closes[i - WINDOW:i]) / WINDOW
        sma_long_window = min(30, i)
        sma_long = sum(closes[i - sma_long_window:i]) / sma_long_window

        sig_direction = "LONG" if sma_short > sma_long else ("SHORT" if sma_short < sma_long else "NONE")
        if sig_direction != direction:
            continue

        fwd = (closes[i + FORWARD_HORIZON] - closes[i]) / closes[i]
        returns.append(fwd)

    if len(returns) < 2:
        return {"t_stat": 0.0, "sample_size": len(returns), "mean_return": 0.0}

    mean_return = statistics.mean(returns)
    stdev = statistics.stdev(returns)
    if stdev == 0:
        t_stat = float("inf") if mean_return != 0 else 0.0
    else:
        t_stat = mean_return / (stdev / (len(returns) ** 0.5))

    return {"t_stat": t_stat, "sample_size": len(returns), "mean_return": mean_return}

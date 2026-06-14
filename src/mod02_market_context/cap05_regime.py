"""CAP-05: Regime Classification (MOD-02).

Minimal real rule: classify regime from the sign of the slope of a short
moving average over the most recent window.
"""

WINDOW = 20


def classify_regime(bars: list[dict]) -> str:
    closes = [b["close"] for b in bars]
    if len(closes) < WINDOW + 1:
        return "NEUTRAL"

    recent = closes[-WINDOW:]
    sma_now = sum(recent) / len(recent)
    prior = closes[-(WINDOW + 1):-1]
    sma_prior = sum(prior) / len(prior)

    if sma_now > sma_prior:
        return "BULLISH"
    if sma_now < sma_prior:
        return "BEARISH"
    return "NEUTRAL"

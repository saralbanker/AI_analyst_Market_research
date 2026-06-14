"""CAP-07: Technical Signal Generation (primary layer, MOD-03).

Minimal real signal: SMA(short) vs SMA(long) crossover. Direction and
strength (normalized separation) are technically pure (VAL05-01) -- no
sentiment input.
"""

SHORT_WINDOW = 10
LONG_WINDOW = 30


def generate_signal(bars: list[dict]) -> dict:
    closes = [b["close"] for b in bars]
    if len(closes) < LONG_WINDOW:
        return {"direction": "NONE", "strength": 0.0}

    sma_short = sum(closes[-SHORT_WINDOW:]) / SHORT_WINDOW
    sma_long = sum(closes[-LONG_WINDOW:]) / LONG_WINDOW

    if sma_long == 0:
        return {"direction": "NONE", "strength": 0.0}

    separation = (sma_short - sma_long) / sma_long
    direction = "LONG" if separation > 0 else ("SHORT" if separation < 0 else "NONE")

    return {"direction": direction, "strength": abs(separation), "sma_short": sma_short, "sma_long": sma_long}

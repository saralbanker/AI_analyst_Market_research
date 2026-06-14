"""Fixed OHLCV fixture for the Phase 2 vertical slice (IMP-001 Section 7.1).

A single synthetic symbol with a monotonic uptrend, so that:
  - both stub vendor adapters return identical data (CAP-02 passes), and
  - a real SMA-crossover signal (CAP-07) and walk-forward check (CAP-10)
    have a deterministic, non-trivial outcome.
"""

SYMBOL = "RELIANCE"

_NUM_DAYS = 60
_START_PRICE = 2000.0
_DAILY_STEP = 5.0


def _generate_bars() -> list[dict]:
    bars = []
    for i in range(_NUM_DAYS):
        close = _START_PRICE + i * _DAILY_STEP
        bars.append({
            "day": i,
            "open": close - 1.0,
            "high": close + 2.0,
            "low": close - 2.0,
            "close": close,
            "volume": 1_000_000 + i * 1000,
        })
    return bars


def vendor_a_bars() -> list[dict]:
    return _generate_bars()


def vendor_b_bars() -> list[dict]:
    # Identical to vendor A -- deliberately matching so CAP-02 passes.
    return _generate_bars()

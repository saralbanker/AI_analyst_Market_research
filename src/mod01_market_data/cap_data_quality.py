"""CAP-01 supporting check: Data Quality Validation (MOD-01, EXT-001 WP07).

Runs before CAP-02 cross-verification. Rejects a vendor bar series outright
if it contains structurally invalid data, so cross-verification never
compares (and ingestion never persists) bad candles. This adds a validation
step within MOD-01's existing CAP-01 ingestion responsibility -- it does not
introduce a new capability, module, or persisted table.
"""

import datetime

TOLERANCE = 1e-9


class DataQualityFailure(Exception):
    pass


def validate_bars(bars: list[dict], source: str) -> None:
    """Raise DataQualityFailure if `bars` (one vendor's series) is invalid.

    Checks, per bar: non-negative/non-zero prices, high >= low, open/close
    within [low, high], non-negative volume, and (if present) a `timestamp`
    that is not in the future. Across the series: no duplicate `day` values
    and no gaps in the `day` sequence (missing candles).
    """
    if not bars:
        raise DataQualityFailure(f"{source}: empty bar series")

    seen_days: set[int] = set()
    now = datetime.datetime.utcnow()

    for bar in bars:
        day = bar.get("day")

        if day in seen_days:
            raise DataQualityFailure(f"{source}: duplicate candle for day {day}")
        seen_days.add(day)

        for field in ("open", "high", "low", "close"):
            value = bar.get(field)
            if value is None or value <= 0:
                raise DataQualityFailure(f"{source}: invalid price {field}={value} on day {day}")

        if bar["high"] < bar["low"] - TOLERANCE:
            raise DataQualityFailure(f"{source}: high < low on day {day} ({bar['high']} < {bar['low']})")

        if not (bar["low"] - TOLERANCE <= bar["open"] <= bar["high"] + TOLERANCE):
            raise DataQualityFailure(f"{source}: open price outside [low, high] on day {day}")

        if not (bar["low"] - TOLERANCE <= bar["close"] <= bar["high"] + TOLERANCE):
            raise DataQualityFailure(f"{source}: close price outside [low, high] on day {day}")

        volume = bar.get("volume")
        if volume is None or volume < 0:
            raise DataQualityFailure(f"{source}: invalid volume {volume} on day {day}")

        timestamp = bar.get("timestamp")
        if timestamp is not None:
            ts = datetime.datetime.fromisoformat(timestamp)
            if ts > now:
                raise DataQualityFailure(f"{source}: future timestamp {timestamp} on day {day}")

    expected_days = set(range(min(seen_days), max(seen_days) + 1))
    missing = expected_days - seen_days
    if missing:
        raise DataQualityFailure(f"{source}: missing candles for day(s) {sorted(missing)}")

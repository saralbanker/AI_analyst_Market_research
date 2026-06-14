"""CAP-02: Data Cross-Verification (MOD-01).

Constitutional blocking gate -- blocks all downstream signal logic if the
configured data sources disagree beyond tolerance (ADR-006 Required
Ordering 2 / DEP-06).
"""

TOLERANCE = 0.01  # fraction of price


class CrossVerificationFailure(Exception):
    pass


def cross_verify(bars_a: list[dict], bars_b: list[dict]) -> list[dict]:
    """Return the verified bar series, or raise CrossVerificationFailure."""
    if len(bars_a) != len(bars_b):
        raise CrossVerificationFailure("source bar counts differ")

    for a, b in zip(bars_a, bars_b):
        if a["close"] == 0:
            continue
        diff = abs(a["close"] - b["close"]) / abs(a["close"])
        if diff > TOLERANCE:
            raise CrossVerificationFailure(
                f"close price mismatch on day {a['day']}: {a['close']} vs {b['close']} (diff={diff:.4f})"
            )

    return bars_a

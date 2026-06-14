"""CAP-10: Walk-Forward Signal Validation (MOD-04).

Constitutional blocking gate -- a signal that fails this check must not
reach CAP-12 confidence scoring (k-fold validation is constitutionally
prohibited; only walk-forward splits are used).

Minimal real check: 2 walk-forward folds. For each fold, generate the
technical signal on the training slice and confirm its direction agrees
with the sign of the forward return on the held-out slice.
"""

from src.mod03_evidence.cap07_technical import generate_signal, LONG_WINDOW

NUM_FOLDS = 2
FORWARD_HORIZON = 5


def _forward_return(closes: list[float], start: int, horizon: int) -> float:
    end = min(start + horizon, len(closes) - 1)
    if closes[start] == 0 or end <= start:
        return 0.0
    return (closes[end] - closes[start]) / closes[start]


def walk_forward_validate(bars: list[dict]) -> dict:
    closes = [b["close"] for b in bars]
    n = len(closes)

    min_required = LONG_WINDOW + FORWARD_HORIZON + NUM_FOLDS
    if n < min_required:
        return {"passed": False, "folds": [], "reason": "insufficient history"}

    fold_size = (n - LONG_WINDOW - FORWARD_HORIZON) // NUM_FOLDS
    folds = []

    for fold_idx in range(NUM_FOLDS):
        train_end = LONG_WINDOW + (fold_idx + 1) * fold_size
        train_end = min(train_end, n - FORWARD_HORIZON)

        train_slice = bars[:train_end]
        signal = generate_signal(train_slice)
        fwd_return = _forward_return(closes, train_end - 1, FORWARD_HORIZON)

        if signal["direction"] == "LONG":
            agreed = fwd_return > 0
        elif signal["direction"] == "SHORT":
            agreed = fwd_return < 0
        else:
            agreed = False

        folds.append({
            "fold": fold_idx,
            "train_end": train_end,
            "direction": signal["direction"],
            "forward_return": fwd_return,
            "agreed": agreed,
        })

    passed = all(f["agreed"] for f in folds)
    return {"passed": passed, "folds": folds, "reason": None if passed else "fold disagreement"}

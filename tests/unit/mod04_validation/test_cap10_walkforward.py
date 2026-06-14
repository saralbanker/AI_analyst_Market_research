from src.mod01_market_data.fixtures import vendor_a_bars
from src.mod04_validation.cap10_walkforward import walk_forward_validate


def test_monotonic_uptrend_fixture_passes_walk_forward():
    bars = vendor_a_bars()
    result = walk_forward_validate(bars)

    assert result["passed"] is True
    assert result["reason"] is None
    assert len(result["folds"]) == 2
    for fold in result["folds"]:
        assert fold["direction"] == "LONG"
        assert fold["forward_return"] > 0
        assert fold["agreed"] is True


def test_insufficient_history_fails_with_reason():
    bars = vendor_a_bars()[:10]
    result = walk_forward_validate(bars)

    assert result["passed"] is False
    assert result["folds"] == []
    assert result["reason"] == "insufficient history"


def test_downtrend_disagrees_with_long_signal():
    # Reverse the uptrend fixture into a downtrend -- SMA crossover signals
    # SHORT, but forward returns are negative, so a SHORT signal should agree
    # while a flipped check (expecting LONG) would not.
    bars = vendor_a_bars()
    reversed_bars = [
        {**b, "close": bars[0]["close"] + (bars[-1]["close"] - b["close"])}
        for b in bars
    ]
    result = walk_forward_validate(reversed_bars)

    assert result["passed"] is True
    for fold in result["folds"]:
        assert fold["direction"] == "SHORT"
        assert fold["forward_return"] < 0

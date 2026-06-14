from src.mod05_recommendation.cap13_ev import compute_ev


def test_ev_is_product_of_mean_return_and_confidence():
    assert compute_ev(mean_return=0.02, confidence=0.5) == 0.01


def test_ev_zero_confidence_gives_zero_ev():
    assert compute_ev(mean_return=0.05, confidence=0.0) == 0.0


def test_ev_rounds_to_six_decimals():
    assert compute_ev(mean_return=1 / 3, confidence=1 / 3) == round((1 / 3) * (1 / 3), 6)


def test_ev_negative_mean_return_gives_negative_ev():
    assert compute_ev(mean_return=-0.02, confidence=0.5) == -0.01

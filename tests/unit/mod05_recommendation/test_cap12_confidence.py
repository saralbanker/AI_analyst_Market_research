from src.mod05_recommendation.cap12_confidence import compute_confidence


def test_zero_strength_and_tstat_gives_zero_confidence():
    assert compute_confidence(strength=0.0, t_stat=0.0) == 0.0


def test_max_strength_and_tstat_gives_full_confidence():
    # strength * 20 >= 1.0 and t_stat / 3 >= 1.0 both saturate at 1.0
    assert compute_confidence(strength=1.0, t_stat=3.0) == 1.0


def test_infinite_tstat_saturates_tstat_component():
    assert compute_confidence(strength=0.0, t_stat=float("inf")) == 0.5


def test_negative_tstat_floors_at_zero():
    assert compute_confidence(strength=0.0, t_stat=-5.0) == 0.0


def test_partial_inputs_blend_evenly():
    # strength=0.025 -> normalized 0.5; t_stat=1.5 -> normalized 0.5
    assert compute_confidence(strength=0.025, t_stat=1.5) == 0.5

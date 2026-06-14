"""CAP-04 (Survivorship-Bias Correction) and CAP-14 (Corporate Action
Adjustment) -- pass-through identity transforms for the Phase 2 fixture
(no delistings or corporate actions in the fixed dataset).
"""


def apply_survivorship_correction(bars: list[dict]) -> list[dict]:
    return bars


def apply_corporate_action_adjustment(bars: list[dict]) -> list[dict]:
    return bars

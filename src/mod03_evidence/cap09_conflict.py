"""CAP-09: Conflict Detection (MOD-03).

VAL05-04/FORB-08/DEP-09: the result is annotation-only -- never a numeric
modifier to CAP-12/13/15/16. Conflict is flagged when the technical
direction and sentiment direction disagree (no sentiment in Phase 2 ->
never conflicts).
"""


def detect_conflict(technical_signal: dict, sentiment: list[dict]) -> bool:
    if not sentiment:
        return False

    technical_direction = technical_signal.get("direction")
    for item in sentiment:
        if item.get("direction") and item["direction"] != technical_direction:
            return True
    return False

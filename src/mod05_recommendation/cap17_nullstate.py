"""CAP-17: Null-State Declaration (MOD-05).

A null-state is declared when there are no validated opportunities to
present, or when Governance Halt (State 1) is active (GOV-01: MOD-05
issuance is gated while other modules continue running).
"""


def should_declare_null_state(validated_signals: list, halts: dict) -> tuple[bool, str | None]:
    governance_halt = halts.get(1, {})
    if governance_halt.get("status") == "active":
        return True, "GOVERNANCE_HALT_ACTIVE"

    if not validated_signals:
        return True, "NO_VALIDATED_OPPORTUNITIES"

    return False, None

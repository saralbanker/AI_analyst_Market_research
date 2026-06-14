"""CAP-21/CAP-22: Attribution (MOD-08).

Read-only/observation-only (DEP-02/OWN-03/INV-08). Reconstruction sources
are MOD-07 (post-gate decisions) and MOD-01/MOD-02 outcomes (ADR-003B);
never MOD-10.

Phase 3 minimal: System Alpha is the EV the system attached to a
recommendation; Human Alpha is the delta introduced by a human override
(reject) -- realized outcomes (time-delayed MOD-01/02 data) are out of
scope for the single-cycle vertical slice and default to 0.0 here.
"""


def compute_attribution(opportunity: dict, decision: str) -> dict:
    system_alpha = opportunity["ev"]
    human_alpha = -system_alpha if decision == "reject" else 0.0
    return {
        "direction": opportunity["direction"],
        "confidence": opportunity["confidence"],
        "ev": opportunity["ev"],
        "allocation_amount": opportunity["allocation_amount"],
        "decision": decision,
        "system_alpha": system_alpha,
        "human_alpha": human_alpha,
    }

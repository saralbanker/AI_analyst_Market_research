"""MOD-04: Statistical Validation -- orchestrator (CAP-10 gate, CAP-11).

A signal failing CAP-10 is filtered out of `validated_signals`; MOD-05
structurally cannot receive un-validated signals because `validated_signals`
is the only signal-shaped argument it accepts (IMP-001 Section 5.3).
"""

from dataclasses import dataclass

from src.mod10_audit import audit
from src.mod01_market_data import VerifiedMarketData
from src.mod03_evidence import EvidencePackage
from src.mod04_validation.cap10_walkforward import walk_forward_validate
from src.mod04_validation.cap11_significance import compute_t_stat


@dataclass
class ValidatedSignal:
    symbol: str
    direction: str
    strength: float
    t_stat: float
    sample_size: int
    mean_return: float


def run(cycle_id: str, verified: VerifiedMarketData, evidence: EvidencePackage) -> list[ValidatedSignal]:
    technical_signal = evidence.technical_signal
    direction = technical_signal.get("direction", "NONE")

    walk_forward = walk_forward_validate(verified.bars)
    audit.record("MOD-04", "CAP-10", cycle_id, "walk_forward_evaluated",
                  {"symbol": verified.symbol, **{k: v for k, v in walk_forward.items() if k != "folds"},
                   "folds": walk_forward["folds"]})

    if not walk_forward["passed"] or direction == "NONE":
        audit.record("MOD-04", "CAP-10", cycle_id, "signal_rejected",
                      {"symbol": verified.symbol, "reason": walk_forward["reason"] or "no direction"})
        return []

    significance = compute_t_stat(verified.bars, direction)
    audit.record("MOD-04", "CAP-11", cycle_id, "significance_evaluated",
                  {"symbol": verified.symbol, **significance})

    validated = ValidatedSignal(
        symbol=verified.symbol,
        direction=direction,
        strength=technical_signal.get("strength", 0.0),
        t_stat=significance["t_stat"],
        sample_size=significance["sample_size"],
        mean_return=significance["mean_return"],
    )

    audit.record("MOD-04", "CAP-11", cycle_id, "signal_validated",
                  {"symbol": verified.symbol, "direction": direction})

    return [validated]

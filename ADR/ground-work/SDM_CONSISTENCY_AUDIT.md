# SDM_CONSISTENCY_AUDIT

## Contradictions
- None detected. By applying the normalization rules and strictly isolating decision logic from architecture/infrastructure (e.g., ignoring FastMCP, DuckDB, SQLite), the resulting SDM flows consistently from objective selection to risk governance without operational contradictions.

## Circular Dependencies
- None detected. The flow forms a coherent Directed Acyclic Graph (DAG):
  `Objective Selection` -> `Universe Selection` -> `Market Regime` -> `Signal Discovery` -> `Signal Validation` -> `Confidence Assessment & Expected Value` -> `Opportunity Ranking` -> `Capital Allocation & Position Management` -> `Human Approval` -> `Signal Lifecycle & Exit Decision`.
  - Risk Governance acts as a continuous overarching enforcement domain rather than a circular dependency loop.

## Missing Decisions
- **Domain-12 Attribution**: Generated as a skeletal placeholder with `[LOW CONFIDENCE]` markers due to a total lack of decision heuristics or mathematical frameworks in the inputs.
- **Domain-14 Research Intake**: Generated as a skeletal placeholder with `[LOW CONFIDENCE]` markers due to a total lack of input evidence regarding unstructured document processing logic.
- **Signal Lifecycle Mathematical Limits**: Exact mathematical indicators to prove an equity has exited an ergodic state and entered an unpredictable tail-risk regime are missing `[VALIDATION_REQUIRED]`.
- **Confidence/Kelly Fractions**: Exact mathematical formulas converting NLP/sentiment scores into confidence weights or Kelly fractions are missing `[VALIDATION_REQUIRED]`.
- **Value-at-Risk (VaR)**: Mathematical framework for VaR modeling under non-ergodic market conditions is absent `[VALIDATION_REQUIRED]`.
- **Aggregate Margin Exposure**: Cross-broker/multi-account margin tracking and execution scale-down quantile limits are missing `[VALIDATION_REQUIRED]`.
- **Slippage Quantification**: Exact mechanical execution barrier math and slippage tolerance thresholds are missing `[VALIDATION_REQUIRED]`.

## Unsupported Decisions
- None detected. Every extracted decision rule across the remaining domains is strictly traceable to `OWNER_DECISION_PROFILE_V1` or the normalized `SDM_INPUT_REGISTRY_V1`. The assumption of "walk-forward accurately mimicking future regimes" was flagged in the input registry and is heavily dependent on the unresolved non-ergodic market mathematics.

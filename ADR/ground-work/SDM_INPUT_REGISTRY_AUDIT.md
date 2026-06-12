# SDM_INPUT_REGISTRY_AUDIT

## Missing Evidence
- Mathematical framework for calculating daily Value-at-Risk (VaR) under non-ergodic market conditions.
- Explicit mathematical formulas for converting AI sentiment scores (FinBERT) into deterministic position sizing / Kelly fractions.
- Empirical latency and uptime logs for Upstox and Angel One APIs during extreme market events.
- Empirical benchmarks proving DuckDB/SQLite concurrency viability at the 50GB Parquet scale.
- Explicit mapping or proof of US-trained NLP sentiment models applying accurately to Indian corporate disclosures.
- Slippage threshold quantification parameters are undefined.
- Specific execution scale-down quantile limits.
- No evidence, definitions, or references found for Domain-12 Attribution.
- No evidence, definitions, or references found for Domain-14 Research Intake.
- BAFI reports contain zero mention of Capital Allocation, Human Approval, Position Management, or Exit Decision.

## Contradictory Evidence
- "Fully AI (ML/Deep Learning) Systems... generate signals or trades directly" vs. "Execution must remain a strictly deterministic, human-gated process." The latter is the dominant accepted constraint within the corpus, making autonomous execution an actively rejected anti-pattern.
- General assumption that social media sentiment is useful vs. empirical findings that it adds almost zero predictive power.
- Litestream millisecond recovery guarantees contradict documented network dropouts crash risks.
- Upstox split-adjusted data completeness claims contradict documented de-merger adjustment complexities.

## Domain Coverage Gaps
- Total coverage gap: Domain-12 Attribution and Domain-14 Research Intake are completely absent from the Research Corpus, ACD Corpus, ADR Corpus, ADR Gap Closure, and OWNER_DECISION_PROFILE_V1.
- Signal Lifecycle (Domain-13) and Exit Decision (Domain-11) lack detailed mechanical exit criteria beyond time-based horizons and generic slippage rules.
- Signal Discovery (Domain-03) lacks a defined mechanism for integrating AI-generated sentiment scores with deterministic execution logic.
- Cross-platform risk management strategies for multi-broker aggregate margin tracking and synthetic leverage opacity are unquantified.
- Concrete methods for adjusting Options Greeks during dynamic hedging feedback loops.
- The precise cloud deployment topology required when transitioning from local execution to SaaS infrastructure (Stage 2 to 4 is unresearched).

## Source Traceability Issues
- The assertion that "Walk-forward out-of-sample data accurately mimics future market regimes" drives multiple foundational decisions but is explicitly identified in the corpus as an unvalidated hidden assumption.
- Yahoo Finance Adjusted Close is cited as an input source but is simultaneously flagged as having "weak support" due to occasional dividend mis-adjustments.
- "decision-log.xml" and "risk-registry.xml" referenced in the architecture bootstrap specification do not exist in the repository.
- RLS policy audits exist only in markdown prose rather than executable SQL.
- Migration history has numbered gaps (e.g., 017–020 are absent) and is considered unreliable for schema authority.
- Telemetry and Runtime Census data are persistently absent from Phase 1 through Phase 3 evidence.

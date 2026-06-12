# SDM_INPUT_REGISTRY_V1

## Domain-01 Universe Selection
Purpose: Define and filter the set of eligible tradable assets while preventing survivorship bias and ensuring data integrity before signal generation.
Inputs: Target Market constraints, Capital Stage parameters, Historical OHLCV Data, Delisted stocks data, News and technical signal streams.
Candidate Rules:
- Target market is strictly restricted to Indian Equities.
- The system should avoid unnecessarily filtering opportunities (missing a genuine winner is considered worse than rejecting too many trades).
- Delisted stocks must be included in historical datasets to avoid survivorship bias.
- OHLCV metrics must be cross-verified across at least two independent providers before running signal logic.
- Split-adjusted data is mandatory; unadjusted splits corrupt technical indicators and backtest validity.
- Zerodha historical API data is structurally incomplete and cannot be used as the sole backtesting source.
- Probability of trades must be prioritized over theoretical return opportunities.
- Technical evidence strictly outweighs news signals; news influences confidence but does not override strong technicals.
Candidate Outputs: Filtered universe of eligible Indian Equities, Opportunity ranking.
Dependencies: Data Ingestion & Integrity, Storage & Infrastructure.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, ADR-004, ADR-005, ADR-011, ADR-013.
Corpus Confidence: High.
Open Questions:
- What is the specific price or liquidity filter threshold required given the ₹5k Initial Capital constraint?
- How are complex de-merger split adjustments properly handled if primary provider data is imperfect?

## Domain-02 Market Regime Classification
Purpose: Classify the current market environment and detect structural shifts to prevent model concept drift and inappropriate strategy execution.
Inputs: Historical OHLCV Data, Walk-forward Out-of-Sample (OOS) data, Model uncertainty quantification metrics.
Candidate Rules:
- Walk-forward cross-validation must be utilized over randomized k-fold CV to prevent chronological data leaks.
- ML models must feature concept drift controls and regime-change re-anchoring to prevent anchoring to peak historical data during market downturns.
- Moving averages are recognized as lagging indicators that fail systematically in sideways/choppy markets.
- Sector rotation strategies should be aligned with a broad market trend filter.
- System must account for market non-ergodicity, where historical correlation matrices break down during macro shocks.
- Denoising autoencoders must not mask real market anomalies from risk systems.
Candidate Outputs: Market regime classification (e.g., Ergodic vs. Non-Ergodic), Regime shift alerts, Trend/Choppy market indicators.
Dependencies: Data Governance.
Evidence Sources: ADR-007, ADR-046, ADR-058, 01_candidate_decision_inventory.md, 03_failure_mode_matrix.md.
Corpus Confidence: Medium.
Open Questions:
- What strict mathematical indicators prove an equity has exited an ergodic state and entered an unpredictable tail-risk regime?
- Does walk-forward OOS data accurately mimic future market regimes?

## Domain-03 Signal Discovery
Purpose: Identify opportunities and generate evidence-based swing trading recommendations.
Inputs: OHLCV metrics, exchange filings, corporate announcements, major financial publications.
Candidate Rules:
- Prioritization of technical evidence over news evidence.
- Utilization of earnings surprises and insider buying as valid indicators.
- Lower weighting or exclusion of analyst rating changes and social media sentiment.
- Alignment of sector rotation strategies with broad market trend filters.
- Recognition of moving averages as lagging indicators that fail in sideways markets.
- Validation of price breakouts using volume spikes.
- Recognition of specific chart patterns possessing statistical edges independent of volume.
- Isolation of AI models exclusively to the semantic/cognitive domain.
- Preference for highest probability opportunities over highest theoretical return opportunities.
- Requirement for news to influence confidence without automatically overriding technical evidence.
Candidate Outputs: Opportunity ranking, allocation suggestions, confidence scoring, supporting evidence.
Dependencies: Data Ingestion & Integrity, Storage & Infrastructure.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 01_candidate_decision_inventory.md.
Corpus Confidence: Medium.
Open Questions:
- How are AI-generated sentiment scores mathematically weighted into deterministic execution logic without violating the deterministic barrier?
- Do NLP sentiment models trained on US markets effectively map to Indian corporate disclosures?

## Domain-04 Signal Validation
Purpose: Verify statistical edge, prevent overfitting, and ensure signal integrity before deployment.
Inputs: Initial signal logic outputs, multi-source validation pipelines, walk-forward out-of-sample data.
Candidate Rules:
- Cross-verification of metrics between independent data providers before running signal logic.
- Utilization of walk-forward cross-validation to prevent chronological data leaks.
- Requirement for statistical edge verification using deflated return metrics or statistical significance tests.
- Tracking of concept drift between training and live data using stability indexes.
- Requirement for high branch coverage in backtesting modules.
- Verification of outlier detectors through synthetic anomaly injection.
- Prohibition of denoising autoencoders masking structural market anomalies from risk systems.
Candidate Outputs: Statistical validation scores, concept drift alerts, validation pipeline approvals.
Dependencies: Domain-03 Signal Discovery, Data Ingestion & Integrity.
Evidence Sources: 01_candidate_decision_inventory.md, 05_adr_candidate_corpus.md, 06e_failure_mode_audit.md.
Corpus Confidence: High.
Open Questions: None explicitly found in corpus.

## Domain-05 Confidence Assessment
Purpose: Quantify the reliability, certainty, and statistical robustness of an opportunity or signal to guide conviction weighting without dictating automated execution.
Inputs: Technical evidence, news sources (exchange filings, corporate announcements, major publications), statistical backtest metrics, walk-forward validation results.
Candidate Rules:
- News influence on confidence evaluated against technical evidence weight.
- Conflicts between technicals and news require case-by-case evaluation.
- Conviction weighting influences allocation scale.
- Statistical significance tests (e.g., t-stat, Deflated Sharpe) act as deployment gates.
- Standard confidence intervals are considered insufficient for deployment validation.
- Technical evidence strictly outweighs news.
Candidate Outputs: Confidence rating, conviction weighting suggestions, supporting evidence summaries.
Dependencies: Technical signals, news signals, backtesting validation pipeline.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 02_decision_audit_report.md.
Corpus Confidence: High.
Open Questions:
- Exact mathematical formulas converting NLP/FinBERT scores into localized position sizing (Kelly fractions).

## Domain-06 Expected Value Assessment
Purpose: Evaluate opportunities based on probability-adjusted returns bounded by strict risk and capital preservation constraints rather than speculative potential.
Inputs: Estimated returns, historical probabilities, technical signal strengths, portfolio drawdown tolerance limits.
Candidate Rules:
- Probability prioritization over speculative return.
- Highest probability opportunities preferred over highest theoretical return opportunities.
- Capital preservation constraints govern acceptable downside risk.
- Maximum portfolio drawdown tolerance limits strictly enforced.
- Cash holding validity during lack of acceptable opportunities.
- Walk-Forward Cross-Validation method mandatory for assessing probabilities (K-Fold prohibited).
- Survivorship bias adjustment through required delisted stock inclusion.
Candidate Outputs: Probability-adjusted return estimates, downside drawdown risk estimates.
Dependencies: Historical split-adjusted data providers, Walk-forward CV results.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 02_decision_audit_report.md.
Corpus Confidence: High.
Open Questions:
- Mathematical framework for VaR modeling under non-ergodic market conditions.
- Missing research on multi-broker aggregate margin exposure management.

## Domain-07 Opportunity Ranking
Purpose: Sort, prioritize, and select the top viable opportunities for final advisory recommendation and allocation suggestions.
Inputs: Expected Value Assessment, Confidence Assessment, available capital, target position limits.
Candidate Rules:
- Higher quality trade preference over increased trade volume.
- Avoidance of unnecessary opportunity filtering to capture genuine winners.
- Target position counts limit the maximum number of recommendations.
- Conviction weighted allocation (confidence-based, then best-idea weighted) preferred over equal-weight allocation.
- Explicit null-state declaration when no actionable opportunities meet requirements.
- Avoidance of forced capital deployment under suboptimal conditions.
Candidate Outputs: Opportunity Ranking list, Target Allocation Suggestions, Exit Suggestions.
Dependencies: Domain-05 Confidence Assessment, Domain-06 Expected Value Assessment.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md.
Corpus Confidence: High.
Open Questions:
- Slippage threshold quantification is completely unquantified.

## Domain-08 Capital Allocation
Purpose: To determine how capital is distributed across selected trading opportunities and when to hold cash.
Inputs: Opportunity confidence scores, conviction rankings, available capital, market volatility, liquidity metrics.
Candidate Rules:
- Cash is a valid position; holding cash is required if no acceptable opportunities exist.
- Capital deployment must never be forced.
- Allocations must be conviction-weighted (Confidence Weighted or Best-Idea Weighted).
- Equal-weight allocation is explicitly not preferred.
- Execution sizing must auto-scale against portfolio illiquidity; static initial margins are disallowed.
- Execution scale-down is required when quantile uncertainty bands widen.
Candidate Outputs: Target capital allocation per opportunity, cash reserve suggestion.
Dependencies: Domain-10 Position Management.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 01_candidate_decision_inventory.md, ADR_CORPUS_V2.md.
Corpus Confidence: High.
Open Questions:
- Mathematical framework for converting sentiment scores to Kelly fractions is unresolved.
- Multi-broker aggregate margin exposure management is unresearched.

## Domain-09 Human Approval
Purpose: To ensure deterministic control and mandatory human authorization over AI-generated trading recommendations before execution.
Inputs: Trade recommendations, supporting evidence, confidence metrics, risk summaries, exit suggestions.
Candidate Rules:
- Human approval is mandatory before any trade action.
- System recommendations are strictly advisory, not executable.
- The owner may override system recommendations and retains final authority.
- Disagreements between owner and system are evaluated case-by-case.
- Execution must remain strictly deterministic and human-gated.
- Direct LLM trade execution is strictly prohibited.
- FastMCP execution boundaries must be physically enforced against prompt injection.
- Mandatory multi-signature human approval is required for algorithmic pricing limit overrides.
Candidate Outputs: Approval/rejection decisions, approved parameter overrides.
Dependencies: None.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 01_candidate_decision_inventory.md, ADR_CORPUS_V2.md.
Corpus Confidence: High.
Open Questions: None explicitly found in corpus.

## Domain-10 Position Management
Purpose: To control portfolio-level risk limits, manage total position count, and prevent systemic drawdowns across active trades.
Inputs: Current active positions, aggregated portfolio drawdown, multi-broker concentration exposure, liquidity depth.
Candidate Rules:
- Target position count ranges must be observed.
- The system may recommend fewer positions or a single opportunity if insufficient opportunities exist.
- Maximum portfolio drawdown tolerances must be strictly observed.
- Capital preservation is mandatory; avoid recommendations that materially threaten portfolio survivability.
- Multi-broker concentration risk and synthetic leverage opacity must be controlled to prevent margin breaches.
- Hard position limits must be enforced via API disconnection rather than passive alerts.
Candidate Outputs: Position count directives, drawdown halt signals, API disconnection triggers.
Dependencies: Domain-08 Capital Allocation.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 01_candidate_decision_inventory.md, ADR_CORPUS_V2.md.
Corpus Confidence: High.
Open Questions:
- Mathematical framework for VaR modeling under non-ergodic market conditions is absent.

## Domain-11 Exit Decision
Purpose: To provide criteria and timeline recommendations for closing active trading positions.
Inputs: Expected time horizon, technical/news evidence continuity, slippage metrics, transaction costs.
Candidate Rules:
- Primary and secondary time horizons govern base expected trade durations.
- Trades extending beyond the expected duration may remain valid if evidence continues to support them.
- Slippage and transaction cost controls must be enforced during live execution exits.
Candidate Outputs: Exit suggestions, exit signals.
Dependencies: Domain-10 Position Management.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, ADR_CORPUS_V2.md.
Corpus Confidence: Medium.
Open Questions:
- Slippage threshold quantification is undefined.

## Domain-12 Attribution
Purpose: No evidence found in corpus.
Inputs: No evidence found in corpus.
Candidate Rules: No evidence found in corpus.
Candidate Outputs: No evidence found in corpus.
Dependencies: No evidence found in corpus.
Evidence Sources: No evidence found in corpus.
Corpus Confidence: Low.
Open Questions: No evidence found in corpus.

## Domain-13 Signal Lifecycle
Purpose: Manage the duration, holding period, and exit conditions of generated signals.
Inputs: Ongoing technical evidence, regime change indicators, trailing volume, macro shock flags.
Candidate Rules:
- Extension of trade validity beyond primary expected durations if supporting evidence persists.
- Alignment of signal horizons with designated short-term and medium-term swing durations.
- Utilization of hard circuit breakers to halt trend-following dynamic hedging cycles.
- Prevention of model anchoring to peak historical transaction data during regime shifts.
- Application of volume-based execution limits relative to trailing volume.
- Automatic reduction of execution size triggered by widening quantile uncertainty bands.
- Implementation of hard kill-switches during extreme macro shocks and non-ergodic market breakdowns.
- Enforcement of position limits via hard API disconnections rather than passive alerts.
Candidate Outputs: Exit suggestions, risk summaries, position limit halts, bid size reduction triggers.
Dependencies: Domain-03 Signal Discovery, Execution & Risk Management.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, 06e_failure_mode_audit.md.
Corpus Confidence: High.
Open Questions:
- What strict mathematical indicators prove an equity has exited an ergodic state and entered an unpredictable tail-risk regime?

## Domain-14 Research Intake
Purpose: No evidence found in corpus.
Inputs: No evidence found in corpus.
Candidate Rules: No evidence found in corpus.
Candidate Outputs: No evidence found in corpus.
Dependencies: No evidence found in corpus.
Evidence Sources: No evidence found in corpus.
Corpus Confidence: Low.
Open Questions: No evidence found in corpus.

## Domain-15 Risk Governance
Purpose: Enforce strict deterministic risk controls, safeguard capital preservation, prevent systemic failure loops, and ensure mandatory human oversight.
Inputs: Market Regime Classification, AI Sentiment Uncertainty Quantile Bands, System Telemetry (API Latency), Broker Margin Limits.
Candidate Rules:
- Capital preservation is mandatory; maximum portfolio drawdown tolerance is explicitly capped (e.g., 5%).
- Cash is recognized as a valid position; capital deployment must never be forced.
- Human approval is mandatory before any trade action; the system is advisory, not an autonomous execution bot.
- Execution logic must remain strictly deterministic; AI must never control deterministic execution or order routing.
- Position limits must be enforced via hard API disconnections rather than passive dashboard alerts.
- Circuit breakers must detect and halt trend-following dynamic hedging cycles.
- Execution algorithms must instantly scale down or halt orders when AI/ML quantile uncertainty bands widen.
- Execution algorithms must instantly disconnect if consolidated tape latency exceeds predefined microsecond thresholds.
- Volume spikes must be monitored for informational cascades to halt non-transparent selling.
- Bespoke scenario limits must carry hard caps to prevent risk manager inflation.
- Variation margin release must be restricted during periods of elevated volatility or market stress.
- Total Return Swap (TRS) margins must be audited to match standard prime brokerage initial margin limits.
Candidate Outputs: Hard API disconnection commands (Kill-Switches), Dynamic margin scaling adjustments, Human approval gates, Critical alert runbooks.
Dependencies: Market Regime Classification (Domain-02), AI Output/Sentiment Analysis.
Evidence Sources: OWNER_DECISION_PROFILE_V1.md, ADR-049, ADR-050, ADR-051, ADR-054, ADR-057, ADR-060, ADR-065, 06d_governance_audit.md.
Corpus Confidence: High.
Open Questions:
- What is the mathematical framework for calculating daily Value-at-Risk under non-ergodic conditions?
- How does the algorithmic system specifically manage aggregate margin exposure across multiple Indian discount brokers simultaneously?
- What are the exact mathematical formulas converting semantic FinBERT scores into localized position sizing without violating deterministic execution boundaries?

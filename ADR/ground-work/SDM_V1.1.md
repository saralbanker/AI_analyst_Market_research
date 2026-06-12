# SDM_V1.1 - Strategy Decision Model

---
[SDM-01 Objective Selection]
Purpose: Define the primary strategic goal, risk tolerance, and operational boundaries of the AI Swing Trading Research Analyst to align with the owner's philosophy.
Inputs:
- Target Market (Indian Equities)
- Capital Stage (₹5k Initial Capital)
- Primary/Secondary Time Horizons (1-10 Days)
- Owner's Risk Philosophy
Decision Logic:
- Generate evidence-based swing trading recommendations that maximize probability-adjusted returns while maintaining strict risk discipline.
- If no acceptable opportunities exist, the system must decide to recommend holding cash.
- The system must never force capital deployment.
- Prioritize higher quality trades, but avoid unnecessarily filtering opportunities (missing a genuine winner is worse than rejecting too many trades).
- Prioritize highest probability opportunities over highest theoretical return opportunities.
- System must remain an advisory research analyst, not an autonomous execution bot.
- All trade recommendations require mandatory human approval.
Outputs:
- Strategic alignment directives
- Null-state declarations (cash recommendation) when opportunities are absent
Dependencies:
- None
Failure Conditions:
- System attempts autonomous execution
- System forces capital deployment when criteria are not met
Human Visibility Requirements:
- Reports must explicitly state "No actionable opportunities currently meet requirements" if null-state is reached
Audit Requirements:
- Validate that recommendations prioritize probability and capital preservation over speculative returns
---

---
[SDM-02 Universe Selection]
Purpose: Define and filter the set of eligible tradable assets while preventing survivorship bias and ensuring data integrity before signal generation.
Inputs: Target Market constraints, Capital Stage parameters (₹5k initial capital), Historical OHLCV Data, Delisted stocks data, News streams, Technical signal streams.
Decision Logic:
- Target market is strictly restricted to Indian Equities.
- Delisted stocks must be included in historical datasets to avoid survivorship bias.
- OHLCV metrics must be cross-verified across at least two independent sources before running signal logic.
- Split-adjusted data is mandatory; unadjusted splits are strictly rejected to protect backtest validity.
- Unnecessary filtering of opportunities must be avoided; missing a genuine winner is considered worse than rejecting too many trades.
- Probability of trades is prioritized over theoretical return opportunities.
- Technical evidence strictly outweighs news signals; news influences confidence but does not override strong technicals.
- [VALIDATION_REQUIRED] Specific price or liquidity filter threshold required given the ₹5k Initial Capital constraint.
- [VALIDATION_REQUIRED] Decision logic for handling complex de-merger split adjustments when primary data is imperfect.
Outputs: Filtered universe of eligible Indian Equities, Base opportunity ranking.
Dependencies: None.
Failure Conditions: Data cross-verification fails between sources; unadjusted split data detected; delisted stocks data missing from set.
Human Visibility Requirements: Display the count of eligible equities versus filtered equities; flag unverified or rejected data sources.
Audit Requirements: Log all assets excluded and the specific filtering rule triggered; maintain cross-verification match/mismatch records.
---

---
[SDM-03 Market Regime Classification]
Purpose: Classify the current market environment and detect structural shifts to prevent model concept drift and inappropriate strategy execution.
Inputs: Historical OHLCV Data, Walk-forward Out-of-Sample (OOS) data, Model uncertainty quantification metrics.
Decision Logic:
- Utilize walk-forward cross-validation over randomized k-fold CV to prevent chronological data leaks.
- Monitor for concept drift and re-anchor regime-change controls to prevent anchoring to peak historical data during market downturns.
- Moving averages are recognized as lagging indicators that fail systematically in sideways/choppy markets and must be contextually adjusted.
- Sector rotation strategies must align with a broad market trend filter.
- Decision thresholds must be adjusted to account for market non-ergodicity, where historical correlation matrices break down during macro shocks.
- Denoising filters must not mask real structural market anomalies from risk evaluation.
- [VALIDATION_REQUIRED] Strict mathematical indicators that prove an equity has exited an ergodic state and entered an unpredictable tail-risk regime.
- [VALIDATION_REQUIRED] Efficacy metric to ensure walk-forward OOS data accurately mimics future market regimes.
Outputs: Market regime classification (e.g., Ergodic vs. Non-Ergodic), Regime shift alerts, Trend/Choppy market indicators.
Dependencies: SDM-02 Universe Selection.
Failure Conditions: Walk-forward validation fails; model uncertainty metrics exceed acceptable bounds; non-ergodic market breakdown detected without a fallback state.
Human Visibility Requirements: Display current market regime classification and trend status; explicitly alert the user on detected regime shifts.
Audit Requirements: Log regime shift triggers, concept drift metrics over time, and walk-forward cross-validation bounds.
---

---
[SDM-04 Signal Discovery]
Purpose: Identify opportunities and generate evidence-based swing trading recommendations based on technical and supplementary evidence.
Inputs:
- OHLCV metrics
- Exchange filings and corporate announcements
- Major financial publications
Decision Logic:
- Prioritize technical evidence strictly over news evidence.
- Prefer highest probability opportunities over highest theoretical return opportunities.
- Influence confidence using news, but do not automatically override strong technical evidence.
- Evaluate conflicts between technicals and news on a case-by-case manual basis.
- Utilize earnings surprises and insider buying as valid supplementary indicators.
- Lower the weight of or exclude analyst rating changes and social media sentiment.
- Align sector rotation strategies with broad market trend filters.
- Validate price breakouts using volume spikes.
- Recognize specific chart patterns possessing statistical edges independent of volume.
- Discount or penalize moving averages as lagging indicators that systematically fail in sideways markets.
- Avoid unnecessarily filtering opportunities; missing a genuine winner is considered worse than rejecting too many trades, but maintain preference for higher quality trades.
- Isolate AI model evaluations exclusively to the semantic/cognitive domain.
Outputs:
- Opportunity ranking
- Allocation suggestions
- Confidence scoring
- Supporting evidence
Dependencies:
- [VALIDATION_REQUIRED] Mathematical weighting of AI-generated sentiment scores into deterministic execution logic.
- [VALIDATION_REQUIRED] Efficacy of NLP sentiment models (trained on US markets) mapped to Indian corporate disclosures.
Failure Conditions:
- No actionable opportunities meet requirements (System must explicitly output: "No actionable opportunities currently meet requirements").
Human Visibility Requirements:
- Present opportunity ranking, supporting evidence, and confidence scores for mandatory human approval.
Audit Requirements:
- Log reasons for overriding news with technical signals.
- Log sentiment and technical evidence weighting for continuous evaluation of signal quality.
---

---
[SDM-05 Signal Validation]
Purpose: Verify statistical edge, prevent overfitting, and ensure signal integrity before recommendation generation.
Inputs:
- Initial signal logic outputs
- Multi-source validation data
- Walk-forward out-of-sample data
Decision Logic:
- Cross-verify metrics between at least two independent data sources before running signal logic.
- Utilize walk-forward cross-validation to prevent chronological data leaks (k-fold cross-validation is strictly prohibited).
- Require comprehensive logic coverage in backtesting validation.
- Verify statistical edge using deflated return metrics or statistical significance tests.
- Track concept drift between training and live data using stability indexes.
- Verify outlier detectors through synthetic anomaly injection.
- Prohibit data smoothing techniques from masking structural market anomalies from risk evaluations.
Outputs:
- Statistical validation scores
- Concept drift alerts
- Validation approvals/rejections
Dependencies:
- SDM-04 Signal Discovery
Failure Conditions:
- Failure to confirm statistical edge via deflated return metrics.
- Detection of unadjusted stock splits or survivorship bias in validation data.
- Anomalies masked by data smoothing logic.
Human Visibility Requirements:
- Present statistical validation scores, concept drift alerts, and validation results.
Audit Requirements:
- Log cross-validation results, outlier detection verifications, and concept drift tracking metrics.
---

---
[SDM-06 Confidence Assessment]
Purpose: Quantify the reliability, certainty, and statistical robustness of an opportunity or signal to guide conviction weighting without dictating automated execution.
Inputs:
- Technical evidence and signals
- News sources (exchange filings, corporate announcements, major financial publications)
- Statistical backtest metrics and walk-forward validation results
Decision Logic:
- Base confidence strictly on technical evidence as the primary weight.
- Modify confidence based on news evidence, weighted by source reliability.
- Ensure news never automatically overrides strong technical evidence.
- Evaluate conflicts between technicals and news on a case-by-case basis.
- Exclude social sentiment from dominating confidence scoring.
- Require statistical significance tests (e.g., t-stat, Deflated Sharpe) as validation gates for active trading approval; standard confidence intervals are insufficient.
Outputs:
- Confidence rating
- Conviction weighting suggestions
- Supporting evidence summaries
Dependencies:
- SDM-04 Signal Discovery
- SDM-05 Signal Validation
Failure Conditions:
- [VALIDATION_REQUIRED] Exact mathematical formulas converting NLP/sentiment scores into confidence weights or Kelly fractions are missing.
- Absence of cross-verified technical evidence.
Human Visibility Requirements:
- Present confidence scoring, supporting evidence, and explicit flagging of any technical vs. news conflicts for human approval.
Audit Requirements:
- Log the source reliability weights applied and the resolution rationale for technical vs. news conflicts.
---

---
[SDM-07 Expected Value Assessment]
Purpose: Evaluate opportunities based on probability-adjusted returns bounded by strict risk and capital preservation constraints rather than speculative potential.
Inputs:
- Estimated theoretical returns
- Historical probability metrics
- Portfolio maximum drawdown tolerance limits (5%)
- Walk-forward cross-validation data
Decision Logic:
- Prioritize trade probability over highest speculative theoretical return.
- Strictly enforce capital preservation constraints and the maximum 5% portfolio drawdown tolerance to bound acceptable downside risk.
- Utilize only walk-forward cross-validation for assessing probabilities (K-Fold CV is explicitly prohibited).
- Adjust for survivorship bias by mandating the inclusion of delisted stocks in historical probability models.
- Treat cash holding as a valid expectation if no opportunity meets probability and drawdown thresholds.
Outputs:
- Probability-adjusted return estimates
- Downside drawdown risk estimates
Dependencies:
- SDM-05 Signal Validation
Failure Conditions:
- [VALIDATION_REQUIRED] Mathematical framework for Value-at-Risk (VaR) modeling under non-ergodic market conditions is missing.
- [VALIDATION_REQUIRED] Framework for aggregate margin exposure limits across multiple accounts is unresolved.
Human Visibility Requirements:
- Display probability-adjusted return breakdowns and explicitly visualize the downside drawdown risk estimates for final approval.
Audit Requirements:
- Record walk-forward probability inputs, drawdown compliance gating, and survivorship bias validation per evaluated opportunity.
---

---
[SDM-08 Opportunity Ranking]
Purpose: Sort, prioritize, and select the top viable opportunities for final advisory recommendation and allocation suggestions.
Inputs:
- Expected Value Assessment (probability-adjusted returns)
- Confidence Assessment (confidence ratings)
- Target position limits (3-5 positions)
Decision Logic:
- Rank opportunities by preferring higher quality (highest probability) trades over higher quantity.
- Retain genuine winners by avoiding overly restrictive filtering (missing a winner is worse than rejecting too many marginal trades).
- Limit selected opportunities to the target position count of 3 to 5.
- Scale down to a single position or zero if insufficient opportunities exist, strictly avoiding forced capital deployment.
- Determine allocation sizes using Conviction Weighting (highest confidence first, then best-idea weighted); reject equal-weight allocation.
- Trigger an explicit null-state if no actionable opportunities meet minimum requirements.
Outputs:
- Opportunity Ranking list
- Target Allocation Suggestions
- Exit Suggestions
- Explicit null-state declaration ("No actionable opportunities currently meet requirements.") if applicable
Dependencies:
- SDM-06 Confidence Assessment
- SDM-07 Expected Value Assessment
Failure Conditions:
- [VALIDATION_REQUIRED] Mathematical quantification for exact slippage thresholds is missing.
Human Visibility Requirements:
- Display ranked list, proposed conviction-weighted allocations, confidence factors, risk summaries, and exit criteria in a unified advisory report.
Audit Requirements:
- Track the ranking logic execution to prove equal-weighting was not used and that null-states are properly declared when quality thresholds fail.
---

---
[SDM-09 Capital Allocation]
Purpose: Determine how capital is distributed across selected trading opportunities and when to hold cash.
Inputs: Opportunity confidence scores, conviction rankings, available capital, market volatility, liquidity metrics.
Decision Logic:
- If no acceptable opportunities exist, the system defaults to holding cash. Capital deployment must never be forced.
- Allocations must follow a conviction-weighted hierarchy: prioritizing Confidence-Weighted allocation first, then Best-Idea-Weighted.
- Equal-weight allocation is explicitly prohibited.
- Higher confidence opportunities receive proportionally larger allocations.
- Maximum position concentration limits must be strictly respected during allocation.
- Execution sizing must automatically scale against portfolio illiquidity.
- Execution size must be scaled down when quantile uncertainty bands widen.
- [VALIDATION_REQUIRED] Mathematical framework for converting sentiment scores into exact position sizing (Kelly fractions).
- [VALIDATION_REQUIRED] Aggregate margin exposure management constraints for allocation.
Outputs: Target capital allocation per opportunity, cash reserve suggestion.
Dependencies: SDM-06 Confidence Assessment, SDM-08 Opportunity Ranking, SDM-11 Position Management.
Failure Conditions: Insufficient viable opportunities triggers a "Hold Cash" state. Widening uncertainty bands force an allocation scale-down.
Human Visibility Requirements: Allocation suggestions and explicit statements if "Hold Cash" is recommended must be provided in the human-facing report. Human approval is mandatory before any capital allocation is deployed.
Audit Requirements: Logging of the conviction weights applied, justification for capital distribution, and any scale-down events triggered by illiquidity or uncertainty.
---

---
[SDM-10 Human Approval]
Purpose: To ensure deterministic control and mandatory human authorization over AI-generated trading recommendations before execution.
Inputs:
- Trade recommendations
- Supporting evidence (technical and news)
- Confidence metrics
- Risk summaries
- Exit suggestions
Decision Logic:
- The system must halt and wait for explicit human approval before any trade action is initiated.
- The system must treat all generated recommendations strictly as advisory; autonomous execution is prohibited.
- The system must accept and prioritize human overrides, granting the owner final authority over any trade parameter.
- The system must trigger a case-by-case evaluation protocol when disagreements occur between the system recommendation and the owner's decision.
- The system must block any modification to algorithmic pricing limits unless explicit secondary human authorization is provided.
Outputs:
- Approval or rejection decisions
- Approved parameter overrides
Dependencies:
- SDM-08 Opportunity Ranking
- SDM-09 Capital Allocation
- SDM-06 Confidence Assessment
Failure Conditions:
- A recommendation transitions into an executable state without documented human approval.
- An algorithmic pricing limit is bypassed or overridden without the required authorization.
Human Visibility Requirements:
- The human owner must be presented with the complete opportunity ranking, allocation suggestions, confidence scores, supporting evidence, risk summaries, and exit suggestions prior to the approval gate.
Audit Requirements:
- Continuous logging of the original system recommendation versus the final human action.
- Immutable record of all owner overrides and authorized parameter modifications.
---

---
[SDM-11 Position Management]
Purpose: Control portfolio-level risk limits, manage total position count, and prevent systemic drawdowns across active trades.
Inputs: Current active positions, aggregated portfolio drawdown, aggregate concentration exposure across accounts, liquidity depth, trailing volume.
Decision Logic:
- Enforce a target position count of 3 to 5 active positions.
- The system must recommend fewer positions (or a single opportunity) if insufficient high-probability opportunities exist.
- Capital preservation is mandatory: the system must block position recommendations that materially threaten portfolio survivability.
- Strictly observe a maximum portfolio drawdown tolerance limit of 5%.
- Control concentration risk and synthetic leverage to prevent aggregate margin breaches.
- Hard position limits must be strictly enforced.
- Automatically reduce recommendation sizing when uncertainty bands (e.g., quantile bands) widen.
- Apply volume-based allocation limits relative to trailing volume.
- [VALIDATION_REQUIRED] Mathematical framework for Value-at-Risk (VaR) modeling under non-ergodic market conditions.
Outputs: Position count directives, drawdown halt triggers, concentration limit enforcement directives, allocation reduction triggers.
Dependencies: SDM-09 Capital Allocation, SDM-07 Expected Value Assessment.
Failure Conditions: Portfolio drawdown approaches or hits the 5% tolerance limit. Concentration limits or margin exposures exceed allowed thresholds.
Human Visibility Requirements: A comprehensive risk summary covering position limits and portfolio survivability must be included in the advisory report. Human approval is mandatory for any position sizing and limit overrides.
Audit Requirements: Logging of active position counts relative to targets, documentation of any drawdown threshold warnings, and records of concentration risk management actions.
---

---
[SDM-12 Exit Decision]
Purpose: Provide criteria and timeline recommendations for closing active trading positions based on evidence continuity and risk factors.
Inputs: Expected time horizon, technical/news evidence continuity, slippage metrics, transaction costs, trailing volume.
Decision Logic:
- Base expected trade durations are governed by a Primary Horizon (1-3 Days) and a Secondary Horizon (5-10 Days).
- Align base signal horizons with designated short-term (1-3 days) and medium-term (5-10 days) swing durations.
- Ongoing technical and news evidence must be assessed continuously throughout the trade lifecycle.
- Technical evidence deterioration strictly outweighs positive news sentiment when evaluating exit conditions.
- Trades extending beyond the expected duration are allowed to remain valid only if the supporting technical evidence explicitly justifies the extension.
- Extend trade validity beyond primary expected durations if supporting evidence continues to persist.
- Exit recommendations must account for estimated transaction costs and execution viability.
- [VALIDATION_REQUIRED] Slippage threshold quantification and exact execution barrier math.
Outputs: Exit suggestions, holding period extension validations.
Dependencies: SDM-11 Position Management.
Failure Conditions: Technical evidence deteriorates or contradicts the original thesis. Expected transaction costs or slippage negate the remaining expected value of the trade.
Human Visibility Requirements: Suggested exit conditions and any justification for extending a trade beyond its initial primary or secondary horizon must be clearly presented in the report. Human approval is mandatory for all exit actions.
Audit Requirements: Documentation of the evidence used to validate trade extensions, and logging of the slippage/transaction cost assumptions used during the exit recommendation.
---

---
[SDM-13 Attribution]
STATUS: DEFERRED

Reason:
Insufficient evidence in authoritative corpus.
---

---
[SDM-14 Research Intake]
STATUS: DEFERRED

Reason:
Insufficient evidence in authoritative corpus.
---

---
[SDM-15 Risk Governance]
Purpose: Enforce strict deterministic risk controls, safeguard capital preservation, prevent systemic failure loops, and ensure mandatory human oversight.
Inputs: Market Regime Classification, AI Sentiment Uncertainty Quantile Bands, Margin Limits, Macro shock flags.
Decision Logic:
- Capital preservation is mandatory; maximum portfolio drawdown tolerance is explicitly capped at 5%.
- Cash is recognized as a valid position; capital deployment must never be forced if acceptable opportunities do not exist.
- Execution logic must remain strictly deterministic; AI is advisory and must never dictate execution sizing or routing.
- Human approval is mandatory before any trade recommendation can be acted upon.
- Position limit breaches must trigger hard deterministic halts rather than passive alerts.
- Circuit breakers must detect and halt recommendations during trend-following dynamic hedging cycles.
- Sizing recommendations must instantly scale down or halt when uncertainty quantile bands widen.
- Volume spikes must be monitored for informational cascades to halt recommendations during non-transparent selling.
- Variation margin assumptions must be restricted during periods of elevated volatility or market stress.
- Synthetic leverage margin assumptions must be audited to match standard initial margin limits.
- Implement hard halt triggers during extreme macro shocks and non-ergodic market breakdowns.
- Halt trend-following dynamic hedging cycles during extreme market conditions.
- Prevent model anchoring to peak historical transaction data during regime shifts.
- [VALIDATION_REQUIRED] Mathematical framework for calculating daily Value-at-Risk under non-ergodic conditions.
- [VALIDATION_REQUIRED] Specific mathematical formulas converting semantic sentiment scores into localized position sizing without violating deterministic boundaries.
- [VALIDATION_REQUIRED] Aggregate margin exposure management rules across multiple independent accounts.
Outputs: Hard recommendation halts, Dynamic margin scaling adjustments, Human approval gates, Critical alert states, allocation reduction triggers.
Dependencies: SDM-03 Market Regime Classification, SDM-07 Expected Value Assessment, SDM-11 Position Management, [VALIDATION_REQUIRED] Exact mathematical indicators to prove an equity has exited an ergodic state and entered an unpredictable tail-risk regime.
Failure Conditions: Portfolio drawdown exceeds 5%; Unapproved trade attempted; Uncertainty bands widen beyond threshold.
Human Visibility Requirements: Explicit request for human approval with supporting evidence; active display of current drawdown versus the 5% limit; clear display of halted or restricted states.
Audit Requirements: Log every human approval or rejection; log all drawdown limit tests; log all triggered halts and scaling adjustments.
---

# SADR_V2.1.md
## System Architecture Design Requirements — Version 2.1

**Derived From:** SDM_V2.3 (FROZEN — FINAL CANONICAL)
**Authority Basis:** SDM_FREEZE_CERTIFICATION.md
**Reconstruction Protocol:** SADR_RECONSTRUCTION_PROTOCOL v1.0
**Change Control:** SADR_CHANGE_CONTROL_AND_RECERTIFICATION_PROTOCOL
**Version:** 2.1
**Status:** CERTIFIED — see SADR_RECERTIFICATION_REPORT.md
**Supersedes:** SADR_V2.md
**Changes from V2:** See SADR_CHANGE_REGISTER_V2.1.md (8 changes — CHANGE-01 through CHANGE-08)

---

## SECTION 1 — EXECUTIVE SUMMARY

This document defines the minimum sufficient capability set required to execute SDM_V2.3 as written. It is the sole specification between the frozen SDM constitution and architecture design.

**Changes from SADR_V2:**
- CAP-29 revised: governance compliance assessment output removed; broker-specific language removed from inputs
- CAP-31 added: Governance Compliance Monitor — the capability that detects governance violations and restorations, owning the constitutionally mandated detection function in GOV-02 Rules 1 and 3
- CAP-26 inputs revised: now receives from CAP-31 (not CAP-29)
- Section 5 dependency chain updated: CAP-31 inserted between CAP-29 and CAP-26
- Section 11 validation classification: 7 items reclassified CLASS_A → CLASS_B; VAL-05 remains sole CLASS_A
- CAP-30 language: "append-only" replaced with "immutable"

**Total Capabilities:** 31
**Deferred Domains:** 1 (SDM-14)
**Open Validation Items:** 17 (VAL-01 through VAL-17)
**CLASS_A Architecture Blockers:** 1 (VAL-05 only)

---

## SECTION 2 — CONSTITUTIONAL CONSTRAINTS

*(Unchanged from SADR_V2. Reproduced in full.)*

**CONSTRAINT-01:** Human approval is mandatory before any trade action is initiated. No capability in this system may initiate, execute, place, modify, or cancel a trade order. (SDM-CONST-06)

**CONSTRAINT-02:** The system identity is AI Swing Trading Research Analyst. All outputs are advisory. No output constitutes an executable trade order. (SDM-CONST-01, SDM-CONST-13)

**CONSTRAINT-03:** Probability-first philosophy governs all ranking and selection logic. Highest probability opportunities take precedence over highest theoretical return. (SDM-CONST-09)

**CONSTRAINT-04:** Technical signals are the primary evidence layer. News signals are supplementary. News may never automatically override strong technical evidence. (SDM-CONST-10)

**CONSTRAINT-05:** Cash is a valid position. The system must never force capital deployment. (SDM-CONST-07)

**CONSTRAINT-06:** Maximum portfolio drawdown tolerance is 5%. This limit is absolute. (SDM-CONST-08)

**CONSTRAINT-07:** Attribution possesses read-only observational authority. It may not write to any recommendation, signal, validation, confidence, ranking, allocation, or governance logic. (SDM-13 Rules 8, 10)

**CONSTRAINT-08:** Walk-forward cross-validation is mandatory for all statistical validation. K-fold cross-validation is constitutionally prohibited. (SDM-03 Rule 1, SDM-05 Rule 2, SDM-07 Rule 3)

**CONSTRAINT-09:** All outputs to the human approval gate must be simultaneously presented as an Open Menu. Sequential forced selection is prohibited. (SDM-08 Rule 8)

**CONSTRAINT-10:** The system is authorized to autonomously execute research, analysis, monitoring, attribution, reporting, and governance functions under three activation modes. This authority does not extend to trade execution, order placement, order modification, or any autonomous market action. (SDM-CONST-15)

---

## SECTION 3 — CAPABILITY CATALOG

| Cap ID | Capability Name | Domain | Authority Class |
|--------|----------------|--------|-----------------|
| CAP-01 | Market Data Ingestion | SDM-02 | AUTONOMOUS_RESEARCH |
| CAP-02 | Data Cross-Verification | SDM-02, SDM-05 | AUTONOMOUS_RESEARCH |
| CAP-03 | Corporate Action Adjustment | SDM-02 | AUTONOMOUS_RESEARCH |
| CAP-04 | Universe Eligibility Enforcement | SDM-02 | AUTONOMOUS_RESEARCH |
| CAP-05 | Market Regime Classification | SDM-03 | AUTONOMOUS_RESEARCH |
| CAP-06 | Concept Drift Detection | SDM-03, SDM-05 | AUTONOMOUS_RESEARCH |
| CAP-07 | Technical Signal Generation | SDM-04 | AUTONOMOUS_RESEARCH |
| CAP-08 | Supplementary Signal Intake | SDM-04 | AUTONOMOUS_RESEARCH |
| CAP-09 | Technical-News Conflict Evaluation | SDM-04, SDM-06 | SHARED_AUTHORITY |
| CAP-10 | Walk-Forward Signal Validation | SDM-05 | AUTONOMOUS_RESEARCH |
| CAP-11 | Statistical Edge Verification | SDM-05 | AUTONOMOUS_RESEARCH |
| CAP-12 | Confidence Scoring | SDM-06 | AUTONOMOUS_RESEARCH |
| CAP-13 | Expected Value Computation | SDM-07 | AUTONOMOUS_RESEARCH |
| CAP-14 | Survivorship Bias Correction | SDM-02, SDM-07 | AUTONOMOUS_RESEARCH |
| CAP-15 | Opportunity Ranking | SDM-08 | AUTONOMOUS_RESEARCH |
| CAP-16 | Conviction-Weighted Allocation | SDM-08, SDM-09 | AUTONOMOUS_RESEARCH |
| CAP-17 | Null-State Declaration | SDM-01, SDM-08 | AUTONOMOUS_RESEARCH |
| CAP-18 | Human Approval Gate | SDM-10, SDM-CONST-06 | HUMAN_APPROVAL |
| CAP-19 | Position Limit Enforcement | SDM-11 | AUTONOMOUS_RESEARCH |
| CAP-20 | Exit Condition Recommendation | SDM-12 | AUTONOMOUS_RESEARCH |
| CAP-21 | Attribution Observation | SDM-13 | AUTONOMOUS_RESEARCH |
| CAP-22 | Human Override Delta Tracking | SDM-13 | AUTONOMOUS_RESEARCH |
| CAP-23 | Risk Circuit Breaker Enforcement | SDM-15 | AUTONOMOUS_RESEARCH |
| CAP-24 | Hard Deterministic Halt | SDM-CONST-14 State 4, SDM-11 | AUTONOMOUS_RESEARCH |
| CAP-25 | Governance Halt | SDM-CONST-14 State 1, GOV-01 | AUTONOMOUS_RESEARCH |
| CAP-26 | Governance Lockout | SDM-CONST-14 State 2, GOV-02 | AUTONOMOUS_RESEARCH |
| CAP-27 | Conditional Recommendation Suspension | SDM-CONST-14 State 3, SDM-15 | AUTONOMOUS_RESEARCH |
| CAP-28 | System Activation Authority | SDM-CONST-15 | AUTONOMOUS_RESEARCH |
| CAP-29 | Portfolio State Visibility | SDM-10, SDM-11, SDM-15 | AUTONOMOUS_RESEARCH |
| CAP-30 | Immutable Audit Log | SDM-02 through SDM-15 (all Audit clauses) | AUTONOMOUS_RESEARCH |
| CAP-31 | Governance Compliance Monitor | GOV-02 Rules 1, 3; SDM-CONST-14 State 2 | AUTONOMOUS_RESEARCH |

---

## SECTION 4 — CAPABILITY SPECIFICATIONS

### Domain: Universe Selection (SDM-02)

**CAP-01 | Market Data Ingestion**
*(Unchanged from SADR_V2)*

*Necessity:* Without the ability to receive market data, no signal, validation, or recommendation is possible.

*Inputs:* OHLCV price and volume data for Indian equities (NSE/BSE). Historical data inclusive of delisted equities.

*Outputs:* Raw, unprocessed market data available to CAP-02 for verification before any signal logic is permitted to consume it.

*Boundary:* Receiving data only. Does not verify, adjust, or filter.

*Constitutional Constraints:* Must support ingestion from at least two independent sources. Must include delisted equities. (SDM-02 Rules 1, 2)

*Open Validation Items:* VAL-01, VAL-02.

---

**CAP-02 | Data Cross-Verification**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-02 Rule 2 and SDM-05 Rule 1 explicitly prohibit signal logic from executing on data not verified across at least two independent sources.

*Inputs:* Raw data from CAP-01, from at least two independent sources for the same data point.

*Outputs:* Verified data cleared for signal logic consumption. Mismatch flags. Cross-verification match/mismatch records for audit.

*Boundary:* Verification only. Does not adjust data (CAP-03). Does not filter the universe (CAP-04).

*Constitutional Constraints:* Signal logic may not receive data that has not passed cross-verification. Hard blocking gate. (SDM-02 Rule 2, SDM-05 Rule 1)

---

**CAP-03 | Corporate Action Adjustment**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-02 Rule 3 mandates split-adjusted data and explicitly rejects unadjusted data.

*Inputs:* Verified data from CAP-02. Corporate action records (splits, de-mergers).

*Outputs:* Split-adjusted OHLCV data. Adjustment audit records. Rejection records for unadjustable data.

*Boundary:* Adjustment only. Does not verify sources (CAP-02). Does not determine eligibility (CAP-04).

*Constitutional Constraints:* Unadjusted split data must be rejected before reaching downstream capabilities. (SDM-02 Rule 3)

*Open Validation Items:* VAL-02.

---

**CAP-04 | Universe Eligibility Enforcement**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-03 restricts the system to Indian equities (NSE/BSE) exclusively.

*Inputs:* Adjusted, verified data from CAP-03.

*Outputs:* Eligible equity set. Count of eligible versus filtered equities (human visibility). Log of all excluded assets and triggered filter rules.

*Boundary:* Eligibility determination only. Does not verify (CAP-02). Does not adjust (CAP-03). Does not generate signals (CAP-07).

*Constitutional Constraints:* NSE/BSE Indian equities only. (SDM-CONST-03)

*Open Validation Items:* VAL-01.

---

### Domain: Market Regime Classification (SDM-03)

**CAP-05 | Market Regime Classification**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-03 requires regime classification to prevent concept drift and inappropriate strategy execution.

*Inputs:* Eligible, verified, adjusted market data.

*Outputs:* Current market regime classification. Regime shift alerts. Walk-forward cross-validation bounds. Broad market trend filter state (for CAP-07 sector rotation evaluation). Non-ergodic condition signal (generic condition signal interface consumed by CAP-23 and CAP-27).

*Boundary:* Classification and alerting only. Does not detect model drift (CAP-06). Does not generate signals (CAP-07). Does not enforce governance (CAP-23 through CAP-27).

*Constitutional Constraints:* Walk-forward mandatory; K-fold prohibited. (SDM-03 Rule 1) Sector rotation evaluation requires broad market trend filter. (SDM-03 Rule 4) Regime shift alerts must be explicit and human-visible.

*Open Validation Items:* VAL-03 (CLASS_B — generic signal interface sufficient for architecture), VAL-04.

---

**CAP-06 | Concept Drift Detection**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-03 Rule 2 mandates concept drift monitoring. SDM-15 Rule 13 prohibits model anchoring.

*Inputs:* Current model behavior metrics. Historical model behavior baselines. Regime classification from CAP-05.

*Outputs:* Concept drift metrics. Drift alerts. Model anchoring detection events.

*Boundary:* Detection and alerting only. Does not modify models. Does not suspend recommendations.

*Constitutional Constraints:* Continuous drift monitoring. Model anchoring to peak historical data during regime transitions must be detected. (SDM-15 Rule 13)

---

### Domain: Signal Discovery (SDM-04)

**CAP-07 | Technical Signal Generation**
*(Unchanged from SADR_V2)*

*Necessity:* Technical signals are the primary evidence layer. (SDM-CONST-10, SDM-04 Rule 1)

*Inputs:* Eligible, verified, adjusted market data. Broad market trend filter state from CAP-05. Regime classification from CAP-05.

*Outputs:* Technical signal set with evidence type, supporting data, and signal quality metadata.

*Boundary:* Signal generation only. Does not validate statistically (CAP-10, CAP-11). Does not score confidence (CAP-12).

*Constitutional Constraints:* Technical evidence takes strict priority. (CONSTRAINT-04) Price breakouts validated using volume spikes. (SDM-04 Rule 8) Chart patterns with statistical edges are valid. (SDM-04 Rule 9) Moving averages contextually handled as lagging. (SDM-04 Rule 10) Sector rotation aligned with trend filter. (SDM-04 Rule 7)

---

**CAP-08 | Supplementary Signal Intake**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-04 Rules 3 and 5 require news as a supplementary evidence layer.

*Inputs:* News and event data. Earnings surprise events. Insider buying events.

*Outputs:* Supplementary signal set with source reliability metadata.

*Boundary:* Intake and classification only. Does not evaluate conflicts (CAP-09). Does not score confidence (CAP-12).

*Constitutional Constraints:* Analyst rating changes and social media sentiment excluded or minimal weight. (SDM-04 Rule 6) AI evaluations isolated to semantic/cognitive domain. (SDM-04 Rule 12)

*Open Validation Items:* VAL-05 (CLASS_A — sole architecture blocker; determines CAP-08 → CAP-12 interface), VAL-06.

---

**CAP-09 | Technical-News Conflict Evaluation**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-04 Rule 4 and SDM-06 Rule 4 define conflict as a constitutionally recognized scenario requiring evaluation.

*Inputs:* Technical signals from CAP-07. Supplementary signals from CAP-08.

*Outputs:* Conflict detection result. Explicit conflict flag when evidence is in opposition. Evidence characterization (both sides). Resolution rationale for audit. Conflict flag presented to human prior to approval gate.

*Boundary:* Conflict detection and characterization only. System identifies and surfaces; human reviews at CAP-18.

*Authority:* SHARED_AUTHORITY — system evaluates and flags; human reviews and decides.

*Constitutional Constraints:* Conflict resolution rationale logged. Human visibility of conflicts mandatory prior to approval gate. (SDM-06 Human Visibility)

---

### Domain: Signal Validation (SDM-05)

**CAP-10 | Walk-Forward Signal Validation**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-05 Rule 2 mandates walk-forward cross-validation. K-fold is constitutionally prohibited.

*Inputs:* Signal candidates from CAP-07. Historical market data with temporal ordering preserved.

*Outputs:* Validated signal set. Walk-forward validation results. Validation scores. Rejected signals with rejection basis.

*Boundary:* Temporal validation only. Does not measure statistical edge (CAP-11).

*Constitutional Constraints:* K-fold prohibited. Walk-forward mandatory. (CONSTRAINT-08) Comprehensive logic coverage required. (SDM-05 Rule 3)

*Open Validation Items:* VAL-04.

---

**CAP-11 | Statistical Edge Verification**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-05 Rules 4, 5, 6 require edge verification, stability tracking, and outlier detection.

*Inputs:* Walk-forward validated signals from CAP-10. Stability baseline metrics.

*Outputs:* Statistical edge verdict per signal. Deflated return metrics or statistical significance test results. Stability index values. Outlier detection verification records.

*Boundary:* Edge measurement only. Does not validate temporal ordering (CAP-10).

*Constitutional Constraints:* Deflated return metrics or statistical significance tests required. (SDM-05 Rule 4) Stability indexes required. (SDM-05 Rule 5) Outlier detectors verified through synthetic anomaly injection. (SDM-05 Rule 6) Data smoothing may not mask structural anomalies. (SDM-05 Rule 7)

---

### Domain: Confidence Assessment (SDM-06)

**CAP-12 | Confidence Scoring**
*(Unchanged from SADR_V2 except VAL-05 note updated)*

*Necessity:* Confidence scores feed conviction weights which govern capital allocation. (SDM-09 Rules 2–4)

*Inputs:* Statistically validated signals from CAP-11. Supplementary signal set with source reliability metadata from CAP-08. Conflict flags from CAP-09.

*Outputs:* Confidence score per opportunity. Source reliability weight log. Explicit conflict marking on scored opportunities.

*Boundary:* Scoring only. Does not generate signals. Does not rank opportunities (CAP-15).

*Constitutional Constraints:* Technical evidence primary weight. (SDM-06 Rule 1) News modifies confidence by source reliability. (SDM-06 Rule 2) Social sentiment excluded from dominance. (SDM-06 Rule 5) Statistical significance tests (t-stat, Deflated Sharpe) required as validation gates. Standard confidence intervals insufficient. (SDM-06 Rule 6) Sentiment integration pathway (whether sentiment enters this computation) awaits VAL-05 resolution.

*Open Validation Items:* VAL-05 (CLASS_A — determines whether CAP-08 is a computational input to this capability or travels an advisory-only channel to CAP-18), VAL-07.

---

### Domain: Expected Value Assessment (SDM-07)

**CAP-13 | Expected Value Computation**
*(Unchanged from SADR_V2 except VAL-08 classification updated)*

*Necessity:* SDM-07 requires probability-adjusted return evaluation bounded by the 5% drawdown constraint.

*Inputs:* Confidence-scored opportunities from CAP-12. Current portfolio state from CAP-29. Historical probability data from CAP-14. Regime context parameter from CAP-05.

*Outputs:* Probability-adjusted return estimate per opportunity. Downside drawdown risk estimate. EV-filtered opportunity set. Cash-holding signal when no opportunity meets thresholds.

*Boundary:* EV computation only. Does not score confidence (CAP-12). Does not rank (CAP-15).

*Constitutional Constraints:* Trade probability over speculative return. (SDM-07 Rule 1, CONSTRAINT-03) 5% drawdown tolerance strictly bounds risk. (SDM-07 Rule 2, CONSTRAINT-06) Walk-forward mandatory; K-fold prohibited. (SDM-07 Rule 3, CONSTRAINT-08) Cash holding when no opportunity qualifies. (SDM-07 Rule 5, CONSTRAINT-05)

*Open Validation Items:* VAL-08 (CLASS_B — regime context input parameter sufficient for architecture; VaR formula is implementation), VAL-09 (CLASS_B — extension point per SDM-CONST-12 sufficient).

---

**CAP-14 | Survivorship Bias Correction**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-02 Rule 1 and SDM-07 Rule 4 mandate inclusion of delisted equities in historical datasets.

*Inputs:* Historical market dataset including delisted equities from CAP-01.

*Outputs:* Survivorship-bias-corrected historical dataset available to CAP-13. Validation confirmation per opportunity for audit.

*Boundary:* Bias correction for historical datasets only.

*Constitutional Constraints:* Historical probability models must include delisted equities. (SDM-02 Rule 1, SDM-07 Rule 4)

---

### Domain: Opportunity Ranking (SDM-08)

**CAP-15 | Opportunity Ranking**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-11 requires opportunity ranking in every recommendation.

*Inputs:* EV-filtered opportunities from CAP-13. Position count from CAP-29.

*Outputs:* Ranked opportunity list targeting 3–5 positions. Ranking logic execution records. Null-state trigger when no opportunities qualify.

*Boundary:* Ranking and selection only. Does not compute EV (CAP-13). Does not declare null-state (CAP-17).

*Constitutional Constraints:* Rank by highest probability. (SDM-08 Rule 1, CONSTRAINT-03) Target 3–5; scale to fewer or zero if needed. (SDM-08 Rules 3, 4) Open Menu simultaneous presentation mandatory. Sequential forced selection prohibited. (SDM-08 Rule 8, CONSTRAINT-09)

---

**CAP-16 | Conviction-Weighted Allocation**
*(Unchanged from SADR_V2 except VAL-12 classification updated)*

*Necessity:* SDM-08 Rule 6 and SDM-09 Rules 2–4 mandate conviction-weighted allocation and prohibit equal-weighting.

*Inputs:* Ranked opportunities from CAP-15 with confidence scores from CAP-12. Portfolio state from CAP-29.

*Outputs:* Conviction-weighted allocation suggestions per opportunity. Explicit "Hold Cash" statement when applicable. Conviction weight justification per suggestion.

*Boundary:* Allocation suggestion only. Does not rank (CAP-15). Does not enforce limits (CAP-19).

*Constitutional Constraints:* Conviction hierarchy: confidence-weighted first, then best-idea-weighted. (SDM-09 Rule 2) Equal-weighting prohibited. (SDM-09 Rule 3) Higher confidence → proportionally larger allocations. (SDM-09 Rule 4) Concentration limits respected. (SDM-09 Rule 5) Sizing scales against illiquidity. (SDM-09 Rule 6) Sizing scales down when uncertainty bands widen. (SDM-09 Rule 7)

*Open Validation Items:* VAL-11, VAL-12 (CLASS_B — extension point per SDM-CONST-12 sufficient).

---

**CAP-17 | Null-State Declaration**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-01 Rule 1, SDM-08 Rule 7, SDM-CONST-11 all require explicit null-state output when no opportunities qualify.

*Inputs:* Null-state trigger from CAP-15.

*Outputs:* Explicit null-state declaration containing the constitutionally mandated statement. Null-state event log record.

*Boundary:* Declaration only. The null-state is a valid and required output type, not an error condition.

*Constitutional Constraints:* Mandatory when qualifying opportunities do not exist. Capital deployment must never be forced. (CONSTRAINT-05)

---

### Domain: Human Approval Gate (SDM-10)

**CAP-18 | Human Approval Gate**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-06 constitutional invariant: human approval mandatory before any trade action.

*Inputs:* Complete advisory package: ranked opportunity list, conviction-weighted allocation suggestions, confidence scores, supporting evidence, risk summaries, exit suggestions, conflict flags, null-state declaration if applicable, active halt states from CAP-24/CAP-25/CAP-26/CAP-27, current drawdown status from CAP-29.

*Outputs:* Human approval decision. Human override parameters. Case-by-case evaluation trigger when human decision conflicts with system recommendation. Secondary authorization trigger for algorithmic pricing limit modifications.

*Boundary:* Presentation and authorization gateway. System presents; human decides. No timeout-based auto-approval. No bypass pathways.

*Authority:* HUMAN_APPROVAL.

*Constitutional Constraints:* All recommendations strictly advisory. (CONSTRAINT-02) System halts and awaits explicit authorization before any trade action. (SDM-10 Rule 1, CONSTRAINT-01) Complete advisory package presented prior to gate. (SDM-10 Human Visibility) Human overrides accepted and prioritized. (SDM-10 Rule 3) Disagreements trigger case-by-case evaluation. (SDM-10 Rule 4) Pricing limit modifications require secondary authorization. (SDM-10 Rule 5) Every approval, rejection, and override logged immutably. (CAP-30)

---

### Domain: Position Management (SDM-11)

**CAP-19 | Position Limit Enforcement**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-11 Rule 6 requires hard position limit enforcement. SDM-CONST-14 State 4 is triggered by breach.

*Inputs:* Active position count from CAP-29. Uncertainty band metrics. Volume data.

*Outputs:* Position limit compliance status. Concentration limit compliance status. Hard halt trigger to CAP-24 on breach. Human-visible alert on breach. Scaling signal to CAP-16 when uncertainty bands widen.

*Boundary:* Limit monitoring and enforcement triggering only. Does not manage halt state (CAP-24).

*Constitutional Constraints:* Hard limits strictly enforced — not passively alerted. (SDM-11 Rule 6) Sizing automatically reduces when uncertainty bands widen. (SDM-11 Rule 7) Volume-based allocation limits apply relative to trailing volume. (SDM-11 Rule 8) Target count 3–5. (SDM-11 Rules 1, 2)

---

### Domain: Exit Decision (SDM-12)

**CAP-20 | Exit Condition Recommendation**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-11 requires exit suggestions in every recommendation.

*Inputs:* Technical evidence on open positions. Supplementary signal evidence on open positions. Time elapsed against horizons. Portfolio state from CAP-29.

*Outputs:* Exit condition recommendation with rationale. Extension justification when trade continuation is proposed. Transaction cost estimates factored into exit viability.

*Boundary:* Exit recommendation generation only. Does not enforce exits (human-only). Does not manage position limits (CAP-19).

*Constitutional Constraints:* Exit precedence: Risk > Technical > Time. (SDM-12 Exit Precedence) Technical deterioration outweighs positive news in exit evaluation. (SDM-12 Rule 3) Extensions require explicit technical evidence. (SDM-12 Rule 4) Transaction costs and execution viability accounted for. (SDM-12 Rule 5) Human approval mandatory before any exit action. (CONSTRAINT-01)

*Open Validation Items:* VAL-10, VAL-13.

---

### Domain: Attribution (SDM-13)

**CAP-21 | Attribution Observation**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-13 defines attribution as a required function with specific tracking obligations.

*Inputs:* System recommendations (accepted and rejected). Post-trade outcomes. Market outcomes for rejected opportunities. Metadata: setup type, market regime context, holding duration.

*Outputs:* System Alpha (Baseline) layer. Theoretical expectancy records for rejected opportunities. Attribution reports, insights, and warnings for human review.

*Boundary:* Observation and reporting only. May generate insights and warnings. May not modify any recommendation behavior. (CONSTRAINT-07)

*Constitutional Constraints:* Tracks accepted and rejected opportunities. (SDM-13 Rule 1) Metadata required. (SDM-13 Rule 2) Theoretical expectancy tracked for rejected. (SDM-13 Rule 3) System Alpha as distinct layer. (SDM-13 Rule 4) May generate insights and warnings for human review. (SDM-13 Rule 7) Changes to system behavior require explicit human approval. (SDM-13 Rules 8, 9, 10)

---

**CAP-22 | Human Override Delta Tracking**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-13 Rules 5 and 6 explicitly require the delta between system recommendation and human action as a distinct layer.

*Inputs:* System recommendations from CAP-18 (pre-decision). Human actions recorded at CAP-18 (post-decision).

*Outputs:* Human Override Delta (Human Alpha/Bleed) layer per trade cycle. Edge analysis: whether human intervention adds value or destroys edge.

*Boundary:* Delta measurement and recording only. Distinct from System Alpha (CAP-21). May not feed back into recommendation logic without human approval. (CONSTRAINT-07)

*Constitutional Constraints:* Human Override Delta maintained as distinct layer from System Alpha. (SDM-13 Rule 5) Delta measures whether human intervention adds value or destroys edge. (SDM-13 Rule 6)

---

### Domain: Risk Governance (SDM-15, GOV-01, GOV-02)

The four halt-state capabilities (CAP-24 through CAP-27) implement SDM-CONST-14's four constitutionally distinct halt states. Each state is governed independently. Multiple states may be simultaneously active. Restoration of one state does not restore another.

**CAP-23 | Risk Circuit Breaker Enforcement**
*(Unchanged from SADR_V2 except VAL-03/VAL-17/VAL-14 classifications updated)*

*Necessity:* SDM-15 Rules 6–12 define market-condition-responsive enforcement mechanisms distinct from the constitutional halt states.

*Inputs:* Uncertainty band metrics. Volume spike data. Margin assumption data. Regime classification and non-ergodic condition signal from CAP-05. Macro condition signals.

*Outputs:* Recommendation scaling signals (to CAP-16 and CAP-15). Recommendation suspension signals (to CAP-27). Margin assumption restriction signals. Margin audit compliance status.

*Boundary:* Detection and signaling only. Produces signals consumed by CAP-27. Does not manage halt states directly.

*Constitutional Constraints:* Circuit breakers detect trend-following dynamic hedging cycles. (SDM-15 Rule 6) Sizing scales down/halts when uncertainty bands widen. (SDM-15 Rule 7) Volume spikes monitored for informational cascades. (SDM-15 Rule 8) Variation margin restricted during elevated volatility. (SDM-15 Rule 9) Synthetic leverage margin audited against initial margin limits. (SDM-15 Rule 10) Hard halt triggers during extreme macro shocks and non-ergodic breakdowns. (SDM-15 Rule 11) Dynamic hedging cycles halted during extreme conditions. (SDM-15 Rule 12)

*Open Validation Items:* VAL-03 (CLASS_B), VAL-08 (CLASS_B), VAL-14 (CLASS_B), VAL-17 (CLASS_B) — all reclassified; generic interface abstractions sufficient for architecture.

---

**CAP-24 | Hard Deterministic Halt**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-14 State 4 defines a constitutional halt state with its own trigger, effect, and exit.

*Inputs:* Hard halt trigger from CAP-19 (position/concentration limit breach). Human acknowledgment and portfolio compliance confirmation for exit.

*Outputs:* Hard halt active flag. Block on position recommendations causing or sustaining the breach. Human-visible alert. Halt entry and exit log records.

*Boundary:* Position recommendation blocking only on breach. Does not suspend all recommendations (CAP-27). Does not suspend new recommendations entirely (CAP-25).

*Constitutional Constraints:* Entry: position/concentration limit breach. Effect: blocks recommendations causing or sustaining breach; human-visible alert. Exit: human acknowledgment + confirmed return within limits. Independent of States 1, 2, 3. (SDM-CONST-14)

---

**CAP-25 | Governance Halt**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-14 State 1 and GOV-01 define this halt state. Without it, drawdown breach has no enforcement mechanism.

*Inputs:* Portfolio drawdown level from CAP-29. Human resumption authorization for exit.

*Outputs:* Governance Halt active flag. Block on all new recommendations. Block on all new capital allocation recommendations. Critical risk escalation report for human review. Halt entry log. Halt exit log (on human authorization).

*Boundary:* New recommendation and allocation blocking under drawdown breach. Does not execute trades or liquidations. (GOV-01 Rule 1)

*Constitutional Constraints:* Entry: portfolio drawdown ≥ 5%. (SDM-CONST-14 State 1) Effect: suspends all new recommendations and allocation recommendations; generates risk escalation report. (GOV-01 Rules 3, 4) Exit: explicit human resumption authorization. (GOV-01 Rule 5) Zero autonomous market execution under any circumstance. (GOV-01 Rule 1) Independent of States 2, 3, 4. (SDM-CONST-14)

---

**CAP-26 | Governance Lockout**
*(CHANGE-03 applied — inputs revised)*

*Necessity:* SDM-CONST-14 State 2 and GOV-02 define the Governance Lockout. Without it, the behavioral lockout governance mechanism has no implementation.

*Inputs:* **Governance violation signal from CAP-31 (entry trigger). Governance restoration signal from CAP-31 (exit trigger).**

*Outputs:* Governance Lockout active flag. Block on all new recommendations. Block on all new allocation recommendations. Block on all new capital deployment recommendations. Halt entry and exit log records.

*Boundary:* Recommendation, allocation, and capital deployment blocking under governance violation conditions. Does not execute trades or modify broker orders. (GOV-02 Rules 4, 5) Does not perform compliance evaluation (CAP-31).

*Constitutional Constraints:* Entry: governance violation signal from CAP-31. (GOV-02 Rule 1) Effect: suspends all new recommendations, allocation recommendations, and capital deployment recommendations. (GOV-02 Rule 2) Exit: governance restoration signal from CAP-31 — automatic on corrective action; no additional human authorization required beyond the corrective action itself. (GOV-02 Rule 3) Independent of States 1, 3, 4. (SDM-CONST-14)

---

**CAP-27 | Conditional Recommendation Suspension**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-14 State 3 defines a constitutional halt state with condition-driven automatic exit.

*Inputs:* Suspension signals from CAP-23. Condition clearance signals from CAP-23 (for automatic exit).

*Outputs:* Conditional Suspension active flag. Scaled-down or suspended recommendations for affected domain only. Suspension entry log with condition state. Suspension exit log with condition state at exit (mandatory per SDM-15 Rule 14).

*Boundary:* Affected-domain-only suspension. Not a system-wide halt.

*Constitutional Constraints:* Entry: adverse conditions per SDM-15 Rules 6, 7, 8, 11, 12. Effect: suspends or scales down recommendations for affected domain only. Exit: condition-driven automatic lift when triggering condition clears — not human-authorization-driven. (SDM-15 Rule 14) Both entry and exit logged with condition state. (SDM-15 Rule 14) Independent of States 1, 2, 4. (SDM-CONST-14)

---

### Domain: System Activation (SDM-CONST-15)

**CAP-28 | System Activation Authority**
*(Unchanged from SADR_V2)*

*Necessity:* SDM-CONST-15 authorizes three activation modes for research, analysis, monitoring, attribution, reporting, and governance functions.

*Inputs:* Mode 1 (Scheduled): predefined schedule. Mode 2 (On-Demand): explicit human request. Mode 3 (Event-Driven): governance, risk, or portfolio events triggering mandatory review.

*Outputs:* Initiated research and analysis cycle. Activation mode recorded in audit log.

*Boundary:* Activation authority for research/analysis/monitoring/attribution/reporting/governance only. No trade execution authority.

*Constitutional Constraints:* All three modes constitutionally authorized. No mode grants trade execution authority. Human approval remains mandatory before any trade action. (SDM-CONST-15, CONSTRAINT-01)

---

### Domain: Portfolio State (Cross-Cutting)

**CAP-29 | Portfolio State Visibility**
*(CHANGE-01 and CHANGE-05 applied)*

*Necessity:* Multiple SDM domains require current portfolio state as a direct constitutional input. Without a defined capability maintaining and providing portfolio state, these constitutional inputs have no source.

*Inputs:* Trade actions confirmed by the human at CAP-18 (the only source of portfolio state changes, since the system never executes trades). **Authoritative record of executed trade actions for state accuracy verification.**

*Outputs:* Current active position count. Current drawdown level against 5% tolerance. Current position concentration status. Current illiquidity metrics. Portfolio state provided to: CAP-13, CAP-15, CAP-16, CAP-18, CAP-19, CAP-20, CAP-25, **CAP-31**.

*Boundary:* State maintenance and provision only. Does not evaluate compliance (CAP-31). Does not compute allocations. Does not enforce limits. Does not execute trades. **Governance compliance assessment is not a function of this capability.**

*Constitutional Constraints:* Portfolio state reflects only human-approved and executed trade actions. The system has no write authority over portfolio state. (CONSTRAINT-01)

---

### Domain: Audit (Cross-Cutting)

**CAP-30 | Immutable Audit Log**
*(CHANGE-06 applied — "append-only" removed)*

*Necessity:* Every SDM decision domain from SDM-02 through SDM-15 contains an explicit Audit clause.

*Inputs:* All events from all capabilities: system decisions, human decisions, override events, halt state entries and exits, validation results, conflict resolutions, recommendation outputs, activation events, governance compliance evaluation events.

*Outputs:* **Immutable** audit trail. Per-domain records as required by each SDM Audit clause. Immutable record of original system recommendation versus final human action.

*Boundary:* Recording only. Does not process events. Does not feed back into any capability.

*Constitutional Constraints:* Original system recommendation versus final human action must be immutably recorded. (SDM-10 Audit) Halt state entry and exit with condition state logged. (SDM-15 Rule 14) All human approvals, rejections, and overrides logged. (SDM-15 Audit)

---

### Domain: Governance Compliance (GOV-02)

**CAP-31 | Governance Compliance Monitor**
*(NEW — CHANGE-02)*

*Necessity:* GOV-02 Rule 1 mandates that "the SDM detects that risk governance has been violated through human override actions." GOV-02 Rule 3 mandates that "the system shall detect restoration automatically from available portfolio state." Detection is an active evaluation function. Without this capability, CAP-26 (Governance Lockout) has no constitutional mechanism for either its entry trigger (violation detected) or its automatic exit condition (restoration detected). No existing capability is constitutionally authorized to perform this evaluation — CAP-29 provides state data; CAP-26 manages lockout state; neither evaluates compliance.

*Inputs:* Portfolio state from CAP-29 (position records, stop-loss presence, risk control compliance status, applied governance constraints).

*Outputs:* Governance violation signal to CAP-26 (entry trigger) when evaluated portfolio state indicates a governance rule has been breached. Governance restoration signal to CAP-26 (exit trigger) when evaluated portfolio state indicates the violated rule has been corrected. Compliance evaluation event records to CAP-30.

*Boundary:* Evaluation and signaling only. Does not manage lockout state (CAP-26). Does not provide portfolio metrics (CAP-29). Evaluates compliance against rules defined by GOV-02; does not define those rules.

*Authority:* AUTONOMOUS_RESEARCH — continuous evaluation executes under constitutionally authorized activation modes.

*Constitutional Constraints:*
- Must detect governance violations: removal of required stop-loss protection, violation of approved risk controls, violation of governance constraints. (GOV-02 Rule 1)
- Must detect restoration automatically from available portfolio state. Restoration is detected from corrective action; no additional human authorization is required for restoration detection itself. (GOV-02 Rule 3)
- Evaluation is continuous — not triggered only at approval gate events.
- Does not grant trade execution authority. (CONSTRAINT-01, CONSTRAINT-10)

---

## SECTION 5 — DEPENDENCY RELATIONSHIPS

### Critical Blocking Dependencies

| Dependency | Rule |
|-----------|------|
| CAP-02 blocks all signal logic | SDM-02 Rule 2, SDM-05 Rule 1 |
| CAP-10 blocks confidence scoring | SDM-05 Rule 2 |
| CAP-18 blocks all trade action | SDM-CONST-06 — no exceptions, no bypass |

### Full Dependency Chain

```
CAP-28 (Activation) — initiates cycle under Mode 1, 2, or 3
  │
  ▼
CAP-01 (Data Ingestion)
  └─▶ CAP-02 (Cross-Verification) ◀── BLOCKING GATE
        └─▶ CAP-03 (Corporate Action Adjustment)
              └─▶ CAP-04 (Universe Eligibility)
                    │
                    ├─▶ CAP-05 (Regime Classification) ──▶ CAP-06 (Concept Drift)
                    │         │
                    │         └─▶ [trend filter + regime context] ──▶ CAP-07
                    │         └─▶ [non-ergodic condition signal] ──▶ CAP-23, CAP-27
                    │
                    └─▶ CAP-14 (Survivorship Bias Correction)
                          └─▶ [bias-corrected history] ──▶ CAP-13

CAP-07 (Technical Signals)
  └─▶ CAP-10 (Walk-Forward Validation) ◀── BLOCKING GATE
        └─▶ CAP-11 (Statistical Edge Verification)
              └─▶ CAP-12 (Confidence Scoring) ◀── also receives CAP-08, CAP-09
                    └─▶ CAP-13 (Expected Value Computation)
                          └─▶ CAP-15 (Opportunity Ranking)
                                ├─▶ CAP-16 (Conviction-Weighted Allocation)
                                └─▶ CAP-17 (Null-State Declaration) [if no opportunities]

CAP-08 (Supplementary Signals) ──▶ CAP-09 (Conflict Evaluation) ──▶ CAP-12

CAP-19 (Position Limit Enforcement) ──▶ CAP-24 (Hard Deterministic Halt) [on breach]
CAP-23 (Risk Circuit Breakers) ──▶ CAP-27 (Conditional Suspension) [on condition]
CAP-29 (Portfolio State) ──▶ CAP-25 (Governance Halt) [on drawdown breach]
CAP-29 (Portfolio State) ──▶ CAP-31 (Governance Compliance Monitor)
CAP-31 ──▶ CAP-26 (Governance Lockout) [violation signal → entry]
CAP-31 ──▶ CAP-26 (Governance Lockout) [restoration signal → exit]

CAP-15, CAP-16, CAP-17, CAP-20 ──▶ CAP-18 (Human Approval Gate) ◀── MANDATORY
  │
  ├─▶ CAP-21 (Attribution Observation) [post-gate, read-only]
  └─▶ CAP-22 (Human Override Delta) [post-gate, read-only]

CAP-30 (Audit Log) ◀── receives from all capabilities
```

### Halt State Independence

The four halt states (CAP-24, CAP-25, CAP-26, CAP-27) are constitutionally independent. Each has its own entry condition, active state, and exit condition. They may be simultaneously active. Restoration of any one does not restore any other. When multiple states are simultaneously active, a recommendation is permissible only if it is not blocked by any currently active state.

---

## SECTION 6 — AUTHORITY RELATIONSHIPS

*(Unchanged from SADR_V2 except CAP-31 added to AUTONOMOUS_RESEARCH)*

### AUTONOMOUS_RESEARCH Authority

All capabilities except CAP-18 (HUMAN_APPROVAL) and CAP-09 (SHARED_AUTHORITY) carry this authority class. Includes CAP-31. Hard boundary: does not extend to trade execution, order placement, order modification, or autonomous market action.

### SHARED_AUTHORITY

| Capability | Basis |
|-----------|-------|
| CAP-09 | System evaluates and flags; human reviews at CAP-18. SDM-04 Rule 4, SDM-06 Rule 4. |

### HUMAN_APPROVAL

| Capability | Basis |
|-----------|-------|
| CAP-18 | Human decision mandatory before any trade action. SDM-CONST-06. No bypass. |

### Prohibited Authorities — Absolute

No capability has been granted: trade execution, order placement, order modification, write authority from attribution to recommendation logic, autonomous market action.

---

## SECTION 7 — GOVERNANCE RELATIONSHIPS

### Halt State Governance

| Capability | State | Entry Authority | Exit Authority |
|-----------|-------|----------------|----------------|
| CAP-24 | Hard Deterministic Halt (State 4) | CAP-19 (limit breach) | Human acknowledgment + confirmed return within limits |
| CAP-25 | Governance Halt (State 1) | CAP-29 (drawdown ≥ 5%) | Explicit human resumption authorization |
| CAP-26 | Governance Lockout (State 2) | CAP-31 (violation signal) | CAP-31 (restoration signal) — automatic on compliance restoration |
| CAP-27 | Conditional Suspension (State 3) | CAP-23 (adverse conditions) | CAP-23 (condition clearance) — automatic |

### Attribution Governance

CAP-21 and CAP-22 are read-only. Their outputs are available for human review. No output may modify any capability's behavior without explicit human approval. (CONSTRAINT-07)

---

## SECTION 8 — ACTIVATION MODEL

*(Unchanged from SADR_V2)*

**Mode 1 — Scheduled:** Autonomous initiation on predefined schedules.
**Mode 2 — On-Demand:** Initiation upon explicit human request.
**Mode 3 — Event-Driven:** Initiation when governance, risk, or portfolio events trigger mandatory review.

No activation mode grants trade execution authority.

---

## SECTION 9 — VALIDATION REQUIREMENTS

*(Constitutional constraints unchanged. Evidence requirements updated for CAP-31.)*

### Constitutional Validation Constraints

| Constraint | Rule |
|-----------|------|
| K-fold prohibited in all statistical validation | SDM-03 Rule 1, SDM-05 Rule 2, SDM-07 Rule 3 |
| Data smoothing may not mask structural anomalies | SDM-05 Rule 7 |
| Statistical significance tests required for active trading approval | SDM-06 Rule 6 |
| Attribution may not write to recommendation logic | SDM-13 Rules 8, 10 |
| Halt state entry and exit logged with condition state | SDM-15 Rule 14 |

### Evidence Requirements

*(CAP-31 added)*

| Capability | Required Validation Evidence |
|-----------|----------------------------|
| CAP-02 | Cross-verification match/mismatch records |
| CAP-10 | Walk-forward validation bounds and OOS documentation |
| CAP-11 | Deflated return metrics or t-stat; stability index values |
| CAP-12 | Confidence computation records; source reliability weights |
| CAP-13 | Probability-adjusted return inputs; drawdown compliance gate logs |
| CAP-14 | Survivorship bias validation confirmation per opportunity |
| CAP-15 | Ranking logic execution logs proving non-equal-weighting |
| CAP-16 | Conviction weight justification per suggestion |
| CAP-17 | Null-state event logs |
| CAP-18 | Immutable record of all approvals, rejections, and overrides |
| CAP-21 | Attribution logs per trade cycle; system alpha records |
| CAP-22 | Human override delta records per trade cycle |
| CAP-24 | Halt entry and exit with portfolio compliance confirmation state |
| CAP-25 | Halt entry log; human resumption authorization record; halt exit log |
| CAP-26 | Lockout entry log (violation signal received); lockout exit log (restoration signal received) |
| CAP-27 | Suspension entry log with condition state; suspension exit log with condition state at exit |
| CAP-31 | Compliance evaluation event records; violation signal issuance records; restoration signal issuance records |

---

## SECTION 10 — DEFERRED DOMAIN REGISTER

*(Unchanged from SADR_V2)*

### SDM-14 | Research Intake

**Status:** DEFERRED. No capabilities derived. No architectural anticipation permitted without constitutional resolution.

---

## SECTION 11 — OPEN VALIDATION ITEMS

*(CHANGE-07 applied — 7 items reclassified)*

| VAL ID | Triage Class | Architecture Impact | Affected Capability |
|--------|-------------|--------------------|--------------------|
| VAL-01 | CLASS_C | None | CAP-04 |
| VAL-02 | CLASS_B | None | CAP-03 |
| VAL-03 | **CLASS_B** | None — generic signal interface sufficient | CAP-05, CAP-23, CAP-27 |
| VAL-04 | CLASS_C | None | CAP-10 |
| VAL-05 | **CLASS_A** | **BLOCKS CAP-08 ↔ CAP-12 interface** | CAP-08, CAP-12 |
| VAL-06 | CLASS_D | None | CAP-08 |
| VAL-07 | CLASS_B | None (requires VAL-05 first) | CAP-12 |
| VAL-08 | **CLASS_B** | None — regime context parameter sufficient | CAP-13, CAP-23 |
| VAL-09 | **CLASS_B** | None — extension point per SDM-CONST-12 sufficient | CAP-13, CAP-16, CAP-23 |
| VAL-10 | CLASS_C | None | CAP-15, CAP-20 |
| VAL-11 | CLASS_B | None (requires VAL-05 first) | CAP-16 |
| VAL-12 | **CLASS_B** | None — extension point per SDM-CONST-12 sufficient | CAP-16, CAP-23 |
| VAL-13 | CLASS_C | None | CAP-20 |
| VAL-14 | **CLASS_B** | None — regime context parameter sufficient | CAP-23, CAP-25 |
| VAL-15 | CLASS_B | None (requires VAL-05 first) | CAP-16, CAP-23 |
| VAL-16 | **CLASS_B** | None — extension point per SDM-CONST-12 sufficient | CAP-23 |
| VAL-17 | **CLASS_B** | None — generic signal interface sufficient; parallel to VAL-03 | CAP-05, CAP-23, CAP-27 |

**VAL-05 is the sole CLASS_A architecture blocker.** Architecture may proceed on all capabilities except the CAP-08 ↔ CAP-12 interface, which requires VAL-05 resolution by owner decision.

---

## SECTION 12 — CAPABILITY TRACEABILITY MATRIX

*(CHANGE-08 applied — CAP-31 added)*

| Cap ID | Capability Name | Primary SDM Source | Constitutional Invariant |
|--------|----------------|-------------------|--------------------------|
| CAP-01 | Market Data Ingestion | SDM-02 Rules 1, 2 | — |
| CAP-02 | Data Cross-Verification | SDM-02 Rule 2, SDM-05 Rule 1 | — |
| CAP-03 | Corporate Action Adjustment | SDM-02 Rule 3 | — |
| CAP-04 | Universe Eligibility Enforcement | SDM-02, SDM-CONST-03 | — |
| CAP-05 | Market Regime Classification | SDM-03 Rules 1–5 | — |
| CAP-06 | Concept Drift Detection | SDM-03 Rule 2, SDM-05 Rule 5, SDM-15 Rule 13 | — |
| CAP-07 | Technical Signal Generation | SDM-04 Rules 1, 7, 8, 9, 10 | Technicals Dominant |
| CAP-08 | Supplementary Signal Intake | SDM-04 Rules 3, 5, 6, 12 | News Supplementary |
| CAP-09 | Technical-News Conflict Evaluation | SDM-04 Rule 4, SDM-06 Rule 4 | — |
| CAP-10 | Walk-Forward Signal Validation | SDM-05 Rules 1, 2, 3 | — |
| CAP-11 | Statistical Edge Verification | SDM-05 Rules 4, 5, 6, 7 | — |
| CAP-12 | Confidence Scoring | SDM-06 Rules 1–6 | Probability-First |
| CAP-13 | Expected Value Computation | SDM-07 Rules 1, 2, 3, 5 | Capital Preservation, Probability-First |
| CAP-14 | Survivorship Bias Correction | SDM-02 Rule 1, SDM-07 Rule 4 | — |
| CAP-15 | Opportunity Ranking | SDM-08 Rules 1–5, 8 | Probability-First, 3–5 Position Model |
| CAP-16 | Conviction-Weighted Allocation | SDM-08 Rule 6, SDM-09 Rules 2–7 | Cash Is A Valid Position |
| CAP-17 | Null-State Declaration | SDM-01 Rule 1, SDM-08 Rule 7, SDM-CONST-11 | Cash Is A Valid Position |
| CAP-18 | Human Approval Gate | SDM-10, SDM-CONST-06, SDM-CONST-13 | Human Approval Required, Human-in-the-Loop |
| CAP-19 | Position Limit Enforcement | SDM-11 Rules 1, 3, 4, 6, 7, 8 | Capital Preservation |
| CAP-20 | Exit Condition Recommendation | SDM-12 Rules 1–5 | — |
| CAP-21 | Attribution Observation | SDM-13 Rules 1–4, 7 | — |
| CAP-22 | Human Override Delta Tracking | SDM-13 Rules 5–6 | — |
| CAP-23 | Risk Circuit Breaker Enforcement | SDM-15 Rules 6–12 | Risk Governance Framework |
| CAP-24 | Hard Deterministic Halt | SDM-CONST-14 State 4, SDM-11 Rule 6 | Risk Governance Framework |
| CAP-25 | Governance Halt | SDM-CONST-14 State 1, GOV-01 | Capital Preservation, Risk Governance Framework |
| CAP-26 | Governance Lockout | SDM-CONST-14 State 2, GOV-02 | Human-in-the-Loop |
| CAP-27 | Conditional Recommendation Suspension | SDM-CONST-14 State 3, SDM-15 Rule 14 | Risk Governance Framework |
| CAP-28 | System Activation Authority | SDM-CONST-15 | Scheduled/On-Demand/Event-Driven Activation |
| CAP-29 | Portfolio State Visibility | SDM-10 Human Visibility, SDM-11 Rules 1–8, SDM-09 Rules 6–7 | Capital Preservation |
| CAP-30 | Immutable Audit Log | SDM-02 through SDM-15 (all Audit clauses) | Human-in-the-Loop |
| CAP-31 | Governance Compliance Monitor | GOV-02 Rules 1, 3; SDM-CONST-14 State 2 | Human-in-the-Loop |

---

*End of SADR_V2.1.md*

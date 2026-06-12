# System Architecture Design Requirements (SADR_V1)

## Executive Summary
This document defines the foundational capabilities required to implement the Strategy Decision Model (SDM_V2.3) for the AI Swing Trading Research Analyst. It acts as the canonical capability specification bridging the frozen SDM constitution and future architecture design. As mandated by the Strategic Capability Derivation Authority (SCDF_PROTOCOL), this document dictates **what** the system must do, without dictating **how** it is implemented. Architecture, technology, infrastructure, and implementation methodologies are strictly excluded.

## Capability Catalog
The system is composed of the following atomic capabilities, consolidated to remove redundancy while preserving constitutional traceability:

*   **CAP-01: Eligibility Filtration** (SDM-02)
*   **CAP-02: Data Verification** (SDM-02, SDM-05)
*   **CAP-03: Regime Classification** (SDM-03, SDM-15)
*   **CAP-04: Concept Drift Detection** (SDM-03, SDM-05)
*   **CAP-05: Signal Extraction** (SDM-04)
*   **CAP-06: Conflict Resolution** (SDM-04, SDM-06)
*   **CAP-07: Statistical Validation** (SDM-05, SDM-06, SDM-07)
*   **CAP-08: Confidence Scoring** (SDM-06)
*   **CAP-09: Probability Estimation** (SDM-07, SDM-08)
*   **CAP-10: Sizing Calculation** (SDM-09, SDM-11)
*   **CAP-11: Risk Boundary Enforcement** (SDM-07, SDM-11, SDM-15)
*   **CAP-12: Human Authorization Interface** (SDM-01, SDM-10, GOV-01, GOV-02)
*   **CAP-13: State Halt Enforcement** (SDM-15, GOV-01, GOV-02)
*   **CAP-14: Exit Evaluation** (SDM-12)
*   **CAP-15: Expectancy Attribution** (SDM-13)

---

## Domain Capability Specifications

### SDM-01: Objective Selection
*   **Purpose:** Generate evidence-based recommendations maximizing probability-adjusted returns.
*   **Inputs:** Validated opportunities, Capital availability.
*   **Outputs:** Advisory recommendations or Explicit Null-State ("Hold Cash").
*   **Capabilities:** CAP-09 (Probability Estimation), CAP-12 (Human Authorization Interface).
*   **Dependencies:** SDM-07, SDM-08.

### SDM-02: Universe Selection
*   **Purpose:** Restrict operational universe exclusively to Indian Equities (NSE/BSE).
*   **Inputs:** Unfiltered market datasets.
*   **Outputs:** Eligible Equity Set.
*   **Capabilities:** CAP-01 (Eligibility Filtration - strictly including delisted assets), CAP-02 (Data Verification - cross-verifying >=2 sources, split adjustments).
*   **Dependencies:** None.

### SDM-03: Market Regime Classification
*   **Purpose:** Classify market environments to prevent model drift and inappropriate execution.
*   **Inputs:** Eligible Equity Set.
*   **Outputs:** Regime Classifications, Non-ergodicity Alerts.
*   **Capabilities:** CAP-03 (Regime Classification), CAP-04 (Concept Drift Detection).
*   **Dependencies:** SDM-02.

### SDM-04: Signal Discovery
*   **Purpose:** Discover opportunities prioritizing technical evidence over news.
*   **Inputs:** Eligible Equity Set, Regime Classifications.
*   **Outputs:** Raw Discovered Signals.
*   **Capabilities:** CAP-05 (Signal Extraction), CAP-06 (Conflict Resolution).
*   **Dependencies:** SDM-02, SDM-03.

### SDM-05: Signal Validation
*   **Purpose:** Ensure signal integrity, prevent overfitting, and verify statistical edge.
*   **Inputs:** Raw Discovered Signals.
*   **Outputs:** Validated Signals.
*   **Capabilities:** CAP-02 (Data Verification), CAP-04 (Concept Drift Detection), CAP-07 (Statistical Validation - walk-forward only).
*   **Dependencies:** SDM-04.

### SDM-06: Confidence Assessment
*   **Purpose:** Quantify reliability based on technical weight and supplementary news.
*   **Inputs:** Validated Signals.
*   **Outputs:** Confidence Scores.
*   **Capabilities:** CAP-06 (Conflict Resolution), CAP-07 (Statistical Validation), CAP-08 (Confidence Scoring).
*   **Dependencies:** SDM-05.

### SDM-07: Expected Value Assessment
*   **Purpose:** Evaluate opportunities based on probability-adjusted returns within drawdown limits.
*   **Inputs:** Confidence Scores.
*   **Outputs:** Probability Metrics, Drawdown Estimations.
*   **Capabilities:** CAP-07 (Statistical Validation), CAP-09 (Probability Estimation), CAP-11 (Risk Boundary Enforcement).
*   **Dependencies:** SDM-06, SDM-11.

### SDM-08: Opportunity Ranking
*   **Purpose:** Prioritize top 3-5 opportunities for human review via an open menu.
*   **Inputs:** Expected Value Metrics.
*   **Outputs:** Ranked Open Menu.
*   **Capabilities:** CAP-09 (Probability Estimation).
*   **Dependencies:** SDM-07.

### SDM-09: Capital Allocation
*   **Purpose:** Distribute capital based on conviction weights without forcing deployment.
*   **Inputs:** Ranked Open Menu.
*   **Outputs:** Recommended Sizing Metrics.
*   **Capabilities:** CAP-10 (Sizing Calculation).
*   **Dependencies:** SDM-08, SDM-11.

### SDM-10: Human Approval Gate
*   **Purpose:** Deterministic interception of recommendations requiring mandatory human action.
*   **Inputs:** Advisory Reports (Allocations, Rankings).
*   **Outputs:** Execution Authorization, Owner Overrides.
*   **Capabilities:** CAP-12 (Human Authorization Interface).
*   **Dependencies:** All prior SDM capabilities.

### SDM-11: Position Management
*   **Purpose:** Maintain portfolio-level limitations and concentration bounds.
*   **Inputs:** Active Portfolio State.
*   **Outputs:** Position Concentration Metrics, Drawdown Status.
*   **Capabilities:** CAP-10 (Sizing Calculation), CAP-11 (Risk Boundary Enforcement).
*   **Dependencies:** SDM-10.

### SDM-12: Exit Decision
*   **Purpose:** Recommend position closure evaluating Risk > Technical > Time parameters.
*   **Inputs:** Active Positions.
*   **Outputs:** Exit Recommendations.
*   **Capabilities:** CAP-14 (Exit Evaluation).
*   **Dependencies:** SDM-11.

### SDM-13: Attribution
*   **Purpose:** Prevent survivorship bias by tracking outcomes of both accepted and rejected setups.
*   **Inputs:** System Recommendations, Human Overrides, Market Outcomes.
*   **Outputs:** Attribution Metrics (System Alpha vs Human Delta).
*   **Capabilities:** CAP-15 (Expectancy Attribution).
*   **Dependencies:** SDM-10, SDM-12.

### SDM-15: Risk Governance
*   **Purpose:** Enforce deterministic limits, circuit breakers, and state halts.
*   **Inputs:** Market Events, Portfolio State.
*   **Outputs:** State Suspensions, Position Modifiers.
*   **Capabilities:** CAP-11 (Risk Boundary Enforcement), CAP-13 (State Halt Enforcement).
*   **Dependencies:** SDM-03, SDM-11.

### GOV-01: Governance Halt
*   **Purpose:** Enforce a hard block on new recommendations upon 5% drawdown breach.
*   **Inputs:** Portfolio Drawdown Metrics.
*   **Outputs:** Halt State 1.
*   **Capabilities:** CAP-13 (State Halt Enforcement), CAP-12 (Human Authorization Interface - for resumption).
*   **Dependencies:** SDM-11.

### GOV-02: Governance Lockout
*   **Purpose:** Halt the system if a human violates constitutional risk rules.
*   **Inputs:** Human Override Actions vs Baseline Controls.
*   **Outputs:** Halt State 2.
*   **Capabilities:** CAP-13 (State Halt Enforcement).
*   **Dependencies:** SDM-10, SDM-15.

---

## Dependency Graph
The sequential flow of capability dependence ensures data integrity and constitutional compliance prior to any human interface.

1.  **Upstream Primitives:** `SDM-02` (Universe)
2.  **Environment State:** `SDM-03` (Regime) -> depends on `SDM-02`
3.  **Discovery Chain:** `SDM-04` (Signal) -> `SDM-05` (Validation) -> `SDM-06` (Confidence) -> depends on `SDM-03`
4.  **Sizing & Risk Chain:** `SDM-07` (EV) -> `SDM-08` (Ranking) -> `SDM-09` (Allocation) -> depends on `SDM-06` & `SDM-11` (Position Limits)
5.  **Governance Layer (Orthogonal Interceptors):** `SDM-15`, `GOV-01`, `GOV-02` -> monitor `SDM-11` and `SDM-03` and can block `SDM-10`
6.  **Terminal Presentation:** `SDM-10` (Human Gate) -> depends on all chains.
7.  **Post-Execution Loop:** `SDM-12` (Exit), `SDM-13` (Attribution) -> depend on `SDM-10` and `SDM-11`.

---

## Authority Model
Every capability operates under strict authority boundaries to preserve the human-in-the-loop requirement.

*   **Autonomous Research Authority:** Permitted to execute data filtering, validation, math calculations, statistical measurements, signal generation, and ranking logic without human intervention. (SDM-02, SDM-03, SDM-04, SDM-05, SDM-06, SDM-07, SDM-08, SDM-09, SDM-15 suspensions).
*   **Human Approval Authority:** Absolute final authority required to act upon any recommendation, approve sizing, modify parameters, exit positions, or resume from Governance Halt. (SDM-01, SDM-10, SDM-11, SDM-12, GOV-01).
*   **Shared Authority (Read-Only):** Permitted to observe and log data, but possesses zero write authority to alter core logic based on findings. (SDM-13 Attribution).

---

## Validation Model
Validation criteria define how an architecture is proven to meet the capability requirement.

*   **Data Integrity Evidence:** Cross-verification match/mismatch logs across multiple sources; survivorship inclusion verification via delisted asset presence.
*   **Math & Logic Evidence:** Walk-forward cross-validation boundary reports (k-fold explicitly prohibited); explicit probability-adjusted rankings (equal-weighting prohibited).
*   **Risk Compliance Evidence:** Simulated drawdown logs proving recommendation cessation at 5% threshold; concentration limit scaling test outcomes.
*   **Authority Evidence:** Immutable logs demonstrating system halt prior to simulated execution attempts; human override delta measurements in attribution.

---

## Deferred Domains
*   **SDM-14: Research Intake** is DEFERRED due to insufficient definition in the authoritative corpus. No capabilities are defined or required for this domain.

---

## Capability Traceability Matrix

| Capability ID | Name | SDM Origin | Test Criteria |
| :--- | :--- | :--- | :--- |
| CAP-01 | Eligibility Filtration | SDM-02 | Verifies NSE/BSE constraint and delisted asset inclusion. |
| CAP-02 | Data Verification | SDM-02, SDM-05 | Checks multi-source OHLCV cross-validation logic. |
| CAP-03 | Regime Classification | SDM-03, SDM-15 | Evaluates market environment state. |
| CAP-04 | Concept Drift Detection | SDM-03, SDM-05 | Verifies deviation between walk-forward intervals. |
| CAP-05 | Signal Extraction | SDM-04 | Validates technical precedence in discovery. |
| CAP-06 | Conflict Resolution | SDM-04, SDM-06 | Evaluates technicals vs news weighting logic. |
| CAP-07 | Statistical Validation | SDM-05, SDM-06, SDM-07| Asserts walk-forward significance, prohibits k-fold. |
| CAP-08 | Confidence Scoring | SDM-06 | Verifies output scores reflect technical weighting. |
| CAP-09 | Probability Estimation | SDM-07, SDM-08 | Calculates EV bounded by 5% drawdown constraints. |
| CAP-10 | Sizing Calculation | SDM-09, SDM-11 | Verifies conviction weighting vs equal-weight. |
| CAP-11 | Risk Boundary Enforcement| SDM-07, SDM-11, SDM-15| Asserts strict 5% drawdown limits and concentration rules. |
| CAP-12 | Human Auth Interface | SDM-01, SDM-10, GOV-01| Validates advisory nature, blocks execution without approval. |
| CAP-13 | State Halt Enforcement | SDM-15, GOV-01, GOV-02| Tests explicit suspension states based on portfolio/human action.|
| CAP-14 | Exit Evaluation | SDM-12 | Asserts Risk > Technical > Time precedence in closure logic. |
| CAP-15 | Expectancy Attribution | SDM-13 | Verifies tracking of accepted and rejected setups independently. |

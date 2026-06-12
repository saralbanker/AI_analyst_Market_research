# SADR Risk Register
**Target:** SADR_V1.md

As per the SCDF_PROTOCOL, this risk register exclusively documents capability, dependency, and traceability risks. Architectural, technological, and implementation risks are strictly out of scope.

## 1. Missing Capability Risks

*   **RISK-CAP-01: Unresolved Validation Logic Dependencies**
    *   **Description:** Several capabilities (CAP-09 Probability Estimation, CAP-10 Sizing Calculation, CAP-11 Risk Boundary Enforcement, CAP-14 Exit Evaluation) depend on specific mathematical frameworks currently marked as `[VALIDATION_REQUIRED]` in the SDM (VAL-01 through VAL-17).
    *   **Impact:** The capability is defined, but the mathematical logic required to execute it remains undefined. Attempting to implement these capabilities without resolving the open validation items will result in arbitrary or unconstitutional behavior.
    *   **Mitigation:** Architecture cannot proceed for these specific sub-components until the foundational mathematics (e.g., non-ergodic VaR, NLP-to-Kelly fraction conversion) are provided.

*   **RISK-CAP-02: Deferred Intake Capability**
    *   **Description:** SDM-14 (Research Intake) is constitutionally DEFERRED. No capabilities exist to define how external human research or new ideas enter the system outside of standard market data feeds.
    *   **Impact:** The system currently possesses a closed analytical loop.
    *   **Mitigation:** Rely solely on Universe Selection (SDM-02) and Signal Discovery (SDM-04) until an amendment defines Research Intake.

## 2. Dependency Risks

*   **RISK-DEP-01: Linear Dependency Cascade to Human Gate**
    *   **Description:** SDM-10 (Human Approval Gate) acts as a terminal dependency for all analytical chains prior to execution.
    *   **Impact:** If an upstream capability (e.g., CAP-07 Statistical Validation or CAP-09 Probability Estimation) triggers a fault, enters an undefined state, or yields no data, the human gate receives a null state, effectively halting all portfolio motion.
    *   **Mitigation:** Ensure upstream capabilities possess robust null-state handling (as mandated by SDM-01) to inform the human owner of upstream processing failures rather than failing silently.

*   **RISK-DEP-02: Data Verification Dependency Squeeze**
    *   **Description:** CAP-02 (Data Verification) requires cross-verifying metrics across at least two independent sources before signal logic executes.
    *   **Impact:** If one data source fails, the dependency condition cannot be met, starving CAP-05 (Signal Extraction) and halting the entire system.
    *   **Mitigation:** Capability design must account for source degradation without violating the minimum two-source constitutional requirement.

*   **RISK-DEP-03: Attribution Read-Only Disconnect**
    *   **Description:** CAP-15 (Expectancy Attribution) tracks Human Override Delta vs. System Alpha but possesses no write authority to feedback into CAP-05 (Signal Extraction) or CAP-09 (Probability Estimation).
    *   **Impact:** Continuous improvement of the model based on attribution findings is entirely manual, heavily depending on the human owner acting upon the reports.
    *   **Mitigation:** No system mitigation allowed. This is an intended feature of the Human-in-the-Loop stricture.

## 3. Traceability Risks

*   **RISK-TRC-01: Slippage of Technical Evidence Priority**
    *   **Description:** CAP-08 (Confidence Scoring) must strictly weigh technical evidence over news. There is a risk that during mapping to implementation, sentiment scoring weights creep up and violate SDM-CONST-10.
    *   **Impact:** Loss of constitutional traceability and potential execution of low-probability trades driven by social sentiment.
    *   **Mitigation:** Implement strict boundary assertions on the maximum weight output of the News Sentiment Evaluator.

*   **RISK-TRC-02: "Cash is a Valid Position" Erosion**
    *   **Description:** CAP-09 (Probability Estimation) and CAP-10 (Sizing Calculation) must default to recommending cash if thresholds are missed (SDM-CONST-07).
    *   **Impact:** Overly aggressive sizing calculations might lower probability thresholds to avoid presenting a "Hold Cash" state to the user, breaking the capital preservation traceability.
    *   **Mitigation:** Treat Cash as a first-class citizen in the allocation open menu.

*   **RISK-TRC-03: Future Feature Creep Orphanage**
    *   **Description:** Any future functionality added to the system during architecture design that does not trace directly back to SADR_V1.md.
    *   **Impact:** Unconstitutional operation of the system.
    *   **Mitigation:** Strict enforcement of the rule: If it is not in the SADR, it cannot be architected.

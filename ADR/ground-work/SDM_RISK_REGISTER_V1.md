# SDM_RISK_REGISTER_V1
**Framework:** Forensic Audit & Enforcement Framework (FAEF)

---

## 1. Constitutional Risks
**Risk-C01: Absolute Non-Autonomy Conflict**
* **Description:** The constitutional rule prohibiting all autonomous broker actions (Gap-04) mathematically conflicts with the constitutional requirement for an aggregate portfolio-level hard risk halt (SDM-15).
* **Severity:** CRITICAL
* **Resolution Required:** The system must either be granted API authority specifically restricted to "Liquidation-Only Market Orders" during portfolio-level breaches, or the broker must natively support Account Equity Stop-Outs.

## 2. Dependency Risks
**Risk-D01: SDM-14 Black Box**
* **Description:** SDM-14 (Research Intake) remains deferred. There is no mapped dependency explaining how a downloaded PDF research report mathematically translates into the SDM-04 Signal logic.
* **Severity:** HIGH
* **Resolution Required:** The architecture phase must define the specific LLM parsing layer or manual intake form that structures unstructured research into tagged signals.

**Risk-D02: Stop-Loss Synchronization**
* **Description:** Pre-authorized stop-losses at the broker level (Gap-04) might drift from the SDM's internal representation if corporate actions (splits, dividends) occur. 
* **Severity:** MEDIUM
* **Resolution Required:** The SDM telemetry must constantly read the broker's active order book to verify the stop-loss remains valid.

## 3. Economic Risks
**Risk-E01: Portfolio Flash Crash Ruin**
* **Description:** Because portfolio-level halts cannot be autonomously executed (Risk-C01), a sudden non-ergodic correlation event (all positions dropping simultaneously without hitting individual stops) will breach the 5% portfolio risk limit while the system helplessly waits for the human to approve liquidation.
* **Severity:** CRITICAL
* **Resolution Required:** Resolve Risk-C01 immediately.

**Risk-E02: Gap Risk on Open**
* **Description:** Swing trading relies on holding assets overnight. Broker stop-losses do not guarantee execution at the stop price during a massive morning gap-down.
* **Severity:** HIGH
* **Resolution Required:** Max position sizing must mathematically assume a 10-15% adverse gap, ensuring that even if a stop is skipped, the sizing prevents total account ruin.

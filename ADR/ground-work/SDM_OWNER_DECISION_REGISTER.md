# SDM_OWNER_DECISION_REGISTER
**Status:** PENDING OWNER ADJUDICATION

The DGAF review has identified two final governance ambiguities that require explicit Owner adjudication, as they represent a direct conflict between Capital Preservation and Human Autonomy.

---

## DECISION-001: The Liquidation Exemption

**Context:** The SDM has a mandatory 5% portfolio drawdown limit. Currently, the SDM has ZERO autonomous execution authority (`ODP-001`). If a flash crash occurs, pre-authorized individual asset stop-losses may be skipped, causing the portfolio to drop 10%. Without autonomous execution authority, the SDM cannot issue a market-sell to halt the portfolio, resulting in catastrophic ruin.

**Options:**
* **ACCEPT Option A (The Liquidation Exemption):** Amend ODP-001. Grant the SDM the strict, narrow authority to autonomously execute *Market Sell Orders ONLY*, and *ONLY* when the 5% portfolio risk threshold is breached.
* **REJECT (The Synthetic Stop):** Maintain zero autonomy. Force the SDM to make individual entry stop-losses so tight that an aggregate 5% breach is mathematically impossible. This guarantees opportunity starvation and frequent stop-outs.

**Owner Verdict Required:** [ACCEPT / REJECT]

---

## DECISION-002: Behavioral Lockout Governance

**Context:** To protect against human psychological drift (revenge trading), the SDM must know how to react if the Human Operator manually cancels a pre-authorized stop-loss at the broker level, violating SDM-15 risk governance.

**Options:**
* **ACCEPT Option B (SDM Lockout):** If the SDM detects a human override that violates risk governance, the SDM algorithmically locks out and refuses to generate new signal discoveries or capital allocations until the existing risk is brought back into mathematical compliance.
* **REJECT (Passive Logging):** The SDM merely logs the human violation in the attribution matrix and continues supplying the operator with new trade ideas.

**Owner Verdict Required:** [ACCEPT / REJECT]

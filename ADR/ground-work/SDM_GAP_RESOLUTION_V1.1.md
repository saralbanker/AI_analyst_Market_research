# SDM_GAP_RESOLUTION_V1.1
**Framework:** Decision Constitutionalization Framework (DCF)
**Target:** SDM Gaps 01, 02, 03, 04
**Status:** Constitutional Amendment to SDM_V1.1

---

## GAP-01: CORRELATION CONTROL

**Problem:** 
Unchecked allocation can cause small-capital portfolios to suffer severe, correlated drawdowns if multiple positions share the same underlying sector or macro driver.

**Decision:** 
Enforce categorical sector diversity and aggregate portfolio heat limits.

**Constitutional Rule:** 
The SDM shall restrict concurrent capital allocation by strictly limiting the number of positions sharing an identical primary market sector and enforcing a maximum aggregate capital heat ceiling per sector.

**Rationale:** 
Small-capital swing trading requires explicit categorical exclusion to prevent correlated ruin, ensuring that a single localized market shock cannot mathematically breach the absolute portfolio drawdown limit.

**Affected SDM Domains:** 
* SDM-08 (Opportunity Ranking)
* SDM-09 (Capital Allocation)
* SDM-15 (Risk Governance)

**Validation Requirements:** 
SDM-02 (Universe Selection) must deterministically assign a primary sector/theme category to all eligible assets before they enter the signal pipeline.

**Future Scale Notes:** 
Scaling to larger capital bases or SaaS may require granular sub-industry and factor mapping to prevent false positives in sector categorization.

---

## GAP-02: ATTRIBUTION MVP (AMENDED V1.1)

**Problem:** 
Without a mechanism to isolate skill (alpha) from market luck (beta), and without evaluating the outcomes of both executed trades and rejected signals, the system cannot identify decaying edges or optimize decision quality, threatening 5-year survivability.

**Decision:** 
Establish a tag-based expectancy matrix tracking Profit Factor and theoretical outcomes against qualitative setup parameters for both Accepted and Rejected Opportunities.

**Constitutional Rule:** 
The SDM shall attribute and evaluate historical edge and decision quality exclusively by segmenting both real trade expectancy (from Accepted Opportunities) and theoretical expectancy (from Rejected Opportunities) across mandatory qualitative metadata tags: Setup Type, Market Regime Context, and Holding Duration.

**Rationale:** 
Provides a minimum viable learning loop focused on holistic Decision Quality Attribution. By tracking exactly which specific setups succeed or fail in specific environments—regardless of whether capital was deployed—the system avoids the survivor bias of only learning from executed trades, without requiring computationally massive institutional factor models.

**Affected SDM Domains:** 
* SDM-04 (Signal Discovery)
* SDM-13 (Attribution)

**Validation Requirements:** 
All signal generations, whether executed or ultimately rejected, must permanently inherit their generating metadata tags, and the system must maintain a closed loop linking both closed P&L and theoretical outcomes back to these tags.

**Future Scale Notes:** 
SaaS scaling enables cross-user anonymized aggregation of tagged setups to dynamically identify universal regime edges.

---

## GAP-03: CONFIDENCE VS EXPECTED VALUE

**Problem:** 
A conflict of logic exists when a highly confident qualitative narrative contradicts a statistically poor mathematical expected value.

**Decision:** 
Expected Value serves as a binary filter; Confidence serves as a continuous allocation sizer.

**Constitutional Rule:** 
The SDM shall utilize mathematical Expected Value strictly as a binary filter for trade qualification, while utilizing qualitative Confidence and Conviction strictly as continuous scalars for capital sizing, capped by asset volatility.

**Rationale:** 
Ensures that mathematically negative expectancy trades are unconditionally rejected (protecting the "Probability-First" philosophy), while maximizing capital deployment velocity on setups supported by strong narrative and technical convergence.

**Affected SDM Domains:** 
* SDM-06 (Confidence Assessment)
* SDM-07 (Expected Value Assessment)
* SDM-08 (Opportunity Ranking)
* SDM-09 (Capital Allocation)

**Validation Requirements:** 
SDM-07 must be restricted to producing binary qualification outputs, while SDM-06 must be restricted to producing relative fractional scalars.

**Future Scale Notes:** 
None required.

---

## GAP-04: HUMAN OVERRIDE BOUNDARIES

**Problem:** 
Absolute human authority creates fatal latency risks during flash crashes, but allowing the SDM to execute risk halts autonomously violates the system's foundational identity as a non-autonomous research analyst.

**Decision:** 
Pre-Authorized Conditional Exits and Critical Escalation.

**Constitutional Rule:** 
The SDM possesses absolute zero autonomous market execution authority. The SDM shall govern catastrophic risk by mandating that human operators pre-authorize conditional broker-level stop-losses during the entry approval phase, and by issuing Critical Escalation alerts and capital-deployment lockouts when portfolio-level risk thresholds are breached.

**Rationale:** 
Protects the "Human-in-the-Loop" prime directive while delegating latency-sensitive flash-crash protection to the execution broker via human pre-authorization, ensuring the SDM remains strictly a research and decision-generation engine.

**Affected SDM Domains:** 
* SDM-10 (Human Approval)
* SDM-15 (Risk Governance)

**Validation Requirements:** 
SDM-10 must output explicit, mathematically defined stop-loss parameters alongside every entry recommendation, treating the entry and the conditional exit as an inseparable approval package.

**Future Scale Notes:** 
Critical Escalation alert telemetry must be rigorously verified to prevent notification failure.


Summary of the investigation before the full document: All four authorities were read in full. The 31 SADR capabilities group into 11 architectural domains under three evidence tests (constitutional rooting, information cohesion, authority cohesion) — every capability assigned exactly once, none invented, split, or renamed. The load-bearing findings: the only apparent dependency cycle (Portfolio State → Synthesis → Human Gate → Portfolio State) is broken at the system boundary by the human executing externally, so the internal graph is acyclic; all four halt states gate recommendation issuance only, never monitoring/reporting/audit (provable from GOV-01 Rule 4, GOV-02 Rule 3, SDM-15 Rule 14); governance detection carries a continuity requirement that no activation mode alone satisfies — recorded as a binding constraint, not a design; and GOV-VAL05's advisory-only sentiment ruling becomes a hard prohibited-dependency edge (DOM-03 supplementary signals → any computation). SDM-14 stays untouched. All four readiness checks pass.

---
ARCHITECTURE_FOUNDATION_V1

Architecture Foundation — Pre-Design Structural Truth

Derived From:
- SDM_V2.3 (FROZEN — FINAL CANONICAL), as amended by OWNER_DECISION_AMENDMENT_VAL-05 (GOV-VAL05)
- SADR_V2.1 (CERTIFIED), as amended by SADR_AMENDMENT_VAL-05
- VAL-05 OWNER DECISION RESOLUTION (RESOLVED — Option B, advisory-only)
- SDM_FREEZE_CERTIFICATION (FREEZE APPROVED — all twelve checks PASS)

Status: DRAFT FOR OWNER REVIEW — contains no architecture decisions
Scope: Defines the architectural domains, authority boundaries, information ownership, dependency structure, and interaction models from which architecture may later be derived. Technology-neutral. No services, databases, APIs, schemas, workflows, agents, queues, or infrastructure are defined or implied.

Method: Every domain, boundary, and ownership claim below is traced to an SDM clause, a SADR capability specification, or GOV-VAL05. Nothing is invented. Where the sources are silent, this document records the silence rather than filling it.

---
SECTION-01 — SYSTEM CONTEXT

1.1 The System Boundary

The system is an AI Swing Trading Research Analyst (SDM-CONST-01). Everything inside the boundary is advisory research, analysis, monitoring, attribution, reporting, and governance (SDM-CONST-15). Everything that touches a market — order placement, modification, cancellation, execution — is outside the boundary without exception (SDM-CONST-06, GOV-01 Rule 1).

1.2 External Actors

Actor: Human Owner / Operator
Constitutional Role: Sole trade execution actor. Sole approval authority (CAP-18). On-demand
  activation requester (SDM-CONST-15 Mode 2). Exit authority for Governance Halt (GOV-01
  Rule 5) and acknowledgment authority for Hard Deterministic Halt (SDM-CONST-14 State 4).
  Corrective actor for Governance Lockout restoration (GOV-02 Rule 3). Approval authority
  for any attribution-driven behavior change (SDM-13 Rule 9). Decision authority for
  remaining open validation items and any future SDM-14 resolution.
Source: SDM-CONST-06, SDM-10, SDM-CONST-14, GOV-01, GOV-02, SDM-13

The Human Owner is the only external actor. No other human role, user class, or operator tier is defined in any authoritative source. (SDM-CONST-04 names "Optional SaaS" as a future scale target only; no SaaS actor exists constitutionally today and none may be anticipated architecturally beyond the modularity requirement of SDM-CONST-12.)

1.3 External Systems and Information Sources

┌───────────────────────────┬────────────────────────────────────────┬─────────────────┐
│      External Source      │  What Crosses the Boundary (Inbound)   │     Source      │
├───────────────────────────┼────────────────────────────────────────┼─────────────────┤
│ Market data providers —   │ OHLCV price and volume data for Indian │ SDM-02 Rules    │
│ at least two independent  │  equities (NSE/BSE), historical data   │ 1–2, CAP-01     │
│ sources                   │ inclusive of delisted equities         │                 │
├───────────────────────────┼────────────────────────────────────────┼─────────────────┤
│ Corporate action record   │ Splits, de-merger records              │ SDM-02 Rule 3,  │
│ sources                   │                                        │ CAP-03          │
├───────────────────────────┼────────────────────────────────────────┼─────────────────┤
│ News and event sources    │ News data, earnings surprise events,   │ SDM-04 Rules 3, │
│                           │ insider buying events                  │  5, CAP-08      │
├───────────────────────────┼────────────────────────────────────────┼─────────────────┤
│ Authoritative record of   │ Confirmation of trades the human       │ CAP-29 Inputs   │
│ executed trade actions    │ actually executed, used for portfolio  │ (CHANGE-05)     │
│                           │ state accuracy verification            │                 │
└───────────────────────────┴────────────────────────────────────────┴─────────────────┘

External System: Broker / execution venue
Relationship: Entirely outside the boundary. The system holds zero interface authority
  toward it: no order placement, no order modification, no liquidation, under any
  circumstance including Governance Halt and Governance Lockout. The human alone interacts
  with it.
Source: GOV-01 Rule 1, GOV-02 Rules 4–5, CONSTRAINT-01

1.4 External Authority Holders

- The Human Owner holds all execution authority, all final trade decision authority, and all halt-resumption authority that is human-gated.
- No external system holds authority. Data sources are informational only; no single source is trusted — cross-verification across two independent sources is a hard blocking gate before any signal logic (SDM-02 Rule 2, SDM-05 Rule 1, CAP-02).

1.5 Outbound Boundary Crossings

The only things that leave the system are advisory artifacts presented to the human: advisory reports, opportunity rankings, allocation suggestions, null-state declarations, exit suggestions, conflict flags, halt-state alerts, escalation reports, attribution reports, and audit records for human review. No output constitutes an executable trade order (SDM-CONST-13).

1.6 Explicitly Outside Scope

- Trade execution and order management (constitutionally prohibited, not merely deferred)
- All markets other than Indian Equities NSE/BSE (SDM-CONST-03)
- SDM-14 Research Intake — DEFERRED; its boundary is undefined and no architectural anticipation is permitted (SADR Section 10)

---
SECTION-02 — ARCHITECTURAL DOMAINS

2.0 Derivation Method

Domains were derived from the SADR capability catalog using three evidence tests, applied in order:

1. Constitutional rooting — capabilities sharing the same SDM decision rule(s) as their primary source belong together unless test 2 or 3 separates them.
2. Information cohesion — capabilities that jointly produce and own a single class of information belong together.
3. Authority cohesion — a capability whose authority class or constitutional independence differs from its neighbors (e.g., CAP-18 HUMAN_APPROVAL; the four constitutionally independent halt states) must not be absorbed into a domain that would dilute that distinction.

Eleven domains result. All 31 capabilities are assigned exactly once. No capability is split, merged, renamed, or invented. SADR capability boundaries are preserved verbatim inside each domain.

┌────────────────────────────────┬─────────────────────────────────────────────┬───────┐
│             Domain             │                Capabilities                 │ Count │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-01 Market Data Foundation  │ CAP-01, CAP-02, CAP-03, CAP-04, CAP-14      │ 5     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-02 Market Context          │ CAP-05, CAP-06                              │ 2     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-03 Evidence Generation     │ CAP-07, CAP-08, CAP-09                      │ 3     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-04 Statistical Validation  │ CAP-10, CAP-11                              │ 2     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-05 Recommendation          │ CAP-12, CAP-13, CAP-15, CAP-16, CAP-17,     │ 6     │
│ Synthesis                      │ CAP-20                                      │       │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-06 Risk & Governance       │ CAP-19, CAP-23, CAP-24, CAP-25, CAP-26,     │ 7     │
│ Enforcement                    │ CAP-27, CAP-31                              │       │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-07 Human Decision          │ CAP-18                                      │ 1     │
│ Authority                      │                                             │       │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-08 Attribution             │ CAP-21, CAP-22                              │ 2     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-09 Portfolio State         │ CAP-29                                      │ 1     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-10 Audit                   │ CAP-30                                      │ 1     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ DOM-11 Activation              │ CAP-28                                      │ 1     │
├────────────────────────────────┼─────────────────────────────────────────────┼───────┤
│ Total                          │                                             │ 31    │
└────────────────────────────────┴─────────────────────────────────────────────┴───────┘

---
DOM-01 — Market Data Foundation

Purpose: Produce the verified, adjusted, eligible, survivorship-bias-corrected market dataset that all downstream evidence and probability logic is constitutionally required to consume — and block everything downstream until that dataset exists.

Owned Capabilities: CAP-01 (Market Data Ingestion), CAP-02 (Data Cross-Verification), CAP-03 (Corporate Action Adjustment), CAP-04 (Universe Eligibility Enforcement), CAP-14 (Survivorship Bias Correction).

Grouping Evidence: All five are rooted in SDM-02 (CAP-14 additionally in SDM-07 Rule 4, but its function — dataset correction — is data preparation, and SADR Section 5 routes its output as a dataset to CAP-13). They form the contiguous head of the SADR dependency chain and jointly own one class of information: market datasets. CAP-02 is the constitutionally mandated blocking gate within this domain (SDM-02 Rule 2, SDM-05 Rule 1).

Authority Type: AUTONOMOUS_RESEARCH (all five).

Information Owned: Raw market data; cross-verification match/mismatch records; split-adjusted data and rejection records for unadjustable data; the eligible equity set; eligible-vs-filtered counts; exclusion logs with triggered filter rules; the survivorship-bias-corrected historical dataset.

---
DOM-02 — Market Context

Purpose: Classify the market environment, detect structural shifts and model drift, and emit the condition signals (trend filter state, regime context, non-ergodic condition signal) that other domains are constitutionally required to consume.

Owned Capabilities: CAP-05 (Market Regime Classification), CAP-06 (Concept Drift Detection).

Grouping Evidence: Both rooted in SDM-03 (CAP-06 also SDM-15 Rule 13). CAP-06 consumes CAP-05's classification directly (SADR Section 5). Together they own one information class: market-context state and its stability.

Authority Type: AUTONOMOUS_RESEARCH.

Information Owned: Current market regime classification; regime shift alerts; broad market trend filter state; non-ergodic condition signal (generic condition-signal interface per VAL-03/VAL-17 CLASS_B resolution); concept drift metrics; model anchoring detection events; walk-forward cross-validation bounds.

---
DOM-03 — Evidence Generation

Purpose: Generate the two constitutional evidence layers — technical (primary) and supplementary news (advisory) — and detect and characterize conflicts between them for the human's benefit.

Owned Capabilities: CAP-07 (Technical Signal Generation), CAP-08 (Supplementary Signal Intake), CAP-09 (Technical-News Conflict Evaluation).

Grouping Evidence: All rooted in SDM-04 (CAP-09 also SDM-06 Rule 4). CAP-09 exists solely to relate CAP-07's and CAP-08's outputs. The Technicals-Dominant / News-Supplementary invariant is a relationship between these capabilities and is preserved only if they share a boundary that encodes it.

Authority Type: Mixed — CAP-07 and CAP-08 AUTONOMOUS_RESEARCH; CAP-09 SHARED_AUTHORITY (system evaluates and flags; human reviews and decides at CAP-18). The domain's autonomous authority does not absorb CAP-09's shared classification.

Information Owned: Technical signal set with evidence and quality metadata; supplementary signal set with source reliability metadata; conflict detection results, conflict flags, evidence characterization, and resolution rationale.

GOV-VAL05 Boundary (binding): The supplementary signal set routes only to the human-facing advisory report assembled for CAP-18. It does not enter CAP-12 or any downstream computation. The conflict flag from CAP-09 flows to CAP-12 as advisory annotation on the score output — never as a computational input that modifies the score. (GOV-VAL05 Rules 1–4; SADR_AMENDMENT_VAL-05.)

---
DOM-04 — Statistical Validation

Purpose: Verify statistical edge and temporal integrity of candidate signals before any confidence or recommendation logic may consume them.

Owned Capabilities: CAP-10 (Walk-Forward Signal Validation), CAP-11 (Statistical Edge Verification).

Grouping Evidence: Both rooted in SDM-05. Sequential within the SADR chain (CAP-10 → CAP-11), jointly owning one information class: validation verdicts. CAP-10 is a constitutional blocking gate (SDM-05 Rule 2: walk-forward mandatory, K-fold prohibited).

Authority Type: AUTONOMOUS_RESEARCH.

Information Owned: Walk-forward validation results and scores; validated signal set; rejected signals with rejection basis; statistical edge verdicts; deflated return metrics / significance test results; stability index values; outlier detection verification records.

---
DOM-05 — Recommendation Synthesis

Purpose: Transform validated technical evidence plus portfolio state into the complete advisory recommendation package: confidence scores, expected value, rankings, conviction-weighted allocations, exit suggestions, and the explicit null-state when nothing qualifies.

Owned Capabilities: CAP-12 (Confidence Scoring), CAP-13 (Expected Value Computation), CAP-15 (Opportunity Ranking), CAP-16 (Conviction-Weighted Allocation), CAP-17 (Null-State Declaration), CAP-20 (Exit Condition Recommendation).

Grouping Evidence: CAP-12/13/15/16/17 are the contiguous SDM-06 → SDM-07 → SDM-08 → SDM-09 → SDM-01 recommendation pipeline in SADR Section 5. CAP-20 is included because SDM-CONST-11 makes the exit suggestion a mandatory component of every recommendation, and CAP-20's output flows into the same advisory package presented at CAP-18 (SADR Section 5). Its information class is a recommendation, not a portfolio state or an enforcement signal. (Considered alternative: grouping CAP-20 with CAP-19 as "position monitoring" — rejected because CAP-19's output class is enforcement triggering (hard halt trigger, scaling signal) while CAP-20's output class is an advisory recommendation requiring human approval; their SDM sources (SDM-11 vs SDM-12) and output types both separate them.)

Authority Type: AUTONOMOUS_RESEARCH.

Information Owned: Confidence scores (derived exclusively from technical evidence and statistical validation per GOV-VAL05 Rule 1) with conflict-flag annotations; probability-adjusted return and downside drawdown estimates; the EV-filtered opportunity set; cash-holding signal; ranked opportunity list (3–5 target); conviction-weighted allocation suggestions with justification; explicit "Hold Cash" statements; null-state declarations; exit condition recommendations with extension justifications and transaction cost estimates. Collectively: Recommendations.

---
DOM-06 — Risk & Governance Enforcement

Purpose: Detect risk and governance conditions, manage the four constitutionally independent halt states, and gate recommendation authority accordingly — while holding zero execution authority.

Owned Capabilities:
- Detection: CAP-19 (Position Limit Enforcement), CAP-23 (Risk Circuit Breaker Enforcement), CAP-31 (Governance Compliance Monitor)
- Halt-state management: CAP-24 (Hard Deterministic Halt — State 4), CAP-25 (Governance Halt — State 1), CAP-26 (Governance Lockout — State 2), CAP-27 (Conditional Recommendation Suspension — State 3)

Grouping Evidence: All seven trace to the Risk Governance Framework invariant cluster: SDM-CONST-14, SDM-15, SDM-11 Rule 6 (hard halts, not passive alerts), GOV-01, GOV-02. SADR Section 7 binds each detector to its halt state as entry/exit authority: CAP-19 → CAP-24; CAP-23 → CAP-27 (entry and automatic exit); CAP-31 → CAP-26 (entry and automatic exit); CAP-29 → CAP-25 (CAP-29 itself remains in DOM-09 — it is a state provider, not an evaluator, per CHANGE-01). The detector/state-manager split inside this domain mirrors SADR boundaries exactly and must be preserved by any derived architecture.

Authority Type: AUTONOMOUS_RESEARCH — with the constitutional ceiling that every halt state governs recommendation authority only; none grants execution authority (SDM-CONST-14).

Information Owned: Governance State — the four independent halt-state flags with entry/exit condition records; position and concentration limit compliance status; circuit breaker detection signals (scaling, suspension, margin restriction, margin audit status); governance violation and restoration signals; compliance evaluation event records; critical risk escalation report content (GOV-01 Rule 4); human-visible breach alerts.

Independence Constraint (binding): The four halt states are constitutionally independent — distinct triggers, distinct effects, distinct exits; simultaneously activatable; restoration of one never restores another. A recommendation is permissible only if no currently active state blocks it. (SDM-CONST-14; SADR Section 5 "Halt State Independence.") No derived architecture may merge the four states into a single state machine that erases this independence.

---
DOM-07 — Human Decision Authority

Purpose: Present the complete advisory package as a simultaneous Open Menu and hold the single, bypass-proof gate at which the human — and only the human — authorizes any trade action.

Owned Capabilities: CAP-18 (Human Approval Gate).

Grouping Evidence: CAP-18 is the only HUMAN_APPROVAL capability (SADR Section 6). Authority cohesion (test 3) forbids merging it into any autonomous domain. It is the sole constitutional choke point: "CAP-18 blocks all trade action — no exceptions, no bypass" (SADR Section 5).

Authority Type: HUMAN_APPROVAL. The system's authority here is presentation only; decision authority is entirely human.

Information Owned: Human approval decisions; human override parameters; case-by-case evaluation triggers (system/human disagreement, SDM-10 Rule 4); secondary authorization events for algorithmic pricing limit modifications (SDM-10 Rule 5). The decisions themselves are human-owned facts; the gate owns their faithful capture and onward provision (to DOM-08, DOM-09 update pathway, DOM-10).

Presentation Constraint (binding): All EV-filtered, positively-ranked opportunities are presented simultaneously as an Open Menu; sequential forced selection is prohibited; no timeout-based auto-approval; no bypass pathways (SDM-08 Rule 8, CONSTRAINT-09, CAP-18 Boundary).

---
DOM-08 — Attribution

Purpose: Observe decision quality across accepted and rejected opportunities, maintain System Alpha and Human Override Delta as distinct layers, and report insights to the human — with no write authority over anything.

Owned Capabilities: CAP-21 (Attribution Observation), CAP-22 (Human Override Delta Tracking).

Grouping Evidence: Both rooted in SDM-13; both post-gate, read-only (SADR Section 5); both bounded by CONSTRAINT-07.

Authority Type: AUTONOMOUS_RESEARCH, restricted to Observation Authority only (SDM-13). No write authority over signal, validation, confidence, EV, ranking, allocation, or governance logic. Any behavior change motivated by attribution findings requires explicit human approval (SDM-13 Rule 9).

Information Owned: Attribution Records — System Alpha (Baseline) layer; Human Override Delta (Human Alpha/Bleed) layer, distinct per SDM-13 Rule 5; theoretical expectancy records for rejected opportunities; tracking metadata (setup type, regime context, holding duration); attribution reports, insights, and warnings for human review.

---
DOM-09 — Portfolio State

Purpose: Maintain and provide the system's authoritative representation of portfolio state — sourced exclusively from human-approved, externally executed trade actions — to every domain constitutionally entitled to it.

Owned Capabilities: CAP-29 (Portfolio State Visibility).

Grouping Evidence: SADR classifies CAP-29 as cross-cutting; it serves eight consumers across five domains (CAP-13, CAP-15, CAP-16, CAP-18, CAP-19, CAP-20, CAP-25, CAP-31). Information cohesion (test 2): it is the sole owner of one information class consumed by many. Absorbing it into any consumer domain would create hidden coupling among the others. CHANGE-01 explicitly stripped compliance evaluation from it — it provides state; it does not judge state.

Authority Type: AUTONOMOUS_RESEARCH (state maintenance and provision only). The system has no write authority over the actual portfolio (CONSTRAINT-01); state changes originate only from human-confirmed trade actions verified against the authoritative external execution record (CAP-29 Inputs).

Information Owned: Portfolio State — active position count; current drawdown level against the 5% tolerance; position concentration status; illiquidity metrics.

---
DOM-10 — Audit

Purpose: Hold the immutable, constitution-mandated record of everything: every system decision, human decision, override, halt entry/exit with condition state, validation result, conflict resolution, recommendation, activation, and compliance evaluation.

Owned Capabilities: CAP-30 (Immutable Audit Log).

Grouping Evidence: Cross-cutting per SADR; every SDM decision domain SDM-02 through SDM-15 carries an Audit clause discharged here. Its boundary — "recording only; does not process events; does not feed back into any capability" — forbids co-location with any producer.

Authority Type: AUTONOMOUS_RESEARCH (recording only).

Information Owned: Audit Records — the immutable audit trail; per-domain records per each SDM Audit clause; the immutable record of original system recommendation versus final human action (SDM-10 Audit).

---
DOM-11 — Activation

Purpose: Initiate research/analysis/monitoring/attribution/reporting/governance cycles under the three constitutionally authorized modes, and record which mode initiated each cycle.

Owned Capabilities: CAP-28 (System Activation Authority).

Grouping Evidence: Sole capability rooted in SDM-CONST-15. It sits before the head of the dependency chain (SADR Section 5) and owns one information class: activation events.

Authority Type: AUTONOMOUS_RESEARCH — explicitly bounded: no activation mode grants trade execution authority (SDM-CONST-15, CONSTRAINT-10).

Information Owned: Activation events (mode, trigger, initiated cycle) as recorded to audit.

---
SECTION-03 — AUTHORITY BOUNDARY MODEL

3.1 Authority Classes (from SADR Section 6 — preserved unchanged)

Class: AUTONOMOUS_RESEARCH
Holder: System
Scope: Research, analysis, monitoring, attribution, reporting, governance — under the three
  activation modes. Hard ceiling: never trade execution, order placement, order
  modification, or autonomous market action.
────────────────────────────────────────
Class: SHARED_AUTHORITY
Holder: System + Human
Scope: System evaluates and flags; human reviews and decides. CAP-09 only.
────────────────────────────────────────
Class: HUMAN_APPROVAL
Holder: Human
Scope: Mandatory human decision before any trade action. CAP-18 only. No bypass.

3.2 Per-Domain Authority Assignment

Domain: DOM-01 Market Data Foundation
AI (Autonomous) Authority: Ingest, verify, adjust, filter, correct data
Human Authority: — (visibility of counts/flags only)
Shared Authority: —
────────────────────────────────────────
Domain: DOM-02 Market Context
AI (Autonomous) Authority: Classify, detect drift, alert
Human Authority: — (visibility of regime/alerts only)
Shared Authority: —
────────────────────────────────────────
Domain: DOM-03 Evidence Generation
AI (Autonomous) Authority: Generate technical and supplementary signals
Human Authority: Decide on flagged conflicts (exercised at CAP-18)
Shared Authority: CAP-09: system flags conflict; human decides
────────────────────────────────────────
Domain: DOM-04 Statistical Validation
AI (Autonomous) Authority: Validate, verify edge, reject signals
Human Authority: —
Shared Authority: —
────────────────────────────────────────
Domain: DOM-05 Recommendation Synthesis
AI (Autonomous) Authority: Compute, rank, allocate, declare null-state, recommend exits
Human Authority: — (all outputs are advisory inputs to the human)
Shared Authority: —
────────────────────────────────────────
Domain: DOM-06 Risk & Governance Enforcement
AI (Autonomous) Authority: Detect conditions; enter/maintain halt states; auto-exit States 2
  and 3 on detected condition clearance
Human Authority: Exit State 1 (explicit resumption authorization, GOV-01 Rule 5); exit State
  4 (acknowledgment + confirmed return within limits); perform the corrective action that
  enables State 2 restoration
Shared Authority: State 2 exit is shared in substance: human corrects the violation; system
  detects restoration automatically (GOV-02 Rule 3)
────────────────────────────────────────
Domain: DOM-07 Human Decision Authority
AI (Autonomous) Authority: Present the package (presentation only)
Human Authority: Approve, reject, override, modify — final authority over all trade
  decisions (SDM-CONST-06, SDM-10 Rule 3); secondary authorization for pricing limit changes
   (SDM-10 Rule 5)
Shared Authority: —
────────────────────────────────────────
Domain: DOM-08 Attribution
AI (Autonomous) Authority: Observe, measure deltas, report insights
Human Authority: Approve any behavior change motivated by findings (SDM-13 Rule 9)
Shared Authority: —
────────────────────────────────────────
Domain: DOM-09 Portfolio State
AI (Autonomous) Authority: Maintain and provide state representation
Human Authority: Cause all actual portfolio change (via external execution)
Shared Authority: —
────────────────────────────────────────
Domain: DOM-10 Audit
AI (Autonomous) Authority: Record immutably
Human Authority: Consume for review
Shared Authority: —
────────────────────────────────────────
Domain: DOM-11 Activation
AI (Autonomous) Authority: Initiate Modes 1 and 3 autonomously
Human Authority: Initiate Mode 2 (explicit request)
Shared Authority: —

3.3 Anti-Leakage Verification

Authority leakage is forbidden. The following checks hold across all eleven domains:

1. No execution leakage: No domain holds any authority toward the broker/market. Halt states govern recommendation authority only (SDM-CONST-14). Governance enforcement is explicitly non-executing (GOV-01 Rule 1, GOV-02 Rules 4–5). Activation grants no execution authority (SDM-CONST-15). ✅
2. No attribution write leakage: DOM-08 has no write edge to any logic in DOM-01 through DOM-06 (CONSTRAINT-07, SDM-13 Rules 8, 10). ✅
3. No audit feedback leakage: DOM-10 has no output edge to any capability (CAP-30 Boundary). ✅
4. No sentiment computational leakage: DOM-03's supplementary signals reach computation nowhere; they reach the human only (GOV-VAL05 Rules 1–4). ✅
5. No portfolio write leakage: DOM-09 represents state; it never originates it (CONSTRAINT-01). ✅
6. No gate bypass: Every trade-action pathway passes through DOM-07; no domain emits anything executable (SADR Section 5 blocking gates; SDM-CONST-13). ✅

---
SECTION-04 — INFORMATION OWNERSHIP MODEL

One owner per information class. Owners are the sole producers; all other domains are read-only consumers via the dependency edges in SECTION-05.

Information Class: Market datasets (raw, verified, adjusted, eligible, bias-corrected)
Owner: DOM-01
Producers (within owner): CAP-01..04, CAP-14
Constitutionally Entitled Consumers: DOM-02, DOM-03, DOM-04, DOM-05 (CAP-13 via
  bias-corrected history)
Notes: Unverified data may reach no signal logic (SDM-02 Rule 2)
────────────────────────────────────────
Information Class: Market context state (regime, trend filter, drift, non-ergodic condition
  signal)
Owner: DOM-02
Producers (within owner): CAP-05, CAP-06
Constitutionally Entitled Consumers: DOM-03 (CAP-07), DOM-05 (CAP-13 regime context), DOM-06
  (CAP-23, CAP-27), human (alerts)
Notes:
────────────────────────────────────────
Information Class: Signals — technical
Owner: DOM-03
Producers (within owner): CAP-07
Constitutionally Entitled Consumers: DOM-04 (validation), DOM-03 (CAP-09)
Notes:
────────────────────────────────────────
Information Class: Signals — supplementary (news/sentiment)
Owner: DOM-03
Producers (within owner): CAP-08
Constitutionally Entitled Consumers: DOM-03 (CAP-09); human only thereafter, via the CAP-18
  advisory report
Notes: GOV-VAL05: advisory-only; never a computational input
────────────────────────────────────────
Information Class: Conflict flags and characterization
Owner: DOM-03
Producers (within owner): CAP-09
Constitutionally Entitled Consumers: DOM-05 (CAP-12, as annotation only), DOM-07 (human
  visibility pre-gate)
Notes: Annotation, not modification
────────────────────────────────────────
Information Class: Validation verdicts and edge evidence
Owner: DOM-04
Producers (within owner): CAP-10, CAP-11
Constitutionally Entitled Consumers: DOM-05 (CAP-12)
Notes:
────────────────────────────────────────
Information Class: Recommendations (confidence, EV, rankings, allocations, null-state, exit
  suggestions)
Owner: DOM-05
Producers (within owner): CAP-12, 13, 15, 16, 17, 20
Constitutionally Entitled Consumers: DOM-07 (presentation), DOM-08 (post-gate observation),
  DOM-10
Notes: Advisory only; never executable (SDM-CONST-13)
────────────────────────────────────────
Information Class: Portfolio State
Owner: DOM-09
Producers (within owner): CAP-29
Constitutionally Entitled Consumers: DOM-05 (CAP-13, 15, 16, 20), DOM-06 (CAP-19, 25, 31),
  DOM-07 (CAP-18 drawdown display)
Notes: Underlying truth originates with the human's executed trades; DOM-09 owns the
  representation
────────────────────────────────────────
Information Class: Governance State (four halt-state flags, entry/exit records, compliance
  signals, limit status)
Owner: DOM-06
Producers (within owner): CAP-19, 23, 24, 25, 26, 27, 31
Constitutionally Entitled Consumers: DOM-05 (gating effect on issuance), DOM-07 (active halt
  states displayed at gate), DOM-11 (event-driven triggers), DOM-10, human (alerts)
Notes:
────────────────────────────────────────
Information Class: Human decisions (approvals, rejections, overrides, secondary
  authorizations)
Owner: DOM-07 (capture); the human (substance)
Producers (within owner): CAP-18
Constitutionally Entitled Consumers: DOM-08 (CAP-21, 22), DOM-09 (state update pathway),
  DOM-10 (immutable record)
Notes:
────────────────────────────────────────
Information Class: Attribution Records (System Alpha, Human Override Delta,
  rejected-opportunity expectancy)
Owner: DOM-08
Producers (within owner): CAP-21, CAP-22
Constitutionally Entitled Consumers: Human review only; DOM-10
Notes: Read-only outward; no system consumer may act on them without human approval
────────────────────────────────────────
Information Class: Audit Records
Owner: DOM-10
Producers (within owner): CAP-30
Constitutionally Entitled Consumers: Human review only
Notes: Immutable; no feedback edge to any capability
────────────────────────────────────────
Information Class: Activation records
Owner: DOM-11
Producers (within owner): CAP-28
Constitutionally Entitled Consumers: DOM-10
Notes:
────────────────────────────────────────
Information Class: Reports
Owner: Composite — see 4.1
Producers (within owner):
Constitutionally Entitled Consumers: Human
Notes:

4.1 Report Ownership

No authoritative source defines a report-assembly capability, and none may be invented. Reports are composite artifacts whose sections remain owned by their producing domains:

- Advisory report (presented at CAP-18): computational sections (rankings, allocations, confidence scores, EV/risk summaries, exit suggestions, null-state) owned by DOM-05; the named sentiment/news advisory section owned by DOM-03 (mandated distinct by GOV-VAL05 Rule 4); conflict flags owned by DOM-03; active halt states owned by DOM-06; current drawdown status owned by DOM-09. Composition occurs at presentation to CAP-18 — the only place SADR locates the assembled package (CAP-18 Inputs).
- Critical risk escalation report (during Governance Halt): owned by DOM-06 (GOV-01 Rule 4).
- Attribution reports, insights, warnings: owned by DOM-08 (SDM-13 Rule 7).

Ownership of each section never transfers at composition; the assembled report is a view, not a new information class.

---
SECTION-05 — DEPENDENCY MODEL

5.1 Domain-Level Dependency Direction

DOM-11 (Activation) ── initiates cycles ──▶ all autonomous domains

DOM-01 (Market Data) ──▶ DOM-02 (Market Context)
DOM-01 ──▶ DOM-03 (Evidence Generation)      [eligible data → CAP-07]
DOM-01 ──▶ DOM-04 (Statistical Validation)   [historical data → CAP-10]
DOM-01 ──▶ DOM-05 (Recommendation Synthesis) [bias-corrected history → CAP-13]
DOM-02 ──▶ DOM-03   [trend filter, regime context → CAP-07]
DOM-02 ──▶ DOM-05   [regime context → CAP-13]
DOM-02 ──▶ DOM-06   [non-ergodic condition signal → CAP-23, CAP-27]
DOM-03 ──▶ DOM-04   [technical signals → CAP-10]
DOM-03 ──▶ DOM-05   [conflict flag annotation only → CAP-12]
DOM-03 ──▶ DOM-07   [supplementary signal set → CAP-18 advisory report]  (GOV-VAL05)
DOM-04 ──▶ DOM-05   [validated signals → CAP-12]
DOM-05 ──▶ DOM-07   [complete advisory package → CAP-18]
DOM-09 ──▶ DOM-05   [portfolio state → CAP-13, 15, 16, 20]
DOM-09 ──▶ DOM-06   [portfolio state → CAP-19, CAP-31; drawdown → CAP-25]
DOM-09 ──▶ DOM-07   [drawdown status → CAP-18 display]
DOM-06 ──▶ DOM-05   [halt gating on recommendation issuance — control dependency]
DOM-06 ──▶ DOM-07   [active halt states → CAP-18 display]
DOM-06 ──▶ DOM-11   [governance/risk events → Mode 3 event-driven activation]
DOM-07 ──▶ DOM-08   [recommendations + human actions, post-gate, read-only]
DOM-07 ──▶ DOM-09   [human-confirmed trade actions — via external execution; see 5.3]

ALL DOMAINS ──▶ DOM-10 (Audit)   [terminal sink; no outbound edges]

5.2 Constitutional Blocking Gates (preserved from SADR Section 5)

┌──────────────┬──────────────────────────────────────────────┬───────────────────────┐
│     Gate     │                    Effect                    │        Source         │
├──────────────┼──────────────────────────────────────────────┼───────────────────────┤
│ CAP-02       │ Blocks all signal logic until                │ SDM-02 Rule 2, SDM-05 │
│ (DOM-01)     │ cross-verification passes                    │  Rule 1               │
├──────────────┼──────────────────────────────────────────────┼───────────────────────┤
│ CAP-10       │ Blocks confidence scoring until walk-forward │ SDM-05 Rule 2         │
│ (DOM-04)     │  validation passes                           │                       │
├──────────────┼──────────────────────────────────────────────┼───────────────────────┤
│ CAP-18       │ Blocks all trade action — no exceptions, no  │ SDM-CONST-06          │
│ (DOM-07)     │ bypass                                       │                       │
└──────────────┴──────────────────────────────────────────────┴───────────────────────┘

5.3 Circularity Analysis

The only apparent cycle is DOM-09 → DOM-05 → DOM-07 → DOM-09 (portfolio state feeds recommendations; approved recommendations eventually change portfolio state). This is not an internal circular dependency: the path from DOM-07 back to DOM-09 exits the system boundary. The human executes (or does not execute) the approved trade externally; DOM-09 updates only from human-confirmed trade actions verified against the authoritative external execution record (CAP-29 Inputs). The cycle is broken at the system boundary by the human actor. Within any single recommendation cycle the internal graph is acyclic.

Secondary check — DOM-06 → DOM-11 → DOM-06 (governance events trigger event-driven activation, which initiates cycles including governance functions): activation is initiation, not data dependency; CAP-28's output is an initiated cycle, not an input consumed by CAP-23/CAP-31 logic. No data circularity exists.

5.4 Prohibited Dependencies (binding on all derived architectures)

- DOM-08 → any recommendation, validation, confidence, EV, ranking, allocation, or governance logic (CONSTRAINT-07)
- DOM-10 → any capability (CAP-30 Boundary)
- DOM-03 supplementary signals → DOM-05 computation (GOV-VAL05 Rule 1)
- Any domain → broker/execution venue (GOV-01 Rule 1, GOV-02 Rules 4–5)
- Any signal logic ← unverified data (SDM-02 Rule 2)
- Any path around CAP-18 to a trade action (SDM-CONST-06)

5.5 Hidden Coupling Controls

- DOM-09 is the single source of portfolio state; no consumer may maintain a private portfolio state derivative that other domains then consume (this would recreate the compliance-evaluation ambiguity that CHANGE-01/CHANGE-02 resolved).
- DOM-02's non-ergodic condition signal is a generic condition-signal interface (VAL-03/VAL-17 CLASS_B); consumers (CAP-23, CAP-27) depend on the interface, not on its internal mathematics.
- The four halt states share no state with each other (SDM-CONST-14 independence).

---
SECTION-06 — GOVERNANCE INTERACTION MODEL

6.1 What Halt States Gate — and What They Never Touch

Constitutional finding: all four halt states gate recommendation issuance only. No halt state suspends research, analysis, monitoring, attribution, audit, or reporting functions. Evidence:

- GOV-01 Rule 4: during Governance Halt the system must generate a critical risk escalation report — reporting continues.
- GOV-02 Rule 3: restoration must be detected automatically from available portfolio state — monitoring (CAP-31, CAP-29) continues during Lockout.
- SDM-15 Rule 14: suspension exit is condition-driven — condition monitoring (CAP-23) continues during Suspension.
- SDM-CONST-15: monitoring/governance/reporting authority is unconditioned on halt states.

Therefore the gating surface of DOM-06 is the issuance boundary of DOM-05 outputs (and their presentation at DOM-07), never the upstream domains DOM-01 through DOM-04, and never DOM-08/DOM-09/DOM-10/DOM-11.

6.2 Per-State Interaction

State: State 1 — Governance Halt (CAP-25)
Entry (detector → state): DOM-09 drawdown ≥ 5% → CAP-25
Blocked Outputs: All new recommendations; all new capital allocation recommendations
Domains Affected: DOM-05 issuance
Exit: Explicit human resumption authorization
Exit Authority: Human
────────────────────────────────────────
State: State 2 — Governance Lockout (CAP-26)
│ DOM-11        │ CAP-28      │ SDM-CONST-15; FDP-OW │ Scheduled/On-Demand/Event-Driv │
│ Activation    │             │ NER_DECISION_01      │ en Activation                  │
└───────────────┴─────────────┴──────────────────────┴────────────────────────────────┘

---
ARCHITECTURE_FOUNDATION_V1 derives its entire authority from SDM_V2.3 (as amended by GOV-VAL05), SADR_V2.1 (as amended by SADR_AMENDMENT_VAL-05), the VAL-05 Owner Decision Resolution, and the SDM Freeze Certification. It introduces no behavior, no capability, no authority, and no technology. Multiple valid architectures may be derived from it; none is selected by it.

---

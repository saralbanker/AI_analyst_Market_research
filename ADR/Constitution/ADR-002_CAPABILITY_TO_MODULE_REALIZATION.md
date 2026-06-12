# ADR-002 — CAPABILITY TO MODULE REALIZATION

**Decision Type:** Architectural Realization
**Method:** Evidence-Bound Investigation (8 mandatory investigations)
**Authority Hierarchy:**
- Level 1: SDM_V2.3 (FROZEN)
- Level 2: VAL05_OWNER_DECISION_RESOLUTION (RESOLVED)
- Level 3: SADR_V2.1 (CERTIFIED)
- Level 4: ARCHITECTURE_FOUNDATION_V1
- Level 5: ADR-000_ARCHITECTURE_PRINCIPLES (P-01 through P-12)
- Level 6: ADR-001_ARCHITECTURAL_STYLE_SELECTION (Modular Monolith + Bounded Event Signaling)

**Status:** CANDIDATE FOR OWNER REVIEW
**Scope:** Determines what modules exist, which capabilities belong to each, what information each owns, which dependencies are permitted and forbidden, how authority classes map, how event boundaries operate, and how governance and audit isolation are preserved. Does not design implementation, software, databases, or infrastructure.

---

## SECTION 1 — EXECUTIVE SUMMARY

The eight mandatory investigations yield the following findings:

**Module count:** 11 modules, derived 1:1 from the 11 constitutional domains in ARCHITECTURE_FOUNDATION_V1. No modules are invented. No constitutional domain is split or merged.

**Capability allocation:** All 31 SADR capabilities are assigned exactly once. Zero orphans. Zero duplicates.

**Information ownership:** 13 information classes, each with exactly one owning module. No shared ownership. No hidden ownership.

**Dependency structure:** A directed acyclic graph preserving the AF 5.1 domain map. Six dependency classes are prohibited. Three constitutional blocking gates are preserved as hard sequential constraints.

**Authority mapping:** AUTONOMOUS_RESEARCH governs 29 capabilities across 9 modules. SHARED_AUTHORITY governs CAP-09 in MOD-03. HUMAN_APPROVAL governs CAP-18 in MOD-07. Authority isolation is structurally preserved.

**Event boundaries:** Constitutionally bounded to two relationship types: MOD-11 activation initiation and MOD-06 governance event signaling to MOD-11. All other inter-module communication is synchronous, sequential, and contained within the modular monolith core.

**Governance isolation:** All four halt states are modularly independent within MOD-06. Monitoring and audit continuity during halt states is preserved by the module boundary design — halt-state modules gate MOD-05 recommendation issuance only, not the monitoring, audit, or portfolio state modules.

**Audit isolation:** MOD-10 receives from all modules and has zero permitted outbound edges to any other module.

**ADR-003 Readiness: MAY PROCEED.**

---

## SECTION 2 — MODULE DERIVATION METHODOLOGY

### 2.1 Derivation Basis

**Evidence:** ARCHITECTURE_FOUNDATION_V1 Section 2.0

The Architecture Foundation derived 11 constitutional domains from the 31 SADR capabilities using three evidence tests applied in order:

1. **Constitutional rooting** — capabilities sharing the same SDM decision rule(s) as their primary source belong together unless test 2 or 3 separates them.
2. **Information cohesion** — capabilities that jointly produce and own a single class of information belong together.
3. **Authority cohesion** — a capability whose authority class or constitutional independence differs from its neighbors must not be absorbed into a domain that would dilute that distinction.

**Reasoning:** The Architecture Foundation's derivation method is at Level 4 authority — frozen and not under review. The module derivation in ADR-002 must preserve this derivation, not re-derive it. The 11 constitutional domains map 1:1 to 11 modules in the Modular Monolith architectural style.

**Validation:** ADR-000 P-11 states: "Architectural domains must map to the 11 constitutional domains derived in ARCHITECTURE_FOUNDATION_V1... SADR capability boundaries must be preserved: no capability may be split across domains, silently merged with another, renamed to combine two, or re-scoped to absorb a function belonging to a different capability."

### 2.2 Module Naming Convention

Each module is named MOD-NN corresponding to its constitutional domain DOM-NN. The name reflects constitutional identity, not implementation technology. Module names are not service names, class names, or deployment unit names.

| Module ID | Constitutional Domain | Mapping Basis |
|-----------|----------------------|---------------|
| MOD-01 | DOM-01 Market Data Foundation | 1:1 |
| MOD-02 | DOM-02 Market Context | 1:1 |
| MOD-03 | DOM-03 Evidence Generation | 1:1 |
| MOD-04 | DOM-04 Statistical Validation | 1:1 |
| MOD-05 | DOM-05 Recommendation Synthesis | 1:1 |
| MOD-06 | DOM-06 Risk & Governance Enforcement | 1:1 |
| MOD-07 | DOM-07 Human Decision Authority | 1:1 |
| MOD-08 | DOM-08 Attribution | 1:1 |
| MOD-09 | DOM-09 Portfolio State | 1:1 |
| MOD-10 | DOM-10 Audit | 1:1 |
| MOD-11 | DOM-11 Activation | 1:1 |

**Total modules: 11. Total constitutional domains: 11. Correspondence: complete.**

---

## SECTION 3 — MODULE CATALOG

---

### MOD-01 | Market Data Foundation

**Purpose:**
Produce the verified, adjusted, eligible, survivorship-bias-corrected market dataset that all downstream evidence and probability logic is constitutionally required to consume — and block everything downstream until that dataset exists.

**Evidence:** AF DOM-01 Purpose statement; SADR CAP-01 through CAP-04 and CAP-14 necessity clauses.

**Owned Capabilities:**
- CAP-01 | Market Data Ingestion
- CAP-02 | Data Cross-Verification ← BLOCKING GATE
- CAP-03 | Corporate Action Adjustment
- CAP-04 | Universe Eligibility Enforcement
- CAP-14 | Survivorship Bias Correction

**Authority Class:** AUTONOMOUS_RESEARCH

**Evidence:** AF Section 3.2: "DOM-01 Market Data Foundation — AI (Autonomous) Authority: Ingest, verify, adjust, filter, correct data." SADR Section 6: all five capabilities carry AUTONOMOUS_RESEARCH.

**Owned Information:**
- Raw market data (inbound from external sources; unprocessed)
- Cross-verification match/mismatch records
- Split-adjusted OHLCV data; adjustment audit records; rejection records for unadjustable data
- The eligible equity set; eligible-vs-filtered counts; exclusion logs with triggered filter rules
- The survivorship-bias-corrected historical dataset

**Evidence:** AF SECTION-04 "Market datasets (raw, verified, adjusted, eligible, bias-corrected)" — Owner: DOM-01.

**Blocking Gate Constraint:**
CAP-02 is a constitutional hard blocking gate. No signal logic in any other module may receive information until CAP-02's cross-verification passes.

**Evidence:** SADR Section 5 "Critical Blocking Dependencies: CAP-02 blocks all signal logic (SDM-02 Rule 2, SDM-05 Rule 1)." AF 5.2 reproduces this verbatim.

**Constitutional Constraints Preserved:**
- At least two independent external sources required (SDM-02 Rule 2)
- Delisted equities included in historical datasets (SDM-02 Rule 1)
- Unadjusted split data rejected before reaching downstream modules (SDM-02 Rule 3)
- Signal logic may not receive data that has not passed cross-verification — hard gate (SADR CONSTRAINT binding on MOD-02, MOD-03, MOD-04, MOD-05)

---

### MOD-02 | Market Context

**Purpose:**
Classify the market environment, detect structural shifts and model drift, and emit the condition signals (trend filter state, regime context, non-ergodic condition signal) that other modules are constitutionally required to consume.

**Evidence:** AF DOM-02 Purpose statement; SADR CAP-05 and CAP-06 necessity clauses.

**Owned Capabilities:**
- CAP-05 | Market Regime Classification
- CAP-06 | Concept Drift Detection

**Authority Class:** AUTONOMOUS_RESEARCH

**Evidence:** AF Section 3.2: "DOM-02 Market Context — AI (Autonomous) Authority: Classify, detect drift, alert." SADR Section 6: both capabilities carry AUTONOMOUS_RESEARCH.

**Owned Information:**
- Current market regime classification
- Regime shift alerts
- Broad market trend filter state (required by CAP-07 for sector rotation evaluation)
- Non-ergodic condition signal (generic condition-signal interface per VAL-03/VAL-17 CLASS_B resolution)
- Concept drift metrics; model anchoring detection events
- Walk-forward cross-validation bounds

**Evidence:** AF SECTION-04 "Market context state (regime, trend filter, drift, non-ergodic condition signal)" — Owner: DOM-02.

**Constitutional Constraints Preserved:**
- Walk-forward mandatory; K-fold prohibited (SDM-03 Rule 1)
- Non-ergodic condition signal is a generic interface — consumers (MOD-05 via CAP-13, MOD-06 via CAP-23, CAP-27) depend on the interface, not on its internal mathematics (AF 5.5; VAL-03/VAL-17 CLASS_B)
- Regime shift alerts must be human-visible (SDM-03 Human Visibility)

---

### MOD-03 | Evidence Generation

**Purpose:**
Generate the two constitutional evidence layers — technical (primary) and supplementary news (advisory) — and detect and characterize conflicts between them for the human's benefit.

**Evidence:** AF DOM-03 Purpose statement; SADR CAP-07, CAP-08, CAP-09 necessity clauses.

**Owned Capabilities:**
- CAP-07 | Technical Signal Generation
- CAP-08 | Supplementary Signal Intake
- CAP-09 | Technical-News Conflict Evaluation

**Authority Class:** MIXED
- CAP-07: AUTONOMOUS_RESEARCH
- CAP-08: AUTONOMOUS_RESEARCH
- CAP-09: SHARED_AUTHORITY (system evaluates and flags; human reviews and decides at CAP-18)

**Evidence:** SADR Section 6: CAP-07 and CAP-08 carry AUTONOMOUS_RESEARCH; CAP-09 carries SHARED_AUTHORITY. AF Section 3.2: "DOM-03: Shared Authority: CAP-09: system flags conflict; human decides." AF DOM-03: "The domain's autonomous authority does not absorb CAP-09's shared classification."

**Owned Information:**
- Technical signal set with evidence type, supporting data, and signal quality metadata
- Supplementary signal set with source reliability metadata
- Conflict detection results, conflict flags, evidence characterization, and resolution rationale

**Evidence:** AF SECTION-04: three distinct information classes owned by DOM-03 — "Signals — technical," "Signals — supplementary (news/sentiment)," "Conflict flags and characterization."

**GOV-VAL05 Routing Constraint (binding on all MOD-03 outputs):**

The supplementary signal set (CAP-08 output) routes ONLY to:
1. CAP-09 within MOD-03 (for conflict evaluation)
2. The human-facing advisory report assembled for MOD-07

It does NOT route to MOD-05 (any computational capability), MOD-04, or any other module as a computational input.

The conflict flag produced by CAP-09 routes to MOD-05 (CAP-12) as advisory annotation on the confidence score output only — it does not modify the score computationally.

**Evidence:** AF DOM-03 GOV-VAL05 Boundary: "The supplementary signal set routes only to the human-facing advisory report assembled for CAP-18. It does not enter CAP-12 or any downstream computation. The conflict flag from CAP-09 flows to CAP-12 as advisory annotation on the score output — never as a computational input that modifies the score." GOV-VAL05 Rule 1; SADR_AMENDMENT_VAL-05; AF 5.4 prohibited dependency.

**Constitutional Constraints Preserved:**
- Technical evidence takes strict priority (SDM-CONST-10; CONSTRAINT-04)
- AI evaluations isolated exclusively to semantic/cognitive domain (SDM-04 Rule 12)
- Analyst rating changes and social media sentiment excluded or given minimal weight (SDM-04 Rule 6)
- Price breakouts validated using volume spikes (SDM-04 Rule 8)
- Sector rotation aligned with broad market trend filter from MOD-02 (SDM-04 Rule 7)

---

### MOD-04 | Statistical Validation

**Purpose:**
Verify statistical edge and temporal integrity of candidate signals before any confidence or recommendation logic may consume them.

**Evidence:** AF DOM-04 Purpose statement; SADR CAP-10 and CAP-11 necessity clauses.

**Owned Capabilities:**
- CAP-10 | Walk-Forward Signal Validation ← BLOCKING GATE
- CAP-11 | Statistical Edge Verification

**Authority Class:** AUTONOMOUS_RESEARCH

**Evidence:** AF Section 3.2: "DOM-04 Statistical Validation — AI (Autonomous) Authority: Validate, verify edge, reject signals." SADR Section 6: both capabilities carry AUTONOMOUS_RESEARCH.

**Owned Information:**
- Walk-forward validation results and scores
- Validated signal set; rejected signals with rejection basis
- Statistical edge verdicts
- Deflated return metrics / statistical significance test results
- Stability index values
- Outlier detection verification records

**Evidence:** AF SECTION-04 "Validation verdicts and edge evidence" — Owner: DOM-04.

**Blocking Gate Constraint:**
CAP-10 is a constitutional hard blocking gate. Confidence scoring (MOD-05 CAP-12) may not execute on signals that have not passed walk-forward validation.

**Evidence:** SADR Section 5: "CAP-10 blocks confidence scoring (SDM-05 Rule 2)." AF 5.2: same verbatim.

**Constitutional Constraints Preserved:**
- K-fold cross-validation constitutionally prohibited (CONSTRAINT-08; SDM-03 Rule 1; SDM-05 Rule 2)
- Walk-forward validation mandatory (CONSTRAINT-08)
- Data smoothing may not mask structural anomalies (SDM-05 Rule 7)
- Deflated return metrics or t-stat required (SDM-05 Rule 4)

---

### MOD-05 | Recommendation Synthesis

**Purpose:**
Transform validated technical evidence plus portfolio state into the complete advisory recommendation package: confidence scores, expected value, rankings, conviction-weighted allocations, exit suggestions, and the explicit null-state when nothing qualifies.

**Evidence:** AF DOM-05 Purpose statement; SADR CAP-12 through CAP-17 and CAP-20 necessity clauses.

**Owned Capabilities:**
- CAP-12 | Confidence Scoring
- CAP-13 | Expected Value Computation
- CAP-15 | Opportunity Ranking
- CAP-16 | Conviction-Weighted Allocation
- CAP-17 | Null-State Declaration
- CAP-20 | Exit Condition Recommendation

**Authority Class:** AUTONOMOUS_RESEARCH

**Evidence:** AF Section 3.2: "DOM-05 Recommendation Synthesis — AI (Autonomous) Authority: Compute, rank, allocate, declare null-state, recommend exits." SADR Section 6: all six capabilities carry AUTONOMOUS_RESEARCH.

**Owned Information:**
- Confidence scores (derived exclusively from technical evidence and statistical validation; conflict-flag annotations are advisory only)
- Probability-adjusted return and downside drawdown estimates
- EV-filtered opportunity set; cash-holding signal
- Ranked opportunity list (3–5 target)
- Conviction-weighted allocation suggestions with justification
- Explicit "Hold Cash" statements
- Null-state declarations
- Exit condition recommendations with extension justifications and transaction cost estimates

**Evidence:** AF SECTION-04 "Recommendations (confidence, EV, rankings, allocations, null-state, exit suggestions)" — Owner: DOM-05.

**Computation Purity Constraint (binding):**
CAP-12 confidence computation is derived exclusively from technical evidence and statistical validation. Supplementary signals (news/sentiment) from MOD-03 do NOT enter the confidence formula as computational inputs. The conflict flag annotation from CAP-09 marks the score for human attention but does not modify the score value.

**Evidence:** GOV-VAL05 Rule 1; SADR_AMENDMENT_VAL-05 CAP-12 after-state; AF DOM-05: "Confidence scores (derived exclusively from technical evidence and statistical validation per GOV-VAL05 Rule 1)."

**Halt State Gating Constraint:**
MOD-05 recommendation issuance is gated by MOD-06. When any halt state in MOD-06 is active and blocking, MOD-05 does not issue the blocked recommendation class. The gating is applied at issuance (CAP-15, CAP-16, CAP-17, CAP-20 outputs to MOD-07), not at computation.

**Evidence:** AF 6.1: "All four halt states gate recommendation issuance only." The gating surface is the issuance boundary of DOM-05 outputs.

**Constitutional Constraints Preserved:**
- Equal-weight allocation prohibited (SDM-08 Rule 6; SDM-09 Rule 3)
- Conviction hierarchy: confidence-weighted first, then best-idea-weighted (SDM-09 Rule 2)
- 3–5 position target; scale to fewer if insufficient opportunities (SDM-08 Rules 3, 4)
- Null-state explicitly declared when no opportunities qualify (SDM-01 Rule 1; CONSTRAINT-05)
- All outputs are advisory; no output constitutes an executable trade order (SDM-CONST-13)

---

### MOD-06 | Risk & Governance Enforcement

**Purpose:**
Detect risk and governance conditions, manage the four constitutionally independent halt states, and gate recommendation authority accordingly — while holding zero execution authority.

**Evidence:** AF DOM-06 Purpose statement; SADR CAP-19, CAP-23 through CAP-27, CAP-31 necessity clauses.

**Owned Capabilities (Detection):**
- CAP-19 | Position Limit Enforcement
- CAP-23 | Risk Circuit Breaker Enforcement
- CAP-31 | Governance Compliance Monitor

**Owned Capabilities (Halt-State Management):**
- CAP-24 | Hard Deterministic Halt (State 4)
- CAP-25 | Governance Halt (State 1)
- CAP-26 | Governance Lockout (State 2)
- CAP-27 | Conditional Recommendation Suspension (State 3)

**Authority Class:** AUTONOMOUS_RESEARCH (with constitutional ceiling: governs recommendation authority only; zero execution authority)

**Evidence:** AF Section 3.2: "DOM-06 Risk & Governance Enforcement — AI (Autonomous) Authority: Detect conditions; enter/maintain halt states; auto-exit States 2 and 3 on detected condition clearance." AF DOM-06: "AUTONOMOUS_RESEARCH — with the constitutional ceiling that every halt state governs recommendation authority only; none grants execution authority (SDM-CONST-14)."

**Owned Information:**
- Governance State: the four independent halt-state flags with entry/exit condition records
- Position and concentration limit compliance status
- Circuit breaker detection signals (scaling, suspension, margin restriction, margin audit status)
- Governance violation and restoration signals
- Compliance evaluation event records
- Critical risk escalation report content (GOV-01 Rule 4)
- Human-visible breach alerts

**Evidence:** AF SECTION-04 "Governance State (four halt-state flags, entry/exit records, compliance signals, limit status)" — Owner: DOM-06.

**Independence Constraint (binding — ADR-000 P-06):**
The four halt states (CAP-24, CAP-25, CAP-26, CAP-27) are constitutionally independent within MOD-06. Each has its own entry logic, active-state representation, and exit logic. No shared state variable, shared trigger evaluator, or shared exit mechanism spans two or more halt states. Simultaneous activation is an emergent property of independent states, not an explicitly handled combined state.

**Evidence:** SDM-CONST-14; SADR Section 5 "Halt State Independence"; AF DOM-06 Independence Constraint: "No derived architecture may merge the four states into a single state machine that erases this independence."

**Governance Continuity Constraint (binding):**
MOD-06 halt states gate recommendation issuance from MOD-05. They do NOT gate:
- MOD-01 (market data processing)
- MOD-02 (regime classification)
- MOD-03 (signal generation)
- MOD-04 (statistical validation)
- MOD-08 (attribution observation)
- MOD-09 (portfolio state maintenance)
- MOD-10 (audit recording)
- MOD-11 (activation)
- MOD-06's own detection functions (CAP-31, CAP-23, CAP-19 continue during any halt state)

**Evidence:** AF 6.1: "All four halt states gate recommendation issuance only. No halt state suspends research, analysis, monitoring, attribution, audit, or reporting functions." GOV-01 Rule 4: reporting continues during Governance Halt. GOV-02 Rule 3: monitoring (CAP-31, CAP-29) continues during Lockout. SDM-15 Rule 14: condition monitoring continues during Suspension.

**Constitutional Constraints Preserved:**
- Zero execution authority under any circumstance (GOV-01 Rule 1; GOV-02 Rules 4–5)
- Halt states govern recommendation authority only (SDM-CONST-14)
- CAP-31 evaluates continuously, not only at approval gate events (SADR CAP-31 constraints)
- GOV-02 Rule 3: Lockout exit detected automatically; no additional human authorization required beyond corrective action

---

### MOD-07 | Human Decision Authority

**Purpose:**
Present the complete advisory package as a simultaneous Open Menu and hold the single, bypass-proof gate at which the human — and only the human — authorizes any trade action.

**Evidence:** AF DOM-07 Purpose statement; SADR CAP-18 necessity clause.

**Owned Capabilities:**
- CAP-18 | Human Approval Gate ← BLOCKING GATE (mandatory; no exceptions; no bypass)

**Authority Class:** HUMAN_APPROVAL

**Evidence:** SADR Section 6: "CAP-18: Human decision mandatory before any trade action. SDM-CONST-06. No bypass." AF Section 3.2: "DOM-07 Human Decision Authority — Human Authority: Approve, reject, override, modify — final authority over all trade decisions." AF DOM-07: "Authority Type: HUMAN_APPROVAL. The system's authority here is presentation only; decision authority is entirely human."

**Owned Information:**
- Human approval decisions
- Human override parameters
- Case-by-case evaluation triggers (system/human disagreement, SDM-10 Rule 4)
- Secondary authorization events for algorithmic pricing limit modifications (SDM-10 Rule 5)

**Evidence:** AF SECTION-04 "Human decisions (approvals, rejections, overrides, secondary authorizations)" — Owner: DOM-07 (capture); the human (substance).

**Blocking Gate Constraint:**
CAP-18 is the constitutional hard blocking gate for all trade action. No output of any module constitutes an executable trade order. All recommendation outputs from MOD-05 are advisory inputs to CAP-18; the human's decision at CAP-18 is the only constitutionally authorized precondition for trade action.

**Evidence:** SADR Section 5: "CAP-18 blocks all trade action — no exceptions, no bypass." AF 5.2: same verbatim. SDM-CONST-06; SDM-CONST-13.

**Presentation Constraint (binding):**
All EV-filtered, positively-ranked opportunities are presented simultaneously as an Open Menu. Sequential forced selection is prohibited. No timeout-based auto-approval. No bypass pathways.

**Evidence:** SDM-08 Rule 8; SADR CONSTRAINT-09; CAP-18 Boundary; AF DOM-07 Presentation Constraint.

**Advisory Package Composition:**
The advisory package assembled for CAP-18 includes:
- Ranked opportunity list, conviction-weighted allocation suggestions, confidence scores, supporting evidence, risk summaries, exit suggestions (owned by MOD-05)
- Named sentiment/news advisory section distinct from computational outputs (owned by MOD-03, per GOV-VAL05 Rule 4)
- Conflict flags (owned by MOD-03)
- Active halt states (owned by MOD-06)
- Current drawdown status (owned by MOD-09)
- Null-state declaration if applicable (owned by MOD-05)

Ownership of each section never transfers at composition. The assembled report is a view, not a new information class.

**Evidence:** AF 4.1 Report Ownership; AF Section 4.1: "Ownership of each section never transfers at composition; the assembled report is a view, not a new information class."

---

### MOD-08 | Attribution

**Purpose:**
Observe decision quality across accepted and rejected opportunities, maintain System Alpha and Human Override Delta as distinct layers, and report insights to the human — with no write authority over anything.

**Evidence:** AF DOM-08 Purpose statement; SADR CAP-21 and CAP-22 necessity clauses.

**Owned Capabilities:**
- CAP-21 | Attribution Observation
- CAP-22 | Human Override Delta Tracking

**Authority Class:** AUTONOMOUS_RESEARCH — restricted to Observation Authority only (SDM-13 Rule 8, 10)

**Evidence:** AF DOM-08: "Authority Type: AUTONOMOUS_RESEARCH, restricted to Observation Authority only (SDM-13). No write authority over signal, validation, confidence, EV, ranking, allocation, or governance logic." SADR CONSTRAINT-07.

**Owned Information:**
- System Alpha (Baseline) layer
- Human Override Delta (Human Alpha/Bleed) layer (distinct per SDM-13 Rule 5)
- Theoretical expectancy records for rejected opportunities
- Tracking metadata (setup type, regime context, holding duration)
- Attribution reports, insights, and warnings for human review

**Evidence:** AF SECTION-04 "Attribution Records (System Alpha, Human Override Delta, rejected-opportunity expectancy)" — Owner: DOM-08. "Constitutionally entitled consumers: Human review only; DOM-10."

**Read-Only Constraint (binding — ADR-000 P-08):**
MOD-08 has zero permitted write edges to MOD-01, MOD-02, MOD-03, MOD-04, MOD-05, or MOD-06. Attribution outputs (reports, insights, warnings) flow only to human review and MOD-10 (audit). Any behavior change motivated by attribution findings requires explicit human approval routed through a constitutionally authorized change process — not through an automated feedback path from MOD-08.

**Evidence:** SDM-13 Rules 8, 9, 10; SADR CONSTRAINT-07; AF DOM-08; AF 3.3 anti-leakage check 2.

**Input Sources:**
MOD-08 receives from MOD-07 (post-gate: recommendations + human actions, read-only, per AF 5.1 and SADR Section 5).

---

### MOD-09 | Portfolio State

**Purpose:**
Maintain and provide the system's authoritative representation of portfolio state — sourced exclusively from human-approved, externally executed trade actions — to every module constitutionally entitled to it.

**Evidence:** AF DOM-09 Purpose statement; SADR CAP-29 necessity clause.

**Owned Capabilities:**
- CAP-29 | Portfolio State Visibility

**Authority Class:** AUTONOMOUS_RESEARCH (state maintenance and provision only)

**Evidence:** AF DOM-09: "Authority Type: AUTONOMOUS_RESEARCH (state maintenance and provision only). The system has no write authority over the actual portfolio (CONSTRAINT-01); state changes originate only from human-confirmed trade actions verified against the authoritative external execution record (CAP-29 Inputs)."

**Owned Information:**
- Active position count
- Current drawdown level against the 5% tolerance
- Position concentration status
- Illiquidity metrics

**Evidence:** AF SECTION-04 "Portfolio State" — Owner: DOM-09. "Constitutionally entitled consumers: DOM-05 (CAP-13, 15, 16, 20), DOM-06 (CAP-19, 25, 31), DOM-07 (CAP-18 drawdown display)."

**Single-Source Constraint (binding — ADR-000 P-05):**
MOD-09 is the single authoritative source of portfolio state. No consumer module may maintain a private derivative of portfolio state that other modules then consume. Portfolio state changes originate only from human-confirmed trade actions verified against the authoritative external execution record.

**Evidence:** AF 5.5: "DOM-09 is the single source of portfolio state; no consumer may maintain a private portfolio state derivative that other domains then consume." SADR CHANGE-01 architectural history.

**Input Source:**
The authoritative external execution record (confirmed trades the human actually executed) — arriving from outside the system boundary per AF Section 1.3.

---

### MOD-10 | Audit

**Purpose:**
Hold the immutable, constitutionally mandated record of everything: every system decision, human decision, override, halt entry/exit with condition state, validation result, conflict resolution, recommendation, activation, and compliance evaluation.

**Evidence:** AF DOM-10 Purpose statement; SADR CAP-30 necessity clause.

**Owned Capabilities:**
- CAP-30 | Immutable Audit Log

**Authority Class:** AUTONOMOUS_RESEARCH (recording only)

**Evidence:** AF Section 3.2: "DOM-10 Audit — AI (Autonomous) Authority: Record immutably. Human Authority: Consume for review." SADR Section 6: CAP-30 carries AUTONOMOUS_RESEARCH.

**Owned Information:**
- The immutable audit trail
- Per-domain records per each SDM Audit clause (SDM-02 through SDM-15)
- The immutable record of original system recommendation versus final human action

**Evidence:** AF SECTION-04 "Audit Records" — Owner: DOM-10. "Constitutionally entitled consumers: Human review only."

**Terminal Sink Constraint (binding — ADR-000 P-07):**
MOD-10 receives from all modules. MOD-10 has zero permitted outbound edges to any other module. No module reads from MOD-10 at runtime to influence its behavior. Human review of audit records is explicitly authorized and is the only legitimate consumer of audit output.

**Evidence:** AF 5.1: "ALL DOMAINS ──▶ DOM-10 (Audit) [terminal sink; no outbound edges]." AF 5.4 prohibited dependency: "DOM-10 → any capability." CAP-30 Boundary: "Recording only. Does not process events. Does not feed back into any capability." AF 3.3 anti-leakage check 3.

**Immutability Constraint:**
Audit records are immutable — not merely append-only. Once written, a record may not be modified or deleted by any system operation.

**Evidence:** SADR CHANGE-06 (replaced "append-only" with "immutable"); SADR CAP-30 Outputs.

---

### MOD-11 | Activation

**Purpose:**
Initiate research/analysis/monitoring/attribution/reporting/governance cycles under the three constitutionally authorized modes, and record which mode initiated each cycle.

**Evidence:** AF DOM-11 Purpose statement; SADR CAP-28 necessity clause.

**Owned Capabilities:**
- CAP-28 | System Activation Authority

**Authority Class:** AUTONOMOUS_RESEARCH

**Evidence:** AF Section 3.2: "DOM-11 Activation — AI (Autonomous) Authority: Initiate Modes 1 and 3 autonomously. Human Authority: Initiate Mode 2 (explicit request)." SADR Section 6: CAP-28 carries AUTONOMOUS_RESEARCH.

**Owned Information:**
- Activation events (mode, trigger, initiated cycle) as recorded to audit

**Evidence:** AF SECTION-04 "Activation records" — Owner: DOM-11. "Constitutionally entitled consumers: DOM-10."

**Activation Mode Definitions (constitutionally fixed):**
- Mode 1 — Scheduled: autonomous initiation on predefined schedules
- Mode 2 — On-Demand: initiation upon explicit human request
- Mode 3 — Event-Driven: initiation when governance, risk, or portfolio events trigger mandatory review

**Authority Ceiling:**
No activation mode grants trade execution authority. This authority applies exclusively to research, analysis, monitoring, attribution, reporting, and governance.

**Evidence:** SDM-CONST-15; SADR CONSTRAINT-10; AF DOM-11.

---

## SECTION 4 — CAPABILITY ALLOCATION MATRIX

All 31 SADR capabilities assigned exactly once. Zero orphans. Zero duplicates.

| Cap ID | Capability Name | Assigned Module | Authority Class |
|--------|----------------|----------------|-----------------|
| CAP-01 | Market Data Ingestion | MOD-01 | AUTONOMOUS_RESEARCH |
| CAP-02 | Data Cross-Verification | MOD-01 | AUTONOMOUS_RESEARCH |
| CAP-03 | Corporate Action Adjustment | MOD-01 | AUTONOMOUS_RESEARCH |
| CAP-04 | Universe Eligibility Enforcement | MOD-01 | AUTONOMOUS_RESEARCH |
| CAP-05 | Market Regime Classification | MOD-02 | AUTONOMOUS_RESEARCH |
| CAP-06 | Concept Drift Detection | MOD-02 | AUTONOMOUS_RESEARCH |
| CAP-07 | Technical Signal Generation | MOD-03 | AUTONOMOUS_RESEARCH |
| CAP-08 | Supplementary Signal Intake | MOD-03 | AUTONOMOUS_RESEARCH |
| CAP-09 | Technical-News Conflict Evaluation | MOD-03 | SHARED_AUTHORITY |
| CAP-10 | Walk-Forward Signal Validation | MOD-04 | AUTONOMOUS_RESEARCH |
| CAP-11 | Statistical Edge Verification | MOD-04 | AUTONOMOUS_RESEARCH |
| CAP-12 | Confidence Scoring | MOD-05 | AUTONOMOUS_RESEARCH |
| CAP-13 | Expected Value Computation | MOD-05 | AUTONOMOUS_RESEARCH |
| CAP-14 | Survivorship Bias Correction | MOD-01 | AUTONOMOUS_RESEARCH |
| CAP-15 | Opportunity Ranking | MOD-05 | AUTONOMOUS_RESEARCH |
| CAP-16 | Conviction-Weighted Allocation | MOD-05 | AUTONOMOUS_RESEARCH |
| CAP-17 | Null-State Declaration | MOD-05 | AUTONOMOUS_RESEARCH |
| CAP-18 | Human Approval Gate | MOD-07 | HUMAN_APPROVAL |
| CAP-19 | Position Limit Enforcement | MOD-06 | AUTONOMOUS_RESEARCH |
| CAP-20 | Exit Condition Recommendation | MOD-05 | AUTONOMOUS_RESEARCH |
| CAP-21 | Attribution Observation | MOD-08 | AUTONOMOUS_RESEARCH |
| CAP-22 | Human Override Delta Tracking | MOD-08 | AUTONOMOUS_RESEARCH |
| CAP-23 | Risk Circuit Breaker Enforcement | MOD-06 | AUTONOMOUS_RESEARCH |
| CAP-24 | Hard Deterministic Halt | MOD-06 | AUTONOMOUS_RESEARCH |
| CAP-25 | Governance Halt | MOD-06 | AUTONOMOUS_RESEARCH |
| CAP-26 | Governance Lockout | MOD-06 | AUTONOMOUS_RESEARCH |
| CAP-27 | Conditional Recommendation Suspension | MOD-06 | AUTONOMOUS_RESEARCH |
| CAP-28 | System Activation Authority | MOD-11 | AUTONOMOUS_RESEARCH |
| CAP-29 | Portfolio State Visibility | MOD-09 | AUTONOMOUS_RESEARCH |
| CAP-30 | Immutable Audit Log | MOD-10 | AUTONOMOUS_RESEARCH |
| CAP-31 | Governance Compliance Monitor | MOD-06 | AUTONOMOUS_RESEARCH |

**Totals:** 31 capabilities assigned. 0 orphans. 0 duplicates.
**AUTONOMOUS_RESEARCH:** 29 capabilities. **SHARED_AUTHORITY:** 1 (CAP-09). **HUMAN_APPROVAL:** 1 (CAP-18).

---

## SECTION 5 — INFORMATION OWNERSHIP MATRIX

All 13 information classes assigned to exactly one owning module. No dual ownership. No unowned classes.

| Information Class | Owner Module | Producing Capabilities | Authorized Consumer Modules |
|------------------|-------------|----------------------|----------------------------|
| Market datasets (raw, verified, adjusted, eligible, bias-corrected) | MOD-01 | CAP-01, CAP-02, CAP-03, CAP-04, CAP-14 | MOD-02, MOD-03, MOD-04, MOD-05 (CAP-13 via bias-corrected history) |
| Market context state (regime, trend filter, drift, non-ergodic condition signal) | MOD-02 | CAP-05, CAP-06 | MOD-03 (CAP-07), MOD-05 (CAP-13 regime context), MOD-06 (CAP-23, CAP-27), human (alerts) |
| Signals — technical | MOD-03 | CAP-07 | MOD-04 (validation), MOD-03 (CAP-09) |
| Signals — supplementary (news/sentiment) | MOD-03 | CAP-08 | MOD-03 (CAP-09) only; human only thereafter via CAP-18 advisory report |
| Conflict flags and characterization | MOD-03 | CAP-09 | MOD-05 (CAP-12, as annotation only), MOD-07 (human visibility pre-gate) |
| Validation verdicts and edge evidence | MOD-04 | CAP-10, CAP-11 | MOD-05 (CAP-12) |
| Recommendations (confidence, EV, rankings, allocations, null-state, exit suggestions) | MOD-05 | CAP-12, CAP-13, CAP-15, CAP-16, CAP-17, CAP-20 | MOD-07 (presentation), MOD-08 (post-gate observation), MOD-10 |
| Portfolio State | MOD-09 | CAP-29 | MOD-05 (CAP-13, 15, 16, 20), MOD-06 (CAP-19, 25, 31), MOD-07 (CAP-18 drawdown display) |
| Governance State (four halt-state flags, entry/exit records, compliance signals, limit status) | MOD-06 | CAP-19, CAP-23, CAP-24, CAP-25, CAP-26, CAP-27, CAP-31 | MOD-05 (gating effect on issuance), MOD-07 (active halt states displayed at gate), MOD-11 (event-driven triggers), MOD-10, human (alerts) |
| Human decisions (approvals, rejections, overrides, secondary authorizations) | MOD-07 (capture) | CAP-18 | MOD-08 (CAP-21, 22), MOD-09 (state update pathway), MOD-10 (immutable record) |
| Attribution Records (System Alpha, Human Override Delta, rejected-opportunity expectancy) | MOD-08 | CAP-21, CAP-22 | Human review only; MOD-10 |
| Audit Records | MOD-10 | CAP-30 | Human review only |
| Activation records | MOD-11 | CAP-28 | MOD-10 |

**Evidence for full matrix:** AF SECTION-04 (all 13 information classes with owners and consumers enumerated verbatim). Consumer constraints reflect AF dependency edges in Section 5.1.

---

## SECTION 6 — ALLOWED DEPENDENCY MATRIX

Dependencies are directional and enumerable per AF 5.1. All permitted dependencies are listed below.

### 6.1 Module-Level Allowed Dependencies

| From Module | To Module | Information Transferred | Constitutional Basis |
|-------------|-----------|------------------------|---------------------|
| MOD-11 | All autonomous modules | Activation initiation signal | AF 5.1: "DOM-11 initiates cycles ──▶ all autonomous domains"; SDM-CONST-15 |
| MOD-01 | MOD-02 | Verified, adjusted, eligible market data | AF 5.1: "DOM-01 ──▶ DOM-02" |
| MOD-01 | MOD-03 | Eligible data → CAP-07 | AF 5.1: "DOM-01 ──▶ DOM-03" |
| MOD-01 | MOD-04 | Historical data → CAP-10 | AF 5.1: "DOM-01 ──▶ DOM-04" |
| MOD-01 | MOD-05 | Bias-corrected history → CAP-13 | AF 5.1: "DOM-01 ──▶ DOM-05" |
| MOD-02 | MOD-03 | Trend filter, regime context → CAP-07 | AF 5.1: "DOM-02 ──▶ DOM-03" |
| MOD-02 | MOD-05 | Regime context → CAP-13 | AF 5.1: "DOM-02 ──▶ DOM-05" |
| MOD-02 | MOD-06 | Non-ergodic condition signal → CAP-23, CAP-27 | AF 5.1: "DOM-02 ──▶ DOM-06" |
| MOD-03 | MOD-04 | Technical signals → CAP-10 | AF 5.1: "DOM-03 ──▶ DOM-04" |
| MOD-03 | MOD-05 | Conflict flag annotation only → CAP-12 | AF 5.1: "DOM-03 ──▶ DOM-05"; GOV-VAL05 (annotation only, not computation) |
| MOD-03 | MOD-07 | Supplementary signal set → CAP-18 advisory report | AF 5.1: "DOM-03 ──▶ DOM-07"; GOV-VAL05 Rule 4 |
| MOD-04 | MOD-05 | Validated signals → CAP-12 | AF 5.1: "DOM-04 ──▶ DOM-05" |
| MOD-05 | MOD-07 | Complete advisory package → CAP-18 | AF 5.1: "DOM-05 ──▶ DOM-07" |
| MOD-09 | MOD-05 | Portfolio state → CAP-13, 15, 16, 20 | AF 5.1: "DOM-09 ──▶ DOM-05" |
| MOD-09 | MOD-06 | Portfolio state → CAP-19, CAP-31; drawdown → CAP-25 | AF 5.1: "DOM-09 ──▶ DOM-06" |
| MOD-09 | MOD-07 | Drawdown status → CAP-18 display | AF 5.1: "DOM-09 ──▶ DOM-07" |
| MOD-06 | MOD-05 | Halt gating on recommendation issuance (control dependency) | AF 5.1: "DOM-06 ──▶ DOM-05" |
| MOD-06 | MOD-07 | Active halt states → CAP-18 display | AF 5.1: "DOM-06 ──▶ DOM-07" |
| MOD-06 | MOD-11 | Governance/risk events → Mode 3 event-driven activation | AF 5.1: "DOM-06 ──▶ DOM-11"; ADR-001 event boundary |
| MOD-07 | MOD-08 | Recommendations + human actions (post-gate, read-only) | AF 5.1: "DOM-07 ──▶ DOM-08" |
| MOD-07 | MOD-09 | Human-confirmed trade actions (via external execution — exits system boundary, re-enters through authoritative record) | AF 5.1: "DOM-07 ──▶ DOM-09"; AF 5.3 circularity analysis |
| ALL | MOD-10 | All events from all capabilities | AF 5.1: "ALL DOMAINS ──▶ DOM-10 (terminal sink)" |

### 6.2 Critical Blocking Gates (sequential enforcement, no exceptions)

| Gate | Located In | Blocks | Constitutional Basis |
|------|-----------|--------|---------------------|
| CAP-02 (Data Cross-Verification) | MOD-01 | All signal logic in MOD-03, MOD-04, MOD-05 | SDM-02 Rule 2; SDM-05 Rule 1; SADR Section 5 |
| CAP-10 (Walk-Forward Validation) | MOD-04 | Confidence scoring (CAP-12) in MOD-05 | SDM-05 Rule 2; SADR Section 5 |
| CAP-18 (Human Approval Gate) | MOD-07 | All trade action — no exceptions, no bypass | SDM-CONST-06; SADR Section 5 |

---

## SECTION 7 — FORBIDDEN DEPENDENCY MATRIX

Six prohibited dependency classes from AF 5.4, explicitly enumerated at module level.

| Prohibition ID | Forbidden Dependency | Constitutional Basis | ADR-000 Principle |
|---------------|---------------------|---------------------|------------------|
| FORB-01 | MOD-08 → MOD-01, MOD-02, MOD-03, MOD-04, MOD-05, MOD-06 (any write edge) | AF 5.4: "DOM-08 → any recommendation, validation, confidence, EV, ranking, allocation, or governance logic"; CONSTRAINT-07; SDM-13 Rules 8, 10 | P-08 |
| FORB-02 | MOD-10 → any module (any outbound edge) | AF 5.4: "DOM-10 → any capability"; CAP-30 Boundary | P-07 |
| FORB-03 | MOD-03 supplementary signals (CAP-08 output) → MOD-05 computation (any computational input to CAP-12, CAP-13, CAP-15, CAP-16) | AF 5.4: "DOM-03 supplementary signals → DOM-05 computation (GOV-VAL05 Rule 1)"; GOV-VAL05 Rule 1 | P-09 |
| FORB-04 | Any module → broker/execution venue (any outbound interface toward market) | AF 5.4: "Any domain → broker/execution venue"; GOV-01 Rule 1; GOV-02 Rules 4–5; CONSTRAINT-01 | P-03 |
| FORB-05 | Any signal logic (MOD-03, MOD-04, MOD-05) ← unverified data (any data that has not passed CAP-02) | AF 5.4: "Any signal logic ← unverified data (SDM-02 Rule 2)" | P-03, P-10 |
| FORB-06 | Any path from any module to a trade action that bypasses MOD-07 (CAP-18) | AF 5.4: "Any path around CAP-18 to a trade action"; SDM-CONST-06 | P-03 |

### Additional Module-Level Prohibitions Derived from ADR-000

| Prohibition ID | Forbidden Dependency | Constitutional Basis | ADR-000 Principle |
|---------------|---------------------|---------------------|------------------|
| FORB-07 | Any module maintaining a private copy of portfolio state consumed by other modules | AF 5.5; SADR CHANGE-01/CHANGE-02 history | P-05 |
| FORB-08 | Conflict flag from CAP-09 (MOD-03) entering CAP-12 (MOD-05) as a numeric modifier to the confidence score | SADR_AMENDMENT_VAL-05; AF DOM-03 GOV-VAL05 Boundary | P-09 |
| FORB-09 | MOD-11 activation events entering any module as data inputs consumed by computational logic | AF 5.3 secondary check: "activation is initiation, not data dependency" | P-10 |
| FORB-10 | MOD-06 halt states sharing any state variable, trigger evaluator, or exit mechanism across two or more halt-state capabilities | SDM-CONST-14; AF DOM-06 Independence Constraint | P-06 |

---

## SECTION 8 — EVENT BOUNDARY CONTRACT

### 8.1 Constitutional Scope of Event Signaling

**Evidence:** ADR-001 Section 6: "The event pattern is applied only where the constitution itself characterizes the relationship as event-based." The event pattern is constitutionally bounded to two relationship types.

### 8.2 Allowed Event Relationships

**Event Type 1: MOD-11 Activation Events**

| Event | Producer | Consumer | Constitutional Basis |
|-------|----------|----------|---------------------|
| Scheduled activation | MOD-11 (Mode 1 — schedule trigger) | All autonomous modules | SDM-CONST-15 Mode 1; SADR Section 8 |
| On-demand activation | MOD-11 (Mode 2 — human request) | All autonomous modules | SDM-CONST-15 Mode 2; SADR Section 8 |
| Event-driven activation | MOD-11 (Mode 3 — governance/risk/portfolio trigger) | All autonomous modules | SDM-CONST-15 Mode 3; SADR Section 8; AF 5.1 |

**Event Type 2: MOD-06 Governance Signaling to MOD-11**

| Event | Producer | Consumer | Constitutional Basis |
|-------|----------|----------|---------------------|
| Governance/risk event trigger | MOD-06 | MOD-11 (Mode 3 entry) | AF 5.1: "DOM-06 ──▶ DOM-11 [governance/risk events → Mode 3 event-driven activation]"; SADR Section 8 Mode 3; AF 5.3 secondary check |

**Nature of these events:** Initiation signals, not data dependencies. MOD-06 publishes a governance/risk event; MOD-11 consumes it as a Mode 3 initiation trigger. The event carries initiation authority, not information that flows into computational logic.

**Evidence:** AF 5.3: "activation is initiation, not data dependency; CAP-28's output is an initiated cycle, not an input consumed by CAP-23/CAP-31 logic. No data circularity exists."

### 8.3 Forbidden Event Relationships

| Forbidden Event Category | Reason | Constitutional Basis |
|--------------------------|--------|---------------------|
| Recommendation pipeline events (MOD-03 → MOD-04 → MOD-05 as event subscriptions) | The blocking gates (CAP-02, CAP-10, CAP-18) require synchronous sequential enforcement; asynchronous event routing creates windows where gates can be bypassed | ADR-001 Section 4 (Candidate C elimination); ADR-001 Section 7 R2; SADR Section 5 blocking gates |
| Portfolio state update events (any module subscribing to portfolio change events) | Portfolio state has a single authoritative source (MOD-09); event-based state propagation creates private state derivatives | ADR-000 P-05; AF 5.5; FORB-07 |
| Attribution feedback events (MOD-08 publishing to any MOD-01..06 subscriber) | Attribution is read-only; event publication from MOD-08 to computational modules is a write relationship regardless of framing | ADR-000 P-08; FORB-01; SDM-13 Rules 8, 10 |
| Sentiment signal events (MOD-03 publishing supplementary signals to a bus where MOD-05 subscribes) | The prohibited dependency FORB-03 applies regardless of whether the routing mechanism is direct call or event subscription | ADR-000 P-09; FORB-03; GOV-VAL05 Rule 1 |
| Audit feedback events (MOD-10 publishing to any subscriber) | Audit is a terminal sink with zero permitted outbound edges | ADR-000 P-07; FORB-02; CAP-30 Boundary |
| Halt-state shared event bus spanning multiple halt capabilities | The four halt states must be constitutionally independent; a shared event bus creates undeclared coupling between their detection timing and state transitions | ADR-000 P-06; FORB-10; SDM-CONST-14 |
| Any cross-module event relationship not listed in Section 8.2 | The event pattern is constitutionally bounded; "consistency" or "convenience" are not constitutional justifications for expansion | ADR-001 Section 7 R9; ADR-001 Risk 2 |

---

## SECTION 9 — AUTHORITY BOUNDARY MODEL

### 9.1 Authority Class Assignment by Module

| Module | Authority Class | Scope Within Module | Constitutional Ceiling |
|--------|----------------|---------------------|----------------------|
| MOD-01 | AUTONOMOUS_RESEARCH | Ingest, verify, adjust, filter, correct market data | No execution authority; no market action |
| MOD-02 | AUTONOMOUS_RESEARCH | Classify, detect drift, alert on regime shifts | No execution authority; no market action |
| MOD-03 | MIXED (AUTONOMOUS_RESEARCH + SHARED_AUTHORITY) | CAP-07, CAP-08: generate signals autonomously; CAP-09: system flags, human decides at CAP-18 | No execution authority; sentiment advisory only |
| MOD-04 | AUTONOMOUS_RESEARCH | Validate, verify statistical edge, reject signals | No execution authority; K-fold prohibited |
| MOD-05 | AUTONOMOUS_RESEARCH | Compute, rank, allocate, declare null-state, recommend exits | No execution authority; all outputs advisory |
| MOD-06 | AUTONOMOUS_RESEARCH | Detect conditions, manage halt states, gate recommendation issuance | No execution authority; governs recommendations only |
| MOD-07 | HUMAN_APPROVAL | Present package only (system); approve/reject/override (human) | Human is sole decision authority; no auto-approval |
| MOD-08 | AUTONOMOUS_RESEARCH (Observation Only) | Observe, measure deltas, report insights | No write authority to any other module |
| MOD-09 | AUTONOMOUS_RESEARCH | Maintain and provide portfolio state representation | No write authority over actual portfolio; state from human-confirmed trades only |
| MOD-10 | AUTONOMOUS_RESEARCH | Record immutably | No feedback to any capability |
| MOD-11 | AUTONOMOUS_RESEARCH | Initiate cycles under three authorized modes | No execution authority; initiation only |

### 9.2 Authority Anti-Leakage Verification

Each of the six anti-leakage checks from AF 3.3 is verified at the module level:

**Check 1 — No execution leakage:**
No module holds any authority toward the broker/market. MOD-06 halt states govern recommendation authority only (SDM-CONST-14). MOD-06 enforcement is explicitly non-executing (GOV-01 Rule 1, GOV-02 Rules 4–5). MOD-11 activation grants no execution authority (SDM-CONST-15). ✅

**Check 2 — No attribution write leakage:**
MOD-08 has no permitted write edge to MOD-01 through MOD-06 (FORB-01; CONSTRAINT-07; SDM-13 Rules 8, 10). ✅

**Check 3 — No audit feedback leakage:**
MOD-10 has no outbound edge to any module (FORB-02; CAP-30 Boundary). ✅

**Check 4 — No sentiment computational leakage:**
MOD-03's supplementary signals reach MOD-05 computation nowhere (FORB-03; GOV-VAL05 Rules 1–4). They reach the human only via MOD-07 advisory report. ✅

**Check 5 — No portfolio write leakage:**
MOD-09 represents state; it never originates actual portfolio state (CONSTRAINT-01). State changes originate only from human-confirmed external execution. ✅

**Check 6 — No gate bypass:**
Every trade-action pathway passes through MOD-07 (FORB-06; SDM-CONST-13). No module emits anything executable. ✅

---

## SECTION 10 — GOVERNANCE ISOLATION MODEL

### 10.1 What MOD-06 Gates and What It Does Not Gate

**Constitutional finding (from AF 6.1):** All four halt states gate recommendation issuance only. No halt state suspends research, analysis, monitoring, attribution, audit, or reporting functions.

**Gating surface:** The issuance boundary of MOD-05 outputs (recommendations, allocations, null-state, exit suggestions) and their presentation at MOD-07.

**What MOD-06 halt states gate:**

| Halt State | Capability | Blocked Output Type |
|-----------|-----------|---------------------|
| State 1 — Governance Halt (CAP-25) | MOD-05 issuance | All new recommendations; all new capital allocation recommendations |
| State 2 — Governance Lockout (CAP-26) | MOD-05 issuance | All new recommendations; all new allocation recommendations; all new capital deployment recommendations |
| State 3 — Conditional Suspension (CAP-27) | MOD-05 issuance | Affected-domain-only recommendations (scaled down or suspended) |
| State 4 — Hard Deterministic Halt (CAP-24) | MOD-05 issuance | Position recommendations that would cause or sustain the limit breach |

**What MOD-06 halt states do NOT gate (all must continue under any active halt state):**
- MOD-01: market data ingestion, verification, adjustment (continuing provides fresh data for when halt clears)
- MOD-02: regime classification, drift detection, alerts (continuing is required by SDM-CONST-14 State 3 condition monitoring)
- MOD-03: signal generation (technical and supplementary)
- MOD-04: statistical validation
- MOD-06 own detection functions: CAP-31 (required to continue for Lockout exit detection, GOV-02 Rule 3), CAP-23 (required to continue for Suspension exit detection, SDM-15 Rule 14), CAP-19 (required to continue for Hard Halt exit detection)
- MOD-07: presentation (human must still receive the halt-state advisory package and escalation reports)
- MOD-08: attribution observation (post-gate read-only, not blocked by halt)
- MOD-09: portfolio state maintenance (required for MOD-06 detection functions to operate)
- MOD-10: audit recording (required for all halt entry/exit logging, SDM-15 Rule 14)
- MOD-11: activation (governance events continue to trigger review cycles)

**Evidence:** AF 6.1; GOV-01 Rule 4; GOV-02 Rule 3; SDM-15 Rule 14; SDM-CONST-15 (activation authority is unconditioned on halt states).

### 10.2 Per-Halt-State Isolation

**State 1 — Governance Halt (CAP-25 in MOD-06)**

Entry detector: MOD-09 drawdown ≥ 5% → CAP-25
Entry authority: Autonomous (drawdown threshold breach)
Effect: Blocks all new MOD-05 recommendations and allocation recommendations
Reporting continues: GOV-01 Rule 4 — critical risk escalation report generated for human review
Exit: Explicit human resumption authorization → CAP-25

**State 2 — Governance Lockout (CAP-26 in MOD-06)**

Entry detector: CAP-31 governance violation signal → CAP-26
Entry authority: Autonomous on CAP-31 signal
Effect: Blocks all new MOD-05 recommendations, allocations, and capital deployment recommendations
Monitoring continues: GOV-02 Rule 3 — CAP-31 and CAP-29 continue operating; restoration detected automatically
Exit: CAP-31 governance restoration signal → CAP-26 (automatic on detected corrective action; no additional human authorization)

**State 3 — Conditional Recommendation Suspension (CAP-27 in MOD-06)**

Entry detector: CAP-23 adverse condition signal → CAP-27
Entry authority: Autonomous on CAP-23 signal
Effect: Suspends or scales down affected-domain MOD-05 recommendations
Condition monitoring continues: SDM-15 Rule 14 — CAP-23 continues detecting; exit is condition-driven
Exit: CAP-23 condition clearance signal → CAP-27 (automatic; not human-authorization-driven)
Both entry and exit logged with condition state (SDM-15 Rule 14)

**State 4 — Hard Deterministic Halt (CAP-24 in MOD-06)**

Entry detector: CAP-19 position/concentration limit breach → CAP-24
Entry authority: Autonomous on CAP-19 breach
Effect: Blocks position recommendations that would cause or sustain the breach; human-visible alert
Limit monitoring continues: CAP-19 continues monitoring for return within limits
Exit: Human acknowledgment + confirmed return within limits → CAP-24

### 10.3 Independence Preservation

The four halt states operate as four independent state elements within MOD-06. Each is owned by a distinct capability (CAP-24, CAP-25, CAP-26, CAP-27). Each has its own entry authority, active state, and exit authority. No shared mechanism spans them.

When multiple states are simultaneously active, MOD-05 recommendation issuance is blocked if blocked by any active state. Restoration of one state does not change any other state.

**Evidence:** SDM-CONST-14; SADR Section 5 "Halt State Independence"; AF DOM-06 Independence Constraint; ADR-000 P-06; FORB-10.

---

## SECTION 11 — AUDIT ISOLATION MODEL

### 11.1 Structural Position

MOD-10 occupies the terminal position in the dependency graph. Its structural role is:

- **Receives from:** All modules — all capability events, system decisions, human decisions, override events, halt state entries and exits with condition state, validation results, conflict resolutions, recommendation outputs, activation events, and compliance evaluation events
- **Writes to:** Nothing within the system. Zero outbound edges.
- **Human access:** Human review only — constitutionally authorized; not a system feedback path

**Evidence:** AF 5.1: "ALL DOMAINS ──▶ DOM-10 (Audit) [terminal sink; no outbound edges]." AF SECTION-04: "Constitutionally entitled consumers: Human review only." CAP-30 Boundary: "Recording only. Does not process events. Does not feed back into any capability."

### 11.2 Coverage Requirement

Every SDM decision domain (SDM-02 through SDM-15) carries an explicit Audit clause. MOD-10 must discharge all of them. Required records include:

| Domain | Required Audit Record | SDM Source |
|--------|-----------------------|------------|
| SDM-02 | Excluded assets and triggered filter rules; cross-verification records | SDM-02 Audit |
| SDM-03 | Regime shift triggers; concept drift metrics; walk-forward bounds | SDM-03 Audit |
| SDM-04 | Signal evidence weighting; technical-vs-news conflict resolution rationale | SDM-04 Audit |
| SDM-05 | Cross-validation results; outlier detection; concept drift metrics | SDM-05 Audit |
| SDM-06 | Confidence computation records; source reliability weights | SDM-06 Audit |
| SDM-07 | Probability-adjusted inputs; drawdown compliance gates; survivorship bias validation | SDM-07 Audit |
| SDM-08 | Ranking logic execution (proving non-equal-weighting); null-state events | SDM-08 Audit |
| SDM-09 | Conviction weights; capital distribution justification; scale-down events | SDM-09 Audit |
| SDM-10 | Original system recommendation vs. final human action (immutable); all approvals, rejections, overrides | SDM-10 Audit |
| SDM-11 | Active position counts vs. targets; drawdown threshold warnings; concentration risk actions | SDM-11 Audit |
| SDM-12 | Slippage assumptions; extension justification evidence; exit rationale | SDM-12 Audit |
| SDM-13 | Attribution events; system alpha outcomes; human override deltas per trade cycle | SDM-13 Audit |
| SDM-15 | Human approvals/rejections; drawdown limit tests; triggered halts; scaling adjustments; halt entry/exit with condition state | SDM-15 Audit; SDM-15 Rule 14 |

### 11.3 Immutability

Audit records are immutable. Once written, no system operation may modify or delete them.

**Evidence:** SADR CHANGE-06 (replaced "append-only" with "immutable"); CAP-30 Outputs; ADR-000 P-07.

### 11.4 No Runtime Read-Back

No module may read from MOD-10 at runtime to influence its computational logic. The prohibition applies to all direct and indirect paths: a component that reads audit records and uses them to calibrate a formula, adjust a weight, or modify a threshold would violate this isolation even if the read is not direct.

**Evidence:** AF 5.4 FORB-02; CAP-30 Boundary; FORB-02.

---

## SECTION 12 — CONSTITUTIONAL COMPLIANCE VALIDATION

### 12.1 Validation Against SDM_V2.3

| SDM Requirement | Satisfied By | Evidence |
|----------------|-------------|---------|
| Human approval mandatory before any trade action (SDM-CONST-06) | MOD-07 is the sole HUMAN_APPROVAL module; CAP-18 is the mandatory blocking gate; FORB-06 prohibits all bypass paths | SADR Section 5; AF 5.2; Section 6 of this document |
| All outputs advisory; no output constitutes executable trade order (SDM-CONST-13) | MOD-05 information class "Recommendations" is advisory only; MOD-07 owns no executable authority | AF SECTION-04; MOD-07 Module Catalog entry |
| Architecture must remain modular and reversible (SDM-CONST-12) | 11 modules with explicit boundary contracts; no shared mutable state across module lines as required; future service extraction enabled | Section 3 module catalog; Section 6 dependency matrix |
| Four constitutionally distinct halt states (SDM-CONST-14) | Four independent capabilities (CAP-24, CAP-25, CAP-26, CAP-27) in MOD-06; FORB-10 prohibits shared state | Section 10; ADR-000 P-06 |
| Attribution read-only (SDM-13 Rules 8, 10) | MOD-08 has FORB-01 prohibiting all write edges to MOD-01..06 | Section 7; Section 9.2 Check 2 |
| Walk-forward mandatory; K-fold prohibited (SDM-03 Rule 1, SDM-05 Rule 2) | MOD-04 owns CAP-10 with this constitutional constraint preserved verbatim | Section 3 MOD-04 |
| Deterministic execution (SDM-15 Rule 3) | MOD-05 confidence computation derives exclusively from technical evidence; FORB-03 prohibits sentiment entry | Section 3 MOD-05; Section 7 FORB-03 |
| Open menu simultaneous presentation (SDM-08 Rule 8) | MOD-07 presentation constraint binding; sequential forced selection prohibited | Section 3 MOD-07 |

### 12.2 Validation Against VAL05_OWNER_DECISION_RESOLUTION

| GOV-VAL05 Rule | Satisfied By | Evidence |
|---------------|-------------|---------|
| GOV-VAL05 Rule 1: Confidence computation derives exclusively from technical evidence; sentiment not a formula input | MOD-05 computation purity constraint; FORB-03 at module boundary | Section 3 MOD-05; Section 7 FORB-03 |
| GOV-VAL05 Rule 2: News modifies human judgment, not computational score | MOD-03 supplementary signals route only to MOD-07 advisory report; FORB-03 prohibits computational routing | Section 3 MOD-03 GOV-VAL05 Routing Constraint; Section 7 |
| GOV-VAL05 Rule 4: Sentiment appears as named advisory section distinct from computational outputs | MOD-03 owns the supplementary signal information class; it is a separate section in the MOD-07 advisory package composition | Section 3 MOD-03; Section 3 MOD-07 Advisory Package Composition |
| GOV-VAL05 Rule 5: VAL-07, VAL-11, VAL-15 pathways closed | No module accepts sentiment-to-confidence-weight, sentiment-to-Kelly-fraction, or sentiment-to-position-sizing as an input interface; FORB-03 and FORB-08 prohibit these | Section 7 FORB-03, FORB-08 |

### 12.3 Validation Against SADR_V2.1

| SADR Constraint | Satisfied By | Evidence |
|----------------|-------------|---------|
| CONSTRAINT-01: No capability initiates, executes, places, modifies, or cancels trade orders | FORB-04 prohibits any module → broker interface; zero execution authority across all 11 modules | Section 7 FORB-04; Section 9 |
| CONSTRAINT-07: Attribution read-only | MOD-08 FORB-01; zero write edges to recommendation/governance logic | Section 7 FORB-01; Section 9.2 |
| CONSTRAINT-08: Walk-forward mandatory; K-fold prohibited | MOD-04 constitutional constraint | Section 3 MOD-04 |
| CONSTRAINT-09: Open Menu; sequential forced selection prohibited | MOD-07 presentation constraint (binding) | Section 3 MOD-07 |
| CONSTRAINT-10: Activation modes do not grant execution authority | MOD-11 authority ceiling; activation is initiation only | Section 3 MOD-11; Section 9 |
| All 31 capabilities assigned exactly once | Capability Allocation Matrix | Section 4 |

### 12.4 Validation Against ARCHITECTURE_FOUNDATION_V1

| AF Requirement | Satisfied By | Evidence |
|---------------|-------------|---------|
| 11 constitutional domains | 11 modules, 1:1 mapping | Section 2.2 |
| All 31 capabilities assigned exactly once | Section 4 matrix | Section 4 |
| 13 information classes, single ownership | Section 5 matrix | Section 5 |
| Six prohibited dependencies (AF 5.4) | FORB-01 through FORB-06 | Section 7 |
| Three blocking gates (AF 5.2) | CAP-02 in MOD-01, CAP-10 in MOD-04, CAP-18 in MOD-07 | Section 6.2 |
| Acyclic internal dependency graph (AF 5.3) | All allowed dependencies in Section 6 are directional; the DOM-07→DOM-09 path exits through human (external) | Section 6; AF 5.3 circularity analysis |
| Halt states gate issuance only; monitoring continues (AF 6.1) | Section 10 governance isolation model | Section 10 |

### 12.5 Validation Against ADR-000 Architecture Principles

| Principle | Satisfied By |
|-----------|-------------|
| P-01: Constitution Before Optimization | Module design derives from constitutional authority only; no optimization criteria introduced |
| P-02: Authority Before Automation | MOD-07 is HUMAN_APPROVAL only; presentation constraint prohibits sequential pressure; no timeout-based approval |
| P-03: Human Approval Cannot Be Bypassed | FORB-06 prohibits all bypass paths to trade action; CAP-18 in MOD-07 is the sole blocking gate |
| P-04: Single Owner Per Information Class | Section 5 matrix: 13 classes, 13 owners, zero dual ownership |
| P-05: No Hidden Portfolio State | MOD-09 is single authoritative source; FORB-07 prohibits private derivatives |
| P-06: No Governance State Coupling | Four halt capabilities independent within MOD-06; FORB-10 prohibits shared state |
| P-07: Audit Is Write-Only | MOD-10 terminal sink; FORB-02 prohibits outbound edges; zero runtime read-back |
| P-08: Attribution Is Read-Only | MOD-08 Observation Authority only; FORB-01 prohibits write edges to MOD-01..06 |
| P-09: Sentiment Is Advisory Only | FORB-03, FORB-08 prohibit supplementary signals entering computation; GOV-VAL05 routing constraint enforced |
| P-10: Dependencies Flow One Direction | All allowed dependencies in Section 6 are directional; apparent DOM-07→DOM-09 cycle is broken at system boundary |
| P-11: Domain Boundaries Preserve Capability Boundaries | 1:1 domain-to-module mapping; all 31 capabilities assigned exactly once without splitting or merging |
| P-12: Architecture Must Remain Technology Neutral | No module definition references any technology; all boundaries are constitutional, not implementation-derived |

### 12.6 Validation Against ADR-001 Architectural Style Selection

| ADR-001 Decision | Satisfied By |
|-----------------|-------------|
| Modular Monolith core | 11 modules with explicit boundary contracts; no distributed coordination; blocking gates are synchronous sequential enforcement |
| Bounded event signaling — allowed only: MOD-11 activation, MOD-06 governance events to MOD-11 | Section 8.2 allows only these two types; Section 8.3 prohibits all others |
| Event scope creep risk (ADR-001 Risk 2) | FORB-09 (activation events are initiation-only, not data inputs); Section 8.3 explicit prohibited event list |
| Governance continuity under halt risk (ADR-001 Risk 3) | Section 10 explicit enumeration of what each halt state does and does not gate |
| Module boundary erosion risk (ADR-001 Risk 1) | FORB-01 through FORB-10 explicit prohibition register; Section 12 compliance validation |

---

## SECTION 13 — ARCHITECTURE READINESS VERDICT

### Verdict: ADR-003 MAY PROCEED

**Evidence:**

**E1 — All 31 capabilities are assigned.**
Every SADR capability has exactly one module assignment. Zero orphans. Zero duplicates. The Capability Allocation Matrix in Section 4 is complete and traceable.

**E2 — All 13 information classes have a single authoritative owner.**
The Information Ownership Matrix in Section 5 assigns every information class to one owning module with its authorized consumer list. Zero dual ownership. Zero unowned classes.

**E3 — All dependency permissions are explicit and traceable.**
The Allowed Dependency Matrix in Section 6 enumerates every permitted module-to-module information flow with constitutional authority. The Forbidden Dependency Matrix in Section 7 enumerates 10 specific prohibitions.

**E4 — Authority classes are structurally assigned and isolated.**
29 capabilities carry AUTONOMOUS_RESEARCH across 9 modules. CAP-09 carries SHARED_AUTHORITY in MOD-03. CAP-18 carries HUMAN_APPROVAL in MOD-07. The three authority classes are structurally distinguishable. Anti-leakage is verified in Section 9.2.

**E5 — Event boundaries are constitutionally scoped and explicitly bounded.**
Two event relationship types are authorized. Eight prohibited event categories are enumerated. The event pattern does not expand into the recommendation pipeline or blocking gate paths.

**E6 — Governance isolation is fully characterized.**
Section 10 specifies exactly which outputs each halt state blocks, which functions continue under each halt state, and how each state's independence is preserved within MOD-06.

**E7 — Audit isolation is fully characterized.**
Section 11 confirms MOD-10's terminal sink status, enumerates required audit coverage from SDM-02 through SDM-15, and establishes the immutability and no-runtime-read-back constraints.

**E8 — Full constitutional compliance is validated.**
Section 12 validates ADR-002 against all six authority levels (SDM, VAL05, SADR, Architecture Foundation, ADR-000, ADR-001). No conflicts found.

**ADR-003 Scope Guidance (non-binding — for orientation only):**

ADR-003 should address:
- Intra-module design: how capabilities are organized within each module (internal capability ordering, within-module information flow contracts)
- Cross-cutting design questions not resolvable at the module level (e.g., how activation initiation signals are structured, how the halt-gating control dependency from MOD-06 to MOD-05 is structurally expressed at module boundary)
- Governance continuity execution model: the specific design pattern within MOD-06 that ensures detection functions (CAP-31, CAP-23, CAP-19) continue operating during active halt states
- Open validation items as extension point contracts: for each open VAL item that affects a module boundary, what interface abstraction is used

ADR-003 must not:
- Select specific technologies, databases, APIs, or infrastructure
- Design deployment architecture
- Resolve constitutionally deferred SDM-14
- Reopen any authority-level decision

---

*ADR-002 derives its authority from SDM_V2.3, VAL05_OWNER_DECISION_RESOLUTION, SADR_V2.1, ARCHITECTURE_FOUNDATION_V1, ADR-000_ARCHITECTURE_PRINCIPLES, and ADR-001_ARCHITECTURAL_STYLE_SELECTION. It introduces no implementation decisions, no technology selections, no database designs, no API specifications, and no deployment architecture. It performs capability-to-module realization within the frozen architectural style.*

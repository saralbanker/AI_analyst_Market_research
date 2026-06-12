# ADR-000 — ARCHITECTURE PRINCIPLES
## Constitutional Principle Derivation

**Derived By:** Constitutional Analysis Mode (4D+ Method)
**Authority Hierarchy:**
- Level 1: SDM_V2.3 (FROZEN — FINAL CANONICAL)
- Level 2: VAL05_OWNER_DECISION_RESOLUTION (RESOLVED — Option B, advisory-only)
- Level 3: SADR_V2.1 (CERTIFIED)
- Level 4: ARCHITECTURE_FOUNDATION_V1

**Status:** CANDIDATE FOR OWNER REVIEW
**Scope:** Defines the constitutional rules that every future ADR must obey. Not an architecture design document. Not a technology strategy document. Not an implementation document.

---

## DERIVATION LOG

### Phase 1 — DECONSTRUCT

**Constitutional rules extracted from SDM_V2.3:**
- Human approval is mandatory before any trade action (SDM-CONST-06)
- All system outputs are advisory; no output constitutes an executable trade order (SDM-CONST-13)
- Autonomous execution is prohibited without exception (SDM-CONST-06)
- Architecture must remain modular and reversible (SDM-CONST-12)
- Four constitutionally distinct, non-overlapping halt states govern recommendation authority only (SDM-CONST-14)
- Halt states may be simultaneously active; restoration of one never restores another (SDM-CONST-14)
- Attribution possesses Observation Authority only; no write authority over future recommendation behavior (SDM-13 Rules 8, 10)
- Attribution may not modify signal, validation, confidence, EV, ranking, allocation, or governance logic (SDM-13 Rule 8)
- Walk-forward cross-validation mandatory; K-fold constitutionally prohibited (SDM-03 Rule 1, SDM-05 Rule 2, SDM-07 Rule 3)
- Cash is a valid position; forced capital deployment is prohibited (SDM-CONST-07)
- Technical signals are the primary evidence layer; news is supplementary (SDM-CONST-10)
- AI model evaluations isolated exclusively to the semantic and cognitive domain (SDM-04 Rule 12)

**Constitutional rules extracted from VAL05_OWNER_DECISION_RESOLUTION:**
- Sentiment/news signals do not enter any computational confidence formula, EV formula, ranking formula, or allocation formula (GOV-VAL05 Rule 1)
- SDM-06 Rule 2 is clarified: news modifies the human operator's confidence judgment, not the system's computational score (GOV-VAL05 Rule 2)
- VAL-07, VAL-11, VAL-15 are closed; the pathways they described do not exist (GOV-VAL05 Rule 5)
- Supplementary signals appear in the human-facing advisory report as a named advisory section, distinct from computationally derived scores, rankings, and allocations (GOV-VAL05 Rule 4)
- Conflict flag from CAP-09 flows to CAP-12 as advisory annotation only; it does not computationally modify the confidence score (SADR_AMENDMENT_VAL-05)

**Ownership rules extracted from ARCHITECTURE_FOUNDATION_V1:**
- One owner per information class; owners are sole producers; all other domains are read-only consumers (AF SECTION-04)
- DOM-09 is the single source of portfolio state; no consumer may maintain a private derivative (AF 5.5)
- DOM-10 (Audit) has no output edge to any capability — terminal sink (AF SECTION-04)
- DOM-08 (Attribution) has no write edge to any logic in DOM-01 through DOM-06 (AF 3.3)
- DOM-03 supplementary signals route only to the advisory report; they never enter computation (AF DOM-03 GOV-VAL05 Boundary)
- Reports are composite artifacts; ownership of each section never transfers at composition (AF 4.1)

**Dependency rules extracted from ARCHITECTURE_FOUNDATION_V1:**
- CAP-02 blocks all signal logic until cross-verification passes (AF 5.2)
- CAP-10 blocks confidence scoring until walk-forward validation passes (AF 5.2)
- CAP-18 blocks all trade action — no exceptions, no bypass (AF 5.2)
- Dependencies flow DAG-only (no internal cycles); the DOM-07→DOM-09 path exits the system boundary through the human (AF 5.3)
- Six prohibited dependency classes defined and binding on all derived architectures (AF 5.4)
- Governance continuity: monitoring, audit, reporting functions are not gated by halt states (AF 6.1)

**Governance rules extracted from SADR_V2.1:**
- CONSTRAINT-01: No capability may initiate, execute, place, modify, or cancel a trade order
- CONSTRAINT-07: Attribution carries read-only observational authority; it may not write to any recommendation, signal, validation, confidence, ranking, allocation, or governance logic
- CONSTRAINT-08: Walk-forward mandatory for all statistical validation; K-fold constitutionally prohibited
- CONSTRAINT-09: All EV-filtered opportunities presented simultaneously as Open Menu; sequential forced selection prohibited
- Authority classes: AUTONOMOUS_RESEARCH, SHARED_AUTHORITY, HUMAN_APPROVAL — all three preserved unchanged from SADR

---

### Phase 2 — DIAGNOSE

**Recurring constitutional themes identified:**

Theme A — Human Authority Is Absolute and Non-Delegable
Appears in: SDM-CONST-06, SDM-CONST-13, SDM-10, GOV-01, GOV-02, SDM-13 Rule 9, CONSTRAINT-01, CONSTRAINT-09, AF DOM-07, AF 3.3 anti-leakage check 1 and 6.

Theme B — Single Information Owner Per Class
Appears in: AF SECTION-04 (13 information classes, each with exactly one owner), AF 5.5 hidden coupling controls, SADR CHANGE-01 (stripped compliance evaluation from CAP-29), SADR CHANGE-02 (created CAP-31 as the designated evaluator).

Theme C — Governance Governs Recommendations, Not Continuity
Appears in: SDM-CONST-14, GOV-01 Rule 4, GOV-02 Rule 3, SDM-15 Rule 14, AF 6.1, SADR Section 7.

Theme D — Sentiment Is Advisory, Computation Is Technical
Appears in: SDM-CONST-10, SDM-04 Rule 12, GOV-VAL05 (all eight criteria), SADR_AMENDMENT_VAL-05, AF DOM-03 GOV-VAL05 Boundary, AF Section 4 "Signals — supplementary."

Theme E — Read-Only Observation Cannot Self-Authorize Change
Appears in: SDM-13 Rules 8, 9, 10; CONSTRAINT-07; AF DOM-08; AF 3.3 anti-leakage check 2.

Theme F — Audit Is Absolute and Terminal
Appears in: Every SDM Audit clause (SDM-02 through SDM-15), CAP-30 Boundary ("does not process events; does not feed back"), AF DOM-10, AF SECTION-04 "Audit Records," AF 5.4 prohibited dependency "DOM-10 → any capability."

Theme G — Dependencies Flow In One Direction
Appears in: SADR Section 5 (full dependency chain), AF 5.1 domain-level dependency direction, AF 5.2 blocking gates, AF 5.3 circularity analysis (only apparent cycle broken at system boundary), AF 5.4 prohibited dependencies.

Theme H — Domain Boundaries Encode Constitutional Distinctions
Appears in: AF 2.0 derivation method (three evidence tests), AF DOM-07 grouping evidence (authority cohesion forbids merging HUMAN_APPROVAL into autonomous domain), AF DOM-06 independence constraint (four halt states must not be merged into single state machine), AF DOM-09 (information cohesion: absorbing portfolio state into a consumer would create hidden coupling).

Theme I — Architecture Must Not Bake In Technology
Appears in: SDM-CONST-12 (modular, replaceable, configurable, independently evolvable), SDM Part V invariants (excludes architecture decisions from constitutionally valid content), SDM Part VI (all unresolved VAL items are implementation/calibration, not architectural structure), SADR CLASS_B/C/D classification (open items are "generic interface sufficient").

---

### Phase 3 — INVESTIGATE

Each of the 12 candidate principles is tested against authority. Evidence is evaluated across all four levels.

**Candidate P-01: Constitution Before Optimization**

Claim: Governance constraints take precedence over performance optimization.

Evidence:
- SDM-CONST-06: Human approval mandatory "without exception." No performance condition is named as an exception.
- SDM-CONST-14: Halt states govern recommendation authority; no efficiency escape clause exists.
- GOV-01 Rule 1: Zero autonomous execution "under all circumstances." "All circumstances" forecloses optimization reasoning.
- SDM Part V constitutional invariants: "may not be overridden by any downstream architectural, implementation, or infrastructure decision."
- AF 3.3 anti-leakage: every trade-action pathway must pass through DOM-07; no exception.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-02: Authority Before Automation**

Claim: Human decision authority must not be compressed, bypassed, or approximated by automated logic.

Evidence:
- SDM-CONST-06: Human approval mandatory before any trade action; autonomous execution prohibited "without exception."
- SDM-10 Rule 1: System halts and awaits explicit human approval — not an implicit approval, not a timeout-based approval.
- CONSTRAINT-09: Open Menu simultaneous presentation; sequential forced selection prohibited. This rule exists because sequential presentation can create automation pressure on the human's choice sequence.
- CAP-18 Boundary: "No timeout-based auto-approval. No bypass pathways."
- GOV-VAL05 Criterion 1: Option B chosen precisely because "the human is not receiving a pre-blended number — they are receiving the raw inputs and doing the blending themselves. Option A delegates part of the human's judgment to a formula."

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-03: Human Approval Cannot Be Bypassed**

Claim: No pathway to a trade action may exist that circumvents the human approval gate.

Evidence:
- SDM-CONST-06: Human approval mandatory "without exception."
- SDM-CONST-13: "No output of this system constitutes an executable trade order."
- SADR CONSTRAINT-01: "No capability in this system may initiate, execute, place, modify, or cancel a trade order."
- SADR Section 5: "CAP-18 blocks all trade action — no exceptions, no bypass." This is named as one of three constitutional blocking gates.
- AF 5.2: Same blocking gate preserved verbatim.
- AF 5.4 prohibited dependency: "Any path around CAP-18 to a trade action."
- GOV-01 Rule 1: "The SDM shall not execute buy orders, sell orders, liquidation orders, or emergency market orders under any circumstance."
- GOV-02 Rules 4–5: "The SDM shall not execute trades during Governance Lockout. The SDM shall not modify broker orders during Governance Lockout." (Applies a fortiori beyond Lockout.)

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.** (Distinct from P-02: P-02 concerns the quality and integrity of the human decision; P-03 concerns the structural impossibility of routing around the gate entirely.)

---

**Candidate P-04: Single Owner Per Information Class**

Claim: Each information class has exactly one owner that is the sole authoritative producer. All other parties are read-only consumers.

Evidence:
- AF SECTION-04: Explicitly names 13 information classes, each with exactly one owning domain, and states: "One owner per information class. Owners are the sole producers; all other domains are read-only consumers via the dependency edges in SECTION-05."
- AF 5.5 hidden coupling controls: "DOM-09 is the single source of portfolio state; no consumer may maintain a private portfolio state derivative that other domains then consume." This rule directly prevents dual-ownership from producing hidden state divergence.
- SADR CHANGE-01 + CHANGE-02: The architectural audit that split compliance evaluation from portfolio state provision is a concrete application of this principle — when CAP-29 was found to have two information-class functions (provide state + evaluate compliance), CHANGE-01 removed one and CHANGE-02 created a dedicated owner (CAP-31) for the compliance evaluation class.
- SDM-13 Rule 10: Attribution "possesses no write authority over any future recommendation behavior" — read-only observational role is the constitutional expression of single-owner authority.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-05: No Hidden Portfolio State**

Claim: Portfolio state must be maintained by a single authoritative source. No domain may maintain a private derivative of portfolio state that other domains consume.

Evidence:
- AF 5.5: "DOM-09 is the single source of portfolio state; no consumer may maintain a private portfolio state derivative that other domains then consume (this would recreate the compliance-evaluation ambiguity that CHANGE-01/CHANGE-02 resolved)."
- SADR CAP-29 Boundary: "Does not evaluate compliance (CAP-31). Does not compute allocations. Does not enforce limits. Does not execute trades. Governance compliance assessment is not a function of this capability."
- SADR CHANGE-01 + CHANGE-02: The architectural history of the split proves the principle is not merely organizational — private state produced an architecturally invalid ambiguity about who held evaluation authority.
- CONSTRAINT-01: "Portfolio state reflects only human-approved and executed trade actions. The system has no write authority over portfolio state." The system's only valid representation must ultimately trace to external human action; private derivatives cannot maintain that fidelity.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.** (P-05 is a specific and operationally critical instance of P-04, warranting its own principle given its architectural significance.)

---

**Candidate P-06: No Governance State Coupling**

Claim: The four halt states are constitutionally independent. No derived architecture may merge them into a shared state machine or allow restoration of one to influence the others.

Evidence:
- SDM-CONST-14: "These states are non-overlapping in trigger but may be simultaneously active." Four distinct states with four distinct triggers, effects, and exits are enumerated.
- SDM-CONST-14 also states: "Each state operates independently. Restoration of one state does not restore another."
- SADR Section 5 "Halt State Independence": "The four halt states (CAP-24, CAP-25, CAP-26, CAP-27) are constitutionally independent. Each has its own entry condition, active state, and exit condition. They may be simultaneously active. Restoration of any one does not restore any other. When multiple states are simultaneously active, a recommendation is permissible only if it is not blocked by any currently active state."
- AF DOM-06 Independence Constraint (binding): "No derived architecture may merge the four states into a single state machine that erases this independence."
- SADR Section 7: Each halt state has its own row — distinct entry authority, distinct exit authority.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-07: Audit Is Write-Only**

Claim: The audit log is the terminal sink of the information flow. It receives from all domains and produces no outputs that feed back into any capability.

Evidence:
- CAP-30 Boundary: "Recording only. Does not process events. Does not feed back into any capability."
- AF DOM-10 Boundary: "forbids co-location with any producer" precisely because any co-location could create a feedback path.
- AF SECTION-04 "Audit Records": Constitutionally entitled consumers: "Human review only."
- AF 5.1: "ALL DOMAINS ──▶ DOM-10 (Audit) [terminal sink; no outbound edges]"
- AF 5.4 prohibited dependency: "DOM-10 → any capability."
- AF 3.3 anti-leakage: "No audit feedback leakage: DOM-10 has no output edge to any capability (CAP-30 Boundary). ✅"

Note: "Write-Only" in this principle names the relationship from the system's perspective — the audit log only receives writes from the system, never writes to the system. Human review of audit records is explicitly authorized and is the only legitimate use of the audit record.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.** (Term "write-only" is acceptable constitutional shorthand for "receives from all; outputs to none within the system.")

---

**Candidate P-08: Attribution Is Read-Only**

Claim: Attribution holds observation authority only. Its outputs are available for human review. No output may modify any system capability's behavior without explicit human approval.

Evidence:
- SDM-13 Rule 8: "Attribution may not autonomously modify Signal Discovery logic, Validation logic, Confidence logic, Expected Value logic, Ranking logic, Capital Allocation logic, or Governance logic."
- SDM-13 Rule 10: "Attribution possesses no write authority over any future recommendation behavior."
- SDM-13 Rule 9: "Changes to SDM recommendation behavior based on attribution findings require explicit human approval."
- SADR CONSTRAINT-07: "Attribution possesses read-only observational authority. It may not write to any recommendation, signal, validation, confidence, ranking, allocation, or governance logic."
- AF DOM-08: "with no write authority over anything."
- AF SECTION-04 "Attribution Records": Constitutionally entitled consumers: "Human review only; DOM-10."
- AF 3.3 anti-leakage: "No attribution write leakage: DOM-08 has no write edge to any logic in DOM-01 through DOM-06. ✅"

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-09: Sentiment Is Advisory Only**

Claim: Sentiment and news signals may never enter the computational confidence, EV, ranking, or allocation pipeline. They are presented to the human as a named advisory section distinct from computationally derived outputs.

Evidence:
- SDM-CONST-10: "News signals are supplementary." The VAL-05 resolution formally defines "supplementary" as contextual and advisory — not "secondary computational input."
- SDM-04 Rule 12: "AI model evaluations shall be isolated exclusively to the semantic and cognitive domain."
- GOV-VAL05 Rule 1: "AI-generated sentiment scores do not enter the confidence scoring computation as inputs. Confidence scoring derives exclusively from technical evidence and statistical validation."
- GOV-VAL05 Rule 4: "Sentiment and news analysis signals shall appear in the human-facing advisory report as a named advisory section, distinct from the computationally derived confidence scores, rankings, and allocation suggestions."
- GOV-VAL05 Rule 5: "VAL-07 (NLP scores to confidence weights), VAL-11 (sentiment to Kelly fractions), and VAL-15 (sentiment to position sizing without violating determinism) are hereby closed. The pathway they described does not exist."
- SADR_AMENDMENT_VAL-05 CAP-12: "Confidence computation is derived exclusively from technical evidence and statistical validation. News and sentiment signals do not enter the confidence formula."
- AF DOM-03 GOV-VAL05 Boundary: "The supplementary signal set routes only to the human-facing advisory report assembled for CAP-18. It does not enter CAP-12 or any downstream computation."
- AF 5.4 prohibited dependency: "DOM-03 supplementary signals → DOM-05 computation (GOV-VAL05 Rule 1)."
- AF 3.3 anti-leakage: "No sentiment computational leakage: DOM-03's supplementary signals reach computation nowhere; they reach the human only. ✅"

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-10: Dependencies Flow One Direction**

Claim: The internal information graph must be acyclic. No information class may flow back toward its own producer within a single recommendation cycle.

Evidence:
- AF 5.1: Complete domain-level dependency direction enumerated. All edges are unidirectional.
- AF 5.3: The only apparent cycle (DOM-09 → DOM-05 → DOM-07 → DOM-09) is explicitly analyzed and resolved: "The cycle is broken at the system boundary by the human actor. Within any single recommendation cycle the internal graph is acyclic."
- AF 5.3 secondary check: DOM-06 → DOM-11 → DOM-06 is confirmed to be an activation initiation chain, not a data dependency cycle.
- AF 5.4 six prohibited dependencies — all six are unidirectional restrictions: attribution → recommendations; audit → capabilities; supplementary signals → computation; system → broker; unverified data → signal logic; paths around CAP-18.
- SADR Section 5 blocking gates: three one-way blocking gates establish the linear progression from data to verification to validation to confidence to approval.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-11: Domain Boundaries Preserve Capability Boundaries**

Claim: Architectural domains must preserve the capability boundaries as defined in SADR. No capability may be split across domains. No SADR-distinct capability may be silently merged with another.

Evidence:
- AF 2.0: "Eleven domains result. All 31 capabilities are assigned exactly once. No capability is split, merged, renamed, or invented. SADR capability boundaries are preserved verbatim inside each domain."
- AF 2.0 three evidence tests: constitutional rooting, information cohesion, authority cohesion — all three must be satisfied for domain grouping.
- AF DOM-05 grouping evidence: The considered alternative of grouping CAP-20 with CAP-19 was explicitly rejected with authority reasoning — their different output classes and SDM sources require separation.
- AF DOM-07 grouping evidence: "Authority cohesion (test 3) forbids merging [CAP-18] into any autonomous domain." — A concrete example of the principle.
- AF DOM-06 independence constraint: "No derived architecture may merge the four states into a single state machine." — The halt-state independence constraint is enforced through domain boundary design.
- SDM-CONST-12: Modular LEGO-style approach; "Components shall be replaceable, configurable, versioned, and independently evolvable." Independent evolution is only possible when boundaries are preserved.

Constitutional test: technology-neutral ✅ | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

**Candidate P-12: Architecture Must Remain Technology Neutral**

Claim: No architectural decision may be contingent on, or couple the system to, a specific technology, infrastructure platform, or implementation choice.

Evidence:
- SDM-CONST-12: "System design shall follow a modular LEGO-style approach. Components shall be replaceable, configurable, versioned, and independently evolvable. Future SaaS expansion must remain possible without requiring complete redesign."
- SDM Part V invariants explicitly prohibit the following from appearing in any downstream artifact: "Architecture Decisions, Implementation Decisions, Database Decisions, Cloud Decisions, MCP Decisions, Broker Decisions, Infrastructure Decisions, Technology Selections."
- SADR Section 11: Open validation items (VAL-03, VAL-08, VAL-09, VAL-12, VAL-14, VAL-16, VAL-17) are classified CLASS_B with the ruling "generic interface sufficient for architecture." This means architecture is not permitted to wait for, or hard-code, specific implementations of these unresolved calibration items.
- AF Method statement: "Technology-neutral. No services, databases, APIs, schemas, workflows, agents, queues, or infrastructure are defined or implied."
- AF derivation note: "Multiple valid architectures may be derived from it; none is selected by it." — This confirms that constitutional truth does not select a technology.
- SDM-CONST-04: Scale target is "Personal Tool → Optional SaaS." Technology-coupling at the personal tool stage would prohibit the Optional SaaS expansion, violating SDM-CONST-12.

Constitutional test: technology-neutral ✅ (this principle is self-proving) | architecture-style-neutral ✅ | traceable to authority ✅ | preserves intent ✅

**VALIDATED.**

---

### Phase 4 — DEVELOP

All 12 candidate principles survived the INVESTIGATE phase with full evidence. Constitutional truths are now converted into architecture principles.

---

### Phase 5 — DELIVER

---

## ADR-000 — ARCHITECTURE PRINCIPLES

---

### P-01 | Constitution Before Optimization

**Principle Statement**

Every governance constraint, halt condition, and constitutional rule takes unconditional precedence over performance, latency, efficiency, throughput, or any optimization objective. No optimization argument may serve as grounds for weakening, deferring, or routing around a governance constraint.

**Constitutional Evidence**

- SDM-CONST-06: Human approval mandatory "without exception." No performance exception exists.
- SDM-CONST-14: Halt states govern recommendation authority without efficiency escape clauses.
- GOV-01 Rule 1: Zero autonomous execution "under all circumstances."
- SDM Part V: Constitutional invariants "may not be overridden by any downstream architectural, implementation, or infrastructure decision."
- AF 3.3, check 6: Every trade-action pathway must pass through DOM-07; no exception.

**Derived Rationale**

The constitutional corpus was deliberately structured to remove efficiency as a competing criterion against governance. The phrase "without exception" appears in multiple locations (SDM-CONST-06, GOV-01 Rule 1) specifically to foreclose optimization reasoning as a justification. The system's identity as a research analyst — not an execution engine — means latency in the governance path is constitutionally acceptable; latency in the recommendation pipeline is merely operational.

**Architectural Implication**

Future ADRs proposing to streamline approval flows, pre-approve categories of trades, apply probabilistic governance bypass, or "fast-path" low-risk recommendations must be rejected on this principle before any technical evaluation begins. Governance correctness is the primary fitness criterion. When a design choice involves a trade-off between governance fidelity and operational efficiency, governance fidelity wins unconditionally.

**Prohibited Violations**

- An approval mechanism that auto-accepts recommendations below a confidence threshold without human interaction
- A halt-state design that silently downgrades a Governance Halt to a warning when the system detects high-confidence signals
- A circuit breaker that bypasses the approval gate under time-pressure conditions
- Any architectural argument that governance overhead should be reduced because the capital at risk is small

**Confidence: High**

---

### P-02 | Authority Before Automation

**Principle Statement**

Human decision authority must never be compressed, approximated, pre-empted, or structurally pressured by automated logic. The architecture must present information to the human for their decision; it must not present decisions to the human for their ratification.

**Constitutional Evidence**

- SDM-CONST-06: Autonomous execution prohibited without exception.
- SDM-10 Rule 1: System halts and awaits explicit approval — not implicit, not timeout-based.
- CAP-18 Boundary: "No timeout-based auto-approval. No bypass pathways."
- CONSTRAINT-09 + SDM-08 Rule 8: Simultaneous Open Menu mandatory; sequential forced selection prohibited. (Sequential framing creates automation pressure on human choice sequence.)
- GOV-VAL05 Criterion 1: Option B selected because "the human is not receiving a pre-blended number — they are receiving the raw inputs and doing the blending themselves."

**Derived Rationale**

The distinction between "information presented for decision" and "decision presented for ratification" is architecturally meaningful. A system that presents a single best-option pre-selected from sequential analysis has structurally narrowed the human's decision space. The Open Menu requirement (CONSTRAINT-09) and the GOV-VAL05 ruling both exist to prevent this narrowing. The architecture must preserve the human's full decision space at the approval gate.

**Architectural Implication**

Future ADRs must ensure: (1) the advisory package presented to the human contains the raw inputs and computationally derived scores as separate, distinguishable artifacts; (2) no pre-selection, ordering that implies preference, or sequential filtering reduces the apparent option space before human review; (3) the approval gate has no time-based completion mechanism. Any design that makes the human's approval more likely by presenting information in a persuasive sequence rather than as a simultaneous inventory violates this principle.

**Prohibited Violations**

- A presentation layer that displays only the top-ranked opportunity and requires a rejection action to view others
- A confidence display that blends sentiment into the score, masking the raw technical confidence from the human
- An approval gate with a configurable auto-approve timeout
- A flow that presents "recommended action" as the primary CTA and requires additional navigation to see the full ranked set

**Confidence: High**

---

### P-03 | Human Approval Cannot Be Bypassed

**Principle Statement**

No pathway to a trade action may exist in the system architecture that does not pass through the human approval gate. This includes emergency paths, high-confidence paths, scheduled paths, and any form of conditional automation.

**Constitutional Evidence**

- SDM-CONST-06: "Autonomous execution is prohibited without exception."
- SDM-CONST-13: No output of this system constitutes an executable trade order.
- SADR CONSTRAINT-01: No capability may initiate, execute, place, modify, or cancel a trade order.
- SADR Section 5 / AF 5.2: "CAP-18 blocks all trade action — no exceptions, no bypass." Named constitutional blocking gate.
- AF 5.4 prohibited dependency: "Any path around CAP-18 to a trade action."
- GOV-01 Rule 1: No market orders "under any circumstance" — "any circumstance" includes emergency, drawdown breach, and governance halt.
- GOV-02 Rules 4–5: No trade execution during Governance Lockout — confirming that even the most severe enforcement state does not grant execution authority.

**Derived Rationale**

This principle is structurally unconditional. The qualification "without exception" and "under any circumstance" in the authority sources leave no room for architectural interpretation. The principle is distinct from P-02 (which concerns quality of human decision) — P-03 concerns the structural impossibility of bypassing the gate entirely. Even when the system is in a maximally constrained governance state (all four halt states simultaneously active), the only permitted output is the escalation report to the human; the system still cannot act on the market.

**Architectural Implication**

Architectural reviews must verify that the dependency graph contains no edge — direct or transitive — from any recommendation-generating capability to any market-interaction surface without passing through CAP-18's authority class. If a future ADR describes a system component that could, under any conditional logic, emit a market order without human action, that ADR must be rejected regardless of the conditions attached.

**Prohibited Violations**

- A "safety liquidation" feature that executes sells autonomously when drawdown approaches 5%
- A scheduled order placement that operates on pre-approved recommendation templates
- A stop-loss placement that is executed by the system after the human approves a trade entry
- Any API integration with a broker that the system can call directly, regardless of what controls wrap it

**Confidence: High**

---

### P-04 | Single Owner Per Information Class

**Principle Statement**

Every information class has exactly one owning domain that is the sole authoritative producer. All other domains are read-only consumers of that information through defined dependency edges. Dual-ownership is prohibited.

**Constitutional Evidence**

- AF SECTION-04: "One owner per information class. Owners are the sole producers; all other domains are read-only consumers via the dependency edges in SECTION-05." Thirteen information classes enumerated with single owners.
- AF 5.5: "DOM-09 is the single source of portfolio state; no consumer may maintain a private portfolio state derivative that other domains then consume."
- SADR CHANGE-01 + CHANGE-02: Formal architectural correction when a single capability held two information-class functions (state provision + compliance evaluation) — resolved by separating into distinct owners.
- SDM-13 Rule 10: Attribution holds no write authority — enforces read-only consumer status for DOM-08.

**Derived Rationale**

Dual-ownership creates ambiguity about which instance of an information class is authoritative when they diverge — which they inevitably will under concurrency, failure, or evolution. The SADR CHANGE-01/CHANGE-02 history demonstrates this is not theoretical: a single capability with two functions produced a real constitutional ambiguity that required an amendment to resolve. The principle prevents that class of problem structurally.

**Architectural Implication**

When a new ADR introduces a component that reads and caches an information class, it must not treat that cache as a source for other consumers. When an ADR introduces a new information class, it must name a single owning domain before the ADR may proceed. If a proposed design has two components that both compute or maintain the same information, the ADR must resolve which is authoritative before implementation.

**Prohibited Violations**

- A recommendation engine that maintains its own internal portfolio position count derived from its recommendation history, used as input to ranking logic alongside the authoritative count from DOM-09
- Two components both tracking drawdown level, with consumers choosing between them by availability
- A risk enforcement component that re-derives confidence scores from raw signals rather than consuming them from DOM-05

**Confidence: High**

---

### P-05 | No Hidden Portfolio State

**Principle Statement**

Portfolio state must exist in exactly one authoritative representation within the system. No capability or component may maintain a private derivative of portfolio state that is consumed by other parts of the system.

**Constitutional Evidence**

- AF 5.5: "DOM-09 is the single source of portfolio state; no consumer may maintain a private portfolio state derivative that other domains then consume (this would recreate the compliance-evaluation ambiguity that CHANGE-01/CHANGE-02 resolved)."
- SADR CAP-29 Boundary: State maintenance and provision only; governance compliance assessment is explicitly not a function of CAP-29.
- SADR CHANGE-01 + CHANGE-02: Direct constitutional history showing that when portfolio state and compliance evaluation were co-located, a structural ambiguity arose about who held evaluation authority.
- CONSTRAINT-01: Portfolio state reflects only human-approved and executed trade actions. Private derivatives cannot maintain that authoritative sourcing.

**Derived Rationale**

Hidden portfolio state is architecturally dangerous because: (1) it silently diverges from the authoritative state, (2) the divergence is invisible to governance checks (CAP-31 evaluates against DOM-09 state; it cannot evaluate against undeclared private state), (3) decisions made against divergent state are constitutionally unauthorized even if numerically close to the correct answer. The principle applies at any scope — a capability-level cache, a domain-level summary, or a reporting layer's local copy all violate it if other components consume them as portfolio state.

**Architectural Implication**

Every component that needs portfolio data must source it from DOM-09 (CAP-29) through the defined dependency edges. Any ADR that introduces portfolio-adjacent data structures must specify clearly that these are not portfolio state — they are derived metrics for a specific purpose, owned by their producing domain, not available as a portfolio state source. Governance compliance monitoring must be architecturally positioned to consume only from the authoritative portfolio state source.

**Prohibited Violations**

- A risk enforcement capability that maintains its own running position count updated on each recommendation cycle, rather than reading from DOM-09 at evaluation time
- A reporting component that caches portfolio state for display and exposes that cache to allocation logic for efficiency
- Any component that tracks hypothetical or "pending" portfolio state as though it were actual portfolio state before human trade confirmation arrives

**Confidence: High**

---

### P-06 | No Governance State Coupling

**Principle Statement**

The four constitutionally distinct halt states must be implemented as architecturally independent state machines. No shared state variable, shared trigger evaluator, or shared exit mechanism may span two or more halt states. The simultaneous activation of multiple halt states must be an emergent property of independent state machines, not an explicitly handled combined state.

**Constitutional Evidence**

- SDM-CONST-14: Four distinct states enumerated with distinct triggers, effects, and exits. "These states are non-overlapping in trigger but may be simultaneously active." "Each state operates independently. Restoration of one state does not restore another."
- SADR Section 5 "Halt State Independence": "constitutionally independent... restoration of any one does not restore any other... a recommendation is permissible only if it is not blocked by any currently active state."
- AF DOM-06 Independence Constraint (binding): "No derived architecture may merge the four states into a single state machine that erases this independence."
- SADR Section 7: Each halt state has its own row in the governance table with distinct entry authority and distinct exit authority.

**Derived Rationale**

The constitutional design of four independent states was deliberate. The SDM needed halt-state behaviors that could be simultaneously active without interfering with each other — the Governance Halt from a drawdown breach must remain active regardless of whether the Governance Lockout from a stop-loss violation is also present. A shared state machine would produce emergent behaviors not sanctioned by the constitution: e.g., clearing all halts when one's exit condition is met, or preventing entry into a second halt when one is already active.

**Architectural Implication**

Each halt state (Governance Halt, Governance Lockout, Conditional Recommendation Suspension, Hard Deterministic Halt) must have its own entry logic, active-state representation, and exit logic. Their combined effect on recommendation issuance is computed by evaluating all four states independently and blocking issuance if any is active. ADRs proposing a unified halt-state controller must demonstrate that the four independence constraints are preserved inside it — the burden is on the proposing ADR.

**Prohibited Violations**

- A single `halt_state` field with an enumerated type that allows only one active state at a time
- An exit procedure that checks "all halt conditions cleared" before resuming rather than checking each state independently
- A design where entering State 2 (Governance Lockout) implicitly also activates State 1 (Governance Halt) behavior
- A shared condition evaluator that fires all halt entries from a single monitoring loop, creating undeclared coupling between their detection timing

**Confidence: High**

---

### P-07 | Audit Is Write-Only

**Principle Statement**

The audit log is the terminal information sink of the system. It receives from all capabilities and produces no output that is consumed by any capability. No feedback edge from the audit domain to any other domain is permitted.

**Constitutional Evidence**

- CAP-30 Boundary: "Recording only. Does not process events. Does not feed back into any capability."
- AF 5.1: "ALL DOMAINS ──▶ DOM-10 (Audit) [terminal sink; no outbound edges]"
- AF 5.4 prohibited dependency: "DOM-10 → any capability."
- AF SECTION-04 "Audit Records": Constitutionally entitled consumers: "Human review only."
- AF 3.3 anti-leakage: "No audit feedback leakage: DOM-10 has no output edge to any capability. ✅"
- AF DOM-10 grouping evidence: The boundary "forbids co-location with any producer."

**Derived Rationale**

"Write-only" from the system's perspective means the system writes to the audit log and nothing in the system reads from it. Human review of the audit record is explicitly constitutionally authorized and is not a violation. The prohibition is against system capabilities reading from the audit log to influence their behavior — that would introduce a feedback loop that could progressively alter system behavior based on accumulated audit history, without the human approval that SDM-13 Rule 9 requires for any behavior change.

**Architectural Implication**

Audit records must not be accessible to any recommendation, validation, confidence, EV, ranking, allocation, or governance capability as a runtime input. Reporting and analytics functions that read the audit record for human-facing dashboards must be architecturally separated from any capability that can influence recommendation behavior. An ADR proposing to use audit history to adjust signal weights, refine model parameters, or tune halt thresholds must route those changes through explicit human approval rather than as an automated feedback path from audit.

**Prohibited Violations**

- A confidence scoring component that reads historical confidence scores from the audit log to calibrate its formula
- A governance component that reads past halt-entry frequency from the audit log to adjust sensitivity thresholds
- An attribution component that reads from the audit log to populate its tracking records (attribution must observe the live system, not read from audit)
- Any automated pipeline where audit data flows into any capability that produces recommendations

**Confidence: High**

---

### P-08 | Attribution Is Read-Only

**Principle Statement**

Attribution holds observation authority only. It may generate insights, warnings, and reports for human review. It may not modify, write to, or automatically influence any capability involved in signal discovery, validation, confidence scoring, expected value assessment, ranking, allocation, or governance. Any behavior change motivated by attribution findings requires explicit human approval.

**Constitutional Evidence**

- SDM-13 Rule 8: "Attribution may not autonomously modify Signal Discovery logic, Validation logic, Confidence logic, Expected Value logic, Ranking logic, Capital Allocation logic, or Governance logic."
- SDM-13 Rule 9: "Changes to SDM recommendation behavior based on attribution findings require explicit human approval."
- SDM-13 Rule 10: "Attribution possesses no write authority over any future recommendation behavior."
- SADR CONSTRAINT-07: "Attribution possesses read-only observational authority. It may not write to any recommendation, signal, validation, confidence, ranking, allocation, or governance logic."
- AF DOM-08: "with no write authority over anything."
- AF 3.3 anti-leakage: "No attribution write leakage. ✅"
- AF SECTION-04 "Attribution Records": Constitutionally entitled consumers: "Human review only; DOM-10."

**Derived Rationale**

Attribution exists to measure decision quality, not to improve it autonomously. The constitutional design anticipates that attribution findings will generate actionable insights — but those insights must travel through the human to become behavioral changes. This preserves the human as the decision-improvement authority. An attribution system that autonomously adjusts signal weights based on observed outcomes would be an unauthorized feedback loop from historical performance data to future recommendation behavior, bypassing the human approval required by SDM-13 Rule 9.

**Architectural Implication**

DOM-08 must have no write edges to DOM-01, DOM-02, DOM-03, DOM-04, DOM-05, or DOM-06 in the dependency graph. Attribution outputs (reports, insights, warnings) must flow only to the human and to the audit log. When a human decides to act on an attribution finding — adjusting a signal weight, changing a confidence formula, modifying a halt threshold — that change must be implemented through a constitutionally authorized change process, not by the attribution system directly. ADRs proposing "adaptive" or "self-improving" components that update based on their own performance history must pass through explicit human approval gates, not automated feedback loops.

**Prohibited Violations**

- An attribution component that writes adjusted signal quality scores back into the signal validation registry
- A feedback mechanism where poor attribution outcomes automatically lower the confidence weight assigned to a strategy type
- A "learning" component that modifies its own parameters based on the delta between its predictions and observed outcomes without human approval
- Any architecture that allows DOM-08 output to serve as an input to DOM-05 computation in the next cycle

**Confidence: High**

---

### P-09 | Sentiment Is Advisory Only

**Principle Statement**

Sentiment and news signals may never enter any computational formula for confidence scoring, expected value assessment, opportunity ranking, or capital allocation. They must appear in the human-facing advisory report as a named, distinct advisory section. The conflict flag produced by technical-news conflict evaluation is annotation only — it marks a recommendation for human attention but does not modify the score.

**Constitutional Evidence**

- SDM-CONST-10: "News signals are supplementary." VAL-05 resolution defines supplementary as advisory, not computationally integrated.
- SDM-04 Rule 12: "AI model evaluations shall be isolated exclusively to the semantic and cognitive domain."
- GOV-VAL05 Rule 1: Sentiment does not enter the confidence computation; confidence derives exclusively from technical evidence and statistical validation.
- GOV-VAL05 Rule 4: Sentiment appears as a named advisory section, distinct from computationally derived outputs.
- GOV-VAL05 Rule 5: VAL-07, VAL-11, VAL-15 closed; the conversion pathways they described do not exist.
- SADR_AMENDMENT_VAL-05 CAP-12: Confidence computation is exclusively technical; news and sentiment signals do not enter the confidence formula.
- AF 5.4 prohibited dependency: "DOM-03 supplementary signals → DOM-05 computation (GOV-VAL05 Rule 1)."
- AF 3.3 anti-leakage: "No sentiment computational leakage. ✅"
- AF DOM-03 GOV-VAL05 Boundary (binding): "The supplementary signal set routes only to the human-facing advisory report... It does not enter CAP-12 or any downstream computation."

**Derived Rationale**

This principle is the direct architectural expression of the VAL-05 owner decision. The decision was made on eight independent criteria, all in favor of the advisory-only pathway. The GOV-VAL05 ruling is a Level 2 authority — it amends the SDM and SADR simultaneously. No future ADR may reopen the computational pathway for sentiment without a new owner decision at the same authority level. The conflict flag annotation is explicitly preserved as advisory — it marks the human's attention without changing the score they are reviewing.

**Architectural Implication**

The data routing for supplementary signals must be architecturally enforced, not merely intended. The dependency graph must have no edge from the supplementary signal set to any confidence, EV, ranking, or allocation component. The only permitted edges from DOM-03's supplementary signal output are: to DOM-03's own conflict evaluation (CAP-09), and to the human-facing advisory report assembled for DOM-07. Conflict flags from CAP-09 may flow to CAP-12 for annotation purposes only — the annotation schema must not allow the flag to serve as a numeric modifier to the score.

**Prohibited Violations**

- A confidence formula that adds a bounded sentiment modifier (positive or negative delta) to the technically-derived score
- A ranking component that re-orders opportunities based on sentiment trend alongside technical probability
- An allocation component that scales position size up for strong positive sentiment signals
- A conflict flag implementation that reduces confidence by a fixed percentage when technical-news conflict is detected
- Any ADR that proposes "bounded" or "limited" sentiment integration as a compromise position

**Confidence: High**

---

### P-10 | Dependencies Flow One Direction

**Principle Statement**

The internal information graph must be a directed acyclic graph (DAG) within any single recommendation cycle. No information class may flow back toward its own producer through an internal system path. The only legitimate "cycle" in the system is closed externally by the human actor.

**Constitutional Evidence**

- AF 5.1: Complete unidirectional domain-level dependency map enumerated.
- AF 5.3: "Within any single recommendation cycle the internal graph is acyclic." The only apparent cycle is explicitly confirmed to be broken at the system boundary.
- AF 5.3 secondary: DOM-06 → DOM-11 → DOM-06 is an activation initiation chain, not a data dependency cycle.
- AF 5.4 six prohibited dependencies: all six are unidirectional restrictions.
- SADR Section 5 three blocking gates: establish the linear progression from data to verification to validation to confidence to approval.
- SADR CONSTRAINT-07 (attribution read-only) and the CAP-30 boundary (audit has no outbound edges): both are cycle-prevention rules.

**Derived Rationale**

Cycles in an information graph produce undefined or system-dependent behavior when information feeds back to modify its own inputs: the system's behavior becomes a function of its own past outputs, which can compound errors, amplify biases, or create governance blind spots. The constitutional design is explicitly acyclic — the SDM's recursive-learning pathway (via attribution findings) is intentionally routed through the human to prevent automated cycles. The only path that looks like a cycle (portfolio state → recommendations → human approval → portfolio state) exits and re-enters through the human, preserving the acyclic internal structure.

**Architectural Implication**

When reviewing an ADR, verify that no data dependency edge, event subscription, or state notification creates a path by which domain A's output eventually feeds back to domain A as a computation input within the same cycle. Legitimate multi-cycle behavior (where the system's outputs in cycle N influence cycle N+1) is constitutionally permitted if and only if the inter-cycle path passes through the human or through a constitutionally authorized change process. Activation events (DOM-11) are initiation signals, not data; they do not constitute cycle-creating data dependencies.

**Prohibited Violations**

- A validation component that updates its own acceptance thresholds based on the confidence scores produced downstream of it
- A market context classifier that learns from the outcomes of recommendations it contributed to, without human approval
- A recommendation component that modifies its signal weights based on the ranking output it produced in the prior cycle
- Any "online learning" or "adaptive" mechanism that is internal to the recommendation pipeline

**Confidence: High**

---

### P-11 | Domain Boundaries Preserve Capability Boundaries

**Principle Statement**

Architectural domains must map to the 11 constitutional domains derived in ARCHITECTURE_FOUNDATION_V1. Within those domains, SADR capability boundaries must be preserved: no capability may be split across domains, silently merged with another, renamed to combine two, or re-scoped to absorb a function belonging to a different capability.

**Constitutional Evidence**

- AF 2.0: "All 31 capabilities are assigned exactly once. No capability is split, merged, renamed, or invented. SADR capability boundaries are preserved verbatim inside each domain."
- AF 2.0 derivation method: Three evidence tests (constitutional rooting, information cohesion, authority cohesion) determine valid groupings.
- AF DOM-05 grouping: Explicit rejection of a plausible alternative grouping (CAP-20 with CAP-19) with authority-traced reasoning.
- AF DOM-07: Authority cohesion forbids merging CAP-18 into any autonomous domain.
- AF DOM-06: Independence constraint — four halt states must not be merged into a single state machine.
- SDM-CONST-12: Components must be "replaceable, configurable, versioned, and independently evolvable." Independent evolution requires intact boundaries.
- SADR CHANGE-01 through CHANGE-08: The amendment history shows that capability boundary changes require formal amendment, not informal re-scoping.

**Derived Rationale**

Domain boundaries are not organizational convenience — they encode constitutional distinctions. The authority cohesion test exists because CAP-18's HUMAN_APPROVAL authority class must not be diluted by co-location with autonomous capabilities. The information cohesion test exists because a domain that owns multiple information classes creates dual-ownership violations (P-04). When SADR split compliance evaluation from portfolio state provision, it was applying this principle retroactively — the original capability boundary was constitutionally incorrect because it merged two information classes into one owner.

**Architectural Implication**

Any ADR that proposes to create a service, module, or component that spans two SADR capabilities must demonstrate that it is a technology-implementation container for those capabilities — not a redesign of the capability boundary itself. The capabilities inside remain distinct and must maintain their distinct inputs, outputs, and authority classes. Any proposal to "simplify" by merging a governance capability with a recommendation capability must be rejected; any proposal to "decompose" a capability into sub-capabilities must be evaluated against whether it creates new, non-constitutionally-authorized information boundaries.

**Prohibited Violations**

- A single component that performs both confidence scoring (CAP-12) and opportunity ranking (CAP-15), treating them as a single function
- An implementation that handles both Governance Halt (CAP-25) and Governance Lockout (CAP-26) through the same state variable because "they both block recommendations"
- A portfolio component that also performs governance compliance evaluation, merging DOM-09 and the DOM-06 detection function
- Re-scoping CAP-18 to include an "advisory pre-screening" step that reduces the option set before human presentation — this would absorb DOM-05 function into the HUMAN_APPROVAL domain

**Confidence: High**

---

### P-12 | Architecture Must Remain Technology Neutral

**Principle Statement**

No ADR may make a constitutional claim contingent on a specific technology, infrastructure platform, programming language, database system, messaging protocol, cloud provider, AI model vendor, or deployment pattern. All architectural decisions must remain valid if every technology choice is replaced.

**Constitutional Evidence**

- SDM-CONST-12: "Components shall be replaceable, configurable, versioned, and independently evolvable."
- SDM Part V invariants: Explicitly lists as prohibited content of downstream artifacts: "Architecture Decisions, Implementation Decisions, Database Decisions, Cloud Decisions, MCP Decisions, Broker Decisions, Infrastructure Decisions, Technology Selections."
- SADR Section 11 CLASS_B rulings: "generic interface sufficient for architecture" — open validation items do not justify technology-specific architectural commitment.
- AF Method: "Technology-neutral. No services, databases, APIs, schemas, workflows, agents, queues, or infrastructure are defined or implied."
- AF final statement: "Multiple valid architectures may be derived from it; none is selected by it."
- SDM-CONST-04: Optional SaaS future target — technology-coupling at personal tool stage would prohibit SaaS expansion without complete redesign, violating SDM-CONST-12.

**Derived Rationale**

Technology neutrality is the mechanism that makes SDM-CONST-12's modularity requirement operational. If an architectural decision is only valid for PostgreSQL, it cannot be replaced with another store without revisiting the architecture — the constitution's "replaceable" requirement is violated. Technology choices belong to implementation ADRs which must themselves trace to constitutional principles; constitutional architecture principles must survive technology changes.

**Architectural Implication**

ADRs that describe information flows, authority relationships, domain boundaries, blocking gates, and dependency directions are technology-neutral and comply with this principle. ADRs that describe a specific persistence technology, a specific messaging broker, a specific AI model vendor, or a specific protocol are implementation ADRs — they must trace to a constitutional principle but must not claim constitutional status themselves. A technology-implementation ADR that becomes invalid when the technology is replaced is not a constitutional artifact; it is a calibration choice.

**Prohibited Violations**

- An architectural principle that reads "CAP-30 must use an immutable database with append-only tables (e.g., PostgreSQL with insert-only policy)" — the immutability constraint is constitutional; the implementation is not
- An ADR that says the dependency between DOM-03 and DOM-07 "requires an event bus" — the dependency is constitutional; the implementation mechanism is not
- Selecting a specific AI model vendor as a constitutional requirement rather than a replaceable implementation choice
- A domain boundary defined by the capabilities of a specific technology rather than by constitutional information cohesion

**Confidence: High**

---

## QUALITY GATE SELF-ASSESSMENT

The following prohibited outputs are confirmed absent from this document:

- Architecture design: No. ADR-000 defines rules; it does not define structure.
- Technology selection: No. No specific technology is named as constitutional.
- Service definitions: No. No services are defined or implied.
- Database definitions: No. No persistence technology is named.
- API definitions: No. No protocols or interfaces are specified.
- New capabilities: No. All 31 SADR capabilities are referenced; none are invented.
- New governance rules: No. All governance rules trace to authority.
- New authority classes: No. The three authority classes from SADR Section 6 are the only ones referenced.

**ADR-000 is a constitutional inheritance document.** Its purpose is to define the rules that every future ADR must obey.

---

## PRINCIPLE SUMMARY

| ID | Principle | Confidence |
|----|-----------|------------|
| P-01 | Constitution Before Optimization | High |
| P-02 | Authority Before Automation | High |
| P-03 | Human Approval Cannot Be Bypassed | High |
| P-04 | Single Owner Per Information Class | High |
| P-05 | No Hidden Portfolio State | High |
| P-06 | No Governance State Coupling | High |
| P-07 | Audit Is Write-Only | High |
| P-08 | Attribution Is Read-Only | High |
| P-09 | Sentiment Is Advisory Only | High |
| P-10 | Dependencies Flow One Direction | High |
| P-11 | Domain Boundaries Preserve Capability Boundaries | High |
| P-12 | Architecture Must Remain Technology Neutral | High |

All 12 candidate principles validated. Zero candidates rejected. All evidence traceable to authority. All principles pass the four constitutional tests.

---

*ADR-000 derives its authority from SDM_V2.3 (as amended by GOV-VAL05), VAL05_OWNER_DECISION_RESOLUTION, SADR_V2.1 (as amended by SADR_AMENDMENT_VAL-05), and ARCHITECTURE_FOUNDATION_V1. It introduces no behavior, no capability, no authority, and no technology. All future ADRs must conform to these principles or present authority-traced justification for deviation.*

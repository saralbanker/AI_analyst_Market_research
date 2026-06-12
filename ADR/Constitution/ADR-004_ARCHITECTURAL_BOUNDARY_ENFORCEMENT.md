# ADR-004 — ARCHITECTURAL BOUNDARY ENFORCEMENT

**Document Type:** Architectural Preservation Specification
**Method:** 4D_PLUS_METHOD (Deconstruct · Diagnose · Develop · Deliver)
**Produced By:** Constitutional Architect / Architecture Governance Analyst / Boundary Enforcement Authority

**Authority Hierarchy:**
- Level 1: SDM_V2.3 (FROZEN — FINAL CANONICAL)
- Level 2: VAL05_OWNER_DECISION_RESOLUTION (RESOLVED — Option B)
- Level 3: SADR_V2.1 (CERTIFIED)
- Level 4: ARCHITECTURE_FOUNDATION_V1
- Level 5: ADR-000_ARCHITECTURE_PRINCIPLES
- Level 6: ADR-001_ARCHITECTURAL_STYLE_SELECTION
- Level 7: ADR-002_CAPABILITY_TO_MODULE_REALIZATION
- Level 8: ADR-003_MODULE_INTERNAL_REALIZATION
- Level 9: ADR-003A_ARCHITECTURAL_OBSERVATIONS_RESOLUTION
- Level 10: ADR-003B_CONSTITUTIONAL_CLARIFICATION_AMENDMENT

**Evidence Boundary:** Constitution/ folder only. No conclusion may originate from outside this folder.
**Status:** FINAL
**Scope:** Defines the complete constitutional enforcement model that preserves the already-approved architecture against implementation drift. Does not create architecture, redesign modules, introduce capabilities, select technology, or make implementation decisions. Every rule herein is derived from constitutional evidence; no rule originates from engineering preference, implementation assumption, or optimization argument.

---

## SECTION 01 — BOUNDARY ENFORCEMENT METHODOLOGY

### 1.1 Purpose

Architecture discovery is complete. Architecture realization is complete. Constitutional clarification is complete.

ADR-004 answers a single question: **how are the already-approved architectural boundaries preserved when implementation begins?**

Preservation differs from creation. The boundaries being preserved were created by the authority corpus. ADR-004 does not add to them. ADR-004 converts each constitutional boundary into an explicit enforcement rule — a named prohibition or constraint against which any future implementation artifact may be evaluated.

### 1.2 Enforcement Derivation Method

**Phase 1 — DECONSTRUCT:** Extract each distinct boundary class from the constitutional corpus: ownership boundaries, dependency boundaries, governance boundaries, audit boundaries, authority boundaries, activation boundaries.

**Phase 2 — DIAGNOSE:** Identify the drift risk that each boundary faces during implementation — what a developer or future ADR could do that would violate the boundary without necessarily intending to.

**Phase 3 — DEVELOP:** Convert each boundary into an enforcement rule stated in terms of what is permanently prohibited, what is permanently permitted, and what any future change must demonstrate before it is constitutionally admissible.

**Phase 4 — DELIVER:** Produce the complete enforcement model as ADR-004.

### 1.3 Enforcement Rule Format

Each enforcement rule follows a standard format:

- **RULE ID** — unique identifier within its section
- **Boundary Class** — which category this rule belongs to
- **Constitutional Source** — the specific authority clause(s) from which the rule is derived
- **What Is Permanently Prohibited** — the drift scenario this rule prevents
- **What Is Permanently Permitted** — the legal behavior that must not be mistaken for a violation
- **Enforcement Test** — the question that any future implementation artifact must answer to demonstrate compliance

### 1.4 Relationship to the Selected Architectural Style

ADR-001 selected the Modular Monolith with constitutionally bounded event signaling as the architectural style. This selection is frozen. ADR-004 enforcement rules apply within that style. An enforcement rule that says "no dependency edge may exist from X to Y" means no import, no function call, no event subscription, no shared state reference, and no indirect routing path from X to Y — regardless of the specific modular monolith implementation mechanism used to express module boundaries.

### 1.5 No Technology Assumption

ADR-004 enforcement rules are technology-neutral. The rules state what cannot exist between modules, what information cannot flow where, and what conditions cannot be merged. They do not specify how those prohibitions are implemented (linters, dependency checkers, compiler module systems, architecture tests, CI gates, or any other mechanism). The implementation mechanism is a calibration choice. The prohibition itself is constitutional.

---

## SECTION 02 — MODULE BOUNDARY ENFORCEMENT RULES

### 2.1 Boundary Derivation

The 11 modules are derived 1:1 from the 11 constitutional domains (AF Section 2.0; ADR-002 Section 2.2). These boundaries encode three constitutional distinctions: constitutional rooting (same SDM authority source), information cohesion (single information class ownership), and authority cohesion (same or compatible authority class). Violations of module boundaries violate all three tests simultaneously.

**Constitutional Sources:** AF 2.0; ADR-000 P-11; ADR-001 CHAR-01; ADR-002 Section 2; SDM-CONST-12.

---

**RULE MB-01 | Capability Assignment Is Frozen**

Constitutional Source: AF 2.0; ADR-002 Section 4 Capability Allocation Matrix; ADR-000 P-11.

What Is Permanently Prohibited:
- Splitting a SADR-defined capability across two or more modules
- Merging two SADR-distinct capabilities into a single component that treats them as one function
- Re-scoping a capability to absorb a function constitutionally assigned to a different capability
- Moving a capability from its constitutional module to another module without a constitutional amendment at AF level or above
- Inventing a capability not present in SADR (31 capabilities total; zero may be invented)

What Is Permanently Permitted:
- An implementation component (class, function, unit, file) that contains the full realization of one SADR capability and nothing else
- A component that contains partial internal logic for one capability (sub-functions), so long as it does not combine logic belonging to two distinct SADR capabilities into a single unit
- Future implementation ADRs that decompose a capability's realization into smaller internal components, provided all components remain within the constitutional module

Enforcement Test: Does the proposed implementation unit represent more than one SADR-defined capability, or does it represent a function that the SADR assigns to a capability other than the one it claims to implement? If yes: PROHIBITED.

---

**RULE MB-02 | Module Count Is Frozen**

Constitutional Source: AF 2.0; ADR-002 Section 2.2; ADR-000 P-11.

What Is Permanently Prohibited:
- Creating a 12th or higher-numbered module that is not derived from a constitutional domain
- Merging two constitutional domains into a single module (e.g., a combined MOD-05+MOD-06 that handles both recommendation synthesis and governance enforcement)
- Splitting a single constitutional domain into multiple modules (e.g., splitting MOD-06 into a "detection module" and a "halt-state module")

What Is Permanently Permitted:
- Creating implementation sub-components, packages, or code units within a single module's boundary, provided these are internal implementation subdivisions and are not named, referenced, or treated as independent modules by other modules
- Future extraction of modules into independently deployable services (authorized by SDM-CONST-12), provided each extracted service corresponds 1:1 to exactly one constitutional module — no merged-service extraction, no split-service extraction

Enforcement Test: Does the proposed structure introduce a module boundary that does not correspond to a constitutional domain? Or does it eliminate a module boundary that separates two constitutional domains? If yes: PROHIBITED.

---

**RULE MB-03 | Authority Class Boundaries Are Inviolable Within Modules**

Constitutional Source: SADR Section 6; AF Section 3.2; ADR-002 Section 4; ADR-000 P-11.

The three authority classes — AUTONOMOUS_RESEARCH, SHARED_AUTHORITY, HUMAN_APPROVAL — must remain architecturally distinguishable. The HUMAN_APPROVAL class applies exclusively to CAP-18 in MOD-07. The SHARED_AUTHORITY class applies exclusively to CAP-09 in MOD-03. All other capabilities carry AUTONOMOUS_RESEARCH.

What Is Permanently Prohibited:
- Co-locating CAP-18 (HUMAN_APPROVAL) with any AUTONOMOUS_RESEARCH capability in a design that dilutes the distinction between the human's approval authority and the system's research authority
- Treating CAP-09 (SHARED_AUTHORITY) as fully autonomous — the human's review and decision authority at CAP-18 cannot be removed from CAP-09's authority class
- Introducing a fourth authority class not present in SADR Section 6

What Is Permanently Permitted:
- An implementation component that contains MOD-07's presentation logic alongside CAP-18's gate logic, provided CAP-18's HUMAN_APPROVAL boundary is explicitly maintained and no autonomous function bypasses it

Enforcement Test: Does the proposed design co-locate a HUMAN_APPROVAL function with an AUTONOMOUS_RESEARCH function in a way that creates an architectural path around the HUMAN_APPROVAL gate? If yes: PROHIBITED.

---

**RULE MB-04 | Domain Boundaries Must Remain Independently Evolvable**

Constitutional Source: SDM-CONST-12; ADR-000 P-11; ADR-001 Section 7, R1.

What Is Permanently Prohibited:
- Shared mutable state between two modules that would cause changes in one module to require changes in the other
- Importing the internal implementation details of one module from within another (shared internal types, private data structures, or implementation-specific interfaces)

What Is Permanently Permitted:
- Well-defined inter-module contracts that expose only the information class outputs relevant to the constitutional dependency edge
- One module depending on the published output contract of another module, provided that contract corresponds to an authorized dependency edge in ADR-002 Section 6.1

Enforcement Test: Can MOD-X be replaced entirely (its internal implementation changed) without requiring any change to MOD-Y, provided MOD-X continues to produce the same constitutional output? If not: a boundary violation exists.

---

## SECTION 03 — OWNERSHIP PROTECTION RULES

### 3.1 Ownership Model

The 13 information classes each have exactly one owning module (AF Section 4; ADR-002 Section 5). Owners are the sole authoritative producers. All other modules are read-only consumers via constitutional dependency edges. Dual-ownership is structurally prohibited.

**Constitutional Sources:** AF SECTION-04; AF 5.5; ADR-000 P-04; ADR-000 P-05; ADR-001 OWN-01 through OWN-07.

---

**RULE OWN-01 | Portfolio State Ownership Is Exclusively MOD-09**

Constitutional Source: AF 5.5; ADR-000 P-05; AF SECTION-04 "Portfolio State" — Owner: DOM-09; SADR CHANGE-01/CHANGE-02; ADR-002 Section 3 MOD-09.

What Is Permanently Prohibited:
- Any module other than MOD-09 maintaining a local copy of portfolio state that is then consumed by another module as authoritative portfolio state
- A recommendation module (MOD-05) maintaining its own running position count derived from its recommendation history and feeding that count to allocation or ranking logic
- A governance module (MOD-06) maintaining a private drawdown estimate used for halt-state entry instead of reading from MOD-09 (CAP-29)
- Any implementation component treating a cached or derived portfolio value as authoritative state for another component

What Is Permanently Permitted:
- A module maintaining a local read-cache of MOD-09's output for performance purposes, provided it is treated strictly as a transient local view and is never consumed by other modules as portfolio state
- MOD-05, MOD-06, MOD-07 receiving portfolio state from MOD-09 through the constitutional dependency edges (ADR-002 Section 6.1)

Enforcement Test: Is the portfolio state being consumed by MOD-05, MOD-06, or MOD-07 sourced from MOD-09 (CAP-29) through the authorized dependency edge? If any module is sourcing portfolio state from anywhere other than MOD-09's output: PROHIBITED.

---

**RULE OWN-02 | Governance State Ownership Is Exclusively MOD-06**

Constitutional Source: AF SECTION-04 "Governance State" — Owner: DOM-06; ADR-001 OWN-04; ADR-002 Section 5; ADR-000 P-06.

The four halt-state flags, entry/exit condition records, compliance signals, and limit compliance status are owned exclusively by MOD-06 (producing capabilities: CAP-19, CAP-23, CAP-24, CAP-25, CAP-26, CAP-27, CAP-31).

What Is Permanently Prohibited:
- Any module other than MOD-06 maintaining authoritative halt-state flags
- MOD-05 maintaining its own internal flag indicating "governance is currently halted" that it evaluates independently of MOD-06's state
- Any module evaluating governance conditions (drawdown ≥ 5%, position limit breach, circuit breaker condition) and acting on that evaluation without routing through MOD-06's constitutionally assigned capabilities

What Is Permanently Permitted:
- MOD-05 receiving the halt gating signal from MOD-06 through the authorized dependency edge (ADR-002 Section 6.1: MOD-06 → MOD-05 — halt gating on recommendation issuance)
- MOD-07 receiving active halt state flags from MOD-06 for display in the advisory package (ADR-002 Section 6.1: MOD-06 → MOD-07)

Enforcement Test: Is the halt-state determination that gates MOD-05's recommendation issuance produced by MOD-06's capabilities (CAP-24, CAP-25, CAP-26, CAP-27) and received by MOD-05 through the authorized dependency edge? If any halt-state determination originates outside MOD-06: PROHIBITED.

---

**RULE OWN-03 | Attribution Record Ownership Is Exclusively MOD-08**

Constitutional Source: AF SECTION-04 "Attribution Records" — Owner: DOM-08; ADR-000 P-08; SADR CONSTRAINT-07; SDM-13 Rules 8, 9, 10; ADR-002 Section 3 MOD-08.

Attribution records (System Alpha layer, Human Override Delta layer, theoretical expectancy records) are owned exclusively by MOD-08. The only authorized consumers are the human (for review) and MOD-10 (for audit).

What Is Permanently Prohibited:
- Any module other than MOD-08 producing attribution measurements and routing them to any recommendation or governance capability
- Any automated feedback path from MOD-08's outputs to MOD-01, MOD-02, MOD-03, MOD-04, MOD-05, or MOD-06
- Any mechanism that applies attribution findings to modify signal weights, validation thresholds, confidence formula parameters, EV computation parameters, ranking criteria, allocation weights, or governance thresholds without explicit human approval

What Is Permanently Permitted:
- MOD-08 outputs (attribution reports, insights, warnings) being made available for human review
- MOD-08 outputs flowing to MOD-10 (audit) as records
- A human, having reviewed attribution findings, initiating a change to system behavior through a constitutionally authorized change process — not through an automated path from MOD-08

Enforcement Test: Does any path exist by which MOD-08's output reaches MOD-01 through MOD-06 without passing through explicit human approval? If yes: PROHIBITED.

---

**RULE OWN-04 | Audit Record Ownership Is Exclusively MOD-10**

Constitutional Source: AF SECTION-04 "Audit Records" — Owner: DOM-10; AF 5.1; AF 5.4; CAP-30 Boundary; ADR-000 P-07; ADR-001 AUD-05, AUD-06.

Audit records are owned exclusively by MOD-10 (CAP-30). The only authorized consumer of audit output is the human (for review). No system capability reads from MOD-10 at runtime.

What Is Permanently Prohibited:
- Any system capability reading from MOD-10's audit records to influence its operational behavior
- A confidence scoring component using historical audit records to calibrate formula parameters autonomously
- A governance component reading past halt-entry frequency from audit records to adjust sensitivity thresholds
- An attribution component reading from audit records to populate tracking records (attribution must observe the live system, not read from audit)
- Any automated pipeline where audit data flows into any recommendation, validation, confidence, EV, ranking, allocation, or governance capability

What Is Permanently Permitted:
- Human review and analysis of audit records for any purpose, including as input to decisions about architectural or behavioral changes (which must then pass through the constitutionally authorized change process)
- Reporting and analytics functions that read audit records for human-facing dashboards, provided these functions have no write path to any capability that produces recommendations

Enforcement Test: Is there any system code path, event subscription, function call, or state access by which any AUTONOMOUS_RESEARCH or SHARED_AUTHORITY capability reads from MOD-10's records? If yes: PROHIBITED.

---

**RULE OWN-05 | Supplementary Signal Ownership and Routing Is Exclusively Constitutional**

Constitutional Source: AF SECTION-04 "Signals — supplementary" — Owner: DOM-03; AF DOM-03 GOV-VAL05 Boundary; GOV-VAL05 Rules 1, 4; ADR-001 OWN-07; ADR-002 Section 3 MOD-03.

Supplementary signals (news/sentiment data produced by CAP-08) are owned by MOD-03. Their constitutional routing is: within MOD-03 to CAP-09 only; then to the human-facing advisory report assembled for MOD-07. No other destination is constitutionally authorized.

What Is Permanently Prohibited:
- Supplementary signal data reaching MOD-04, MOD-05, or any module whose function is computation rather than advisory presentation
- A direct or indirect path from CAP-08's output to CAP-12, CAP-13, CAP-15, or CAP-16 (whether labeled "input," "modifier," "weight," "factor," or any other name)
- Passing supplementary signal data through a neutral intermediary module in a routing pattern that circumvents this rule

What Is Permanently Permitted:
- Supplementary signals flowing within MOD-03: CAP-08 → CAP-09 (for conflict evaluation)
- Supplementary signals flowing from MOD-03 to MOD-07: the complete supplementary signal set appearing as a named advisory section in the advisory package presented at CAP-18
- The conflict flag produced by CAP-09 flowing to CAP-12 as advisory annotation on the confidence score output — provided the annotation schema cannot be used as a numeric modifier to the score

Enforcement Test: Is there any path by which supplementary signal data (CAP-08 output) reaches MOD-05's computational capabilities (CAP-12, CAP-13, CAP-15, CAP-16)? If yes: PROHIBITED. Is the conflict flag received by CAP-12 used as a numeric input to the confidence computation rather than as annotation metadata? If yes: PROHIBITED.

---

**RULE OWN-06 | Report Composition Does Not Transfer Section Ownership**

Constitutional Source: AF 4.1; ADR-002 Section 3 MOD-07; ADR-000 P-04.

The advisory report assembled at MOD-07 is a composite view. Each section of the report is owned by the module that produced it. Composition at MOD-07 does not transfer ownership.

What Is Permanently Prohibited:
- MOD-07 treating the advisory report as a single owned information class that it produces from scratch — it assembles from constitutional inputs, it does not originate them
- Any post-composition transformation that modifies a section's content in a way that would constitute MOD-07 "producing" that section's data
- MOD-07 filtering, re-ordering, or selectively presenting recommendations in a way that effectively re-performs the ranking function that constitutionally belongs to MOD-05 (CAP-15)

What Is Permanently Permitted:
- MOD-07 assembling the complete advisory package from its constitutional inputs: MOD-05 outputs + MOD-03 supplementary advisory section + MOD-06 halt state flags + MOD-09 drawdown status
- MOD-07 presenting the assembled package to the human as the Open Menu mandated by CONSTRAINT-09 and SDM-08 Rule 8

Enforcement Test: Is MOD-07's presentation layer modifying the content, ordering, or selection of any recommendation section in a way that effectively re-performs a function assigned to MOD-05? If yes: PROHIBITED.

---

## SECTION 04 — DEPENDENCY ENFORCEMENT RULES

### 4.1 The Constitutional Dependency Graph

The allowed dependency graph is specified exhaustively in AF 5.1 and ADR-002 Section 6.1. "All permitted dependencies are listed" in ADR-002 Section 6.1. Any dependency not enumerated in that list is not permitted.

**Constitutional Sources:** AF 5.1; AF 5.4; ADR-002 Section 6.1; ADR-002 Section 7; ADR-000 P-10; ADR-001 DEP-01 through DEP-10.

---

**RULE DEP-01 | The Dependency Graph Is a DAG Within Any Single Cycle**

Constitutional Source: AF 5.3; ADR-000 P-10; ADR-001 DEP-01.

What Is Permanently Prohibited:
- Any information class flowing back toward its own producer within a single recommendation cycle through an internal system path
- An online-learning or adaptive mechanism internal to the recommendation pipeline that updates its own inputs based on its outputs within the same cycle
- A validation component that updates its own acceptance thresholds based on the confidence scores produced downstream of it in the same cycle

What Is Permanently Permitted:
- Inter-cycle evolution of system behavior through explicit human approval (SDM-13 Rule 9), which routes attribution findings through the human before any behavioral change is authorized
- The DOM-07 → DOM-09 path (recommendations → portfolio state update) which exits the system boundary through the human's external execution and re-enters only when the external execution record is confirmed — this path is broken at the system boundary by the human actor and does not constitute a cycle (AF 5.3)
- The DOM-06 → DOM-11 relationship, which is an activation initiation chain (not a data dependency cycle) confirmed by AF 5.3 secondary check

Enforcement Test: Does any data dependency path within the system create a route by which a module's own prior-cycle output feeds back as a current-cycle input without passing through the human or through a constitutionally authorized change process? If yes: PROHIBITED.

---

**RULE DEP-02 | FORB-01: Attribution Has No Write Edge to Recommendation or Governance Logic**

Constitutional Source: AF 5.4; SADR CONSTRAINT-07; SDM-13 Rules 8, 10; ADR-000 P-08; ADR-002 FORB-01.

What Is Permanently Prohibited:
- MOD-08 → MOD-01 (any write edge)
- MOD-08 → MOD-02 (any write edge)
- MOD-08 → MOD-03 (any write edge)
- MOD-08 → MOD-04 (any write edge)
- MOD-08 → MOD-05 (any write edge)
- MOD-08 → MOD-06 (any write edge)
- Any transitive path by which MOD-08 output modifies any recommendation, validation, confidence, EV, ranking, allocation, or governance logic

What Is Permanently Permitted:
- MOD-07 → MOD-08 (ADR-002 Section 6.1: post-gate read-only)
- MOD-01 → MOD-08 (ADR-002 Section 6.1 as amended by ADR-003B: market outcome data, read-only, time-delayed, for CAP-21 only)
- MOD-02 → MOD-08 (ADR-002 Section 6.1 as amended by ADR-003B: market regime context, read-only, time-delayed, for CAP-21 only)
- MOD-08 → human (attribution reports, insights, warnings — read-only presentation)
- MOD-08 → MOD-10 (attribution event records — audit only)

Enforcement Test: Does MOD-08 produce any output, event, signal, state update, or side effect that is consumed by any capability in MOD-01 through MOD-06 as a computational or governance input? If yes: PROHIBITED.

---

**RULE DEP-03 | FORB-02: Audit Has No Outbound Edge**

Constitutional Source: AF 5.4; AF 5.1; CAP-30 Boundary; ADR-000 P-07; ADR-002 FORB-02.

What Is Permanently Prohibited:
- MOD-10 → any other module (any outbound edge of any type)
- Any system capability reading from MOD-10's records at runtime to influence its behavior

What Is Permanently Permitted:
- ALL modules → MOD-10 (all events from all capabilities flow to audit; this is the constitutional inbound direction)
- Human reading from MOD-10's audit records for review

Enforcement Test: Does any module other than human review have any read access to MOD-10's records that is then used to influence the behavior of any capability? If yes: PROHIBITED. Does MOD-10 produce any output to any other module? If yes: PROHIBITED.

---

**RULE DEP-04 | FORB-03: Supplementary Signals Do Not Enter MOD-05 Computation**

Constitutional Source: AF 5.4; GOV-VAL05 Rule 1; ADR-002 FORB-03; ADR-000 P-09; ADR-003B CHANGE_01.

What Is Permanently Prohibited:
- MOD-03 supplementary signals (CAP-08 output) → CAP-12 (as computational input)
- MOD-03 supplementary signals (CAP-08 output) → CAP-13 (as computational input)
- MOD-03 supplementary signals (CAP-08 output) → CAP-15 (as computational input)
- MOD-03 supplementary signals (CAP-08 output) → CAP-16 (as computational input)
- Any routing pattern that achieves the same computational effect through intermediate modules

What Is Permanently Permitted:
- MOD-03 supplementary signals → CAP-09 within MOD-03 (conflict evaluation only)
- MOD-03 supplementary signals → MOD-07 (advisory report section only, per GOV-VAL05 Rule 4)
- MOD-03 supplementary signals → CAP-20 for exit evaluation only, subject to SDM-12's exit precedence hierarchy (Risk > Technical > Time), per ADR-003B CHANGE_01 — CAP-20 is not in the FORB-03 enumerated prohibition because exit evaluation is governed by SDM-12 (Level 1), not GOV-VAL05 (Level 2)

Enforcement Test: Is there any dependency edge, function call, shared state access, or event subscription by which any output of CAP-08 reaches CAP-12, CAP-13, CAP-15, or CAP-16 as a computational input? If yes: PROHIBITED.

---

**RULE DEP-05 | FORB-04: No Module Has an Interface Toward the Broker or Execution Venue**

Constitutional Source: AF 5.4; GOV-01 Rule 1; GOV-02 Rules 4–5; SADR CONSTRAINT-01; ADR-000 P-03; ADR-002 FORB-04.

What Is Permanently Prohibited:
- Any module, capability, or implementation component establishing any outbound interface, API call, message, or network connection toward any broker, execution venue, or market-order routing system
- Any autonomous stop-loss execution, emergency liquidation, or trade modification that the system initiates without human action
- Any implementation that could, under any conditional logic, emit a market order without requiring a prior explicit human action at CAP-18

What Is Permanently Permitted:
- The human interacting with a broker independently of the system, and the system subsequently receiving the authoritative external execution record as a system input to MOD-09 (CAP-29)

Enforcement Test: Does any implementation component have any outbound interface, API client, message producer, or connection that routes toward a broker or execution venue? If yes: PROHIBITED regardless of what logic wraps it or what conditions must be satisfied.

---

**RULE DEP-06 | FORB-05: No Signal Logic May Consume Unverified Data**

Constitutional Source: AF 5.4; SDM-02 Rule 2; SDM-05 Rule 1; ADR-002 FORB-05.

What Is Permanently Prohibited:
- Any signal generation capability (MOD-03), validation capability (MOD-04), or recommendation computation capability (MOD-05) receiving data that has not passed CAP-02's cross-verification gate
- Any implementation pattern that receives raw market data directly and performs signal logic before verification is confirmed

What Is Permanently Permitted:
- MOD-01 receiving raw data for the sole purpose of feeding it to CAP-02 for verification — before verification, MOD-01 holds the data internally and does not forward it to any signal logic

Enforcement Test: Is there any data path by which raw, unverified market data reaches MOD-03, MOD-04, or MOD-05 without having passed CAP-02's cross-verification gate? If yes: PROHIBITED.

---

**RULE DEP-07 | FORB-06: No Path to Trade Action Bypasses CAP-18**

Constitutional Source: AF 5.4; SDM-CONST-06; SDM-CONST-13; SADR CONSTRAINT-01; ADR-000 P-03; ADR-002 FORB-06.

What Is Permanently Prohibited:
- Any path — direct, transitive, conditional, or emergency — from any recommendation-generating capability to any trade action that does not pass through CAP-18 (MOD-07)
- A "safety liquidation" feature that executes trades autonomously when drawdown approaches a threshold
- A scheduled order placement operating on pre-approved recommendation templates
- A stop-loss placement executed by the system after the human approves a trade entry
- Any approval mechanism that auto-accepts recommendations below a confidence threshold or after a time limit elapses without explicit human interaction

What Is Permanently Permitted:
- The human, having received the full advisory package at CAP-18, choosing to take a trade action through their broker — entirely outside the system boundary

Enforcement Test: Starting from any recommendation-producing capability (CAP-12, CAP-13, CAP-15, CAP-16, CAP-17, CAP-20), does any path exist — through any combination of modules — to any market-facing action that does not require an explicit human action at CAP-18 to proceed? If yes: PROHIBITED.

---

**RULE DEP-08 | FORB-07: No Module Maintains a Private Portfolio State Derivative**

Constitutional Source: AF 5.5; ADR-000 P-05; ADR-002 FORB-07; SADR CHANGE-01/CHANGE-02.

What Is Permanently Prohibited:
- Any module maintaining a private copy of portfolio position count, drawdown, concentration, or illiquidity state that is then consumed by other modules as authoritative portfolio state
- A risk enforcement module maintaining its own running position count updated on each recommendation cycle rather than reading from MOD-09 at evaluation time

What Is Permanently Permitted:
- A module maintaining a transient local copy of MOD-09 output within a single processing unit for the duration of one computation, provided this copy is never exported to other modules as portfolio state

Enforcement Test: Is any portfolio state value being consumed by MOD-05, MOD-06, or MOD-07 sourced from anywhere other than MOD-09 (CAP-29) through the authorized dependency edge? If yes: PROHIBITED.

---

**RULE DEP-09 | FORB-08: Conflict Flag Is Annotation Only in CAP-12**

Constitutional Source: SADR_AMENDMENT_VAL-05; AF DOM-03 GOV-VAL05 Boundary; ADR-002 FORB-08; ADR-003 IAC-06.

The conflict flag produced by CAP-09 (MOD-03) may flow to CAP-12 (MOD-05) for annotation purposes only. It must not serve as a numeric modifier to the confidence score.

What Is Permanently Prohibited:
- A confidence formula where the conflict flag input produces a numeric delta (positive or negative) applied to the score
- A confidence formula where the conflict flag triggers a percentage reduction in the confidence score
- Any schema for the conflict flag that allows it to be parsed as a numeric weight by CAP-12's computation

What Is Permanently Permitted:
- The conflict flag appearing as a metadata attribute on the confidence score output, readable by the human but not consumed by any downstream computation as a numeric modifier
- The conflict flag being displayed in the advisory package at CAP-18 as a human-visible annotation

Enforcement Test: Is the conflict flag received by CAP-12 processed through any arithmetic or weighted formula before producing the confidence score output? If yes: PROHIBITED.

---

**RULE DEP-10 | FORB-09: MOD-11 Activation Events Are Not Data Inputs to Computational Logic**

Constitutional Source: AF 5.3 secondary check; ADR-002 FORB-09; ADR-003B CHANGE_02; ADR-003 IAC-12.

What Is Permanently Prohibited:
- Any module consuming the MOD-11 activation event as a computational data input — i.e., using the event's content, timing, or mode as an input variable to any capability's computational logic
- CAP-23, CAP-19, or CAP-31 in MOD-06 using the activation event as a trigger that "starts" their monitoring — these capabilities are continuous and not cycle-gated

What Is Permanently Permitted:
- The activation event reaching all autonomous modules as an initiation signal that authorizes a new recommendation cycle to begin
- Modules that are cycle-dependent using the activation event to initiate their processing
- MOD-06's detection capabilities (CAP-19, CAP-23, CAP-31) operating continuously, receiving the activation event only as context that a new cycle was authorized — not as a computational input consumed by their detection logic (per ADR-003B CHANGE_02)

Enforcement Test: Is the activation event produced by CAP-28 (MOD-11) consumed as a data value — parsed for its content, used as an input variable, or treated as a "start command" — by any detection or computational capability? If yes: PROHIBITED.

---

**RULE DEP-11 | FORB-10: Halt States Share No State Across Their Boundaries**

Constitutional Source: SDM-CONST-14; AF DOM-06 Independence Constraint; ADR-000 P-06; ADR-002 FORB-10; ADR-003 IAC-07.

What Is Permanently Prohibited:
- A single shared variable, flag, trigger evaluator, or exit mechanism that spans two or more halt-state capabilities (CAP-24, CAP-25, CAP-26, CAP-27)
- An exit procedure for one halt state that checks or depends on the state of another halt state
- A design where entering one halt state implicitly activates, suppresses, or modifies another halt state
- A combined halt-state manager with a single enumerated state that allows only one active halt state at a time
- A shared condition evaluator that triggers entry into multiple halt states from a single monitoring check

What Is Permanently Permitted:
- The combined gating effect of all simultaneously active halt states being computed by evaluating each state independently and blocking recommendation issuance if any is active
- Each halt-state capability maintaining its own independent entry condition evaluator, active-state representation, and exit condition evaluator

Enforcement Test: Does the proposed implementation allow the entry logic, state representation, or exit logic of any one halt state to share a variable, function, or state reference with any other halt state? If yes: PROHIBITED.

---

**RULE DEP-12 | All Unlisted Dependencies Are Prohibited**

Constitutional Source: ADR-002 Section 6.1: "All permitted dependencies are listed below"; ADR-001 DEP-09; AF 5.1.

What Is Permanently Prohibited:
- Any dependency edge between two modules that is not explicitly listed in ADR-002 Section 6.1 (as amended by ADR-003B for MOD-01 → MOD-08 and MOD-02 → MOD-08)
- Creating a new module-to-module data flow path for "convenience," "performance," or "simplification" without first establishing its constitutional authority through a constitutional amendment

What Is Permanently Permitted:
- Every dependency edge listed in ADR-002 Section 6.1
- Future constitutional amendments that add authorized dependency edges, provided each addition is traced to constitutional authority at Level 1 (SDM) or Level 3 (SADR) and does not violate any prohibition in AF 5.4

Enforcement Test: For any proposed dependency edge from Module A to Module B: is it explicitly listed in ADR-002 Section 6.1? If not: PROHIBITED until a constitutional amendment adds it with full authority tracing.

---

## SECTION 05 — GOVERNANCE ENFORCEMENT RULES

### 5.1 Governance Boundary Derivation

Governance is the constitutional function that gates recommendation authority when risk or compliance conditions are detected. All governance authority is owned by MOD-06. Governance gates recommendation issuance only — it never gates monitoring, audit, attribution, reporting, or portfolio state maintenance.

**Constitutional Sources:** SDM-CONST-14; GOV-01; GOV-02; SDM-15; AF 6.1; AF 6.2; ADR-000 P-06; ADR-002 Section 3 MOD-06.

---

**RULE GOV-01 | Governance Gates Recommendation Issuance — Nothing Else**

Constitutional Source: AF 6.1; GOV-01 Rule 4; GOV-02 Rule 3; SDM-15 Rule 14; ADR-001 GOV-R02; ADR-003 IAC-08.

What Is Permanently Prohibited:
- Any halt state suspending, pausing, or disabling MOD-01 (market data), MOD-02 (market context), MOD-03 (evidence generation), MOD-04 (statistical validation), MOD-08 (attribution), MOD-09 (portfolio state), MOD-10 (audit), or MOD-11 (activation) functions
- Any halt state preventing MOD-06's own detection capabilities (CAP-19, CAP-23, CAP-31) from continuing to operate
- Any implementation design where a halt-state flag, if set, propagates into non-recommendation modules and suspends their operation

What Is Permanently Permitted:
- Any halt state blocking MOD-05's issuance of recommendations to MOD-07 (the constitutional gating surface)
- MOD-06 detecting conditions and entering halt states while all other system functions continue
- GOV-01 Rule 4 compliance: during Governance Halt (State 1), the system must generate a critical risk escalation report — reporting (MOD-06 escalation report) must continue

Enforcement Test: Does the implementation of any halt state cause any capability in MOD-01, MOD-02, MOD-03, MOD-04, MOD-08, MOD-09, MOD-10, or MOD-11 to stop operating? If yes: PROHIBITED. Does the implementation cause MOD-06's detection capabilities to stop operating? If yes: PROHIBITED.

---

**RULE GOV-02 | The Four Halt States Are Constitutionally Independent**

Constitutional Source: SDM-CONST-14; SADR Section 5 "Halt State Independence"; AF DOM-06 Independence Constraint; ADR-000 P-06; ADR-003 IAC-07.

What Is Permanently Prohibited:
- A single `halt_state` enumeration or flag that can represent only one active state at a time
- Any exit condition that restores multiple halt states simultaneously
- Any entry condition for one halt state that implicitly also activates another
- Any design where clearing one halt state implicitly permits recommendation issuance without checking whether other halt states remain active
- A shared state variable accessed by two or more halt-state capabilities (CAP-24, CAP-25, CAP-26, CAP-27)

What Is Permanently Permitted:
- Four independent halt-state representations, each maintained by its designated capability, any combination of which may be simultaneously active
- The combined gating effect computed by evaluating all four states independently and blocking issuance if any is active

Enforcement Test: Can States 1 and 4 be simultaneously active? Does the implementation support this? Does clearing State 4 leave State 1 still active? If the answers are not "yes, yes, yes": PROHIBITED.

---

**RULE GOV-03 | Governance Holds Zero Execution Authority**

Constitutional Source: SDM-CONST-14; GOV-01 Rule 1; GOV-02 Rules 4–5; ADR-001 GOV-R08; ADR-002 Section 3 MOD-06.

What Is Permanently Prohibited:
- Any halt state triggering any form of autonomous market action (stop-loss, emergency sale, position reduction)
- MOD-06 capabilities producing any output directed toward a broker or market system
- A governance enforcement design where a limit breach triggers automatic position reduction by the system

What Is Permanently Permitted:
- MOD-06 producing human-visible alerts and escalation reports during halt states, which the human may act upon through their broker independently

Enforcement Test: Does MOD-06's halt-state management produce any output other than: (a) blocking MOD-05 issuance, (b) human-visible alerts/escalation reports, (c) governance events to MOD-11, (d) audit records to MOD-10? If yes: PROHIBITED.

---

**RULE GOV-04 | Halt-State Exit Authorities Are Constitutionally Fixed**

Constitutional Source: AF 6.2; SDM-CONST-14; GOV-01 Rule 5; GOV-02 Rule 3; SDM-15 Rule 14; SADR Section 7; ADR-001 GOV-R04 through GOV-R07.

The exit authority for each state is constitutionally fixed and may not be changed by an implementation ADR:

| State | Exit Authority | Exit Mechanism |
|-------|---------------|----------------|
| State 1 — Governance Halt (CAP-25) | Human | Explicit human resumption authorization |
| State 2 — Governance Lockout (CAP-26) | System + Human | Human corrects violation; system (CAP-31) detects restoration automatically |
| State 3 — Conditional Recommendation Suspension (CAP-27) | System | CAP-23 detects condition clearance automatically |
| State 4 — Hard Deterministic Halt (CAP-24) | Human + System | Human acknowledgment plus system confirms return within limits |

What Is Permanently Prohibited:
- A State 1 exit that occurs automatically without explicit human authorization
- A State 2 exit that requires human re-authorization beyond the corrective action — restoration detection is automatic once the violation is corrected
- A State 3 exit that requires human action — it must be condition-driven and automatic
- A State 4 exit that occurs from system condition detection alone without human acknowledgment

Enforcement Test: For each halt state, does the implementation require exactly the exit authority specified above — neither more nor less? If any state exits through a different authority than specified: PROHIBITED.

---

## SECTION 06 — HUMAN AUTHORITY ENFORCEMENT RULES

### 6.1 Human Authority Boundary

The human is the sole trade execution actor, sole approval authority, and sole authority for certain governance exits. No system component holds execution authority. No path to a trade action may exist that does not pass through CAP-18 (MOD-07). This is an unconditional constitutional prohibition with no performance escape clause and no emergency exception.

**Constitutional Sources:** SDM-CONST-06; SDM-CONST-13; CAP-18 Boundary; SADR CONSTRAINT-01; AF 5.2; AF 5.4; ADR-000 P-02, P-03; ADR-001 DEP-04; GOV-01 Rule 1.

---

**RULE HAP-01 | CAP-18 Is the Unconditional Gate for All Trade Actions**

Constitutional Source: SDM-CONST-06; SDM-CONST-13; SADR CONSTRAINT-01; SADR Section 5 / AF 5.2 "CAP-18 blocks all trade action — no exceptions, no bypass"; ADR-000 P-03.

What Is Permanently Prohibited:
- Any implementation that allows a trade action to occur without an explicit, contemporaneous human action at CAP-18
- A timeout-based auto-approval that converts a non-action into approval after a waiting period
- A pre-approved template mechanism that applies human approval from a previous cycle to execute a recommendation in the current cycle
- A conditional automation that executes a trade if specified conditions are met without human interaction at the time of execution
- Any implementation ADR describing a component that could, under any conditional logic, emit a market order without requiring a prior explicit human action

What Is Permanently Permitted:
- A human explicitly approving a recommendation through CAP-18, after which the system records the approved decision and makes it available (to MOD-08 post-gate and to MOD-09 via the external execution pathway) — note that the trade itself is still executed by the human through their broker, not by the system

Enforcement Test: Is there any path through the system from any recommendation to any market-facing action that does not require the human to take an explicit, irreplaceable action at CAP-18 at the time of that specific action? If yes: PROHIBITED.

---

**RULE HAP-02 | Advisory Presentation Must Preserve Human Decision Space**

Constitutional Source: SDM-08 Rule 8; SADR CONSTRAINT-09; CAP-18 Boundary; GOV-VAL05 Criterion 1; ADR-000 P-02; ADR-003 IAC-09.

What Is Permanently Prohibited:
- A presentation mechanism that displays only the top-ranked opportunity and requires rejection to view others — this constitutes sequential forced selection, prohibited by CONSTRAINT-09
- A presentation mechanism that pre-blends the sentiment advisory section into the confidence score before presenting it to the human — this violates GOV-VAL05's preservation of "raw inputs" for human judgment
- A presentation sequence that pressures the human's choice by ordering information in a persuasive sequence rather than as a simultaneous inventory
- An approval gate with any form of timeout-based auto-completion

What Is Permanently Permitted:
- A presentation that displays all EV-filtered, positively-ranked opportunities simultaneously, with their complete computational scores and the supplementary advisory section displayed as a distinct named section — the Open Menu required by SDM-08 Rule 8

Enforcement Test: Does the implementation of MOD-07's presentation layer present all authorized opportunities simultaneously? Is the sentiment advisory section clearly distinct from computationally derived scores? Is there any auto-completion mechanism of any kind? If not, not, or yes respectively: PROHIBITED.

---

**RULE HAP-03 | Human Authority Over Attribution-Driven Behavior Change**

Constitutional Source: SDM-13 Rule 9; ADR-000 P-08; SADR CONSTRAINT-07; ADR-002 Section 3 MOD-08.

What Is Permanently Prohibited:
- Any automated mechanism by which attribution findings (MOD-08 outputs) modify the behavior of any AUTONOMOUS_RESEARCH capability without an explicit human approval action

What Is Permanently Permitted:
- Attribution findings being presented to the human as insights and warnings
- The human, having reviewed attribution findings, deciding to change system behavior and initiating that change through a constitutionally authorized change process that requires explicit human action at each step

Enforcement Test: Is there any path from MOD-08's attribution outputs to any behavioral change in MOD-01 through MOD-06 that does not require an explicit human approval action? If yes: PROHIBITED.

---

## SECTION 07 — VAL05 ENFORCEMENT RULES

### 7.1 VAL05 Scope and Permanence

GOV-VAL05 (VAL05_OWNER_DECISION_RESOLUTION) is a Level 2 authority — it amends SDM_V2.3 and SADR_V2.1 simultaneously. Its ruling is permanent and may not be reopened by any implementation ADR. Its effect is to permanently close the computational pathway between sentiment/news signals and the confidence scoring, EV computation, opportunity ranking, and conviction-weighted allocation pipelines.

**Constitutional Sources:** GOV-VAL05 Rules 1–5; SADR_AMENDMENT_VAL-05; AF DOM-03 GOV-VAL05 Boundary; AF 3.3 anti-leakage check 4; ADR-000 P-09.

---

**RULE VAL05-01 | Confidence Computation Is Technically Pure**

Constitutional Source: GOV-VAL05 Rule 1; SADR_AMENDMENT_VAL-05 CAP-12; ADR-003 IAC-05.

What Is Permanently Prohibited:
- Any sentiment score, news sentiment value, NLP output score, or AI-model emotional valuation entering the confidence formula for CAP-12 in any form — as an addend, multiplier, weight, modifier, floor, ceiling, or conditional gate
- A confidence formula that uses sentiment as a "tiebreaker" between two technically equal opportunities
- A confidence implementation where sentiment data is pre-processed into a "technical-looking" number and then fed into the confidence formula with the sentiment origin obscured

What Is Permanently Permitted:
- The confidence score being derived exclusively from technical evidence (CAP-07 outputs) and statistical validation (CAP-10, CAP-11 outputs)
- The conflict flag from CAP-09 appearing as annotation metadata on the confidence score output without modifying the score value

Enforcement Test: Does the confidence score produced by CAP-12 change in response to any input that is traceable to CAP-08 (supplementary signal intake), to any NLP model output, or to any news event valuation? If yes: PROHIBITED.

---

**RULE VAL05-02 | EV Computation, Ranking, and Allocation Are Technically Pure**

Constitutional Source: GOV-VAL05 Rule 1; GOV-VAL05 Rule 5 (VAL-11 closed: sentiment to Kelly fractions; VAL-15 closed: sentiment to position sizing); ADR-000 P-09.

What Is Permanently Prohibited:
- Sentiment data entering CAP-13 (Expected Value Computation) as any form of input — adjustment, signal weight, or parameter
- Sentiment data entering CAP-15 (Opportunity Ranking) as a re-ordering criterion or tiebreaker
- Sentiment data entering CAP-16 (Conviction-Weighted Allocation) as a position size modifier, Kelly fraction input, or allocation scaling factor

What Is Permanently Permitted:
- CAP-13, CAP-15, CAP-16 receiving from technically pure upstream sources: CAP-12 confidence scores, MOD-01 market data, MOD-02 regime context, MOD-09 portfolio state — all of which are exclusively technically derived

Enforcement Test: Does the output of CAP-13, CAP-15, or CAP-16 change in response to any input traceable to supplementary signal data (CAP-08 output)? If yes: PROHIBITED.

---

**RULE VAL05-03 | Closed Pathways VAL-07, VAL-11, VAL-15 Are Permanently Closed**

Constitutional Source: GOV-VAL05 Rule 5; ADR-000 P-09.

What Is Permanently Prohibited:
- Implementing or re-opening the computational pathway described by VAL-07 (NLP sentiment scores to confidence weights)
- Implementing or re-opening the computational pathway described by VAL-11 (sentiment scores to Kelly fractions / allocation inputs)
- Implementing or re-opening the computational pathway described by VAL-15 (sentiment to position sizing without violating determinism)
- Any implementation ADR that describes any of these three pathways as an open option for resolution

What Is Permanently Permitted:
- No future ADR may re-open these pathways without a new Level 2 authority decision by the owner — a Level 8 or lower implementation ADR cannot reopen what a Level 2 resolution has permanently closed

Enforcement Test: Does the proposed implementation introduce any pathway that converts sentiment signal data into confidence weights, Kelly fractions, or position size inputs? If yes: PROHIBITED regardless of how the pathway is labeled.

---

**RULE VAL05-04 | Sentiment Appears in the Advisory Report as a Distinct Named Section**

Constitutional Source: GOV-VAL05 Rule 4; AF DOM-03 GOV-VAL05 Boundary; ADR-002 Section 3 MOD-03.

What Is Permanently Prohibited:
- Presenting sentiment data to the human in a format that visually blends it with computationally derived confidence scores, EV estimates, or rankings
- Displaying sentiment as a modifier to or qualifier of the confidence score display (e.g., "Confidence: 78% (positive sentiment)")
- Embedding sentiment analysis results within the computational sections of the advisory report

What Is Permanently Permitted:
- A dedicated, clearly labeled advisory section in the human-facing advisory report that presents the supplementary signal set, including news analysis, sentiment scores, and CAP-09 conflict flags, as a distinct section separate from the computational outputs

Enforcement Test: In the advisory package presented at CAP-18, is the supplementary signal content in a section that is visually and structurally distinct from the computationally derived confidence scores, EV estimates, rankings, and allocation suggestions? If not: PROHIBITED.

---

## SECTION 08 — AUDIT PROTECTION RULES

### 8.1 Audit Inviolability

MOD-10 is the terminal information sink. It receives immutably from all modules and has zero outbound edges. Its records are structurally protected from modification and from use as computational inputs by any capability.

**Constitutional Sources:** CAP-30 Boundary; AF 5.1; AF 5.4; AF DOM-10; ADR-000 P-07; ADR-001 AUD-01 through AUD-06; ADR-002 Section 3 MOD-10; ADR-003 IAC-11.

---

**RULE AUD-01 | Every Capability Must Produce an Audit Record**

Constitutional Source: SDM-02 through SDM-15 Audit clauses; SADR CAP-30 necessity clause; ADR-003 IAC-04.

What Is Permanently Prohibited:
- Any capability that performs a constitutionally mandated function without producing an audit record of that function's execution
- An implementation design where audit record production is optional or conditional

What Is Permanently Permitted:
- Every capability routing its audit output to MOD-10 as a mandatory, unconditional output of its execution

Enforcement Test: For each of the 31 SADR capabilities, is there a mandatory, unconditional audit record produced and delivered to MOD-10? If any capability may complete its function without producing an audit record: PROHIBITED.

---

**RULE AUD-02 | Audit Records Are Immutable**

Constitutional Source: SADR CHANGE-06; SADR CAP-30 Outputs; ADR-001 AUD-06; ADR-002 Section 3 MOD-10; ADR-003 IAC-11.

What Is Permanently Prohibited:
- Any system operation that modifies a record once it has been received by MOD-10
- Any system operation that deletes an audit record
- An audit implementation described as "append-only" unless the appended records are also individually immutable (the constitutional standard is "immutable," not merely "append-only" per SADR CHANGE-06)

What Is Permanently Permitted:
- New audit records being appended over time as the system continues to operate
- Human review of audit records (read access only, no modification)

Enforcement Test: Can any system capability modify or delete a record once it has been received by MOD-10? If yes: PROHIBITED.

---

**RULE AUD-03 | The Original Recommendation vs. Final Human Action Must Be Immutably Paired**

Constitutional Source: SDM-10 Audit; ADR-001 AUD-02.

What Is Permanently Prohibited:
- An audit implementation that records the final human action without also immutably recording the original system recommendation that preceded it
- Separate, unlinked audit trails for system recommendations and human actions that cannot be deterministically paired

What Is Permanently Permitted:
- A single immutable audit record (or linked pair) that captures both the original system recommendation and the human's final action for each cycle and each decision point

Enforcement Test: For each human decision event at CAP-18, is there an immutable record that can be used to determine both what the system recommended and what the human decided? If not: PROHIBITED.

---

## SECTION 09 — ACTIVATION PROTECTION RULES

### 9.1 Activation Scope

MOD-11 (CAP-28) initiates recommendation cycles. It does not orchestrate them. It does not own the execution of what it initiates. It does not govern outcomes. Its output is an initiation signal — not a data dependency, not a computational input.

**Constitutional Sources:** SDM-CONST-15; SADR CONSTRAINT-10; AF 5.3; ADR-002 FORB-09; ADR-003 IAC-12; ADR-003 Section 8.3; ADR-003B CHANGE_02.

---

**RULE ACT-01 | Activation Is Initiation — Not Orchestration**

Constitutional Source: AF 5.3; ADR-003 Section 8.3; ADR-003 IAC-12; ADR-002 Section 3 MOD-11.

What Is Permanently Prohibited:
- CAP-28 determining or controlling the sequence of module execution after initiation — "first do MOD-01, then MOD-02, then MOD-03" is orchestration, which is constitutionally prohibited
- CAP-28 tracking the progress of a cycle after initiating it
- CAP-28 governing or adjudicating the outcomes of an initiated cycle
- Any implementation that transforms MOD-11 into an orchestration layer by having it issue sequenced commands to modules

What Is Permanently Permitted:
- CAP-28 emitting a single activation initiation signal that authorizes all autonomous modules to begin their cycle
- The execution sequence across modules being determined by the constitutional dependency graph in ADR-002 — each module proceeds when its constitutional inputs are available
- MOD-11 recording which activation mode produced each cycle (for audit)

Enforcement Test: After emitting the activation initiation signal, does MOD-11 (CAP-28) take any subsequent action that directs, sequences, or monitors the execution of any downstream module? If yes: PROHIBITED.

---

**RULE ACT-02 | Three Constitutionally Authorized Activation Modes — No Others**

Constitutional Source: SDM-CONST-15; SADR Section 8; AF DOM-11; ADR-002 Section 3 MOD-11.

The three activation modes are constitutionally fixed:
- Mode 1 — Scheduled: autonomous initiation on predefined schedules
- Mode 2 — On-Demand: initiation upon explicit human request
- Mode 3 — Event-Driven: initiation when governance, risk, or portfolio events trigger mandatory review

What Is Permanently Prohibited:
- A fourth activation mode not present in SDM-CONST-15
- A "background continuous" mode that continuously re-initiates cycles without any of the three constitutional triggers
- Activation triggered by an external system other than the human (Mode 2) or a constitutionally defined governance/risk/portfolio event (Mode 3)

What Is Permanently Permitted:
- All three constitutionally defined modes implemented and operational
- Mode 3 being triggered by governance events from MOD-06 through the constitutionally characterized DOM-06 → DOM-11 event relationship

Enforcement Test: Are all activation triggers in the implementation traceable to one of the three constitutionally authorized modes? If any trigger exists outside these three: PROHIBITED.

---

**RULE ACT-03 | No Activation Mode Grants Trade Execution Authority**

Constitutional Source: SDM-CONST-15; SADR CONSTRAINT-10; AF DOM-11; ADR-002 Section 3 MOD-11.

What Is Permanently Prohibited:
- Any activation mode (including Mode 3 event-driven, even when triggered by a severe governance event) granting any form of trade execution authority to any module
- An argument that a Mode 3 activation triggered by a critical risk event implicitly authorizes the system to take protective market action

What Is Permanently Permitted:
- Mode 3 activation resulting in a new research and governance cycle — including the production of updated recommendations, updated halt states, and updated escalation reports — all of which are advisory and still require human action at CAP-18

Enforcement Test: Does any activation mode grant any module the authority to interact with a broker or market system? If yes: PROHIBITED regardless of the activation trigger's severity.

---

**RULE ACT-04 | Event Pattern Scope Is Constitutionally Bounded**

Constitutional Source: ADR-001 Section 6, Section 7 R7–R9; AF 5.3; SDM-CONST-15.

ADR-001 selected the Hybrid Architectural Style with a bounded event pattern scoped exclusively to:
1. DOM-11 activation initiation (all three modes)
2. DOM-06 governance event signaling to DOM-11

What Is Permanently Prohibited:
- Extending the event pattern to any other inter-module communication relationship not explicitly characterized as event-based in the constitutional corpus
- Using the event pattern in the recommendation pipeline (MOD-03 through MOD-05) — the recommendation pipeline operates within the synchronous modular monolith core
- Using the event pattern to route data across the three blocking gates (CAP-02, CAP-10, CAP-18) — blocking gates require synchronous, unconditional enforcement
- Using the event pattern for audit routing (MOD-10) or portfolio state updates (MOD-09)

What Is Permanently Permitted:
- The event pattern used for Mode 1 activation (scheduled trigger → CAP-28)
- The event pattern used for Mode 2 activation (human request → CAP-28)
- The event pattern used for Mode 3 activation (MOD-06 governance event → CAP-28)

Enforcement Test: Is any proposed event-pattern usage traceable to the two constitutionally characterized event relationships (DOM-11 activation; DOM-06 → DOM-11 governance events)? If not: PROHIBITED.

---

## SECTION 10 — FUTURE EVOLUTION CONSTRAINTS

### 10.1 What Future Architects May Never Change Without Constitutional Amendment

These items are constitutionally frozen at Level 1 through Level 3 (SDM, VAL05, SADR). No implementation ADR, implementation decision, or architectural evolution may alter them. Alteration requires a new owner decision at the same or higher authority level.

---

**EVOCON-01 | The 11 Module / 31 Capability / 13 Information Class Structure Is Frozen**

Constitutional Source: AF 2.0; SADR capability catalog; ADR-002 Sections 2–5; ADR-000 P-11.

No future architect may:
- Add a 12th module without a constitutional amendment to the Architecture Foundation
- Add a 32nd capability without a constitutional amendment to SADR
- Add a 14th information class without a constitutional amendment to the Architecture Foundation
- Remove any of the 31 capabilities
- Reassign a capability from one module to another without a constitutional amendment

---

**EVOCON-02 | Human Approval at CAP-18 Is Permanent and Unconditional**

Constitutional Source: SDM-CONST-06; SDM-CONST-13; SADR CONSTRAINT-01; AF 5.2; ADR-000 P-03.

No future architect may:
- Remove the CAP-18 gate
- Make the CAP-18 gate conditional ("only required above a certain capital threshold")
- Replace the CAP-18 gate with an automated approval mechanism for any category of recommendation
- Re-scope CAP-18 to operate as a ratification mechanism (presenting a pre-selected decision rather than raw inputs for human decision)

This constraint holds regardless of capital scale, system maturity, or future SaaS expansion.

---

**EVOCON-03 | GOV-VAL05 Computational Prohibition Is Permanent**

Constitutional Source: GOV-VAL05 (all rules); ADR-000 P-09; ADR-001 Risk 1.

No future architect may:
- Open a computational pathway from sentiment/news signals to confidence scoring, EV computation, opportunity ranking, or conviction-weighted allocation
- Treat GOV-VAL05 as a calibration choice that can be revisited by an implementation ADR
- Re-open VAL-07, VAL-11, or VAL-15

This is a Level 2 authority decision. Re-opening it requires a new Level 2 authority decision by the owner — not an ADR at any lower level.

---

**EVOCON-04 | The Four Halt States Are Permanently Independent**

Constitutional Source: SDM-CONST-14; AF DOM-06 Independence Constraint; ADR-000 P-06.

No future architect may:
- Merge the four halt states into a unified state machine
- Allow simultaneous active states to share state or exit logic
- Reduce the four halt states to fewer by merging conditions

This constraint applies even if a future system scale makes independent state management operationally more complex — operational complexity does not override constitutional independence.

---

**EVOCON-05 | Attribution Observation Authority Is Permanently Read-Only**

Constitutional Source: SDM-13 Rules 8, 9, 10; SADR CONSTRAINT-07; ADR-000 P-08.

No future architect may:
- Grant MOD-08 any write authority over MOD-01 through MOD-06
- Create an automated feedback path from attribution findings to recommendation behavior
- Implement "adaptive" or "self-improving" components in the recommendation pipeline that update without explicit human approval

---

**EVOCON-06 | The Audit Log Is Permanently Immutable and Terminal**

Constitutional Source: SADR CHANGE-06; CAP-30 Boundary; AF 5.4; ADR-000 P-07.

No future architect may:
- Add any outbound edge from MOD-10 to any capability
- Make audit records modifiable or deletable by any system operation
- Reduce the immutability requirement to "append-only" (which permits deletion without adding — the standard is fully immutable per SADR CHANGE-06)

---

**EVOCON-07 | The Event Pattern Scope Cannot Be Extended Without Constitutional Justification**

Constitutional Source: ADR-001 Section 7 R9; SDM-CONST-15; AF 5.3.

No future architect may:
- Extend the event pattern to any inter-module communication relationship without constitutional evidence that the relationship is characterized as event-based in the authority corpus
- Use "consistency" or "convenience" as justification for extending the event pattern to the recommendation pipeline or to blocking gates

---

**EVOCON-08 | Open Validation Items Must Remain as Extension Points**

Constitutional Source: SADR Section 11 CLASS_B/C/D; SDM-CONST-12; ADR-001 TRC-05; ADR-003 IAC-13.

The open validation items (VAL-01, VAL-02, VAL-03, VAL-04, VAL-06, VAL-08, VAL-09, VAL-10, VAL-12, VAL-13, VAL-14, VAL-16, VAL-17 — minus items closed by GOV-VAL05) are classified CLASS_B/C/D per SADR Section 11. No future architecture or implementation ADR may:
- Treat a CLASS_B validation item's generic interface as a hard-coded formula choice
- Prematurely close an open validation item by baking a specific formula into a module boundary
- Merge two open validation items' generic interfaces in a way that makes future independent resolution impossible

---

**EVOCON-09 | SDM-14 Research Intake Is Constitutionally Deferred — No Anticipation Permitted**

Constitutional Source: SADR Section 10; ADR-001 MOD-05.

SDM-14 (Research Intake / potential future expansion to additional market types or research domains) is constitutionally deferred. No future implementation ADR may:
- Create architectural structures that anticipate SDM-14's resolution
- Design module boundaries that incorporate undeclared assumptions about what SDM-14 will require
- Pre-implement capabilities for SDM-14 scope

---

**EVOCON-10 | Indian Equities NSE/BSE Is the Constitutionally Fixed Market Scope**

Constitutional Source: SDM-CONST-03; AF Section 1.6.

No future architect may:
- Expand the market scope to non-Indian equities markets without a constitutional amendment to SDM-CONST-03
- Design module structures that implicitly assume multi-market data ingestion without a constitutional amendment

---

## SECTION 11 — ARCHITECTURE INTEGRITY VALIDATION

### 11.1 Validation Against SDM_V2.3

| SDM Requirement | Enforcement Rule | Result |
|----------------|-----------------|--------|
| SDM-CONST-06: Human approval mandatory without exception | HAP-01; DEP-07 | ✅ ENFORCED |
| SDM-CONST-12: Modular, replaceable, independently evolvable | MB-04; EVOCON-01 | ✅ ENFORCED |
| SDM-CONST-13: No output is an executable trade order | DEP-05; HAP-01 | ✅ ENFORCED |
| SDM-CONST-14: Four constitutionally independent halt states | GOV-02; DEP-11; EVOCON-04 | ✅ ENFORCED |
| SDM-CONST-15: Three authorized activation modes only | ACT-02; ACT-03 | ✅ ENFORCED |
| SDM-02 Rule 2: No signal logic on unverified data | DEP-06 | ✅ ENFORCED |
| SDM-05 Rule 2: Walk-forward mandatory, K-fold prohibited | MB-01 (capability boundary for CAP-10) | ✅ ENFORCED |
| SDM-08 Rule 8: Open Menu simultaneous presentation | HAP-02 | ✅ ENFORCED |
| SDM-13 Rules 8, 9, 10: Attribution read-only | DEP-02; OWN-03; HAP-03; EVOCON-05 | ✅ ENFORCED |

### 11.2 Validation Against VAL05_OWNER_DECISION_RESOLUTION

| GOV-VAL05 Rule | Enforcement Rule | Result |
|---------------|-----------------|--------|
| Rule 1: Confidence computation technically pure | VAL05-01; DEP-04; OWN-05 | ✅ ENFORCED |
| Rule 4: Sentiment as distinct named advisory section | VAL05-04 | ✅ ENFORCED |
| Rule 5: VAL-07, VAL-11, VAL-15 permanently closed | VAL05-03; EVOCON-03 | ✅ ENFORCED |

### 11.3 Validation Against SADR_V2.1

| SADR Requirement | Enforcement Rule | Result |
|-----------------|-----------------|--------|
| CONSTRAINT-01: No capability initiates, places, modifies, or cancels trade orders | DEP-05; HAP-01; ACT-03 | ✅ ENFORCED |
| CONSTRAINT-07: Attribution read-only | DEP-02; OWN-03; HAP-03 | ✅ ENFORCED |
| CONSTRAINT-08: Walk-forward mandatory | MB-01 (CAP-10 boundary) | ✅ ENFORCED |
| CONSTRAINT-09: Open Menu simultaneous presentation | HAP-02 | ✅ ENFORCED |
| CONSTRAINT-10: No activation mode grants execution authority | ACT-03 | ✅ ENFORCED |
| SADR Section 5 blocking gates (CAP-02, CAP-10, CAP-18) | DEP-06; DEP-03 (CAP-10); HAP-01 | ✅ ENFORCED |
| SADR Section 6 authority classes preserved | MB-03 | ✅ ENFORCED |
| SADR Section 7 halt-state independence | GOV-02; DEP-11 | ✅ ENFORCED |
| SADR CHANGE-06: Audit records immutable | AUD-02; OWN-04 | ✅ ENFORCED |

### 11.4 Validation Against ARCHITECTURE_FOUNDATION_V1

| AF Requirement | Enforcement Rule | Result |
|---------------|-----------------|--------|
| AF 2.0: 11 domains, 31 capabilities, 1:1 module mapping | MB-01; MB-02; EVOCON-01 | ✅ ENFORCED |
| AF SECTION-04: 13 information classes, single ownership | OWN-01 through OWN-06 | ✅ ENFORCED |
| AF 5.1: DAG dependency structure | DEP-01; DEP-12 | ✅ ENFORCED |
| AF 5.2: Three blocking gates | DEP-06; DEP-07; HAP-01 | ✅ ENFORCED |
| AF 5.3: No data circularity (DOM-06→DOM-11 secondary check) | DEP-10; DEP-01 | ✅ ENFORCED |
| AF 5.4: Six prohibited dependency classes | DEP-02 through DEP-07 | ✅ ENFORCED |
| AF 5.5: No hidden portfolio state | OWN-01; DEP-08 | ✅ ENFORCED |
| AF 6.1: Governance gates issuance only, never monitoring | GOV-01 | ✅ ENFORCED |
| AF 6.2: Per-state exit authority | GOV-04 | ✅ ENFORCED |
| AF 3.3 anti-leakage checks (all six) | DEP-02; OWN-04; OWN-05; OWN-01; DEP-05; DEP-07 | ✅ ENFORCED |

### 11.5 Validation Against ADR-000_ARCHITECTURE_PRINCIPLES

| Principle | Enforcement Rule | Result |
|-----------|-----------------|--------|
| P-01: Constitution Before Optimization | EVOCON-02; GOV-03 (governance over efficiency) | ✅ ENFORCED |
| P-02: Authority Before Automation | HAP-02; HAP-03 | ✅ ENFORCED |
| P-03: Human Approval Cannot Be Bypassed | HAP-01; DEP-07; EVOCON-02 | ✅ ENFORCED |
| P-04: Single Owner Per Information Class | OWN-01 through OWN-06; DEP-12 | ✅ ENFORCED |
| P-05: No Hidden Portfolio State | OWN-01; DEP-08 | ✅ ENFORCED |
| P-06: No Governance State Coupling | GOV-02; DEP-11; EVOCON-04 | ✅ ENFORCED |
| P-07: Audit Is Write-Only | OWN-04; DEP-03; AUD-01; AUD-02 | ✅ ENFORCED |
| P-08: Attribution Is Read-Only | DEP-02; OWN-03; HAP-03; EVOCON-05 | ✅ ENFORCED |
| P-09: Sentiment Is Advisory Only | VAL05-01 through VAL05-04; OWN-05; DEP-04; EVOCON-03 | ✅ ENFORCED |
| P-10: Dependencies Flow One Direction | DEP-01; DEP-12 | ✅ ENFORCED |
| P-11: Domain Boundaries Preserve Capability Boundaries | MB-01; MB-02; MB-03; MB-04 | ✅ ENFORCED |
| P-12: Architecture Must Remain Technology Neutral | Section 1.5 (no technology assumption); all rules are technology-neutral | ✅ ENFORCED |

### 11.6 Validation Against ADR-001_ARCHITECTURAL_STYLE_SELECTION

| ADR-001 Requirement | Enforcement Rule | Result |
|--------------------|-----------------|--------|
| Modular Monolith as core style | MB-01 through MB-04 | ✅ ENFORCED |
| Event pattern bounded to DOM-11 activation and DOM-06 governance signaling only | ACT-04 | ✅ ENFORCED |
| Risk 1 (boundary erosion): boundary enforcement is explicit, not implicit | DEP-12; RULE format: every prohibited dep is named | ✅ ADDRESSED |
| Risk 2 (event pattern scope creep): event scope is frozen | ACT-04; EVOCON-07 | ✅ ADDRESSED |
| Risk 3 (governance continuity under halt): monitoring functions protected | GOV-01 | ✅ ADDRESSED |

### 11.7 Validation Against ADR-002_CAPABILITY_TO_MODULE_REALIZATION

| ADR-002 Requirement | Enforcement Rule | Result |
|--------------------|-----------------|--------|
| Section 6.1: All permitted dependencies listed — unlisted = prohibited | DEP-12 | ✅ ENFORCED |
| Section 7: FORB-01 through FORB-10 | DEP-02 through DEP-11 (one rule per FORB) | ✅ ENFORCED |
| Section 4: 31 capability allocation frozen | MB-01; EVOCON-01 | ✅ ENFORCED |
| Section 5: 13 information class ownership frozen | OWN-01 through OWN-06; EVOCON-01 | ✅ ENFORCED |

### 11.8 Validation Against ADR-003_MODULE_INTERNAL_REALIZATION

| ADR-003 Requirement | Enforcement Rule | Result |
|--------------------|-----------------|--------|
| IAC-01 through IAC-13: Internal architecture constraints | Covered by ownership, dependency, and governance rules throughout | ✅ ENFORCED |
| IAC-07: Halt state independence within MOD-06 | DEP-11; GOV-02 | ✅ ENFORCED |
| IAC-08: MOD-06 detection continuous | GOV-01 | ✅ ENFORCED |
| IAC-09: Open Menu at MOD-07 | HAP-02 | ✅ ENFORCED |
| IAC-10: MOD-08 read-only | DEP-02; OWN-03 | ✅ ENFORCED |
| IAC-11: MOD-10 immutability | AUD-02 | ✅ ENFORCED |
| IAC-12: MOD-11 initiation only | ACT-01 | ✅ ENFORCED |

### 11.9 Validation Against ADR-003A and ADR-003B

| ADR-003A/B Clarification | Enforcement Rule | Result |
|--------------------------|-----------------|--------|
| OBS-01 (ADR-003B CHANGE_01): Exit domain governed by SDM-12; supplementary signals permitted at CAP-20 under SDM-12 | DEP-04 (explicitly permits CAP-20 with SDM-12 citation) | ✅ INCORPORATED |
| OBS-03 (ADR-003B CHANGE_02): Activation signal to MOD-06 is not a computational input | DEP-10 (explicitly covers CAP-19, CAP-23, CAP-31) | ✅ INCORPORATED |
| OBS-04 (ADR-003B CHANGE_03): MOD-01→MOD-08 and MOD-02→MOD-08 authorized | DEP-02 (explicitly permits these two edges) | ✅ INCORPORATED |

### 11.10 Overall Validation Verdict

All nine investigations have been executed. All enforcement rules are traceable to the constitutional corpus within the Constitution/ folder. No rule originates from assumption, technology preference, or implementation opinion.

**Validation result: COMPLETE.**

---

## SECTION 12 — ARCHITECTURE READINESS VERDICT

### 12.1 Completeness Evidence

**E1 — All Nine Required Investigations Completed:**

| Investigation | Section | Enforcement Rules Produced |
|-------------|---------|--------------------------|
| 01: Module Boundary Enforcement | Section 02 | MB-01, MB-02, MB-03, MB-04 |
| 02: Ownership Protection | Section 03 | OWN-01 through OWN-06 |
| 03: Dependency Enforcement | Section 04 | DEP-01 through DEP-12 |
| 04: Governance Enforcement | Section 05 | GOV-01, GOV-02, GOV-03, GOV-04 |
| 05: Human Authority Enforcement | Section 06 | HAP-01, HAP-02, HAP-03 |
| 06: VAL05 Enforcement | Section 07 | VAL05-01 through VAL05-04 |
| 07: Audit Enforcement | Section 08 | AUD-01, AUD-02, AUD-03 |
| 08: Activation Enforcement | Section 09 | ACT-01, ACT-02, ACT-03, ACT-04 |
| 09: Future Evolution Constraints | Section 10 | EVOCON-01 through EVOCON-10 |

**Total enforcement rules: 41 named rules across 9 investigation domains.**

**E2 — All FORB-01 through FORB-10 Explicitly Enforced:**

| Prohibition | Enforcement Rule |
|-------------|-----------------|
| FORB-01: MOD-08 write to MOD-01..06 | DEP-02 |
| FORB-02: MOD-10 outbound edge | DEP-03 |
| FORB-03: Supplementary signals → MOD-05 computation | DEP-04 |
| FORB-04: Any module → broker/execution venue | DEP-05 |
| FORB-05: Signal logic ← unverified data | DEP-06 |
| FORB-06: Any path around CAP-18 | DEP-07 |
| FORB-07: Private portfolio state derivative | DEP-08 |
| FORB-08: Conflict flag as numeric modifier | DEP-09 |
| FORB-09: MOD-11 activation events as data inputs | DEP-10 |
| FORB-10: Halt states sharing state across boundaries | DEP-11 |

**E3 — All 12 ADR-000 Principles Covered:** Validated in Section 11.5.

**E4 — All ADR-001 Risks Addressed:**
- Risk 1 (boundary erosion): DEP-12 establishes that all unlisted dependencies are prohibited; every boundary rule is named and explicit
- Risk 2 (event pattern scope creep): ACT-04 and EVOCON-07 freeze the event pattern scope
- Risk 3 (governance continuity): GOV-01 permanently enforces that no halt state suspends monitoring

**E5 — ADR-003A/B Clarifications Incorporated:** Validated in Section 11.9.

**E6 — No New Architecture Introduced:** ADR-004 creates no module, no capability, no information class, no dependency edge, and no authority class. Every rule derives from constitutional evidence. Every prohibition was already prohibited by the authority corpus — ADR-004 makes those prohibitions explicit as named enforcement rules.

**E7 — Technology Neutral:** Section 1.5 confirms that all enforcement rules are technology-neutral. No rule specifies an implementation mechanism. The rules prohibit behaviors; they do not prescribe the means of prohibition.

**E8 — Future Evolution Path Preserved:** ADR-001's verdict that microservices remain a valid future evolution path from a well-maintained modular monolith is preserved. ADR-004 imposes no constraints that would prevent service extraction from the modular monolith into distributed services, provided: each extracted service corresponds 1:1 to exactly one constitutional module (MB-02), module ownership contracts are maintained at service boundaries, and the three blocking gates remain synchronous and unconditional.

### 12.2 Architecture Readiness Verdict

**ADR-005 MAY PROCEED**

**Evidence:**

The constitutional enforcement model is complete. All boundaries are named. All prohibitions are explicit. All permitted behaviors are identified. All future evolution constraints are enumerated. The 41 enforcement rules cover all nine required investigation domains and address all ten ADR-002 FORB prohibitions, all 12 ADR-000 principles, all five ADR-001 architectural risks, and all ADR-003B clarifications.

No unresolved enforcement gaps have been identified. No new constitutional observations have arisen. The approved architecture is constitutionally protected against implementation drift by a named rule for every boundary class.

ADR-005 should address: the specific mechanisms by which the enforcement rules are verified in the implementation (architecture testing approaches, boundary checking methods, dependency verification methods) — none of which are specified by ADR-004, as those are implementation mechanism choices. ADR-005 may also address extension point design for the open validation items (EVOCON-08) and the SaaS evolution pathway (MB-02, SDM-CONST-12) if the owner determines that these require architectural specification beyond what the current enforcement model provides.

---

*ADR-004 derives its entire authority from the admissible constitutional corpus within the Constitution/ folder. It introduces no new architecture, no new capabilities, no new information classes, no new module structure, no new authority classes, and no technology selections. Its sole function is to make explicit — as named, traceable enforcement rules — the boundaries that the constitutional corpus already established. Every rule may be traced to a specific constitutional clause. No rule originates from implementation preference, engineering opinion, or optimization argument.*

*End of ADR-004_ARCHITECTURAL_BOUNDARY_ENFORCEMENT*

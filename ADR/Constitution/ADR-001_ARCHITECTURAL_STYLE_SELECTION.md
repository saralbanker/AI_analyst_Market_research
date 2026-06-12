# ADR-001 — ARCHITECTURAL STYLE SELECTION

**Decision:** Architectural Style Adjudication
**Method:** 4D+ Constitutional Analysis
**Authority Hierarchy:**
- Level 1: SDM_V2.3 (FROZEN — FINAL CANONICAL)
- Level 2: VAL05_OWNER_DECISION_RESOLUTION (RESOLVED)
- Level 3: SADR_V2.1 (CERTIFIED)
- Level 4: ARCHITECTURE_FOUNDATION_V1
- Level 5: ADR-000_ARCHITECTURE_PRINCIPLES (P-01 through P-12)

**Status:** CANDIDATE FOR OWNER REVIEW
**Scope:** Determines which architectural style satisfies the frozen authority corpus. Does not design modules, services, databases, APIs, or infrastructure.

---

## SECTION 01 — AUTHORITY-DERIVED ARCHITECTURAL REQUIREMENTS

### Derivation Method (Phase 1 — DECONSTRUCT)

Requirements are catalogued by category. Each requirement is traced to its authority source. These are not summaries — they are the raw architectural obligations the system must satisfy.

---

### 1.1 Ownership Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| OWN-01 | Each of the 13 information classes has exactly one owning domain; all other domains are read-only consumers | AF SECTION-04 |
| OWN-02 | DOM-09 is the single authoritative source of portfolio state; no consumer may maintain a private derivative | AF 5.5 |
| OWN-03 | Reports are composite views — ownership of each section never transfers at composition | AF 4.1 |
| OWN-04 | The four halt-state flags are owned exclusively by DOM-06; no other domain may hold authoritative halt state | AF SECTION-04 "Governance State" |
| OWN-05 | Audit records are owned exclusively by DOM-10; DOM-10 has no output edge to any capability | AF SECTION-04 "Audit Records"; AF 5.4 |
| OWN-06 | Attribution records (System Alpha, Human Override Delta) are owned by DOM-08; no system consumer may act on them without human approval | AF SECTION-04 "Attribution Records" |
| OWN-07 | Supplementary signals (news/sentiment) are owned by DOM-03; their only authorized consumer path beyond DOM-03's own CAP-09 is the human-facing advisory report | AF SECTION-04; GOV-VAL05 Rule 4 |

---

### 1.2 Dependency Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| DEP-01 | The internal information graph must be a DAG within any single recommendation cycle | AF 5.3 |
| DEP-02 | CAP-02 is a hard blocking gate — no signal logic may execute on unverified data | SADR Section 5; AF 5.2 |
| DEP-03 | CAP-10 is a hard blocking gate — confidence scoring may not execute on unvalidated signals | SADR Section 5; AF 5.2 |
| DEP-04 | CAP-18 is a hard blocking gate — no trade action may occur without human approval, no exceptions, no bypass | SADR Section 5; AF 5.2; SDM-CONST-06 |
| DEP-05 | DOM-03 supplementary signals must not reach DOM-05 computation — a prohibited dependency edge | AF 5.4; GOV-VAL05 Rule 1 |
| DEP-06 | DOM-08 must have no write edge to DOM-01 through DOM-06 | AF 5.4; CONSTRAINT-07 |
| DEP-07 | DOM-10 must have no outbound edge to any capability | AF 5.4; CAP-30 Boundary |
| DEP-08 | No domain may connect to the broker/execution venue in any direction | AF 5.4; GOV-01 Rule 1; GOV-02 Rules 4–5 |
| DEP-09 | All dependencies must be directional and enumerable per the AF 5.1 domain map | AF 5.1 |
| DEP-10 | Governance events (DOM-06) may trigger event-driven activation (DOM-11 Mode 3) — this is initiation, not data dependency | AF 5.3 secondary check; AF 5.1 |

---

### 1.3 Governance Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| GOV-R01 | The four halt states must be constitutionally independent — distinct triggers, effects, exits; may be simultaneously active | SDM-CONST-14; AF DOM-06 independence constraint |
| GOV-R02 | Halt states gate recommendation issuance only — monitoring, audit, reporting, and governance detection must continue during any active halt state | AF 6.1; GOV-01 Rule 4; GOV-02 Rule 3; SDM-15 Rule 14 |
| GOV-R03 | Governance compliance monitoring (CAP-31) must operate continuously — not only at approval gate events | SADR CAP-31 constitutional constraints |
| GOV-R04 | Governance Lockout exit is automatic on CAP-31 detecting restoration — no additional human authorization required beyond the corrective action | GOV-02 Rule 3; SADR CAP-26 |
| GOV-R05 | Governance Halt exit requires explicit human resumption authorization | GOV-01 Rule 5; SADR CAP-25 |
| GOV-R06 | Conditional Suspension exit is condition-driven and automatic when CAP-23 detects clearance | SDM-15 Rule 14; SADR CAP-27 |
| GOV-R07 | Hard Deterministic Halt exit requires human acknowledgment plus confirmed return within limits | SDM-CONST-14 State 4; SADR CAP-24 |
| GOV-R08 | Governance enforcement holds zero execution authority; it gates recommendations only | SDM-CONST-14; GOV-01 Rule 1 |

---

### 1.4 Audit Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| AUD-01 | Every SDM decision domain (SDM-02 through SDM-15) has an explicit Audit clause — all must be discharged | SADR CAP-30 Necessity |
| AUD-02 | The original system recommendation versus final human action must be immutably recorded | SDM-10 Audit |
| AUD-03 | Halt state entry and exit with condition state must be logged | SDM-15 Rule 14 |
| AUD-04 | All human approvals, rejections, and overrides must be logged | SDM-15 Audit |
| AUD-05 | Audit is write-only from the system's perspective; no capability reads from audit at runtime | ADR-000 P-07; AF 5.4 |
| AUD-06 | Audit records are immutable — not merely append-only, but structurally immutable | SADR CHANGE-06; CAP-30 Outputs |

---

### 1.5 Traceability Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| TRC-01 | Every capability must have a traceable authority class (AUTONOMOUS_RESEARCH, SHARED_AUTHORITY, or HUMAN_APPROVAL) | SADR Section 6 |
| TRC-02 | Every capability must have a traceable constitutional source (SDM clause or GOV rule) | SADR Section 12 |
| TRC-03 | Domain boundaries must be derivable from three evidence tests — any future architectural change must maintain this derivability | AF 2.0 |
| TRC-04 | Any behavior change motivated by attribution must be traceable to explicit human approval | SDM-13 Rule 9; ADR-000 P-08 |
| TRC-05 | Open validation items (VAL-01 through VAL-17, minus closed items) must remain as extension points — no architectural decision may prematurely close them | SADR Section 11 CLASS_B/C/D; SDM-CONST-12 |

---

### 1.6 Information Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| INF-01 | Technical signals are the primary evidence layer; supplementary signals are advisory only | SDM-CONST-10; GOV-VAL05 |
| INF-02 | Confidence scores derive exclusively from technical evidence and statistical validation | GOV-VAL05 Rule 1; SADR_AMENDMENT_VAL-05 CAP-12 |
| INF-03 | Conflict flags from CAP-09 annotate confidence scores; they do not modify them | SADR_AMENDMENT_VAL-05; AF DOM-03 GOV-VAL05 Boundary |
| INF-04 | Portfolio state is sourced exclusively from human-confirmed, externally executed trade actions | SADR CAP-29 Inputs; AF DOM-09 |
| INF-05 | Data must be cross-verified from at least two independent sources before signal logic may consume it | SDM-02 Rule 2; SDM-05 Rule 1; CAP-02 |
| INF-06 | Historical datasets must include delisted equities to prevent survivorship bias | SDM-02 Rule 1; SDM-07 Rule 4 |
| INF-07 | All EV-filtered opportunities must be presented simultaneously as Open Menu | SDM-08 Rule 8; CONSTRAINT-09 |
| INF-08 | Walk-forward cross-validation is mandatory; K-fold is constitutionally prohibited | CONSTRAINT-08 |

---

### 1.7 Modularity and Evolvability Requirements

| Req ID | Requirement | Authority |
|--------|-------------|-----------|
| MOD-01 | Components must be replaceable, configurable, versioned, and independently evolvable | SDM-CONST-12 |
| MOD-02 | Future SaaS expansion must remain possible without complete redesign | SDM-CONST-12 |
| MOD-03 | The architectural style must remain valid if all technology choices change | ADR-000 P-12 |
| MOD-04 | Open validation items must be satisfiable as extension points — the style must accommodate future calibration without structural revision | SADR Section 11; SDM-CONST-12 |
| MOD-05 | SDM-14 (Research Intake) is constitutionally deferred — no architectural anticipation is permitted | SADR Section 10 |

---

## SECTION 02 — EVALUATION METHODOLOGY

### 2.1 Required Architectural Characteristics

From the requirements above, the following architectural characteristics are derived. These are properties the selected style must exhibit or enable. They are not style features — they are constitutional obligations expressed as structural properties.

| Char ID | Characteristic | Derived From |
|---------|----------------|--------------|
| CHAR-01 | **Explicit, enforceable information ownership** — each information class must have a single authoritative producer; the architecture must prevent unauthorized writes | OWN-01 through OWN-07 |
| CHAR-02 | **Directional, acyclic information flow** — the dependency graph must be a DAG; no information class may feed back to its own producer within a cycle | DEP-01, DEP-09, DEP-10 |
| CHAR-03 | **Hard blocking gate enforcement** — three specific checkpoints (data verification, signal validation, human approval) must function as unconditional flow blockers | DEP-02, DEP-03, DEP-04 |
| CHAR-04 | **Isolated governance domains** — governance state must be owned and maintained by a distinct domain that neither receives instructions from nor delegates authority to recommendation logic | GOV-R01 through GOV-R08; OWN-04 |
| CHAR-05 | **Governance continuity under halt** — monitoring, detection, audit, and reporting must remain active during any halt state; only recommendation issuance is gated | GOV-R02, GOV-R03 |
| CHAR-06 | **Immutable, terminal audit** — audit receives from all, writes to none, and cannot be read back by any system capability | AUD-01 through AUD-06 |
| CHAR-07 | **Read-only attribution** — the attribution domain must have no write path to any recommendation or governance logic | TRC-04; OWN-06 |
| CHAR-08 | **Prohibited edge enforcement** — six specific dependency prohibitions (AF 5.4) must be structurally unroutable, not merely policy-controlled | DEP-05 through DEP-08 |
| CHAR-09 | **Authority class preservation** — the three authority classes (AUTONOMOUS_RESEARCH, SHARED_AUTHORITY, HUMAN_APPROVAL) must be structurally distinguishable | TRC-01 |
| CHAR-10 | **Technology neutrality** — the style must make no claim that depends on a specific implementation technology | MOD-03; ADR-000 P-12 |
| CHAR-11 | **Independent evolvability of domains** — each of the 11 constitutional domains must be independently modifiable without requiring cascade changes in other domains | MOD-01, MOD-02; ADR-000 P-11 |
| CHAR-12 | **Single-point advisory presentation** — the Open Menu constraint requires that all ranked opportunities reach the human simultaneously, not via sequential delivery | INF-07; CHAR-03 |

---

### 2.2 Evaluation Approach

Each of the six candidate styles is first subjected to constitutional attack — the evaluator actively attempts to find conditions under which the style conflicts with authority. A style that produces irresolvable conflicts with any authority level is eliminated. A style that produces tensions requiring compensating architectural decisions is marked with warnings. A style that survives all attacks is retained for comparative assessment.

The evaluation is not a feature matrix. A style with fewer "strengths" may be constitutionally superior if those strengths directly address the highest-priority requirements. Popularity, ecosystem maturity, and implementation convenience are irrelevant.

---

## SECTION 03 — CANDIDATE ANALYSIS

---

### Candidate A — Modular Monolith

A single deployable unit whose internal structure is organized into well-defined modules with explicit boundaries, dependency rules, and ownership controls enforced at the code/compilation level rather than at a network or process boundary.

#### Constitutional Strengths

**A-S1: Ownership enforcement by construction.** In a modular monolith, module boundaries are enforced at the language/compilation level. The single-owner-per-information-class requirement (CHAR-01, ADR-000 P-04) is structurally expressible: a module owns its types; other modules receive outputs, not internals.

**A-S2: Dependency direction enforced by module graph.** Cyclic module dependencies are detectable and preventable at build time. The DAG requirement (CHAR-02, ADR-000 P-10) is verifiable without runtime inspection.

**A-S3: Hard blocking gates are natural sequential flows.** The three blocking gates (CAP-02, CAP-10, CAP-18) map naturally to mandatory function calls within a single execution context. There is no asynchronous routing that could bypass them.

**A-S4: Governance isolation by module boundary.** DOM-06's independence — governing recommendation issuance without being part of the recommendation pipeline — is naturally expressible as a separate module with defined input and output contracts.

**A-S5: Audit as a terminal sink.** A dedicated audit module with write-only interfaces is straightforwardly implemented: all modules may call audit.write(); no module calls audit.read() in operational code.

**A-S6: Technology neutrality.** The modular monolith style makes no claim about a specific technology, database, or platform. Any language, runtime, or persistence mechanism is compatible.

**A-S7: SDM-CONST-12 modularity.** "Modular LEGO-style approach. Components shall be replaceable, configurable, versioned, and independently evolvable." The modular monolith's internal module structure is the direct architectural expression of this constitutional mandate.

#### Constitutional Weaknesses

**A-W1: Boundary enforcement depends on discipline.** Unlike network-separated services, module boundaries in a monolith can be violated without architectural intervention — only tooling (linters, dependency checkers, architecture tests) enforces them. The prohibited dependency edges (CHAR-08) are policy-enforced, not physically impossible.

**A-W2: Governance continuity under halt may require careful design.** If recommendation generation and governance monitoring share a single execution thread, halting recommendation issuance while continuing governance monitoring requires explicit design. In a naïve single-threaded monolith, a halt might stop all processing. This is a design challenge, not an irresolvable conflict — the constitution requires continuity (CHAR-05) and the monolith can provide it, but the design must be explicit.

**A-W3: Optional SaaS expansion may require structural decomposition.** SDM-CONST-12 requires SaaS expansion to be possible without complete redesign. A well-structured modular monolith can be decomposed into distributed services when the time comes — but only if the module boundaries are maintained with sufficient discipline throughout development. This is a risk, not a disqualifier.

#### SDM Fit: Strong
SDM-CONST-12 explicitly describes a "modular LEGO-style approach" — the modular monolith is the direct structural expression of this language. Human approval gate (SDM-CONST-06) is straightforwardly enforced as a required function invocation. Halt states (SDM-CONST-14) map to distinct modules with independent state.

#### VAL05 Fit: Strong
The prohibited dependency edge (DOM-03 supplementary signals → DOM-05 computation) is enforced by module boundary — the computation modules do not import from the supplementary signal module for computational inputs. Advisory routing to the presentation layer is an explicit module-level design constraint.

#### SADR Fit: Strong
All 31 capabilities are assignable to modules with explicit boundaries. The three authority classes remain distinguishable at the module level. The three blocking gates are enforceable as sequential function call requirements.

#### Architecture Foundation Fit: Strong
The 11 constitutional domains map cleanly to module groups. The 13 information class ownership rules are expressible as module-level ownership. The six prohibited dependencies are enforceable as module-level import rules.

#### ADR-000 Fit: Strong
P-04 (single owner), P-05 (no hidden portfolio state), P-07 (audit terminal), P-08 (attribution read-only), P-09 (sentiment advisory), P-10 (DAG dependencies), P-11 (domain boundaries), P-12 (technology neutral) — all are naturally enforceable at module-boundary level.

---

### Candidate B — Microservices

A distributed architecture in which each service is an independently deployable unit operating as a separate process, communicating via network interfaces (APIs, messaging), with its own deployment lifecycle and often its own storage.

#### Constitutional Strengths

**B-S1: Physical service boundary enforces ownership.** A microservice that owns an information class physically cannot be written to by another service without crossing a network boundary — making unauthorized writes detectable.

**B-S2: Independent deployment aligns with SDM-CONST-12.** Services can be individually upgraded or replaced without coordinated deployment.

**B-S3: Authority class separation is physical.** CAP-18 (HUMAN_APPROVAL) can be deployed as a distinct service with no shared runtime with autonomous capabilities.

#### Constitutional Weaknesses

**B-W1: Network dependency paths are harder to restrict than module-level paths.** The six prohibited dependency edges (CHAR-08, AF 5.4) become network routing restrictions. A service that "should not" receive data from another service may still do so through indirect paths (shared storage, event subscriptions, API calls). Enforcing the DOM-03 → DOM-05 prohibition and the DOM-08 → DOM-01..06 prohibition requires governance of network connectivity, not merely module boundaries.

**B-W2: Hard blocking gates become distributed transactions.** The three constitutional blocking gates (CAP-02, CAP-10, CAP-18) require that downstream services do not receive data until upstream verification passes. In a distributed system, this becomes a coordination problem — partial failures, timeouts, and retry logic can create windows where the gate is nominally enforced but practically bypassed. The CAP-18 gate in particular — "no exceptions, no bypass" — carries zero tolerance for partial enforcement.

**B-W3: Governance continuity is more complex.** CHAR-05 requires that governance monitoring (CAP-31, CAP-23, CAP-29) continues during halt states. In a microservices architecture with per-service health management, a halt state must not cause the governance monitoring services to also suspend. This requires careful service dependency design that adds complexity relative to what the constitution requires.

**B-W4: DAG enforcement becomes a network-topology problem.** In a modular monolith, cyclic dependencies are detectable at build time. In microservices, they manifest as runtime call cycles that can be difficult to detect and prevent. The AF 5.3 acyclicity requirement becomes an operational constraint rather than a compile-time constraint.

**B-W5: Technology assumptions are embedded in the style.** Microservices imply network communication protocols, service discovery, API contracts, and often messaging infrastructure. ADR-000 P-12 prohibits technology-specific architectural claims. The microservices style, as a style, does not mandate specific technologies — but its characteristic patterns (API-based communication, independent deployment pipelines, service mesh) carry implementation assumptions that risk bleeding into the architecture layer.

**B-W6: Current scale does not justify complexity cost.** SDM-CONST-04 defines the current system as a personal tool at ₹5,000 capital. The complexity overhead of microservices — network partition handling, distributed tracing, service coordination — is not justified by constitutional requirements. SDM-CONST-12 requires future SaaS expansion to be possible, not that it be pre-built. Microservices would pre-implement SaaS-scale concerns for a personal tool, producing structural complexity without constitutional benefit.

#### SDM Fit: Moderate
The system identity and governance rules are satisfiable in microservices, but the distributed nature introduces complexity not required by the constitution.

#### VAL05 Fit: Moderate
The prohibited dependency edge is expressible as a network routing rule, but enforcement is less certain than module-level prohibition.

#### SADR Fit: Weak-to-Moderate
The three blocking gates become distributed coordination problems. The CONSTRAINT-01 prohibition on trade execution is structurally satisfiable, but the zero-tolerance language ("no exceptions, no bypass") is harder to guarantee across network boundaries.

#### Architecture Foundation Fit: Moderate
Domain ownership is physically enforceable, but the prohibited dependencies require network-level governance controls rather than compile-time enforcement.

#### ADR-000 Fit: Moderate
P-03 (bypass prohibition) and P-06 (governance independence) are satisfiable but require additional compensating design relative to a monolith. P-12 (technology neutrality) is in tension with the style's characteristic network communication patterns.

---

### Candidate C — Event-Driven Architecture

A style in which components communicate primarily through the production and consumption of events, often via a message bus or event stream. Components are decoupled from each other; each responds to events it subscribes to.

#### Constitutional Strengths

**C-S1: Temporal decoupling aligns with three activation modes.** DOM-11's three activation modes (scheduled, on-demand, event-driven) map naturally to event publishing and subscription patterns.

**C-S2: Audit as an event consumer.** DOM-10's terminal-sink property — receiving from all, writing to none — maps naturally to an audit consumer that subscribes to all events but publishes none.

**C-S3: Governance events as first-class triggers.** DOM-06 → DOM-11 (governance events triggering Mode 3 activation) is naturally expressed as governance domains publishing events that DOM-11 consumes.

#### Constitutional Weaknesses

**C-W1: Event subscriptions can create invisible dependency violations.** The most critical constitutional requirement is the enforcement of six prohibited dependency edges (AF 5.4). In a pure event-driven architecture, any component may potentially subscribe to any event — the DOM-03 supplementary signal event could be subscribed to by DOM-05 components without a structural prohibition. Preventing unauthorized subscriptions requires governance of the event bus topology, which is operationally fragile relative to a compile-time enforcement mechanism.

**C-W2: Hard blocking gates are structurally at odds with event-driven patterns.** Event-driven architectures typically implement eventual consistency and asynchronous processing — patterns that are in fundamental tension with the three constitutional hard blocking gates. DEP-02 (CAP-02 blocks all signal logic), DEP-03 (CAP-10 blocks confidence scoring), and DEP-04 (CAP-18 blocks all trade action) require synchronous, unconditional blocking. If an event consumer begins processing a signal before cross-verification completes — because it received the signal event and the verification result hasn't arrived yet — the blocking gate is violated even if the final result would have been correct.

**C-W3: Causal ordering guarantees are required but complex.** The dependency chain from CAP-01 through CAP-18 represents a strict causal ordering requirement: no capability may receive information until all prerequisites have completed. Event-driven architectures do not natively guarantee causal ordering without explicit sequencing mechanisms — which adds implementation complexity that is not constitutionally required.

**C-W4: DAG enforcement becomes an event-subscription topology problem.** The acyclicity requirement (DEP-01, CHAR-02) must be enforced as a property of event subscription topology. In a pure event-driven system, components that emit and consume events from the same namespace can inadvertently create feedback loops — exactly what the constitution prohibits.

**C-W5: Attribution read-only constraint is harder to enforce.** DOM-08's prohibition on writing to DOM-01 through DOM-06 (CHAR-07) requires that DOM-08 may not publish events that DOM-01..06 subscribe to. This is enforceable but requires explicit event topology governance.

**C-W6: Governance continuity requires careful event design.** CHAR-05 requires monitoring and governance functions to continue during halt states. In an event-driven system where a halt state "stops" the recommendation pipeline, the governance domain must continue consuming its own events without interruption — requiring careful partitioning of event streams by domain.

**C-W7: Single information ownership is difficult to enforce.** When information is propagated as events on a bus, any domain could in principle maintain its own copy of any event payload — creating private state derivatives in violation of P-05 (No Hidden Portfolio State). Preventing this requires event topology governance, not merely structural prohibition.

#### SDM Fit: Moderate
Activation modes map well. Hard blocking gates and governance isolation map poorly to pure event-driven patterns.

#### VAL05 Fit: Weak
The clean separation of supplementary signals from computation is architecturally harder to enforce when both are event consumers on a shared bus.

#### SADR Fit: Weak
The three constitutional blocking gates are fundamentally at odds with the asynchronous, eventually-consistent nature of pure event-driven architectures.

#### Architecture Foundation Fit: Weak
The six prohibited dependency edges are much harder to enforce as subscription restrictions than as module-level import rules.

#### ADR-000 Fit: Weak-to-Moderate
P-03 (hard bypass prohibition), P-04 (single ownership), P-05 (no hidden state), and P-08 (attribution read-only) all face structural challenges in a pure event-driven architecture.

---

### Candidate D — Agent-Centric Architecture

A style in which autonomous agents perceive their environment, maintain internal state, and take actions toward objectives — often with dynamic orchestration, emergent behavior from agent interaction, and goal-directed reasoning.

#### Constitutional Strengths

**D-S1: Conceptual alignment with AI research functions.** The system's identity (AI Swing Trading Research Analyst) involves AI-driven analysis, which agent-centric architectures are designed to support.

**D-S2: Flexible activation.** Agent-centric systems can implement all three activation modes naturally.

#### Constitutional Weaknesses

**D-W1: Emergent behavior is constitutionally prohibited.** The SDM's constitutional invariants are deterministic by design. Every halt state has defined entry, effect, and exit conditions. The confidence scoring computation must be deterministic (SDM-15 Rule 3: "Execution logic must remain strictly deterministic"). Agent-centric architectures derive value from emergent, adaptive behavior — the exact property that the SDM's determinism requirements prohibit in governance and recommendation logic.

**D-W2: Goal-directed reasoning in agents conflicts with constitutional constraints.** An agent that pursues an objective may find pathways to that objective that were not constitutionally authorized. SDM-CONST-06 prohibits autonomous execution "without exception." An agent optimizing a research objective could, by goal-directed reasoning, determine that a particular API call or portfolio action advances its objective — and the agent-centric style does not structurally prevent this. The prohibition requires that no system component hold the architectural capacity for this reasoning.

**D-W3: Authority class assignment is incompatible with agent autonomy.** SADR's three authority classes (AUTONOMOUS_RESEARCH, SHARED_AUTHORITY, HUMAN_APPROVAL) require explicit, traceable authority boundaries. Agent-centric architectures typically feature dynamic authority allocation — agents negotiate tasks, delegate sub-goals, and coordinate without fixed authority hierarchies. This directly conflicts with TRC-01.

**D-W4: Single information ownership is structurally violated by agent state.** Agents maintain internal state by design. Any agent that internally caches portfolio state, governance state, or recommendation state creates private state derivatives — violating P-04 (Single Owner) and P-05 (No Hidden Portfolio State).

**D-W5: Hard blocking gates are architecturally foreign to agent patterns.** Agents are designed to proceed toward objectives when possible, working around obstacles. A constitutional hard blocking gate ("no exceptions, no bypass") is the architectural opposite of this design philosophy. An agent-centric architecture would require imposing non-agent, sequential blocking logic on top of an agent framework — making the agent properties a liability rather than an asset.

**D-W6: Attribution-writes-nothing rule is difficult to enforce.** In an agent system where agents observe outcomes and update their internal models, the boundary between "observing" (constitutionally permitted) and "learning/updating" (requiring explicit human approval per SDM-13 Rule 9) becomes structurally ambiguous.

**D-W7: Governance independence is at odds with dynamic orchestration.** The four halt states must be constitutionally independent and cannot be merged (ADR-000 P-06). Dynamic agent orchestration may produce emergent coordination between halt-related agents — violating the independence constraint.

#### SDM Fit: Very Weak
The determinism requirements (SDM-15 Rule 3), the prohibition on autonomous execution (SDM-CONST-06), and the fixed authority structure are directly incompatible with core agent-centric design properties.

#### VAL05 Fit: Very Weak
The advisory-only sentiment boundary requires that AI evaluation outputs stay in the semantic domain. An agent-centric system where AI agents directly influence recommendation computation would routinely cross this boundary.

#### SADR Fit: Very Weak
CONSTRAINT-01 (no trade execution), CONSTRAINT-07 (attribution read-only), and the three authority classes are all in fundamental tension with agent autonomy.

#### Architecture Foundation Fit: Very Weak
The single-owner-per-information-class model and the prohibited dependency edges are structurally incompatible with agent state management.

#### ADR-000 Fit: Very Weak
P-01 (constitution before optimization), P-02 (authority before automation), P-03 (bypass prohibition), P-04 (single owner), P-06 (governance independence), P-08 (attribution read-only) all face irresolvable structural conflicts.

---

### Candidate E — Layered Architecture

A style in which the system is organized into horizontal layers (e.g., presentation, application, domain, infrastructure), with dependencies permitted only downward — each layer may call the layer below it but not the layer above.

#### Constitutional Strengths

**E-S1: Directional dependencies.** Layered architecture enforces downward-only dependencies — aligning with the DAG requirement (CHAR-02, DEP-01).

**E-S2: Simple and well-understood boundary enforcement.** Layer rules are straightforward to audit: does a component in layer N call a component in layer N+2? If so, it is a violation.

**E-S3: Technology neutral.** The layered style makes no claim about specific technologies.

#### Constitutional Weaknesses

**E-W1: Domain ownership does not map to horizontal layers.** The constitutional information ownership model is organized by domain — 11 domains, each owning specific information classes. Horizontal layers cut across domains. DOM-01 (Market Data) and DOM-06 (Risk & Governance) would both appear in the "domain" layer — but they have entirely different authority classes, ownership contracts, and dependency rules. A layered architecture cannot express the authority cohesion requirement (AF 2.0 test 3) because it organizes by abstraction level, not by constitutional domain.

**E-W2: The four halt states have no natural layer placement.** Governance halt states gate recommendation issuance (DOM-05) but must not halt monitoring (DOM-01 through DOM-04) or audit (DOM-10). In a horizontal layer model, the governance layer would be positioned above or below the domain layer — but governance both depends on domain data (from DOM-09 for portfolio state) and controls domain outputs (gating DOM-05). This bidirectional relationship violates layered dependencies.

**E-W3: Attribution and audit have no natural layer.** DOM-08 (Attribution) receives from DOM-07 (post-gate) and writes only to human review and audit. DOM-10 (Audit) receives from all. Neither fits naturally into a horizontal layer without cross-layer dependencies.

**E-W4: The three blocking gates span multiple "layers."** CAP-02 gates data before signal generation. CAP-10 gates signal validation before confidence. CAP-18 gates human approval before any trade action. These are domain-specific gates, not layer-to-layer gates — a layered architecture cannot express them as first-class architectural features.

**E-W5: The simultaneous-presentation Open Menu constraint has no layer analog.** INF-07 and CHAR-12 require that all ranked opportunities are simultaneously presented to the human. A layered architecture has no natural mechanism for expressing this as an architectural constraint — it would be an application-level concern invisible at the style level.

#### SDM Fit: Weak
The domain organization of the SDM does not map to horizontal abstraction layers. Key constitutional concepts (halt states, authority classes, blocking gates) have no natural expression in a purely layered style.

#### VAL05 Fit: Moderate
The prohibited dependency from supplementary signals to computation could be expressed as a layer rule, but the advisory routing to the presentation layer is awkward in a strict downward-dependency model.

#### SADR Fit: Weak
The three authority classes and the three blocking gates do not map naturally to layers. CONSTRAINT-09 (Open Menu) has no layer-level expression.

#### Architecture Foundation Fit: Weak
The 11 constitutional domains and their specific authority assignments cannot be expressed in a horizontal layer model without losing constitutional precision.

#### ADR-000 Fit: Weak
P-04, P-05, P-06, P-09, P-11 all require domain-centric organization that the layered style cannot provide. P-10 (DAG dependencies) is satisfiable but more restrictively expressed than the constitution requires.

---

### Candidate F — Hybrid Architecture

A deliberate combination of two or more styles, where each style is applied to the portion of the system for which it provides the strongest constitutional fit, and the combination is governed by explicit inter-style boundary rules.

#### Constitutional Strengths

**F-S1: Constitutional precision over stylistic purity.** The constitution defines 11 domains with three different authority classes, distinct dependency patterns, and specialized governance requirements. No single pure style satisfies all these requirements with equal precision. A hybrid allows the strongest-fitting style to govern each domain category.

**F-S2: Modular Monolith as the core satisfies the primary constitutional requirements.** The modular monolith style satisfies CHAR-01 through CHAR-12 with strong direct evidence. Its weaknesses (A-W1, A-W2, A-W3) are addressable through supplementary style components, not through abandoning the core style.

**F-S3: Event-driven patterns for activation and governance triggers.** DEP-10 explicitly describes DOM-06 → DOM-11 as an event initiation relationship, not a data dependency. DOM-11's three activation modes include an event-driven mode. A limited, constitutionally-scoped event pattern for activation and governance-event signaling addresses this without imposing event-driven architecture on the recommendation pipeline.

**F-S4: The hybrid is bounded by constitutional authority, not by style preference.** The hybrid is not arbitrary eclecticism — it is derived from the requirement that each constitutional domain receive the style treatment most suited to its specific authority class and dependency pattern. The boundaries between hybrid components are themselves constitutionally derived.

#### Constitutional Weaknesses

**F-W1: Inter-style boundaries require explicit constitutional justification.** A hybrid carries the risk of using "hybrid" as justification for arbitrary style mixing. This risk is mitigated if every inter-style boundary is traced to a specific constitutional requirement — not to convenience or preference.

**F-W2: Boundary consistency must be maintained across style components.** If the modular core and the event-triggered activation use different ownership models for shared information, the P-04 (single owner) requirement could be violated at the style boundary. This requires explicit boundary design.

---

## SECTION 04 — CANDIDATE ELIMINATION ANALYSIS

### Candidate D — Agent-Centric Architecture: ELIMINATED

**Elimination verdict: Irresolvable constitutional conflicts.**

The agent-centric style's core design properties — emergent behavior, goal-directed reasoning, dynamic authority allocation, agent-internal state management — directly conflict with the SDM's determinism requirements (SDM-15 Rule 3), the prohibition on autonomous execution (SDM-CONST-06), the fixed three-class authority model (SADR Section 6), and the single-owner-per-information-class requirement (P-04). These are not tension points addressable by supplementary design — they are fundamental incompatibilities between the style's defining properties and the constitution's defining requirements. No compensating design can make an agent architecture constitutionally compliant without removing the properties that define it as an agent architecture.

**D is eliminated from further consideration.**

---

### Candidate C — Pure Event-Driven Architecture: ELIMINATED

**Elimination verdict: Irresolvable conflict with constitutional blocking gates.**

The three constitutional blocking gates (DEP-02, DEP-03, DEP-04) require synchronous, unconditional, zero-tolerance blocking. Pure event-driven architectures are fundamentally built on asynchronous, eventually-consistent processing — the opposite of what the blocking gates require. The CAP-18 gate language ("no exceptions, no bypass") cannot be structurally guaranteed in a pure event-driven system without imposing synchronous blocking mechanisms that override the style's defining properties. Additionally, the six prohibited dependency edges (CHAR-08) are much harder to enforce as subscription restrictions than as module-level import rules — event bus topologies are operationally governed rather than structurally enforced.

**Note:** Event-driven patterns remain constitutionally applicable in a bounded, scoped context — specifically for DOM-11 activation mode triggers and DOM-06 governance event signaling. This is addressed in the Hybrid analysis.

**C as a pure architectural style is eliminated. Event-driven patterns remain viable as a bounded component of a hybrid.**

---

### Candidate E — Layered Architecture: ELIMINATED

**Elimination verdict: Cannot express the constitutional domain model.**

The layered architecture organizes by abstraction level (horizontal layers). The constitutional model is organized by domain ownership, authority class, and information class. These organizational principles are orthogonal — domain-centric organization cannot be expressed as horizontal layers without losing the precision required by AF 2.0, SADR Section 6, and ADR-000 P-11. The four halt states, the three authority classes, and the three blocking gates have no natural expression in a layered style. The authority cohesion test (AF 2.0 test 3) — which forbids merging authority-distinct capabilities into the same domain — cannot be expressed as a layer rule.

**E is eliminated from further consideration.**

---

### Candidate B — Microservices: CONDITIONALLY ELIMINATED

**Conditional elimination verdict: Not disqualified on constitutional grounds, but unjustified by constitutional requirements at current scale.**

Microservices can satisfy all constitutional requirements — the ownership, dependency, governance, and audit rules are all expressible in a microservices architecture. However, the microservices style introduces distributed systems complexity (network partition handling, causal ordering guarantees, distributed tracing, service coordination) that the constitution does not require. ADR-000 P-01 (Constitution Before Optimization) applies inversely here: the constitution does not require pre-emptive SaaS-scale infrastructure. SDM-CONST-12 requires future SaaS expansion to be *possible* without complete redesign — not that it be pre-implemented. The modular monolith satisfies this requirement through its module boundaries, which enable later extraction into services. The microservices style's hard blocking gate challenge (B-W2) — where the zero-tolerance bypass prohibition becomes a distributed coordination problem — is a real constitutional risk that a modular monolith does not carry.

**B is conditionally eliminated: not constitutionally disqualified, but unjustified at current constitutional scale. It remains a valid future evolution path from a well-structured modular monolith.**

---

### Candidates A and F — Surviving Candidates

Candidate A (Modular Monolith) and Candidate F (Hybrid Architecture with Modular Monolith as the core) both survive constitutional attack. The key question for comparative assessment is whether the hybrid's additions are constitutionally justified or constitutionally neutral additions.

---

## SECTION 05 — COMPARATIVE ANALYSIS

| Dimension | A: Modular Monolith | F: Hybrid (Modular Monolith + Bounded Event Patterns) |
|-----------|--------------------|---------------------------------------------------------|
| **Ownership enforcement** | Module-level, compile-time | Same core; event pattern boundary requires explicit ownership rules at inter-style boundary |
| **Dependency enforcement** | Compile-time module graph | Same core; event subscriptions require topology governance |
| **Hard blocking gate fidelity** | High — synchronous by default | Same core; event patterns scoped away from blocking gates |
| **Governance isolation** | Module boundary | Same; governance events are a constitutionally natural addition |
| **Governance continuity under halt** | Design challenge; addressable | Same; event-based governance signals may improve continuity |
| **Audit terminal sink** | Straightforward module-level | Same |
| **Attribution read-only** | Module boundary, no write imports | Same |
| **Sentiment advisory enforcement** | Module-level import restriction | Same core |
| **Activation mode support** | All three supported | All three supported; event-driven mode is explicitly natural |
| **DOM-06 → DOM-11 governance events** | Supported; implementation varies | Constitutionally natural expression via bounded event pattern |
| **Technology neutrality** | Full | Full |
| **SaaS evolvability** | Supported through modular boundaries | Same |
| **Constitutional justification for complexity** | Fully justified | Partially justified; bounded event pattern is constitutionally grounded in DEP-10 and DOM-11 |
| **Risk of style boundary violations** | Lower | Higher; requires explicit boundary governance |

### Key Finding

The core distinction between Candidate A and Candidate F is whether the bounded event-driven pattern for governance signaling and activation is constitutionally required or merely constitutionally permitted.

**Evidence for constitutional grounding of bounded event patterns:**
- AF 5.1 explicitly distinguishes DOM-06 → DOM-11 as a governance-event-to-activation-initiation relationship, not a data dependency
- AF 5.3 confirms this is not a data circularity
- SDM-CONST-15 Mode 3 (Event-Driven Activation) is a constitutionally authorized activation mode by name
- AF DOM-11: "Initiate research/analysis/monitoring/attribution/reporting/governance cycles under the three constitutionally authorized modes"
- SADR Section 8: "Mode 3 — Event-Driven: Initiation when governance, risk, or portfolio events trigger mandatory review."

The constitution does not merely permit event-driven activation — it names it as one of three constitutionally authorized modes. The activation domain (DOM-11) and governance domain (DOM-06) have a relationship that the constitution explicitly characterizes as event-based (governance events trigger mandatory review cycles). A Hybrid that formalizes this constitutionally characterized relationship is not arbitrary style mixing — it is constitutional precision.

However, the hybrid's event patterns must be **strictly scoped** to:
1. DOM-11 activation triggering (all three modes)
2. DOM-06 governance event signaling to DOM-11

They must **not** extend to:
1. The recommendation pipeline (DOM-03 through DOM-05)
2. The blocking gates (CAP-02, CAP-10, CAP-18)
3. The audit domain (DOM-10)
4. Portfolio state updates (DOM-09)

---

## SECTION 06 — SELECTED ARCHITECTURAL STYLE

### Selected: Hybrid Architectural Style

**Primary Style:** Modular Monolith

**Supplementary Pattern:** Bounded Event-Driven — scoped exclusively to constitutionally characterized event relationships:
- DOM-11 activation initiation (all three modes)
- DOM-06 governance event signaling to DOM-11

**Style Characterization:**

The selected style is a **Modular Monolith with constitutionally scoped event signaling** — not a general event-driven architecture. The event pattern is applied only where the constitution itself characterizes the relationship as event-based. All recommendation pipeline logic, all blocking gates, and all information ownership enforcement operate within the modular monolith core.

The scope of the event pattern is derived, not chosen. It is bounded by two constitutional facts: (1) SDM-CONST-15 names "Event-Driven Activation" as a constitutionally authorized mode, and (2) AF 5.3 characterizes the DOM-06 → DOM-11 relationship as activation initiation (an event), not a data dependency.

---

## SECTION 07 — DECISION RATIONALE

### 7.1 Why Modular Monolith Is the Constitutional Core

**R1: SDM-CONST-12 describes a modular structure.** The constitution's modularity mandate — "LEGO-style approach; components shall be replaceable, configurable, versioned, and independently evolvable" — is the definitional description of a modular architecture. Among the candidate styles, only the modular monolith (and its hybrid derivatives) directly instantiates this constitutional language.

**R2: The three hard blocking gates require synchronous enforcement.** DEP-02, DEP-03, and DEP-04 carry zero-tolerance language ("no exceptions, no bypass" for CAP-18; "blocking gate" for CAP-02 and CAP-10). Synchronous sequential execution in a modular monolith is the style that most directly ensures these gates cannot be circumvented by asynchronous routing, partial processing, or distributed coordination failure.

**R3: Compile-time dependency enforcement satisfies CHAR-08 most strongly.** The six prohibited dependency edges (AF 5.4) — especially DOM-03 supplementary signals → DOM-05 computation — are most reliably enforced as structural impossibilities at module-level import rules rather than as operational policies on message buses or network routing tables.

**R4: Single information ownership is most tractable at module boundaries.** P-04 and P-05 require that each information class has exactly one authoritative producer. In a modular monolith, module ownership of types and data structures is an established pattern with strong tooling support. Private state derivatives are structurally discouraged when modules can only access each other through defined interfaces.

**R5: Authority class distinctions are naturally preserved.** The HUMAN_APPROVAL authority class of CAP-18 — which must not be diluted by co-location with autonomous capabilities — is naturally expressed as a distinct module with its authority class explicit in its design. The SHARED_AUTHORITY of CAP-09 is similarly expressible. In a modular monolith, authority classes are module-level properties. In a distributed system, they require network-level enforcement.

**R6: The current constitutional scope is a personal tool.** SDM-CONST-04 identifies the current system as a personal tool at ₹5,000 capital. SDM-CONST-12 requires future SaaS expansion to be possible without complete redesign. The modular monolith satisfies both: it is appropriately scoped for the current constitutional identity, and its well-maintained module boundaries enable future service extraction when the scale demands it. Implementing distributed infrastructure now would violate P-01 (Constitution Before Optimization) by optimizing for a future scale that the constitution does not yet require.

### 7.2 Why the Event Pattern Is a Constitutionally Grounded Addition

**R7: SDM-CONST-15 names Event-Driven Activation as a constitutionally authorized mode.** This is not a preference — it is an explicit constitutional authorization. An architectural style that provides no natural expression for this mode would be constitutionally incomplete. The bounded event pattern provides that expression without imposing event-driven architecture on the recommendation pipeline.

**R8: AF explicitly characterizes DOM-06 → DOM-11 as event-based.** AF 5.3 specifically analyzes the DOM-06 → DOM-11 → DOM-06 apparent cycle and confirms it is "activation initiation, not data dependency." The language "governance/risk events trigger mandatory review" appears in SADR Section 8. The constitution has already characterized this relationship as event-based. Formalizing it as such in the architectural style selection is constitutional precision, not style preference.

**R9: The bounded scope prevents event-driven pattern expansion.** By declaring the event pattern bounded to DOM-11 activation and DOM-06 governance signaling — and explicitly excluding it from the recommendation pipeline, blocking gates, audit, and portfolio state — this decision traces the exact constitutional boundary between where event patterns are constitutionally grounded and where they would create constitutional risk.

### 7.3 Why Eliminated Candidates Were Eliminated

**R10: Agent-Centric.** SDM-15 Rule 3 requires deterministic execution logic. Agent-centric architectures derive value from non-deterministic, emergent behavior. These are irreconcilable at the design philosophy level.

**R11: Pure Event-Driven.** The three blocking gates require synchronous, unconditional enforcement. Pure event-driven asynchronous processing cannot provide this guarantee without ceasing to be event-driven. The prohibition is structural, not compensable.

**R12: Layered.** The constitutional model is domain-organized and authority-organized. Horizontal layers cannot express domain ownership, authority class assignment, or the halt-state independence requirement without losing constitutional precision.

**R13: Microservices.** Not constitutionally disqualified, but constitutionally unjustified at the current personal-tool scale. The distributed systems complexity is not required by any constitutional provision. P-01 (Constitution Before Optimization) precludes pre-implementing SaaS-scale infrastructure for a personal tool.

---

## SECTION 08 — ARCHITECTURAL RISKS

### Risk 1: Module Boundary Erosion Over Time

**Description:** The modular monolith's primary weakness (A-W1) is that module boundaries require discipline to maintain. Without tooling or architectural tests enforcing the prohibited dependencies (AF 5.4), boundaries can erode over time — especially the DOM-03 → DOM-05 sentiment prohibition, which developers may find it tempting to "just add" as a small incremental change.

**Constitutional Source:** ADR-000 P-09; AF 5.4; GOV-VAL05 Rule 1

**Mitigation at Style Level:** Every future ADR that introduces a module or modifies a module boundary must include an explicit prohibited-dependency audit against AF 5.4. The ADR-002 (domain/module design) must specify boundary enforcement mechanisms as a first-class requirement, not an afterthought.

**Severity:** High — this risk, if realized, could produce a VAL-05 constitutional violation.

---

### Risk 2: Event Pattern Scope Creep

**Description:** The bounded event pattern, once established for DOM-11 activation and DOM-06 governance signaling, may be extended to other inter-domain communications without constitutional justification — converting the hybrid into a general event-driven architecture, with its associated blocking gate and dependency enforcement risks.

**Constitutional Source:** ADR-000 P-03; DEP-02, DEP-03, DEP-04; AF 5.4

**Mitigation at Style Level:** Every future ADR that proposes extending the event pattern scope must provide constitutional justification at the level of authority citation. "Convenience" or "consistency" are not constitutional justifications. ADR-001 explicitly bounds the event pattern to two relationship types; any expansion requires a new ADR with authority tracing.

**Severity:** Medium-High — scope creep could undermine the blocking gate fidelity that justified the Modular Monolith core.

---

### Risk 3: Governance Continuity Under Halt (Design Challenge)

**Description:** A-W2 identified that governance continuity under halt states requires explicit design in a modular monolith. If recommendation generation and governance monitoring share execution resources without explicit separation, a halt state could inadvertently halt monitoring functions that the constitution requires to continue.

**Constitutional Source:** AF 6.1; GOV-01 Rule 4; GOV-02 Rule 3; SDM-15 Rule 14; CHAR-05

**Mitigation at Style Level:** ADR-002 must specify that governance monitoring capabilities (CAP-31, CAP-23, CAP-29 state maintenance) operate independently of recommendation issuance — whether through separate execution contexts, separate scheduling, or explicit non-halting design. This is a design responsibility for ADR-002, not a style-level resolution.

**Severity:** Medium — the constitution is explicit about continuity requirements; the resolution is achievable but must be designed.

---

### Risk 4: Future Microservices Extraction Boundary Discipline

**Description:** SDM-CONST-12 requires future SaaS expansion to be possible without complete redesign. This means the module boundaries established now must be designed for future extraction into services. If modules are designed with tight internal coupling — even within their authorized boundaries — extraction will be difficult.

**Constitutional Source:** SDM-CONST-12; MOD-01, MOD-02

**Mitigation at Style Level:** ADR-002 must note that module boundaries should be designed as potential service boundaries — with explicit interface contracts, no shared mutable state across module lines, and well-defined input/output contracts per SADR capability specifications. This is a forward-looking design discipline, not a current implementation requirement.

**Severity:** Low-Medium — this is a future risk, not a current constitutional violation. Well-designed module boundaries address it.

---

### Risk 5: Open Validation Items as Extension Points

**Description:** 13 open validation items (CLASS_B/C/D) remain unresolved. The modular monolith must accommodate these as extension points — meaning the modules that depend on them must be designed with their interfaces defined by the generic abstractions specified in SADR, not by premature resolution of the unresolved items.

**Constitutional Source:** SADR Section 11; SDM-CONST-12; MOD-04

**Mitigation at Style Level:** No ADR may bake a specific implementation of an open validation item into a module boundary. Where a validation item affects a module's computation (e.g., VAL-03 affects CAP-05's non-ergodic condition signal), the module boundary must express the generic interface, not the specific formula.

**Severity:** Low — this is a design discipline issue. The SADR CLASS_B ruling "generic interface sufficient" already specifies the resolution approach.

---

## SECTION 09 — ADR-002 READINESS VERDICT

### Verdict: ADR-002 MAY PROCEED

**Evidence:**

1. **Architectural style is determined.** The selected style — Modular Monolith with constitutionally bounded event signaling for DOM-11 activation and DOM-06 governance events — is fully traced to authority and provides a definitive basis for domain/module design.

2. **No constitutional gaps remain.** All five authority levels are frozen. ADR-000 defines the 12 architectural principles that ADR-002 must satisfy. The Architecture Foundation defines the 11 constitutional domains, 13 information ownership rules, and 6 prohibited dependency edges that ADR-002 must preserve.

3. **Constitutional domain boundaries are pre-established.** ADR-002 does not need to re-derive domain boundaries — they are frozen in ARCHITECTURE_FOUNDATION_V1. ADR-002's task is to map those constitutional domains to the modular architecture the selected style prescribes.

4. **The blocking gate enforcement model is clear.** The modular monolith core provides a natural enforcement model for the three constitutional blocking gates. ADR-002 must specify the module-level expression of each gate without re-designing the gates themselves.

5. **The five architectural risks are identified and bounded.** ADR-002 has an explicit risk registry to address. Risk 1 (boundary erosion) and Risk 3 (governance continuity) are the highest priority design responsibilities for ADR-002.

**ADR-002 Scope Guidance (non-binding — for orientation only):**

ADR-002 should address:
- Mapping of 11 constitutional domains to modular structure
- Boundary enforcement mechanism for the six prohibited dependencies
- Module-level expression of the three authority classes
- Governance continuity design under halt states
- Event pattern boundary definition for DOM-11 and DOM-06 signaling
- Extension point design for the 13 remaining open validation items

ADR-002 must not:
- Design services, databases, APIs, or infrastructure
- Select specific technologies
- Resolve open validation items prematurely
- Reopen any constitutional or capability question

---

*ADR-001 derives its authority from SDM_V2.3 (as amended by GOV-VAL05), VAL05_OWNER_DECISION_RESOLUTION, SADR_V2.1 (as amended by SADR_AMENDMENT_VAL-05), ARCHITECTURE_FOUNDATION_V1, and ADR-000_ARCHITECTURE_PRINCIPLES. It introduces no module designs, no service designs, no technology selections, and no implementation decisions. It selects a style. All future ADRs must conform to this selection.*

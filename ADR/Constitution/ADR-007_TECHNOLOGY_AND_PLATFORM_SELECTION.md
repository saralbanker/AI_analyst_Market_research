# ADR-007 — TECHNOLOGY AND PLATFORM SELECTION

**Document Type:** Technology Realization Specification (Constitutional Boundary Artifact)
**Method:** ADR-007 Technology and Platform Selection Protocol — Constitutional Technology Adjudication
**Produced By:** Technology Realization Authority

**Authority Hierarchy (admissible evidence — exclusive):**
- Level 1: [SDM_V2.3.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/SDM_V2.3.md) (FROZEN — FINAL CANONICAL)
- Level 2: [VAL05_OWNER_DECISION_RESOLUTION.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/VAL05_OWNER_DECISION_RESOLUTION.md) (RESOLVED — Option B)
- Level 3: [SADR_V2.1.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/SADR_V2.1.md) (CERTIFIED)
- Level 4: [ARCHITECTURE_FOUNDATION_V1.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ARCHITECTURE_FOUNDATION_V1.md)
- Level 5: [ADR-000_ARCHITECTURE_PRINCIPLES.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-000_ARCHITECTURE_PRINCIPLES.md)
- Level 6: [ADR-001_ARCHITECTURAL_STYLE_SELECTION.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-001_ARCHITECTURAL_STYLE_SELECTION.md)
- Level 7: [ADR-002_CAPABILITY_TO_MODULE_REALIZATION.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-002_CAPABILITY_TO_MODULE_REALIZATION.md)
- Level 8: [ADR-003_MODULE_INTERNAL_REALIZATION.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-003_MODULE_INTERNAL_REALIZATION.md)
- Level 9: [ADR-003A](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-003A_ARCHITECTURAL_OBSERVATIONS_RESOLUTION.md) & [ADR-003B](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-003B_CONSTITUTIONAL_CLARIFICATION_AMENDMENT.md)
- Level 10: [ADR-004_ARCHITECTURAL_BOUNDARY_ENFORCEMENT.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-004_ARCHITECTURAL_BOUNDARY_ENFORCEMENT.md)
- Level 11: [ADR-005_STATE_AND_PERSISTENCE_REALIZATION.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-005_STATE_AND_PERSISTENCE_REALIZATION.md)
- Level 12: [ADR-006_INTERACTION_AND_EXECUTION_REALIZATION.md](file:///mnt/data/rj/AI_analyst_Market_research/ADR/Constitution/ADR-006_INTERACTION_AND_EXECUTION_REALIZATION.md)

**Evidence Boundary:** `Constitution/` directory only. No conclusion originates from outside this boundary. No conclusion derives from popularity, trend, vendor marketing, ecosystem size, developer preference, or implementation convenience.

> ### ⚠ STATUS BANNER — READ FIRST
>
> **Status:** FINAL — Implementation-Level ADR. **NON-CONSTITUTIONAL. ALL SELECTIONS REPLACEABLE.**
>
> ADR-007 is the **first and only** artifact in this corpus that names a technology. SDM Part V prohibits "Technology Selections, Database Decisions, Cloud Decisions, MCP Decisions, Broker Decisions, Infrastructure Decisions" from appearing in any **constitutional** artifact. ADR-000 P-12, ADR-005 §8.1, and ADR-004 §12.2 each explicitly delegate technology realization to "downstream technology-selection ADRs." ADR-007 **is** that downstream artifact. It therefore occupies a constitutional boundary: it must select technology, yet it must do so without granting any technology constitutional status. Per ADR-000 P-12, **every selection herein is a calibration choice that must remain valid if replaced.** A selection that becomes load-bearing for the architecture — such that replacing it would force an architectural change — is itself a constitutional violation and is rejected.
>
> **ADR-007 conforms technology to architecture. It never conforms architecture to technology.** It introduces no module, capability, information class, dependency edge, authority class, or governance rule. The architecture is frozen and unchanged.

---

## SECTION 1 — TECHNOLOGY SELECTION METHODOLOGY

### 1.1 The Single Question

Architecture is complete (ADR-001). Module realization is complete (ADR-002/003). Boundary enforcement is complete (ADR-004). State and persistence are complete (ADR-005). Execution is complete (ADR-006). ADR-007 answers one question:

> **Which technology stack realizes the frozen constitutional architecture with the lowest constitutional risk, while remaining fully replaceable?**

### 1.2 Selection Rules

1. **Architecture supremacy.** Technology conforms to architecture. Where a technology's idiom would pressure an architectural boundary, the technology is rejected, not the boundary (ADR-000 P-01; P-12).
2. **Minimum sufficiency.** The success condition is the *minimum* compliant stack, not the most capable. Any technology not required to satisfy a constitutional obligation, and not justified by a constitutional obligation, is classified *Unjustified* and excluded — because pre-implementing un-required capability optimizes for a scale the constitution does not yet mandate (ADR-000 P-01; ADR-001 R13; SDM-CONST-04).
3. **Replaceability is mandatory.** Each selection must survive substitution without architectural change (ADR-000 P-12; SDM-CONST-12 "replaceable, configurable, versioned, independently evolvable").
4. **Scale discipline.** The constitution defines the current system as a personal tool at ₹5,000 capital (SDM-CONST-04). Future SaaS expansion must remain *possible*, not be *pre-built* (SDM-CONST-12; ADR-001 R13; ADR-004 MB-02).
5. **Authority trace per decision.** No recommendation exists without an authority trace. Every selection carries: Constitutional Requirement → Candidates → Comparative Evaluation → Constitutional Risks → Preferred Selection → Authority Trace.

### 1.3 Classification Vocabulary

Each technology is classified into exactly one class:

| Class | Meaning |
|-------|---------|
| **Required** | A constitutional obligation cannot be discharged without a technology of this kind. A concrete, replaceable instance is selected. |
| **Optional** | Constitutionally permitted; selected only if it discharges an obligation more safely than the minimum, and only as a replaceable calibration. |
| **Prohibited** | Selecting any instance would violate a constitutional prohibition. Forbidden absolutely. |
| **Unjustified** | Constitutionally permitted but not required by any obligation at current scale; excluded under minimum-sufficiency (rule 2). May become justified only by a future constitutional amendment (e.g., SaaS expansion). |

### 1.4 What This Document Does Not Do (Forbidden Actions Honored)

It does not redesign architecture, modules, governance, ownership, execution, or state; it adds, removes, merges, and splits no capability; it modifies no dependency, authority, or governance structure (Protocol FORBIDDEN_ACTIONS; EVOCON-01). It does not reopen any frozen decision, including GOV-VAL05 (EVOCON-03) or the four-halt-state independence (EVOCON-04).

---

## SECTION 2 — CONSTITUTIONAL REQUIREMENTS MATRIX

The matrix below extracts, from the authority chain, every constraint that any technology selection must satisfy. These are the fitness criteria; the rest of the document tests candidates against them.

| Req | Constitutional Obligation | Technology Implication | Authority |
|-----|---------------------------|------------------------|-----------|
| **T-01** | Single deployable, modular, LEGO-style; future SaaS without redesign | Single-process modular monolith with module-boundary enforcement; no distributed infra now; service-extraction path preserved | SDM-CONST-12; ADR-001 §6; ADR-004 MB-02, MB-04 |
| **T-02** | Three blocking gates (CAP-02, CAP-10, CAP-18) are synchronous, unconditional, zero-bypass | Synchronous in-process call sequence for the pipeline; no async/eventual-consistency on gate paths | SDM-CONST-06; SADR §5; ADR-001 R2; ADR-006 INV-11; ADR-002 §8.3 |
| **T-03** | No path to a trade action; zero broker/execution interface under any circumstance | **No** broker SDK, order API, FIX/exchange client, or outbound execution path may be selected — at all | SDM-CONST-06/13; GOV-01 R1; GOV-02 R4–5; ADR-004 DEP-05/HAP-01; EVOCON-02 |
| **T-04** | Determinism of execution/governance logic | Deterministic runtime constructs on computational paths; no emergent/agentic control flow; AI confined to semantic domain | SDM-15 R3; ADR-001 §4 (D eliminated); SDM-04 R12 |
| **T-05** | Single owner per information class; 13 classes, 11 modules 1:1 | Persistence schema with one owning module per data class; no shared writable state | AF §4; ADR-000 P-04/P-05; ADR-004 OWN-01..06 |
| **T-06** | Audit immutable, write-once, terminal, no runtime read-back, tamper-evident | Append-only store with revoked UPDATE/DELETE + application tamper-evidence; isolated from operational state; no read path into capabilities | SADR CHANGE-06; ADR-000 P-07; ADR-004 AUD-02, DEP-03; ADR-005 §8.1 (mechanism delegated here) |
| **T-07** | Portfolio + governance state survive crash; boot into active halt state; reconstructable | Durable, crash-consistent (ACID) persistence for MOD-09 and MOD-06; trade-replay & detector-replay reconstruction | ADR-005 §5, §8.2–8.4; SC-01, SC-03; ADR-006 §8.4 |
| **T-08** | Sentiment advisory only; never enters computation | NLP/LLM output routed to presentation only; structurally unable to reach CAP-12/13/15/16 | GOV-VAL05 R1; ADR-000 P-09; ADR-004 DEP-04, VAL05-01..04 |
| **T-09** | CAP-18 Open Menu: simultaneous presentation, no timeout, distinct sentiment section, no re-ranking by UI | Single-user presentation surface that renders all opportunities at once; no auto-submit; presentation-only (no recompute) | SDM-08 R8; SADR CONSTRAINT-09; ADR-000 P-02; ADR-004 HAP-02, OWN-06 |
| **T-10** | Three activation modes (scheduled, on-demand, event-driven); MOD-11 initiates only | In-process scheduler + entrypoint + bounded in-process event dispatch; no orchestration engine | SDM-CONST-15; ADR-004 ACT-01..04; ADR-006 §9 |
| **T-11** | Event pattern bounded to DOM-11 activation + DOM-06→DOM-11 signaling only | In-process signaling only; **no** message broker / streaming infra | ADR-001 §5–6; ADR-004 ACT-04; EVOCON-07; ADR-002 §8 |
| **T-12** | ≥2 independent market-data sources cross-verified; delisted equities; Indian equities NSE/BSE only | Inbound read-only data adapters to ≥2 vendors + corporate-action + news + external-execution-record sources; replaceable per P-12 | SDM-02 R1–2; SDM-CONST-03; AF §1.3; EVOCON-10 |
| **T-13** | Mandated statistical methods: walk-forward CV (K-fold prohibited), deflated Sharpe / t-stat, survivorship-bias correction | A numerical/statistical computation capability sufficient to realize these methods deterministically | SDM-03 R1; SDM-05 R2,4; SDM-07 R4; CONSTRAINT-08 |
| **T-14** | Boundary erosion is the highest-severity architectural risk (could cause a VAL-05 violation) | A boundary-enforcement mechanism (compiler module system, or linter + architecture tests in CI) is **mandatory**, not optional | ADR-001 Risk 1 (High); ADR-004 §1.5; DEP-12 |

---

## SECTION 3 — PERSISTENCE TECHNOLOGY EVALUATION

**Constitutional Requirement (T-05, T-06, T-07).** State must survive restarts and crashes; portfolio (MOD-09) and governance (MOD-06) state must be crash-consistent so the system boots into any active halt state; audit (MOD-10) must be immutable, write-once, terminal, tamper-evident, and isolated; human decisions (MOD-07) and attribution (MOD-08) must persist as primary/reconstructable records; each of the 13 information classes must have exactly one owning writer.

**Candidate Technologies.**
- **(P-a)** Embedded single-file relational engine (SQLite-class): in-process, ACID, single deployable artifact.
- **(P-b)** Client–server relational engine (PostgreSQL-class): ACID, separate server process, networked.
- **(P-c)** Document store (MongoDB-class): schema-flexible, separate server.
- **(P-d)** Flat files / hand-rolled append-only logs for all state.

**Comparative Evaluation.**

| Criterion | P-a Embedded RDBMS | P-b Client/Server RDBMS | P-c Document store | P-d Flat files |
|-----------|--------------------|--------------------------|--------------------|----------------|
| Single deployable (T-01) | ✅ in-process | ⚠ extra server process | ⚠ extra server process | ✅ |
| ACID crash-consistency for halt-state boot (T-07) | ✅ | ✅ | ⚠ weaker multi-doc guarantees | ❌ hand-rolled |
| Single-owner schema enforcement (T-05) | ✅ table-per-class, grants per module | ✅ | ⚠ enforced only in app code | ❌ |
| Audit immutability via revoked UPDATE/DELETE (T-06) | ✅ | ✅ (role-based, stronger) | ⚠ app-level only | ⚠ app-level only |
| Minimum-sufficiency at ₹5k personal scale (rule 2) | ✅ | ❌ pre-builds server infra | ❌ pre-builds server infra | ✅ but unsafe |
| SaaS-evolution target (SDM-CONST-12) | ✅ migrates to P-b | ✅ is the target | ✅ | ❌ |

**Constitutional Risks.** P-b/P-c introduce a networked server process unjustified at current scale (ADR-000 P-01; ADR-001 R13) — adoption now would optimize for a future the constitution does not yet require. P-d cannot structurally guarantee crash-consistency (T-07) or immutability (T-06) and would re-create the hidden-state and tamper risks the constitution forbids (P-05, P-07). P-a's only risk is that an embedded engine's single-file store must keep **audit physically separated** from operational state to honor audit isolation and the terminal-sink boundary (DEP-03) — addressed in Section 7.

**Preferred Selection.**
- **Required:** an **embedded, ACID, relational persistence engine** for operational state (MOD-09 portfolio, MOD-06 governance flags, MOD-07 human decisions, MOD-08 attribution), realized as **one table-group per owning module** with write grants restricted to that module's code path. Replaceable instance: SQLite-class embedded engine.
- **Optional / future:** a client–server relational engine (PostgreSQL-class) is the **designated SaaS-evolution target** when (and only when) a future amendment authorizes multi-node scale; until then it is Unjustified.
- **Prohibited:** any persistence configuration that exposes the audit store to capability read-back, or that lets two modules write the same information class.
- **Unjustified now:** document stores; distributed/cloud-managed databases.

**Authority Trace.** SDM-CONST-04 (scale), SDM-CONST-12 (modular/replaceable/SaaS), ADR-000 P-01/P-04/P-05/P-07/P-12, ADR-001 R13, ADR-004 OWN-01..06 + DEP-03, ADR-005 §3, §5, §7, §8 (SC-01..SC-06).

---

## SECTION 4 — EXECUTION TECHNOLOGY EVALUATION

**Constitutional Requirement (T-02, T-04, T-10).** The recommendation cycle is the unit of execution, with a constitutionally ordered, synchronous pipeline gated by three absolute blocking gates; continuous monitors (CAP-19/23/31), portfolio maintenance (CAP-29), and audit (CAP-30) run cycle-independently and are never halted; three activation modes initiate cycles; MOD-11 initiates but never orchestrates.

**Candidate execution models.**
- **(X-a)** Synchronous in-process pipeline + in-process scheduler + long-lived background tasks for continuous monitors.
- **(X-b)** Asynchronous event-driven execution across the pipeline (message-passing between stages).
- **(X-c)** External job queue / workflow-orchestration engine driving stages as distributed tasks.

**Comparative Evaluation.**

| Criterion | X-a Synchronous in-process | X-b Async event pipeline | X-c External orchestrator |
|-----------|----------------------------|--------------------------|----------------------------|
| Blocking-gate fidelity (T-02) | ✅ gates are mandatory synchronous calls | ❌ eventual-consistency windows bypass gates | ❌ partial-failure/retry windows |
| Determinism (T-04) | ✅ sequential, reproducible | ⚠ ordering nondeterminism | ⚠ scheduler nondeterminism |
| MOD-11 = initiation, not orchestration (T-10) | ✅ dependency graph drives order | ⚠ bus topology becomes implicit orchestrator | ❌ orchestrator owns workflow (ACT-01 violation) |
| Continuous monitors never halted (INV-14) | ✅ background tasks/threads independent of cycle | ⚠ requires careful stream partitioning | ⚠ requires separate always-on workers |
| Minimum sufficiency (rule 2) | ✅ | ❌ infra not required | ❌ infra not required |

**Constitutional Risks.** X-b is the pure event-driven style **already eliminated** in ADR-001 §4 precisely because asynchronous, eventually-consistent processing cannot guarantee the synchronous blocking gates (ADR-001 R2/R11). X-c converts MOD-11 into an orchestration layer, directly violating ACT-01 (`Activation Is Initiation — Not Orchestration`) and importing distributed-coordination complexity unjustified at scale (P-01).

**Preferred Selection.**
- **Required:** **X-a — a single-process application** in which (i) the recommendation pipeline executes as a **synchronous, dependency-ordered call sequence** with the three gates as mandatory in-line checks; (ii) continuous monitors (CAP-19/23/31), CAP-29, and CAP-30 run as **long-lived in-process background tasks** independent of cycle activation; (iii) Mode 1 uses an **in-process scheduler** (or host cron invoking the on-demand entrypoint), Mode 2 an explicit human-invoked entrypoint, Mode 3 an **in-process event dispatch** from MOD-06 to MOD-11.
- **Permitted optimization (bounded):** concurrency *within* MOD-01 to fetch from multiple data vendors in parallel is allowed, because cross-verification (CAP-02) still executes synchronously as a gate before any signal logic (DEP-06). Concurrency may never be applied to a gate path or to reorder the pipeline.
- **Prohibited:** asynchronous routing across any blocking gate; any orchestration engine that sequences modules.
- **Unjustified now:** external job queues, workflow engines, async task brokers.

**Authority Trace.** SDM-CONST-15, SADR §5, ADR-001 §4 + R2/R11, ADR-002 §8.3, ADR-004 ACT-01..04 + DEP-06, ADR-006 §2, §4, §9, INV-11, INV-13, INV-14.

---

## SECTION 5 — FRONTEND TECHNOLOGY EVALUATION

**Constitutional Requirement (T-09).** The frontend realizes CAP-18 (DOM-07) visibility: the complete advisory package presented **simultaneously** as an Open Menu (no sequential forced selection); the sentiment/news section rendered as a **distinct named section** separate from computational scores; active halt states and current drawdown-vs-5% displayed; explicit human decision captured with **no timeout/auto-approval**; presentation-only (the UI must not re-rank, filter, or recompute — that would re-perform MOD-05's function, OWN-06). Single human owner; one user class only (AF §1.2).

**Candidate Technologies.**
- **(F-a)** Local single-user web interface served by the modular monolith (server-rendered).
- **(F-b)** Single-page application (separate client build) talking to the monolith.
- **(F-c)** Desktop GUI / terminal (TUI/CLI) application.

**Comparative Evaluation.**

| Criterion | F-a Local web (server-rendered) | F-b SPA | F-c Desktop/CLI |
|-----------|----------------------------------|---------|------------------|
| Open Menu, all-at-once (T-09) | ✅ | ✅ | ✅ |
| No client-side re-ranking / OWN-06 safe | ✅ presentation logic stays at MOD-07 | ⚠ tempting to recompute client-side | ✅ |
| No auto-submit/timeout (HAP-02) | ✅ | ✅ | ✅ |
| Sentiment as distinct section (VAL05-04) | ✅ | ✅ | ✅ |
| Single deployable / minimum infra (T-01, rule 2) | ✅ inside the monolith | ⚠ separate build/deploy pipeline | ✅ |
| Single-user scope (AF §1.2) | ✅ | ✅ | ✅ |

**Constitutional Risks.** Any frontend can technically auto-submit or pre-select a "recommended" action — both forbidden (ADR-000 P-02; ADR-004 HAP-02). The dominant risk is a client that **recomputes or re-orders** opportunities, silently re-performing CAP-15 ranking and violating OWN-06; F-b raises this risk most. Blending sentiment into the score display violates VAL05-04 and must be structurally prevented in the view layer regardless of framework.

**Preferred Selection.**
- **Required:** **F-a — a local, single-user presentation surface served by the modular monolith**, rendering the assembled advisory view produced by MOD-07. It must present all EV-filtered, positively-ranked opportunities simultaneously, render the supplementary/sentiment section as a labelled distinct section, display halt states + drawdown, capture an explicit decision (approve / reject / override) with no auto-completion, and perform **zero** ranking/filtering/score computation.
- **Optional:** an SPA (F-b) or desktop/TUI (F-c) is admissible as a pure replaceable presentation calibration **iff** it imports no ranking/scoring logic and adds no decision-pressuring affordance.
- **Prohibited:** any timeout-based auto-approval; any "recommended action" CTA that hides the full ranked set; any sentiment-into-score blending; any order-entry / broker UI.

**Authority Trace.** SDM-08 R8, SADR CONSTRAINT-09, GOV-VAL05 R4, AF §1.2, ADR-000 P-02, ADR-004 HAP-01/HAP-02/OWN-06/VAL05-04, ADR-006 §6.

---

## SECTION 6 — BACKEND TECHNOLOGY EVALUATION

**Constitutional Requirement (T-04, T-05, T-13, T-14).** The backend realizes 11 modules with compile-/build-time-preservable boundaries and six structurally-unroutable prohibited edges; deterministic computation; the mandated statistical methods (walk-forward CV, deflated Sharpe / t-stat, survivorship-bias correction); and a **mandatory** boundary-enforcement mechanism (T-14 — boundary erosion is the highest-severity risk).

**Candidate Technologies (core implementation language/runtime).**
- **(B-a)** Dynamically-typed scientific language (Python-class): dominant numerical/statistical/NLP capability; module boundaries enforced by tooling (linters + architecture tests), not by a compiler.
- **(B-b)** Statically-typed module-system language (JVM/.NET/Go/Rust-class): structural compile-time boundary enforcement; numerical/NLP capability present but less direct for the mandated quant/NLP methods.

**Comparative Evaluation.**

| Criterion | B-a Scientific dynamic | B-b Typed module-system |
|-----------|------------------------|--------------------------|
| Realizes mandated statistics/NLP deterministically (T-13, T-08) | ✅ most direct realization of walk-forward, deflated Sharpe, survivorship correction, semantic NLP | ⚠ achievable, less direct |
| Structural boundary enforcement (T-14) | ⚠ requires CI-enforced linter + architecture tests | ✅ compiler/module system enforces natively |
| Determinism on computational paths (T-04) | ✅ with discipline | ✅ with discipline |
| Single deployable / per-module future extraction (T-01, MB-02) | ✅ | ✅ |
| Replaceability (P-12) — language must not be load-bearing | ✅ per-module substitution permitted | ✅ |

**Resolution of the trade.** Two constitutional pressures pull in opposite directions: T-13 (the constitution *mandates specific statistical methods* and isolates AI to the semantic domain) favors B-a; T-14 (boundary erosion is the single High-severity architectural risk) favors B-b. ADR-004 §1.5 makes the boundary-enforcement *mechanism* a calibration choice — meaning B-a's tooling-based enforcement is constitutionally **sufficient if actually enforced**. ADR-001 Risk 1, however, makes *some* enforcement **mandatory**. Therefore B-a is admissible **only when paired with a mandatory, CI-gated boundary-enforcement layer**.

**Constitutional Risks.** Selecting B-a without enforced boundary tooling realizes ADR-001 Risk 1 (boundary erosion → potential GOV-VAL05 computational-leak, severity High). Selecting any language as a *constitutional dependency* (such that the architecture only holds for that language) violates P-12. Using language-level metaprogramming/agentic frameworks that enable emergent control flow violates SDM-15 R3 (determinism) and the ADR-001 §4 agent-centric elimination.

**Preferred Selection.**
- **Required (preferred instance):** **B-a — a scientific dynamically-typed core language (Python-class)**, because it most directly and verifiably realizes the constitutionally-*mandated* computation (walk-forward CV, deflated Sharpe/t-stat, survivorship-bias-corrected datasets) and the semantic-domain NLP — selected on constitutional-method fitness, **not** ecosystem popularity.
- **Required co-selection (T-14, non-negotiable):** a **boundary-enforcement layer** — module/import-dependency linting plus architecture tests asserting the AF 5.1 allowed-edge list and the six AF 5.4 prohibitions, run as a **CI gate**. This discharges ADR-001 Risk 1 and DEP-12.
- **Equally admissible alternative:** **B-b — a statically-typed module-system language** — for an owner who prefers structural compile-time enforcement over ecosystem directness. The architecture is invariant to this choice (P-12); per-module language substitution is permitted under MB-02/SDM-CONST-12.
- **Prohibited:** autonomous-agent / goal-directed frameworks as control flow; any backend construct that lets attribution, audit, or sentiment reach computation (enforced structurally per Section 7–8).

**Authority Trace.** SDM-03 R1, SDM-05 R2/R4, SDM-07 R4, SDM-15 R3, CONSTRAINT-08, SDM-04 R12, ADR-000 P-11/P-12, ADR-001 §4 + Risk 1, ADR-004 §1.5 + DEP-12 + MB-01..04.

---

## SECTION 7 — AUDIT TECHNOLOGY EVALUATION

**Constitutional Requirement (T-06).** Audit (MOD-10/CAP-30) is the terminal sink: it receives from all, emits to none; records are **structurally immutable** (not merely append-only — SADR CHANGE-06), write-once, never read back into any capability at runtime; tamper-evidence must be verifiable; reconstruction/verification must confirm no record was modified, deleted, or reordered. **ADR-005 §8.1 explicitly delegates the tamper-evidence mechanism to this ADR** (ADR-005A removed the prescribed hash-chain from the constitutional layer for this reason).

**Candidate Technologies.**
- **(A-a)** Append-only audit table in the relational store, with UPDATE/DELETE grants revoked + per-record cryptographic hash-chain (each record commits a hash of the prior), in a persistence boundary separate from operational state.
- **(A-b)** Append-only log file(s) with hash-chaining / signed segments.
- **(A-c)** External managed immutable/WORM ledger or blockchain service.

**Comparative Evaluation.**

| Criterion | A-a Append-only table + hash-chain | A-b Append-only file + hash-chain | A-c External WORM/ledger |
|-----------|-------------------------------------|-----------------------------------|---------------------------|
| Structural immutability (CHANGE-06) | ✅ revoked UPDATE/DELETE + chain | ✅ if writer enforces | ✅ |
| Terminal sink, no read-back into capabilities (DEP-03) | ✅ no read API to capabilities | ✅ | ⚠ network dependency invites coupling |
| Tamper-evidence verifiable (T-06) | ✅ chain re-validation | ✅ | ✅ |
| Isolation from operational state (T-05/T-06) | ✅ separate schema/file | ✅ inherently separate | ✅ |
| Minimum sufficiency (rule 2) | ✅ | ✅ | ❌ external infra unjustified |

**Constitutional Risks.** The defining risk is any **outbound edge from MOD-10** or any capability reading audit at runtime (DEP-03/OWN-04/INV-04). The store must expose **no read interface to AUTONOMOUS_RESEARCH or SHARED_AUTHORITY capabilities**; only a human-facing review/reporting function may read, and that function must have no write path to any capability. "Append-only" alone is insufficient: deletion-without-modification must also be impossible (ADR-004 AUD-02). A-c additionally risks importing external coupling and is unjustified at scale.

**Preferred Selection.**
- **Required:** **A-a — an append-only audit table with UPDATE/DELETE revoked at the persistence-grant level, a per-record hash-chain for tamper-evidence, written write-once by every capability, physically isolated from operational state, and exposed for read only to a human-review function that holds no write edge to any capability.** Verification = re-walk the hash-chain; reconstruction never reads audit into capabilities (ADR-005 §8.4).
- **Optional hardening:** filesystem/object WORM retention under the audit store; record signing.
- **Prohibited:** any audit read path into a capability; any UPDATE/DELETE capability over audit records; any MOD-10 outbound edge.
- **Unjustified now:** external ledger/blockchain services.

**Authority Trace.** SADR CHANGE-06, CAP-30 Boundary, AF §5.1/§5.4, ADR-000 P-07, ADR-004 AUD-01/AUD-02/AUD-03 + DEP-03 + OWN-04, ADR-005 §3.12/§5.1/§8.1, ADR-006 INV-04 + §7.

---

## SECTION 8 — EVENT, PORTFOLIO-STATE, AND INTEGRATION-BOUNDARY EVALUATION

### 8.1 Event Realization (Investigation 05)

**Constitutional Requirement (T-11).** The event pattern is constitutionally bounded to exactly two relationships: DOM-11 activation initiation (all three modes) and DOM-06→DOM-11 governance signaling. It must **not** touch the recommendation pipeline, the blocking gates, audit, or portfolio updates (ADR-004 ACT-04; ADR-002 §8.3).

**Candidates:** (E-a) in-process publish/subscribe or direct callback for the two bounded relationships; (E-b) external message broker / streaming platform (Kafka/RabbitMQ/cloud queue); (E-c) Redis-class pub/sub.

**Evaluation & Risk.** E-b/E-c are message **infrastructure**: they invite the event pattern to spread to the pipeline (scope creep — ADR-001 Risk 2, EVOCON-07), and a shared bus across halt capabilities would create undeclared coupling that violates four-state independence (ADR-002 §8.3; P-06). None of it is required at single-process, personal scale (P-01).

**Selection.** **Required:** **E-a — in-process bounded event signaling** for the two authorized relationships only. **Prohibited / Unjustified:** message brokers, streaming platforms, and shared event buses — there is no constitutional obligation that justifies messaging infrastructure; architecture requirements drive this conclusion, not preference.

**Authority Trace.** SDM-CONST-15, ADR-001 §5–6 + Risk 2, ADR-002 §8.2/§8.3, ADR-004 ACT-04 + DEP-11 + EVOCON-07, AF §5.3.

### 8.2 Portfolio State Realization (Investigation 07)

**Constitutional Requirement.** CAP-29 (MOD-09) is the single authoritative source, sourced exclusively from human-confirmed external execution records; persistent across restart; reconstructable by trade replay (`S_t = S_0 + ΣT_i`); no shadow/private derivative anywhere (SC-01; INV-07; DEP-08).

**Selection.** **Required:** portfolio state lives in **one owning table-group in the embedded ACID store (Section 3)**, written only by MOD-09's reconciliation path from the inbound external-execution-record adapter (Section 8.3), with an ordered, replayable trade ledger enabling reconstruction. **Prohibited:** any other module persisting portfolio-derived state consumed as authoritative; any "pending"/hypothetical portfolio state before human confirmation (ADR-000 P-05).

**Authority Trace.** AF §5.5, ADR-000 P-05, ADR-004 OWN-01/DEP-08, ADR-005 §3.8/§4.1/§8.2, ADR-006 INV-07.

### 8.3 Integration Boundary Realization (Investigation 08)

**Constitutional Requirement (T-03, T-12).** Inbound, read-only crossings only: ≥2 independent NSE/BSE market-data vendors (cross-verified at CAP-02), corporate-action source, news/event source(s), and the authoritative external execution record into MOD-09. The broker / execution venue is **entirely outside the boundary with zero interface in any direction, under all circumstances including every halt state** (AF §1.3; GOV-01 R1; GOV-02 R4–5; DEP-05).

| Boundary | Direction | Technology Class | Authority |
|----------|-----------|------------------|-----------|
| Market-data vendors (≥2 independent) | Inbound, read-only | **Required, replaceable** vendor adapters (anti-corruption layer in MOD-01); architecture depends on the *two-source cross-verification interface*, never a specific vendor | SDM-02 R1–2; SDM-CONST-03; EVOCON-10; P-12 |
| Corporate-action source | Inbound, read-only | **Required, replaceable** adapter (MOD-01) | SDM-02 R3; AF §1.3 |
| News / event source(s) | Inbound, read-only | **Optional, replaceable** adapter (MOD-03) feeding advisory-only sentiment | SDM-04; GOV-VAL05; T-08 |
| Authoritative external execution record | Inbound, read-only | **Required, replaceable** adapter (MOD-09) | CAP-29 Inputs; ADR-005 §3.8 |
| **Broker / execution venue** | **None** | **PROHIBITED — no SDK, no order API, no FIX/exchange client, no outbound execution path may be selected at all** | SDM-CONST-06/13; GOV-01 R1; GOV-02 R4–5; SADR CONSTRAINT-01; ADR-004 DEP-05/HAP-01; EVOCON-02 |

**The single hardest constraint in this document:** the *absence* of any broker/execution technology is itself a constitutional requirement. The external execution record is an **inbound** observation; it must never be repurposed into an outbound order path.

### 8.4 AI / NLP Technology (Sentiment, CAP-08)

**Constitutional Requirement (T-04, T-08).** AI model evaluations are isolated **exclusively to the semantic and cognitive domain** (SDM-04 R12); their output is advisory-only and may not enter CAP-12/13/15/16 in any form (GOV-VAL05; VAL05-01..03). VAL-06 (efficacy of US-trained NLP on Indian disclosures) remains an open extension point (EVOCON-08).

**Selection.** **Optional, replaceable:** an NLP/LLM component for CAP-08 that emits **advisory text/sentiment routed only to the MOD-07 advisory section**, structurally unable to reach any computational capability. The model/vendor is a replaceable calibration (P-12) and an open extension point (VAL-06) — it **cannot** be a constitutional dependency, and per latest-model guidance any such model is swappable without architectural change. **Prohibited:** any path from NLP output into a confidence/EV/ranking/allocation formula; any agentic/tool-using model with a route toward execution or computation (SDM-15 R3; P-03; ADR-001 §4 D-elimination).

---

## SECTION 9 — DEPLOYMENT MODEL EVALUATION

**Constitutional Requirement (T-01, T-07, T-10).** A single deployable modular monolith at personal-tool scale, persisting state across restarts, booting into any active halt state, supporting the three activation modes; future SaaS extraction possible without redesign.

**Candidates:** (D-a) single-host single process + local persistent volume; (D-b) single container image on one host; (D-c) container orchestration platform (Kubernetes-class) / managed cloud.

**Evaluation & Risk.** D-c pre-builds SaaS-scale operational infrastructure the constitution does not require, violating minimum-sufficiency and P-01 (ADR-001 R13). Multi-node deployment would also place the synchronous blocking gates across a network — the exact distributed-coordination risk that conditionally eliminated microservices (ADR-001 §4 B; ADR-004 §12.2 E8).

**Preferred Selection.**
- **Required:** **D-a — single-host, single-process deployment** of the modular monolith with a **local persistent volume** for the embedded operational store and the isolated audit store; Mode 1 via in-process scheduler or host cron; restart procedure recovers portfolio + governance state and boots into active halt states **before** resuming recommendation issuance (ADR-006 §8.4–8.5).
- **Optional:** **D-b — a single container image** for reproducibility/portability (supports SDM-CONST-12 replaceability), provided it remains a single deployable unit.
- **Unjustified now:** orchestration platforms, multi-node, managed cloud (the designated SaaS-evolution path, gated on a future amendment; each future-extracted service must map 1:1 to one constitutional module per MB-02).

**Authority Trace.** SDM-CONST-04/12, ADR-000 P-01, ADR-001 §4 B + R13, ADR-004 MB-02 + §12.2 E8, ADR-006 §8.4–8.5.

---

## SECTION 10 — TECHNOLOGY STACK DECISION

**Required (minimum compliant stack):**

| Layer | Selection (replaceable instance) | Class |
|-------|----------------------------------|-------|
| Architectural style (frozen by ADR-001) | Modular Monolith + bounded in-process event signaling | — |
| Backend core | Scientific dynamically-typed language (Python-class) **+ mandatory CI-gated boundary-enforcement** (import linter + architecture tests asserting AF 5.1 / AF 5.4) | Required |
| Execution | Single-process synchronous pipeline; in-process scheduler; long-lived background monitors | Required |
| Operational persistence | Embedded ACID relational engine (SQLite-class), one table-group per owning module | Required |
| Audit persistence | Append-only audit table, UPDATE/DELETE revoked, per-record hash-chain, isolated, read-only to human review | Required |
| Frontend | Local single-user presentation surface served by the monolith; presentation-only | Required |
| Events | In-process bounded pub/sub for DOM-11 activation + DOM-06→DOM-11 only | Required |
| Inbound integrations | Replaceable read-only adapters: ≥2 market-data vendors, corporate-action, external-execution-record | Required |
| News/NLP sentiment | Replaceable advisory-only NLP component (CAP-08 → MOD-07 only) | Optional |
| Deployment | Single host / single process (optionally one container image) + local persistent volume | Required |

**Prohibited (absolute):** any broker / execution-venue / order-routing technology (SDK, API, FIX, exchange client) — Section 8.3, T-03; any timeout/auto-approval mechanism at CAP-18 (T-09); any audit read-back path or MOD-10 outbound edge (T-06); any sentiment→computation path (T-08); any autonomous-agent control-flow framework (T-04); any shared event bus across halt capabilities (P-06).

**Unjustified now (excluded under minimum-sufficiency; reconsider only on a future amendment):** client–server / distributed / cloud-managed databases; message brokers & streaming platforms; external job queues / workflow orchestrators; container orchestration / multi-node / managed cloud; external WORM/ledger services.

---

## SECTION 11 — ARCHITECTURE COMPLIANCE VALIDATION

Every selection validated against the authority chain; any technology-driven architecture reasoning rejected.

| Authority | Obligation | ADR-007 Compliance | Result |
|-----------|-----------|--------------------|--------|
| SDM-CONST-06/13; GOV-01/02; DEP-05; EVOCON-02 | No execution; zero broker interface | Broker technology **Prohibited**; external record is inbound-only | ✅ |
| SDM-CONST-12; ADR-000 P-12 | Modular, replaceable, SaaS-possible | All selections replaceable; single deployable; SaaS path preserved, not pre-built | ✅ |
| SDM-CONST-15; ADR-004 ACT-01..04 | Three modes; initiation not orchestration | In-process scheduler/entrypoint/event dispatch; no orchestrator | ✅ |
| SADR §5; ADR-001 R2; INV-11 | Synchronous blocking gates | Synchronous in-process pipeline; async barred from gate paths | ✅ |
| SDM-15 R3; ADR-001 §4 (D) | Determinism; no emergent control flow | Sequential execution; AI confined to semantic domain | ✅ |
| AF §4; ADR-000 P-04/P-05; OWN-01..06 | Single owner per class; no shadow state | Table-group per owning module; portfolio sole-source | ✅ |
| SADR CHANGE-06; P-07; DEP-03; ADR-005 §8.1 | Immutable, terminal, no read-back audit | Append-only + revoked UPDATE/DELETE + hash-chain; no capability read path | ✅ |
| ADR-005 §5/§8; ADR-006 §8.4 | Crash-survival; boot into halt state | Embedded ACID store; recovery before issuance | ✅ |
| GOV-VAL05; P-09; DEP-04; VAL05-01..04 | Sentiment advisory only | NLP routed to presentation only; no computational edge | ✅ |
| SDM-08 R8; CONSTRAINT-09; HAP-02; OWN-06 | Open Menu; no timeout; presentation-only | Local surface renders all-at-once; no auto-submit; no recompute | ✅ |
| ADR-001 §5–6; ACT-04; EVOCON-07 | Event pattern bounded | In-process signaling only; messaging infra excluded | ✅ |
| SDM-02 R1–2; SDM-CONST-03; EVOCON-10 | ≥2 sources cross-verified; Indian equities only | Replaceable inbound adapters; cross-verify gate preserved | ✅ |
| ADR-001 Risk 1; ADR-004 §1.5; DEP-12 | Boundary erosion mitigation mandatory | CI-gated boundary enforcement is a co-required selection | ✅ |
| SDM Part V; ADR-000 P-12 | No technology may gain constitutional status | Status banner; every selection replaceable & non-load-bearing | ✅ |

**No architecture redesign performed. No capability added/removed/merged/split. No dependency, authority, or governance structure modified.** ADR-007 selected technology *under* the frozen architecture only.

---

## SECTION 12 — IMPLEMENTATION READINESS VERDICT

### Constitutional Evidence Chain
1. **SDM_V2.3 → ADR-006** are frozen and complete; ADR-006 issued `ADR-007 MAY PROCEED`.
2. ADR-005 §8.1 and ADR-004 §12.2 explicitly delegated the remaining technology/mechanism choices (tamper-evidence, boundary-enforcement mechanism, persistence, deployment) to this ADR.
3. ADR-007 selected the **minimum constitutionally compliant stack**, classified every technology as Required / Optional / Prohibited / Unjustified, and traced each to authority.
4. Every selection is replaceable; none is load-bearing for the architecture (P-12). The single absolute prohibition — no broker/execution technology — is itself a constitutional requirement, satisfied by selecting nothing there.

### Verdict

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║              IMPLEMENTATION MAY PROCEED                          ║
║                                                                  ║
║  The minimum constitutionally compliant technology stack is      ║
║  selected. Ownership, governance, audit isolation, human         ║
║  authority, execution integrity, state integrity, and            ║
║  architectural boundaries are preserved. Lowest constitutional   ║
║  risk achieved by excluding all unjustified infrastructure and   ║
║  prohibiting every execution/broker technology absolutely.       ║
║  Every selection is replaceable. The architecture is unchanged.  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

### Residual Risk Register (carried into implementation)
| Risk | Source | Mitigation |
|------|--------|------------|
| Boundary erosion (High) | ADR-001 Risk 1 | CI-gated boundary enforcement is a **co-required** selection (Section 6); not optional |
| Event-pattern scope creep (Med-High) | ADR-001 Risk 2 | Messaging infra Prohibited/Unjustified; in-process signaling only (Section 8.1) |
| Audit read-back leakage | INV-04 | Audit store exposes no read interface to capabilities (Section 7) |
| Sentiment computational leakage | GOV-VAL05 | NLP structurally confined to presentation (Section 8.4) |
| Premature SaaS infra | ADR-000 P-01 | All distributed/cloud tech classified Unjustified until a future amendment |

---

*ADR-007 derives its authority exclusively from SDM_V2.3, VAL05_OWNER_DECISION_RESOLUTION, SADR_V2.1, ARCHITECTURE_FOUNDATION_V1, and ADR-000 through ADR-006. It is the constitutionally-authorized downstream technology-selection artifact. It introduces no module, capability, information class, dependency edge, authority class, or governance rule, and it grants no technology constitutional status. Every selection is a replaceable calibration choice that must remain valid if substituted. Technology conforms to architecture; architecture never conforms to technology.*

*End of ADR-007_TECHNOLOGY_AND_PLATFORM_SELECTION*

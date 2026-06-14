# IMP-001 — IMPLEMENTATION BOOTSTRAP

**Document Type:** Implementation Bootstrap Specification
**Authority:** Implements ADR-000 through ADR-007 (FROZEN). Introduces no architecture, no modules, no capabilities, no dependencies, no governance. Converts the frozen architecture into a running, minimum-compliant codebase.
**Status:** ACTIVE — living document, updated as phases complete.

**Phase Status:** Phase 1 COMPLETE. Phase 2 COMPLETE. Phase 3 COMPLETE. All six
Section 9 Working Software Requirement checks pass (`python -m src.main`,
`python -m src.scheduler`, `pytest tests/architecture`, audit chain verified,
GOV-01 halt-gating demonstrated). Remaining work is extensibility/optimization
beyond the minimum-compliant vertical slice (additional symbols, real vendor
adapters, CAP-08 news source, CAP-26 lockout entry logic, etc.) — not required
for the Working Software Requirement.

---

## SECTION 1 — IMPLEMENTATION STRATEGY

### 1.1 Order of Implementation (dependency order = risk order)

The constitutional dependency graph (ADR-002 §6.1, ADR-006 §4) already fixes the execution order of the recommendation pipeline. Implementation order follows the same graph, because every downstream module is meaningless without its upstream producer:

1. **Persistence foundation** — embedded ACID store (ADR-007 §3), schema with one table-group per owning module (ADR-005 §7).
2. **MOD-10 (Audit)** — built first among "modules" because every other module's first real write is an audit record (ADR-004 AUD-01). A module that cannot write audit cannot be considered working.
3. **MOD-09 (Portfolio State)** — required by MOD-05/MOD-06/MOD-07; trivial to seed.
4. **MOD-11 (Activation)** — the entrypoint; initiation-only (ADR-006 §9).
5. **MOD-01 (Market Data Foundation)** — including the CAP-02 blocking gate, even if vendor adapters are stubs.
6. **MOD-02 (Market Context)** — minimal regime classifier.
7. **MOD-03 (Evidence Generation)** — technical signal generation (CAP-07); CAP-08/CAP-09 as minimal pass-through stubs.
8. **MOD-04 (Statistical Validation)** — CAP-10 blocking gate + CAP-11, even if the validation logic is a minimal walk-forward placeholder.
9. **MOD-05 (Recommendation Synthesis)** — CAP-12 through CAP-20.
10. **MOD-06 (Risk & Governance)** — halt-state flags persisted, detection stubs that always evaluate (continuously callable), gating applied to MOD-05 issuance.
11. **MOD-07 (Human Decision Authority)** — CLI Open Menu + CAP-18 gate.
12. **MOD-08 (Attribution)** — post-gate observer, last because it depends on MOD-07 output.

### 1.2 Risk-First Deviations

Two items are pulled forward regardless of "natural" order because they are the highest-severity constitutional risks (ADR-007 Residual Risk Register):

- **CI-gated boundary enforcement** (ADR-004 §1.5, ADR-007 T-14, DEP-12) is implemented in **Phase 1**, before any module beyond the persistence layer, so that no module can ever be written without the dependency-edge test already watching it.
- **Audit write path** is implemented before any other module produces its first record, so "every capability produces an audit record" (AUD-01) is true from the first line of business logic onward.

### 1.3 What "Working" Means at Each Phase

Per the Working Software Rule, each phase ends with a command that can be executed and observed to produce output — not merely a passing unit test. Phase exit criteria are stated in Section 8.

---

## SECTION 2 — REPOSITORY STRUCTURE

### 2.1 Root Layout

```
/ADR/                       (existing — frozen, untouched)
/IMP/                        IMP-series implementation bootstrap docs (this file)
/src/                        application source (the modular monolith)
/tests/
  /architecture/             boundary-enforcement tests (T-14, DEP-12)
  /unit/                      per-module unit tests (mirrors /src layout)
  /integration/               vertical-slice / cycle tests
/data/                        local SQLite files (gitignored)
README.md
.gitignore
```

### 2.2 `/src` Module Layout (1:1 with ADR-002 §2.2)

```
src/
  main.py                     # Mode 2 (on-demand) entrypoint; wires the cycle
  scheduler.py                # Mode 1 (scheduled) entrypoint
  persistence/
    __init__.py
    db.py                      # connection factory, migration runner
    schema.sql                 # one table-group per owning module (ADR-005 §7)
  mod01_market_data/            # MOD-01
  mod02_market_context/         # MOD-02
  mod03_evidence/                # MOD-03
  mod04_validation/              # MOD-04
  mod05_recommendation/          # MOD-05
  mod06_governance/               # MOD-06
  mod07_human_gate/               # MOD-07
  mod08_attribution/              # MOD-08
  mod09_portfolio/                 # MOD-09
  mod10_audit/                     # MOD-10
  mod11_activation/                # MOD-11
```

Each `modNN_*` package corresponds to exactly one constitutional module (MB-02). No package may be merged, split, or renamed across constitutional identity. Each package exposes a single public module-level interface (`__init__.py` re-exports) — this is the "published output contract" referenced by ADR-004 RULE MB-04.

### 2.3 Naming Discipline

Package names embed `modNN` so that the boundary-enforcement linter (Section 3.2) can pattern-match module identity directly from the import path without a side-table. This is an implementation calibration (ADR-007 P-12 — replaceable), not a constitutional rule.

---

## SECTION 3 — DEVELOPMENT ARCHITECTURE

### 3.1 Package/Dependency Structure

- Each `modNN_*` package may import from another `modNN_*` package **only** if that edge appears in ADR-002 §6.1 (as amended by ADR-003B) — see Allowed Edge Table below.
- Each `modNN_*` package may import from `persistence` only for **its own owning table-group** (enforced by convention: `persistence.db.get_connection(module="MOD-XX")` returns a connection scoped to that module's tables — Section 4.3).
- `mod10_audit` may be imported by every module (write-only client). `mod10_audit` imports nothing from any `modNN_*` package (DEP-03).
- No package imports `main` or `scheduler` (those are composition roots only).

**Allowed Edge Table** (from ADR-002 §6.1 / ADR-006 §3.2, restated as import-direction pairs):

| Importer | May import from |
|---|---|
| mod01 | persistence, mod10 |
| mod02 | mod01, persistence, mod10 |
| mod03 | mod01, mod02, persistence, mod10 |
| mod04 | mod01, mod03, persistence, mod10 |
| mod05 | mod01, mod02, mod03, mod04, mod09, mod06 (gating signal only), persistence, mod10 |
| mod06 | mod02, mod09, persistence, mod10 |
| mod07 | mod03, mod05, mod06, mod09, persistence, mod10 |
| mod08 | mod01 (time-delayed, CAP-21 only), mod02 (time-delayed, CAP-21 only), mod07, persistence, mod10 |
| mod09 | persistence, mod10 |
| mod10 | persistence (audit table-group only) |
| mod11 | persistence, mod10 (records activation events) |

Any import not in this table fails the boundary test (Section 3.2).

### 3.2 Boundary Enforcement Mechanism (T-14, mandatory co-selection)

`tests/architecture/test_boundaries.py`:
- Walks `src/` with `ast`, extracts every `import` / `from ... import` statement.
- For each `modNN_*` source file, resolves the imported package's `modNN` prefix (if any).
- Asserts the (importer, imported) pair is in the Allowed Edge Table above.
- Additionally asserts the ten FORB-01..FORB-10 prohibitions as named, individually-failing assertions (e.g., `test_forb01_mod08_has_no_write_edge_to_mod01_through_mod06`), so a violation reports the **constitutional rule name**, not just "edge not allowed."
- Runs as a normal `pytest` test — "CI gate" at this stage means "must pass before any commit is considered complete," enforced by running it in Phase 1 and on every subsequent phase.

### 3.3 Testing Structure

- `tests/unit/modNN_*/` mirrors `src/modNN_*/` — one test module per capability file.
- `tests/integration/test_cycle.py` — runs a full Mode 2 cycle against a temporary SQLite file and asserts: activation record exists, audit records exist for every capability invoked, a recommendation (or null-state) reaches MOD-07, a human decision is captured, attribution and audit records close the cycle (ADR-006 §2.3).
- `tests/architecture/` — Section 3.2.

### 3.4 Module Ownership Boundaries (internal)

Within each `modNN_*` package, one file per owned capability (e.g., `mod01_market_data/cap01_ingestion.py`, `cap02_cross_verification.py`, ...). This satisfies ADR-004 RULE MB-01 ("an implementation unit that represents one SADR capability and nothing else") while allowing capabilities to share private helpers within the package.

---

## SECTION 4 — PERSISTENCE BOOTSTRAP

### 4.1 Initialization Sequence

1. `persistence/db.py` opens (or creates) `data/system.db` — a single embedded SQLite file (ADR-007 §3, D-a).
2. `persistence/db.py` opens (or creates) `data/audit.db` — a **second, physically separate** SQLite file for MOD-10, satisfying "audit must be physically isolated from operational state" (ADR-007 §7, A-a) and enforcing DEP-03 even at the storage layer (a capability cannot accidentally `JOIN` into audit because it is a different database file/connection entirely).
3. `schema.sql` (operational) is applied to `system.db` idempotently (`CREATE TABLE IF NOT EXISTS`) — one table-group per owning module (MOD-01, MOD-02, MOD-06, MOD-07, MOD-08, MOD-09, MOD-11; MOD-03/04/05 outputs that are cycle-only are not persisted as tables, only as in-memory dataclasses, per ADR-005 §6/§7).
4. `audit_schema.sql` is applied to `audit.db`: a single append-only `audit_log` table with `UPDATE`/`DELETE` revoked via SQLite triggers that raise on any `UPDATE`/`DELETE` against `audit_log` (the embedded-engine realization of "revoked UPDATE/DELETE grants," ADR-007 §7), plus a `prev_hash`/`record_hash` column pair realizing the per-record hash-chain.
5. `persistence/db.py:get_connection(module)` returns a connection bound to `system.db` for all modules except MOD-10, and to `audit.db` for MOD-10. This is the single chokepoint through which Section 3.1's ownership rule is mechanically realized.

### 4.2 Ownership Boundaries (schema)

| Table | Owning Module | Writers |
|---|---|---|
| `portfolio_state`, `trade_ledger` | MOD-09 | MOD-09 only |
| `governance_state` (4 independent rows/flags, no shared row) | MOD-06 | MOD-06 only (one capability per flag — CAP-24/25/26/27 — write only their own row) |
| `human_decisions` | MOD-07 | MOD-07 only |
| `attribution_records` | MOD-08 | MOD-08 only |
| `activation_log` | MOD-11 | MOD-11 only |
| `market_baselines`, `eligible_universe` | MOD-01 | MOD-01 only |
| `regime_state`, `drift_metrics` | MOD-02 | MOD-02 only |
| `audit_log` (separate DB) | MOD-10 | every module, append-only |

`governance_state` is **four independent rows** keyed by halt-state ID (1–4), each with its own `entered_at`/`exited_at`/`condition` columns — never a single enum column — directly realizing GOV-02/DEP-11 (no shared state variable across halt states) at the schema level.

### 4.3 Migration Approach

Given personal-tool scale (SDM-CONST-04) and a single embedded file, migrations are **idempotent forward-only DDL scripts** (`CREATE TABLE IF NOT EXISTS`, `ALTER TABLE ... ADD COLUMN` guarded by `PRAGMA table_info` checks) applied on every startup by `persistence/db.py`. No migration framework is introduced (minimum sufficiency, ADR-007 rule 2) — this is a replaceable calibration (P-12); a framework may be substituted later without architectural change.

### 4.4 State Bootstrap (first run)

On first run with no `data/system.db`:
- MOD-09 `portfolio_state` is seeded with a single row: zero positions, zero drawdown, ₹5,000 capital (SDM-CONST-04).
- MOD-06 `governance_state` is seeded with all four halt states `inactive`.
- No other table requires seed data — MOD-01 through MOD-05 outputs are produced on first activation.

### 4.5 Recovery Sequence (ADR-006 §8.4)

`main.py` startup, before any cycle work:
1. Read `governance_state` — if State 1 (Governance Halt) row is `active`, the process starts in a halt-aware mode: MOD-05 issuance is gated, but MOD-01–04, MOD-08, MOD-09, MOD-10, MOD-11 still run normally (GOV-01).
2. Read `portfolio_state` — if absent, refuse to start MOD-05 (HAP-01/INV-07 precondition); MOD-01–04 may still run.
3. Re-run CAP-31/CAP-23/CAP-19 detectors against recovered state to refresh States 2/3/4 (ADR-005 §8.3).
4. Proceed to normal activation handling.

---

## SECTION 5 — EXECUTION BOOTSTRAP

### 5.1 Startup Path

`main.py`:
1. Parse CLI args (`--mode {on-demand,scheduled}`, default `on-demand` → Mode 2).
2. `persistence.db.init()` — Section 4.1–4.5.
3. `mod11_activation.activate(mode=..., trigger=...)` — writes `activation_log` row, writes audit record (CAP-28).
4. Returns a `cycle_id`. `main.py` then calls the pipeline functions directly, in the fixed order below — **this sequence is the dependency graph, not orchestration by MOD-11** (ACT-01): MOD-11's job ends at step 3.

### 5.2 Activation Path (the call sequence realizing Stage 2)

```
cycle_id = mod11_activation.activate(mode, trigger)

verified = mod01_market_data.run(cycle_id)        # CAP-01..04, CAP-14; CAP-02 gate raises if cross-verify fails
context  = mod02_market_context.run(cycle_id, verified)            # CAP-05, CAP-06
evidence = mod03_evidence.run(cycle_id, verified, context)           # CAP-07, CAP-08, CAP-09
validated = mod04_validation.run(cycle_id, evidence)                  # CAP-10 gate, CAP-11
portfolio = mod09_portfolio.get_state()                                # CAP-29 (read)
halts     = mod06_governance.get_active_halts()                        # current flags (read)
package   = mod05_recommendation.run(cycle_id, validated, context, portfolio, evidence.conflict_flags, halts)
                                                                           # CAP-12,13,15,16,17,20 — gated by `halts`
decision  = mod07_human_gate.present_and_capture(cycle_id, package, evidence.advisory_section, halts, portfolio)
                                                                           # CAP-18
mod08_attribution.observe(cycle_id, package, decision)                  # CAP-21, CAP-22
```

Each `run(...)`/`activate(...)`/`observe(...)` call writes its own audit record(s) via `mod10_audit.record(...)` internally — `main.py` never calls `mod10_audit` directly except to read the cycle-complete confirmation for the final printed summary.

### 5.3 Execution Path — Blocking Gates

- **CAP-02 (in `mod01_market_data.run`)**: if cross-verification across the (≥2, currently stub) sources disagrees beyond tolerance, `run()` raises `CrossVerificationFailure`. `main.py` catches this, writes an audit record, and **halts the cycle before MOD-02 is called** — Required Ordering 2 / DEP-06 realized as a Python exception that aborts the call chain before any downstream call exists in the stack.
- **CAP-10 (in `mod04_validation.run`)**: signals failing walk-forward validation are filtered out of the returned `validated` set, not raised as exceptions (a signal failing validation is a normal outcome, not a system failure) — but `mod05_recommendation.run` structurally cannot receive un-validated signals because `validated` is the only signal-shaped argument it accepts.
- **CAP-18 (in `mod07_human_gate.present_and_capture`)**: blocks on `input()` (CLI) until the human responds. No timeout. No default branch that proceeds without a captured decision.

### 5.4 Continuous / Cycle-Independent Processes (Section 2.4, INV-14)

Implemented as a **second entrypoint**, `scheduler.py`, run as a separate long-lived process (still single-process-per-concern, satisfying D-a — "single host, single process" refers to the deployable unit, not a literal single OS thread):
- Loop: every N seconds, call `mod06_governance.run_detectors()` (CAP-19, CAP-23, CAP-31) against current `portfolio_state` and market context; update `governance_state` rows independently; write audit records.
- This loop never calls `mod05_recommendation` and is never paused by any halt state (GOV-01).
- Mode 1 (scheduled activation) is realized by `scheduler.py` also checking a configurable schedule and invoking `main.run_cycle(mode="scheduled", trigger="schedule")` when due.
- Mode 3 (event-driven) is realized by `mod06_governance.run_detectors()` calling `mod11_activation.activate(mode="event_driven", trigger=<event>)` → `main.run_cycle(...)` in-process when a governance/risk event is detected — this is the bounded MOD-06 → MOD-11 in-process signal (E-a, Section 8.1 of ADR-007), implemented as a direct function call carrying only `(event_type, cycle_trigger_id)`, never raw governance state.

### 5.5 Shutdown Path

- `main.py`'s on-demand cycle is request/response — it exits after step in Section 5.2 completes (success, gate failure, or human decision captured).
- `scheduler.py` handles `SIGTERM`/`SIGINT` by finishing the current detector pass, writing a final audit record (`activation_log`/governance audit), and exiting — no partial writes to `governance_state` or `audit_log` (SQLite transaction per detector pass).
- No state requires explicit "shutdown" persistence beyond normal transaction commit, because all cross-cycle-persistent state (Section 4.2) is committed synchronously at the point of change, not buffered.

---

## SECTION 6 — AUDIT BOOTSTRAP

### 6.1 Immutable Audit Foundation

`mod10_audit/audit.py` exposes exactly one write function:

```python
def record(module: str, capability: str, cycle_id: str | None, event_type: str, payload: dict) -> None
```

- Computes `record_hash = sha256(prev_hash || canonical_json(payload) || module || capability || event_type || timestamp)`.
- Inserts into `audit_log` (in `audit.db`) with `prev_hash` = the previous row's `record_hash` (genesis row uses a fixed constant).
- `audit.db` has `CREATE TRIGGER` guards that raise `sqlite3.IntegrityError` on any `UPDATE` or `DELETE` against `audit_log`, realizing AUD-02 structurally rather than by convention alone.

### 6.2 Write-Only Audit Flow

- Every `modNN_*.run(...)`/equivalent function calls `mod10_audit.record(...)` at minimum once on entry (capability invoked) and once on completion (capability result summary) — AUD-01.
- `mod10_audit` exposes **no read function importable by any `modNN_*` package** (DEP-03). A separate, human-only function `mod10_audit.review(filters) -> Iterator[AuditRecord]` exists but is called **only** from a `tools/audit_review.py` CLI script that is not imported by any `modNN_*` package — enforced by the boundary test (Section 3.2) treating `mod10_audit.review` as a forbidden import target from any `src/modNN_*` path.

### 6.3 Audit Isolation

- Physical: `audit.db` is a separate file from `system.db` (Section 4.1).
- Logical: `mod10_audit` imports nothing from `mod01`..`mod09`/`mod11` (no inbound data dependency that could become a read-back path).
- Verification: `tools/audit_review.py` includes a `--verify-chain` mode that re-walks `audit_log` recomputing `record_hash` from `prev_hash` and payload, confirming no row was altered, deleted, or reordered (ADR-005 §8.1, ADR-007 §7).

---

## SECTION 7 — VERTICAL SLICE SELECTION

### 7.1 Selected Slice

**"One on-demand cycle, one symbol, CLI presentation, full audit trail."**

Concretely:
- MOD-11: Mode 2 activation triggered by `python -m src.main`.
- MOD-01: two **stub vendor adapters** returning the same fixed OHLCV fixture for one symbol (e.g., RELIANCE) with deliberately matching values so CAP-02 passes; CAP-03/04/14 are pass-through identity transforms on the fixture (no real corporate actions in the fixture).
- MOD-02: CAP-05 returns a constant regime label (`"NEUTRAL"`) computed from a trivial rule (e.g., 20-day SMA slope sign) — real computation, minimal sophistication.
- MOD-03: CAP-07 computes one real technical signal (e.g., SMA crossover) from the fixture; CAP-08 returns an empty supplementary set; CAP-09 returns "no conflict."
- MOD-04: CAP-10 performs a minimal walk-forward split (e.g., 2 folds) on the fixture and a real pass/fail check; CAP-11 computes a real (if simplified) t-stat.
- MOD-05: CAP-12 computes confidence from CAP-07 signal strength + CAP-11 t-stat (technically pure, VAL05-01); CAP-13 computes EV using MOD-09's seeded portfolio state; CAP-15/16 rank and allocate (or CAP-17 declares null-state if the single signal fails validation); CAP-20 produces a trivial exit suggestion if a position exists.
- MOD-06: `governance_state` read (all four flags inactive on first run) — gating signal is "no halt," issuance proceeds.
- MOD-07: CLI prints the Open Menu (ranked opportunities + sentiment section + halts + drawdown) and reads `approve`/`reject` from stdin.
- MOD-09: seeded portfolio state, read-only this cycle.
- MOD-08: records System Alpha placeholder + Human Override Delta (none, since no prior recommendation to compare).
- MOD-10: every step above writes audit records; `tools/audit_review.py --verify-chain` confirms the chain after the run.

### 7.2 Why This Slice

- It is the **smallest cycle that touches all eleven modules** and both blocking-gate-adjacent paths (CAP-02 passes, CAP-10 runs a real check) without requiring real broker, real vendor, or real NLP integrations — all of which are Optional/Unjustified at this stage (ADR-007 §8.3, §8.4).
- It exercises the **human gate for real** (a human types `approve`/`reject`), proving HAP-01/HAP-02 are implemented as actual blocking I/O, not a mock.
- It produces a **non-empty, verifiable audit chain**, proving AUD-01/AUD-02/the audit isolation model end-to-end.
- It is implementable without the boundary-enforcement layer (Phase 1) having anything non-trivial to check until Phase 2 — so Phase 1's tests are exercised meaningfully starting Phase 2.

---

## SECTION 8 — IMPLEMENTATION PLAN

### Phase 1 — Foundation (working software: "the system boots, persists, and audits nothing happening")

- `persistence/db.py`, `schema.sql`, `audit_schema.sql` (Sections 4.1–4.4).
- `mod10_audit/audit.py` (Section 6.1).
- `mod11_activation/activation.py` (CAP-28 — writes `activation_log` + audit record only).
- `tests/architecture/test_boundaries.py` with the Allowed Edge Table (Section 3.1) and ten named FORB tests — passing trivially since only MOD-10/MOD-11/persistence exist.
- `main.py` that calls `mod11_activation.activate(...)` and prints the resulting `cycle_id`.

**Exit criterion:** `python -m src.main` prints a `cycle_id`; `data/system.db` and `data/audit.db` exist; `tools/audit_review.py --verify-chain` reports a valid 1-2 record chain; `pytest tests/architecture` passes.

### Phase 2 — Research Pipeline (working software: "the system produces a recommendation or a null-state from real data")

- `mod09_portfolio/portfolio.py` (CAP-29, seeded state).
- `mod01_market_data/` (CAP-01..04, CAP-14 with stub adapters + CAP-02 gate).
- `mod02_market_context/` (CAP-05, CAP-06).
- `mod03_evidence/` (CAP-07, CAP-08, CAP-09).
- `mod04_validation/` (CAP-10 gate, CAP-11).
- `mod05_recommendation/` (CAP-12, 13, 15, 16, 17, 20).
- `mod06_governance/` minimal: `get_active_halts()` reading seeded `governance_state` (all inactive); detectors deferred to Phase 3.
- Extend `main.py` to run the full Section 5.2 sequence up to `package` (no MOD-07/MOD-08 yet) and print the recommendation package or null-state declaration as JSON.

**Exit criterion:** `python -m src.main` prints either a ranked opportunity (with confidence, EV, allocation) or an explicit `"null_state": true` declaration; CAP-02/CAP-10 gate tests in `tests/integration` demonstrate both pass and (with a deliberately mismatched fixture) fail paths; boundary tests still pass with all eleven... ten modules' imports now real.

### Phase 3 — Human Gate, Attribution, Governance Closure (working software: "a complete recommendation cycle with human decision and audit closure")

- `mod07_human_gate/` (CAP-18 CLI Open Menu + decision capture into `human_decisions`).
- `mod08_attribution/` (CAP-21, CAP-22 post-gate observers).
- `mod06_governance/` detectors (CAP-19, CAP-23, CAP-31) + halt-state entry/exit logic (CAP-24..27) as independent functions/rows.
- `scheduler.py` (Section 5.4) running detectors continuously and supporting Mode 1/Mode 3.
- Recovery sequence (Section 4.5) wired into `main.py` startup.

**Exit criterion:** `python -m src.main` runs the full Section 5.2 sequence end-to-end: prints the Open Menu, accepts `approve`/`reject` from stdin, writes `human_decisions` and `attribution_records`, and `tools/audit_review.py --verify-chain` shows a complete, unbroken chain covering every capability invoked in the run. `scheduler.py` runs independently and can be killed mid-detector-pass without corrupting `governance_state` (verified by re-running and observing consistent state). Simulating a State-1 halt (manually setting the `governance_state` row) and re-running `main.py` demonstrates MOD-05 issuance is blocked while MOD-01–04/08/09/10/11 still execute and audit normally (GOV-01 demonstration).

---

## SECTION 9 — WORKING SOFTWARE REQUIREMENT

At the end of Phase 3, the following is true and demonstrable by running commands, not reading documents:

1. `python -m src.main` — system boots, recovers/initializes state, runs a complete recommendation cycle, presents an Open Menu, captures a human decision.
2. `data/system.db` contains current portfolio state, governance flags (four independent rows), the captured human decision, and attribution records.
3. `data/audit.db` contains an immutable, hash-chained record of every capability invocation in the run; `tools/audit_review.py --verify-chain` confirms integrity.
4. `python -m src.scheduler` — runs continuous governance detectors independently of any cycle, demonstrating INV-14.
5. `pytest tests/architecture` — passes, demonstrating the boundary-enforcement co-requirement (T-14) is live, not aspirational.
6. Manually activating Governance Halt (State 1) and re-running `python -m src.main` demonstrates recommendation issuance is blocked while every other module still runs and audits (GOV-01/AF 6.1 — the constitutional property hardest to get "accidentally right").

No phase is complete while its exit criterion is undemonstrated. Documentation updates to this file do not advance phase completion; only the commands above do.

---

*IMP-001 derives its authority from ADR-000 through ADR-007 (FROZEN). It introduces no architectural change. Every structural choice herein (file layout, migration approach, hash-chain mechanism, CLI presentation) is a replaceable implementation calibration per ADR-000 P-12 and may be substituted without amendment to this document's Section references, provided the referenced constitutional properties remain satisfied.*

*End of IMP-001_IMPLEMENTATION_BOOTSTRAP*

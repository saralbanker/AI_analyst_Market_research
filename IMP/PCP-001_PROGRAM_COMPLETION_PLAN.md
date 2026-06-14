# PCP-001 — PROGRAM COMPLETION PLAN

**Document Type:** Program Completion Plan (PLAN artifact — REVIEW gate pending, no EXECUTE authorized)
**Mission:** Program Completion Optimization → Operational Readiness → Paper-Trading Activation
**Authority basis (inherited, unmodified):** SDM_V2.3 ▸ VAL05 ▸ SADR_V2.1 ▸ ARCHITECTURE_FOUNDATION_V1 ▸ ADR-000..007 ▸ IMP-001 ▸ VER-001 ▸ EXT-001.
**Constraint:** Architecture FROZEN. Technology FROZEN. Capability FROZEN. No ADR/SDM/SADR/governance/ownership/boundary file may change. Every item below is additive (new `src/adapters/*`, new tests, `tools/*`, config, gitignore) or a bug-fix inside an already-owned module — never a new architectural decision.
**Date:** 2026-06-13

---

## 01 — Current Program Assessment

The certified truth-state was **independently re-verified against the working tree**, not taken on faith. Findings:

**Confirmed accurate (matches VER-001 / EXT-001):**
- `pytest tests/architecture` → **6 passed**. Boundary/Allowed-Edge enforcement is real and rejects out-of-authority edges (re-confirmed by reading `tests/architecture/test_boundaries.py`).
- Config validation (`src/config.py`), startup wiring in `main.py`/`scheduler.py`, audit hash-chain, human-gate blocking read, governance-halt independence, VAL05 sentiment isolation, paper-trade bookkeeping, metrics, daily report, attribution journal, and CAP-02/CAP-10 blocking gates are all present and consistent with the reports.
- Adapter framework exists: `MarketAdapter`/`NewsAdapter`/`MacroAdapter` protocols, always-available stubs, vendor skeletons, factory fallback. No live network calls anywhere. Stub-mode full cycle runs end-to-end.

**Scope reality:** ~2,471 LOC Python, single developer, 11 modules + adapters/tools. The vertical slice is single-symbol (RELIANCE), fixture-fed.

**New findings not captured in the prior reports (the actual remaining work):**

| # | Finding | Severity | Why it matters to activation |
|---|---|---|---|
| **F-A** | **Factory selects adapters by *behaviour-probe*, not config-presence.** `factory.py` calls `fetch_ohlcv("__probe__")` and only catches `AdapterNotConfigured`/`NotImplementedError`. | **CRITICAL** | The moment the HTTP body is written, every factory call fires a **real network request for a bogus symbol**, and any live auth/network error (not the two caught types) **propagates and crashes startup**. Credential arrival would therefore *require code redesign* — a direct violation of the CREDENTIAL_READY_CONSTITUTION ("No redesign permitted"). |
| **F-B** | **`portfolio_state.drawdown_pct` is never updated by paper trading.** `cap_paper_trading.py` writes `capital`/`positions_json` but not `drawdown_pct`; `run_drawdown_detector` gates State 3 (Conditional Suspension) on `drawdown_pct`, which stays `0.0`. | **CRITICAL** | The drawdown governance halt is **dead during paper trading** — the exact condition it exists to catch (equity decline) can never trigger it. Defeats a core reliability/governance control precisely when paper P/L is at risk. |
| **F-C** | **Zero functional test coverage.** `tests/unit/` and `tests/integration/` contain only empty `__init__.py`. Only the 6 architecture tests exist. | **HIGH** | The activation gate "**Validation passes → Activation**" has *nothing functional to run*. Recommendation math, walk-forward, paper P/L, metrics, and config are unverified by any repeatable suite. |
| **F-D** | **No credential-free adapter completion path.** The `fetch_*` bodies are `NotImplementedError` with no recorded-response fixtures or contract tests. | **HIGH** | EXT-001 ADAPTER_COMPLETION_STRATEGY requires implementations be *completed and tested without real credentials*. Today that is impossible — so credential arrival ≠ config-only. |
| **F-E** | **`src/.env` is untracked but NOT gitignored**, and `FINNHUB_API_KEY` already holds a value. | **MEDIUM** | A stray `git add -A` commits a live secret. No committed `.env.example` template exists. |
| **F-F** | Governance completeness gaps: CAP-26 (State 2 lockout *entry*) and CAP-24 (State 4 hard-halt fault source) are unimplemented (acknowledged in VER-001 §13). | LOW (defer) | Off the first-activation path; needed before *profitability validation*, not before *boot*. |

**Verdict:** The system is **boot-ready and stub-paper-trading-ready today**, but it is **not credential-ready** (F-A), its **drawdown governance control is inert under paper trading** (F-B), and it **cannot demonstrate "validation passes"** (F-C/F-D). These four are the entire meaningful remaining body of work.

---

## 02 — Remaining Work Inventory

Classified strictly by the GOVERNING_QUESTION ("if credentials arrived tomorrow, what would still block immediate paper trading?").

**MANDATORY (blocks credential-ready activation or its validation):**
- **M1 — Config-presence adapter selection (fixes F-A).** Replace the probe in `factory.py` with non-empty-credential checks; construct the vendor adapter only, never call it to decide. Add a `MARKET_DATA_SOURCE`-style explicit override is *not* required — env-var presence is sufficient and matches `config.py` semantics.
- **M2 — Paper-equity drawdown computation (fixes F-B).** Within MOD-09 (OWN-01 preserved), recompute `drawdown_pct` from peak-to-current paper equity (capital + mark-to-market) on each `open/close`/mark. Makes State 3 live.
- **M3 — Functional test suite (fixes F-C).** `tests/unit`: confidence/EV/ranking/allocation, walk-forward agreement, significance, data-quality rejection cases, config validation, paper P/L arithmetic, metrics. `tests/integration`: full clean-DB cycle (approve + reject + governance-halt null-state), audit-chain verify, drawdown→State-3 transition (depends on M2).
- **M4 — Credential-free adapter completion (fixes F-D).** Capture representative vendor JSON as `tests/fixtures/`; implement the three `fetch_*` parse-and-map bodies against a swappable transport (real HTTP injected at call, parse logic pure/testable); contract tests asserting vendor JSON → canonical shape that passes `validate_bars`. Outcome: credential arrival = config only.

**RECOMMENDED (cheap, high reliability/governance ROI, do alongside mandatory):**
- **R1 — Secret hygiene (fixes F-E).** Add `src/.env` to `.gitignore`; commit `src/.env.example` (keys only, no values). Rotate the present Finnhub key if it was ever at risk.
- **R2 — Activation runbook (single doc).** One `CLAUDE.md` at repo root: the exact credential-injection → validation → activation → paper-trading sequence and the go/no-go checklist. Replaces ad-hoc tribal knowledge.

**DEFERRED (not on first-activation path; schedule before profitability validation):**
- **D1** — CAP-26 lockout entry + CAP-24 hard-halt fault source (F-F).
- **D2** — Macro adapter wiring into MOD-02 (additive; no consumer exists yet).

**ELIMINATED (anti-busywork — explicitly not done):**
- Multiple `*_CLAUDE.md` files, specialist agents, new ADRs, new workflows, governance frameworks, multi-agent review pipelines, any PostgreSQL/Supabase/Convex migration, any broker/order-routing work. None move the program toward credential-ready paper trading; all add maintenance/token/complexity cost. See §11.

---

## 03 — Constitutional Enforcement Strategy

Enforcement already exists and is sufficient; **do not add governance, harden the existing layer with the missing tests.**
- **Boundary authority (ADR-004):** `tests/architecture` is the enforcement mechanism — it already fails on disallowed edges. **Rule:** every PCP change must keep it at 6/6; M1–M4 add no module-to-module edges (`adapters`, `tools`, `config` are outside the `MODULES` walk; M2 lives inside MOD-09).
- **VAL05 (sentiment isolation):** Protect by a regression test (part of M3) asserting `compute_confidence`/`compute_ev`/`rank_candidates`/`compute_allocation` accept no sentiment-derived argument and that `grep` finds no sentiment data-path into MOD-05.
- **Audit terminality (AUD-01/02):** unchanged; M3 integration test re-runs `--verify-chain` after every scenario.
- **Human authority (CAP-18):** untouched; no flag added that bypasses the blocking read.
- **Change discipline:** PLAN → REVIEW → EXECUTE. This document is PLAN. No code is written until REVIEW approves.

---

## 04 — AI Governance System Design (minimum viable)

The constitutional answer to CLAUDE_FILE_ANALYSIS / AGENT_ANALYSIS / WORKFLOW_ANALYSIS for a 2.5k-LOC single-owner repo:

- **CLAUDE files:** **One.** A single root `CLAUDE.md` (the §02-R2 runbook + invariants: "architecture frozen, additive-only, keep `tests/architecture` green, never commit `src/.env`, sentiment never numeric"). Separate IMPLEMENTATION/VERIFICATION/RESEARCH CLAUDE files would duplicate the ADRs and the runbook → **rejected as overlap/maintenance burden.**
- **Specialist agents:** **Zero.** No task here has a unique, repeatable, measurable responsibility that a human + the existing test gates don't already cover. Agents would be capability work without measurable impact → forbidden by ANTI_BUSYWORK_CONSTITUTION.
- **Workflows:** **One, lightweight** — the activation go/no-go checklist (a section in `CLAUDE.md`, not an engine). Failure risk is concentrated entirely at credential-injection; that single checkpoint is the only place a workflow earns its keep.

Net: **1 doc, 0 agents, 1 checklist.** Stronger and fewer, per AI_GOVERNANCE_REQUIREMENTS.

---

## 05 — Paper Trading Operations Plan

Operating model once M1–M4 land (no broker, human is sole execution actor — unchanged):
1. **Cycle:** `python -m src.main` (on-demand) or `scheduler.py` (Mode 1/3) produces the Open Menu; human approves/rejects at the blocking gate.
2. **Bookkeeping:** on a human-approved opportunity, the operator records the paper fill via `mod09_portfolio.open_position(...)`; exits via `close_position(...)`. (These remain deliberate human-invoked bookkeeping calls — EXT-001 FORBIDDEN_ACTIONS preserved.)
3. **Mark-to-market & governance:** scheduler's detector pass reads `drawdown_pct` — now live (M2) — and fires State 3 if paper equity breaches 15%, auto-exits below 10%.
4. **Measurement:** `tools/metrics.py` (expectancy, win rate, profit factor, max DD) + `tools/daily_report.py` daily.
5. **Audit:** every step writes to the append-only chain; `tools/audit_review.py --verify-chain` is the daily integrity check.

**Data source during validation:** fixture/stub until credentials arrive; then config-only switch to live (M1 guarantees no redesign). The full vertical slice — recommendation → human gate → paper P/L → metrics → report → audit — runs *today* against fixtures, which is the correct way to validate operations before live data.

---

## 06 — Profitability Improvement Framework

Profitability is **unproven and must be discovered, not assumed.** The measurement system to discover it is largely built (attribution journal, metrics, daily report); the gap is **trustworthy inputs and a baseline.**
- **Expectancy as the primary discovery metric** (`tools/metrics.py`) computed solely from `paper_trades` — already correct.
- **Attribution separation** (System Alpha vs Human Override Delta) is recorded per cycle — this is the lever that tells you whether edge comes from the model or the human. Protect it with M3 tests.
- **What M2 adds:** without live drawdown, risk-adjusted return is unmeasurable; M2 makes max-DD real, enabling expectancy-per-unit-risk.
- **What M4 adds:** until adapters deliver real bars, every metric is computed on synthetic data — *operationally valid, statistically meaningless for profitability*. M4 is the precondition for any real expectancy reading.
- **Discovery protocol:** run ≥N cycles in paper mode, require expectancy > 0 with a minimum sample before declaring any edge; null-state and rejection cycles count. No profitability claim is permitted from fixture data.

---

## 07 — Reliability Improvement Framework

Ranked by measurable reliability gain per unit cost:
1. **M2 (drawdown live)** — restores an inert safety control. Highest reliability ROI.
2. **M3 (functional tests)** — converts "works once by inspection" into "verified every change." Directly raises governance/decision/recovery reliability and is the gate referenced by every roadmap stage.
3. **M1 (config-presence selection)** — eliminates a startup-crash-at-credential-time class of failure.
4. **R1 (secret hygiene)** — removes a credential-leak failure mode.
5. **D1 (CAP-26/CAP-24)** — completes governance state-machine coverage; scheduled before profitability validation, not before boot.

Data reliability (CAP-02 cross-verify + CAP-data-quality) is already strong; M4's contract tests extend it to the live-vendor parse boundary.

---

## 08 — Execution Roadmap (sequenced, with stage gates)

```
Current_State
  → Operational_Readiness        (M1, M2, M3, M4, R1, R2)
  → Credential_Acquisition       (external; owner obtains Upstox/Finnhub/TE keys)
  → Credential_Validation        (config-only inject; startup diagnostics + adapter smoke)
  → External_Data_Activation     (factory auto-selects real adapters; M1 guarantees no redesign)
  → Paper_Trading                (full slice on live data)
  → Performance_Measurement      (metrics + daily report accumulate)
  → Profitability_Validation     (expectancy > 0 over min sample; D1 governance complete)
  → Production_Readiness         (out of current scope)
```

| Stage | Objectives | Dependencies | Exit Criteria | Risks |
|---|---|---|---|---|
| **Operational Readiness** | Land M1–M4, R1, R2 | None (no credentials needed) | `pytest tests/` green incl. new unit+integration; `tests/architecture` still 6/6; clean-DB cycle + drawdown→State-3 demo pass; `.env` gitignored + `.env.example` committed; runbook merged | Scope creep into architecture (mitigate: additive-only rule, REVIEW gate) |
| **Credential Acquisition** | Owner obtains keys | Operational Readiness done | Keys present in `src/.env` | External/timeline only |
| **Credential Validation** | Inject + validate, no code change | M1, M4 | `config.diagnostics` shows keys `set`; adapter smoke test returns real bars passing `validate_bars` | A populated key auto-activates live calls (mitigate: M1 explicit, smoke test first) |
| **External Data Activation** | Live data flows through mod01/mod03 | Credential Validation | One full live cycle produces an Open Menu from real bars; audit chain verifies | Vendor schema drift (mitigate: M4 contract tests pin the mapping) |
| **Paper Trading** | Human-gated paper fills on live data | Activation | ≥1 open+close round-trip with correct P/L + audit | Operator process error (mitigate: R2 checklist) |
| **Performance Measurement** | Accumulate metrics | Paper Trading | Daily reports + metrics over running window | Insufficient sample |
| **Profitability Validation** | Discover edge | Measurement + D1 | Expectancy > 0 over predefined min sample, with attribution split | Overfitting to small sample (mitigate: min-sample rule) |

---

## 09 — Prioritized Execution Queue

Order chosen so each item unblocks the next and the credential-ready guarantee is established before any live work:

1. **M1 — config-presence adapter selection** (smallest, removes the redesign-at-credential risk; unblocks M4 testing cleanly).
2. **M4 — adapter parse bodies + recorded-fixture contract tests** (delivers "credential = config only"; testable without keys).
3. **M2 — paper-equity drawdown** (restores State 3; required by an M3 integration test).
4. **M3 — unit + integration suite** (locks M1/M2/M4 and the existing slice behind a repeatable gate).
5. **R1 — `.env` gitignore + `.env.example`** (do with M1; one commit).
6. **R2 — root `CLAUDE.md` activation runbook** (last; documents the now-stable sequence).

Deferred (post-activation, pre-profitability): **D1** (CAP-26/CAP-24), then **D2** (macro wiring) only if/when a consumer is specified.

---

## 10 — Credential-Ready Activation Strategy

The end-state the whole plan serves: **Credential_Arrival → Secret_Injection → Validation → Activation → Paper_Trading, with no redesign.**

- **Injection:** owner fills `src/.env` values only (keys already declared as `OPTIONAL_KEYS` in `config.py`). No code touched.
- **Selection (M1):** `get_*_adapter()` checks the required env vars are non-empty → returns the vendor adapter; else the stub. **No probe call, no behaviour-based branching.** This is the single change that makes the constitution's "no redesign" literally true.
- **Transport (M4):** `fetch_*` already contains tested parse-and-map logic; only the live HTTP transport is exercised for the first time at activation, and a smoke test precedes the first real cycle.
- **Validation:** `config.diagnostics()` confirms keys `set`; an adapter smoke test confirms real bars pass `validate_bars` and CAP-02 cross-verification before a full cycle runs.
- **Guarantee:** after M1+M4, the delta between stub-mode and live-mode is **environment values only** — zero source edits, zero architectural decisions.

---

## 11 — Governance Complexity Analysis

Applying the PROGRAM_COMPLETION_FILTER to every candidate, what was **eliminated** and why:

| Rejected candidate | Reason (filter) |
|---|---|
| Multiple `*_CLAUDE.md` files | Overlap with ADRs + runbook; maintenance cost > readiness ROI |
| Specialist agents / multi-agent review | No unique measurable responsibility; capability work, forbidden |
| New ADRs / governance frameworks | Architecture frozen; governance already enforces via tests; bloat |
| Workflow engines | Single failure point (credential injection) is covered by one checklist |
| DB migration (Postgres/Supabase/Convex) | Technology frozen; SQLite verified sufficient |
| Broker / order-routing / approval automation | Violates the Ultimate System Boundary; FORBIDDEN |

**Retained governance footprint:** the existing 6 architecture tests + new functional tests (M3) + 1 runbook + 1 checklist. This is the minimum that enforces Authority/Recommendation/Validation/Attribution quality without proliferation.

---

## 12 — Program Completion Recommendation (FINAL DECISION)

**The smallest body of work that maximizes paper-trading readiness, profitability discovery, reliability, governance compliance, and attribution quality — while minimizing maintenance, tokens, governance complexity, and overhead — is exactly four code changes plus two cheap supports:**

> **M1** (config-presence adapter selection) · **M2** (live paper-equity drawdown) · **M3** (unit + integration test suite) · **M4** (credential-free adapter completion with recorded-fixture contract tests) — supported by **R1** (`.env` hygiene) and **R2** (one activation runbook).

**Everything else is eliminated.** No new architecture, no new modules, no new capabilities, no agents, no extra CLAUDE files, no governance frameworks.

This set, and only this set, converts the current "boot-ready, stub-only, unverified" state into one where **credentials arrive → secrets inject → validation passes → data activates → paper trading begins — with no redesign**, while making the drawdown safety control real and giving profitability somewhere trustworthy to be discovered.

**Status: PLAN complete. Awaiting REVIEW approval before any EXECUTE.** Per the PLAN→REVIEW→EXECUTE constitution, no source has been modified; the four findings (F-A, F-B, F-C, F-D) are documented above with file-level evidence for the reviewer.

---

*PCP-001 introduces no architectural change. M1/M4 modify only `src/adapters/*` and add `tests/`; M2 modifies only MOD-09-owned `cap_paper_trading.py`; M3 adds only test files; R1/R2 touch only `.gitignore`, a new `.env.example`, and a new `CLAUDE.md`. `tests/architecture` (6/6) is the merge gate for every one of them.*

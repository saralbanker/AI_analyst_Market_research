# MULTI_SYMBOL_CONSTITUTIONAL_VERIFICATION_REPORT

**Protocol:** PLAN-003 Multi-Symbol Universe Constitutional Verification
**Mode:** Constitutional Tribunal — verification only. No implementation, no roadmap, no optimization.
**Authority basis (descending):** SDM_V2.3 (L1) → VAL05 (L2) → SADR_V2.1 (L3) → ARCHITECTURE_FOUNDATION_V1 (L4) → ADR-000..007 (L5) → IMP-001 (L6) → VER-001 (L7) → EXT-001 (L8) → FEASIBILITY-001 (L9)
**Primary rule applied:** Observation ≠ Authorization. Bootstrap realization ≠ Constitutional requirement. Empirical evidence (L9) cannot override constitutional authority (L1–L5).

---

## HEADLINE FINDING (orienting the reader)

The investigation inverts the protocol's implicit suspicion. The question posed was *"is multi-symbol authorized?"* The constitutional truth is stronger: **multi-symbol is the constitutional baseline, and the present single-symbol realization is an under-realization of the constitution, not a constitutional state.** Multiple constitutional invariants (notably the 3–5 Position Model, position concentration, and "eligible versus filtered equities") are structurally unsatisfiable at a one-symbol universe. Multi-symbol therefore requires **no** amendment at any authority level. It is an execution extension that realizes capacity the frozen constitution already mandates.

---

## SECTION 01 — Single-Symbol Bootstrap Analysis

**Classification: BOOTSTRAP REALIZATION (not a constitutional requirement).**

Evidence:

- **No constitutional source restricts the universe to one symbol.** A full read of SDM_V2.3 Parts I–VI, SADR_V2.1, and ARCHITECTURE_FOUNDATION_V1 finds zero "single symbol," "one instrument," or "one position" obligation. The only universe statement is SDM-CONST-03 / SDM-02: "exclusively Indian Equities (NSE/BSE)" — a *membership* restriction, not a *cardinality* restriction.
- **The single-symbol scope is recorded only at the implementation tier.** VER-001 §13 certifies "the implemented vertical slice only (single symbol RELIANCE, stub vendor adapters...)." IMP-001 scoped the slice. These are L6–L7 documents — below the constitution. The single-symbol fact lives in the realization layer, never in L1–L5.
- **The code confirms a bootstrap coupling, not an architectural one.** `src/mod01_market_data/market_data.py:36` reads `symbol = fixtures.SYMBOL`; the pipeline returns a scalar `VerifiedMarketData`, and `upstox_instruments.py` maps exactly one symbol. This is a hard-wired one-element universe — an implementation choice, not an enforced boundary.
- **FEASIBILITY-001 is itself multi-symbol** (20 real symbols). The empirical layer already exercised the universe concept; the production vertical slice simply has not been widened.

**Conclusion:** SUPPORTED that single-symbol is a bootstrap realization. The constitution neither requires nor privileges it.

---

## SECTION 02 — Capability Analysis (CAP-03, 05, 06, 07, 15, 16, 17)

| CAP | Constitutional granularity | Classification | Basis |
|---|---|---|---|
| **CAP-03** Corporate Action Adjustment | Operates per equity (splits/de-mergers are per-instrument) | **Single-symbol granularity, universe-iterated** | SADR CAP-03; SDM-02 Rule 3. No portfolio semantics; applied independently to each eligible symbol. |
| **CAP-05** Market Regime Classification | Market/context level (broad-market trend filter, regime, non-ergodic signal) | **Multi-symbol-neutral (market-level)** | SADR CAP-05 inputs are "eligible…market data" and broad-market trend filter; not bound to one symbol. |
| **CAP-06** Concept Drift Detection | Model-behaviour level | **Multi-symbol-neutral (model-level)** | SADR CAP-06; detects model/anchoring drift, independent of universe cardinality. |
| **CAP-07** Technical Signal Generation | Per-symbol signal | **Single-symbol granularity, universe-iterated** | SADR CAP-07; generates a signal set per instrument; direction is LONG/SHORT/NONE (direction is orthogonal to universe size). |
| **CAP-15** Opportunity Ranking | Multi-candidate by construction | **Multi-symbol by design** | SADR CAP-15: "Ranked opportunity list targeting 3–5 positions"; SDM-08 Rules 3–4. Single-symbol *under-exercises* it. |
| **CAP-16** Conviction-Weighted Allocation | Multi-position by construction | **Multi-symbol by design** | SADR CAP-16: distributes across selected opportunities, "concentration limits respected," "equal-weight prohibited." Concentration is meaningless at N=1. |
| **CAP-17** Null-State Declaration | Universe/cycle level | **Multi-symbol-neutral (universe-level)** | SADR CAP-17 fires when *no* candidate in the universe qualifies. FEASIBILITY-001 ("LONG-only produced no opportunities") is exactly its universe-level trigger. |

**Adversarial check honored — "ranking does not imply universe":** Ranking alone is *not* the derivation of multi-symbol (one could rank multiple setups on one symbol). The multi-symbol requirement is derived instead from SDM-02's plural "eligible **versus** filtered equities," SDM-11's "active position **count** 3–5," and "position **concentration**" — all of which require *distinct instruments*, not merely multiple setups.

---

## SECTION 03 — Portfolio Ownership Analysis (MOD-09)

**Determination: MOD-09 constitutionally owns multiple positions, concurrent holdings, and portfolio exposure. This is its designed operating point — not an extension of its authority.**

- SADR CAP-29 / ADR-002 MOD-09 owns: **"active position count," "position concentration status," "illiquidity metrics," "drawdown level against the 5% tolerance."** Every one of these is portfolio-level and degenerate at N=1: a "count" of one, "concentration" of 100%, and a portfolio drawdown indistinguishable from single-position drawdown.
- ADR-005 §3.8 / §3.13: Portfolio State is a **position registry**, "concentration ratios," cross-cycle persistent — explicitly plural.
- The single authoritative-source constraint (INV-07, SC-01, ADR-000 P-05) is *strengthened*, not stressed, by multiple positions: it exists precisely to prevent shadow per-position state.
- "Concurrent holdings" carry **no concurrent-execution obligation on the system** — positions are held by the human in the external broker; MOD-09 only *reflects* the authoritative external execution record (CAP-29 inputs; ADR-006 §3.2 MOD-07→MOD-09). See Section 06.

**Conclusion:** SUPPORTED. Portfolio ownership at multi-symbol scale is constitutionally pre-existing and unambiguous.

---

## SECTION 04 — Governance Scaling Analysis (CAP-19, 23, 24, 27, 31)

| CAP | Multi-symbol behaviour | Classification |
|---|---|---|
| **CAP-19** Position Limit Enforcement | Defined on "active position count" (3–5) and "concentration limit" — inherently multi-position. Single-symbol cannot exercise the limit it exists to enforce. | **SUPPORTED — designed for multi-position** (SDM-11 Rules 1,2,6; SADR CAP-19) |
| **CAP-23** Risk Circuit Breakers | Trigger on conditions (uncertainty bands, volume spikes, margin, non-ergodic signal), not on symbol count. CAP-27 suspends "affected domain only." | **SUPPORTED — condition-scoped, cardinality-independent** |
| **CAP-24** Hard Deterministic Halt | Fires on CAP-19 breach (position/concentration). Multi-position is its trigger domain. | **SUPPORTED** |
| **CAP-27** Conditional Suspension | Affected-domain-only, condition-driven auto-exit. Independent of universe size. | **SUPPORTED** |
| **CAP-31** Governance Compliance Monitor | Inputs are portfolio state "position records" (plural). Must detect a missing stop-loss / control breach on **any** position (GOV-02 Rule 1, "removal of required stop-loss protection"). | **SUPPORTED — already plural in specification** |

**Adversarial check honored — "do not assume detectors scale":** Each detector was traced to its constitutional input. None depends on universe cardinality; CAP-19/CAP-31 are *defined over* the multi-position portfolio state. The continuous, cycle-independent operation of CAP-19/23/31 (ADR-006 §2.4) is unaffected by how many symbols a cycle screens.

**One constitutional obligation surfaced (not a conflict):** CAP-31 violation detection is per-position — a single non-compliant position must trip Governance Lockout (State 2) for the portfolio. This is already what GOV-02 Rule 1 requires; it is not new authority.

---

## SECTION 05 — Audit Scaling Analysis (CAP-30)

**Determination: All audit guarantees remain intact at any universe size.**

- The three CAP-30 invariants — **terminal sink, immutable, non-participatory** (INV-04, SC-02, ADR-000 P-07) — are per-record properties independent of record volume. The hash chain (VER-001 §04) is sequential regardless of how many symbols produced the records.
- The constitution **already anticipates many assets in the audit stream**: SDM-02 Audit mandates "Log all excluded assets and the specific filtering rule triggered" — a per-excluded-asset obligation that only becomes meaningful with a real universe. Multi-symbol *realizes* this clause rather than straining it.
- Increased record count is a volume/performance matter, explicitly out of scope ("Do NOT optimize").

**Conclusion:** SUPPORTED. No audit guarantee weakens with scale.

---

## SECTION 06 — Boundary Analysis (Ownership / Dependency / Authority preservation)

- **Ownership preservation:** Multi-symbol introduces no new information class and no new owner. The 13 information classes (ADR-002 §5) are each cardinality-agnostic: "Market datasets," "Recommendations," "Portfolio State," etc. carry sets, not singletons. INV-02 holds unchanged.
- **Dependency preservation:** The DAG (ADR-002 §6, ADR-006 §3.2) is unchanged. A universe is iterated through MOD-01→MOD-04 to produce a *candidate set*, then MOD-05 ranks it. The three blocking gates (CAP-02, CAP-10, CAP-18) remain in force; their semantics are per-symbol/per-cycle and untouched.
- **Authority preservation:** No authority class changes. CAP-18 remains the sole HUMAN_APPROVAL gate per cycle (INV-01, INV-03). Multi-symbol does not add execution authority anywhere — FORB-04/FORB-06 unaffected.
- **No concurrency requirement is introduced.** The system is single-threaded advisory research; "concurrent positions" are external human holdings reflected by MOD-09. ADR-006's per-cycle execution model already accommodates an N-element universe as sequential/batched candidate evaluation feeding one ranking. **The protocol's "does the current execution model support concurrency?" question is answered: concurrency is not required, therefore the absence of a concurrency model is not a conflict.**

**One boundary observation (implementation-tier, flagged for the EXECUTE phase, not a constitutional defect):** the bootstrap aborts the entire cycle on a single symbol's CAP-02 vendor mismatch (VER-001 §07, V06). At N>1 the constitution requires the *opposite* — per-asset **exclusion with logging** (SDM-02 Audit; SDM-02 Rule 4 "missing a genuine winner is worse than rejecting too many"). The constitution already specifies per-asset exclusion; the cycle-abort behaviour is a one-symbol artifact, and realizing per-asset exclusion is *honoring* existing constitutional intent.

---

## SECTION 07 — Statistical Scaling Analysis (FEASIBILITY-001 → 50 / 100 / 200)

**FEASIBILITY-001 evidence (L9):** 20 symbols → 19 rejected, 1 SHORT survivor; LONG-only produced none; CAP-17 behaved correctly.

What this evidence *does* establish (constitutional compatibility):
- The rejection machinery, null-state (CAP-17), and "do-not-force-deployment" posture operate correctly on a real multi-symbol universe. A 95% rejection rate is **constitutionally healthy**, not a failure: SDM-01 Rule 4, SDM-07 Rule 5, CONSTRAINT-05 (cash is a valid position).

What this evidence does **not** establish (adversarial limit — "do not generalize FEASIBILITY-001"):
- One sample of 20 with one survivor proves *nothing* about statistical adequacy at 200. As L9 empirical evidence, it **cannot override** the L1 statistical constraints and cannot be generalized into a density or alpha claim.

Constitutional compatibility at scale:

| Universe | Constitutional compatibility | Governing authority |
|---|---|---|
| 50 | Compatible | Below applies at all three |
| 100 | Compatible | — |
| 200 | Compatible | — |

- **Decoupling principle (key result):** the constitution caps *output* (3–5 positions; Invariant 5) but sets **no cap on universe input** (SDM-02). Universe size and position count are decoupled, so growing the universe can never threaten the 3–5 invariant — it only increases the number of *rejections*.
- **Multiple-comparisons guard is already mandated:** SDM-05 Rule 4 ("deflated return metrics or statistical significance tests") and SDM-06 Rule 6 ("Deflated Sharpe… standard confidence intervals are insufficient") are precisely the controls for screening many candidates. CAP-11 owns this. This mandate becomes *more* load-bearing as N grows — but it already exists.
- **Open statistical refinement (owned, not a blocker):** whether the deflation is parameterized by the *number of trials = universe size* is a mathematical refinement within CAP-11's existing mandate (kin to VAL-class open items). It is owned by CAP-11; it is not an authorization gate and not an unowned responsibility.

**Adversarial checks honored:** "opportunity density improves" and "100 symbols means more alpha" are **rejected** — FEASIBILITY-001 evidences the opposite tendency (sparse survivors), and the constitution expects and welcomes that.

**Conclusion:** SUPPORTED for constitutional compatibility at 50/100/200. Statistical *adequacy* at large N is governed by the pre-existing deflated-metric mandate (CAP-11) and is a refinement, not a constitutional change.

---

## SECTION 08 — Responsibility Gap Analysis

Every emergent multi-symbol responsibility maps to an existing constitutional owner. **No UNOWNED RESPONSIBILITY found.**

| Emergent responsibility | Constitutional owner | Status |
|---|---|---|
| Rank a many-candidate set to 3–5 | CAP-15 (MOD-05) | Owned; designed for it |
| Allocate ₹5,000 across selected positions w/ conviction + concentration | CAP-16 (MOD-05) | Owned; designed for it |
| Cross-position concentration limit | CAP-19 (MOD-06) + CAP-16 | Owned |
| Portfolio exposure / position count / drawdown across holdings | MOD-09 (CAP-29) | Owned |
| Per-position governance compliance (stop-loss on any position) | CAP-31 (MOD-06) | Owned |
| Per-asset gate-failure exclusion + logging (vs cycle abort) | CAP-04 / CAP-02 semantics (SDM-02 Audit) | Owned; bootstrap implements as abort |
| Multiple-testing deflation scaled to trial count | CAP-11 (SDM-05 R4 / SDM-06 R6) | Owned; math refinement (VAL-class analog) |
| Cross-symbol correlation / portfolio VaR under concurrent positions | CAP-13 + CAP-23 (VAL-08, VAL-14, both CLASS_B) | Owned; deferred math, extension-point sufficient |
| Universe membership thresholds (liquidity/price for ₹5k) | CAP-04 (VAL-01, CLASS_C) | Owned; already a registered open item |

**Conclusion:** Zero unowned responsibilities. The constitution was authored multi-symbol; the owners pre-exist.

---

## SECTION 09 — Conflict Analysis

**No constitutional conflict (ownership / dependency / governance / portfolio / execution / audit / evidence / state / concurrency / human-authority) is created by multi-symbol operation.**

The single tension identified is **implementation-vs-constitution**, and it resolves *in favor of multi-symbol*:

| Tension | Trace | Determination |
|---|---|---|
| Bootstrap is single-symbol; constitution mandates 3–5 positions + concentration + "eligible vs filtered equities" | SDM-11; Invariant 5; SDM-02 vs IMP-001/VER-001 §13 scope | **False positive as a "conflict."** It is an under-realization. Constitution prevails; no amendment implicated. |
| Bootstrap aborts cycle on one symbol's CAP-02 mismatch | VER-001 §07 vs SDM-02 Audit / Rule 4 | **Implementation gap**, not constitutional conflict. Constitution already prescribes per-asset exclusion. |

Human-authority, audit-immutability, sentiment-isolation (VAL05 / INV-09), attribution read-only (INV-08), and halt-state independence (INV-06) are all **orthogonal to universe size** and remain intact.

---

## SECTION 10 — Amendment Analysis

| Authority | Change required? | Reason |
|---|---|---|
| **SDM_V2.3** | **No** | SDM-02 (universe), SDM-08 (ranking 3–5), SDM-09 (allocation across positions), SDM-11 (3–5 count, concentration), Invariant 5 already specify multi-symbol. Frozen text needs nothing added. |
| **SADR_V2.1** | **No** | All 31 capabilities are already specified for sets (CAP-15 ranks 3–5; CAP-16 allocates across positions; CAP-29 owns count/concentration). |
| **ARCHITECTURE_FOUNDATION_V1** | **No** | 11 domains and the dependency map are cardinality-agnostic. |
| **ADR-000 … ADR-007** | **No** | Module/dependency/state/execution/boundary models are symbol-count-neutral and already plural. No ADR asserts single-symbol. |

The only document that records single-symbol is the **implementation tier (IMP-001 / VER-001 scope statements)** — below the ADR constitution. Updating that scope record is an implementation-tier documentation action, not a constitutional amendment.

---

## SECTION 11 — Implementation Classification

**PLAN-003 = EXECUTION EXTENSION.**

It realizes constitutional capacity that already exists at L1–L5 without altering any architecture, ownership, dependency, authority, governance, or constitutional rule. It is not an ADR Realization Update (no ADR document requires editing), not an Architecture Change, and not a Constitutional Amendment. (If the tribunal treats IMP-001's "single symbol" *scope* note as a binding realization record, the only paperwork is an implementation-tier scope supersession — still below the ADR constitution.)

---

## SECTION 12 — Final Verdict

**A — NO CONSTITUTIONAL CHANGES REQUIRED.**

No SDM, SADR, AF, or ADR-000..007 amendment is implicated. Multi-symbol is the constitution's intended operating point; the single-symbol slice is a bootstrap under-realization of it.

---

## SECTION 13 — Authorization Decision

**PLAN_003_MULTI_SYMBOL_UNIVERSE — AUTHORIZED.**

Authorized because multi-symbol is **constitutionally required**, not merely permitted, and requires no amendment at any authority level.

Any conforming realization remains bound by these pre-existing constitutional obligations (stated as constraints, not as a roadmap):

1. **Output cardinality cap is invariant:** 3–5 positions regardless of universe size (Invariant 5; SDM-08/11). Universe growth must only increase rejections, never the position cap.
2. **Per-asset isolation at the gates:** a CAP-02 / CAP-10 / eligibility failure on one symbol excludes that symbol with logged reason (SDM-02 Audit; Rule 4) — it must not abort the universe.
3. **Statistical control scales with the universe:** CAP-11's deflated-Sharpe / significance mandate (SDM-05 R4, SDM-06 R6) must remain the screening gate as N grows; multiple-testing must not erode it.
4. **Single authoritative portfolio state preserved:** MOD-09 remains sole owner of count/concentration/drawdown across all positions (INV-07, SC-01); no per-symbol shadow state.
5. **Concentration and 5% portfolio-drawdown bounds apply across concurrent positions** (SDM-11 Rule 5; CONSTRAINT-06; CAP-13/CAP-16/CAP-19).
6. **Human gate per cycle and sentiment isolation are untouched** (INV-01, INV-09 / VAL05).
7. **Empirical evidence (FEASIBILITY-001) authorizes nothing on its own** — it confirms compatibility; the constitution authorizes.

---

*This report performs constitutional verification only. It contains no implementation design, no migration, no code, and no optimization. All conclusions trace to the authority hierarchy; FEASIBILITY-001 (L9) is treated as compatibility evidence and is denied override of L1–L5.*

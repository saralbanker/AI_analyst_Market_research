# MACRO_DATA_PROVIDER_DECISION_REPORT

**Document Type:** Constitutional Decision Adjudication (Governance Approval Artifact)
**Scope:** Determination only. No implementation, integration, or coding authorized.
**Authority Basis (exclusive, in hierarchy order):** SDM_V2.3 (FROZEN) → VAL05_OWNER_DECISION_RESOLUTION → SADR_V2.1 (CERTIFIED) → ARCHITECTURE_FOUNDATION_V1 → ADR-000..ADR-007 → IMP-001 / VER-001 / EXT-001.
**Evidence Boundary:** Conclusions derive only from the frozen corpus and the certified implementation. No conclusion originates from popularity, convenience, developer experience, or implementation difficulty.

---

## 0. THRESHOLD CORRECTION — A PREMISE THAT MUST BE RESOLVED FIRST

The investigation request frames the central question as *"what CAP-06 and CAP-07 actually require"* with respect to macroeconomic data. **Against the frozen constitution this premise is incorrect, and the error is material to the verdict.** It is corrected here before any determination is made, because the entire adjudication turns on it.

Per SADR_V2.1 §3–4 and §12 (Capability Traceability Matrix):

| Cap | Actual constitutional name | Primary source | Consumes macro data? |
|-----|----------------------------|----------------|----------------------|
| **CAP-06** | **Concept Drift Detection** | SDM-03 R2, SDM-05 R5, SDM-15 R13 | **No.** Inputs are *model behavior metrics, historical baselines, and CAP-05 regime classification.* |
| **CAP-07** | **Technical Signal Generation** | SDM-04 R1,7,8,9,10 | **No.** Inputs are *eligible/verified/adjusted market data + CAP-05 trend filter.* |

Neither CAP-06 nor CAP-07 has any constitutional relationship to macroeconomic data. CAP-06 detects *model* drift (the model anchoring to stale regimes); CAP-07 generates *price/volume technical* signals. The implementation confirms this exactly: `cap06_drift.py` compares first-half vs second-half return volatility of the **price bars**; `cap05_regime.py`/`cap07_technical.py` operate on **price bars only**. There is no macro input anywhere in MOD-02 or MOD-03.

**Where macro actually lives constitutionally** is an entirely different place: the **Risk Governance** domain. This correction does not weaken the case for macro data — it relocates it from the *alpha/evidence* path (where it would be a continuous requirement) to the *circuit-breaker/halt* path (where it is a tail-event trigger). That relocation is the single most decision-relevant fact in this report.

---

## 1. CONSTITUTIONAL ANALYSIS — THE INTENDED ROLE OF MACRO DATA

Because CAP-06/CAP-07 are not the relevant capabilities, the constitutional role of macro data must be traced through every actual occurrence of "macro" / "non-ergodic" / "correlation breakdown" in the frozen corpus.

**Every constitutional appearance of macroeconomic conditions:**

1. **SDM-03 Rule 5** — *"Decision thresholds must account for market non-ergodicity, where historical correlation matrices break down during macro shocks."*
2. **SDM-15 Rule 11** — *"Hard halt triggers must be implemented during extreme macro shocks and non-ergodic market breakdowns."*
3. **SDM-CONST-14 State 3 (Conditional Recommendation Suspension)** — trigger list includes *"extreme macro shocks, non-ergodic market breakdowns."*
4. **SADR_V2.1 CAP-23 (Risk Circuit Breaker Enforcement)** — Inputs include *"Macro condition signals"*; Constitutional Constraint: *"Hard halt triggers during extreme macro shocks and non-ergodic breakdowns (SDM-15 Rule 11)."*
5. **SADR_V2.1 CAP-05 (Market Regime Classification)** — Output: *"Non-ergodic condition signal (generic condition signal interface consumed by CAP-23 and CAP-27)."*

**Determination of intended role.** Macroeconomic data is constitutionally a **risk-governance tail-event detector**, not an evidence or alpha input. Its only sanctioned destination is **CAP-23 → CAP-27** (State 3 suspension) and the hard-halt path (SDM-15 R11). It exists to *stop the system from issuing recommendations during a regime in which its statistical machinery is invalid* — i.e., to protect the 5% drawdown invariant (SDM-CONST-08), not to find opportunities.

**What the constitution forbids macro data from doing.** The evidence hierarchy is closed and ordered: **Technicals primary (CONSTRAINT-04 / SDM-CONST-10), News supplementary, nothing else.** Macro is *not* in the evidence hierarchy at all. There is **no constitutional pathway** from macro data into CAP-12 (Confidence), CAP-13 (Expected Value), CAP-15 (Ranking), or CAP-16 (Allocation). Routing macro into any of those would manufacture a third evidence layer the constitution never authorized and would violate SDM-15 R3 (deterministic boundary) and the closed evidence hierarchy. **Macro may inform a halt; it may never inform a score.**

---

## 2. INDICATOR REQUIREMENTS ANALYSIS

Classification is by **constitutional traceability**, not analytical usefulness.

### 2.1 Mandatory (constitutionally required to *exist*, source-agnostic)

| Requirement | Authority | Nature |
|-------------|-----------|--------|
| A **macro-shock / non-ergodic condition signal** capable of triggering a hard halt and a State-3 suspension | SDM-15 R11; SDM-03 R5; SDM-CONST-14 State 3; CAP-23 | An **abstract condition signal** — *not a named indicator and not a named provider.* |

This is the **only** macro-traceable mandatory element, and the SADR explicitly rules it satisfiable by a **generic interface** (see §4 of this report). Nothing in the corpus names a single concrete macroeconomic series as mandatory.

### 2.2 Recommended (sharpen the shock detector; not mandated)

These *improve the fidelity* of the CAP-23 macro-shock trigger for real-capital operation but are constitutionally optional: **policy interest rate (RBI repo), headline inflation (CPI), INR/USD exchange rate, market-wide volatility (India VIX), and system liquidity.** They are recommended because the things SDM-15 R11 reacts to (correlation breakdown, volatility regime change, liquidity stress) are most directly observable through them.

### 2.3 Optional (beneficial context, no constitutional hook)

GDP growth, IIP, PMI, FII/DII flows, US Fed funds rate / global risk indices. Useful narrative context for a human reviewer; zero constitutional traceability.

### 2.4 Explicitly excluded (constitutionally prohibited destination)

Any macro indicator wired as a **computational input** to confidence, EV, ranking, or allocation. No such pathway exists or may be created (closed evidence hierarchy; CONSTRAINT-04; SDM-15 R3).

---

## 3. PROVIDER EVALUATION

Evaluated against the *actual* requirement (§1–2): supply a **macro-shock condition signal** to CAP-23, as a **replaceable** adapter (ADR-000 P-12; SDM-CONST-12), that **never** becomes load-bearing for the architecture (ADR-007 selection rule 2–3).

| Source | Fitness for the *constitutional* role (CAP-23 shock signal) | Verdict |
|--------|--------------------------------------------------------------|---------|
| **Upstox-derived / market-derived regime signals** | The shock the constitution cares about (volatility regime change, correlation breakdown, index drawdown, breadth collapse) is **directly derivable from the already-approved market-data feed** via CAP-05's non-ergodic signal. No new vendor, no new credential, no new boundary. | **Preferred / Sufficient minimum.** |
| **FRED** | Free, stable, API-clean. India coverage is thin but real (CPI, policy rate, INR/USD, some IIP). "US-centric" is only a defect if macro were an alpha input — it is not; for a *shock* trigger, the global/US risk channel (Fed funds, US yields, DXY) is genuinely relevant to Indian non-ergodic breakdowns. | **Preferred external fallback** (free, replaceable). |
| **data.gov.in / RBI bulletin data** | India-native CPI/IIP/policy data. No modern developer-friendly REST API (confirmed constraint); ingestion is brittle/manual. Acceptable as an *India-specific supplement*, not a primary feed. | **Permitted supplement.** |
| **RBI Data Portal** | No modern public REST API (confirmed). Cannot be a clean replaceable adapter. | **Not viable as primary.** |
| **Trading Economics** | No acceptable free usage model (confirmed). Adopting it for a *mandatory* role would make a paid vendor **load-bearing**, which ADR-007 rule 3 (replaceability mandatory) **rejects as a constitutional violation**. | **Rejected** for any required role; admissible only as an optional, fully-replaceable calibration if ever desired. |
| **Other free providers (World Bank, IMF, Alpha Vantage econ, DBnomics)** | Comparable to FRED; free, replaceable, India coverage varies. | **Admissible alternatives** to FRED; none required. |

**Current implementation state (EXT-001).** `src/adapters/macro.py` already encodes exactly this posture: a `MacroAdapter` Protocol, an always-available `StubMacroAdapter` returning `{}`, and a `TradingEconomicsMacroAdapter` **skeleton** that is **not consumed by any module**. The factory falls back to the stub. The system is certified paper-ready with macro returning empty. This is constitutionally correct — and notably the skeleton points at the one provider (§3) that should *not* be the required choice.

---

## 4. PAPER-TRADING REQUIREMENTS

**Determination: a macro API is NOT required for paper trading. (UNNECESSARY at this stage.)**

Evidence:
- EXT-001 §1, §8, §9 certify paper-trading **READY** with the macro adapter in stub mode (`{}`), explicitly: *"Macro adapter is available but not yet consumed by MOD-02 … additive wiring, optional for readiness."*
- SADR_V2.1 §11 reclassified **every** macro/non-ergodicity/VaR validation item — **VAL-03, VAL-08, VAL-14, VAL-17** — from CLASS_A to **CLASS_B**, each with the explicit ruling *"generic signal interface sufficient for architecture"* / *"regime context parameter sufficient."* **VAL-05 (sentiment) is the sole remaining CLASS_A blocker** — macro is not an architecture blocker at all.
- Paper trading's purpose is to validate the recommendation→approval→bookkeeping→attribution→metrics loop. None of that loop consumes macro data.

---

## 5. REAL-CAPITAL DEPLOYMENT REQUIREMENTS

**Determination: a dedicated macro API is NOT constitutionally *required* even for real-money deployment — but it is a *recommended enhancement* to the risk circuit breaker.**

Reasoning, strictly from authority:
- SDM-15 R11 mandates that hard halts **trigger** on extreme macro shocks. It mandates the **trigger**, not a **vendor**. SADR_V2.1 satisfies this with CAP-05's *"non-ergodic condition signal (generic condition signal interface)"* and classifies the underlying validation items CLASS_B — i.e., the architecture is complete with a **market-derived** signal. The constitution nowhere obligates an *external* macro feed.
- Therefore, for real capital, the constitutionally-sufficient path is: derive the macro-shock condition signal from the **already-approved Upstox market data** (index volatility regime, correlation/breadth breakdown, drawdown velocity) feeding CAP-23.
- An external macro feed (FRED-class) **improves** that detector — it adds policy-rate / inflation / currency / global-risk channels that pure price data lags on. This is a genuine, defensible risk-quality gain when real capital and the 5% invariant (SDM-CONST-08) are live. But "improves the detector" is **RECOMMENDED**, not **REQUIRED**. The constitution sets no threshold that an external feed alone can clear.

**Net:** real-money deployment *raises the value* of a macro feed from negligible to material, but does **not** cross the line into constitutional necessity. It remains optional — a risk-hardening calibration, gated to the CAP-23 path only.

---

## 6. COST-BENEFIT ANALYSIS

| Dimension | Finding |
|-----------|---------|
| **Benefit ceiling** | Bounded. Macro can only ever improve **one** capability (CAP-23 shock detection). It is structurally barred from improving alpha, confidence, EV, ranking, or allocation. So the upside is "better/earlier halts," not "better/more recommendations." |
| **Free sources sufficient?** | **Yes.** A FRED-class free feed plus market-derived signals fully covers the recommended indicator set (§2.2). The shock-detection benefit does not require paid granularity or low latency — macro shocks are not intraday-priced events for a 1–10 day swing horizon (SDM-CONST-05). |
| **Paid sources justified?** | **No.** Paid macro (Trading Economics-class) buys breadth/convenience the constitutional role does not need, and adopting it for a *required* function would violate replaceability (ADR-007 rule 3). At ₹5,000 capital (SDM-CONST-04) and minimum-sufficiency (ADR-007 rule 2), a recurring paid macro subscription is **Unjustified**. |
| **Cost of the minimum path** | Effectively zero: market-derived signal reuses an approved feed; FRED is free. |

**Conclusion:** if macro is adopted, it must be **free and replaceable**. Paid macro data is **not justified** at any currently-authorized stage.

---

## 7. MINIMUM VIABLE MACRO LAYER

The smallest constitutionally-acceptable macro layer is:

> **A single replaceable `MacroConditionSignal` adapter that emits one bounded "non-ergodic / macro-shock" condition signal into CAP-23 (and thence CAP-27), defaulting to a market-derived computation over the already-approved Upstox feed, with an optional free external enrichment (FRED-class) behind the same interface.**

Properties it must hold (all already latent in the codebase):
1. **Interface, not vendor.** Architecture depends on the *condition-signal interface* (CAP-05 output → CAP-23 input), never on a named provider (ADR-007 §8.3; P-12). The existing `MacroAdapter` Protocol + factory-fallback pattern already realizes this.
2. **Halt-path only.** Output may reach **only** CAP-23/CAP-27. It must remain structurally unable to reach CAP-12/13/15/16 (closed evidence hierarchy; CONSTRAINT-04; SDM-15 R3).
3. **Degrades to empty.** Absence of any macro source must yield a safe, defined state (today: `StubMacroAdapter → {}`), never a crash and never a forced deployment (CONSTRAINT-05).
4. **Replaceable / non-load-bearing.** Substituting or removing the external source must force **no** architectural change (SDM-CONST-12; ADR-007 rule 3).

Anything beyond this single condition signal is enhancement, not requirement.

---

## 8. FINAL VERDICT

> ## **OPTIONAL**

A dedicated macroeconomic data provider is **OPTIONAL** across the entire authorized program.

- It is **UNNECESSARY** for paper trading (§4) — certified ready without it.
- It is **OPTIONAL / RECOMMENDED-as-enhancement** for real-capital deployment (§5) — it improves the CAP-23 shock detector but is never constitutionally mandated; the requirement (SDM-15 R11) is fully satisfiable by a market-derived condition signal that the SADR explicitly deemed sufficient (CLASS_B reclassification of VAL-03/08/14/17).
- It is **PROHIBITED as a load-bearing dependency** and **PROHIBITED on the alpha/evidence path** in all cases.

The verdict is **OPTIONAL** rather than **REQUIRED LATER** precisely because the SADR already certified the architecture complete using a generic, market-derivable condition signal. No deployment phase crosses into necessity.

---

## 9. PROVIDER RECOMMENDATION

| Role | Selection | Justification |
|------|-----------|---------------|
| **Preferred (minimum)** | **Market-derived condition signal** from the approved **Upstox** feed via CAP-05's non-ergodic output | Zero new vendor/credential/boundary; constitutionally sufficient (SADR CLASS_B ruling); reuses an approved integration (ADR-007 §8.3). |
| **Preferred external fallback** | **FRED** (or equivalent free, replaceable source: World Bank / IMF / DBnomics) | Free, clean API, replaceable; adds policy-rate/inflation/currency/global-risk channels relevant to *shock* detection; "US-centric" critique is moot for a tail-risk trigger and is offset by genuine global-risk relevance. |
| **Permitted supplement** | **data.gov.in** (India-native CPI/IIP/policy) | India specificity; accept brittleness because it is supplementary, not primary. |
| **Rejected (as required role)** | **Trading Economics** | No acceptable free model; making it required would violate replaceability (ADR-007 rule 3). Admissible only as a fully-optional, swappable calibration. |
| **Rejected (as primary)** | **RBI Data Portal** | No modern public REST API; cannot form a clean replaceable adapter. |

All adoption must keep the macro source behind the existing `MacroAdapter` interface, feeding the CAP-23 path only.

---

## 10. EXECUTIVE DECISION (for Governance Approval)

**Recommended governance resolution:**

1. **Adopt verdict OPTIONAL.** No dedicated macroeconomic data provider is required to proceed. Paper-trading activation is **not** gated on this decision and may continue.
2. **Do not procure any paid macro subscription.** Paid macro data (incl. Trading Economics) is Unjustified at current scale and would create a replaceability violation if treated as required.
3. **Treat macro as a risk-governance enhancement, not an evidence input.** Any future macro wiring connects **only** to CAP-23/CAP-27. Wiring macro into confidence/EV/ranking/allocation is constitutionally prohibited and must be rejected at review.
4. **When real-capital deployment is contemplated, schedule (not now) a bounded task** to implement the *Minimum Viable Macro Layer* (§7): first a market-derived shock signal, optionally enriched by a free FRED-class source — both behind the existing replaceable adapter, defaulting safely to empty.
5. **Record the premise correction (§0)** in the governance log: CAP-06 = Concept Drift Detection and CAP-07 = Technical Signal Generation; neither is a macro capability. Future macro discussion must reference the Risk Governance domain (SDM-15 R11 / CAP-23), not CAP-06/CAP-07.

**One-line constitutional determination:**
> *Macroeconomic data is an optional, free-only, replaceable circuit-breaker input to CAP-23 — never a required dependency and never an evidence-path input — at every authorized stage of this system.*

---

*This report is a decision adjudication only. It authorizes no implementation, integration, or coding. It introduces no capability, dependency, authority, or governance rule, and modifies no frozen artifact. Its authority derives exclusively from SDM_V2.3, VAL05_OWNER_DECISION_RESOLUTION, SADR_V2.1, ARCHITECTURE_FOUNDATION_V1, ADR-000..ADR-007, IMP-001, VER-001, and EXT-001.*

*End of MACRO_DATA_PROVIDER_DECISION_REPORT*

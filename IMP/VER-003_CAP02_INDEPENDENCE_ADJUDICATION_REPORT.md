# VER-003 — CAP-02 INDEPENDENCE ADJUDICATION REPORT

**Task:** VER-003_CAP02_INDEPENDENCE_ADJUDICATION
**Date:** 2026-06-20
**Mode:** Constitutional adjudication only — no repair, no implementation, no optimization, no redesign.
**Predecessor authority:** VER-002 (PARTIALLY_CERTIFIED; blocking finding A-1).
**Question collapsed to:** *What constitutes constitutional independence for CAP-02?*

**Evidence convention.** Each claim is tagged **[OBSERVED]** (verbatim authority text or runtime fact) or **[INFERENCE]** (derived from the authority hierarchy). Where the hierarchy does not decide a question, it is declared **[INSUFFICIENT EVIDENCE]** rather than resolved by assumption.

---

## §01 — Constitutional interpretation of SDM-02 Rule 2

The cross-verification mandate is **not** a single isolated clause; it is asserted redundantly at three authority levels, and the lower realization narrows the meaning of the higher abstraction.

**[OBSERVED] L1 — SDM_V2.3:**
- SDM-02 Rule 2: *"OHLCV metrics must be cross-verified across at least two independent sources before signal logic executes."*
- SDM-05 Rule 1: *"Metrics must be cross-verified between at least two independent data sources before signal logic executes."*

**[OBSERVED] L3 — SADR_V2.1:**
- CAP-01 Constraint: *"Must support ingestion from at least two independent sources."* (SDM-02 R1, 2)
- CAP-02 Necessity: *"SDM-02 Rule 2 and SDM-05 Rule 1 explicitly prohibit signal logic from executing on data not verified across at least two independent sources."*
- CAP-02 Inputs: *"Raw data from CAP-01, from at least two independent sources **for the same data point**."*
- CAP-02 Constraint: *"Signal logic may not receive data that has not passed cross-verification. **Hard blocking gate.**"*

**[OBSERVED] L5 — ADR-007 (Technology & Platform Selection):**
- T-12: *"≥2 independent market-data sources cross-verified … Inbound read-only data adapters to **≥2 vendors** … replaceable per P-12."*
- §271: *"≥2 independent NSE/BSE market-data **vendors** (cross-verified at CAP-02)."*
- §275: *"Market-data vendors (≥2 independent) … architecture depends on the *two-source cross-verification interface*, **never a specific vendor**."*
- §145: permitted optimization is *"concurrency within MOD-01 to fetch from **multiple data vendors** in parallel … because cross-verification (CAP-02) still executes synchronously as a gate."*
- §321: *"≥2 market-data vendors … Required."*

**[INFERENCE] Interpretation.** The higher authorities (L1, L3) use the abstract noun **"source."** The frozen realization (L5, ADR-007) operationalizes that abstraction into **"vendor"** — consistently and without exception. ADR-007 is the constitutional authority charged with technology realization; its reading is the authoritative resolution of *how* "two independent sources" is to be realized. The three levels are **harmonious, not conflicting**: a vendor is a source, and ADR-007 specifies that the two required sources are two **vendors**, not two views of one vendor. The purpose clause (SADR CAP-02 Necessity) — preventing signal logic from consuming **unverified/corrupt** data — is served only if the two sources can fail *independently*. Two paths sharing a single upstream pipeline cannot disagree on a corruption originating in that shared pipeline; the gate would pass vacuously. The phrase **"for the same data point"** (SADR) confirms the intent: two genuinely separate observations of one fact, compared.

---

## §02 — Definition of independence

The constitution does not supply a glossary entry for "independent." **[OBSERVED]** No definition of "independent" or "source" exists anywhere in `ADR/Constitution/`. The meaning must therefore be derived from the cross-verification *purpose* and from ADR-007's "vendor" realization.

**[INFERENCE] Operative definition.** Two sources are *independent* for CAP-02 purposes when **they share no upstream failure mode** — i.e., a data corruption, outage, or error in one cannot, by construction, propagate identically into the other. Decomposed across the dimensions named in the investigation objective:

| Dimension | Required for independence? | Basis |
|---|---|---|
| **Vendor / provider entity** | **YES — decisive** | ADR-007 "≥2 … vendors", "never a specific vendor" |
| **Upstream exchange-feed origin** | Materially relevant | NSE/BSE is the common truth; total feed-origin separation is impossible, so independence is at the *vendor pipeline* layer, not the exchange layer |
| **Infrastructure / hosting** | Follows from vendor separation | Distinct vendors normally imply distinct ingestion/storage stacks |
| **Computation (adjustment, normalization)** | Materially relevant | Distinct vendors apply distinct corporate-action/normalization logic — the differences CAP-02 exists to surface |
| **Ownership / billing entity** | Strong proxy for vendor independence | Same owner ⇒ shared pipeline risk |
| **API endpoint** | **NOT sufficient alone** | Two endpoints of one vendor share that vendor's pipeline ⇒ common failure mode |
| **Time source** | Not constitutionally specified | No authority addresses clock independence (cf. VER-002 A-2, timestamp loss — separate finding) |

**[INFERENCE] Floor.** Independence is established at the **vendor** layer. Independence at the *endpoint* layer alone (the current A-1 condition) does **not** satisfy it. Independence cannot be required at the *exchange-feed* layer (both vendors ultimately observe NSE/BSE; that shared truth is the point of comparison, not a defect).

---

## §03 — Candidate source analysis

The constitution is deliberately **vendor-agnostic on identity** (**[OBSERVED]** ADR-007 §275 "never a specific vendor"; §21 "No conclusion derives from … vendor marketing"). Therefore the constitution **cannot name** an acceptable vendor; it can only state the *properties* a second source must hold. Each candidate below is evaluated against those properties. Empirical adequacy (does vendor X actually serve correct NSE/BSE OHLCV for the same data point) is an implementation/test question I am forbidden to resolve here and is marked accordingly.

- **Alternate Upstox endpoints** — **FAILS (constitutional).** Same vendor, same ownership, same upstream pipeline ⇒ shared failure mode. This is precisely the A-1 condition. Not two vendors.
- **Cached snapshots (of Upstox)** — **FAILS (constitutional).** A cache is a *copy* of one source, not a second source. Shares the original's failure mode; "for the same data point" comparison is circular.
- **Synthetic / fixture paths** — **FAILS (constitutional).** Not a market-data source at all; introduces fabricated data into a live evidence path. Cross-verifying real data against synthetic data is a vacuous gate and corrupts the evidence philosophy. (Also out of scope: forbidden to implement.)
- **Finnhub** — **FAILS (role mismatch).** Finnhub is wired as the **news/sentiment** source. Sentiment/news is advisory-only and constitutionally barred from the computational evidence path (VAL05/INV-09). Using it as a market-OHLCV cross-verifier would either (a) require it to serve NSE/BSE OHLCV [INSUFFICIENT EVIDENCE it does on this tier] and (b) risk contaminating the advisory/computational boundary. Not a qualifying market-data vendor as wired.
- **Yahoo Finance** — **CANDIDATE, constitutionally permissible *as a class*; identity not certifiable here.** A distinct vendor with an independent pipeline ⇒ satisfies the *independence property*. Whether it supplies correct NSE/BSE OHLCV "for the same data point" is **[INSUFFICIENT EVIDENCE]** — empirical, and forbidden to test under this task.
- **Alpha Vantage** — same disposition as Yahoo: distinct vendor ⇒ independence property satisfied; NSE/BSE adequacy **[INSUFFICIENT EVIDENCE]**. (Note: an `ALPHA_VANTAGE_API_KEY` slot exists in `src/config.py` and `src/.env` but is **[OBSERVED] empty and not wired into the market factory** — `src/adapters/factory.py::get_market_adapter` references only Upstox.)
- **Twelve Data** — same disposition: distinct vendor ⇒ independence property satisfied; NSE/BSE adequacy **[INSUFFICIENT EVIDENCE]**. (Same wiring status: key slot present, empty, unwired.)
- **NSE official sources** — **CANDIDATE, but caution.** A distinct vendor/provider relative to Upstox ⇒ independence property at the vendor layer satisfied. Caveat: it is *nearer the exchange origin*, which strengthens accuracy but means the comparison is against the primary feed rather than a second independent processor; constitutionally this still qualifies as a second independent vendor. NSE/BSE retrieval adequacy/terms **[INSUFFICIENT EVIDENCE]**.

---

## §04 — Independence matrix

Legend: ✔ independent of Upstox on this dimension · ~ partial/shared-by-nature · ✘ not independent · ? insufficient evidence.

| Candidate | Distinct vendor | Distinct infra | Distinct computation | Distinct ownership | Distinct endpoint | NSE/BSE same-data-point coverage | CAP-02 independence verdict |
|---|---|---|---|---|---|---|---|
| Upstox alt endpoint | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **FAILS** |
| Upstox cache/snapshot | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **FAILS** |
| Synthetic / fixture | ✘ | ✘ | ✘ | ✘ | n/a | ✘ | **FAILS** |
| Finnhub (news role) | ✔ | ✔ | ✔ | ✔ | ✔ | ? (and role-barred) | **FAILS (role)** |
| Yahoo Finance | ✔ | ✔ | ✔ | ✔ | ✔ | ? | **QUALIFIES on property; identity ?** |
| Alpha Vantage | ✔ | ✔ | ✔ | ✔ | ✔ | ? | **QUALIFIES on property; identity ?** |
| Twelve Data | ✔ | ✔ | ✔ | ✔ | ✔ | ? | **QUALIFIES on property; identity ?** |
| NSE official | ✔ | ✔ | ~ (nearer origin) | ✔ | ✔ | ? | **QUALIFIES on property; identity ?** |

**[INFERENCE]** The matrix yields a clean partition: the **same-vendor / copy / synthetic** row-group fails on the *constitutional* independence test outright; the **distinct-vendor** row-group satisfies the *constitutional* independence property, with their *empirical* NSE/BSE adequacy left open (and out of scope). No candidate is constitutionally *named* as required or blessed.

---

## §05 — Minimal acceptable architecture

**[INFERENCE] from [OBSERVED] ADR-007 + SADR CAP-01/02.** The constitutionally minimal configuration that would satisfy SDM-02 Rule 2 is:

> **Two independent market-data vendors**, each a read-only inbound adapter behind MOD-01's anti-corruption boundary, both supplying NSE/BSE OHLCV **for the same data point**, compared at CAP-02 as a synchronous hard blocking gate before any signal logic executes; each vendor **replaceable** without architectural change (P-12), neither vendor privileged.

What this minimum **does not** require: a specific named vendor; a paid vendor; symmetric vendors; a third source; clock/time-source independence. What it **does** require and the present system lacks: a **second, genuinely distinct vendor** in the `variant="b"` slot. **[OBSERVED]** Today `get_market_adapter("a")` and `("b")` both return `UpstoxMarketAdapter` when credentials are present — the `variant` argument is ignored in live mode — so the minimum is **not met**. (This is the A-1 condition; stated as fact, not as a remediation instruction.)

---

## §06 — Free vs paid vendor analysis

**[OBSERVED]** ADR-007 §21 bars deriving any conclusion from "cost," "implementation convenience," or "vendor marketing." ADR-007 §275/§321 require only "≥2 independent … vendors," "replaceable," "never a specific vendor." No authority at any level (L1–L5) conditions cross-verification on a price tier, a commercial-licensing class, or a paid SLA.

**[INFERENCE] Ruling.** **Paid vendors are NOT constitutionally required.** Cost is constitutionally irrelevant. A *free* second vendor that (a) is a genuinely independent vendor and (b) supplies correct NSE/BSE OHLCV for the same data point satisfies SDM-02 Rule 2 exactly as well as a paid one. Equally, the constitution does **not** declare free vendors *sufficient* in the abstract — sufficiency turns on the independence + coverage properties, not on the price. The free/paid axis is simply **not a constitutional axis**.

---

## §07 — Paper-trading gate determination

**[OBSERVED]** CAP-02 is a **hard blocking gate**: "Signal logic may not receive data that has not passed cross-verification" (SADR CAP-02; SADR §637/§648 blocking-gate diagram). **[OBSERVED]** EXT-001 governs paper-trading readiness; VER-002 (current blocking authority) returned **PARTIALLY_CERTIFIED** because the gate currently passes **vacuously** (Upstox compared to itself ⇒ diff = 0).

**[INFERENCE] Ruling.** A vacuous pass is **not** a constitutional pass. The gate's precondition — corroboration by two *independent* sources — is unmet, therefore signal logic is, constitutionally, executing on data that **has not passed cross-verification**. Paper trading consumes the identical MOD-01 → signal pipeline through the identical gate. Therefore **paper trading MAY NOT proceed under the current partial certification.** It remains **BLOCKED** until the CAP-02 gate is satisfied by a genuinely independent second vendor. (Determination only — no remediation prescribed.)

---

## §08 — PLAN-003 authorization status

**[INFERENCE] from VER-002 + §05.** PLAN-003 (multi-symbol universe) remains a *constitutionally valid design* (per the prior multi-symbol verification) but is **operationally BLOCKED**, unchanged by this adjudication. Multi-symbol expansion would replicate the unmet single-vendor precondition across every symbol — propagating a vacuous CAP-02 gate at scale. The governing sequence holds: **certification before expansion.** PLAN-003 is **NOT AUTHORIZED to begin** while CAP-02 independence is unsatisfied.

---

## §09 — Final constitutional verdict

> ## VERDICT: **A — TWO FULL (INDEPENDENT) VENDORS REQUIRED**

**Basis.** SDM-02 R2 and SDM-05 R1 (L1) mandate "two independent sources"; SADR CAP-01/02 (L3) restate it as "two independent sources for the same data point" behind a hard blocking gate; ADR-007 (L5) resolves "source" into "**≥2 independent … vendors**," explicitly, repeatedly, and without a single-source carve-out anywhere in L1–L5. **[OBSERVED]** No exception, waiver, or single-source provision exists in the constitution.

**Why not B (independent evidence paths sufficient).** ADR-007 reads the requirement as ≥2 *vendors*, and "for the same data point" + the anti-corruption purpose require that the two paths fail independently. Two endpoints of one vendor, a vendor + its cache, or a vendor + synthetic data are "two paths" but share a failure mode — exactly the vacuous condition (A-1) the gate exists to prevent. B understates the mandate.

**Why not C (single source permissible).** No single-source provision exists at any level; the requirement is asserted four times across three authorities. C is constitutionally foreclosed.

**Why not D (insufficient evidence).** On the *constitutional question asked* — what independence means — the evidence is explicit, redundant, and internally consistent. D would be the verdict only if the authorities were silent or conflicting; they are neither.

**Bounded INSUFFICIENT-EVIDENCE declarations (do not affect the verdict):**
1. Whether any **specific named** vendor (Yahoo, Alpha Vantage, Twelve Data, NSE) actually serves correct NSE/BSE OHLCV for the same data point — **empirical**, the constitution is vendor-agnostic by design, and testing is out of scope.
2. Time-source/clock independence — **unaddressed** by any authority (related to but distinct from VER-002 A-2).

---

## §10 — Executive ruling

CAP-02 independence means **two independent market-data vendors** — distinct provider entities whose data pipelines share no common upstream failure mode — each supplying NSE/BSE OHLCV for the same data point, compared at a synchronous hard blocking gate before any signal logic runs, each replaceable, none privileged. This is fixed text at L1 (SDM-02 R2 / SDM-05 R1), L3 (SADR CAP-01/02), and L5 (ADR-007), with no single-source exception anywhere.

The current system does **not** meet it: both `variant` slots resolve to Upstox, so CAP-02 compares Upstox to itself and passes vacuously (A-1). That is **not** a constitutional pass.

Consequently:
- **Independence is at the vendor layer**, not the endpoint layer. Same-vendor endpoints, caches, and synthetic paths all FAIL.
- **Paid vendors are NOT required**; cost is not a constitutional axis. A free, independent, NSE/BSE-covering vendor qualifies.
- **A qualifying second vendor must be a distinct provider**; the constitution names none and blesses none — distinct-vendor candidates (Yahoo / Alpha Vantage / Twelve Data / NSE) satisfy the *independence property*, but their empirical adequacy is out of scope.
- **Paper trading remains BLOCKED**; the CAP-02 precondition is unmet.
- **PLAN-003 remains NOT AUTHORIZED**; certification precedes expansion.

This report renders a constitutional determination only. It prescribes no implementation, no repair, no roadmap, and asserts nothing beyond the observed authority hierarchy.

**— END VER-003 —**

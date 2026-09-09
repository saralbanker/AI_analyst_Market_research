# VER-002 — MARKET DATA CERTIFICATION REPORT

**Task:** VER_002_MARKET_DATA_CERTIFICATION
**Mode:** Certification Tribunal — verification only. No repair, no optimization, no implementation, no migration, no multi-symbol work.
**Date:** 2026-06-20
**Scope:** Primary market evidence path of the single-symbol (RELIANCE) bootstrap slice: CAP-01, CAP-05, CAP-06, CAP-07, CAP-10, CAP-11, CAP-17, plus audit / governance / human-authority integrity under real market data.
**Evidence basis:** SDM_V2.3 (L1) … EXT-002 (L9). Per L9, runtime evidence overrides assumptions.

---

## HEADLINE

The capabilities downstream of the cross-verification gate are **proven valid on genuine Upstox data**. Certification of the *full* market-data path is blocked by **one isolated, constitutional non-compliance: A-1.** CAP-02's constitutional precondition (SDM-02 Rule 2 — cross-verification across **two independent sources**) is not met at runtime, so the gate that authorizes all downstream signal logic is passing **vacuously**. This is an *implementation/wiring* defect, not an architectural one — but it **is** a certification blocker because it leaves a constitutional precondition for signal execution unsatisfied.

**Verdict: B — PARTIALLY_CERTIFIED.** **PLAN-003 is NOT authorized to begin** (certification before expansion).

---

## SECTION 01 — Market Data Authenticity Analysis

Genuine Upstox data is **PROVEN** (EXT-002 L9, re-confirmed this tribunal by a fresh clean-DB run):

- Persisted `market_baselines`: 59 bars, opens/closes ₹1258.8–1463.6, volumes ~19–25M, 58/59 distinct closes, **non-monotonic**, **no `2000.0` fixture anchor** — fails every fixture signature.
- Internal consistency check (authenticity, not just non-fixture): regime **BEARISH** is corroborated by CAP-07's real moving averages **SMA-short 1295.34 < SMA-long 1328.59** → SHORT — a coherent bearish structure that synthetic fixtures (monotonic uptrend → BULLISH) cannot produce.
- Reproducible/deterministic across two independent runs (same regime, same signal, same rejection).
- No silent fixture fallback on the market path: an `AdapterError` would raise `CrossVerificationFailure → cycle_aborted`; no abort occurred and real bars persisted.

**Authenticity: ESTABLISHED.** (Per forbidden-assumptions: authenticity is necessary but **not** sufficient for certification — see §06.)

---

## SECTION 02 — Capability Validation

| CAP | Function | Real-data evidence | Status |
|---|---|---|---|
| **CAP-01** Ingestion | Two live Upstox `historical-candle` calls; real OHLCV persisted; `validate_bars` passed | Ingestion of genuine data proven | **VALID** |
| **CAP-05** Regime Classification | `regime_classified: BEARISH` on real prices; corroborated by real MA structure | Operates correctly on real data | **VALID** |
| **CAP-06** Concept Drift | `drift_evaluated: drift_detected=false, first_half_vol=0.0187, second_half_vol=0.0131` — computed from real volatility | Operates correctly on real data | **VALID** |
| **CAP-07** Technical Signal | `direction=SHORT, strength=0.0250, sma_short=1295.34, sma_long=1328.59` — derived from real bars; direction consistent with MAs | Operates correctly on real data | **VALID** |
| **CAP-10** Walk-Forward Validation | `walk_forward_evaluated: passed=false, reason="fold disagreement"` (fold 0 SHORT, forward_return −0.0318…) → `signal_rejected` | **Exercised on real data; genuinely rejects** | **VALID** |
| **CAP-11** Statistical Edge / Significance | **NOT REACHED** — CAP-10 rejected upstream, so CAP-11 did not execute on real data | Source-agnostic function; prior fixture evidence (VER-001 `signal_validated`) certifies behaviour; **no real-data observation available in this slice** | **VALID-BY-CONSTRUCTION; UNEXERCISED on real data (L-1, limited evidence — not a defect)** |
| **CAP-17** Null-State Declaration | `null_state_declared: NO_VALIDATED_OPPORTUNITIES`; `decisions: []`; "Hold cash" posture | Operates correctly on real data | **VALID** |

**Key adversarial note:** Real RELIANCE daily data **deterministically fails CAP-10** (fold disagreement), so the production slice cannot, on its own data, drive CAP-11. CAP-11's correctness is independent of data source (it is a statistical test over already-validated signals), so this is a **coverage gap, not a fault**. Manufacturing a passing signal to force CAP-11 would constitute implementation/optimization — **forbidden** — so it is recorded as limited evidence (L-1), not asserted beyond the evidence.

---

## SECTION 03 — Audit Integrity Analysis

- `tools/audit_review.py --verify-chain` → **chain verified** (EXT-002: 20 records).
- Full ordered trail on real data: MOD-11 → MOD-01(CAP-01/02/03) → MOD-02(CAP-05/06) → MOD-03(CAP-07/08/09) → MOD-04(CAP-10) → MOD-09(CAP-29) → MOD-06(CAP-24..27) → MOD-05(CAP-17) → MOD-07(CAP-18) → MOD-08(CAP-21). Matches ADR-006 ordering.
- Audit survives real market data unchanged; immutability triggers intact (VER-001 AUD-02).

**Status: VALID.**

---

## SECTION 04 — Governance Integrity Analysis

- Four halt states read **independently**, all inactive (`active_halts: []`) on real data.
- MOD-06 detection (CAP-19/23/31) and gating unaffected by data source.
- `AUTO_EXECUTION_ENABLED=false`, `BROKER_EXECUTION_ENABLED=false`; zero execution authority.
- Null-state correctly gated MOD-05 issuance without disturbing other modules.

**Status: VALID.**

---

## SECTION 05 — Human Authority Analysis

- CAP-18 reached on real data; under null-state produced `no_decision_required` — no auto-approval, no timeout bypass, no pre-approval.
- Human gate remains the sole, bypass-proof precondition for any trade action (INV-01). Real data did not alter this.

**Status: VALID.**

---

## SECTION 06 — A-1 Constitutional Analysis (CAP-02 self-verification)

**Determination: A-1 is an IMPLEMENTATION DEFECT that is ALSO a CERTIFICATION BLOCKER.**

Two distinct questions, separated to avoid conflation:

1. **Is the architecture defective?** No. CAP-02 exists, is correctly positioned as the constitutional hard blocking gate (SADR §5; ADR-002 §6.2; ADR-006 Required Ordering 2), and `cross_verify` logic is correct — it *would* reject divergence > 1%. The architecture satisfies the constitution.
2. **Is the constitutional precondition met at runtime?** **No.** `factory.get_market_adapter` ignores `variant` in live mode and returns `UpstoxMarketAdapter` for **both** A and B (`factory.py:21-27`; `market_data.py:41-42`). CAP-02 compares Upstox to itself → `diff=0` → vacuous pass. **SDM-02 Rule 2** ("OHLCV metrics must be cross-verified across **at least two independent sources** before signal logic executes") is **unsatisfied**. No second real market source is wired (`ALPHA_VANTAGE_API_KEY` / `TWELVE_DATA_API_KEY` are empty and unconnected).

**Why it blocks certification (attacking the "real data is enough" assumption):** SDM-02 Rule 2 is a *precondition for signal execution*, and CAP-02 is a *blocking gate* — "signal logic may not receive data that has not passed cross-verification." Currently all downstream signal logic (CAP-05/06/07/10) executes on data that passed **only a self-comparison**. The data is authentic, but its **independent corroboration — the specific constitutional guarantee CAP-02 exists to provide — is absent.** Authenticity ≠ cross-verification. The gate's constitutional function is not performed.

**Can single-vendor operation be certified for the bootstrap slice? (attacking both "invalid" and "acceptable" assumptions):**
- It is **not "acceptable"**: the frozen SDM provides **no single-source carve-out**; Rule 2 says "at least two independent sources," unconditionally. There is no bootstrap exemption in L1–L5.
- It is **not intrinsically "invalid" architecturally**: nothing in the design forbids a second vendor; the gate is sound and one credentialed independent source away from compliance.
- Therefore: **single-vendor operation cannot be certified against the frozen constitution.** Certifying it would require a constitutional deviation/amendment — out of scope and forbidden. A-1 stands as an **open constitutional blocker** to full market-layer certification, isolated to the source-independence of one gate.

**Classification: PROVEN constitutional non-compliance via implementation defect. Certification blocker. Not an architecture defect.**

---

## SECTION 07 — A-2 Observability Analysis (timestamp loss)

**Determination: A-2 is an OBSERVABILITY DEFECT, NOT a standalone certification blocker.**

- The Upstox adapter discards the real candle timestamp (`market.py` drops `candle[0]`) and substitutes a synthetic `day` index `0..n-1`. The adapter **sorts chronologically before re-indexing**, so **temporal ordering is preserved** — the property CAP-10 walk-forward actually depends on (SDM-05 Rule 2: prevent chronological leaks). Walk-forward validity is therefore intact (and was exercised correctly on real data, §02).
- No constitutional rule mandates **absolute** timestamp retention. SDM-02 Rules concern OHLCV cross-verification and split adjustment, not wall-clock retention.
- **However**, two genuine observability holes exist: (a) staleness/recency cannot be observed (no real date on persisted bars); (b) the data-quality "no gaps in `day` sequence" check is **structurally defeated** — re-indexing to a contiguous `0..n-1` makes a real missing trading day invisible (it simply yields a shorter contiguous run). The future-timestamp guard is also dead (conditional on a field that is never present).

**Why not a blocker:** the *computational* evidence path (ordering → walk-forward → significance) is constitutionally intact; A-2 degrades *observability and gap-detection*, not the validity of the temporal computation. It must be carried as a **named open observability item**, not a certification-denial cause.

**Classification: observability defect; non-fatal; open item.**

---

## SECTION 08 — Conflict Analysis (all blockers)

| ID | Finding | Authority impacted | Type | Blocks full cert? | Confidence |
|---|---|---|---|---|---|
| **A-1** | CAP-02 cross-verifies one vendor against itself | SDM-02 Rule 2; SADR CAP-02 | Implementation defect → constitutional precondition unmet | **YES** | PROVEN |
| **A-2** | Real timestamps discarded; gap-check defeated; staleness unobservable | SDM-02 (observability margin); SDM-05 (ordering intact) | Observability defect | No | PROVEN |
| **L-1** | CAP-11 not exercised on real data (CAP-10 rejects upstream) | SADR CAP-11 | Evidence-coverage gap (no fault) | No | PROVEN (limited evidence) |
| A-3 | Finnhub news empty/degraded | — | Out of tribunal scope (advisory) | No | (per EXT-002) |

**Sole full-certification blocker: A-1.**

---

## SECTION 09 — Certification Scope Analysis (market vs news vs macro)

**Determination: market-layer certification CAN be assessed independently of news and macro.**

- **News (CAP-08):** advisory-only, supplementary (SDM-CONST-10), computationally isolated from CAP-12/13/15/16 (VAL05 / INV-09 / FORB-03). Empty news is constitutionally permitted. The market evidence path's validity does not depend on it.
- **Macro (Trading Economics):** not consumed by any module (EXT-001: available, not wired into MOD-02). Zero bearing on the market path.
- The market/technical layer is the **primary** evidence layer (SDM-CONST-10) and self-contained: CAP-01 → CAP-02 → CAP-05/06/07 → CAP-10/11 → CAP-17. Its correctness is independent of the supplementary layers.

**Separation is valid.** Market-layer certification is therefore evaluated on its own merits — and is blocked solely by A-1.

---

## SECTION 10 — Final Verdict

**B — PARTIALLY_CERTIFIED.**

- **Certified:** CAP-01, CAP-05, CAP-06, CAP-07, CAP-10, CAP-17 operate correctly on genuine Upstox data; audit integrity, governance independence, and human authority all survive real data intact. CAP-11 is valid-by-construction (prior evidence), unexercised on real data (L-1).
- **Not certified:** the cross-verification gate (CAP-02) — its constitutional precondition (SDM-02 Rule 2, two independent sources) is unmet at runtime (A-1).
- **Not C:** the path is not fundamentally broken — every capability is sound, the architecture is compliant, and the defect is a single isolated wiring/credentialing gap. **Not A:** a constitutional precondition for signal execution is unsatisfied, so full market-layer certification cannot be granted.

A-2 is recorded as a non-fatal observability open item; it does not change the verdict.

---

## SECTION 11 — Authorization Decision (PLAN-003)

**PLAN-003_MULTI_SYMBOL_UNIVERSE is NOT authorized to begin.**

- PLAN-003 remains **constitutionally authorized as a design** (prior verification: no SDM/SADR/AF/ADR amendment required). That standing is unchanged.
- **Operationally, it is gated.** The governing principle of this verification chain is *certification before expansion*. The single-symbol market path is only **partially certified**: its root cross-verification gate (CAP-02) does not meet SDM-02 Rule 2. Expanding to a universe would replicate A-1 across **every** symbol (each self-compared), propagating an unmet constitutional precondition at scale rather than resolving it.
- Therefore, authorization to **begin** PLAN-003 is **withheld until the single-symbol market path is fully certified** — i.e., until A-1 is resolved such that CAP-02 cross-verifies across two genuinely independent sources. (Per task constraints, no remediation roadmap, repair, or solution is offered here — only the certification gate determination.)

---

*VER-002 is a certification tribunal output. No code, architecture, governance, persistence, or scope was modified; no fix, migration, or optimization was performed. The `data/` SQLite stores are gitignored, ephemeral artifacts recreated by the confirmatory live run.*

*End of VER-002_MARKET_DATA_CERTIFICATION_REPORT.*

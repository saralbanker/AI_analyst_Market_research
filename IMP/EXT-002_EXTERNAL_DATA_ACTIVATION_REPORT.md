# EXT-002 — EXTERNAL DATA ACTIVATION REPORT

**Protocol:** EXT_002_EXTERNAL_DATA_ACTIVATION_VERIFICATION_PROTOCOL
**Mode:** Activation Certification Tribunal — runtime evidence first, adversarial, certification only. No implementation, no optimization, no repair.
**Date:** 2026-06-20
**Scope:** Single-symbol vertical slice (RELIANCE). Vendors in scope: Upstox (market data), Finnhub (news/sentiment).
**Conflict rule applied:** Runtime behaviour overrides assumptions; observed vendor responses override code intent; unknown stays UNKNOWN until proven.

---

## HEADLINE TRUTH

The advisory cycle's **primary evidence layer (technical/market data) is operating on real Upstox data — PROVEN.** The **supplementary layer (Finnhub news/sentiment) is NOT delivering live data for the production symbol** and silently degrades to empty via a swallowed adapter error. In live mode the constitutional **two-independent-source guarantee of CAP-02 (SDM-02 Rule 2) is not satisfied** — only one real market vendor is wired, and it is cross-verified against itself.

**Final verdict: B — PARTIALLY_CERTIFIED.**

> ⚠️ Note: `CLAUDE.md` is now stale — it states "Upstox and Trading Economics are in stub mode." Observed `src/.env` state: **Upstox = configured (key/secret/access-token all set), Finnhub = configured, Trading Economics = empty (stub).** The adapter HTTP bodies that EXT-001 left as `NotImplementedError` are now fully implemented.

---

## SECTION 01 — AUTHENTICATION_VERIFICATION

**Upstox — PASS.** Full `python -m src.main` run executed two live `GET https://api.upstox.com/v2/historical-candle/...` calls with `Authorization: Bearer <access_token>`; the cycle completed without an `AdapterError`/abort, and real candles were persisted (Section 02). A 401/403 would have raised `AdapterError → CrossVerificationFailure → cycle_aborted`; no such abort occurred. Authentication is therefore proven by successful authorized retrieval.

**Finnhub — PASS (key valid).** Direct probe with the configured key:
- `GET /company-news?symbol=AAPL` → **HTTP 200, 250 records** (proves the key authenticates).
- `GET /company-news?symbol=RELIANCE` → HTTP 200, 0 records.
- `GET /company-news?symbol=RELIANCE.NS` → **HTTP 403** "You don't have access to this resource."
- `GET /news-sentiment?symbol=AAPL` → **HTTP 403** "You don't have access to this resource." (premium endpoint, not on this tier).

**Trading Economics — N/A (out of scope; credentials empty → `StubMacroAdapter`).**

**Classification: PASS** (both in-scope vendors authenticate).

---

## SECTION 02 — MARKET_DATA_VERIFICATION

**Upstox OHLCV retrieval — PASS, real data PROVEN.** Persisted `market_baselines` after the live run:

| Property | Observed | Fixture signature (falsified) |
|---|---|---|
| bar_count | 59 (~90 calendar days of trading) | 60 |
| first bar | `{day:0, open:1400.0, high:1415.6, low:1391.0, close:1407.8, volume:18,979,554}` | open 2000.0 |
| last bar | `{day:58, close:1309.5, volume:24,887,034}` | monotonic up |
| close range | 1258.8 – 1463.6 (realistic NSE RELIANCE) | flat/2000-based |
| distinct closes | 58 of 59 | low |
| monotonic increasing | **False** | True |
| any close == 2000.0 | **False** | True |

The data fails every fixture signature (the fixture is a monotonic uptrend anchored at 2000.0) and matches real RELIANCE NSE price/volume magnitudes. Regime classified **BEARISH** (fixture yields BULLISH). **This is genuine Upstox market data.**

- **Instrument lookup — PASS.** `SYMBOL_TO_INSTRUMENT_KEY["RELIANCE"] = "NSE_EQ|INE002A01018"` (correct RELIANCE ISIN) used in the live URL.
- **Parsing — PASS.** Most-recent-first candles re-sorted chronological; OHLCV mapped to bar shape; passed `cap_data_quality.validate_bars` and CAP-02.
- **Timestamp validity — CANNOT BE VERIFIED (anomaly A-2).** The adapter **discards** the real candle timestamp (`candle[0]`) and substitutes a synthetic `day` index `0..n-1`. No `timestamp` field reaches the bar; `validate_bars`' future-timestamp guard is conditional on `if present` and therefore never executes on live data. Real temporal validity is structurally unobservable in the persisted record.

**Classification: PASS** (retrieval/lookup/parsing proven real; timestamp validity unverifiable — noted as anomaly, not a retrieval failure).

---

## SECTION 03 — NEWS_VERIFICATION

**News retrieval — FAIL (for the production symbol).** Live cycle audit: `MOD-03 CAP-08 sentiment_fetched {"count": 0}`. Direct probe proves the cause is not "quiet news day":
- `company-news?symbol=RELIANCE` returns 0 records (US-centric coverage; NSE symbol unsupported on this tier).
- `company-news?symbol=RELIANCE.NS` returns **403** (no entitlement).

**Sentiment retrieval — FAIL (endpoint not entitled).** `FinnhubNewsAdapter.fetch_sentiment` unconditionally calls `/news-sentiment`, which returns **403 on this tier even for AAPL**. `raise_for_status()` → `RequestException` → `AdapterError`. `cap08_sentiment.fetch_sentiment` **catches `AdapterError` and returns `[]` silently**. Consequence: even when `/company-news` has data, the method aborts on the 403 and yields `[]`. For RELIANCE, sentiment is empty for two compounding reasons (no NSE news coverage **and** premium-endpoint 403).

**Constitutional note (not an exoneration):** News is advisory-only and supplementary (SDM-CONST-10; CAP-08; VAL05 / INV-09). An empty sentiment set does **not** block the cycle and is constitutionally permissible (`StubNewsAdapter` returns `[]` by design). However, for the EXT-002 mission — "operating on real external data" — the news layer is **not live**: it is functionally equivalent to the stub.

**Classification: FAIL** (no real news/sentiment data for the production symbol; silent degradation masks it).

---

## SECTION 04 — DATA_QUALITY_VERIFICATION

- **CAP-01 ingestion — PASS.** Real bars ingested, `data_quality` validation passed on live data (no malformed/duplicate/gap rejection).
- **CAP-02 cross-verification — PROVEN STRUCTURAL DEFECT (anomaly A-1).** `market_data.run()` obtains both series from `get_market_adapter(variant="a")` and `(variant="b")`. In live mode `factory.get_market_adapter` **ignores `variant`** and returns `UpstoxMarketAdapter` for both. CAP-02 therefore compares **Upstox against Upstox** — identical payloads, `diff = 0`, well within `TOLERANCE = 0.01`. The gate passes **vacuously**. `SDM-02 Rule 2` ("metrics must be cross-verified across at least two **independent** sources before signal logic executes") and SADR CAP-02 are **not satisfied**: there is exactly one real market source, self-compared. (Empty `ALPHA_VANTAGE_API_KEY` / `TWELVE_DATA_API_KEY` exist in `.env` but are **not wired** into the market factory.)

**Falsification attempt:** I attempted to find a genuine second source — none exists in the factory. The "two vendors" are an artifact of the fixture era (`vendor_a_bars` vs `vendor_b_bars`), collapsed to one in live mode.

**Classification: FAIL** (CAP-01 real and valid, but CAP-02's independent-source guarantee is structurally violated in live mode).

---

## SECTION 05 — FAILURE_RECOVERY_VERIFICATION

- **Market path — PASS (fails safe, no silent fixture fallback).** On `AdapterError`, `market_data.run` raises `CrossVerificationFailure`; `main.run_cycle` records `cycle_aborted` and returns `aborted:true`. There is **no fallback to `FixtureMarketAdapter`** on a live error — a vendor outage aborts visibly, it does not silently revert to synthetic data. (Confirmed by code path; the prior VER-001 V06 demonstrated the abort behaviour.)
- **News path — DEGRADES SILENTLY (anomaly A-3).** `cap08_sentiment` swallows `AdapterError` → `[]` with no audit of the failure reason (`sentiment_fetched count:0` is logged identically for "no news" and "vendor 403"). Constitutionally safe (advisory-only) but evidentially opaque.
- **Rate-limit / retry — UNKNOWN (not exercised).** No retry/backoff logic exists; a 429 would surface as `AdapterError` (news → `[]`; market → cycle abort). Not triggered during verification; classified UNKNOWN per the conflict rule (not asserted).

**Classification: PASS** for market fail-safe; the news silent-degradation and absence of retry are documented anomalies (A-3) / UNKNOWN.

---

## SECTION 06 — EXECUTION_VERIFICATION

`python -m src.main` (piped `reject`) executed end-to-end on live data. Observed:
- Diagnostics report Upstox + Finnhub `set`; TE/AlphaVantage/TwelveData `EMPTY (stub mode)`.
- Regime **BEARISH**, technical signal **SHORT** (strength 0.025) — derived from real Upstox bars.
- CAP-10 walk-forward **passed:false (fold disagreement)** → signal rejected → CAP-17 **null_state `NO_VALIDATED_OPPORTUNITIES`** → `decisions: []`.

**Hidden-stub scan:**
- Market data: **no stub/fixture in path** (real bars persisted; fixture signature falsified).
- News: **stub-equivalent empty result** reached via swallowed `AdapterError` (Section 03/05).
- Macro: stub (`StubMacroAdapter`) — out of scope, not consumed by MOD-02.

**Classification: PASS for market-data execution; PARTIAL** because the news limb of the path resolves to a stub-equivalent result.

---

## SECTION 07 — AUDIT_VERIFICATION

- **Audit chain — PASS.** `tools/audit_review.py --verify-chain` → `OK: 20 audit record(s), chain verified.`
- **Traceability — PASS.** Full ordered trail present: MOD-11 activation → MOD-01 CAP-01/02/03 → MOD-02 CAP-05/06 → MOD-03 CAP-07/08/09 → MOD-04 CAP-10 (reject) → MOD-09 CAP-29 → MOD-06 CAP-24..27 → MOD-05 CAP-17 → MOD-07 CAP-18 → MOD-08 CAP-21. Ordering matches ADR-006.
- **Attribution recording — PASS (correctly skipped).** `MOD-08 CAP-21 attribution_skipped {"reason":"null_state"}` — constitutionally correct (no opportunity, no decision to attribute).

**Classification: PASS.**

---

## SECTION 08 — GOVERNANCE_VERIFICATION

- Four halt states read independently; all inactive (`active_halts: []`).
- Startup recovery read governance + portfolio state before cycle work; `governance_halt_active:false`, capital 5000.0.
- Human gate (CAP-18) reached and produced `no_decision_required` under null-state (no auto-approval, no bypass).
- `AUTO_EXECUTION_ENABLED=false`, `BROKER_EXECUTION_ENABLED=false`; no execution authority anywhere.
- Boundary tests: `pytest tests/architecture` → **6 passed**.

**Classification: PASS.**

---

## SECTION 09 — STUB_ELIMINATION_VERIFICATION

| Path | State |
|---|---|
| Market data (Upstox) | **VERIFIED_REMOVED** — real data only; no fixture fallback even on error |
| News/sentiment (Finnhub) | **PARTIALLY_PRESENT** — real HTTP calls are made, but the result resolves to a stub-equivalent `[]` (no NSE coverage + premium `/news-sentiment` 403, error swallowed) |
| Macro (Trading Economics) | **PARTIALLY_PRESENT (out of scope)** — `StubMacroAdapter` active (no credentials); not consumed by any module |
| CAP-02 second source | **PARTIALLY_PRESENT** — no second real source; single vendor self-compared |

**Overall: PARTIALLY_PRESENT.**

---

## SECTION 10 — CONFLICT_ANALYSIS

| ID | Finding | Evidence | Impact | Confidence |
|---|---|---|---|---|
| **A-1** | CAP-02 cross-verifies Upstox against itself; one real source | `factory.py:21-27` ignores `variant` in live mode; `market_data.py:41-42`; `cap02` `TOLERANCE=0.01`, diff=0 vacuous pass | Violates SDM-02 Rule 2 (≥2 independent sources). The blocking gate provides no real divergence protection in live mode. | **PROVEN** |
| **A-2** | Real candle timestamps discarded; replaced by synthetic `day` index | `market.py:96-106` drops `candle[0]`; `cap_data_quality` future-check is `if present` only | Timestamp validity / staleness unverifiable on live data; cannot detect stale or future candles. | **PROVEN** |
| **A-3** | Finnhub sentiment silently degrades to `[]`; `/news-sentiment` 403 + NSE uncovered | probes (200/0, 403, 403); `cap08_sentiment` catches `AdapterError`→`[]`; audit logs only `count:0` | News layer not live for RELIANCE; failure indistinguishable from "no news" in audit. Advisory-only ⇒ no cycle/constitutional block. | **PROVEN** |
| A-4 | No retry/backoff for rate limits | code inspection; not exercised | Unknown live resilience under 429. | UNKNOWN |
| A-5 | `CLAUDE.md` adapter-status table stale (says Upstox stub) | observed `.env` + run diagnostics | Documentation drift; operator may mis-assess activation state. | PROVEN |

No defect violated audit integrity, governance boundaries, or human-authority gates.

---

## SECTION 11 — FINAL_VERDICT

**B — PARTIALLY_CERTIFIED.**

Justification (evidence-bound):
- **Real external market data is PROVEN live** (Upstox; primary evidence layer per SDM-CONST-10), and the full advisory cycle, audit chain, governance, and human gate operate correctly on it.
- **Certification is withheld from full (A)** because: (1) **A-1** — CAP-02's constitutional two-independent-source requirement (SDM-02 Rule 2) is not met in live mode (single-vendor self-comparison); (2) **A-3** — the Finnhub news/sentiment layer is not delivering live data for the production symbol and silently degrades to stub-equivalent empty; (3) **A-2** — timestamp validity is structurally unverifiable.
- **Not (C) ACTIVATION_FAILED**, because no STOP condition tripped: both vendors authenticate, real market data is proven, audit integrity holds, governance boundaries hold, and the market path contains no active stub.

---

## SECTION 12 — AUTHORIZATION_DECISION

**Progression to VER-002_EXTERNAL_DATA_CERTIFICATION: NOT AUTHORIZED as unconditional.**

Two findings are constitutional, not cosmetic, and must be adjudicated before external-data certification can be claimed:
- **A-1 (SDM-02 Rule 2):** "cross-verified across at least two **independent** sources before signal logic executes." A live single-source self-comparison does not satisfy this. Until a genuinely independent second market source is verified (or the constitution's two-source requirement is formally reconciled for the single-vendor slice), CAP-02's certification cannot extend to live operation.
- **A-3:** the supplementary evidence layer is not live and fails opaquely.

The market-data limb (Upstox) is, on its own evidence, certifiable as live. VER-002 may proceed **only** if its scope is explicitly bounded to the Upstox market-data limb with A-1/A-2/A-3 carried as open, named blockers — otherwise authorization is denied pending their resolution.

*(Per protocol: this section states the authorization determination only. No remediation roadmap, no implementation plan, and no optimization is provided.)*

---

## EVIDENCE APPENDIX (commands run, all read-only / non-mutating to source)

1. `.env` credential-state inspection (names + presence only; no values printed).
2. Static read: `src/adapters/{market,news,macro,factory}.py`, `upstox_instruments.py`, `mod01_market_data/{market_data,cap02_cross_verification,cap_data_quality}.py`, `mod03_evidence/cap08_sentiment.py`, `main.py`.
3. `rm -rf data/ && echo reject | python -m src.main` (fresh-DB live run) — captured diagnostics, Open Menu, cycle JSON.
4. SQLite inspection of `market_baselines` (bars) and `audit.db` (full trail).
5. Direct Finnhub probes (`/company-news` for RELIANCE, RELIANCE.NS, AAPL; `/news-sentiment` for AAPL).
6. `tools/audit_review.py --verify-chain` → chain verified (20 records).
7. `pytest tests/architecture` → 6 passed.

*EXT-002 performs activation verification only. No code, architecture, governance, persistence, or scope was modified. The `data/` SQLite databases are gitignored, ephemeral build artifacts recreated by the live run.*

*End of EXT-002_EXTERNAL_DATA_ACTIVATION_REPORT.*

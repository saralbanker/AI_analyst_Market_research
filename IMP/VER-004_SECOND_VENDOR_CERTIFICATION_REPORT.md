# VER-004 — SECOND VENDOR EMPIRICAL CERTIFICATION REPORT

**Protocol:** VER-004_SECOND_VENDOR_EMPIRICAL_CERTIFICATION
**Mode:** Certification tribunal — observation first, adversarial, no repair, no optimization.
**Date:** 2026-06-21
**Scope:** Dhan as CAP-02 second independent market-data vendor.
**Predecessor authorities:** VER-003 (CAP-02 independence adjudication, verdict A — two independent vendors required); DHAN_TOKEN_AUTOMATION_REPORT (token lifecycle infrastructure).
**Conflict rule:** Observed runtime evidence overrides expectations. `[OBSERVED]` = direct runtime output or HTTP response. `[INFERENCE]` = derived. `[INSUFFICIENT EVIDENCE]` = cannot be resolved from available data.

---

## §01 — RUNTIME ENVIRONMENT

**[OBSERVED] System state at certification run time (2026-06-21 ~09:00 UTC):**

| Variable | State |
|---|---|
| `UPSTOX_API_KEY` | SET (len=36) |
| `UPSTOX_API_SECRET` | SET (len=10) |
| `UPSTOX_REDIRECT_URI` | SET |
| `UPSTOX_ACCESS_TOKEN` | SET (len=337) — JWT, expires 2027-06-16T22:00:00 UTC (~360 days remaining) |
| `DHAN_CLIENT_ID` | **EMPTY** |
| `DHAN_CLIENT_SECRET` | **EMPTY** |
| `secrets/dhan_token.json` | **ABSENT** |
| `logs/token_refresh.log` | **ABSENT** |
| Python version | 3.14.4 |
| Test suite | 51/51 passed (pre-certification baseline) |
| Architecture tests | 6/6 passed |

**[OBSERVED] Factory adapter selection (post config load):**
```
variant="a"  →  UpstoxMarketAdapter   (Upstox credentials present)
variant="b"  →  FixtureMarketAdapter  (DHAN_CLIENT_ID absent)
```

**[OBSERVED] Current live full-cycle outcome:**
```json
{
  "cycle_id": "61f1bef8-3c55-40c4-a751-1288d2d4506b",
  "aborted": true,
  "reason": "source bar counts differ"
}
```
The live cycle cannot complete in the present configuration. This is a newly introduced condition (see §12 — failure mode F-4).

---

## §02 — DHAN AUTHENTICATION VALIDATION

**[OBSERVED] Dhan API server reachability:**
The Dhan API at `https://api.dhan.co` is live and serving responses. All probed endpoints returned deterministic HTTP responses (no timeout, no ConnectionError).

**[OBSERVED] Token endpoint probe results:**

| Endpoint | Method | HTTP response | Interpretation |
|---|---|---|---|
| `/v2/token` | POST | 404 `Not Found` | Endpoint does not exist |
| `/token` | POST | 200 HTML | Web login page, not a token API |
| `/v2/tokenGenerate` | POST | 404 `Not Found` | Does not exist |
| `/v2/generateAccessToken` | POST | 404 `Not Found` | Does not exist |
| `/oauth2/token` | GET | 200 HTML | OAuth login page redirect, not a token API |

**[INFERENCE]** No programmatic token generation endpoint has been located. The correct token acquisition URL is unknown without Dhan KYC completion and documentation access. The `DHAN_TOKEN_URL` default (`https://api.dhan.co/v2/token`) in `scripts/generate_dhan_token.py` is **incorrect** (404 confirmed).

**[OBSERVED] Auth header pattern (discovered via live probing):**
- Headers `access-token: <token>` + `X-Client-Id: <id>` → HTTP 401, error `DH-901` ("Client ID or user generated access token is invalid or expired.")
- Headers `Authorization: Bearer <token>` + `X-Client-Id: <id>` → HTTP 400, error `DH-905` ("Missing required fields") — auth check not reached; server rejects before auth validation when `Authorization:` used without `access-token:`.
- No auth headers → HTTP 400, error `DH-905`.

**[INFERENCE]** The correct Dhan authentication headers are `access-token` and `X-Client-Id`. The `Authorization: Bearer` pattern is NOT the correct Dhan pattern. The `DhanMarketAdapter` implementation uses `Authorization: Bearer` — this is an implementation defect (see §12 — defect D-2).

**[OBSERVED] Credential acquisition attempt:**
```
$ python scripts/generate_dhan_token.py
ERROR: DHAN_CLIENT_ID is not set. Add it to src/.env.
Exit code: 1
```
Token acquisition blocked by absent credentials. No network call was made to Dhan.

**Classification: BLOCKED.** Authentication cannot be validated without credentials.

---

## §03 — INSTRUMENT IDENTITY VALIDATION

**[OBSERVED] Dhan instruments registry (publicly accessible):**
`https://images.dhan.co/api-data/api-scrip-master.csv` — HTTP 200, 30.1 MB, 237,788 rows.

**[OBSERVED] RELIANCE NSE entry in Dhan instruments CSV:**

| Field | Observed value |
|---|---|
| `SEM_EXM_EXCH_ID` | `NSE` |
| `SEM_SEGMENT` | `E` |
| `SEM_SMST_SECURITY_ID` | **`2885`** |
| `SEM_INSTRUMENT_NAME` | `EQUITY` |
| `SEM_TRADING_SYMBOL` | `RELIANCE` |
| `SEM_SERIES` | `EQ` |
| `SEM_EXCH_INSTRUMENT_TYPE` | `ES` |
| `SM_SYMBOL_NAME` | `RELIANCE INDUSTRIES LTD` |

**[OBSERVED] Implementation defect — security ID mismatch (defect D-1):**
`src/adapters/dhan_instruments.py::SYMBOL_TO_SECURITY_ID["RELIANCE"]` is `"1333"`.
The authoritative Dhan instruments CSV records RELIANCE NSE as `"2885"`.
`"1333"` does not appear in the instruments CSV for any NSE equity entry. This is incorrect.

**[INFERENCE]** With security ID `"1333"`, any live Dhan OHLCV request for RELIANCE would either retrieve data for a different instrument or return an error. The CAP-02 cross-verification gate would receive incorrect or absent data.

**[OBSERVED] Correct mapping derived from authoritative source:**
- NSE RELIANCE INDUSTRIES: `securityId="2885"`, `exchangeSegment="NSE_EQ"` (or segment code `E`)
- BSE RELIANCE INDUSTRIES: `securityId="500325"`, `exchangeSegment="BSE_EQ"` (or segment code `E`)

**Classification: FAIL (defect D-1 confirmed).** Correct security ID is known and documented above; the implementation is wrong.

---

## §04 — OHLCV RETRIEVAL VALIDATION

**[OBSERVED] Dhan OHLCV endpoint behavior (unauthenticated/invalid-auth probe):**

```
POST https://api.dhan.co/v2/charts/historical
payload: {securityId: "2885", exchangeSegment: "NSE_EQ", instrument: "EQUITY",
          expiryCode: 0, oi: false, fromDate: "2026-03-01", toDate: "2026-06-20", type: "Day"}
no auth  →  HTTP 400  DH-905 "Missing required fields"
with access-token headers → HTTP 401  DH-901 "Client ID or user generated access token is invalid or expired"
```

**[INFERENCE]** The endpoint exists and validates auth before returning data. HTTP 401 confirms the endpoint is auth-guarded and would respond to valid credentials.

**[OBSERVED] Upstox OHLCV retrieved for baseline (live, confirmed):**
- 59 bars, chronological, day indices 0–58
- First bar: `{day:0, open:1400.0, high:1415.6, low:1391.0, close:1407.8, volume:18,979,554}`
- Last bar: `{day:58, open:1328.0, high:1338.2, low:1305.3, close:1309.5, volume:24,887,034}`
- Close range: 1258.80 – 1463.60
- Source: NSE RELIANCE live candles, ~90 calendar days

**[INSUFFICIENT EVIDENCE]** Dhan OHLCV data for RELIANCE cannot be retrieved. Credentials absent. Whether Dhan can serve this data is empirically unknown.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §05 — TIMESTAMP ALIGNMENT

**[OBSERVED]** Both Upstox and Dhan adapters discard raw timestamps. Upstox re-indexes candles to `day:0..n-1`; Dhan adapter design does the same (`enumerate(zip(opens, highs, ...))` → day index). No timestamp field reaches the canonical bar shape from either adapter.

**[INSUFFICIENT EVIDENCE]** Dhan OHLCV not retrieved. The number of trading days Dhan would return for the same 90-calendar-day window is unknown. Upstox returns 59 bars; whether Dhan returns the same 59 days is empirically unverifiable without live Dhan data.

**[OBSERVED contextual finding]** Timestamp loss was previously documented as anomaly A-2 (EXT-002). This anomaly is structurally unchanged for both vendors: neither adapter preserves the actual trade date, only a synthetic index. Cross-verification can only compare by position (day index 0..n-1), making it sensitive to bar count differences between vendors.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §06 — INTERVAL ALIGNMENT

**[INSUFFICIENT EVIDENCE]** Dhan OHLCV not retrieved. It is unknown whether Dhan and Upstox would return the same set of trading days for any given date range. If they differ (e.g., one counts a day the other treats as a holiday), `cross_verify()` would raise `CrossVerificationFailure("source bar counts differ")` before any price comparison. This would be a genuine blocking divergence, not a false alarm, but its likelihood is empirically unverifiable.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §07 — CORPORATE-ACTION DIFFERENCES

**[INSUFFICIENT EVIDENCE]** No Dhan data retrieved. Dhan and Upstox may apply different corporate-action adjustment methodologies (e.g., back-adjustment of historical prices for dividends and splits). For RELIANCE, any adjustment difference would manifest as systematic close-price divergence. Whether this would exceed the `TOLERANCE = 0.01` (1%) threshold in `cross_verify()` is empirically unknown.

**[OBSERVED]** Upstox applies corporate-action adjustment at the vendor level (adjusted prices delivered). Whether Dhan applies equivalent adjustment is unknown.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §08 — MISSING-BAR ANALYSIS

**[INSUFFICIENT EVIDENCE]** Dhan data not retrieved. Whether Dhan omits any bars that Upstox includes (or vice versa) for the same 90-day window is unknown.

**[OBSERVED contextual finding]** `cross_verify()` would fail immediately on a bar count mismatch (`len(bars_a) != len(bars_b)`). Any structural missing-bar disagreement between vendors would correctly trip the gate before price comparison begins. This is the correct constitutional behavior.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §09 — PRECISION ANALYSIS

**[OBSERVED]** Upstox delivers prices as floats with 1 decimal place (e.g., 1407.8, 1309.5). Indian exchange tick sizes for large-cap equities are typically ₹0.05. Upstox rounds to 1 decimal.

**[OBSERVED]** Dhan instruments CSV records `SEM_TICK_SIZE: 10.0000` for RELIANCE. This may indicate a different precision convention or a CSV artifact.

**[INSUFFICIENT EVIDENCE]** Dhan price precision in OHLCV response is unknown. If Dhan delivers prices at a different precision (e.g., 2 decimal places vs Upstox's 1), the fractional `diff = abs(a-b)/abs(a)` in `cross_verify()` could still pass within tolerance, or may systematically differ. Empirically unverifiable without live data.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §10 — CROSS-VERIFICATION BEHAVIOR

**[OBSERVED] Genuine divergence rejection (confirmed operative):**
```python
cross_verify(
    [{..., "close": 1000.0}],
    [{..., "close": 1020.0}]   # 2% divergence
)
# → CrossVerificationFailure("close price mismatch on day 0: 1000.0 vs 1020.0 (diff=0.0200)")
```
The gate correctly rejects >1% price divergence. TOLERANCE = 0.01 is enforced.

**[OBSERVED] Genuine convergence pass (confirmed operative):**
```python
cross_verify(
    [{..., "close": 1000.0}],
    [{..., "close": 1000.5}]   # 0.05% diff
)
# → returns bars_a (pass)
```
The gate correctly accepts <1% price divergence.

**[OBSERVED] Bar count mismatch — current live state:**
Upstox (variant=a): 59 bars; FixtureMarketAdapter (variant=b): 60 bars.
`cross_verify()` raises `CrossVerificationFailure("source bar counts differ")` immediately.
The live advisory cycle currently aborts at CAP-02.

**[OBSERVED] Pre-DHAN_TOKEN_AUTOMATION state (from EXT-002 §04):**
Both variant="a" and "b" returned `UpstoxMarketAdapter` (variant argument ignored), yielding identical 59-bar series. `diff = 0` → gate passed vacuously. This was the A-1 condition.

**[OBSERVED] Post-DHAN_TOKEN_AUTOMATION state (this certification):**
variant="b" now returns `FixtureMarketAdapter(variant="b")` when `DHAN_CLIENT_ID` is absent. Fixture yields 60 synthetic bars (closes 2000.0–2295.0). Upstox yields 59 real bars. The gate raises `CrossVerificationFailure("source bar counts differ")`. The system is in a degraded state relative to EXT-002 — the cycle can no longer complete even in the interim Dhan-absent configuration.

**[INFERENCE]** The factory change from DHAN_TOKEN_AUTOMATION (which routes variant="b" to Dhan/Fixture) eliminated the vacuous Upstox-vs-Upstox pass but introduced a new failure mode: when Dhan is unconfigured, the cycle aborts on bar count rather than completing with the old vacuous gate.

**Classification: OBSERVED defect F-4 (regression; see §12). Cross-verify logic itself is correct.**

---

## §11 — RATE-LIMIT OBSERVATIONS

**[OBSERVED]** Seven HTTP requests made to `api.dhan.co` during this certification run. All returned within 8 seconds. No rate-limit response (HTTP 429) was received.

**[INSUFFICIENT EVIDENCE]** Dhan's API rate limits, daily request quotas, and behavior under sustained load are unknown. Cannot be tested without valid credentials.

**Classification: INSUFFICIENT EVIDENCE.**

---

## §12 — FAILURE-MODE ANALYSIS

| ID | Failure | Source | Evidence | Severity |
|---|---|---|---|---|
| **D-1** | Wrong RELIANCE security ID in `dhan_instruments.py` | `SYMBOL_TO_SECURITY_ID["RELIANCE"] = "1333"` | Instruments CSV RELIANCE NSE = `2885`; `1333` not found as NSE equity | **CRITICAL** |
| **D-2** | Wrong auth header in `DhanMarketAdapter` | `"Authorization": f"Bearer {self._access_token}"` | Dhan requires `access-token: <token>` header; `Authorization: Bearer` causes HTTP 400 (auth check not reached) | **CRITICAL** |
| **D-3** | Wrong token endpoint URL | `DEFAULT_TOKEN_URL = "https://api.dhan.co/v2/token"` | Endpoint returns HTTP 404 | **CRITICAL** |
| **F-1** | Dhan credentials absent | `DHAN_CLIENT_ID=EMPTY`, `DHAN_CLIENT_SECRET=EMPTY` | Startup diagnostics observed | BLOCKING (external) |
| **F-2** | Token file absent | `secrets/dhan_token.json` does not exist | `ls secrets/` | BLOCKING (follows F-1) |
| **F-3** | DHAN_TOKEN_AUTOMATION programmatic token endpoint unknown | No `/v2/token` exists | All candidate endpoints probed: 404 | BLOCKING |
| **F-4** | **Factory regression** — cycle aborts when Dhan unconfigured | `variant="b"` → `FixtureMarketAdapter(variant="b")` → 60 bars vs Upstox 59 → `CrossVerificationFailure` | Live cycle output: `"aborted": true, "reason": "source bar counts differ"` | **REGRESSION** |

**Summary of defects requiring correction before any live Dhan testing is possible:**
- D-1: correct security ID to `2885`
- D-2: change auth header to `access-token` (not `Authorization: Bearer`)
- D-3: determine correct token endpoint from Dhan documentation post-KYC
- F-4: interim fallback behavior when Dhan unconfigured must not abort the live Upstox cycle (this regression must be repaired before system can return to EXT-002 PARTIALLY_CERTIFIED baseline)

---

## §13 — CAP-02 CONSTITUTIONAL COMPLIANCE

**[OBSERVED] Constitutional requirement (VER-003 §09):**
> "Two independent market-data vendors — distinct provider entities whose data pipelines share no common upstream failure mode — each supplying NSE/BSE OHLCV for the same data point, compared at a synchronous hard blocking gate before any signal logic runs."

**[OBSERVED] Current system compliance status:**

| Requirement | Status |
|---|---|
| Two independent vendors (vendor layer) | **NOT MET** — only Upstox serves live data; Dhan credentials absent |
| Same data point (RELIANCE OHLCV) | **CANNOT VERIFY** — Dhan not reachable |
| Synchronous blocking gate (CAP-02) | **OPERATIVE** — cross_verify() logic confirmed functional |
| Gate genuinely rejects divergence | **CONFIRMED** — 2% divergence case tested and rejected |
| Gate genuinely passes convergence | **CONFIRMED** — <1% case tested and passed |
| Pipeline not blocked by vacuous pass | **INAPPLICABLE** — pipeline is blocked by regression F-4 |

**[OBSERVED] New state introduced by DHAN_TOKEN_AUTOMATION factory change:**
The A-1 condition (vacuous Upstox-vs-Upstox self-comparison) no longer exists. In its place, the cycle aborts immediately on bar count mismatch (Upstox 59 bars vs Fixture 60 bars). CAP-02 now fails loudly rather than passing silently. This is constitutionally more honest (a genuine rejection rather than a vacuous pass), but it is operationally worse: no advisory cycle can complete until Dhan credentials are configured or the fallback is corrected.

**[INFERENCE] VER-003 verdict A compliance determination:**
The constitutional two-independent-vendor requirement remains **NOT SATISFIED**:
- Dhan is not yet an operational second vendor (credentials absent, three implementation defects)
- The fallback to FixtureMarketAdapter for variant="b" is not a constitutional second vendor (VER-003 §03 ruled "synthetic/fixture paths FAIL constitutional independence test")
- The factory regression prevents any live cycle from completing

**Classification: CERTIFICATION_DENIED.**

Basis: Dhan cannot be empirically certified as a second independent vendor because (a) credentials are absent, blocking all live tests; (b) three implementation defects (D-1, D-2, D-3) are confirmed that would prevent correct operation even with credentials; (c) the factory change introduced a regression (F-4) that prevents the current live system from completing any advisory cycle.

---

## §14 — PAPER-TRADING GATE DETERMINATION

**BLOCKED.**

CAP-02's two-independent-vendor precondition remains unmet. VER-003 §07 held: "Paper trading MAY NOT proceed under the current partial certification." The conditions from VER-003 are not improved by this certification; they are unchanged plus the F-4 regression.

Paper trading gate: **BLOCKED** (inherits from VER-003; not resolved by this certification).

---

## §15 — PLAN-003 GATE DETERMINATION

**BLOCKED.**

VER-003 §08 held: "PLAN-003 remains NOT AUTHORIZED; certification precedes expansion." CAP-02 independence is still unmet. Multi-symbol expansion before resolving the single-symbol two-vendor requirement would replicate the constitutional defect at scale.

PLAN-003 gate: **BLOCKED** (unchanged).

---

## §16 — EXECUTIVE RULING

**Verdict: C — CERTIFICATION_DENIED.**

### Basis

**[OBSERVED] Dhan infrastructure is live and structurally sound:**
- `api.dhan.co` is reachable, serving valid HTTP responses.
- `/v2/charts/historical` endpoint exists and applies auth validation (`DH-901` with invalid token).
- The instruments registry (`api-scrip-master.csv`) is accessible and authoritative.
- RELIANCE NSE is listed in Dhan's universe: `securityId=2885`, `exchangeSegment=NSE_EQ`.

**[OBSERVED] Three implementation defects block live operation:**
1. **D-1**: `dhan_instruments.py` encodes `RELIANCE → "1333"`. Correct ID is `"2885"` (authoritative source: Dhan instruments CSV, 2026-06-21). Any live request would query the wrong instrument.
2. **D-2**: `DhanMarketAdapter` uses `Authorization: Bearer` header. Dhan's API requires `access-token` header. Confirmed by live probing: `Authorization: Bearer` reaches the server but triggers `DH-905` (input exception) rather than `DH-901` (auth failure) — auth check is not reached.
3. **D-3**: `generate_dhan_token.py` default token URL (`/v2/token`) returns HTTP 404. The correct programmatic token endpoint is unknown and must be obtained from Dhan post-KYC.

**[OBSERVED] One regression degrades system below EXT-002 baseline:**
4. **F-4**: The factory change in DHAN_TOKEN_AUTOMATION routes `variant="b"` to `FixtureMarketAdapter(variant="b")` when Dhan is unconfigured. Fixture returns 60 synthetic bars; Upstox returns 59 real bars. `cross_verify()` raises `CrossVerificationFailure("source bar counts differ")`. The live advisory cycle now **aborts on every run** rather than completing (as it did under the EXT-002 A-1 vacuous-pass condition). The system is operationally degraded.

**[OBSERVED] Credential state prevents empirical testing:**
The 10 empirical questions posed by this certification (OHLCV retrieval, timestamp alignment, interval alignment, corporate-action differences, missing-bar analysis, precision, convergence/divergence of real data, rate limits) cannot be answered without `DHAN_CLIENT_ID`, `DHAN_CLIENT_SECRET`, and a valid `secrets/dhan_token.json`.

**[INFERENCE] Bounded INSUFFICIENT-EVIDENCE declarations (do not affect verdict):**
1. Whether Dhan serves RELIANCE NSE OHLCV for the same 90-day window as Upstox.
2. Whether bar counts would align between vendors (same trading days).
3. Whether corporate-action adjustments would fall within the 1% tolerance.
4. What the correct programmatic token endpoint is.

**This report renders an empirical certification determination only. It prescribes no fixes, no architecture, no roadmap, and no optimization.** The observed defects and regression are stated as facts. No code was modified during this certification run.

---

## EVIDENCE APPENDIX (commands run — all read-only to source, no source modification)

1. `src/.env` credential-state inspection (key presence + length only; no values).
2. `python scripts/generate_dhan_token.py` → exit 1 (no credentials).
3. `python tools/check_dhan_token.py` → FAIL (file absent).
4. Factory adapter selection probe (variant=a, variant=b) — code read and runtime test.
5. Live Upstox OHLCV fetch → 59 bars, confirmed real.
6. HTTP probes to `api.dhan.co`: `/v2/token`, `/token`, `/v2/tokenGenerate`, `/v2/generateAccessToken`, `/oauth2/token`, `/v2/charts/historical` (multiple payload/header variants).
7. Dhan instruments CSV fetch (`images.dhan.co/api-data/api-scrip-master.csv`) → 237,788 rows; RELIANCE NSE entry extracted.
8. Upstox JWT decode → expiry 2027-06-16 (~360 days remaining).
9. `cross_verify()` divergence and convergence tests (synthetic data; no vendor calls).
10. Current full-cycle run (`python -m src.main --mode on-demand`) → `aborted:true, reason:source bar counts differ`.
11. Source inspection: `DhanMarketAdapter.fetch_ohlcv` auth headers, `dhan_instruments.py` security ID, `cap02_cross_verification.py` tolerance logic.
12. `pytest` → 51/51 (unchanged; architecture tests 6/6).

*No source file, database, configuration, or governance artifact was modified. No network call was made with real Dhan credentials (none exist). No synthetic data was passed through the live pipeline. All findings are derived from direct observation.*

**— END VER-004 —**

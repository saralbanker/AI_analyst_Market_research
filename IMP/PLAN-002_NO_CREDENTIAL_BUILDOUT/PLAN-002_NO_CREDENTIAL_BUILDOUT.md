# PLAN-002: No-Credential Buildout to Paper-Trading Readiness

**Status:** PLAN (awaiting REVIEW before EXECUTE, per constitution)
**Supersedes scope of:** PCP-001 execution queue (M1 -> M4 -> M2 -> M3 -> R1 -> R2)
**Constraint:** Upstox (and Finnhub / Trading Economics) API credentials are **not yet available**.
Everything in this plan must work, and be testable, with `src/.env` left exactly as-is
(empty vendor keys). No step requires a live network call to succeed.

---

## Goal

Close the four gaps from the PCP-001 re-verification (F-A..F-D) so that:

1. The system runs end-to-end today, on fixture data, without crashing or making
   stray network calls.
2. The moment real Upstox/Finnhub/Trading Economics credentials are dropped into
   `src/.env`, the system switches to live adapters **with zero code changes**
   ("credential insertion only" — EXT-001 invariant).
3. Drawdown-based governance halts (State 3) actually function during paper trading.
4. A real functional test suite exists and is the merge gate.

---

## M1 — Fix adapter factory selection (F-A, CRITICAL)

**File:** `src/adapters/factory.py`

**Problem:** Each `get_*_adapter()` constructs the real-vendor adapter and calls a
"probe" method (`fetch_ohlcv("__probe__")`, `fetch_sentiment("__probe__")`,
`fetch_indicators()`) to decide whether to fall back to a stub. Once those methods
contain real HTTP code (M4 below), this probe becomes a real network call on
*every* startup — for a bogus symbol — and any transient network error crashes
startup instead of falling back.

**Fix:** Replace the behaviour-probe with a **config-presence check**. No
construction-time network calls, ever.

```python
def get_market_adapter(variant: str = "a") -> MarketAdapter:
    if all(os.environ.get(k) for k in ("UPSTOX_API_KEY", "UPSTOX_API_SECRET", "UPSTOX_ACCESS_TOKEN")):
        return UpstoxMarketAdapter(
            api_key=os.environ["UPSTOX_API_KEY"],
            api_secret=os.environ["UPSTOX_API_SECRET"],
            access_token=os.environ["UPSTOX_ACCESS_TOKEN"],
        )
    return FixtureMarketAdapter(variant=variant)
```

Same pattern for `get_news_adapter` (`FINNHUB_API_KEY`) and `get_macro_adapter`
(`TRADING_ECONOMICS_API_KEY` + `TRADING_ECONOMICS_SECRET`).

`AdapterNotConfigured` stays on each real adapter class as a defensive
double-check inside `fetch_*` (cheap, no behaviour change), but the factory no
longer relies on catching it.

**Why this is safe without credentials:** with all vendor keys empty (current
`.env`), every `get_*_adapter()` returns the stub/fixture adapter — identical
runtime behaviour to today, just without the probe call.

**Test (new):** `tests/unit/adapters/test_factory.py`
- empty env -> returns `FixtureMarketAdapter` / `StubNewsAdapter` / `StubMacroAdapter`
- env with all Upstox vars set (dummy strings) -> returns `UpstoxMarketAdapter`,
  *without* calling any of its methods (use `unittest.mock` to assert no HTTP
  client method is invoked at construction time)

---

## M4 — Implement adapter bodies with recorded-response fixtures (F-D, HIGH)

**Files:** `src/adapters/market.py`, `src/adapters/news.py`, `src/adapters/macro.py`,
new `tests/fixtures/vendor_responses/`

**Problem:** `fetch_*` bodies are `NotImplementedError`. Cannot write/test real
HTTP integration without credentials — but we *can* write the real implementation
now and validate it against recorded (cassette-style) responses, so it's ready
the instant a key is inserted.

**Approach — "implement against a recorded fixture, not a live call":**

1. Add `requests` (or reuse an existing HTTP lib already in the project — check
   `pyproject.toml`/`requirements.txt` first) as the HTTP client.
2. Implement `UpstoxMarketAdapter.fetch_ohlcv(symbol)`:
   - Build the request (Upstox historical candle endpoint, auth header from
     `access_token`).
   - Parse the JSON response into the `{"day", "open", "high", "low", "close",
     "volume"}` shape required by `cap_data_quality.validate_bars`.
   - Raise a clear `AdapterError` (new exception) on non-200 / malformed JSON —
     do **not** let raw `requests` exceptions escape (keeps `main.py` error
     handling in `CrossVerificationFailure` / cycle-abort path intact).
3. Same for `FinnhubNewsAdapter.fetch_sentiment` and
   `TradingEconomicsMacroAdapter.fetch_indicators`.
4. Add **recorded response fixtures** (hand-written JSON, shaped like real vendor
   payloads — copy field names from each vendor's public API docs):
   - `tests/fixtures/vendor_responses/upstox_ohlcv_sample.json`
   - `tests/fixtures/vendor_responses/finnhub_sentiment_sample.json`
   - `tests/fixtures/vendor_responses/trading_economics_indicators_sample.json`
5. **Contract tests** (`tests/unit/adapters/test_market_upstox.py`, etc.):
   mock the HTTP layer to return the recorded fixture JSON, call
   `fetch_ohlcv("RELIANCE")`, assert the returned shape passes
   `cap_data_quality.validate_bars` and matches expected values. This is the test
   that proves "credential insertion only" — when real creds arrive, only the
   mock boundary changes (mock -> real HTTP), the adapter code does not.

**Symbol mapping note:** Upstox identifies instruments by `instrument_key`
(exchange-specific), not bare ticker symbols like `"RELIANCE"`. Add a small
`src/adapters/upstox_instruments.py` lookup table (or static JSON) mapping the
universe symbols (from `cap03_universe.py`) to Upstox instrument keys — needed
regardless of credentials, and easy to get wrong silently.

**Deliverable check:** after M1+M4, running `python -m src.main` with empty
`.env` behaves exactly as today (fixture data, no network), but
`tests/unit/adapters/` proves the real-vendor code paths are correct against
recorded payloads.

---

## M2 — Fix paper-trading drawdown tracking (F-B, CRITICAL)

**File:** `src/mod09_portfolio/cap_paper_trading.py`, `src/mod02_market_context/cap06_drift.py`
(read-only reference for how `drawdown_pct` is consumed), `src/mod06_governance/detectors.py`
(`run_drawdown_detector`, read-only reference)

**Problem:** `open_position` / `close_position` update `capital` and
`positions_json` but never `portfolio_state.drawdown_pct` or a running
peak-equity value. `run_drawdown_detector` reads `drawdown_pct`, which stays
`0.0` forever -> State 3 (Conditional Suspension) can never trigger during paper
trading.

**Fix:**
1. Add a `peak_equity` column to `portfolio_state` (migration — see
   `src/persistence/schema.sql`; add an `ALTER TABLE` migration or bump schema
   version per existing migration convention — check `db.py` for how schema
   versioning is handled).
2. Add a helper `recompute_drawdown(conn, current_equity)`:
   ```python
   def recompute_drawdown(conn, current_equity: float) -> float:
       row = conn.execute("SELECT peak_equity FROM portfolio_state WHERE id = 1").fetchone()
       peak = max(row[0] or 0.0, current_equity)
       drawdown_pct = 0.0 if peak <= 0 else max(0.0, (peak - current_equity) / peak)
       conn.execute(
           "UPDATE portfolio_state SET peak_equity = ?, drawdown_pct = ? WHERE id = 1",
           (peak, drawdown_pct),
       )
       return drawdown_pct
   ```
3. Call it from `open_position` and `close_position` after updating `capital`,
   using `current_equity = capital + sum(unrealized_pnl(...) for open positions)`
   (mark-to-market using entry prices for positions without a live price is
   acceptable — document the approximation).
4. Also call it from wherever MOD-09's `get_state()` is invoked per-cycle (so
   drawdown updates even on cycles with no trades, as prices move) — check
   `src/mod09_portfolio/portfolio.py::get_state` for the right hook.

**Test (new):** `tests/unit/mod09_portfolio/test_drawdown.py`
- open position, simulate price drop via `unrealized_pnl` input, assert
  `drawdown_pct` increases and `run_drawdown_detector` (MOD-06) transitions to
  active when the configured threshold is crossed.

---

## M3 — Functional test suite (F-C, HIGH)

**Dirs:** `tests/unit/`, `tests/integration/` (currently empty except `__init__.py`)

Minimum suite to make `tests/` a real merge gate, in priority order:

1. `tests/unit/mod05_recommendation/test_cap13_ev.py` — EV/confidence math
   (`cap12_confidence.py`, `cap13_ev.py`) against hand-computed expected values.
2. `tests/unit/mod04_validation/test_cap10_walkforward.py` — walk-forward split
   logic against the fixture data in `src/mod01_market_data/fixtures.py`
   (deterministic uptrend -> deterministic pass/fail).
3. `tests/unit/mod09_portfolio/test_cap_paper_trading.py` — open/close position
   bookkeeping, insufficient-capital error, double-open error, realized P/L math
   (extend with M2's drawdown assertions).
4. `tests/unit/test_config.py` — `config.load_config()` / `diagnostics()`:
   missing required key -> `ConfigError`; bad boolean -> `ConfigError`; empty
   optional vendor keys -> no error.
5. `tests/integration/test_cycle_fixture.py` — run `run_cycle("on-demand",
   "manual")` end-to-end against fixture adapters (no network, no creds),
   asserting the cycle completes, produces a `package`, and writes audit rows.
   This is the closest thing to "fetch me next week's analysis" as an automated
   check.

**Gate:** `tests/architecture/test_boundaries.py` (existing 6/6) +
all of the above must pass before EXECUTE on any future PCP is considered done.

---

## R1 — `.env` hygiene

**Files:** `.gitignore`, `src/.env`

`src/.env` is currently tracked (not gitignored) and contains a real
`FINNHUB_API_KEY` value. Fix:
1. Add `src/.env` to `.gitignore`.
2. `git rm --cached src/.env` (keep the local file, stop tracking it).
3. Add `src/.env.example` (tracked) with all `ALL_KEYS` from `config.py` present
   but empty, so the shape is documented without leaking secrets.
4. **Separately flag to the user:** if `FINNHUB_API_KEY` was ever pushed to a
   remote, it should be rotated — this plan only stops *future* commits.

---

## R2 — Root CLAUDE.md runbook

**File:** `CLAUDE.md` (new, repo root)

A short operator runbook so any agent (Claude Code, Antigravity CLI, etc.) opened
in this repo root knows, without re-deriving it:
- How to run a cycle: `python -m src.main --mode on-demand`
- How to run the detector loop: `python -m src.scheduler`
- How to run tests: `pytest`
- Current adapter status (fixture/stub until env vars set — list the exact
  var names from `config.py`)
- Pointer to this plan and to `IMP/PCP-001_PROGRAM_COMPLETION_PLAN.md` for
  status tracking
- The PLAN -> REVIEW -> EXECUTE convention so an agent doesn't start editing
  code on a casual request

---

## Execution Order & Why

```
M1 (factory fix)        — no deps, unlocks safe iteration on M4
  -> M4 (adapter bodies) — implemented + tested against recorded fixtures,
                           inert until real creds land (depends on M1's
                           config-presence gate)
  -> M2 (drawdown fix)   — independent of M4, but ordered after so the new
                           integration test (M3.5) can assert drawdown +
                           real-adapter-shaped data together
  -> M3 (test suite)     — written last so it covers M1/M2/M4 output, becomes
                           the permanent merge gate
  -> R1 (.env hygiene)   — housekeeping, do anytime but before any push
  -> R2 (CLAUDE.md)      — final, documents the now-stable state
```

## Definition of Done

- `pytest` passes (architecture 6/6 + all new unit/integration tests).
- `python -m src.main --mode on-demand` runs to completion on fixture data with
  zero network calls (verifiable via a test that patches `socket`/`requests` to
  raise if called, in the no-credential path).
- Dropping real `UPSTOX_*` / `FINNHUB_API_KEY` / `TRADING_ECONOMICS_*` values into
  `src/.env` flips the factory to live adapters with no code edits (proven by
  M1's factory test + M4's contract tests).
- Paper-trading drawdown halts (State 3) are reachable in a test.
- `CLAUDE.md` exists and an agent can follow it to run a cycle and report results
  in natural language ("fetch me next week's analysis").

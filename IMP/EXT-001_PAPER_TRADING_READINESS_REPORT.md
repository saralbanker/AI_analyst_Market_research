# EXT-001 — PAPER TRADING READINESS REPORT

**Document Type:** Execution Readiness Report
**Authority:** Implements no new architecture; operates within ADR-000..ADR-007, SDM_V2.3, SADR_V2.1, IMP-001, VER-001 (all FROZEN/CERTIFIED).
**Status:** COMPLETE — all seven work packages implemented and verified against a clean-state run.

---

## 1. Adapter Framework Status — IMPLEMENTED

- New shared utility package `src/adapters/` (non-`modNN_*`, exempt from `tests/architecture/test_boundaries.py`'s `MODULES` list — verified by reading the test: it only walks `MODULES` and ignores `adapters` as an import target).
- `src/adapters/market.py`: `MarketAdapter` Protocol, `FixtureMarketAdapter` (always available), `UpstoxMarketAdapter` skeleton (reads `UPSTOX_API_KEY`/`UPSTOX_API_SECRET`/`UPSTOX_ACCESS_TOKEN`, raises `AdapterNotConfigured` until set, then `NotImplementedError`).
- `src/adapters/news.py`: `NewsAdapter` Protocol, `StubNewsAdapter` (returns `[]`), `FinnhubNewsAdapter` skeleton (reads `FINNHUB_API_KEY`).
- `src/adapters/macro.py`: `MacroAdapter` Protocol, `StubMacroAdapter` (returns `{}`), `TradingEconomicsMacroAdapter` skeleton (reads `TRADING_ECONOMICS_API_KEY`/`TRADING_ECONOMICS_SECRET`).
- `src/adapters/factory.py`: `get_market_adapter()`, `get_news_adapter()`, `get_macro_adapter()` — return the real-vendor adapter if configured, else the stub. No live network calls anywhere.
- Wired: `mod01_market_data/market_data.py` now sources both vendor bar series via `get_market_adapter()`; `mod03_evidence/cap08_sentiment.py` now sources sentiment via `get_news_adapter()`. Macro adapter is available but not yet consumed by MOD-02 (CAP-05/06 are price-bar-only; wiring is additive when needed, not required for readiness).
- Verified: `pytest tests/architecture` passes (6/6); full cycle (`python -m src.main`) runs end-to-end with adapters in stub mode, producing identical output to pre-change baseline.

**Evidence:** `src/adapters/{__init__,market,news,macro,factory}.py`, `src/mod01_market_data/market_data.py:13,37-38`, `src/mod03_evidence/cap08_sentiment.py`.

**Confidence:** High.

---

## 2. Environment Validation Status — IMPLEMENTED

- New `src/config.py`: `load_config()` reads `src/.env` into `os.environ` (without overriding real env vars), validates `REQUIRED_KEYS` (APP_ENV, AUDIT_CHAIN_ENABLED, GOVERNANCE_ENABLED, PAPER_TRADING_ENABLED, AUTO_EXECUTION_ENABLED, BROKER_EXECUTION_ENABLED) are present and non-empty, and that `BOOLEAN_KEYS` parse as true/false. Raises `ConfigError` (with one message per problem, naming `src/.env`) if invalid — blocks startup before `db.init()`.
- `diagnostics()` prints a startup summary without leaking credential values (vendor keys reported as `EMPTY (stub mode)` / `set`).
- Wired into both composition roots: `src/main.py` and `src/scheduler.py` call `config.load_config()` + print diagnostics before `db.init()`.
- Verified: clean-state run of `python -m src.main` and `python -m src.scheduler --once` both print diagnostics and proceed normally; vendor credential vars (`UPSTOX_*`, `FINNHUB_API_KEY`, `TRADING_ECONOMICS_*`) are correctly reported as empty/stub without blocking startup.

**Evidence:** `src/config.py`, `src/main.py` (import + call before `db.init()`), `src/scheduler.py` (same).

**Confidence:** High.

---

## 3. Paper Trading Status — IMPLEMENTED

- New tables in MOD-09's table group (`src/persistence/schema.sql`): `paper_positions` (one row per open position) and `paper_trades` (immutable OPEN/CLOSE ledger with `realized_pnl`).
- New `src/mod09_portfolio/cap_paper_trading.py`: `open_position(symbol, quantity, price, cycle_id)`, `close_position(symbol, price, cycle_id)`, `unrealized_pnl(current_prices)`. All capital/positions bookkeeping flows through `portfolio_state` (capital, `positions_json`), preserving MOD-09 as sole authoritative source (OWN-01). Each call writes an audit record via `mod10_audit`.
- Re-exported via `src/mod09_portfolio/__init__.py`. `mod09_portfolio` still has zero outbound module edges (boundary test `test_forb_mod09_portfolio_has_no_shadow_dependencies` passes).
- No broker integration, no execution automation — these are deliberate bookkeeping calls (e.g. invoked after a human-approved recommendation), matching EXT-001 FORBIDDEN_ACTIONS.
- Verified end-to-end from a clean DB: `open_position('RELIANCE', 1, 2000.0)` → capital 5000→3000; `unrealized_pnl` → `{'RELIANCE': 100.0}`; `close_position('RELIANCE', 2100.0)` → `realized_pnl=100.0`, capital→5100.

**Evidence:** `src/persistence/schema.sql` (paper_positions/paper_trades DDL), `src/mod09_portfolio/cap_paper_trading.py`, `src/mod09_portfolio/__init__.py`.

**Confidence:** High.

---

## 4. Metrics Engine Status — IMPLEMENTED

- New `tools/metrics.py` (human-only CLI, outside `modNN_*` boundary, same pattern as `tools/audit_review.py`): `compute_metrics()` reads `paper_trades` (CLOSE rows with `realized_pnl`) and computes win rate, expectancy, average gain, average loss, profit factor, and max drawdown over the cumulative-P/L equity curve.
- Derives solely from paper trading records (`paper_trades`), per WORK_PACKAGE_04 requirement.
- Verified: `python tools/metrics.py` against the one closed trade above produced `win_rate=1.0, expectancy=100.0, average_gain=100.0, average_loss=0.0, profit_factor=None (no losses), max_drawdown=0.0`.

**Evidence:** `tools/metrics.py`.

**Confidence:** High.

---

## 5. Recommendation Journal Status — IMPLEMENTED

- Extended `attribution_records` (MOD-08's table group) with `direction`, `confidence`, `ev`, `allocation_amount`, `decision` columns, alongside existing `system_alpha`/`human_alpha`. Forward-only migration added to `src/persistence/db.py:_migrate()` (idempotent `ALTER TABLE ... ADD COLUMN`, guarded by `PRAGMA table_info`, per IMP-001 Section 4.3) for pre-existing databases.
- `src/mod08_attribution/cap21_22_attribution.py:compute_attribution()` now extracts `direction`, `confidence`, `ev`, `allocation_amount`, `decision` directly from the `opportunity` dict / `Decision` already passed into `MOD-08.observe()` — no new dependency edges (MOD-08 still does not import MOD-05 or MOD-09).
- `src/mod08_attribution/attribution.py:_persist()` writes all fields. Historical traceability: each row now records the full recommendation (direction/confidence/ev/allocation), the human approval/rejection decision, and the resulting system/human alpha — queryable by `cycle_id`/`symbol`/`recorded_at`.
- Verified: end-to-end cycle run produced an `attribution_records` row with `direction=LONG, confidence=0.725, ev=0.008389, allocation_amount=362.5, decision=approve`.

**Evidence:** `src/persistence/schema.sql` (attribution_records DDL), `src/persistence/db.py:_migrate`, `src/mod08_attribution/cap21_22_attribution.py`, `src/mod08_attribution/attribution.py`.

**Confidence:** High.

---

## 6. Daily Reporting Status — IMPLEMENTED

- New `tools/daily_report.py` (human-only CLI, outside `modNN_*` boundary): `build_report(date)` reads `activation_log` (cycles run), `attribution_records` (recommendations generated + decision), `human_decisions` (approval/rejection counts), `paper_positions` (open positions), `paper_trades` (closed positions for the date), `portfolio_state` (capital/drawdown), and `tools.metrics.compute_metrics()` (performance summary).
- Covers all required content: recommendations generated, approvals, rejections, open positions, closed positions, performance summary.
- Verified: `python tools/daily_report.py` against the post-cycle clean-state DB printed a complete report for the day, including 1 cycle, 1 recommendation (RELIANCE LONG, decision=approve), 1 approval, 0 rejections, 0 open positions, 1 closed position (realized_pnl=100.0), and the performance summary.

**Evidence:** `tools/daily_report.py`.

**Confidence:** High.

---

## 7. Data Quality Validation Status — IMPLEMENTED

- New `src/mod01_market_data/cap_data_quality.py`: `validate_bars(bars, source)` rejects (raises `DataQualityFailure`) on: empty series, duplicate `day` values, missing candles (gaps in the `day` sequence), non-positive open/high/low/close, `high < low`, open/close outside `[low, high]`, negative volume, and future `timestamp` (if present).
- Wired into `src/mod01_market_data/market_data.py:run()`, called on both vendor bar series **before** `cross_verify()` (CAP-02) — bad data is rejected before ingestion, as required. On rejection: an audit record (`data_quality_rejected`) is written and `CrossVerificationFailure` is raised, reusing the existing CAP-02 blocking-gate path (no new exception type surfaced to `main.py`, no execution-model change).
- Verified: `pytest tests/architecture` passes; full cycle with the existing fixture (which is well-formed) passes validation and proceeds normally.

**Evidence:** `src/mod01_market_data/cap_data_quality.py`, `src/mod01_market_data/market_data.py`.

**Confidence:** High.

---

## 8. External Integration Readiness

| Vendor | Adapter | Credential vars (in `src/.env`) | Status |
|---|---|---|---|
| Upstox (market data) | `src/adapters/market.py:UpstoxMarketAdapter` | `UPSTOX_API_KEY`, `UPSTOX_API_SECRET`, `UPSTOX_ACCESS_TOKEN`, `UPSTOX_REDIRECT_URI` | Skeleton ready; factory auto-selects it once credentials are non-empty (currently raises `NotImplementedError` for the actual fetch — the HTTP call body is the only remaining work, not architecture) |
| Finnhub (news) | `src/adapters/news.py:FinnhubNewsAdapter` | `FINNHUB_API_KEY` | Skeleton ready; same pattern |
| Trading Economics (macro) | `src/adapters/macro.py:TradingEconomicsMacroAdapter` | `TRADING_ECONOMICS_API_KEY`, `TRADING_ECONOMICS_SECRET` | Skeleton ready, not yet consumed by MOD-02 (additive wiring, optional for readiness) |

All three skeletons compile, integrate cleanly into the existing pipeline (mod01/mod03), and make no live calls. `src/config.py` validates the presence of the credential variable *names* and reports their (empty) state at startup without blocking.

**Residual implementation work (explicitly NOT architecture, NOT in scope for this protocol):** implement the HTTP request/response bodies inside `UpstoxMarketAdapter.fetch_ohlcv`, `FinnhubNewsAdapter.fetch_sentiment`, `TradingEconomicsMacroAdapter.fetch_indicators` once credentials are inserted into `src/.env`. The factory functions will then automatically select the real adapters with no further code changes (verified by the `try/except AdapterNotConfigured` fallback logic).

---

## 9. Paper Trading Readiness Verdict

**READY** (for credential insertion + paper trading validation), with one explicitly-scoped exception noted below.

- All seven work packages are operational and verified against a clean-state run (`rm -rf data/` → `python -m src.main` → `python -m src.scheduler --once` → `tools/audit_review.py --verify-chain` → `tools/metrics.py` → `tools/daily_report.py`, all succeeded).
- `pytest tests/architecture` (6/6) confirms the boundary-enforcement co-requirement still holds — no Allowed Edge Table violation was introduced.
- No architecture, ADR, SDM, SADR, governance, ownership, or module-boundary file was modified.
- No PostgreSQL/Supabase/Convex introduced; SQLite (`system.db`/`audit.db`) unchanged as the persistence engine, extended only via additive columns/tables within existing module table-groups.
- No broker integration, order routing, or approval automation was added; CAP-18 human gate is untouched.

**Exception:** The three vendor adapter `fetch_*` methods raise `NotImplementedError` after credential presence is confirmed — i.e., credential insertion alone is *not yet* sufficient to receive live data; the HTTP call bodies must also be filled in. This is implementation work confined entirely to `src/adapters/{upstox,finnhub,trading_economics}` classes (3 self-contained functions), requires no further architectural decisions, and does not block starting paper-trading validation in stub mode today. Recommend treating "fill in the three adapter HTTP calls" as the literal next task when live data is desired; until then, the system runs the full paper-trading-ready vertical slice against fixture data with real paper P/L tracking, metrics, and reporting.

---

*EXT-001 derives its authority from ADR-000 through ADR-007 (FROZEN), IMP-001, and VER-001 (CERTIFIED). It introduces no architectural change — every addition is either a new non-`modNN_*` utility package (`src/adapters/`, `src/config.py`), additive columns/tables within an existing module's owning table-group, or a human-only `tools/` CLI outside the boundary-enforcement scope.*

*End of EXT-001_PAPER_TRADING_READINESS_REPORT*

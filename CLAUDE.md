# CLAUDE.md — Operator Runbook

This file orients any coding agent (Claude Code, Antigravity CLI, etc.) opened
in this repo root. Read this before exploring further.

## What this is

A CLI-only Python application — no API/server layer. See `README.md` for the
full constitutional architecture. There is nothing to "connect" an agent to:
run the commands below directly via shell and read their output/JSON.

## Running it

```bash
# One on-demand research cycle (Stage 2-4 pipeline, ends at the human gate)
python -m src.main --mode on-demand

# Continuous detector loop (MOD-06, runs independently of cycles)
python -m src.scheduler

# Test suite (architecture boundaries + functional tests)
pytest
```

`python -m src.main` prints config diagnostics, recovery state, the Open
Menu of opportunities, then blocks on `input()` per opportunity (approve/
reject) — CAP-18, no automated decisions. Pipe `reject`/`approve` answers via
stdin for non-interactive runs.

## Adapter / credential status

Adapter selection (`src/adapters/factory.py`) is by **config-presence**: if
the relevant env vars in `src/.env` are non-empty, the real adapter is used;
otherwise it falls back to a fixture/stub. No code changes are needed when
credentials are inserted ("credential insertion only").

| Adapter | Env vars (in `src/.env`) | Fallback when empty |
|---|---|---|
| Market data (Upstox) | `UPSTOX_API_KEY`, `UPSTOX_API_SECRET`, `UPSTOX_ACCESS_TOKEN` | `FixtureMarketAdapter` (synthetic RELIANCE bars) |
| News/sentiment (Finnhub) | `FINNHUB_API_KEY` | `StubNewsAdapter` (empty list) |
| Macro (Trading Economics) | `TRADING_ECONOMICS_API_KEY`, `TRADING_ECONOMICS_SECRET` | `StubMacroAdapter` (empty dict) |

Copy `src/.env.example` to `src/.env` and fill in real values to activate a
vendor. `src/.env` is gitignored — never commit it.

Currently: Finnhub is configured and live. Upstox and Trading Economics are
in stub mode (no credentials).

New Upstox symbols must be added to
`src/adapters/upstox_instruments.py::SYMBOL_TO_INSTRUMENT_KEY`.

## Workflow convention

This project follows **PLAN -> REVIEW -> EXECUTE**. Planning documents live in
`IMP/`. Don't start large code changes from a casual request — check whether
there's a relevant PLAN doc in `IMP/` first, and if not, propose one.

- `IMP/PCP-001_PROGRAM_COMPLETION_PLAN.md` — overall program status
- `IMP/PLAN-002_NO_CREDENTIAL_BUILDOUT/` — adapter/test/governance buildout
  (M1-M4, R1-R2 — all complete as of this writing)

## Architecture rules (don't violate)

- Sentiment/news (CAP-08) is advisory-only and must never reach
  confidence/EV/ranking/allocation computation (CAP-12/13/15/16).
- MOD-09 is the sole writer of portfolio state (`capital`, `positions_json`,
  `drawdown_pct`, `peak_equity`).
- No automated order execution anywhere (`AUTO_EXECUTION_ENABLED` /
  `BROKER_EXECUTION_ENABLED` must stay `false`).
- `tests/architecture/test_boundaries.py` enforces module import boundaries —
  must stay green.

-- Operational schema (system.db). One table-group per owning module.
-- ADR-005 Section 7 (Persistence Requirements Matrix).

-- MOD-11: Activation
CREATE TABLE IF NOT EXISTS activation_log (
    cycle_id        TEXT PRIMARY KEY,
    mode            TEXT NOT NULL,
    trigger         TEXT NOT NULL,
    activated_at    TEXT NOT NULL
);

-- MOD-09: Portfolio State (sole authoritative source, OWN-01)
CREATE TABLE IF NOT EXISTS portfolio_state (
    id              INTEGER PRIMARY KEY CHECK (id = 1),
    capital         REAL NOT NULL,
    positions_json  TEXT NOT NULL,
    drawdown_pct    REAL NOT NULL,
    peak_equity     REAL NOT NULL DEFAULT 0,
    updated_at      TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS trade_ledger (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    cycle_id        TEXT,
    symbol          TEXT NOT NULL,
    action          TEXT NOT NULL,
    quantity        REAL NOT NULL,
    price           REAL NOT NULL,
    recorded_at     TEXT NOT NULL
);

-- EXT-001 WP03: Paper trading infrastructure (MOD-09 owned -- OWN-01).
-- paper_positions: one row per currently-open paper position.
CREATE TABLE IF NOT EXISTS paper_positions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol          TEXT NOT NULL UNIQUE,
    quantity        REAL NOT NULL,
    entry_price     REAL NOT NULL,
    opened_cycle_id TEXT,
    opened_at       TEXT NOT NULL
);

-- paper_trades: immutable record of every open/close action (realized P/L
-- recorded on close).
CREATE TABLE IF NOT EXISTS paper_trades (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    cycle_id        TEXT,
    symbol          TEXT NOT NULL,
    action          TEXT NOT NULL CHECK (action IN ('OPEN','CLOSE')),
    quantity        REAL NOT NULL,
    price           REAL NOT NULL,
    realized_pnl    REAL,
    recorded_at     TEXT NOT NULL
);

-- MOD-06: Governance State (4 independent halt states, GOV-02/DEP-11 -- no shared row)
CREATE TABLE IF NOT EXISTS governance_state (
    halt_state_id   INTEGER PRIMARY KEY CHECK (halt_state_id IN (1,2,3,4)),
    name            TEXT NOT NULL,
    status          TEXT NOT NULL CHECK (status IN ('inactive','active')),
    condition_json  TEXT,
    entered_at      TEXT,
    exited_at       TEXT
);

-- MOD-07: Human Decisions (Primary Source, immutable)
CREATE TABLE IF NOT EXISTS human_decisions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    cycle_id        TEXT NOT NULL,
    symbol          TEXT,
    decision        TEXT NOT NULL CHECK (decision IN ('approve','reject')),
    decided_at      TEXT NOT NULL
);

-- MOD-08: Attribution (reconstructable from MOD-07 + MOD-01 + MOD-02)
-- EXT-001 WP05: direction/confidence/ev/allocation_amount/decision columns
-- added for recommendation-journal traceability -- values are taken from the
-- RecommendationPackage + Decision already passed into MOD-08.observe().
CREATE TABLE IF NOT EXISTS attribution_records (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    cycle_id            TEXT NOT NULL,
    symbol              TEXT,
    direction           TEXT,
    confidence          REAL,
    ev                  REAL,
    allocation_amount   REAL,
    decision            TEXT,
    system_alpha        REAL,
    human_alpha         REAL,
    recorded_at         TEXT NOT NULL
);

-- MOD-01: Market Data Foundation
CREATE TABLE IF NOT EXISTS market_baselines (
    cycle_id        TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    ohlcv_json      TEXT NOT NULL,
    recorded_at     TEXT NOT NULL,
    PRIMARY KEY (cycle_id, symbol)
);

CREATE TABLE IF NOT EXISTS eligible_universe (
    cycle_id        TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    eligible        INTEGER NOT NULL,
    PRIMARY KEY (cycle_id, symbol)
);

-- MOD-02: Market Context
CREATE TABLE IF NOT EXISTS regime_state (
    cycle_id        TEXT PRIMARY KEY,
    regime          TEXT NOT NULL,
    recorded_at     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS drift_metrics (
    cycle_id        TEXT PRIMARY KEY,
    drift_json      TEXT NOT NULL,
    recorded_at     TEXT NOT NULL
);

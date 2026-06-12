# 01 Architecture Driver Registry

**Objective:** Map consensus architectural drivers from the audited ADR candidate corpus.

### DRV-001: Local First Data Ingestion and Processing
- **DRIVER_ID:** DRV-001
- **NAME:** Local First Data Ingestion and Processing
- **SOURCE_ADRS:** ADR-001 (embedded zero-copy DuckDB+SQLite), ADR-002 (SQLite time-series inadequacies), ADR-003 (Hive-partitioned Parquet storage format).
- **PROBLEM_SOLVED:** Network dependencies and query latency over distributed databases during real-time trading executions.
- **EVIDENCE:** ADR-001 (embedded zero-copy DuckDB+SQLite), ADR-002 (SQLite time-series inadequacies), ADR-003 (Hive-partitioned Parquet storage format).
- **CRITICALITY:** CRITICAL

### DRV-002: Deterministic Execution Isolation
- **DRIVER_ID:** DRV-002
- **NAME:** Deterministic Execution Isolation
- **SOURCE_ADRS:** ADR-071 (LLM direct execution prohibition via FastMCP boundary), ADR-078 (Isolate AI exclusively to Research/Cognitive domain).
- **PROBLEM_SOLVED:** Direct LLM trading execution logic causing non-deterministic order routes or catastrophic binary formatting errors.
- **EVIDENCE:** ADR-071 (LLM direct execution prohibition via FastMCP boundary), ADR-078 (Isolate AI exclusively to Research/Cognitive domain).
- **CRITICALITY:** CRITICAL

### DRV-003: Human Approval Gates
- **DRIVER_ID:** DRV-003
- **NAME:** Human Approval Gates
- **SOURCE_ADRS:** ADR-072 (dedicated critical alert runbooks), ADR-073 (multi-signature limits override), ADR-077 (active risk committee oversight).
- **PROBLEM_SOLVED:** Operator alert fatigue and bypass of position bounds leading to uncoordinated high-volume algorithmic risks.
- **EVIDENCE:** ADR-072 (dedicated critical alert runbooks), ADR-073 (multi-signature limits override), ADR-077 (active risk committee oversight).
- **CRITICALITY:** HIGH

### DRV-004: Multi-Source Feed Verification
- **DRIVER_ID:** DRV-004
- **NAME:** Multi-Source Feed Verification
- **SOURCE_ADRS:** ADR-004 (disqualification of Zerodha as sole backtest source), ADR-011 (cross-verify OHLCV metrics), ADR-012 (verify minute feed length).
- **PROBLEM_SOLVED:** Incomplete provider data, dropped pricing candles, and split adjustments corruption.
- **EVIDENCE:** ADR-004 (disqualification of Zerodha as sole backtest source), ADR-011 (cross-verify OHLCV metrics), ADR-012 (verify minute feed length).
- **CRITICALITY:** HIGH

### DRV-005: Rigorous System Auditability
- **DRIVER_ID:** DRV-005
- **NAME:** Rigorous System Auditability
- **SOURCE_ADRS:** ADR-054 (automated binary hash verification), ADR-055 (memory configuration flags audit).
- **PROBLEM_SOLVED:** Uncoordinated server binary deployments and legacy configuration reactivation paths (Knight Capital failure mode).
- **EVIDENCE:** ADR-054 (automated binary hash verification), ADR-055 (memory configuration flags audit).
- **CRITICALITY:** HIGH

### DRV-006: System Survivability Controls
- **DRIVER_ID:** DRV-006
- **NAME:** System Survivability Controls
- **SOURCE_ADRS:** ADR-031 (dynamic margin scale), ADR-032 (model uncertainty scaling), ADR-034 (circuit breaker controls).
- **PROBLEM_SOLVED:** Positive feedback loops in volatile regimes, market non-ergodicity defaults, and collateral fire sales.
- **EVIDENCE:** ADR-031 (dynamic margin scale), ADR-032 (model uncertainty scaling), ADR-034 (circuit breaker controls).
- **CRITICALITY:** CRITICAL

### DRV-007: Data Governance Standards
- **DRIVER_ID:** DRV-007
- **NAME:** Data Governance Standards
- **SOURCE_ADRS:** ADR-008 (SEBI rate limits static IP), ADR-009 (deprecated code removal).
- **PROBLEM_SOLVED:** Regulatory non-compliance with SEBI API limits, static IP routing, and OAuth requirements.
- **EVIDENCE:** ADR-008 (SEBI rate limits static IP), ADR-009 (deprecated code removal).
- **CRITICALITY:** CRITICAL

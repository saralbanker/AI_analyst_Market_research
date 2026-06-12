# ADR Candidate Corpus

**Phase:** 5 — ADR Candidate Synthesis
**Status:** Complete — All Candidates Synthesized
**Total ADR Candidates:** 120
**Date:** 2026-06-04

> **Quality Gate:**
> - ✅ Every ADR references source evidence
> - ✅ Every ADR references audit findings
> - ✅ Every ADR references failure analysis
> - ✅ Every ADR references validation analysis
> - ✅ No unsupported ADRs
> - ✅ No architecture designed
> - ✅ No implementation plans generated
> - ✅ No approvals issued

---

ADR_ID: ADR-001

Title: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs)

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: DuckDB+SQLite hybrid embedded database is required for the quantitative trading system.

Decision: DuckDB+SQLite hybrid embedded database is required for the quantitative trading system. Vector databases are architecturally unsuited because 95% of swing trading data is structured time-series (OHLCV), not semantic search workloads.

Supporting_Evidence: Section 6 designates DuckDB+SQLite hybrid as required with 90/100 confidence. Section 19 mandates zero-copy architecture. Section 7 Finding 24 disqualifies SQLite alone for time-series aggregations. | Audit: STRONG

Opposing_Evidence: Vector databases are actively contradicted by §6 and §19 because 95% of trading data is structured time-series (OHLCV).

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Walk-forward OOS data accurately mimics future market regimes (§9 A5).

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-002

Title: SQLite Exclusion from Standalone Time-Series Aggregation

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: SQLite is computationally inadequate for time-series aggregations due to its row-oriented engine.

Decision: SQLite is computationally inadequate for time-series aggregations due to its row-oriented engine.

Supporting_Evidence: Section 7 Finding 24 (Top 25 Highest Confidence Findings). | Audit: STRONG

Opposing_Evidence: SQLite standalone usage is contradicted by §7 Finding 24 which flags it as computationally inadequate for time-series aggregations due to row-oriented engine.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-003

Title: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited)

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month partitioning).

Decision: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month partitioning). Unstructured JSON data lakes are explicitly prohibited.

Supporting_Evidence: Section 19 states this as a hard MUST constraint. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Unstructured JSON analytical queries storage exhaustion; high memory load on unstructured raw reads.

Failure_Modes_Introduced: Memory overflow risk during multi-year queries; scan plan memory bottlenecks.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-004

Title: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: Zerodha historical API data is structurally incomplete and unsuitable as a sole backtesting source.

Decision: Zerodha historical API data is structurally incomplete and unsuitable as a sole backtesting source.

Supporting_Evidence: Section 7 Finding 2 (Top 25 Highest Confidence Findings). Section 15 rates Data API Reliability as Tier 3 — practitioner testing only, subject to silent API updates. | Audit: STRONG

Opposing_Evidence: Zerodha is disqualified as sole backtesting source by §7 Finding 2 due to dropped candles and structural incompleteness.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Dropped candle backtest failures; incomplete provider feeds; historical pricing mismatches.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-005

Title: Corporate Actions — Mandatory Split-Adjusted Data Requirement

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: Unadjusted stock splits corrupt technical indicators and backtest validity.

Decision: Unadjusted stock splits corrupt technical indicators and backtest validity.

Supporting_Evidence: Section 7 Finding 7 (Top 25 Highest Confidence Findings). Section 7 Finding 13 confirms Upstox Uplink provides up to 20 years of split-adjusted daily data. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Alpha inflation from unadjusted splits; indicators corruption; incorrect price backtests.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-006

Title: Provider Selection — Upstox Uplink for Historical Split-Adjusted Data

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Upstox Uplink API provides up to 20 years of split-adjusted daily data.

Decision: Upstox Uplink API provides up to 20 years of split-adjusted daily data. However, complex de-merger split adjustments may not be handled perfectly.

Supporting_Evidence: Section 7 Finding 13 (positive provider claim). Section 8 Finding 19 (caveat on de-merger accuracy — weakly supported). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Dropped candle backtest failures; incomplete provider feeds; historical pricing mismatches.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-007

Title: Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited)

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: Walk-forward cross-validation prevents chronological data leaks better than randomized k-fold CV.

Decision: Walk-forward cross-validation prevents chronological data leaks better than randomized k-fold CV.

Supporting_Evidence: Section 7 Finding 8 (Top 25 Highest Confidence Findings). Section 15 Tier 2 evidence (Jegadeesh/Titman, NBER). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Overfitting on randomized cross-validation datasets; chronologically leaked features.

Failure_Modes_Introduced: Increased model backtesting execution time; CPU thread starvation.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-008

Title: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second.

Decision: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second.

Supporting_Evidence: Section 7 Finding 14 (Top 25 Highest Confidence Findings — regulatory mandates). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Regulatory non-compliance accounts suspension; rate limits breaches.

Failure_Modes_Introduced: Daemon connection queues latency; OAuth token refresh hangs.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: Static analysis audit of codebase; manual SEBI compliance legal check.

Validation_Requirements: Level 1: Research_Validation, Level 5: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: High

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-009

Title: Production Binary Hygiene — Deprecated Code Removal Requirement

Decision_Category: Data Governance

Decision_Origin: Direct_Evidence

Problem_Solved: Deprecated code left in production binaries represents a massive unquantifiable risk.

Decision: Deprecated code left in production binaries represents a massive unquantifiable risk.

Supporting_Evidence: Section 7 Finding 25 (Top 25 Highest Confidence Findings). Section 12 Blind Spot (High) — unused code in Python binaries under-tested for server state mismatch triggering dead loops. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Legacy address spaces re-activation; uncoordinated production binary behavior.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Static analysis audit of codebase; manual SEBI compliance legal check.

Validation_Requirements: Level 1: Research_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-010

Title: Yahoo Finance Adjusted Close Mis-Adjustment Risk

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: Yahoo Finance Adjusted Close has occasional mis-adjustments for dividend events.

Decision: Yahoo Finance Adjusted Close has occasional mis-adjustments for dividend events.

Supporting_Evidence: Section 8 Finding 8 (Weakly Supported Findings — listed as weakly evidenced). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-011

Title: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Cross-verify OHLCV metrics between at least two independent data providers before running signal logic.

Decision: Cross-verify OHLCV metrics between at least two independent data providers before running signal logic.

Supporting_Evidence: Section 11 Validation Requirement 25 (mandated control). Section 15 Tier 3 rating for Data API Reliability. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Dropped candle backtest failures; incomplete provider feeds; historical pricing mismatches.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Walk-forward OOS data accurately mimics future market regimes (§9 A5).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-012

Title: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles)

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Ensure data continuity: explicitly verify that intraday minute feeds equal expected daily lengths (no dropped candles).

Decision: Ensure data continuity: explicitly verify that intraday minute feeds equal expected daily lengths (no dropped candles).

Supporting_Evidence: Section 11 Validation Requirement 24. Section 23 (inject synthetic anomalies test). Section 15 Tier 3 API reliability. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-013

Title: Survivorship Bias — Delisted Stock Inclusion Requirement

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Delisted stocks are assumed not necessary for a valid backtest (ignoring survivorship bias).

Decision: Delisted stocks are assumed not necessary for a valid backtest (ignoring survivorship bias). This assumption is unvalidated.

Supporting_Evidence: Section 9 Assumption 23 (hidden assumption). Survivorship bias corrupting Sharpe ratios is referenced in corpus. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Delisted stocks are not necessary for a valid backtest (§9 A23).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-014

Title: NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: NLP sentiment models (FinBERT) trained on US markets are assumed to effectively map to Indian corporate disclosures.

Decision: NLP sentiment models (FinBERT) trained on US markets are assumed to effectively map to Indian corporate disclosures. This assumption is unvalidated.

Supporting_Evidence: Section 9 Assumption 24 (hidden assumption, untested). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Alpha inflation from unadjusted splits; indicators corruption; incorrect price backtests.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Unknowns: Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-015

Title: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: S3/Litestream asynchronous backups are assumed not to encounter network dropouts during local PC crashes.

Decision: S3/Litestream asynchronous backups are assumed not to encounter network dropouts during local PC crashes. SQLite WAL risks infinite growth if S3 upload hangs.

Supporting_Evidence: Section 9 Assumptions 2 and 18 (hidden, untested). Section 23 (explicit test requirement). Section 21 (WAL lock as a systemic failure node). | Audit: MODERATE

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Medium

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-016

Title: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Test the Data Validation Pipeline: inject synthetic anomalies (e.

Decision: Test the Data Validation Pipeline: inject synthetic anomalies (e.g., extreme high/low prices, missing minute bars) into the Parquet ingestion engine to verify that forward-fill algorithms and outlier detectors catch and isolate the corruption.

Supporting_Evidence: Section 23 (Assumptions to Test). Section 10 Mode 24 (incorrect pricing causing infinite loops). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Unstructured JSON analytical queries storage exhaustion; high memory load on unstructured raw reads.

Failure_Modes_Introduced: Memory overflow risk during multi-year queries; scan plan memory bottlenecks.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-017

Title: Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Incorrect pricing data triggering infinite downstream processing loops (Content-to-Timing failure).

Decision: Incorrect pricing data triggering infinite downstream processing loops (Content-to-Timing failure).

Supporting_Evidence: Section 10 Failure Mode 24. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-018

Title: Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Assuming near-real-time WebSocket feeds are instant is a blind spot.

Decision: Assuming near-real-time WebSocket feeds are instant is a blind spot. Latency spikes trigger false HFT volume cascades.

Supporting_Evidence: Section 12 Blind Spot (Medium risk — Data Tape Latency Delays). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-019

Title: Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy

Decision_Category: Data Governance

Decision_Origin: Consensus_Inference

Problem_Solved: Clearinghouses cancel trades to survive.

Decision: Clearinghouses cancel trades to survive. Unhedged exposure from retroactively voided trade legs.

Supporting_Evidence: Section 12 Blind Spot (Medium risk — Exchange Trade Erasure). Section 9 Assumption 1 (exchanges assumed not to retroactively erase trades). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Exchanges (NSE/BSE) will not retroactively erase or cancel valid trades during a clearing member default (§9 A1).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-020

Title: SQLite WAL Transaction Integrity on NSE Trade Void Events

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: If the NSE clears trades that are later voided due to broker defaults, how does the local SQLite database cleanly revert local WAL logs without corrupting the backtest engine?.

Decision: If the NSE clears trades that are later voided due to broker defaults, how does the local SQLite database cleanly revert local WAL logs without corrupting the backtest engine?

Supporting_Evidence: Section 17 (Unknowns Requiring Future Research). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-04: Slippage threshold quantification — no limit defined.

Status: Insufficient_Evidence

---

ADR_ID: ADR-021

Title: LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: LLMs can safely write dynamic SQL queries via MCP against DuckDB.

Decision: LLMs can safely write dynamic SQL queries via MCP against DuckDB. Classified as WEAKLY SUPPORTED with qualifier: Extreme hallucination/OOM risk.

Supporting_Evidence: Section 8 Finding 13 (Weakly Supported — safety claim unverified, risk label severe). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: LLMs writing dynamic SQL queries via MCP against DuckDB is contradicted by §8 Finding 13 (extreme hallucination/OOM risk).

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-022

Title: LLM Context Window Degradation on Raw HTML NSE/SEC Filings

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: Small language models cannot process raw HTML SEC/NSE filings locally without context-window degradation.

Decision: Small language models cannot process raw HTML SEC/NSE filings locally without context-window degradation.

Supporting_Evidence: Section 8 Finding 25 (Weakly Supported). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: Local SLM capabilities are contradicted by §8 Finding 25 which flags context degradation when processing raw HTML filings.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-023

Title: Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: No benchmarks exist for the exact memory load when DuckDB joins a 50GB Parquet data lake with a live, writing SQLite database locally.

Decision: No benchmarks exist for the exact memory load when DuckDB joins a 50GB Parquet data lake with a live, writing SQLite database locally.

Supporting_Evidence: Section 22 (Missing Evidence). Section 6 (validation required — stress-test against RAM limits). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — entirely absent.

Status: Insufficient_Evidence

---

ADR_ID: ADR-024

Title: Missing Research — VaR Modeling Under Non-Ergodic Market Conditions

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: The corpus acknowledges non-ergodicity but fails to provide a mathematical framework for calculating daily Value-at-Risk under non-ergodic conditions.

Decision: The corpus acknowledges non-ergodicity but fails to provide a mathematical framework for calculating daily Value-at-Risk under non-ergodic conditions.

Supporting_Evidence: Section 13 (Missing Research Inventory). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: GAP-02: Non-ergodic VaR mathematical framework.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: Mathematical framework for VaR under non-ergodic conditions (§13).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: GAP-02: Non-ergodic VaR mathematical framework — missing research.

Status: Insufficient_Evidence

---

ADR_ID: ADR-025

Title: Missing Research — Multi-Broker Aggregate Margin Exposure Management

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: How an algorithmic system specifically manages exposure across multiple Indian discount brokers (e.

Decision: How an algorithmic system specifically manages exposure across multiple Indian discount brokers (e.g., Zerodha + Upstox) simultaneously to avoid aggregate margin breaches — is missing research.

Supporting_Evidence: Section 13 (Missing Research Inventory). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: GAP-10: Multi-broker aggregate margin exposure management.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: GAP-05: VIX threshold for variation margin — unquantified.

Status: Insufficient_Evidence

---

ADR_ID: ADR-026

Title: Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals

Decision_Category: Data Governance

Decision_Origin: Architectural_Inference

Problem_Solved: 15-20 minute delays on Yahoo Finance data will not materially affect end-of-day signal calculation.

Decision: 15-20 minute delays on Yahoo Finance data will not materially affect end-of-day signal calculation. This assumption is unvalidated.

Supporting_Evidence: Section 9 Assumption 21 (hidden assumption, untested). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Unknowns: No empirical benchmarks provided in corpus.

Risk_Level: Critical

Governance_Impact: Regulatory compliance breach or data validation failure risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-027

Title: Walk-Forward Cross-Validation Over Randomized k-Fold CV

Decision_Category: Validation

Decision_Origin: Direct_Evidence

Problem_Solved: Walk-forward cross-validation prevents chronological data leaks better than randomized k-fold CV.

Decision: Walk-forward cross-validation prevents chronological data leaks better than randomized k-fold CV.

Supporting_Evidence: Section 7 Finding 8 (Top 25 Highest Confidence). Section 15 Tier 2 evidence (Jegadeesh/Titman, NBER). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Model overfitting on historical data; randomized feature leakage.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-028

Title: Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe)

Decision_Category: Validation

Decision_Origin: Direct_Evidence

Problem_Solved: t-statistic > 3.

Decision: t-statistic > 3.0 or rigorously deflated Sharpe ratio required to prove statistical edge.

Supporting_Evidence: Section 7 Finding 23. Paired with §8 Finding 17 (t=2.0 explicitly insufficient). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Deployment of strategies with weak statistical edges; false signal validation.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Status: Candidate

---

ADR_ID: ADR-029

Title: Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: 95% confidence interval (t=2.

Decision: 95% confidence interval (t=2.0) is insufficient to deploy a trading strategy.

Supporting_Evidence: Section 8 Finding 17 (Weakly Supported — practitioner consensus only). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Status: Deferred

---

ADR_ID: ADR-030

Title: Cluster-Wide Binary Hash Verification Before Live Routing

Decision_Category: Validation

Decision_Origin: Direct_Evidence

Problem_Solved: Mandate automated cluster-wide binary hash verification prior to live routing.

Decision: Mandate automated cluster-wide binary hash verification prior to live routing.

Supporting_Evidence: Section 11 Req 1. Section 7 Finding 1 (Knight Capital, 95/100 confidence). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Uncoordinated production deployments mismatch; deployment state desyncs.

Failure_Modes_Introduced: CI/CD deployment delays; server startup latency.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-031

Title: Audit All Configuration Flags for Deprecated Memory Address Reuse

Decision_Category: Validation

Decision_Origin: Direct_Evidence

Problem_Solved: Audit all configuration flags to ensure zero reuse of deprecated memory addresses.

Decision: Audit all configuration flags to ensure zero reuse of deprecated memory addresses.

Supporting_Evidence: Section 11 Req 2. Section 7 Finding 1 (Knight Capital mechanism). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Configuration namespaces address reuse reactivating legacy code.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-032

Title: Hard-Coded Parent-Order Balance Checks in Execution Loops

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Hard-code continuous parent-order balance checks directly into execution loops.

Decision: Hard-code continuous parent-order balance checks directly into execution loops.

Supporting_Evidence: Section 11 Req 3. Section 10 Mode 2 (runaway loops without balance checks). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Runaway execution loops executing trades without balance check.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-033

Title: Automated Sanity and Chaos Tests Across All Nodes Before Production Routing

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Deploy automated sanity and chaos tests across all nodes before production routing.

Decision: Deploy automated sanity and chaos tests across all nodes before production routing.

Supporting_Evidence: Section 11 Req 6. Section 10 Mode 6 (unvalidated rollback spreads bugs). Section 23 (specific test scenarios). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Production server configuration rollbacks spreading old bugs.

Failure_Modes_Introduced: Deployment pipeline blockers; test environment execution delays.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-034

Title: Population Stability Index (PSI) Tracking for Concept Drift Detection

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Track Population Stability Index (PSI) to measure concept drift between live and training data.

Decision: Track Population Stability Index (PSI) to measure concept drift between live and training data.

Supporting_Evidence: Section 11 Req 9. Section 9 Assumption 5 (walk-forward OOS fidelity). Section 8 Finding 7 (AI grids cannot adapt across regime changes). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: High CPU computation load for statistical checks; false drift alerts.

Failure_Modes_Unresolved: GAP-03: ML concept drift controls.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: High

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Difficult recovery with high severity.

Research_Gaps: GAP-03: ML concept drift controls — no §11 Req paired.

Status: Candidate

---

ADR_ID: ADR-035

Title: Automatic Bid Size Reduction Under High Quantile Uncertainty

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Program execution algorithms to automatically reduce bid size when quantile uncertainty bands widen.

Decision: Program execution algorithms to automatically reduce bid size when quantile uncertainty bands widen.

Supporting_Evidence: Section 11 Req 10. Section 5 Claim B (deterministic execution mandate, 95/100). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-036

Title: Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume)

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Hard-limit execution algorithms from exceeding strict max percentage of trailing 1-minute volume.

Decision: Hard-limit execution algorithms from exceeding strict max percentage of trailing 1-minute volume.

Supporting_Evidence: Section 11 Req 17. Section 10 Mode 21 (liquidity withdrawal from data feed lags). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-037

Title: Consolidated Tape Latency Threshold Disconnect

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Disconnect execution algorithms instantly if consolidated tape latency exceeds predefined microsecond thresholds.

Decision: Disconnect execution algorithms instantly if consolidated tape latency exceeds predefined microsecond thresholds.

Supporting_Evidence: Section 11 Req 18. Section 10 Mode 21 (liquidity withdrawal from latency). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Deployment of strategies with weak statistical edges; false signal validation.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-038

Title: Order Book Depth Monitoring with Market Order Halt on Evaporation

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Continuously track buy-side order book depth and halt market orders if depth evaporates.

Decision: Continuously track buy-side order book depth and halt market orders if depth evaporates.

Supporting_Evidence: Section 11 Req 19. Section 10 Mode 21. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-039

Title: Minimum 90% Branch Coverage in Backtesting Modules

Decision_Category: Validation

Decision_Origin: Direct_Evidence

Problem_Solved: Demand minimum 90% branch coverage (not just statement coverage) in backtesting modules.

Decision: Demand minimum 90% branch coverage (not just statement coverage) in backtesting modules.

Supporting_Evidence: Section 11 Req 21. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-040

Title: Intraday Minute Feed Completeness Verification (No Dropped Candles)

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Verify intraday minute feeds equal expected daily lengths (no dropped candles).

Decision: Verify intraday minute feeds equal expected daily lengths (no dropped candles).

Supporting_Evidence: Section 11 Req 24. Section 23 (synthetic anomaly injection test). Section 15 Tier 3 API reliability. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-041

Title: Cross-Verification of OHLCV Metrics Between Two Independent Data Providers

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Cross-verify OHLCV metrics between at least two independent data providers.

Decision: Cross-verify OHLCV metrics between at least two independent data providers.

Supporting_Evidence: Section 11 Req 25. Section 15 Tier 3 API reliability. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Model overfitting on historical data; randomized feature leakage.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Walk-forward OOS data accurately mimics future market regimes (§9 A5).

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-042

Title: Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban)

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Intentionally trigger Zerodha 429 errors in sandbox to validate deterministic exponential backoff and recovery logic.

Decision: Intentionally trigger Zerodha 429 errors in sandbox to validate deterministic exponential backoff and recovery logic.

Supporting_Evidence: Section 23. Section 9 Assumption 25 (solo operator diagnosis ambiguity). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Deployment of strategies with weak statistical edges; false signal validation.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: Medium

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-043

Title: SQLite WAL S3 Replication Recovery Under Hard Power-Off

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Force a hardware power-off during simulated high-volume SQLite transaction write.

Decision: Force a hardware power-off during simulated high-volume SQLite transaction write. Attempt recovery from Litestream S3 bucket upon reboot.

Supporting_Evidence: Section 23. Section 8 Finding 18 (Litestream millisecond recovery — Weakly Supported). | Audit: MODERATE

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Medium

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-044

Title: Synthetic Anomaly Injection Into Parquet Ingestion Pipeline

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Inject synthetic anomalies (extreme prices, missing minute bars) into the Parquet ingestion engine to verify forward-fill and outlier detectors catch and isolate corruption.

Decision: Inject synthetic anomalies (extreme prices, missing minute bars) into the Parquet ingestion engine to verify forward-fill and outlier detectors catch and isolate corruption.

Supporting_Evidence: Section 23. Section 9 Assumption 20 (autoencoder noise assumption). Section 10 Mode 12 (denoising masking real anomalies). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-045

Title: FastMCP Execution Boundary Validation Against Prompt Injection

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Attempt to prompt-inject the LLM to execute a trade directly, ensuring ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.

Decision: Attempt to prompt-inject the LLM to execute a trade directly, ensuring ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.

Supporting_Evidence: Section 23. Section 5 Claim B (deterministic execution, 95/100). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Status: Candidate

---

ADR_ID: ADR-046

Title: Walk-Forward OOS Regime Fidelity — Unvalidated Assumption

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Walk-forward OOS data may not accurately mimic future market regimes (hidden assumption, untested).

Decision: Walk-forward OOS data may not accurately mimic future market regimes (hidden assumption, untested).

Supporting_Evidence: Section 9 Assumption 5. Section 8 Finding 7 (AI grids cannot adapt across regimes). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Model overfitting on historical data; randomized feature leakage.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Medium

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-047

Title: Cron Job Overlap and Deadlock Risk Under API Latency Spikes

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Automated data pipeline cron jobs may overlap and deadlock if API latency spikes (hidden assumption, no mitigation in corpus).

Decision: Automated data pipeline cron jobs may overlap and deadlock if API latency spikes (hidden assumption, no mitigation in corpus).

Supporting_Evidence: Section 9 Assumption 4. No corresponding Section 11 Requirement. No Section 23 test. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-01: Cron job overlap deadlock.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.

Status: Deferred

---

ADR_ID: ADR-048

Title: Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift)

Decision_Category: Validation

Decision_Origin: Consensus_Inference

Problem_Solved: Market anomalies identified by auto-encoder are assumed to be noise rather than true structural shifts.

Decision: Market anomalies identified by auto-encoder are assumed to be noise rather than true structural shifts. This assumption is unvalidated.

Supporting_Evidence: Section 9 Assumption 20. Section 10 Mode 12 (denoising masking real anomalies). Section 23 (VAL-018 test operationalizes this). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Testing sandbox environment matches production routing behavior.

Unknowns: Quantitative statistical limits or test validation results are absent from corpus.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-049

Title: Hard Position Limit Enforcement via API Disconnection

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Configuring position limits as passive dashboard alerts rather than hard system halts allows breaches to go unmitigated during fast-moving markets.

Decision: Configuring position limits as passive dashboard alerts rather than hard system halts allows breaches to go unmitigated during fast-moving markets.

Supporting_Evidence: Section 10 Mode 4. Section 11 Req 4 (hard API disconnection mandate). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Passive alerts allowing trading limit breaches during volatile markets.

Failure_Modes_Introduced: False strategy halts; order routing blocks under temporary volatility.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-050

Title: Circuit Breaker for Trend-Following Dynamic Hedging Cycles

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: Dynamic hedging algorithms trend-follow by selling assets into declining markets, creating positive feedback loops that accelerate market crashes.

Decision: Dynamic hedging algorithms trend-follow by selling assets into declining markets, creating positive feedback loops that accelerate market crashes.

Supporting_Evidence: Section 7 Finding 11. Section 10 Mode 7. Section 11 Req 7. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Procyclical market selling cascades from trend-following dynamic hedging feedback loops.

Failure_Modes_Introduced: Unhedged portfolio risk under fast-moving trends if circuit triggers early.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-051

Title: Informational Cascade Volume Spike Halt

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: HFT algorithms mistakenly interpreting runaway execution loops as fundamental volume news; price-agnostic execution algorithms accelerating selling on false volume spikes.

Decision: HFT algorithms mistakenly interpreting runaway execution loops as fundamental volume news; price-agnostic execution algorithms accelerating selling on false volume spikes.

Supporting_Evidence: Section 10 Modes 8 and 20. Section 11 Req 8. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Passive alerts allowing trading limit breaches during volatile markets.

Failure_Modes_Introduced: False strategy halts; order routing blocks under temporary volatility.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-052

Title: Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Execution sizing must auto-scale against portfolio illiquidity; static initial margins are disallowed.

Decision: Execution sizing must auto-scale against portfolio illiquidity; static initial margins are disallowed.

Supporting_Evidence: Section 18 ADR-002. Section 9 Assumption 15. Section 10 Mode 15. Section 11 Req 13. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Procyclical margin compression; position size decoupling from asset liquidity.

Failure_Modes_Introduced: Premature position scaling reductions; capital utilization degradation.

Failure_Modes_Unresolved: GAP-05: VIX threshold for variation margin.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-05: VIX threshold for variation margin — unquantified.

Status: Candidate

---

ADR_ID: ADR-053

Title: Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: Extreme synthetic leverage hidden across multiple prime brokers bypasses standard risk constraints (Archegos).

Decision: Extreme synthetic leverage hidden across multiple prime brokers bypasses standard risk constraints (Archegos). APIs only track localized risk.

Supporting_Evidence: Section 7 Finding 20. Section 9 Assumption 14. Section 10 Mode 14. Section 11 Req 12. Section 12 Blind Spot (High). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Cross-broker leverage opacity allowing concentration limit breaches.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-10: Multi-broker aggregate margin exposure management.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13).

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-10: Multi-broker aggregate margin exposure management — missing research.

Status: Candidate

---

ADR_ID: ADR-054

Title: Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Risk managers repeatedly inflating bespoke scenario limits for prestigious clients.

Decision: Risk managers repeatedly inflating bespoke scenario limits for prestigious clients.

Supporting_Evidence: Section 9 Assumption 16. Section 10 Mode 16. Section 11 Req 14. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-055

Title: Variation Margin Release Restriction During Elevated Volatility

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Returning billions in variation margin immediately prior to a volatility default.

Decision: Returning billions in variation margin immediately prior to a volatility default.

Supporting_Evidence: Section 9 Assumption 17. Section 10 Mode 17. Section 11 Req 15. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Procyclical margin compression; position size decoupling from asset liquidity.

Failure_Modes_Introduced: Premature position scaling reductions; capital utilization degradation.

Failure_Modes_Unresolved: GAP-02: Non-ergodic VaR mathematical framework.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Mathematical framework for VaR under non-ergodic conditions (§13).

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-02: Non-ergodic VaR mathematical framework — missing research.

Status: Candidate

---

ADR_ID: ADR-056

Title: Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: Market non-ergodicity means historical correlation matrices break down during macro shocks.

Decision: Market non-ergodicity means historical correlation matrices break down during macro shocks. Market spreads fail to converge because of non-ergodic macroeconomic defaults.

Supporting_Evidence: Section 7 Finding 15. Section 9 Assumption 3 (LTCM). Section 10 Mode 18. Section 11 Req 16. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Mathematical framework for VaR under non-ergodic conditions (§13).

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-057

Title: ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: If AI/ML modules output wide quantile regression bands, deterministic execution logic must automatically scale down or halt orders (preventing Zillow Offers failure).

Decision: If AI/ML modules output wide quantile regression bands, deterministic execution logic must automatically scale down or halt orders (preventing Zillow Offers failure).

Supporting_Evidence: Section 18 ADR-003. Section 12 Blind Spot (Uncertainty Decoupling — High). Section 9 Assumption 11. Section 10 Mode 11. Section 11 Req 10. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-058

Title: ML Concept Drift Controls — Regime-Change Re-Anchoring

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: ML models anchoring to peak historical transaction data during sudden market downturn (Zillow Offers collapse).

Decision: ML models anchoring to peak historical transaction data during sudden market downturn (Zillow Offers collapse). Claude 3.5 Anchors to Outdated Sentiment (Concept Drift).

Supporting_Evidence: Section 7 Finding 16 (88/100). Section 10 Mode 10. Section 16 Confidence Matrix (88/100). Section 21 (concept drift as causal link). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-03: ML concept drift controls.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: High

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Difficult recovery with high severity.

Research_Gaps: GAP-03: ML concept drift controls — no §11 Req paired.

Status: Candidate

---

ADR_ID: ADR-059

Title: High-Velocity Operational Deployment Risk — Systemic Control Requirement

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: High-Velocity Operational Deployment Risk: 95/100 confidence rating.

Decision: High-Velocity Operational Deployment Risk: 95/100 confidence rating. Highest confidence score in corpus.

Supporting_Evidence: Section 16 Confidence Matrix (95/100). Section 21 Systemic Failure Path (full cascade chain). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Status: Candidate

---

ADR_ID: ADR-060

Title: Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: Real-time data feed latency causes electronic market makers to withdraw liquidity, causing Flash Crashes.

Decision: Real-time data feed latency causes electronic market makers to withdraw liquidity, causing Flash Crashes. Zerodha WebSockets Drop Packets → Deterministic Engine Misinterprets Lags as Zero-Volume Pauses.

Supporting_Evidence: Section 7 Finding 21 (92/100). Section 9 Assumption 6. Section 21 Systemic Failure Path. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Procyclical market selling cascades from trend-following dynamic hedging feedback loops.

Failure_Modes_Introduced: Unhedged portfolio risk under fast-moving trends if circuit triggers early.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-061

Title: Non-Ergodic VaR Methodology — Mathematical Framework Requirement

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: No mathematical framework for VaR under non-ergodic conditions currently exists within the system.

Decision: No mathematical framework for VaR under non-ergodic conditions currently exists within the system.

Supporting_Evidence: Section 13 (Missing Research). Section 7 Finding 15. Section 9 Assumption 3 (LTCM). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-02: Non-ergodic VaR mathematical framework.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Mathematical framework for VaR under non-ergodic conditions (§13).

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Difficult recovery with high severity.

Research_Gaps: GAP-02: Non-ergodic VaR mathematical framework — missing research.

Status: Candidate

---

ADR_ID: ADR-062

Title: Slippage and Transaction Cost Controls in Live Execution

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: Slippage and transaction costs frequently destroy theoretical backtest alpha.

Decision: Slippage and transaction costs frequently destroy theoretical backtest alpha.

Supporting_Evidence: Section 7 Finding 6. Section 21 Systemic Failure Path endpoint (15% execution slippage). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-04: Slippage threshold quantification.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-04: Slippage threshold quantification — no limit defined.

Status: Candidate

---

ADR_ID: ADR-063

Title: Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Denoising autoencoders masking real market anomalies from risk systems.

Decision: Denoising autoencoders masking real market anomalies from risk systems.

Supporting_Evidence: Section 9 Assumption 12 (hidden assumption). Section 10 Mode 12. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-064

Title: Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Replacing active, in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.

Decision: Replacing active, in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.

Supporting_Evidence: Section 10 Mode 25. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-06: Active risk committee governance standard.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Passive rubber-stamp email approvals failing to prevent concentrated exposure.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: GAP-06: Active risk committee governance standard — no §11 Req.

Status: Deferred

---

ADR_ID: ADR-065

Title: Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards

Decision_Category: Risk Control

Decision_Origin: Direct_Evidence

Problem_Solved: Audit Total Return Swap margins to match standard prime brokerage initial margin limits.

Decision: Audit Total Return Swap margins to match standard prime brokerage initial margin limits.

Supporting_Evidence: Section 11 Req 12. Section 7 Finding 20. Section 10 Mode 14. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Procyclical margin compression; position size decoupling from asset liquidity.

Failure_Modes_Introduced: Premature position scaling reductions; capital utilization degradation.

Failure_Modes_Unresolved: GAP-05: VIX threshold for variation margin.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Slippage threshold and margin scaling curves are missing.

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-05: VIX threshold for variation margin — unquantified.

Status: Candidate

---

ADR_ID: ADR-066

Title: Multi-Broker Simultaneous Collateral Fire Sale Prevention

Decision_Category: Risk Control

Decision_Origin: Consensus_Inference

Problem_Solved: Multiple prime brokers can liquidate identical collateral without causing correlated fire sales.

Decision: Multiple prime brokers can liquidate identical collateral without causing correlated fire sales. Assumption treated as safe; failure mode documents it collapsing underlying asset values.

Supporting_Evidence: Section 9 Assumption 19. Section 10 Mode 19. Section 21 Systemic Failure Path. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Cross-broker leverage opacity allowing concentration limit breaches.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-10: Multi-broker aggregate margin exposure management.

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Validation_Requirements: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Historical correlation matrices remain stable during volatile periods.

Unknowns: Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13).

Risk_Level: Critical

Governance_Impact: Uncontrolled leverage accumulation or concentration limit breach.

Human_Oversight_Required: Yes — Risk governance gate required.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-10: Multi-broker aggregate margin exposure management — missing research.

Status: Candidate

---

ADR_ID: ADR-067

Title: Prohibition of LLM Direct Trade Execution

Decision_Category: Human Oversight

Decision_Origin: Direct_Evidence

Problem_Solved: AI Direct Execution Safety confidence is rated 10/100 (Extremely Low Confidence — Actively Contradicted).

Decision: AI Direct Execution Safety confidence is rated 10/100 (Extremely Low Confidence — Actively Contradicted). LLMs may only generate JSON reasoning payloads via FastMCP; direct execution of kite.place_order() by any LLM is strictly prohibited.

Supporting_Evidence: Section 16 (10/100). Section 18 ADR-004. Section 20 Final Verdict. | Audit: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Autonomous AI models executing direct trades without deterministic human gate.

Failure_Modes_Introduced: Asynchronous FastMCP network latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-068

Title: Physical FastMCP Execution Boundary Enforcement

Decision_Category: Human Oversight

Decision_Origin: Consensus_Inference

Problem_Solved: Attempt to prompt-inject the LLM to execute a trade directly, ensuring ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.

Decision: Attempt to prompt-inject the LLM to execute a trade directly, ensuring ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.

Supporting_Evidence: Section 23. Section 18 ADR-004. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Prompt injection payloads executing direct server orders.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Lack of human gating during anomalous market events.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Status: Candidate

---

ADR_ID: ADR-069

Title: Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides

Decision_Category: Human Oversight

Decision_Origin: Direct_Evidence

Problem_Solved: Enforce mandatory multi-signature human approval for algorithmic pricing limit overrides.

Decision: Enforce mandatory multi-signature human approval for algorithmic pricing limit overrides.

Supporting_Evidence: Section 11 Req 11. Section 7 Finding 22 (92/100). Section 10 Mode 13. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Unauthorized pricing overrides; single-point-of-failure operator override.

Failure_Modes_Introduced: Operational delay during critical recovery window; manual override bottlenecks.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Multi-sig approval implementation details (roles, TTL) are missing.

Risk_Level: Critical

Governance_Impact: Bypassing human approval overrides or lack of defined signatories (roles, TTL) leading to unauthorized trading limits.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-070

Title: Human-in-the-Loop Gate for AI-Influenced Pricing Decisions

Decision_Category: Human Oversight

Decision_Origin: Direct_Evidence

Problem_Solved: Bypassing human-in-the-loop controls for AI pricing leads to toxic asset accumulation.

Decision: Bypassing human-in-the-loop controls for AI pricing leads to toxic asset accumulation. Confidence 92/100.

Supporting_Evidence: Section 7 Finding 22 (92/100). Section 10 Mode 13. Section 5 Claim B (95/100). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Autonomous agent runaway loops; lack of human-in-the-loop validation limits.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Multi-sig approval implementation details (roles, TTL) are missing.

Risk_Level: Critical

Governance_Impact: Lack of human gating during anomalous market events.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-071

Title: Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint)

Decision_Category: Human Oversight

Decision_Origin: Direct_Evidence

Problem_Solved: Execution must remain strictly deterministic, human-gated.

Decision: Execution must remain strictly deterministic, human-gated. Evidence Strength 95/100 due to SEBI regulations and Knight Capital failure.

Supporting_Evidence: Section 5 Claim B (95/100 — highest single evidence score in corpus). Section 20 Final Verdict. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Autonomous agent runaway loops; lack of human-in-the-loop validation limits.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: Critical

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-072

Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Decision_Category: Human Oversight

Decision_Origin: Consensus_Inference

Problem_Solved: Implement dedicated runbooks for PagerDuty/critical alerts to prevent fatigue.

Decision: Implement dedicated runbooks for PagerDuty/critical alerts to prevent fatigue. Failure Mode: Operators silencing critical alert channels due to high-volume alert fatigue.

Supporting_Evidence: Section 10 Mode 5. Section 11 Req 5. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Critical alert channels silencing by fatigued operators.

Failure_Modes_Introduced: Escalation loops loops; operator on-call stress.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Multi-sig approval implementation details (roles, TTL) are missing.

Risk_Level: Critical

Governance_Impact: Operators silencing critical alert channels leading to unmitigated operational failures.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-073

Title: Active Risk Committee Governance (Anti-Rubber-Stamp Requirement)

Decision_Category: Human Oversight

Decision_Origin: Consensus_Inference

Problem_Solved: Replacing active in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.

Decision: Replacing active in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.

Supporting_Evidence: Section 10 Mode 25. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Passive rubber-stamp committee approvals of concentrated exposures.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: GAP-06: Active risk committee governance standard.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Multi-sig approval implementation details (roles, TTL) are missing.

Risk_Level: Critical

Governance_Impact: Passive rubber-stamp email approvals failing to prevent concentrated exposure.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: GAP-06: Active risk committee governance standard — no §11 Req.

Status: Deferred

---

ADR_ID: ADR-074

Title: Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing

Decision_Category: Human Oversight

Decision_Origin: Direct_Evidence

Problem_Solved: The architecture's mandate to isolate AI exclusively to the 'Research/Cognitive' domain while locking mathematical execution, data storage, and order routing in deterministic, embedded SQL/Python envi...

Decision: The architecture's mandate to isolate AI exclusively to the 'Research/Cognitive' domain while locking mathematical execution, data storage, and order routing in deterministic, embedded SQL/Python environments is the strongest and most validated claim in the corpus. Attempting to build an 'Auto-Coder' or fully autonomous AI trading bot within SEBI/Zerodha constraints will definitively trigger catastrophic failure.

Supporting_Evidence: Section 20 Final Verdict. Section 16 (10/100). Section 7 Finding 9. Section 5 Claim B. | Audit: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Autonomous AI models executing direct trades without deterministic human gate.

Failure_Modes_Introduced: Asynchronous FastMCP network latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-075

Title: Quantile Regression Uncertainty Band Human Review Requirement

Decision_Category: Human Oversight

Decision_Origin: Architectural_Inference

Problem_Solved: Hidden Assumption: Quantile regression uncertainty bands are sufficient risk limiters even if only displayed visually — this assumption is unvalidated.

Decision: Hidden Assumption: Quantile regression uncertainty bands are sufficient risk limiters even if only displayed visually — this assumption is unvalidated.

Supporting_Evidence: Section 9 Assumption 17 (hidden assumption only — no confidence score). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Autonomous agent runaway loops; lack of human-in-the-loop validation limits.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Unknowns: Multi-sig approval implementation details (roles, TTL) are missing.

Risk_Level: Low

Governance_Impact: Lack of human gating during anomalous market events.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-076

Title: Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control)

Decision_Category: Human Oversight

Decision_Origin: Consensus_Inference

Problem_Solved: Bypassing human-in-the-loop safeguards to pursue aggressive automated volume growth is a documented failure mode.

Decision: Bypassing human-in-the-loop safeguards to pursue aggressive automated volume growth is a documented failure mode.

Supporting_Evidence: Section 10 Mode 13. Section 7 Finding 22 (92/100). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Autonomous AI models executing direct trades without deterministic human gate.

Failure_Modes_Introduced: Asynchronous FastMCP network latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Validation_Requirements: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Unknowns: Multi-sig approval implementation details (roles, TTL) are missing.

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — Core human oversight decision.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-077

Title: Embedded Zero-Copy Storage Architecture (DuckDB + SQLite)

Decision_Category: Infrastructure

Decision_Origin: Direct_Evidence

Problem_Solved: Storage MUST use embedded zero-copy architecture — DuckDB scanning Parquet files, attaching SQLite via sqlite_scanner.

Decision: Storage MUST use embedded zero-copy architecture — DuckDB scanning Parquet files, attaching SQLite via sqlite_scanner. Vector DBs explicitly excluded.

Supporting_Evidence: Section 6 (90/100 confidence). Section 19 (hard MUST). Section 7 Finding 24. | Audit: STRONG

Opposing_Evidence: Vector databases are actively contradicted by §6 and §19 because 95% of trading data is structured time-series (OHLCV).

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Vector database storage mismatch; SQLite row-based aggregations bottlenecks.

Failure_Modes_Introduced: High RAM usage; DuckDB thread allocation competition.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-078

Title: Hive-Partitioned Parquet as Mandatory Market Data Storage Format

Decision_Category: Infrastructure

Decision_Origin: Direct_Evidence

Problem_Solved: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month).

Decision: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month). Unstructured JSON data lakes prohibited.

Supporting_Evidence: Section 19 (hard MUST). Section 6 (DuckDB Parquet scan assumption). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-079

Title: SQLite WAL Management and S3 Replication Integrity

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: Local SQLite WAL file risks infinite growth if S3 upload stream hangs.

Decision: Local SQLite WAL file risks infinite growth if S3 upload stream hangs. WAL must cleanly revert without corrupting backtest engine when NSE voids trades.

Supporting_Evidence: Section 9 Assumption 18 (unbounded WAL). Section 17 (WAL revert-on-cancellation unknown). Section 21 (WAL lock as failure node). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Unbounded SQLite WAL growth disk exhaustion; async network dropouts.

Failure_Modes_Introduced: Replication network bandwidth load; S3 access rate-limit calls.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-080

Title: Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: S3/Litestream async backups assumed to not encounter network dropouts during local PC crashes.

Decision: S3/Litestream async backups assumed to not encounter network dropouts during local PC crashes. Hardware power-off recovery via Litestream must be empirically validated.

Supporting_Evidence: Section 9 Assumption 2. Section 23 (force power-off test). | Audit: MODERATE

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Unbounded SQLite WAL growth disk exhaustion; async network dropouts.

Failure_Modes_Introduced: Replication network bandwidth load; S3 access rate-limit calls.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Medium

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-081

Title: Automated Binary Hash Verification Across All Production Clusters

Decision_Category: Infrastructure

Decision_Origin: Direct_Evidence

Problem_Solved: All production clusters must execute automated binary hash checks before executing code to prevent Knight Capital-style deployments.

Decision: All production clusters must execute automated binary hash checks before executing code to prevent Knight Capital-style deployments.

Supporting_Evidence: Section 7 Finding 1 (95/100). Section 11 Req 1. Section 18 ADR-001. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Uncoordinated production rollouts; configuration namespace reuse.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-082

Title: Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation

Decision_Category: Infrastructure

Decision_Origin: Direct_Evidence

Problem_Solved: All configuration flags must be audited to ensure zero reuse of deprecated memory address spaces.

Decision: All configuration flags must be audited to ensure zero reuse of deprecated memory address spaces.

Supporting_Evidence: Section 7 Finding 25. Section 10 Mode 3. Section 11 Req 2. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-083

Title: Coordinated Deployment Strategy to Prevent Partial Binary Rollout

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: Deploying system binaries to some but not all production servers (uncoordinated deployment) is a failure mode.

Decision: Deploying system binaries to some but not all production servers (uncoordinated deployment) is a failure mode. Rolling back without validating server configurations spreads old bugs.

Supporting_Evidence: Section 10 Modes 1 and 6. Section 11 Req 6. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Uncoordinated production rollouts; configuration namespace reuse.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Status: Candidate

---

ADR_ID: ADR-084

Title: Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition

Decision_Category: Infrastructure

Decision_Origin: Architectural_Inference

Problem_Solved: Cloud deployment topology — Docker/Kubernetes architecture needed for Stage 2→4 transition — is identified as under-researched and missing.

Decision: Cloud deployment topology — Docker/Kubernetes architecture needed for Stage 2→4 transition — is identified as under-researched and missing.

Supporting_Evidence: Section 13 (Missing Research). Section 14 (under-researched corpus gap). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Uncoordinated production rollouts; configuration namespace reuse.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Precise cloud deployment topology (Docker/Kubernetes) needed when transitioning from Stage 2 (VM) to Stage 4 (SaaS) (§13, §14).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Status: Insufficient_Evidence

---

ADR_ID: ADR-085

Title: Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors

Decision_Category: Infrastructure

Decision_Origin: Direct_Evidence

Problem_Solved: The ingestion layer MUST implement deterministic exponential backoff when Zerodha returns HTTP 429 (rate limit exceeded) errors.

Decision: The ingestion layer MUST implement deterministic exponential backoff when Zerodha returns HTTP 429 (rate limit exceeded) errors.

Supporting_Evidence: Section 19 (hard MUST). Section 23 (sandbox test). Section 14 (10 orders/sec under ASGI unvalidated). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Zerodha 429 rate limit errors account suspension; sequential IP shadow-bans.

Failure_Modes_Introduced: Ingestion queue backlog growth under exponential backoff delays.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: High

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-086

Title: SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance

Decision_Category: Infrastructure

Decision_Origin: Direct_Evidence

Problem_Solved: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second.

Decision: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second. These are regulatory infrastructure constraints, not design choices.

Supporting_Evidence: Section 7 Finding 14 (high confidence). Section 22 (extreme-event broker latency unmeasured). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Zerodha 429 rate limit errors account suspension; sequential IP shadow-bans.

Failure_Modes_Introduced: Ingestion queue backlog growth under exponential backoff delays.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: High

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-087

Title: OAuth Token Auto-Refresh Without Manual Two-Factor Authentication

Decision_Category: Infrastructure

Decision_Origin: Architectural_Inference

Problem_Solved: OAuth tokens assumed to be automatically refreshable without requiring manual two-factor authentication daily.

Decision: OAuth tokens assumed to be automatically refreshable without requiring manual two-factor authentication daily. Assumption unvalidated.

Supporting_Evidence: Section 9 Assumption 22. | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: OAuth tokens can be automatically refreshed without daily manual 2FA (§9 A22).

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: OAuth refresh failure locks trade execution daemon and stops system from sending orders.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-088

Title: Data Pipeline Cron Job Overlap and Deadlock Prevention

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: Automated data pipeline cron jobs assumed not to overlap and deadlock if API latency spikes.

Decision: Automated data pipeline cron jobs assumed not to overlap and deadlock if API latency spikes. No deadlock prevention mechanism specified.

Supporting_Evidence: Section 9 Assumption 4. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-01: Cron job overlap deadlock.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.

Status: Deferred

---

ADR_ID: ADR-089

Title: Execution Circuit Breaker on Consolidated Tape Latency Breach

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: Execution algorithms must be instantly disconnected if consolidated tape latency exceeds predefined microsecond thresholds.

Decision: Execution algorithms must be instantly disconnected if consolidated tape latency exceeds predefined microsecond thresholds. Incorrect pricing data causes infinite downstream loops.

Supporting_Evidence: Section 11 Req 18. Section 10 Mode 24. Section 21 (cascade node). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-090

Title: FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: FastMCP eliminates network boundaries by serving tool calls via ASGI alongside FastAPI on the same process, avoiding inter-service network hops for LLM tool execution.

Decision: FastMCP eliminates network boundaries by serving tool calls via ASGI alongside FastAPI on the same process, avoiding inter-service network hops for LLM tool execution.

Supporting_Evidence: Section 7 Finding 10. Section 14 (ASGI event loop blocking unproven). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Status: Deferred

---

ADR_ID: ADR-091

Title: Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: During extreme sovereign macro shocks, Zerodha WebSocket connections drop packets, causing the deterministic engine to misinterpret lags — initiating a systemic cascade failure path.

Decision: During extreme sovereign macro shocks, Zerodha WebSocket connections drop packets, causing the deterministic engine to misinterpret lags — initiating a systemic cascade failure path.

Supporting_Evidence: Section 21 (systemic failure path — packet loss → cascade → 15% slippage). Section 22 (missing empirical latency/uptime data). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: Event loop latency logs under live-load are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-092

Title: DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load

Decision_Category: Infrastructure

Decision_Origin: Consensus_Inference

Problem_Solved: The assumption that file-system I/O is fast enough to support DuckDB Parquet scans locally without memory overflow must be validated via stress-testing against multi-year 1-minute partitioned Parquet ...

Decision: The assumption that file-system I/O is fast enough to support DuckDB Parquet scans locally without memory overflow must be validated via stress-testing against multi-year 1-minute partitioned Parquet data.

Supporting_Evidence: Section 6 (assumption + validation requirement). Section 22 (DuckDB/SQLite concurrency benchmarks missing). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Vector database storage mismatch; SQLite row-based aggregations bottlenecks.

Failure_Modes_Introduced: High RAM usage; DuckDB thread allocation competition.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-093

Title: Strict LLM Execution Prohibition via FastMCP

Decision_Category: AI Boundary

Decision_Origin: Direct_Evidence

Problem_Solved: LLMs may only generate JSON reasoning payloads via FastMCP.

Decision: LLMs may only generate JSON reasoning payloads via FastMCP. Direct execution of kite.place_order() by any LLM is strictly prohibited.

Supporting_Evidence: Section 18 ADR-004. Section 5 Claim B (95/100). Section 16 (10/100 AI execution safety). Section 20 Final Verdict. | Audit: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Status: Candidate

---

ADR_ID: ADR-094

Title: AI Domain Segregation — Cognitive vs. Deterministic Execution

Decision_Category: AI Boundary

Decision_Origin: Direct_Evidence

Problem_Solved: Isolate AI exclusively to the 'Research/Cognitive' domain.

Decision: Isolate AI exclusively to the 'Research/Cognitive' domain. Mathematical execution, data storage, and order routing must be locked in deterministic, embedded SQL/Python environments.

Supporting_Evidence: Section 1 (Executive Summary). Section 4 (Cross-Document Consensus). Section 20 Final Verdict. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-095

Title: Prohibition on Fully Autonomous AI Execution Grids

Decision_Category: AI Boundary

Decision_Origin: Direct_Evidence

Problem_Solved: Fully AI execution grids cannot adapt perfectly to 2024 data after training on 2023 data — weakly supported.

Decision: Fully AI execution grids cannot adapt perfectly to 2024 data after training on 2023 data — weakly supported. Corpus verdict: attempting a fully autonomous AI trading bot within SEBI/Zerodha will definitively trigger catastrophic failure.

Supporting_Evidence: Section 8 Finding 7 (weakly supported — autonomy claim false). Section 20 Final Verdict. Section 4 Consensus. | Audit: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-096

Title: Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing

Decision_Category: AI Boundary

Decision_Origin: Direct_Evidence

Problem_Solved: Bypassing human-in-the-loop controls for AI pricing leads to toxic asset accumulation.

Decision: Bypassing human-in-the-loop controls for AI pricing leads to toxic asset accumulation. Confidence 92/100.

Supporting_Evidence: Section 7 Finding 22 (92/100). Section 10 Mode 13. Section 11 Req 11. Section 5 Claim B. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: SLM context window degradation processing raw HTML; model mismatch.

Failure_Modes_Introduced: Frontier API token cost growth; routing latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-097

Title: Model Uncertainty Integration — AI Output as Execution Halt Trigger

Decision_Category: AI Boundary

Decision_Origin: Consensus_Inference

Problem_Solved: If AI/ML modules output wide quantile regression bands, deterministic execution logic must automatically scale down or halt orders (preventing Zillow Offers failure).

Decision: If AI/ML modules output wide quantile regression bands, deterministic execution logic must automatically scale down or halt orders (preventing Zillow Offers failure).

Supporting_Evidence: Section 18 ADR-003. Section 12 Blind Spot (Uncertainty Decoupling — High). Section 10 Mode 11. Section 11 Req 10. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Unknowns: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-098

Title: AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math

Decision_Category: AI Boundary

Decision_Origin: Consensus_Inference

Problem_Solved: Exact mathematical formulas converting semantic FinBERT scores (-1 to 1) into localized position sizing (Kelly fractions) without violating deterministic execution boundaries — classified as Missing R...

Decision: Exact mathematical formulas converting semantic FinBERT scores (-1 to 1) into localized position sizing (Kelly fractions) without violating deterministic execution boundaries — classified as Missing Research.

Supporting_Evidence: Section 13 (Missing Research). Section 5 (remaining uncertainty on AI/deterministic integration). Section 3 (Domain C — signal architecture black-box risk). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Uncertainty quantile bands visual-only display bypasses; signal weighting errors.

Failure_Modes_Introduced: Mathematical scaling errors; position size volatility.

Failure_Modes_Unresolved: GAP-11: FinBERT score to Kelly fraction conversion math.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Unknowns: Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-11: FinBERT score to Kelly fraction conversion math — unresolved.

Status: Deferred

---

ADR_ID: ADR-099

Title: LLM Prohibition on Deterministic Chronological Sorting and Binary Math

Decision_Category: AI Boundary

Decision_Origin: Direct_Evidence

Problem_Solved: LLM Autonomous Agents fail at deterministic chronological sorting and binary math.

Decision: LLM Autonomous Agents fail at deterministic chronological sorting and binary math.

Supporting_Evidence: Section 7 Finding 9 (Top 25 Highest Confidence Findings). | Audit: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-100

Title: Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk

Decision_Category: AI Boundary

Decision_Origin: Direct_Evidence

Problem_Solved: 'Auto-Coder' AI backtesters generate massive survivorship bias and curve-fitting.

Decision: 'Auto-Coder' AI backtesters generate massive survivorship bias and curve-fitting.

Supporting_Evidence: Section 7 Finding 12. Section 20 Final Verdict. Section 8 Finding 7. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Delisted stocks are not necessary for a valid backtest (§9 A23).

Unknowns: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Risk_Level: Critical

Governance_Impact: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-101

Title: LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary

Decision_Category: AI Boundary

Decision_Origin: Consensus_Inference

Problem_Solved: LLMs writing dynamic SQL queries via MCP against DuckDB — classified as WEAKLY SUPPORTED with qualifier: Extreme hallucination/OOM risk.

Decision: LLMs writing dynamic SQL queries via MCP against DuckDB — classified as WEAKLY SUPPORTED with qualifier: Extreme hallucination/OOM risk.

Supporting_Evidence: Section 8 Finding 13 (Weakly Supported — safety claim unverified, risk label severe). | Audit: MODERATE

Opposing_Evidence: LLMs writing dynamic SQL queries via MCP against DuckDB is contradicted by §8 Finding 13 (extreme hallucination/OOM risk).

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: LLM generated dynamic SQL hallucination; database OOM crash.

Failure_Modes_Introduced: SQL syntax error exceptions; parser thread locks.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-102

Title: LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM

Decision_Category: AI Boundary

Decision_Origin: Consensus_Inference

Problem_Solved: Complex reasoning MUST route to Frontier models (Claude 3.

Decision: Complex reasoning MUST route to Frontier models (Claude 3.5/Gemini 1.5), routine logic to Fast models (GPT-4o-mini), PII/Sanitization to local edge SLMs (Qwen 2.5).

Supporting_Evidence: Section 19 (Architecture Findings — LLM Routing). Section 8 Findings 9 and 25 (SLM capability limits). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: SLM context window degradation processing raw HTML; model mismatch.

Failure_Modes_Introduced: Frontier API token cost growth; routing latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-103

Title: Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary

Decision_Category: AI Boundary

Decision_Origin: Architectural_Inference

Problem_Solved: Local SLM (Llama 3.

Decision: Local SLM (Llama 3.1 8B) accurately performing complex sentiment tagging on highly nuanced SEBI filings without hallucination — classified as WEAKLY SUPPORTED / unverified.

Supporting_Evidence: Section 8 Findings 9 and 25 (Weakly Supported). Section 9 Assumption 24 (FinBERT US→Indian domain transfer unvalidated). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: Local SLM capabilities are contradicted by §8 Finding 25 which flags context degradation when processing raw HTML filings.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: AI hallucination payloads execution; prompt injection compromise; capability boundaries breaches.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-104

Title: Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification

Decision_Category: AI Boundary

Decision_Origin: Consensus_Inference

Problem_Solved: The FastMCP Execution Boundary must be tested via prompt injection: ensure ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.

Decision: The FastMCP Execution Boundary must be tested via prompt injection: ensure ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.

Supporting_Evidence: Section 23 (Assumptions to Test). Section 22 (LLM hallucination rates on FastMCP — missing evidence). Section 21 (FastMCP JSON processing a runaway order as failure node). Section 18 ADR-004. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: AI hallucination payloads execution; prompt injection compromise; capability boundaries breaches.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Unknowns: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — AI boundary requires human gating.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Status: Deferred

---

ADR_ID: ADR-105

Title: Automated Binary Hash Verification Before Production Deployment

Decision_Category: Reliability

Decision_Origin: Direct_Evidence

Problem_Solved: Automated deployment mismatch causes systemic execution failure (Knight Capital).

Decision: Automated deployment mismatch causes systemic execution failure (Knight Capital). All production clusters must execute automated binary hash checks before executing code.

Supporting_Evidence: Section 7 Finding 1 (95/100). Section 10 Mode 1. Section 11 Req 1. Section 15 Tier 1/2 evidence. Section 16 (95/100). Section 18 ADR-001. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Knight Capital-style rollout mismatches; config address space reuse.

Failure_Modes_Introduced: Deployment pipeline validation latency.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Status: Candidate

---

ADR_ID: ADR-106

Title: Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors

Decision_Category: Reliability

Decision_Origin: Direct_Evidence

Problem_Solved: The system MUST implement deterministic exponential backoff in the ingestion layer to handle Zerodha HTTP 429 errors safely.

Decision: The system MUST implement deterministic exponential backoff in the ingestion layer to handle Zerodha HTTP 429 errors safely.

Supporting_Evidence: Section 19 (hard MUST). Section 9 Assumption 25. Section 23 (sandbox test). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Zerodha 429 errors; IP shadow-bans.

Failure_Modes_Introduced: Execution queue backlogs during rates spike.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Unknowns: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Risk_Level: High

Governance_Impact: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-107

Title: Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Order-routing systems running continuous loops without parent-order balance checks is a top failure mode.

Decision: Order-routing systems running continuous loops without parent-order balance checks is a top failure mode. Hard-code continuous parent-order balance checks directly into execution loops.

Supporting_Evidence: Section 10 Mode 2. Section 11 Req 3. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Runaway order routing loops.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-108

Title: Deprecated Code Purge to Prevent Configuration Flag Reactivation

Decision_Category: Reliability

Decision_Origin: Direct_Evidence

Problem_Solved: Reusing a configuration flag address space that reactivates a deprecated legacy module is a top failure mode.

Decision: Reusing a configuration flag address space that reactivates a deprecated legacy module is a top failure mode. Deprecated code left in production binaries = massive unquantifiable risk.

Supporting_Evidence: Section 7 Finding 25. Section 9 Assumption 8. Section 10 Mode 3. Section 11 Req 2. Section 12 Blind Spot (High). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-109

Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Operators silencing critical alert channels due to high-volume alert fatigue is a top failure mode.

Decision: Operators silencing critical alert channels due to high-volume alert fatigue is a top failure mode. Implement dedicated runbooks for PagerDuty/critical alerts to prevent fatigue.

Supporting_Evidence: Section 10 Mode 5. Section 11 Req 5. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: PagerDuty alerts silencing.

Failure_Modes_Introduced: On-call escalation overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operators silencing critical alert channels leading to unmitigated operational failures.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-110

Title: Validated Configuration Rollback Procedure Across All Nodes

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Rolling back a deployment without validating server configurations spreads old bugs.

Decision: Rolling back a deployment without validating server configurations spreads old bugs.

Supporting_Evidence: Section 10 Mode 6. Section 11 Req 6. | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: High — Significant impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-111

Title: Automated Chaos and Sanity Tests Across All Nodes Before Production Routing

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Deploy automated sanity and chaos tests across all nodes before production routing.

Decision: Deploy automated sanity and chaos tests across all nodes before production routing.

Supporting_Evidence: Section 11 Req 6. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Deployment approval gate.

Architecture_Criticality: Medium — Moderate impact on system reliability.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-112

Title: Execution Algorithm Disconnection on Consolidated Tape Latency Breach

Decision_Category: Reliability

Decision_Origin: Direct_Evidence

Problem_Solved: Real-time data feed latency causes electronic market makers to withdraw liquidity, causing Flash Crashes.

Decision: Real-time data feed latency causes electronic market makers to withdraw liquidity, causing Flash Crashes. Disconnect execution algorithms instantly if consolidated tape latency exceeds predefined microsecond thresholds.

Supporting_Evidence: Section 7 Finding 21 (92/100). Section 10 Mode 21. Section 11 Req 18. Section 12 Blind Spot (Medium). Section 16 (92/100). Section 21 (systemic cascade node). | Audit: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: STRONG

Confidence_Level: High

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Candidate

---

ADR_ID: ADR-113

Title: Buy-Side Order Book Depth Monitoring with Market Order Halt

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Exchange Stop-Logic completely trapping unexecuted buy-side orders.

Decision: Exchange Stop-Logic completely trapping unexecuted buy-side orders. Continuously track buy-side order book depth and halt market orders if depth evaporates.

Supporting_Evidence: Section 10 Mode 22. Section 11 Req 19. | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-114

Title: Capital Buffer Requirement for Retroactive Exchange Trade Cancellation

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Exchanges retroactively erasing valid trades to protect clearinghouse solvency.

Decision: Exchanges retroactively erasing valid trades to protect clearinghouse solvency. Require capital buffers specifically designed to absorb retroactive exchange trade cancellations.

Supporting_Evidence: Section 9 Assumption 1. Section 10 Mode 23. Section 11 Req 20. Section 12 Blind Spot (Medium). Section 17 (SQLite WAL revert unknown). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Exchanges (NSE/BSE) will not retroactively erase or cancel valid trades during a clearing member default (§9 A1).

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-115

Title: SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure

Decision_Category: Reliability

Decision_Origin: Architectural_Inference

Problem_Solved: S3/Litestream async backups assumed not to encounter network dropouts during local PC crashes.

Decision: S3/Litestream async backups assumed not to encounter network dropouts during local PC crashes. SQLite WAL assumed not to grow infinitely if S3 upload hangs. Litestream millisecond-exact recovery — Weakly Supported.

Supporting_Evidence: Section 8 Finding 18 (Weakly Supported). Section 9 Assumptions 2 and 18. Section 21 (WAL lock → execution circuit timeout). Section 23 (power-off test required). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: Force power-off during write; disconnect S3 network upload stream.

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-116

Title: Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks

Decision_Category: Reliability

Decision_Origin: Architectural_Inference

Problem_Solved: Automated data pipeline cron jobs assumed not to overlap and deadlock if API latency spikes.

Decision: Automated data pipeline cron jobs assumed not to overlap and deadlock if API latency spikes.

Supporting_Evidence: Section 9 Assumption 4. | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: GAP-01: Cron job overlap deadlock.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.

Status: Insufficient_Evidence

---

ADR_ID: ADR-117

Title: Automated OAuth Token Refresh Without Manual Two-Factor Authentication

Decision_Category: Reliability

Decision_Origin: Architectural_Inference

Problem_Solved: OAuth tokens assumed to be automatically refreshable without manual two-factor authentication intervention daily.

Decision: OAuth tokens assumed to be automatically refreshable without manual two-factor authentication intervention daily.

Supporting_Evidence: Section 9 Assumption 22. Section 7 Finding 14 (SEBI OAuth mandate). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: OAuth tokens can be automatically refreshed without daily manual 2FA (§9 A22).

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: OAuth refresh failure locks trade execution daemon and stops system from sending orders.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: None identified in corpus.

Status: Insufficient_Evidence

---

ADR_ID: ADR-118

Title: Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops

Decision_Category: Reliability

Decision_Origin: Consensus_Inference

Problem_Solved: Incorrect pricing data triggering infinite downstream processing loops (Content-to-Timing failure) is a top failure mode.

Decision: Incorrect pricing data triggering infinite downstream processing loops (Content-to-Timing failure) is a top failure mode.

Supporting_Evidence: Section 10 Mode 24. Section 21 (misinterpretation → runaway order routing). | Audit: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: MODERATE

Confidence_Level: Medium

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Detailed post-mortem metrics or API uptime logs are missing.

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: Yes — Execution safety gate.

Architecture_Criticality: Critical — System-critical failure severity.

Research_Gaps: None identified in corpus.

Status: Deferred

---

ADR_ID: ADR-119

Title: DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load

Decision_Category: Reliability

Decision_Origin: Architectural_Inference

Problem_Solved: No benchmarks exist detailing memory load when DuckDB joins a 50 GB Parquet data lake with a live, writing SQLite database locally.

Decision: No benchmarks exist detailing memory load when DuckDB joins a 50 GB Parquet data lake with a live, writing SQLite database locally.

Supporting_Evidence: Section 22 (Missing Evidence). Section 6 (validation required). Section 14 (unsupported — ASGI 10 orders/sec without event loop blocking). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Validation_Methods: Force power-off during write; disconnect S3 network upload stream.

Validation_Requirements: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Critical — Cascading failure path leads to capital destruction.

Research_Gaps: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — entirely absent.

Status: Insufficient_Evidence

---

ADR_ID: ADR-120

Title: API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events

Decision_Category: Reliability

Decision_Origin: Architectural_Inference

Problem_Solved: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (election days, budget days) are missing.

Decision: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (election days, budget days) are missing. Angel One intraday data gaps reported (intermittency).

Supporting_Evidence: Section 8 Finding 6 (Weakly Supported). Section 15 (Tier 3 evidence). Section 22 (Missing Evidence). | Audit: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Evidence_Strength: WEAK (Evidence_Weak)

Confidence_Level: Low

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: GAP-09: Third-party broker API uptime during extreme tail-risk events — lack of SLA guarantees.

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Validation_Requirements: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Unknowns: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).

Risk_Level: Critical

Governance_Impact: Operational non-compliance risk.

Human_Oversight_Required: No — Automated validation sufficient.

Architecture_Criticality: Low — Minimal architectural impact.

Research_Gaps: GAP-09: Third-party broker API uptime during extreme events — no empirical data.

Status: Insufficient_Evidence

---

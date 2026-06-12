# Failure Mode Matrix Report

**Phase:** 3 — Failure Mode Analysis (Reliability & Survivability Stress-Test)
**Status:** Complete — All Candidates Failure-Mapped
**Total Candidates Analyzed:** 120 (DG: 26 | VAL: 22 | RC: 18 | HO: 10 | INF: 16 | AIB: 12 | REL: 16)
**Date:** 2026-06-04

---

Candidate_ID: DG-001

Decision_Title: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs)

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-002

Decision_Title: SQLite Exclusion from Standalone Time-Series Aggregation

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-003

Decision_Title: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited)

Failure_Modes_Reduced: Unstructured JSON analytical queries storage exhaustion; high memory load on unstructured raw reads.

Failure_Modes_Introduced: Memory overflow risk during multi-year queries; scan plan memory bottlenecks.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-004

Decision_Title: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source

Failure_Modes_Reduced: Dropped candle backtest failures; incomplete provider feeds; historical pricing mismatches.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-005

Decision_Title: Corporate Actions — Mandatory Split-Adjusted Data Requirement

Failure_Modes_Reduced: Alpha inflation from unadjusted splits; indicators corruption; incorrect price backtests.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Complex corporate de-mergers or stock split events.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-006

Decision_Title: Provider Selection — Upstox Uplink for Historical Split-Adjusted Data

Failure_Modes_Reduced: Dropped candle backtest failures; incomplete provider feeds; historical pricing mismatches.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Complex corporate de-mergers or stock split events.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: DG-007

Decision_Title: Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited)

Failure_Modes_Reduced: Overfitting on randomized cross-validation datasets; chronologically leaked features.

Failure_Modes_Introduced: Increased model backtesting execution time; CPU thread starvation.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: High

---

Candidate_ID: DG-008

Decision_Title: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit

Failure_Modes_Reduced: Regulatory non-compliance accounts suspension; rate limits breaches.

Failure_Modes_Introduced: Daemon connection queues latency; OAuth token refresh hangs.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: Rate limit exceeded -> exponential backoff delays orders -> queue backlogs grow -> execution lag increases -> price slippage increases -> strategy capital drawdown.

Trigger_Conditions: Consecutive order placement requests exceeding 10 orders/second.

Detection_Methods: HTTP response status logs; broker rate limit header monitoring.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: DG-009

Decision_Title: Production Binary Hygiene — Deprecated Code Removal Requirement

Failure_Modes_Reduced: Legacy address spaces re-activation; uncoordinated production binary behavior.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Deployment binary mismatch -> nodes execute different version -> state database sync fails -> orders route on incorrect signals -> massive execution loss.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Automated checksum verification failures logs during deployment startup.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: DG-010

Decision_Title: Yahoo Finance Adjusted Close Mis-Adjustment Risk

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: DG-011

Decision_Title: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers

Failure_Modes_Reduced: Dropped candle backtest failures; incomplete provider feeds; historical pricing mismatches.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-012

Decision_Title: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles)

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-013

Decision_Title: Survivorship Bias — Delisted Stock Inclusion Requirement

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: DG-014

Decision_Title: NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures

Failure_Modes_Reduced: Alpha inflation from unadjusted splits; indicators corruption; incorrect price backtests.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Complex corporate de-mergers or stock split events.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: DG-015

Decision_Title: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Medium

Detectability: Difficult

Recovery_Difficulty: Difficult

Confidence: Medium

---

Candidate_ID: DG-016

Decision_Title: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion

Failure_Modes_Reduced: Unstructured JSON analytical queries storage exhaustion; high memory load on unstructured raw reads.

Failure_Modes_Introduced: Memory overflow risk during multi-year queries; scan plan memory bottlenecks.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: API latency spikes -> cron jobs overlap -> database table locks -> execution engine misses market candles -> signal generation stalls -> delayed orders executed on old prices.

Trigger_Conditions: LLM processing of un-sanitized news feeds or SEBI filings containing adversarial text.

Detection_Methods: FastMCP ASGI exception logs; input validation error alerts.

Severity: High

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-017

Decision_Title: Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: DG-018

Decision_Title: Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: WebSocket drops packets -> engine misinterprets lag as zero-volume -> AI model anchors to outdated sentiment -> orders route to empty book -> 15% execution slippage.

Trigger_Conditions: Extreme market volatility events causing network packet congestion.

Detection_Methods: WebSocket heartbeat timeouts logs; packet sequence checks.

Severity: Medium

Detectability: Difficult

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: DG-019

Decision_Title: Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Clearinghouse cancels trade -> local SQLite state desyncs -> system believes hedge is active -> unhedged exposure exposed to market gap -> strategy bankruptcy.

Trigger_Conditions: Clearinghouse default or extreme market-maker default event.

Detection_Methods: Clearing member account balance desync alerts; trade status audits.

Severity: Critical

Detectability: Hidden

Recovery_Difficulty: Extreme

Confidence: Medium

---

Candidate_ID: DG-020

Decision_Title: SQLite WAL Transaction Integrity on NSE Trade Void Events

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: Low

---

Candidate_ID: DG-021

Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: DG-022

Decision_Title: LLM Context Window Degradation on Raw HTML NSE/SEC Filings

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: DG-023

Decision_Title: Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale

Failure_Modes_Reduced: Row-based DB analytic queries bottleneck; SQL aggregation execution timeouts; unstructured data storage.

Failure_Modes_Introduced: High local filesystem I/O load; concurrent write/read lockouts; DuckDB event loop blocking.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: High concurrent write load during market open/close joined with heavy DuckDB queries.

Detection_Methods: DuckDB memory profile monitoring; SQLite write transaction timeouts logs.

Severity: Low

Detectability: Difficult

Recovery_Difficulty: Extreme

Confidence: Low

---

Candidate_ID: DG-024

Decision_Title: Missing Research — VaR Modeling Under Non-Ergodic Market Conditions

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: GAP-02: Non-ergodic VaR mathematical framework.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Extreme

Confidence: Low

---

Candidate_ID: DG-025

Decision_Title: Missing Research — Multi-Broker Aggregate Margin Exposure Management

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: GAP-10: Multi-broker aggregate margin exposure management.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: DG-026

Decision_Title: Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals

Failure_Modes_Reduced: Data ingestion failures; data quality corruption; database state desyncs.

Failure_Modes_Introduced: Additional validation pipeline latency; parsing overhead.

Failure_Modes_Unresolved: Data de-merger adjustment errors; provider data tape latency spikes.

Cascading_Failures: Data feed corruption -> signal generation invalid -> incorrect trades executed -> margin call.

Trigger_Conditions: Broker API historical feed updates or de-mergers.

Detection_Methods: Outlier price range checks; missing candle completeness audits.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: VAL-001

Decision_Title: Walk-Forward Cross-Validation Over Randomized k-Fold CV

Failure_Modes_Reduced: Model overfitting on historical data; randomized feature leakage.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: High

---

Candidate_ID: VAL-002

Decision_Title: Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe)

Failure_Modes_Reduced: Deployment of strategies with weak statistical edges; false signal validation.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-003

Decision_Title: Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: VAL-004

Decision_Title: Cluster-Wide Binary Hash Verification Before Live Routing

Failure_Modes_Reduced: Uncoordinated production deployments mismatch; deployment state desyncs.

Failure_Modes_Introduced: CI/CD deployment delays; server startup latency.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Deployment binary mismatch -> nodes execute different version -> state database sync fails -> orders route on incorrect signals -> massive execution loss.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Automated checksum verification failures logs during deployment startup.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: VAL-005

Decision_Title: Audit All Configuration Flags for Deprecated Memory Address Reuse

Failure_Modes_Reduced: Configuration namespaces address reuse reactivating legacy code.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-006

Decision_Title: Hard-Coded Parent-Order Balance Checks in Execution Loops

Failure_Modes_Reduced: Runaway execution loops executing trades without balance check.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-007

Decision_Title: Automated Sanity and Chaos Tests Across All Nodes Before Production Routing

Failure_Modes_Reduced: Production server configuration rollbacks spreading old bugs.

Failure_Modes_Introduced: Deployment pipeline blockers; test environment execution delays.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-008

Decision_Title: Population Stability Index (PSI) Tracking for Concept Drift Detection

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: High CPU computation load for statistical checks; false drift alerts.

Failure_Modes_Unresolved: GAP-03: ML concept drift controls.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Difficult

Recovery_Difficulty: Difficult

Confidence: High

---

Candidate_ID: VAL-009

Decision_Title: Automatic Bid Size Reduction Under High Quantile Uncertainty

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: VAL-010

Decision_Title: Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume)

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-011

Decision_Title: Consolidated Tape Latency Threshold Disconnect

Failure_Modes_Reduced: Deployment of strategies with weak statistical edges; false signal validation.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: WebSocket drops packets -> engine misinterprets lag as zero-volume -> AI model anchors to outdated sentiment -> orders route to empty book -> 15% execution slippage.

Trigger_Conditions: Extreme market volatility events causing network packet congestion.

Detection_Methods: WebSocket heartbeat timeouts logs; packet sequence checks.

Severity: High

Detectability: Easy

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-012

Decision_Title: Order Book Depth Monitoring with Market Order Halt on Evaporation

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-013

Decision_Title: Minimum 90% Branch Coverage in Backtesting Modules

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-014

Decision_Title: Intraday Minute Feed Completeness Verification (No Dropped Candles)

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-015

Decision_Title: Cross-Verification of OHLCV Metrics Between Two Independent Data Providers

Failure_Modes_Reduced: Model overfitting on historical data; randomized feature leakage.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-016

Decision_Title: Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban)

Failure_Modes_Reduced: Deployment of strategies with weak statistical edges; false signal validation.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: Rate limit exceeded -> exponential backoff delays orders -> queue backlogs grow -> execution lag increases -> price slippage increases -> strategy capital drawdown.

Trigger_Conditions: Consecutive order placement requests exceeding 10 orders/second.

Detection_Methods: HTTP response status logs; broker rate limit header monitoring.

Severity: Medium

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: Medium

---

Candidate_ID: VAL-017

Decision_Title: SQLite WAL S3 Replication Recovery Under Hard Power-Off

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: Medium

---

Candidate_ID: VAL-018

Decision_Title: Synthetic Anomaly Injection Into Parquet Ingestion Pipeline

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: API latency spikes -> cron jobs overlap -> database table locks -> execution engine misses market candles -> signal generation stalls -> delayed orders executed on old prices.

Trigger_Conditions: LLM processing of un-sanitized news feeds or SEBI filings containing adversarial text.

Detection_Methods: FastMCP ASGI exception logs; input validation error alerts.

Severity: High

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-019

Decision_Title: FastMCP Execution Boundary Validation Against Prompt Injection

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: LLM processing of un-sanitized news feeds or SEBI filings containing adversarial text.

Detection_Methods: FastMCP ASGI exception logs; input validation error alerts.

Severity: Critical

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: VAL-020

Decision_Title: Walk-Forward OOS Regime Fidelity — Unvalidated Assumption

Failure_Modes_Reduced: Model overfitting on historical data; randomized feature leakage.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: Medium

---

Candidate_ID: VAL-021

Decision_Title: Cron Job Overlap and Deadlock Risk Under API Latency Spikes

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: GAP-01: Cron job overlap deadlock.

Cascading_Failures: API latency spikes -> cron jobs overlap -> database table locks -> execution engine misses market candles -> signal generation stalls -> delayed orders executed on old prices.

Trigger_Conditions: API latency spikes exceeding the cron scheduling interval.

Detection_Methods: Process lock audits; execution scheduling delay monitoring alerts.

Severity: Medium

Detectability: Difficult

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: VAL-022

Decision_Title: Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift)

Failure_Modes_Reduced: Validation pipeline gaps; testing coverage deficits; signal validation errors.

Failure_Modes_Introduced: Increased validation execution overhead; deployment pipeline bottlenecks.

Failure_Modes_Unresolved: Out-of-sample walk-forward regime shifts mismatches.

Cascading_Failures: Validation gate fails -> overfitted model deployed -> live execution regime shift -> massive drawdown.

Trigger_Conditions: Production software rollouts or major regime shifts.

Detection_Methods: Sharpe ratio sanity checks; backtest coverage metrics.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: RC-001

Decision_Title: Hard Position Limit Enforcement via API Disconnection

Failure_Modes_Reduced: Passive alerts allowing trading limit breaches during volatile markets.

Failure_Modes_Introduced: False strategy halts; order routing blocks under temporary volatility.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: Critical

Detectability: Easy

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-002

Decision_Title: Circuit Breaker for Trend-Following Dynamic Hedging Cycles

Failure_Modes_Reduced: Procyclical market selling cascades from trend-following dynamic hedging feedback loops.

Failure_Modes_Introduced: Unhedged portfolio risk under fast-moving trends if circuit triggers early.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-003

Decision_Title: Informational Cascade Volume Spike Halt

Failure_Modes_Reduced: Passive alerts allowing trading limit breaches during volatile markets.

Failure_Modes_Introduced: False strategy halts; order routing blocks under temporary volatility.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-004

Decision_Title: Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity

Failure_Modes_Reduced: Procyclical margin compression; position size decoupling from asset liquidity.

Failure_Modes_Introduced: Premature position scaling reductions; capital utilization degradation.

Failure_Modes_Unresolved: GAP-05: VIX threshold for variation margin.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-005

Decision_Title: Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls

Failure_Modes_Reduced: Cross-broker leverage opacity allowing concentration limit breaches.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-10: Multi-broker aggregate margin exposure management.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-006

Decision_Title: Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-007

Decision_Title: Variation Margin Release Restriction During Elevated Volatility

Failure_Modes_Reduced: Procyclical margin compression; position size decoupling from asset liquidity.

Failure_Modes_Introduced: Premature position scaling reductions; capital utilization degradation.

Failure_Modes_Unresolved: GAP-02: Non-ergodic VaR mathematical framework.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-008

Decision_Title: Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-009

Decision_Title: ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-010

Decision_Title: ML Concept Drift Controls — Regime-Change Re-Anchoring

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-03: ML concept drift controls.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Difficult

Recovery_Difficulty: Difficult

Confidence: High

---

Candidate_ID: RC-011

Decision_Title: High-Velocity Operational Deployment Risk — Systemic Control Requirement

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-012

Decision_Title: Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker

Failure_Modes_Reduced: Procyclical market selling cascades from trend-following dynamic hedging feedback loops.

Failure_Modes_Introduced: Unhedged portfolio risk under fast-moving trends if circuit triggers early.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Extreme market volatility events causing network packet congestion.

Detection_Methods: WebSocket heartbeat timeouts logs; packet sequence checks.

Severity: High

Detectability: Difficult

Recovery_Difficulty: Difficult

Confidence: High

---

Candidate_ID: RC-013

Decision_Title: Non-Ergodic VaR Methodology — Mathematical Framework Requirement

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-02: Non-ergodic VaR mathematical framework.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Extreme

Confidence: High

---

Candidate_ID: RC-014

Decision_Title: Slippage and Transaction Cost Controls in Live Execution

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-04: Slippage threshold quantification.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-015

Decision_Title: Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: Co-incident market liquidity evaporation.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: Medium

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: RC-016

Decision_Title: Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals

Failure_Modes_Reduced: Risk control overrides; portfolio margin breaches; concentration risk accumulation.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-06: Active risk committee governance standard.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: RC-017

Decision_Title: Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards

Failure_Modes_Reduced: Procyclical margin compression; position size decoupling from asset liquidity.

Failure_Modes_Introduced: Premature position scaling reductions; capital utilization degradation.

Failure_Modes_Unresolved: GAP-05: VIX threshold for variation margin.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: RC-018

Decision_Title: Multi-Broker Simultaneous Collateral Fire Sale Prevention

Failure_Modes_Reduced: Cross-broker leverage opacity allowing concentration limit breaches.

Failure_Modes_Introduced: Increased signal processing latency; false risk limits triggers.

Failure_Modes_Unresolved: GAP-10: Multi-broker aggregate margin exposure management.

Cascading_Failures: Risk control fails -> leverage limits breached -> market shock triggers liquidation -> strategy insolvency.

Trigger_Conditions: VIX surge or portfolio margin limits breach.

Detection_Methods: Margin utilization warnings; scenario limit alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-001

Decision_Title: Prohibition of LLM Direct Trade Execution

Failure_Modes_Reduced: Autonomous AI models executing direct trades without deterministic human gate.

Failure_Modes_Introduced: Asynchronous FastMCP network latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-002

Decision_Title: Physical FastMCP Execution Boundary Enforcement

Failure_Modes_Reduced: Prompt injection payloads executing direct server orders.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-003

Decision_Title: Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides

Failure_Modes_Reduced: Unauthorized pricing overrides; single-point-of-failure operator override.

Failure_Modes_Introduced: Operational delay during critical recovery window; manual override bottlenecks.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: Urgent operational request to change trading limits during market stress.

Detection_Methods: Multi-sig transaction logs audit; limit change event alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-004

Decision_Title: Human-in-the-Loop Gate for AI-Influenced Pricing Decisions

Failure_Modes_Reduced: Autonomous agent runaway loops; lack of human-in-the-loop validation limits.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Human gate bypassed -> autonomous trading loop runs -> runaway order routing -> capital destruction.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-005

Decision_Title: Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint)

Failure_Modes_Reduced: Autonomous agent runaway loops; lack of human-in-the-loop validation limits.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-006

Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Failure_Modes_Reduced: Critical alert channels silencing by fatigued operators.

Failure_Modes_Introduced: Escalation loops loops; operator on-call stress.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Human gate bypassed -> autonomous trading loop runs -> runaway order routing -> capital destruction.

Trigger_Conditions: System anomaly generating high volume of low-priority PagerDuty alerts.

Detection_Methods: PagerDuty incident escalation logs; alert-to-resolution duration monitoring.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Easy

Confidence: Medium

---

Candidate_ID: HO-007

Decision_Title: Active Risk Committee Governance (Anti-Rubber-Stamp Requirement)

Failure_Modes_Reduced: Passive rubber-stamp committee approvals of concentrated exposures.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: GAP-06: Active risk committee governance standard.

Cascading_Failures: Human gate bypassed -> autonomous trading loop runs -> runaway order routing -> capital destruction.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: HO-008

Decision_Title: Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing

Failure_Modes_Reduced: Autonomous AI models executing direct trades without deterministic human gate.

Failure_Modes_Introduced: Asynchronous FastMCP network latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: HO-009

Decision_Title: Quantile Regression Uncertainty Band Human Review Requirement

Failure_Modes_Reduced: Autonomous agent runaway loops; lack of human-in-the-loop validation limits.

Failure_Modes_Introduced: Operational gates bottlenecks; latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: HO-010

Decision_Title: Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control)

Failure_Modes_Reduced: Autonomous AI models executing direct trades without deterministic human gate.

Failure_Modes_Introduced: Asynchronous FastMCP network latency overhead.

Failure_Modes_Unresolved: Intentional insider bypass of human gating safeguards.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: AI pricing models producing anomalous values.

Detection_Methods: Model pricing logs audit; human gate override logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: INF-001

Decision_Title: Embedded Zero-Copy Storage Architecture (DuckDB + SQLite)

Failure_Modes_Reduced: Vector database storage mismatch; SQLite row-based aggregations bottlenecks.

Failure_Modes_Introduced: High RAM usage; DuckDB thread allocation competition.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: INF-002

Decision_Title: Hive-Partitioned Parquet as Mandatory Market Data Storage Format

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: Database block -> trading system freezes -> unable to exit positions during crash -> capital wipeout.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: INF-003

Decision_Title: SQLite WAL Management and S3 Replication Integrity

Failure_Modes_Reduced: Unbounded SQLite WAL growth disk exhaustion; async network dropouts.

Failure_Modes_Introduced: Replication network bandwidth load; S3 access rate-limit calls.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: High

---

Candidate_ID: INF-004

Decision_Title: Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery

Failure_Modes_Reduced: Unbounded SQLite WAL growth disk exhaustion; async network dropouts.

Failure_Modes_Introduced: Replication network bandwidth load; S3 access rate-limit calls.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: Medium

Detectability: Difficult

Recovery_Difficulty: Difficult

Confidence: Medium

---

Candidate_ID: INF-005

Decision_Title: Automated Binary Hash Verification Across All Production Clusters

Failure_Modes_Reduced: Uncoordinated production rollouts; configuration namespace reuse.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: Deployment binary mismatch -> nodes execute different version -> state database sync fails -> orders route on incorrect signals -> massive execution loss.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Automated checksum verification failures logs during deployment startup.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: INF-006

Decision_Title: Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: Database block -> trading system freezes -> unable to exit positions during crash -> capital wipeout.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: INF-007

Decision_Title: Coordinated Deployment Strategy to Prevent Partial Binary Rollout

Failure_Modes_Reduced: Uncoordinated production rollouts; configuration namespace reuse.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Cascading_Failures: Deployment binary mismatch -> nodes execute different version -> state database sync fails -> orders route on incorrect signals -> massive execution loss.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Automated checksum verification failures logs during deployment startup.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: INF-008

Decision_Title: Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition

Failure_Modes_Reduced: Uncoordinated production rollouts; configuration namespace reuse.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Cascading_Failures: Database block -> trading system freezes -> unable to exit positions during crash -> capital wipeout.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: INF-009

Decision_Title: Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors

Failure_Modes_Reduced: Zerodha 429 rate limit errors account suspension; sequential IP shadow-bans.

Failure_Modes_Introduced: Ingestion queue backlog growth under exponential backoff delays.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: Rate limit exceeded -> exponential backoff delays orders -> queue backlogs grow -> execution lag increases -> price slippage increases -> strategy capital drawdown.

Trigger_Conditions: Consecutive order placement requests exceeding 10 orders/second.

Detection_Methods: HTTP response status logs; broker rate limit header monitoring.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: INF-010

Decision_Title: SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance

Failure_Modes_Reduced: Zerodha 429 rate limit errors account suspension; sequential IP shadow-bans.

Failure_Modes_Introduced: Ingestion queue backlog growth under exponential backoff delays.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: Rate limit exceeded -> exponential backoff delays orders -> queue backlogs grow -> execution lag increases -> price slippage increases -> strategy capital drawdown.

Trigger_Conditions: Consecutive order placement requests exceeding 10 orders/second.

Detection_Methods: HTTP response status logs; broker rate limit header monitoring.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: INF-011

Decision_Title: OAuth Token Auto-Refresh Without Manual Two-Factor Authentication

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: Database block -> trading system freezes -> unable to exit positions during crash -> capital wipeout.

Trigger_Conditions: Expiration of OAuth tokens requiring manual multi-factor authentication.

Detection_Methods: Authentication token status logs; connection retry failures.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: INF-012

Decision_Title: Data Pipeline Cron Job Overlap and Deadlock Prevention

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-01: Cron job overlap deadlock.

Cascading_Failures: API latency spikes -> cron jobs overlap -> database table locks -> execution engine misses market candles -> signal generation stalls -> delayed orders executed on old prices.

Trigger_Conditions: API latency spikes exceeding the cron scheduling interval.

Detection_Methods: Process lock audits; execution scheduling delay monitoring alerts.

Severity: Medium

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: INF-013

Decision_Title: Execution Circuit Breaker on Consolidated Tape Latency Breach

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: WebSocket drops packets -> engine misinterprets lag as zero-volume -> AI model anchors to outdated sentiment -> orders route to empty book -> 15% execution slippage.

Trigger_Conditions: Extreme market volatility events causing network packet congestion.

Detection_Methods: WebSocket heartbeat timeouts logs; packet sequence checks.

Severity: Critical

Detectability: Difficult

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: INF-014

Decision_Title: FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: INF-015

Decision_Title: Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events

Failure_Modes_Reduced: Database performance bottlenecks; deployment configuration desyncs; rate limit locks.

Failure_Modes_Introduced: Infrastructure resource constraints; dependency complexity.

Failure_Modes_Unresolved: Local hardware disk write failures recovery.

Cascading_Failures: WebSocket drops packets -> engine misinterprets lag as zero-volume -> AI model anchors to outdated sentiment -> orders route to empty book -> 15% execution slippage.

Trigger_Conditions: Extreme market volatility events causing network packet congestion.

Detection_Methods: WebSocket heartbeat timeouts logs; packet sequence checks.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: INF-016

Decision_Title: DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load

Failure_Modes_Reduced: Vector database storage mismatch; SQLite row-based aggregations bottlenecks.

Failure_Modes_Introduced: High RAM usage; DuckDB thread allocation competition.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: Operator overrides pricing limit -> multi-sig approval bypassed -> system accumulates toxic assets -> capital margins breached -> prime broker liquidates collateral.

Trigger_Conditions: Network partitions or local hardware power failure.

Detection_Methods: Litestream replication delay metrics; local disk space alerts.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: AIB-001

Decision_Title: Strict LLM Execution Prohibition via FastMCP

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: AIB-002

Decision_Title: AI Domain Segregation — Cognitive vs. Deterministic Execution

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: AIB-003

Decision_Title: Prohibition on Fully Autonomous AI Execution Grids

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: AIB-004

Decision_Title: Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing

Failure_Modes_Reduced: SLM context window degradation processing raw HTML; model mismatch.

Failure_Modes_Introduced: Frontier API token cost growth; routing latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: AI boundary breached -> invalid payload accepted -> ASGI thread locks -> trade routing hangs.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: AIB-005

Decision_Title: Model Uncertainty Integration — AI Output as Execution Halt Trigger

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: AIB-006

Decision_Title: AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math

Failure_Modes_Reduced: Uncertainty quantile bands visual-only display bypasses; signal weighting errors.

Failure_Modes_Introduced: Mathematical scaling errors; position size volatility.

Failure_Modes_Unresolved: GAP-11: FinBERT score to Kelly fraction conversion math.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Difficult

Confidence: Medium

---

Candidate_ID: AIB-007

Decision_Title: LLM Prohibition on Deterministic Chronological Sorting and Binary Math

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: Deployment binary mismatch -> nodes execute different version -> state database sync fails -> orders route on incorrect signals -> massive execution loss.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: Automated checksum verification failures logs during deployment startup.

Severity: Critical

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: AIB-008

Decision_Title: Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk

Failure_Modes_Reduced: AI direct order execution SEBI violations; model direct routing.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: AIB-009

Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary

Failure_Modes_Reduced: LLM generated dynamic SQL hallucination; database OOM crash.

Failure_Modes_Introduced: SQL syntax error exceptions; parser thread locks.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: AI boundary breached -> invalid payload accepted -> ASGI thread locks -> trade routing hangs.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: AIB-010

Decision_Title: LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM

Failure_Modes_Reduced: SLM context window degradation processing raw HTML; model mismatch.

Failure_Modes_Introduced: Frontier API token cost growth; routing latency jitter.

Failure_Modes_Unresolved: Frontier models API service outages.

Cascading_Failures: AI boundary breached -> invalid payload accepted -> ASGI thread locks -> trade routing hangs.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: AIB-011

Decision_Title: Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary

Failure_Modes_Reduced: AI hallucination payloads execution; prompt injection compromise; capability boundaries breaches.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: AI boundary breached -> invalid payload accepted -> ASGI thread locks -> trade routing hangs.

Trigger_Conditions: Frontier models API outages or cold-starts.

Detection_Methods: JSON schema validation error logs; API error code alerts.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: AIB-012

Decision_Title: Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification

Failure_Modes_Reduced: AI hallucination payloads execution; prompt injection compromise; capability boundaries breaches.

Failure_Modes_Introduced: Model API dependency failure points; latency jitter.

Failure_Modes_Unresolved: GAP-07: FastMCP ASGI physical block verification.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: LLM processing of un-sanitized news feeds or SEBI filings containing adversarial text.

Detection_Methods: FastMCP ASGI exception logs; input validation error alerts.

Severity: Medium

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: REL-001

Decision_Title: Automated Binary Hash Verification Before Production Deployment

Failure_Modes_Reduced: Knight Capital-style rollout mismatches; config address space reuse.

Failure_Modes_Introduced: Deployment pipeline validation latency.

Failure_Modes_Unresolved: GAP-12: Cloud deployment topology Stage 2→4.

Cascading_Failures: Deployment binary mismatch -> nodes execute different version -> state database sync fails -> orders route on incorrect signals -> massive execution loss.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: Automated checksum verification failures logs during deployment startup.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: REL-002

Decision_Title: Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors

Failure_Modes_Reduced: Zerodha 429 errors; IP shadow-bans.

Failure_Modes_Introduced: Execution queue backlogs during rates spike.

Failure_Modes_Unresolved: ASGI event loop blocking under 10 orders/sec rate limit load.

Cascading_Failures: Rate limit exceeded -> exponential backoff delays orders -> queue backlogs grow -> execution lag increases -> price slippage increases -> strategy capital drawdown.

Trigger_Conditions: Consecutive order placement requests exceeding 10 orders/second.

Detection_Methods: HTTP response status logs; broker rate limit header monitoring.

Severity: High

Detectability: Easy

Recovery_Difficulty: Easy

Confidence: High

---

Candidate_ID: REL-003

Decision_Title: Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops

Failure_Modes_Reduced: Runaway order routing loops.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Prompt injection bypasses gate -> LLM executes order directly -> loop ignores position limits -> runaway leverage -> account default.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: REL-004

Decision_Title: Deprecated Code Purge to Prevent Configuration Flag Reactivation

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: REL-005

Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Failure_Modes_Reduced: PagerDuty alerts silencing.

Failure_Modes_Introduced: On-call escalation overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: System anomaly generating high volume of low-priority PagerDuty alerts.

Detection_Methods: PagerDuty incident escalation logs; alert-to-resolution duration monitoring.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Easy

Confidence: Medium

---

Candidate_ID: REL-006

Decision_Title: Validated Configuration Rollback Procedure Across All Nodes

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: High

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: REL-007

Decision_Title: Automated Chaos and Sanity Tests Across All Nodes Before Production Routing

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: Medium

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: REL-008

Decision_Title: Execution Algorithm Disconnection on Consolidated Tape Latency Breach

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: WebSocket drops packets -> engine misinterprets lag as zero-volume -> AI model anchors to outdated sentiment -> orders route to empty book -> 15% execution slippage.

Trigger_Conditions: Extreme market volatility events causing network packet congestion.

Detection_Methods: WebSocket heartbeat timeouts logs; packet sequence checks.

Severity: Critical

Detectability: Easy

Recovery_Difficulty: Moderate

Confidence: High

---

Candidate_ID: REL-009

Decision_Title: Buy-Side Order Book Depth Monitoring with Market Order Halt

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: REL-010

Decision_Title: Capital Buffer Requirement for Retroactive Exchange Trade Cancellation

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Clearinghouse cancels trade -> local SQLite state desyncs -> system believes hedge is active -> unhedged exposure exposed to market gap -> strategy bankruptcy.

Trigger_Conditions: Clearinghouse default or extreme market-maker default event.

Detection_Methods: Clearing member account balance desync alerts; trade status audits.

Severity: Critical

Detectability: Hidden

Recovery_Difficulty: Extreme

Confidence: Medium

---

Candidate_ID: REL-011

Decision_Title: SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: Low

Detectability: Difficult

Recovery_Difficulty: Difficult

Confidence: Low

---

Candidate_ID: REL-012

Decision_Title: Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: GAP-01: Cron job overlap deadlock.

Cascading_Failures: API latency spikes -> cron jobs overlap -> database table locks -> execution engine misses market candles -> signal generation stalls -> delayed orders executed on old prices.

Trigger_Conditions: API latency spikes exceeding the cron scheduling interval.

Detection_Methods: Process lock audits; execution scheduling delay monitoring alerts.

Severity: Low

Detectability: Hidden

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: REL-013

Decision_Title: Automated OAuth Token Refresh Without Manual Two-Factor Authentication

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: Expiration of OAuth tokens requiring manual multi-factor authentication.

Detection_Methods: Authentication token status logs; connection retry failures.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

Candidate_ID: REL-014

Decision_Title: Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: Litestream WAL recovery millisecond state loss.

Cascading_Failures: Recovery loop fails -> database state stale -> system executes stale orders -> massive slippage.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: Critical

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Medium

---

Candidate_ID: REL-015

Decision_Title: DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — analytical blocking of SQLite WAL writes.

Cascading_Failures: Litestream async backup fails -> local hardware crash occurs -> SQLite database state corrupts -> system boots on stale state -> routes duplicate orders -> strategy capital depletion.

Trigger_Conditions: High concurrent write load during market open/close joined with heavy DuckDB queries.

Detection_Methods: DuckDB memory profile monitoring; SQLite write transaction timeouts logs.

Severity: Low

Detectability: Difficult

Recovery_Difficulty: Extreme

Confidence: Low

---

Candidate_ID: REL-016

Decision_Title: API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events

Failure_Modes_Reduced: Uptime failures; system recovery latency; failover desyncs.

Failure_Modes_Introduced: Automated recovery execution overhead.

Failure_Modes_Unresolved: GAP-09: Third-party broker API uptime during extreme tail-risk events — lack of SLA guarantees.

Cascading_Failures: WebSocket drops packets -> engine misinterprets lag as zero-volume -> AI model anchors to outdated sentiment -> orders route to empty book -> 15% execution slippage.

Trigger_Conditions: Local power-off event during active writes.

Detection_Methods: System startup integrity checks; WAL check logs.

Severity: Low

Detectability: Moderate

Recovery_Difficulty: Moderate

Confidence: Low

---

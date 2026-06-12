# Validation Matrix Report

**Phase:** 4 — Validation Analysis (Verification & Stress-Testing Rules)
**Status:** Complete — All Candidates Validation-Mapped
**Total Candidates Mapped:** 120 (DG: 26 | VAL: 22 | RC: 18 | HO: 10 | INF: 16 | AIB: 12 | REL: 16)
**Date:** 2026-06-04

---

Candidate_ID: DG-001

Decision_Title: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-002

Decision_Title: SQLite Exclusion from Standalone Time-Series Aggregation

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-003

Decision_Title: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-004

Decision_Title: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-005

Decision_Title: Corporate Actions — Mandatory Split-Adjusted Data Requirement

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-006

Decision_Title: Provider Selection — Upstox Uplink for Historical Split-Adjusted Data

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-007

Decision_Title: Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-008

Decision_Title: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit

Required_Validation_Levels: Level 1: Research_Validation, Level 5: Production_Validation

Validation_Methods: Static analysis audit of codebase; manual SEBI compliance legal check.

Promotion_Criteria: Zero deprecated addresses in final binary hash signature.

Rejection_Criteria: Detection of deprecated memory address reuse or compliance violation.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: Audit confidence >= High

Failure_Conditions: Any compliance issue detected during production build check.

Revalidation_Triggers: schema_change, source_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-009

Decision_Title: Production Binary Hygiene — Deprecated Code Removal Requirement

Required_Validation_Levels: Level 1: Research_Validation, Level 5: Production_Validation

Validation_Methods: Static analysis audit of codebase; manual SEBI compliance legal check.

Promotion_Criteria: Zero deprecated addresses in final binary hash signature.

Rejection_Criteria: Detection of deprecated memory address reuse or compliance violation.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: Audit confidence >= High

Failure_Conditions: Any compliance issue detected during production build check.

Revalidation_Triggers: schema_change, source_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-010

Decision_Title: Yahoo Finance Adjusted Close Mis-Adjustment Risk

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-011

Decision_Title: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-012

Decision_Title: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-013

Decision_Title: Survivorship Bias — Delisted Stock Inclusion Requirement

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-014

Decision_Title: NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-015

Decision_Title: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-016

Decision_Title: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-017

Decision_Title: Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-018

Decision_Title: Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-019

Decision_Title: Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-020

Decision_Title: SQLite WAL Transaction Integrity on NSE Trade Void Events

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-021

Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-022

Decision_Title: LLM Context Window Degradation on Raw HTML NSE/SEC Filings

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-023

Decision_Title: Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-024

Decision_Title: Missing Research — VaR Modeling Under Non-Ergodic Market Conditions

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-025

Decision_Title: Missing Research — Multi-Broker Aggregate Margin Exposure Management

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: DG-026

Decision_Title: Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Inject synthetic anomalies into ingestion pipeline; verify schema updates; E2E historical backtests.

Promotion_Criteria: 100% data ingestion completeness on synthetic test feeds; no dropped candles over 30 days.

Rejection_Criteria: Unadjusted stock splits detected; data tape latency > threshold.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Data reconciliation mismatch > 0.01% between independent providers.

Revalidation_Triggers: source_change, schema_change, reconciliation_failure, vendor_change

Validation_Confidence: High

---

Candidate_ID: VAL-001

Decision_Title: Walk-Forward Cross-Validation Over Randomized k-Fold CV

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-002

Decision_Title: Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-003

Decision_Title: Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-004

Decision_Title: Cluster-Wide Binary Hash Verification Before Live Routing

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-005

Decision_Title: Audit All Configuration Flags for Deprecated Memory Address Reuse

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-006

Decision_Title: Hard-Coded Parent-Order Balance Checks in Execution Loops

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-007

Decision_Title: Automated Sanity and Chaos Tests Across All Nodes Before Production Routing

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-008

Decision_Title: Population Stability Index (PSI) Tracking for Concept Drift Detection

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-009

Decision_Title: Automatic Bid Size Reduction Under High Quantile Uncertainty

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-010

Decision_Title: Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-011

Decision_Title: Consolidated Tape Latency Threshold Disconnect

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-012

Decision_Title: Order Book Depth Monitoring with Market Order Halt on Evaporation

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-013

Decision_Title: Minimum 90% Branch Coverage in Backtesting Modules

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-014

Decision_Title: Intraday Minute Feed Completeness Verification (No Dropped Candles)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-015

Decision_Title: Cross-Verification of OHLCV Metrics Between Two Independent Data Providers

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-016

Decision_Title: Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-017

Decision_Title: SQLite WAL S3 Replication Recovery Under Hard Power-Off

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-018

Decision_Title: Synthetic Anomaly Injection Into Parquet Ingestion Pipeline

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-019

Decision_Title: FastMCP Execution Boundary Validation Against Prompt Injection

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-020

Decision_Title: Walk-Forward OOS Regime Fidelity — Unvalidated Assumption

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-021

Decision_Title: Cron Job Overlap and Deadlock Risk Under API Latency Spikes

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: VAL-022

Decision_Title: Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Walk-forward cross-validation run; Sharpe ratio deflation audit; branch coverage check.

Promotion_Criteria: positive_oos_performance; no_regime_specific_dependency; t_stat > 3.0

Rejection_Criteria: p_value >= 0.01 or t_stat <= 3.0 or deflated_sharpe <= 1.5 in OOS walk-forward.

Evidence_Threshold: p_value < 0.01, t_stat > 3.0, deflated_sharpe > 1.5

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Degradation of Sharpe ratio below 1.0 or unexplained backtest deviation.

Revalidation_Triggers: dependency_upgrade, deployment_change, schema_change, source_change

Validation_Confidence: Very_High

---

Candidate_ID: RC-001

Decision_Title: Hard Position Limit Enforcement via API Disconnection

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-002

Decision_Title: Circuit Breaker for Trend-Following Dynamic Hedging Cycles

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-003

Decision_Title: Informational Cascade Volume Spike Halt

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-004

Decision_Title: Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-005

Decision_Title: Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-006

Decision_Title: Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-007

Decision_Title: Variation Margin Release Restriction During Elevated Volatility

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-008

Decision_Title: Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-009

Decision_Title: ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-010

Decision_Title: ML Concept Drift Controls — Regime-Change Re-Anchoring

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-011

Decision_Title: High-Velocity Operational Deployment Risk — Systemic Control Requirement

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-012

Decision_Title: Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-013

Decision_Title: Non-Ergodic VaR Methodology — Mathematical Framework Requirement

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-014

Decision_Title: Slippage and Transaction Cost Controls in Live Execution

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-015

Decision_Title: Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-016

Decision_Title: Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-017

Decision_Title: Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: RC-018

Decision_Title: Multi-Broker Simultaneous Collateral Fire Sale Prevention

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Historical_Backtest_Validation, Level 3: Walk_Forward_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Historical replay of market crashes (e.g. March 2020); paper trading risk limit tests.

Promotion_Criteria: Zero position limit breaches during 30 days paper trade; no unexplained failures.

Rejection_Criteria: Hedge execution latency > 1 second or risk limits exceeded without system halt.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: positive_oos_performance, no_regime_specific_dependency

Failure_Conditions: Loss exceeding maximum drawdown limits; failure of hard halt circuit breaker.

Revalidation_Triggers: schema_change, source_change, vendor_change

Validation_Confidence: High

---

Candidate_ID: HO-001

Decision_Title: Prohibition of LLM Direct Trade Execution

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-002

Decision_Title: Physical FastMCP Execution Boundary Enforcement

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-003

Decision_Title: Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-004

Decision_Title: Human-in-the-Loop Gate for AI-Influenced Pricing Decisions

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-005

Decision_Title: Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint)

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-006

Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-007

Decision_Title: Active Risk Committee Governance (Anti-Rubber-Stamp Requirement)

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-008

Decision_Title: Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-009

Decision_Title: Quantile Regression Uncertainty Band Human Review Requirement

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: HO-010

Decision_Title: Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control)

Required_Validation_Levels: Level 1: Research_Validation, Level 4: Paper_Trading_Validation, Level 5: Production_Validation

Validation_Methods: Simulate prompt injection and human override scenarios; audit multi-sig approval latency.

Promotion_Criteria: 100% human-in-the-loop overrides require multi-signature; no unauthorized order routing.

Rejection_Criteria: Single operator override successful without multi-signature approval.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Order routed without deterministic human gate check or signature approval.

Revalidation_Triggers: model_version_change, api_contract_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: INF-001

Decision_Title: Embedded Zero-Copy Storage Architecture (DuckDB + SQLite)

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-002

Decision_Title: Hive-Partitioned Parquet as Mandatory Market Data Storage Format

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-003

Decision_Title: SQLite WAL Management and S3 Replication Integrity

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-004

Decision_Title: Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-005

Decision_Title: Automated Binary Hash Verification Across All Production Clusters

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-006

Decision_Title: Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-007

Decision_Title: Coordinated Deployment Strategy to Prevent Partial Binary Rollout

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-008

Decision_Title: Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-009

Decision_Title: Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-010

Decision_Title: SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-011

Decision_Title: OAuth Token Auto-Refresh Without Manual Two-Factor Authentication

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-012

Decision_Title: Data Pipeline Cron Job Overlap and Deadlock Prevention

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-013

Decision_Title: Execution Circuit Breaker on Consolidated Tape Latency Breach

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-014

Decision_Title: FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-015

Decision_Title: Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: INF-016

Decision_Title: DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Local power failure simulation; S3 network dropout injection; high concurrent read/write test (50GB scale).

Promotion_Criteria: DuckDB write transaction lock contention <= 50ms; S3 backup completes within SLA after reconnection.

Rejection_Criteria: Database corruption on power-off; SQLite WAL file growth exceeds disk limit.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Data corruption in WAL; backup replication lag > 5 minutes.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: Medium

---

Candidate_ID: AIB-001

Decision_Title: Strict LLM Execution Prohibition via FastMCP

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-002

Decision_Title: AI Domain Segregation — Cognitive vs. Deterministic Execution

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-003

Decision_Title: Prohibition on Fully Autonomous AI Execution Grids

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-004

Decision_Title: Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-005

Decision_Title: Model Uncertainty Integration — AI Output as Execution Halt Trigger

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-006

Decision_Title: AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-007

Decision_Title: LLM Prohibition on Deterministic Chronological Sorting and Binary Math

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-008

Decision_Title: Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-009

Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-010

Decision_Title: LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-011

Decision_Title: Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: AIB-012

Decision_Title: Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: FastMCP ASGI gateway prompt injection stress testing; LLM payload schema validation check.

Promotion_Criteria: 0% direct order execution by LLM; 100% of LLM reasoning payloads pass JSON schemas.

Rejection_Criteria: LLM successfully bypasses FastMCP boundary to execute order directly; malformed JSON accepted.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: LLM outputs invalid schema payloads exceeding 1% error rate.

Revalidation_Triggers: model_version_change, api_contract_change, latency_degradation, context_window_change, tool_access_change

Validation_Confidence: High

---

Candidate_ID: REL-001

Decision_Title: Automated Binary Hash Verification Before Production Deployment

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-002

Decision_Title: Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-003

Decision_Title: Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-004

Decision_Title: Deprecated Code Purge to Prevent Configuration Flag Reactivation

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-005

Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-006

Decision_Title: Validated Configuration Rollback Procedure Across All Nodes

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-007

Decision_Title: Automated Chaos and Sanity Tests Across All Nodes Before Production Routing

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-008

Decision_Title: Execution Algorithm Disconnection on Consolidated Tape Latency Breach

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-009

Decision_Title: Buy-Side Order Book Depth Monitoring with Market Order Halt

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-010

Decision_Title: Capital Buffer Requirement for Retroactive Exchange Trade Cancellation

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-011

Decision_Title: SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Force power-off during write; disconnect S3 network upload stream.

Promotion_Criteria: Database automatically recovers using Litestream WAL with zero transaction loss.

Rejection_Criteria: Unrecoverable database corruption; recovery process takes > 10 seconds.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Litestream replication delay metrics exceed 60 seconds; database file locks.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: High

---

Candidate_ID: REL-012

Decision_Title: Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-013

Decision_Title: Automated OAuth Token Refresh Without Manual Two-Factor Authentication

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-014

Decision_Title: Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

Candidate_ID: REL-015

Decision_Title: DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load

Required_Validation_Levels: Level 1: Research_Validation, Level 2: LoadTesting, Level 3: ChaosTesting, Level 4: Production_Validation

Validation_Methods: Force power-off during write; disconnect S3 network upload stream.

Promotion_Criteria: Database automatically recovers using Litestream WAL with zero transaction loss.

Rejection_Criteria: Unrecoverable database corruption; recovery process takes > 10 seconds.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: Litestream replication delay metrics exceed 60 seconds; database file locks.

Revalidation_Triggers: dependency_upgrade, database_upgrade, deployment_change, storage_change

Validation_Confidence: High

---

Candidate_ID: REL-016

Decision_Title: API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events

Required_Validation_Levels: Level 1: Research_Validation, Level 2: Staging, Level 3: Production_Validation

Validation_Methods: PagerDuty escalation rule simulation; check configuration drift across nodes.

Promotion_Criteria: All critical alerts correctly page on-call within 30 seconds; 0% configuration drift.

Rejection_Criteria: Alert silenced due to fatigue; incorrect binary deployed without hash mismatch warning.

Evidence_Threshold: evidence_strength >= High

Confidence_Threshold: minimum_30_days, no_unexplained_failures

Failure_Conditions: On-call response SLA exceeded; uncoordinated deploy mismatch detected.

Revalidation_Triggers: dependency_upgrade, deployment_change

Validation_Confidence: High

---

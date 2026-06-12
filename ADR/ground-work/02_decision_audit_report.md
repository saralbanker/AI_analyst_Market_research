# Decision Audit Report

**Phase:** 2 — Governance Audit (Risk & Reliability Stress-Test)
**Status:** Complete — All Candidates Audited
**Total Candidates Audited:** 120 (DG: 26 | VAL: 22 | RC: 18 | HO: 10 | INF: 16 | AIB: 12 | REL: 16)
**Date:** 2026-06-03

---

Candidate_ID: DG-001

Decision_Title: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Vector databases are actively contradicted by §6 and §19 because 95% of trading data is structured time-series (OHLCV).

Hidden_Assumptions: Walk-forward OOS data accurately mimics future market regimes (§9 A5).

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-002

Decision_Title: SQLite Exclusion from Standalone Time-Series Aggregation

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: SQLite standalone usage is contradicted by §7 Finding 24 which flags it as computationally inadequate for time-series aggregations due to row-oriented engine.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-003

Decision_Title: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-004

Decision_Title: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Zerodha is disqualified as sole backtesting source by §7 Finding 2 due to dropped candles and structural incompleteness.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-005

Decision_Title: Corporate Actions — Mandatory Split-Adjusted Data Requirement

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-006

Decision_Title: Provider Selection — Upstox Uplink for Historical Split-Adjusted Data

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: DG-007

Decision_Title: Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-008

Decision_Title: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: None identified in corpus.

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-009

Decision_Title: Production Binary Hygiene — Deprecated Code Removal Requirement

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-010

Decision_Title: Yahoo Finance Adjusted Close Mis-Adjustment Risk

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: DG-011

Decision_Title: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Walk-forward OOS data accurately mimics future market regimes (§9 A5).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-012

Decision_Title: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: Dropped packets during volatile periods misread as zero-volume.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-013

Decision_Title: Survivorship Bias — Delisted Stock Inclusion Requirement

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Delisted stocks are not necessary for a valid backtest (§9 A23).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: DG-014

Decision_Title: NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Missing_Evidence: Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13).

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: DG-015

Decision_Title: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Local hardware crash during high-volume writes causing database corruption.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: DG-016

Decision_Title: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Contradiction between autoencoder anomaly classifications (noise vs. structural shift, §9 A20) and risk systems visibility (§10 M12).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: Pipeline cron jobs overlap and deadlock if latency spikes.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-017

Decision_Title: Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: DG-018

Decision_Title: Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: Dropped packets during volatile periods misread as zero-volume.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: DG-019

Decision_Title: Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Exchanges (NSE/BSE) will not retroactively erase or cancel valid trades during a clearing member default (§9 A1).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Clearinghouse retroactively voiding trade legs during member default leaves system unhedged.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: DG-020

Decision_Title: SQLite WAL Transaction Integrity on NSE Trade Void Events

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-04: Slippage threshold quantification — no limit defined.

Audit_Confidence: LOW

---

Candidate_ID: DG-021

Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: LLMs writing dynamic SQL queries via MCP against DuckDB is contradicted by §8 Finding 13 (extreme hallucination/OOM risk).

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: DG-022

Decision_Title: LLM Context Window Degradation on Raw HTML NSE/SEC Filings

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: Local SLM capabilities are contradicted by §8 Finding 25 which flags context degradation when processing raw HTML filings.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: DG-023

Decision_Title: Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — entirely absent.

Audit_Confidence: LOW

---

Candidate_ID: DG-024

Decision_Title: Missing Research — VaR Modeling Under Non-Ergodic Market Conditions

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: Mathematical framework for VaR under non-ergodic conditions (§13).

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-02: Non-ergodic VaR mathematical framework — missing research.

Audit_Confidence: LOW

---

Candidate_ID: DG-025

Decision_Title: Missing Research — Multi-Broker Aggregate Margin Exposure Management

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-05: VIX threshold for variation margin — unquantified.

Audit_Confidence: LOW

---

Candidate_ID: DG-026

Decision_Title: Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).

Missing_Evidence: No empirical benchmarks provided in corpus.

Contradictions: None identified in corpus.

Governance_Risks: Regulatory compliance breach or data validation failure risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: VAL-001

Decision_Title: Walk-Forward Cross-Validation Over Randomized k-Fold CV

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-002

Decision_Title: Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-003

Decision_Title: Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Audit_Confidence: MEDIUM

---

Candidate_ID: VAL-004

Decision_Title: Cluster-Wide Binary Hash Verification Before Live Routing

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-005

Decision_Title: Audit All Configuration Flags for Deprecated Memory Address Reuse

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-006

Decision_Title: Hard-Coded Parent-Order Balance Checks in Execution Loops

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-007

Decision_Title: Automated Sanity and Chaos Tests Across All Nodes Before Production Routing

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-008

Decision_Title: Population Stability Index (PSI) Tracking for Concept Drift Detection

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: ML models anchoring to peak transaction values during sudden market downturns causes catastrophic capital drawdowns.

Research_Gaps: GAP-03: ML concept drift controls — no §11 Req paired.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-009

Decision_Title: Automatic Bid Size Reduction Under High Quantile Uncertainty

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: VAL-010

Decision_Title: Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-011

Decision_Title: Consolidated Tape Latency Threshold Disconnect

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Data feed latency spike triggers false signals or runaway loops.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-012

Decision_Title: Order Book Depth Monitoring with Market Order Halt on Evaporation

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-013

Decision_Title: Minimum 90% Branch Coverage in Backtesting Modules

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-014

Decision_Title: Intraday Minute Feed Completeness Verification (No Dropped Candles)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Dropped packets during volatile periods misread as zero-volume.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-015

Decision_Title: Cross-Verification of OHLCV Metrics Between Two Independent Data Providers

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Walk-forward OOS data accurately mimics future market regimes (§9 A5).

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-016

Decision_Title: Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban)

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: VAL-017

Decision_Title: SQLite WAL S3 Replication Recovery Under Hard Power-Off

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Local hardware crash during high-volume writes causing database corruption.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: VAL-018

Decision_Title: Synthetic Anomaly Injection Into Parquet Ingestion Pipeline

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: Contradiction between autoencoder anomaly classifications (noise vs. structural shift, §9 A20) and risk systems visibility (§10 M12).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Pipeline cron jobs overlap and deadlock if latency spikes.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-019

Decision_Title: FastMCP Execution Boundary Validation Against Prompt Injection

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Audit_Confidence: HIGH

---

Candidate_ID: VAL-020

Decision_Title: Walk-Forward OOS Regime Fidelity — Unvalidated Assumption

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: ML models anchoring to peak transaction values during sudden market downturns causes catastrophic capital drawdowns.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: VAL-021

Decision_Title: Cron Job Overlap and Deadlock Risk Under API Latency Spikes

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Pipeline cron jobs overlap and deadlock if latency spikes.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.

Audit_Confidence: MEDIUM

---

Candidate_ID: VAL-022

Decision_Title: Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift)

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Testing sandbox environment matches production routing behavior.

Missing_Evidence: Quantitative statistical limits or test validation results are absent from corpus.

Contradictions: Contradiction between autoencoder anomaly classifications (noise vs. structural shift, §9 A20) and risk systems visibility (§10 M12).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: RC-001

Decision_Title: Hard Position Limit Enforcement via API Disconnection

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: Data feed latency spike triggers false signals or runaway loops.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-002

Decision_Title: Circuit Breaker for Trend-Following Dynamic Hedging Cycles

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-003

Decision_Title: Informational Cascade Volume Spike Halt

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-004

Decision_Title: Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-05: VIX threshold for variation margin — unquantified.

Audit_Confidence: HIGH

---

Candidate_ID: RC-005

Decision_Title: Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13).

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-10: Multi-broker aggregate margin exposure management — missing research.

Audit_Confidence: HIGH

---

Candidate_ID: RC-006

Decision_Title: Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-007

Decision_Title: Variation Margin Release Restriction During Elevated Volatility

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Mathematical framework for VaR under non-ergodic conditions (§13).

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-02: Non-ergodic VaR mathematical framework — missing research.

Audit_Confidence: HIGH

---

Candidate_ID: RC-008

Decision_Title: Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Mathematical framework for VaR under non-ergodic conditions (§13).

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-009

Decision_Title: ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-010

Decision_Title: ML Concept Drift Controls — Regime-Change Re-Anchoring

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: ML models anchoring to peak transaction values during sudden market downturns causes catastrophic capital drawdowns.

Research_Gaps: GAP-03: ML concept drift controls — no §11 Req paired.

Audit_Confidence: HIGH

---

Candidate_ID: RC-011

Decision_Title: High-Velocity Operational Deployment Risk — Systemic Control Requirement

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Audit_Confidence: HIGH

---

Candidate_ID: RC-012

Decision_Title: Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: RC-013

Decision_Title: Non-Ergodic VaR Methodology — Mathematical Framework Requirement

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Mathematical framework for VaR under non-ergodic conditions (§13).

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-02: Non-ergodic VaR mathematical framework — missing research.

Audit_Confidence: HIGH

---

Candidate_ID: RC-014

Decision_Title: Slippage and Transaction Cost Controls in Live Execution

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-04: Slippage threshold quantification — no limit defined.

Audit_Confidence: HIGH

---

Candidate_ID: RC-015

Decision_Title: Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: Contradiction between autoencoder anomaly classifications (noise vs. structural shift, §9 A20) and risk systems visibility (§10 M12).

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: RC-016

Decision_Title: Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Passive rubber-stamp email approvals failing to prevent concentrated exposure.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-06: Active risk committee governance standard — no §11 Req.

Audit_Confidence: MEDIUM

---

Candidate_ID: RC-017

Decision_Title: Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Slippage threshold and margin scaling curves are missing.

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-05: VIX threshold for variation margin — unquantified.

Audit_Confidence: HIGH

---

Candidate_ID: RC-018

Decision_Title: Multi-Broker Simultaneous Collateral Fire Sale Prevention

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Historical correlation matrices remain stable during volatile periods.

Missing_Evidence: Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13).

Contradictions: None identified in corpus.

Governance_Risks: Uncontrolled leverage accumulation or concentration limit breach.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-10: Multi-broker aggregate margin exposure management — missing research.

Audit_Confidence: HIGH

---

Candidate_ID: HO-001

Decision_Title: Prohibition of LLM Direct Trade Execution

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: HO-002

Decision_Title: Physical FastMCP Execution Boundary Enforcement

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: None identified in corpus.

Governance_Risks: Lack of human gating during anomalous market events.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Audit_Confidence: HIGH

---

Candidate_ID: HO-003

Decision_Title: Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Multi-sig approval implementation details (roles, TTL) are missing.

Contradictions: None identified in corpus.

Governance_Risks: Bypassing human approval overrides or lack of defined signatories (roles, TTL) leading to unauthorized trading limits.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: HO-004

Decision_Title: Human-in-the-Loop Gate for AI-Influenced Pricing Decisions

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Multi-sig approval implementation details (roles, TTL) are missing.

Contradictions: None identified in corpus.

Governance_Risks: Lack of human gating during anomalous market events.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: HO-005

Decision_Title: Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: HO-006

Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Multi-sig approval implementation details (roles, TTL) are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operators silencing critical alert channels leading to unmitigated operational failures.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: HO-007

Decision_Title: Active Risk Committee Governance (Anti-Rubber-Stamp Requirement)

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Multi-sig approval implementation details (roles, TTL) are missing.

Contradictions: None identified in corpus.

Governance_Risks: Passive rubber-stamp email approvals failing to prevent concentrated exposure.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-06: Active risk committee governance standard — no §11 Req.

Audit_Confidence: MEDIUM

---

Candidate_ID: HO-008

Decision_Title: Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: HO-009

Decision_Title: Quantile Regression Uncertainty Band Human Review Requirement

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Missing_Evidence: Multi-sig approval implementation details (roles, TTL) are missing.

Contradictions: None identified in corpus.

Governance_Risks: Lack of human gating during anomalous market events.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: HO-010

Decision_Title: Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control)

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Operators will closely monitor dashboard displays and respond to critical alert runbooks without alert fatigue.

Missing_Evidence: Multi-sig approval implementation details (roles, TTL) are missing.

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: INF-001

Decision_Title: Embedded Zero-Copy Storage Architecture (DuckDB + SQLite)

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Vector databases are actively contradicted by §6 and §19 because 95% of trading data is structured time-series (OHLCV).

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-002

Decision_Title: Hive-Partitioned Parquet as Mandatory Market Data Storage Format

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-003

Decision_Title: SQLite WAL Management and S3 Replication Integrity

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-004

Decision_Title: Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Local SQLite WAL file grows infinitely and locks disk if S3 upload hangs.

Survivability_Risks: Local hardware crash during high-volume writes causing database corruption.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: INF-005

Decision_Title: Automated Binary Hash Verification Across All Production Clusters

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-006

Decision_Title: Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-007

Decision_Title: Coordinated Deployment Strategy to Prevent Partial Binary Rollout

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Audit_Confidence: HIGH

---

Candidate_ID: INF-008

Decision_Title: Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Precise cloud deployment topology (Docker/Kubernetes) needed when transitioning from Stage 2 (VM) to Stage 4 (SaaS) (§13, §14).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Audit_Confidence: LOW

---

Candidate_ID: INF-009

Decision_Title: Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: None identified in corpus.

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-010

Decision_Title: SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: None identified in corpus.

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-011

Decision_Title: OAuth Token Auto-Refresh Without Manual Two-Factor Authentication

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: OAuth tokens can be automatically refreshed without daily manual 2FA (§9 A22).

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: OAuth refresh failure locks trade execution daemon and stops system from sending orders.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: INF-012

Decision_Title: Data Pipeline Cron Job Overlap and Deadlock Prevention

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Pipeline cron jobs overlap and deadlock if latency spikes.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.

Audit_Confidence: MEDIUM

---

Candidate_ID: INF-013

Decision_Title: Execution Circuit Breaker on Consolidated Tape Latency Breach

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Data feed latency spike triggers false signals or runaway loops.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: INF-014

Decision_Title: FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Audit_Confidence: MEDIUM

---

Candidate_ID: INF-015

Decision_Title: Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: Event loop latency logs under live-load are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Dropped packets during volatile periods misread as zero-volume.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: INF-016

Decision_Title: DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: AIB-001

Decision_Title: Strict LLM Execution Prohibition via FastMCP

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-002

Decision_Title: AI Domain Segregation — Cognitive vs. Deterministic Execution

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-003

Decision_Title: Prohibition on Fully Autonomous AI Execution Grids

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-004

Decision_Title: Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-005

Decision_Title: Model Uncertainty Integration — AI Output as Execution Halt Trigger

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).

Missing_Evidence: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-006

Decision_Title: AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Missing_Evidence: Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-11: FinBERT score to Kelly fraction conversion math — unresolved.

Audit_Confidence: MEDIUM

---

Candidate_ID: AIB-007

Decision_Title: LLM Prohibition on Deterministic Chronological Sorting and Binary Math

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: Direct AI execution is actively contradicted by §16 (AI Direct Execution Safety = 10/100) due to SEBI regulations and Knight Capital failures.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Contradictions: Active contradiction between Claim A (Fully AI systems may outperform rules in turbulence, §5) and Claim B (Execution must remain strictly deterministic and human-gated, §5).

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-008

Decision_Title: Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Delisted stocks are not necessary for a valid backtest (§9 A23).

Missing_Evidence: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Contradictions: None identified in corpus.

Governance_Risks: Direct AI order routing violating SEBI regulatory compliance and deterministic gates.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: AIB-009

Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: LLMs writing dynamic SQL queries via MCP against DuckDB is contradicted by §8 Finding 13 (extreme hallucination/OOM risk).

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: AIB-010

Decision_Title: LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Hallucination rates and prompt-injection vulnerability benchmarks are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: AIB-011

Decision_Title: Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: Local SLM capabilities are contradicted by §8 Finding 25 which flags context degradation when processing raw HTML filings.

Hidden_Assumptions: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: None identified in corpus.

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: AIB-012

Decision_Title: Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Frontier models maintain stable response latency and deterministic tool definitions under stress.

Missing_Evidence: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.

Audit_Confidence: MEDIUM

---

Candidate_ID: REL-001

Decision_Title: Automated Binary Hash Verification Before Production Deployment

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.

Audit_Confidence: HIGH

---

Candidate_ID: REL-002

Decision_Title: Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Brokers allow sequential API polling without shadow-banning IPs (§9 A9); zero-volume candles in intraday feed mean no trades occurred, rather than dropped WebSocket packets (§9 A7).

Missing_Evidence: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).

Contradictions: None identified in corpus.

Governance_Risks: Non-compliance with SEBI rate limits (10 orders/sec) triggers broker-level account suspension and regulatory penalties.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: API rate violations trigger shadow IP bans that remain undetected by solo operators.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: REL-003

Decision_Title: Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: REL-004

Decision_Title: Deprecated Code Purge to Prevent Configuration Flag Reactivation

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: REL-005

Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operators silencing critical alert channels leading to unmitigated operational failures.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: REL-006

Decision_Title: Validated Configuration Rollback Procedure Across All Nodes

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: REL-007

Decision_Title: Automated Chaos and Sanity Tests Across All Nodes Before Production Routing

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: REL-008

Decision_Title: Execution Algorithm Disconnection on Consolidated Tape Latency Breach

Supporting_Evidence_Strength: STRONG

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Data feed latency spike triggers false signals or runaway loops.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: HIGH

---

Candidate_ID: REL-009

Decision_Title: Buy-Side Order Book Depth Monitoring with Market Order Halt

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: REL-010

Decision_Title: Capital Buffer Requirement for Retroactive Exchange Trade Cancellation

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Exchanges (NSE/BSE) will not retroactively erase or cancel valid trades during a clearing member default (§9 A1).

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Clearinghouse retroactively voiding trade legs during member default leaves system unhedged.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: REL-011

Decision_Title: SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: Litestream recovery millisecond-exact claim is weakly supported and contradicted by potential disk write failures (§8 Finding 18).

Hidden_Assumptions: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: REL-012

Decision_Title: Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: Pipeline cron jobs overlap and deadlock if latency spikes.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.

Audit_Confidence: LOW

---

Candidate_ID: REL-013

Decision_Title: Automated OAuth Token Refresh Without Manual Two-Factor Authentication

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: OAuth tokens can be automatically refreshed without daily manual 2FA (§9 A22).

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: OAuth refresh failure locks trade execution daemon and stops system from sending orders.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: LOW

---

Candidate_ID: REL-014

Decision_Title: Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops

Supporting_Evidence_Strength: MODERATE

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Detailed post-mortem metrics or API uptime logs are missing.

Contradictions: None identified in corpus.

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: None identified in corpus.

Audit_Confidence: MEDIUM

---

Candidate_ID: REL-015

Decision_Title: DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).

Contradictions: Litestream millisecond recovery guarantee (§8 F18) vs network dropouts crash risk (§9 A2).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: DuckDB database lock or event loop blocking under concurrent load.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — entirely absent.

Audit_Confidence: LOW

---

Candidate_ID: REL-016

Decision_Title: API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events

Supporting_Evidence_Strength: WEAK (Evidence_Weak)

Opposing_Evidence: None in corpus. General practitioner consensus supports this approach.

Hidden_Assumptions: Hardware failure rates follow standard bathtub curves and are predictable.

Missing_Evidence: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).

Contradictions: Upstox split adjusted claim (§7 F13) vs de-merger adjustment complexity (§8 F19).

Governance_Risks: Operational non-compliance risk.

Reliability_Risks: System execution failure or downtime risk.

Survivability_Risks: Capital destruction or strategy insolvency risk.

Research_Gaps: GAP-09: Third-party broker API uptime during extreme events — no empirical data.

Audit_Confidence: LOW

---

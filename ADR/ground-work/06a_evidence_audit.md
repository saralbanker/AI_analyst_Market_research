# 06a Evidence Audit

**Objective:** Verify evidence availability, traceability, and validity of mapping to decisions.

| ADR_ID | Title | Traceability Status | Support Level | Source Sections | Evidence Audit Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ADR-001 | Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) | Traceable | Fully Supported | Section 6, Section 19, Section 7 | Traceable to high-confidence audit section findings. |
| ADR-002 | SQLite Exclusion from Standalone Time-Series Aggregation | Traceable | Fully Supported | Section 7 | Traceable to high-confidence audit section findings. |
| ADR-003 | Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) | Traceable | Fully Supported | Section 19 | Traceable to high-confidence audit section findings. |
| ADR-004 | Provider Disqualification — Zerodha Historical API as Sole Backtesting Source | Traceable | Fully Supported | Section 7, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-005 | Corporate Actions — Mandatory Split-Adjusted Data Requirement | Traceable | Fully Supported | Section 7, Section 7 | Traceable to high-confidence audit section findings. |
| ADR-006 | Provider Selection — Upstox Uplink for Historical Split-Adjusted Data | Traceable | Fully Supported | Section 7, Section 8 | Traceable to high-confidence audit section findings. |
| ADR-007 | Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) | Traceable | Fully Supported | Section 7, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-008 | SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit | Traceable | Fully Supported | Section 7 | Traceable to high-confidence audit section findings. |
| ADR-009 | Production Binary Hygiene — Deprecated Code Removal Requirement | Traceable | Fully Supported | Section 7, Section 12 | Traceable to high-confidence audit section findings. |
| ADR-010 | Yahoo Finance Adjusted Close Mis-Adjustment Risk | Traceable | Partially Supported | Section 8 | Relies on weakly supported findings or low confidence metrics. |
| ADR-011 | Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers | Traceable | Fully Supported | Section 11, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-012 | Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) | Traceable | Fully Supported | Section 11, Section 23, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-013 | Survivorship Bias — Delisted Stock Inclusion Requirement | Traceable | Fully Supported | Section 9 | Traceable to high-confidence audit section findings. |
| ADR-014 | NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures | Traceable | Partially Supported | Section 9 | Relies on weakly supported findings or low confidence metrics. |
| ADR-015 | Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery | Traceable | Fully Supported | Section 9, Section 23, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-016 | Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion | Traceable | Fully Supported | Section 23, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-017 | Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops | Traceable | Fully Supported | Section 10 | Traceable to high-confidence audit section findings. |
| ADR-018 | Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment | Traceable | Fully Supported | Section 12 | Traceable to high-confidence audit section findings. |
| ADR-019 | Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy | Traceable | Fully Supported | Section 12, Section 9 | Traceable to high-confidence audit section findings. |
| ADR-020 | SQLite WAL Transaction Integrity on NSE Trade Void Events | Traceable | Partially Supported | Section 17 | Relies on weakly supported findings or low confidence metrics. |
| ADR-021 | LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk | Traceable | Partially Supported | Section 8 | Relies on weakly supported findings or low confidence metrics. |
| ADR-022 | LLM Context Window Degradation on Raw HTML NSE/SEC Filings | Traceable | Partially Supported | Section 8 | Relies on weakly supported findings or low confidence metrics. |
| ADR-023 | Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale | Traceable | Partially Supported | Section 22, Section 6 | Relies on weakly supported findings or low confidence metrics. |
| ADR-024 | Missing Research — VaR Modeling Under Non-Ergodic Market Conditions | Traceable | Partially Supported | Section 13 | Relies on weakly supported findings or low confidence metrics. |
| ADR-025 | Missing Research — Multi-Broker Aggregate Margin Exposure Management | Traceable | Partially Supported | Section 13 | Relies on weakly supported findings or low confidence metrics. |
| ADR-026 | Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals | Traceable | Partially Supported | Section 9 | Relies on weakly supported findings or low confidence metrics. |
| ADR-027 | Walk-Forward Cross-Validation Over Randomized k-Fold CV | Traceable | Fully Supported | Section 7, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-028 | Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) | Traceable | Fully Supported | Section 7, §8 | Traceable to high-confidence audit section findings. |
| ADR-029 | Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate | Traceable | Fully Supported | Section 8 | Traceable to high-confidence audit section findings. |
| ADR-030 | Cluster-Wide Binary Hash Verification Before Live Routing | Traceable | Fully Supported | Section 11, Section 7 | Traceable to high-confidence audit section findings. |
| ADR-031 | Audit All Configuration Flags for Deprecated Memory Address Reuse | Traceable | Fully Supported | Section 11, Section 7 | Traceable to high-confidence audit section findings. |
| ADR-032 | Hard-Coded Parent-Order Balance Checks in Execution Loops | Traceable | Fully Supported | Section 11, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-033 | Automated Sanity and Chaos Tests Across All Nodes Before Production Routing | Traceable | Fully Supported | Section 11, Section 10, Section 23 | Traceable to high-confidence audit section findings. |
| ADR-034 | Population Stability Index (PSI) Tracking for Concept Drift Detection | Traceable | Fully Supported | Section 11, Section 9, Section 8 | Traceable to high-confidence audit section findings. |
| ADR-035 | Automatic Bid Size Reduction Under High Quantile Uncertainty | Traceable | Fully Supported | Section 11, Section 5 | Traceable to high-confidence audit section findings. |
| ADR-036 | Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) | Traceable | Fully Supported | Section 11, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-037 | Consolidated Tape Latency Threshold Disconnect | Traceable | Fully Supported | Section 11, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-038 | Order Book Depth Monitoring with Market Order Halt on Evaporation | Traceable | Fully Supported | Section 11, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-039 | Minimum 90% Branch Coverage in Backtesting Modules | Traceable | Fully Supported | Section 11 | Traceable to high-confidence audit section findings. |
| ADR-040 | Intraday Minute Feed Completeness Verification (No Dropped Candles) | Traceable | Fully Supported | Section 11, Section 23, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-041 | Cross-Verification of OHLCV Metrics Between Two Independent Data Providers | Traceable | Fully Supported | Section 11, Section 15 | Traceable to high-confidence audit section findings. |
| ADR-042 | Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) | Traceable | Fully Supported | Section 23, Section 9 | Traceable to high-confidence audit section findings. |
| ADR-043 | SQLite WAL S3 Replication Recovery Under Hard Power-Off | Traceable | Fully Supported | Section 23, Section 8 | Traceable to high-confidence audit section findings. |
| ADR-044 | Synthetic Anomaly Injection Into Parquet Ingestion Pipeline | Traceable | Fully Supported | Section 23, Section 9, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-045 | FastMCP Execution Boundary Validation Against Prompt Injection | Traceable | Fully Supported | Section 23, Section 5 | Traceable to high-confidence audit section findings. |
| ADR-046 | Walk-Forward OOS Regime Fidelity — Unvalidated Assumption | Traceable | Fully Supported | Section 9, Section 8 | Traceable to high-confidence audit section findings. |
| ADR-047 | Cron Job Overlap and Deadlock Risk Under API Latency Spikes | Traceable | Fully Supported | Section 9, Section 11, Section 23 | Traceable to high-confidence audit section findings. |
| ADR-048 | Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) | Traceable | Fully Supported | Section 9, Section 10, Section 23 | Traceable to high-confidence audit section findings. |
| ADR-049 | Hard Position Limit Enforcement via API Disconnection | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-050 | Circuit Breaker for Trend-Following Dynamic Hedging Cycles | Traceable | Fully Supported | Section 7, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-051 | Informational Cascade Volume Spike Halt | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-052 | Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity | Traceable | Fully Supported | Section 18, Section 9, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-053 | Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls | Traceable | Fully Supported | Section 7, Section 9, Section 10, Section 11, Section 12 | Traceable to high-confidence audit section findings. |
| ADR-054 | Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation | Traceable | Fully Supported | Section 9, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-055 | Variation Margin Release Restriction During Elevated Volatility | Traceable | Fully Supported | Section 9, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-056 | Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns | Traceable | Fully Supported | Section 7, Section 9, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-057 | ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands | Traceable | Fully Supported | Section 18, Section 12, Section 9, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-058 | ML Concept Drift Controls — Regime-Change Re-Anchoring | Traceable | Fully Supported | Section 7, Section 10, Section 16, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-059 | High-Velocity Operational Deployment Risk — Systemic Control Requirement | Traceable | Fully Supported | Section 16, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-060 | Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker | Traceable | Fully Supported | Section 7, Section 9, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-061 | Non-Ergodic VaR Methodology — Mathematical Framework Requirement | Traceable | Fully Supported | Section 13, Section 7, Section 9 | Traceable to high-confidence audit section findings. |
| ADR-062 | Slippage and Transaction Cost Controls in Live Execution | Traceable | Fully Supported | Section 7, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-063 | Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance | Traceable | Fully Supported | Section 9, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-064 | Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals | Traceable | Fully Supported | Section 10 | Traceable to high-confidence audit section findings. |
| ADR-065 | Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards | Traceable | Fully Supported | Section 11, Section 7, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-066 | Multi-Broker Simultaneous Collateral Fire Sale Prevention | Traceable | Fully Supported | Section 9, Section 10, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-067 | Prohibition of LLM Direct Trade Execution | Traceable | Fully Supported | Section 16, Section 18, Section 20 | Traceable to high-confidence audit section findings. |
| ADR-068 | Physical FastMCP Execution Boundary Enforcement | Traceable | Fully Supported | Section 23, Section 18 | Traceable to high-confidence audit section findings. |
| ADR-069 | Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides | Traceable | Fully Supported | Section 11, Section 7, Section 10 | Traceable to high-confidence audit section findings. |
| ADR-070 | Human-in-the-Loop Gate for AI-Influenced Pricing Decisions | Traceable | Fully Supported | Section 7, Section 10, Section 5 | Traceable to high-confidence audit section findings. |
| ADR-071 | Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint) | Traceable | Fully Supported | Section 5, Section 20 | Traceable to high-confidence audit section findings. |
| ADR-072 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-073 | Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) | Traceable | Fully Supported | Section 10 | Traceable to high-confidence audit section findings. |
| ADR-074 | Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing | Traceable | Fully Supported | Section 20, Section 16, Section 7, Section 5 | Traceable to high-confidence audit section findings. |
| ADR-075 | Quantile Regression Uncertainty Band Human Review Requirement | Traceable | Partially Supported | Section 9 | Relies on weakly supported findings or low confidence metrics. |
| ADR-076 | Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) | Traceable | Fully Supported | Section 10, Section 7 | Traceable to high-confidence audit section findings. |
| ADR-077 | Embedded Zero-Copy Storage Architecture (DuckDB + SQLite) | Traceable | Fully Supported | Section 6, Section 19, Section 7 | Traceable to high-confidence audit section findings. |
| ADR-078 | Hive-Partitioned Parquet as Mandatory Market Data Storage Format | Traceable | Fully Supported | Section 19, Section 6 | Traceable to high-confidence audit section findings. |
| ADR-079 | SQLite WAL Management and S3 Replication Integrity | Traceable | Fully Supported | Section 9, Section 17, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-080 | Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery | Traceable | Fully Supported | Section 9, Section 23 | Traceable to high-confidence audit section findings. |
| ADR-081 | Automated Binary Hash Verification Across All Production Clusters | Traceable | Fully Supported | Section 7, Section 11, Section 18 | Traceable to high-confidence audit section findings. |
| ADR-082 | Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation | Traceable | Fully Supported | Section 7, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-083 | Coordinated Deployment Strategy to Prevent Partial Binary Rollout | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-084 | Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition | Traceable | Partially Supported | Section 13, Section 14 | Relies on weakly supported findings or low confidence metrics. |
| ADR-085 | Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors | Traceable | Fully Supported | Section 19, Section 23, Section 14 | Traceable to high-confidence audit section findings. |
| ADR-086 | SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance | Traceable | Fully Supported | Section 7, Section 22 | Traceable to high-confidence audit section findings. |
| ADR-087 | OAuth Token Auto-Refresh Without Manual Two-Factor Authentication | Traceable | Partially Supported | Section 9 | Relies on weakly supported findings or low confidence metrics. |
| ADR-088 | Data Pipeline Cron Job Overlap and Deadlock Prevention | Traceable | Fully Supported | Section 9 | Traceable to high-confidence audit section findings. |
| ADR-089 | Execution Circuit Breaker on Consolidated Tape Latency Breach | Traceable | Fully Supported | Section 11, Section 10, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-090 | FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries | Traceable | Fully Supported | Section 7, Section 14 | Traceable to high-confidence audit section findings. |
| ADR-091 | Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events | Traceable | Fully Supported | Section 21, Section 22 | Traceable to high-confidence audit section findings. |
| ADR-092 | DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load | Traceable | Fully Supported | Section 6, Section 22 | Traceable to high-confidence audit section findings. |
| ADR-093 | Strict LLM Execution Prohibition via FastMCP | Traceable | Fully Supported | Section 18, Section 5, Section 16, Section 20 | Traceable to high-confidence audit section findings. |
| ADR-094 | AI Domain Segregation — Cognitive vs. Deterministic Execution | Traceable | Fully Supported | Section 1, Section 4, Section 20 | Traceable to high-confidence audit section findings. |
| ADR-095 | Prohibition on Fully Autonomous AI Execution Grids | Traceable | Fully Supported | Section 8, Section 20, Section 4 | Traceable to high-confidence audit section findings. |
| ADR-096 | Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing | Traceable | Fully Supported | Section 7, Section 10, Section 11, Section 5 | Traceable to high-confidence audit section findings. |
| ADR-097 | Model Uncertainty Integration — AI Output as Execution Halt Trigger | Traceable | Fully Supported | Section 18, Section 12, Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-098 | AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math | Traceable | Fully Supported | Section 13, Section 5, Section 3 | Traceable to high-confidence audit section findings. |
| ADR-099 | LLM Prohibition on Deterministic Chronological Sorting and Binary Math | Traceable | Fully Supported | Section 7 | Traceable to high-confidence audit section findings. |
| ADR-100 | Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk | Traceable | Fully Supported | Section 7, Section 20, Section 8 | Traceable to high-confidence audit section findings. |
| ADR-101 | LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary | Traceable | Fully Supported | Section 8 | Traceable to high-confidence audit section findings. |
| ADR-102 | LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM | Traceable | Fully Supported | Section 19, Section 8 | Traceable to high-confidence audit section findings. |
| ADR-103 | Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary | Traceable | Partially Supported | Section 8, Section 9 | Relies on weakly supported findings or low confidence metrics. |
| ADR-104 | Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification | Traceable | Fully Supported | Section 23, Section 22, Section 21, Section 18 | Traceable to high-confidence audit section findings. |
| ADR-105 | Automated Binary Hash Verification Before Production Deployment | Traceable | Fully Supported | Section 7, Section 10, Section 11, Section 15, Section 16, Section 18 | Traceable to high-confidence audit section findings. |
| ADR-106 | Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors | Traceable | Fully Supported | Section 19, Section 9, Section 23 | Traceable to high-confidence audit section findings. |
| ADR-107 | Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-108 | Deprecated Code Purge to Prevent Configuration Flag Reactivation | Traceable | Fully Supported | Section 7, Section 9, Section 10, Section 11, Section 12 | Traceable to high-confidence audit section findings. |
| ADR-109 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-110 | Validated Configuration Rollback Procedure Across All Nodes | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-111 | Automated Chaos and Sanity Tests Across All Nodes Before Production Routing | Traceable | Fully Supported | Section 11 | Traceable to high-confidence audit section findings. |
| ADR-112 | Execution Algorithm Disconnection on Consolidated Tape Latency Breach | Traceable | Fully Supported | Section 7, Section 10, Section 11, Section 12, Section 16, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-113 | Buy-Side Order Book Depth Monitoring with Market Order Halt | Traceable | Fully Supported | Section 10, Section 11 | Traceable to high-confidence audit section findings. |
| ADR-114 | Capital Buffer Requirement for Retroactive Exchange Trade Cancellation | Traceable | Fully Supported | Section 9, Section 10, Section 11, Section 12, Section 17 | Traceable to high-confidence audit section findings. |
| ADR-115 | SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure | Traceable | Partially Supported | Section 8, Section 9, Section 21, Section 23 | Relies on weakly supported findings or low confidence metrics. |
| ADR-116 | Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks | Traceable | Partially Supported | Section 9 | Relies on weakly supported findings or low confidence metrics. |
| ADR-117 | Automated OAuth Token Refresh Without Manual Two-Factor Authentication | Traceable | Partially Supported | Section 9, Section 7 | Relies on weakly supported findings or low confidence metrics. |
| ADR-118 | Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops | Traceable | Fully Supported | Section 10, Section 21 | Traceable to high-confidence audit section findings. |
| ADR-119 | DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load | Traceable | Partially Supported | Section 22, Section 6, Section 14 | Relies on weakly supported findings or low confidence metrics. |
| ADR-120 | API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events | Traceable | Partially Supported | Section 8, Section 15, Section 22 | Relies on weakly supported findings or low confidence metrics. |
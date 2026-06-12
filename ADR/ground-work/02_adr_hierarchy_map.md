# 02 ADR Hierarchy Map

**Objective:** Map root, dependent, derived, and consequence relationships for all 120 ADRs.

| ADR_ID | Title | Category | Hierarchy Type | Parent / Dependent ADRs | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ADR-001 | Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) | Data Governance | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-002 | SQLite Exclusion from Standalone Time-Series Aggregation | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-003 | Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) | Data Governance | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-004 | Provider Disqualification — Zerodha Historical API as Sole Backtesting Source | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-005 | Corporate Actions — Mandatory Split-Adjusted Data Requirement | Data Governance | DEPENDENT_ADR | ADR-006 | Depends on Upstox API provider selection (ADR-006). |
| ADR-006 | Provider Selection — Upstox Uplink for Historical Split-Adjusted Data | Data Governance | DEPENDENT_ADR | ADR-006 | Depends on Upstox API provider selection (ADR-006). |
| ADR-007 | Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-008 | SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit | Data Governance | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-009 | Production Binary Hygiene — Deprecated Code Removal Requirement | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-010 | Yahoo Finance Adjusted Close Mis-Adjustment Risk | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-011 | Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-012 | Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-013 | Survivorship Bias — Delisted Stock Inclusion Requirement | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-014 | NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-015 | Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-016 | Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion | Data Governance | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-017 | Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-018 | Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-019 | Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-020 | SQLite WAL Transaction Integrity on NSE Trade Void Events | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-021 | LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-022 | LLM Context Window Degradation on Raw HTML NSE/SEC Filings | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-023 | Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale | Data Governance | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-024 | Missing Research — VaR Modeling Under Non-Ergodic Market Conditions | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-025 | Missing Research — Multi-Broker Aggregate Margin Exposure Management | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-026 | Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals | Data Governance | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-027 | Walk-Forward Cross-Validation Over Randomized k-Fold CV | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-028 | Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-029 | Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-030 | Cluster-Wide Binary Hash Verification Before Live Routing | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-031 | Audit All Configuration Flags for Deprecated Memory Address Reuse | Validation | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-032 | Hard-Coded Parent-Order Balance Checks in Execution Loops | Validation | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-033 | Automated Sanity and Chaos Tests Across All Nodes Before Production Routing | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-034 | Population Stability Index (PSI) Tracking for Concept Drift Detection | Validation | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-035 | Automatic Bid Size Reduction Under High Quantile Uncertainty | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-036 | Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-037 | Consolidated Tape Latency Threshold Disconnect | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-038 | Order Book Depth Monitoring with Market Order Halt on Evaporation | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-039 | Minimum 90% Branch Coverage in Backtesting Modules | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-040 | Intraday Minute Feed Completeness Verification (No Dropped Candles) | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-041 | Cross-Verification of OHLCV Metrics Between Two Independent Data Providers | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-042 | Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) | Validation | CONSEQUENCE_ADR | ADR-008 | Consequence of SEBI 10 orders/sec rate limit enforcement (ADR-008). |
| ADR-043 | SQLite WAL S3 Replication Recovery Under Hard Power-Off | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-044 | Synthetic Anomaly Injection Into Parquet Ingestion Pipeline | Validation | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-045 | FastMCP Execution Boundary Validation Against Prompt Injection | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-046 | Walk-Forward OOS Regime Fidelity — Unvalidated Assumption | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-047 | Cron Job Overlap and Deadlock Risk Under API Latency Spikes | Validation | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-048 | Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) | Validation | DEPENDENT_ADR | ADR-011 | Depends on cross-verification requirements (ADR-011). |
| ADR-049 | Hard Position Limit Enforcement via API Disconnection | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-050 | Circuit Breaker for Trend-Following Dynamic Hedging Cycles | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-051 | Informational Cascade Volume Spike Halt | Risk Control | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-052 | Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-053 | Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-054 | Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation | Risk Control | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-055 | Variation Margin Release Restriction During Elevated Volatility | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-056 | Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-057 | ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-058 | ML Concept Drift Controls — Regime-Change Re-Anchoring | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-059 | High-Velocity Operational Deployment Risk — Systemic Control Requirement | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-060 | Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-061 | Non-Ergodic VaR Methodology — Mathematical Framework Requirement | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-062 | Slippage and Transaction Cost Controls in Live Execution | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-063 | Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance | Risk Control | DEPENDENT_ADR | ADR-011 | Depends on cross-verification requirements (ADR-011). |
| ADR-064 | Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-065 | Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-066 | Multi-Broker Simultaneous Collateral Fire Sale Prevention | Risk Control | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-067 | Prohibition of LLM Direct Trade Execution | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-068 | Physical FastMCP Execution Boundary Enforcement | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-069 | Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-070 | Human-in-the-Loop Gate for AI-Influenced Pricing Decisions | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-071 | Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint) | Human Oversight | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-072 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Human Oversight | DERIVED_ADR | ADR-072 | Logical extension of human oversight fatigue management. |
| ADR-073 | Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-074 | Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-075 | Quantile Regression Uncertainty Band Human Review Requirement | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-076 | Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) | Human Oversight | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-077 | Embedded Zero-Copy Storage Architecture (DuckDB + SQLite) | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-078 | Hive-Partitioned Parquet as Mandatory Market Data Storage Format | Infrastructure | ROOT_ADR | None | Foundational architectural constraint that remains necessary if other decisions are removed. |
| ADR-079 | SQLite WAL Management and S3 Replication Integrity | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-080 | Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-081 | Automated Binary Hash Verification Across All Production Clusters | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-082 | Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-083 | Coordinated Deployment Strategy to Prevent Partial Binary Rollout | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-084 | Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-085 | Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors | Infrastructure | CONSEQUENCE_ADR | ADR-008 | Consequence of SEBI 10 orders/sec rate limit enforcement (ADR-008). |
| ADR-086 | SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance | Infrastructure | CONSEQUENCE_ADR | ADR-008 | Consequence of SEBI 10 orders/sec rate limit enforcement (ADR-008). |
| ADR-087 | OAuth Token Auto-Refresh Without Manual Two-Factor Authentication | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-088 | Data Pipeline Cron Job Overlap and Deadlock Prevention | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-089 | Execution Circuit Breaker on Consolidated Tape Latency Breach | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-090 | FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-091 | Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events | Infrastructure | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-092 | DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load | Infrastructure | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-093 | Strict LLM Execution Prohibition via FastMCP | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-094 | AI Domain Segregation — Cognitive vs. Deterministic Execution | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-095 | Prohibition on Fully Autonomous AI Execution Grids | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-096 | Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-097 | Model Uncertainty Integration — AI Output as Execution Halt Trigger | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-098 | AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-099 | LLM Prohibition on Deterministic Chronological Sorting and Binary Math | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-100 | Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-101 | LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-102 | LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-103 | Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-104 | Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification | AI Boundary | DEPENDENT_ADR | ADR-001 | Dependent on core database storage selection. |
| ADR-105 | Automated Binary Hash Verification Before Production Deployment | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-106 | Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors | Reliability | CONSEQUENCE_ADR | ADR-008 | Consequence of SEBI 10 orders/sec rate limit enforcement (ADR-008). |
| ADR-107 | Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-108 | Deprecated Code Purge to Prevent Configuration Flag Reactivation | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-109 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Reliability | DERIVED_ADR | ADR-072 | Logical extension of human oversight fatigue management. |
| ADR-110 | Validated Configuration Rollback Procedure Across All Nodes | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-111 | Automated Chaos and Sanity Tests Across All Nodes Before Production Routing | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-112 | Execution Algorithm Disconnection on Consolidated Tape Latency Breach | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-113 | Buy-Side Order Book Depth Monitoring with Market Order Halt | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-114 | Capital Buffer Requirement for Retroactive Exchange Trade Cancellation | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-115 | SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-116 | Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-117 | Automated OAuth Token Refresh Without Manual Two-Factor Authentication | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-118 | Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
| ADR-119 | DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load | Reliability | DEPENDENT_ADR | ADR-001 | Depends on embedded database zero-copy selection (ADR-001). |
| ADR-120 | API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events | Reliability | CONSEQUENCE_ADR | ADR-031 | Consequence of core risk limits or controls. |
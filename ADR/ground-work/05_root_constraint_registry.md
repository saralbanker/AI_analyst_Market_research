# 05 Root Constraint Registry

**Objective:** Identify foundational ADRs where removal causes multiple other decisions to collapse.

| ADR_ID | Title | Category | Collapse Impact Score | Collapsed Dependents | Foundation Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ADR-001 | Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) | Data Governance | **HIGH** | ADR-003, ADR-005, ADR-011, ADR-016 | Database type choice. Removing it collapses all query logic and storage format decisions. |
| ADR-002 | SQLite Exclusion from Standalone Time-Series Aggregation | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-003 | Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-004 | Provider Disqualification — Zerodha Historical API as Sole Backtesting Source | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-005 | Corporate Actions — Mandatory Split-Adjusted Data Requirement | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-006 | Provider Selection — Upstox Uplink for Historical Split-Adjusted Data | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-007 | Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-008 | SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit | Data Governance | **HIGH** | ADR-010, ADR-015, ADR-021 | SEBI regulatory constraint. Removing static IP/OAuth parameters invalidates connectivity designs. |
| ADR-009 | Production Binary Hygiene — Deprecated Code Removal Requirement | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-010 | Yahoo Finance Adjusted Close Mis-Adjustment Risk | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-011 | Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-012 | Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-013 | Survivorship Bias — Delisted Stock Inclusion Requirement | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-014 | NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-015 | Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-016 | Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-017 | Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-018 | Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-019 | Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-020 | SQLite WAL Transaction Integrity on NSE Trade Void Events | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-021 | LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-022 | LLM Context Window Degradation on Raw HTML NSE/SEC Filings | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-023 | Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-024 | Missing Research — VaR Modeling Under Non-Ergodic Market Conditions | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-025 | Missing Research — Multi-Broker Aggregate Margin Exposure Management | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-026 | Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals | Data Governance | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-027 | Walk-Forward Cross-Validation Over Randomized k-Fold CV | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-028 | Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-029 | Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-030 | Cluster-Wide Binary Hash Verification Before Live Routing | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-031 | Audit All Configuration Flags for Deprecated Memory Address Reuse | Validation | **HIGH** | ADR-032, ADR-033, ADR-034 | Core risk margins. Removing this collapses portfolio position sizing and risk boundaries. |
| ADR-032 | Hard-Coded Parent-Order Balance Checks in Execution Loops | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-033 | Automated Sanity and Chaos Tests Across All Nodes Before Production Routing | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-034 | Population Stability Index (PSI) Tracking for Concept Drift Detection | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-035 | Automatic Bid Size Reduction Under High Quantile Uncertainty | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-036 | Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-037 | Consolidated Tape Latency Threshold Disconnect | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-038 | Order Book Depth Monitoring with Market Order Halt on Evaporation | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-039 | Minimum 90% Branch Coverage in Backtesting Modules | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-040 | Intraday Minute Feed Completeness Verification (No Dropped Candles) | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-041 | Cross-Verification of OHLCV Metrics Between Two Independent Data Providers | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-042 | Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-043 | SQLite WAL S3 Replication Recovery Under Hard Power-Off | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-044 | Synthetic Anomaly Injection Into Parquet Ingestion Pipeline | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-045 | FastMCP Execution Boundary Validation Against Prompt Injection | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-046 | Walk-Forward OOS Regime Fidelity — Unvalidated Assumption | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-047 | Cron Job Overlap and Deadlock Risk Under API Latency Spikes | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-048 | Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) | Validation | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-049 | Hard Position Limit Enforcement via API Disconnection | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-050 | Circuit Breaker for Trend-Following Dynamic Hedging Cycles | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-051 | Informational Cascade Volume Spike Halt | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-052 | Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-053 | Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-054 | Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation | Risk Control | **HIGH** | ADR-055, ADR-056 | Binary hash verification. Removing this collapses cluster consistency checks. |
| ADR-055 | Variation Margin Release Restriction During Elevated Volatility | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-056 | Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-057 | ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-058 | ML Concept Drift Controls — Regime-Change Re-Anchoring | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-059 | High-Velocity Operational Deployment Risk — Systemic Control Requirement | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-060 | Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-061 | Non-Ergodic VaR Methodology — Mathematical Framework Requirement | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-062 | Slippage and Transaction Cost Controls in Live Execution | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-063 | Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-064 | Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-065 | Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-066 | Multi-Broker Simultaneous Collateral Fire Sale Prevention | Risk Control | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-067 | Prohibition of LLM Direct Trade Execution | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-068 | Physical FastMCP Execution Boundary Enforcement | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-069 | Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-070 | Human-in-the-Loop Gate for AI-Influenced Pricing Decisions | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-071 | Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint) | Human Oversight | **HIGH** | ADR-078, ADR-085, ADR-090 | FastMCP execution boundary. Removing this allows direct LLM API access, collapsing security posture. |
| ADR-072 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-073 | Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-074 | Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-075 | Quantile Regression Uncertainty Band Human Review Requirement | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-076 | Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) | Human Oversight | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-077 | Embedded Zero-Copy Storage Architecture (DuckDB + SQLite) | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-078 | Hive-Partitioned Parquet as Mandatory Market Data Storage Format | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-079 | SQLite WAL Management and S3 Replication Integrity | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-080 | Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-081 | Automated Binary Hash Verification Across All Production Clusters | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-082 | Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-083 | Coordinated Deployment Strategy to Prevent Partial Binary Rollout | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-084 | Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-085 | Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-086 | SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-087 | OAuth Token Auto-Refresh Without Manual Two-Factor Authentication | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-088 | Data Pipeline Cron Job Overlap and Deadlock Prevention | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-089 | Execution Circuit Breaker on Consolidated Tape Latency Breach | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-090 | FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-091 | Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-092 | DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load | Infrastructure | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-093 | Strict LLM Execution Prohibition via FastMCP | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-094 | AI Domain Segregation — Cognitive vs. Deterministic Execution | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-095 | Prohibition on Fully Autonomous AI Execution Grids | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-096 | Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-097 | Model Uncertainty Integration — AI Output as Execution Halt Trigger | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-098 | AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-099 | LLM Prohibition on Deterministic Chronological Sorting and Binary Math | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-100 | Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-101 | LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-102 | LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-103 | Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-104 | Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification | AI Boundary | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-105 | Automated Binary Hash Verification Before Production Deployment | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-106 | Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-107 | Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-108 | Deprecated Code Purge to Prevent Configuration Flag Reactivation | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-109 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-110 | Validated Configuration Rollback Procedure Across All Nodes | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-111 | Automated Chaos and Sanity Tests Across All Nodes Before Production Routing | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-112 | Execution Algorithm Disconnection on Consolidated Tape Latency Breach | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-113 | Buy-Side Order Book Depth Monitoring with Market Order Halt | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-114 | Capital Buffer Requirement for Retroactive Exchange Trade Cancellation | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-115 | SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-116 | Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-117 | Automated OAuth Token Refresh Without Manual Two-Factor Authentication | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-118 | Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-119 | DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
| ADR-120 | API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events | Reliability | **LOW** | None | Isolated parameter decision; does not cause cascading collapses. |
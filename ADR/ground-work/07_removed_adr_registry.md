# 07 Removed ADR Registry

**Objective:** List ADRs excluded from the Architecture Core set (tooling, operational, implementation details).

| ADR_ID | Title | Category | Reason for Exclusion |
| :--- | :--- | :--- | :--- |
| ADR-005 | Corporate Actions — Mandatory Split-Adjusted Data Requirement | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-006 | Provider Selection — Upstox Uplink for Historical Split-Adjusted Data | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-007 | Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-009 | Production Binary Hygiene — Deprecated Code Removal Requirement | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-010 | Yahoo Finance Adjusted Close Mis-Adjustment Risk | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-013 | Survivorship Bias — Delisted Stock Inclusion Requirement | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-014 | NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-017 | Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-018 | Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-019 | Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-020 | SQLite WAL Transaction Integrity on NSE Trade Void Events | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-021 | LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-022 | LLM Context Window Degradation on Raw HTML NSE/SEC Filings | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-023 | Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-024 | Missing Research — VaR Modeling Under Non-Ergodic Market Conditions | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-025 | Missing Research — Multi-Broker Aggregate Margin Exposure Management | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-026 | Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals | Data Governance | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-027 | Walk-Forward Cross-Validation Over Randomized k-Fold CV | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-028 | Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-029 | Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-030 | Cluster-Wide Binary Hash Verification Before Live Routing | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-033 | Automated Sanity and Chaos Tests Across All Nodes Before Production Routing | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-035 | Automatic Bid Size Reduction Under High Quantile Uncertainty | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-036 | Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-037 | Consolidated Tape Latency Threshold Disconnect | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-038 | Order Book Depth Monitoring with Market Order Halt on Evaporation | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-039 | Minimum 90% Branch Coverage in Backtesting Modules | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-040 | Intraday Minute Feed Completeness Verification (No Dropped Candles) | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-041 | Cross-Verification of OHLCV Metrics Between Two Independent Data Providers | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-042 | Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-043 | SQLite WAL S3 Replication Recovery Under Hard Power-Off | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-044 | Synthetic Anomaly Injection Into Parquet Ingestion Pipeline | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-045 | FastMCP Execution Boundary Validation Against Prompt Injection | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-046 | Walk-Forward OOS Regime Fidelity — Unvalidated Assumption | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-047 | Cron Job Overlap and Deadlock Risk Under API Latency Spikes | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-048 | Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) | Validation | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-049 | Hard Position Limit Enforcement via API Disconnection | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-050 | Circuit Breaker for Trend-Following Dynamic Hedging Cycles | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-051 | Informational Cascade Volume Spike Halt | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-052 | Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-053 | Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-055 | Variation Margin Release Restriction During Elevated Volatility | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-056 | Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-057 | ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-058 | ML Concept Drift Controls — Regime-Change Re-Anchoring | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-059 | High-Velocity Operational Deployment Risk — Systemic Control Requirement | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-060 | Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-061 | Non-Ergodic VaR Methodology — Mathematical Framework Requirement | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-062 | Slippage and Transaction Cost Controls in Live Execution | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-063 | Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-064 | Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-065 | Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-066 | Multi-Broker Simultaneous Collateral Fire Sale Prevention | Risk Control | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-067 | Prohibition of LLM Direct Trade Execution | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-068 | Physical FastMCP Execution Boundary Enforcement | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-069 | Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-070 | Human-in-the-Loop Gate for AI-Influenced Pricing Decisions | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-074 | Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-075 | Quantile Regression Uncertainty Band Human Review Requirement | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-076 | Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) | Human Oversight | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-079 | SQLite WAL Management and S3 Replication Integrity | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-080 | Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-081 | Automated Binary Hash Verification Across All Production Clusters | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-082 | Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-083 | Coordinated Deployment Strategy to Prevent Partial Binary Rollout | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-084 | Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-085 | Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-086 | SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-087 | OAuth Token Auto-Refresh Without Manual Two-Factor Authentication | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-088 | Data Pipeline Cron Job Overlap and Deadlock Prevention | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-089 | Execution Circuit Breaker on Consolidated Tape Latency Breach | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-090 | FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-091 | Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-092 | DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load | Infrastructure | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-093 | Strict LLM Execution Prohibition via FastMCP | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-094 | AI Domain Segregation — Cognitive vs. Deterministic Execution | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-095 | Prohibition on Fully Autonomous AI Execution Grids | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-096 | Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-097 | Model Uncertainty Integration — AI Output as Execution Halt Trigger | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-098 | AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-099 | LLM Prohibition on Deterministic Chronological Sorting and Binary Math | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-100 | Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-101 | LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-102 | LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-103 | Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-104 | Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification | AI Boundary | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-105 | Automated Binary Hash Verification Before Production Deployment | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-106 | Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-107 | Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-108 | Deprecated Code Purge to Prevent Configuration Flag Reactivation | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-109 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-110 | Validated Configuration Rollback Procedure Across All Nodes | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-111 | Automated Chaos and Sanity Tests Across All Nodes Before Production Routing | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-112 | Execution Algorithm Disconnection on Consolidated Tape Latency Breach | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-113 | Buy-Side Order Book Depth Monitoring with Market Order Halt | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-114 | Capital Buffer Requirement for Retroactive Exchange Trade Cancellation | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-115 | SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-116 | Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-117 | Automated OAuth Token Refresh Without Manual Two-Factor Authentication | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-118 | Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-119 | DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
| ADR-120 | API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events | Reliability | Excluded implementation, operational monitor, or specific coding rule. |
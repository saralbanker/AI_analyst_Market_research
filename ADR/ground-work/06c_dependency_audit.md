# 06c Dependency Audit

**Objective:** Verify dependency chains, blockers, ordering correctness, and circular dependencies.

| ADR_ID | Title | Category | Dependencies / Related | Blocker Status | Circularity Check | Dependency Audit Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ADR-001 | Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) | Data Governance | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-002 | SQLite Exclusion from Standalone Time-Series Aggregation | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-003 | Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-004 | Provider Disqualification — Zerodha Historical API as Sole Backtesting Source | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-005 | Corporate Actions — Mandatory Split-Adjusted Data Requirement | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-006 | Provider Selection — Upstox Uplink for Historical Split-Adjusted Data | Data Governance | ADR-001 | Active Blocker | Clean (DAG) | Depends on structural components: ADR-001. Deferred status blocks execution implementation. |
| ADR-007 | Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-008 | SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-009 | Production Binary Hygiene — Deprecated Code Removal Requirement | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-010 | Yahoo Finance Adjusted Close Mis-Adjustment Risk | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-011 | Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-012 | Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-013 | Survivorship Bias — Delisted Stock Inclusion Requirement | Data Governance | ADR-001 | Active Blocker | Clean (DAG) | Depends on structural components: ADR-001. Deferred status blocks execution implementation. |
| ADR-014 | NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-015 | Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery | Data Governance | ADR-001 | Active Blocker | Clean (DAG) | Depends on structural components: ADR-001. Deferred status blocks execution implementation. |
| ADR-016 | Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-017 | Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-018 | Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment | Data Governance | ADR-001 | Active Blocker | Clean (DAG) | Depends on structural components: ADR-001. Deferred status blocks execution implementation. |
| ADR-019 | Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy | Data Governance | ADR-001 | Active Blocker | Clean (DAG) | Depends on structural components: ADR-001. Deferred status blocks execution implementation. |
| ADR-020 | SQLite WAL Transaction Integrity on NSE Trade Void Events | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-021 | LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-022 | LLM Context Window Degradation on Raw HTML NSE/SEC Filings | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-023 | Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-024 | Missing Research — VaR Modeling Under Non-Ergodic Market Conditions | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-025 | Missing Research — Multi-Broker Aggregate Margin Exposure Management | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-026 | Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals | Data Governance | ADR-001 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-001. |
| ADR-027 | Walk-Forward Cross-Validation Over Randomized k-Fold CV | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-028 | Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-029 | Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-030 | Cluster-Wide Binary Hash Verification Before Live Routing | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-031 | Audit All Configuration Flags for Deprecated Memory Address Reuse | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-032 | Hard-Coded Parent-Order Balance Checks in Execution Loops | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-033 | Automated Sanity and Chaos Tests Across All Nodes Before Production Routing | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-034 | Population Stability Index (PSI) Tracking for Concept Drift Detection | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-035 | Automatic Bid Size Reduction Under High Quantile Uncertainty | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-036 | Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-037 | Consolidated Tape Latency Threshold Disconnect | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-038 | Order Book Depth Monitoring with Market Order Halt on Evaporation | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-039 | Minimum 90% Branch Coverage in Backtesting Modules | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-040 | Intraday Minute Feed Completeness Verification (No Dropped Candles) | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-041 | Cross-Verification of OHLCV Metrics Between Two Independent Data Providers | Validation | ADR-004, ADR-006 | Clean Pathway | Clean (DAG) | Depends on structural components: ADR-004, ADR-006. |
| ADR-042 | Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-043 | SQLite WAL S3 Replication Recovery Under Hard Power-Off | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-044 | Synthetic Anomaly Injection Into Parquet Ingestion Pipeline | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-045 | FastMCP Execution Boundary Validation Against Prompt Injection | Validation | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-046 | Walk-Forward OOS Regime Fidelity — Unvalidated Assumption | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-047 | Cron Job Overlap and Deadlock Risk Under API Latency Spikes | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-048 | Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) | Validation | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-049 | Hard Position Limit Enforcement via API Disconnection | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-050 | Circuit Breaker for Trend-Following Dynamic Hedging Cycles | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-051 | Informational Cascade Volume Spike Halt | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-052 | Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-053 | Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-054 | Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-055 | Variation Margin Release Restriction During Elevated Volatility | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-056 | Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-057 | ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-058 | ML Concept Drift Controls — Regime-Change Re-Anchoring | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-059 | High-Velocity Operational Deployment Risk — Systemic Control Requirement | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-060 | Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-061 | Non-Ergodic VaR Methodology — Mathematical Framework Requirement | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-062 | Slippage and Transaction Cost Controls in Live Execution | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-063 | Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance | Risk Control | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-064 | Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals | Risk Control | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-065 | Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-066 | Multi-Broker Simultaneous Collateral Fire Sale Prevention | Risk Control | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-067 | Prohibition of LLM Direct Trade Execution | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-068 | Physical FastMCP Execution Boundary Enforcement | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-069 | Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-070 | Human-in-the-Loop Gate for AI-Influenced Pricing Decisions | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-071 | Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint) | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-072 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Human Oversight | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-073 | Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) | Human Oversight | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-074 | Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-075 | Quantile Regression Uncertainty Band Human Review Requirement | Human Oversight | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-076 | Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) | Human Oversight | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-077 | Embedded Zero-Copy Storage Architecture (DuckDB + SQLite) | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-078 | Hive-Partitioned Parquet as Mandatory Market Data Storage Format | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-079 | SQLite WAL Management and S3 Replication Integrity | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-080 | Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery | Infrastructure | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-081 | Automated Binary Hash Verification Across All Production Clusters | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-082 | Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-083 | Coordinated Deployment Strategy to Prevent Partial Binary Rollout | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-084 | Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-085 | Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-086 | SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-087 | OAuth Token Auto-Refresh Without Manual Two-Factor Authentication | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-088 | Data Pipeline Cron Job Overlap and Deadlock Prevention | Infrastructure | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-089 | Execution Circuit Breaker on Consolidated Tape Latency Breach | Infrastructure | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-090 | FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries | Infrastructure | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-091 | Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events | Infrastructure | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-092 | DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load | Infrastructure | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-093 | Strict LLM Execution Prohibition via FastMCP | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-094 | AI Domain Segregation — Cognitive vs. Deterministic Execution | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-095 | Prohibition on Fully Autonomous AI Execution Grids | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-096 | Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-097 | Model Uncertainty Integration — AI Output as Execution Halt Trigger | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-098 | AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math | AI Boundary | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-099 | LLM Prohibition on Deterministic Chronological Sorting and Binary Math | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-100 | Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-101 | LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary | AI Boundary | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-102 | LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM | AI Boundary | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-103 | Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary | AI Boundary | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-104 | Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification | AI Boundary | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-105 | Automated Binary Hash Verification Before Production Deployment | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-106 | Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-107 | Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-108 | Deprecated Code Purge to Prevent Configuration Flag Reactivation | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-109 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Reliability | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-110 | Validated Configuration Rollback Procedure Across All Nodes | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-111 | Automated Chaos and Sanity Tests Across All Nodes Before Production Routing | Reliability | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-112 | Execution Algorithm Disconnection on Consolidated Tape Latency Breach | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-113 | Buy-Side Order Book Depth Monitoring with Market Order Halt | Reliability | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-114 | Capital Buffer Requirement for Retroactive Exchange Trade Cancellation | Reliability | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-115 | SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-116 | Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-117 | Automated OAuth Token Refresh Without Manual Two-Factor Authentication | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-118 | Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops | Reliability | None | Active Blocker | Clean (DAG) | Correctly sequenced. Deferred status blocks execution implementation. |
| ADR-119 | DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
| ADR-120 | API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events | Reliability | None | Clean Pathway | Clean (DAG) | Correctly sequenced. |
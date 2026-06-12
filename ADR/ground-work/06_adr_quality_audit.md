# 06 ADR Quality Audit

**Objective:** Consolidate quality findings for all 120 ADRs, map trust levels, identify gaps, and assess architecture readiness.

## 1. ADR Trust Level Registry

| ADR_ID | Title | Decision Category | Trust Level | Evidence Strength | Missing Validation / Unknowns | Architecture Impact | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ADR-001 | Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) | Data Governance | **PROVISIONAL** | STRONG | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-002 | SQLite Exclusion from Standalone Time-Series Aggregation | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-003 | Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-004 | Provider Disqualification — Zerodha Historical API as Sole Backtesting Source | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-005 | Corporate Actions — Mandatory Split-Adjusted Data Requirement | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-006 | Provider Selection — Upstox Uplink for Historical Split-Adjusted Data | Data Governance | **PROVISIONAL** | MODERATE | Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22). | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-007 | Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-008 | SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit | Data Governance | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-009 | Production Binary Hygiene — Deprecated Code Removal Requirement | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-010 | Yahoo Finance Adjusted Close Mis-Adjustment Risk | Data Governance | **WEAK** | WEAK (Evidence_Weak) | No empirical benchmarks provided in corpus. | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-011 | Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-012 | Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-013 | Survivorship Bias — Delisted Stock Inclusion Requirement | Data Governance | **PROVISIONAL** | MODERATE | No empirical benchmarks provided in corpus. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-014 | NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures | Data Governance | **WEAK** | WEAK (Evidence_Weak) | Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13). | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-015 | Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery | Data Governance | **PROVISIONAL** | MODERATE | No empirical benchmarks provided in corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-016 | Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-017 | Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops | Data Governance | **PROVISIONAL** | STRONG | No empirical benchmarks provided in corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-018 | Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment | Data Governance | **PROVISIONAL** | MODERATE | No empirical benchmarks provided in corpus. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-019 | Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy | Data Governance | **PROVISIONAL** | MODERATE | No empirical benchmarks provided in corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-020 | SQLite WAL Transaction Integrity on NSE Trade Void Events | Data Governance | **WEAK** | WEAK (Evidence_Weak) | No empirical benchmarks provided in corpus. | Critical — Cascading failure path leads to capital destruction. | Weak supporting evidence or low audit confidence. |
| ADR-021 | LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk | Data Governance | **WEAK** | WEAK (Evidence_Weak) | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-022 | LLM Context Window Degradation on Raw HTML NSE/SEC Filings | Data Governance | **WEAK** | WEAK (Evidence_Weak) | No empirical benchmarks provided in corpus. | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-023 | Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale | Data Governance | **WEAK** | WEAK (Evidence_Weak) | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Critical — Cascading failure path leads to capital destruction. | Weak supporting evidence or low audit confidence. |
| ADR-024 | Missing Research — VaR Modeling Under Non-Ergodic Market Conditions | Data Governance | **WEAK** | WEAK (Evidence_Weak) | Mathematical framework for VaR under non-ergodic conditions (§13). | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-025 | Missing Research — Multi-Broker Aggregate Margin Exposure Management | Data Governance | **WEAK** | WEAK (Evidence_Weak) | Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22). | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-026 | Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals | Data Governance | **WEAK** | WEAK (Evidence_Weak) | No empirical benchmarks provided in corpus. | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-027 | Walk-Forward Cross-Validation Over Randomized k-Fold CV | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-028 | Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-029 | Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate | Validation | **PROVISIONAL** | MODERATE | Quantitative statistical limits or test validation results are absent from corpus. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-030 | Cluster-Wide Binary Hash Verification Before Live Routing | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-031 | Audit All Configuration Flags for Deprecated Memory Address Reuse | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-032 | Hard-Coded Parent-Order Balance Checks in Execution Loops | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-033 | Automated Sanity and Chaos Tests Across All Nodes Before Production Routing | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-034 | Population Stability Index (PSI) Tracking for Concept Drift Detection | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Difficult recovery with high severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-035 | Automatic Bid Size Reduction Under High Quantile Uncertainty | Validation | **PROVISIONAL** | MODERATE | Quantitative statistical limits or test validation results are absent from corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-036 | Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-037 | Consolidated Tape Latency Threshold Disconnect | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-038 | Order Book Depth Monitoring with Market Order Halt on Evaporation | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-039 | Minimum 90% Branch Coverage in Backtesting Modules | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-040 | Intraday Minute Feed Completeness Verification (No Dropped Candles) | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-041 | Cross-Verification of OHLCV Metrics Between Two Independent Data Providers | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-042 | Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) | Validation | **PROVISIONAL** | MODERATE | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-043 | SQLite WAL S3 Replication Recovery Under Hard Power-Off | Validation | **PROVISIONAL** | MODERATE | Quantitative statistical limits or test validation results are absent from corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-044 | Synthetic Anomaly Injection Into Parquet Ingestion Pipeline | Validation | **PROVISIONAL** | STRONG | Quantitative statistical limits or test validation results are absent from corpus. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-045 | FastMCP Execution Boundary Validation Against Prompt Injection | Validation | **PROVISIONAL** | STRONG | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-046 | Walk-Forward OOS Regime Fidelity — Unvalidated Assumption | Validation | **PROVISIONAL** | MODERATE | Quantitative statistical limits or test validation results are absent from corpus. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-047 | Cron Job Overlap and Deadlock Risk Under API Latency Spikes | Validation | **PROVISIONAL** | MODERATE | Quantitative statistical limits or test validation results are absent from corpus. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-048 | Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) | Validation | **PROVISIONAL** | MODERATE | Quantitative statistical limits or test validation results are absent from corpus. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-049 | Hard Position Limit Enforcement via API Disconnection | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-050 | Circuit Breaker for Trend-Following Dynamic Hedging Cycles | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-051 | Informational Cascade Volume Spike Halt | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-052 | Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-053 | Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls | Risk Control | **PROVISIONAL** | STRONG | Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-054 | Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-055 | Variation Margin Release Restriction During Elevated Volatility | Risk Control | **PROVISIONAL** | STRONG | Mathematical framework for VaR under non-ergodic conditions (§13). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-056 | Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns | Risk Control | **PROVISIONAL** | STRONG | Mathematical framework for VaR under non-ergodic conditions (§13). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-057 | ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-058 | ML Concept Drift Controls — Regime-Change Re-Anchoring | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | High — Difficult recovery with high severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-059 | High-Velocity Operational Deployment Risk — Systemic Control Requirement | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-060 | Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-061 | Non-Ergodic VaR Methodology — Mathematical Framework Requirement | Risk Control | **PROVISIONAL** | STRONG | Mathematical framework for VaR under non-ergodic conditions (§13). | High — Difficult recovery with high severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-062 | Slippage and Transaction Cost Controls in Live Execution | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-063 | Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance | Risk Control | **PROVISIONAL** | MODERATE | Slippage threshold and margin scaling curves are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-064 | Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals | Risk Control | **PROVISIONAL** | MODERATE | Slippage threshold and margin scaling curves are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-065 | Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards | Risk Control | **PROVISIONAL** | STRONG | Slippage threshold and margin scaling curves are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-066 | Multi-Broker Simultaneous Collateral Fire Sale Prevention | Risk Control | **PROVISIONAL** | STRONG | Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-067 | Prohibition of LLM Direct Trade Execution | Human Oversight | **PROVISIONAL** | STRONG | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-068 | Physical FastMCP Execution Boundary Enforcement | Human Oversight | **PROVISIONAL** | STRONG | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-069 | Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides | Human Oversight | **PROVISIONAL** | STRONG | Multi-sig approval implementation details (roles, TTL) are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-070 | Human-in-the-Loop Gate for AI-Influenced Pricing Decisions | Human Oversight | **PROVISIONAL** | STRONG | Multi-sig approval implementation details (roles, TTL) are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-071 | Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint) | Human Oversight | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-072 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Human Oversight | **PROVISIONAL** | MODERATE | Multi-sig approval implementation details (roles, TTL) are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-073 | Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) | Human Oversight | **PROVISIONAL** | MODERATE | Multi-sig approval implementation details (roles, TTL) are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-074 | Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing | Human Oversight | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-075 | Quantile Regression Uncertainty Band Human Review Requirement | Human Oversight | **WEAK** | WEAK (Evidence_Weak) | Multi-sig approval implementation details (roles, TTL) are missing. | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-076 | Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) | Human Oversight | **PROVISIONAL** | MODERATE | Multi-sig approval implementation details (roles, TTL) are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-077 | Embedded Zero-Copy Storage Architecture (DuckDB + SQLite) | Infrastructure | **PROVISIONAL** | STRONG | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-078 | Hive-Partitioned Parquet as Mandatory Market Data Storage Format | Infrastructure | **PROVISIONAL** | STRONG | Event loop latency logs under live-load are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-079 | SQLite WAL Management and S3 Replication Integrity | Infrastructure | **PROVISIONAL** | STRONG | Event loop latency logs under live-load are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-080 | Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery | Infrastructure | **PROVISIONAL** | MODERATE | Event loop latency logs under live-load are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-081 | Automated Binary Hash Verification Across All Production Clusters | Infrastructure | **PROVISIONAL** | STRONG | Event loop latency logs under live-load are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-082 | Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation | Infrastructure | **PROVISIONAL** | STRONG | Event loop latency logs under live-load are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-083 | Coordinated Deployment Strategy to Prevent Partial Binary Rollout | Infrastructure | **PROVISIONAL** | STRONG | Event loop latency logs under live-load are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-084 | Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition | Infrastructure | **WEAK** | WEAK (Evidence_Weak) | Precise cloud deployment topology (Docker/Kubernetes) needed when transitioning from Stage 2 (VM) to Stage 4 (SaaS) (§13, §14). | Critical — Cascading failure path leads to capital destruction. | Weak supporting evidence or low audit confidence. |
| ADR-085 | Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors | Infrastructure | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-086 | SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance | Infrastructure | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-087 | OAuth Token Auto-Refresh Without Manual Two-Factor Authentication | Infrastructure | **WEAK** | WEAK (Evidence_Weak) | Event loop latency logs under live-load are missing. | Critical — Cascading failure path leads to capital destruction. | Weak supporting evidence or low audit confidence. |
| ADR-088 | Data Pipeline Cron Job Overlap and Deadlock Prevention | Infrastructure | **PROVISIONAL** | MODERATE | Event loop latency logs under live-load are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-089 | Execution Circuit Breaker on Consolidated Tape Latency Breach | Infrastructure | **PROVISIONAL** | STRONG | Event loop latency logs under live-load are missing. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-090 | FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries | Infrastructure | **PROVISIONAL** | MODERATE | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-091 | Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events | Infrastructure | **PROVISIONAL** | MODERATE | Event loop latency logs under live-load are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-092 | DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load | Infrastructure | **PROVISIONAL** | MODERATE | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-093 | Strict LLM Execution Prohibition via FastMCP | AI Boundary | **PROVISIONAL** | STRONG | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-094 | AI Domain Segregation — Cognitive vs. Deterministic Execution | AI Boundary | **PROVISIONAL** | STRONG | Hallucination rates and prompt-injection vulnerability benchmarks are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-095 | Prohibition on Fully Autonomous AI Execution Grids | AI Boundary | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-096 | Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing | AI Boundary | **PROVISIONAL** | STRONG | Hallucination rates and prompt-injection vulnerability benchmarks are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-097 | Model Uncertainty Integration — AI Output as Execution Halt Trigger | AI Boundary | **PROVISIONAL** | STRONG | Hallucination rates and prompt-injection vulnerability benchmarks are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-098 | AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math | AI Boundary | **PROVISIONAL** | MODERATE | Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-099 | LLM Prohibition on Deterministic Chronological Sorting and Binary Math | AI Boundary | **PROVISIONAL** | STRONG | Hallucination rates and prompt-injection vulnerability benchmarks are missing. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-100 | Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk | AI Boundary | **PROVISIONAL** | STRONG | Hallucination rates and prompt-injection vulnerability benchmarks are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-101 | LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary | AI Boundary | **PROVISIONAL** | MODERATE | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-102 | LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM | AI Boundary | **PROVISIONAL** | MODERATE | Hallucination rates and prompt-injection vulnerability benchmarks are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-103 | Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary | AI Boundary | **WEAK** | WEAK (Evidence_Weak) | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-104 | Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification | AI Boundary | **PROVISIONAL** | MODERATE | Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22). | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-105 | Automated Binary Hash Verification Before Production Deployment | Reliability | **PROVISIONAL** | STRONG | Detailed post-mortem metrics or API uptime logs are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-106 | Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors | Reliability | **PROVISIONAL** | STRONG | Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14). | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-107 | Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops | Reliability | **PROVISIONAL** | STRONG | Detailed post-mortem metrics or API uptime logs are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-108 | Deprecated Code Purge to Prevent Configuration Flag Reactivation | Reliability | **PROVISIONAL** | STRONG | Detailed post-mortem metrics or API uptime logs are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-109 | Alert Fatigue Prevention via Dedicated Critical Alert Runbooks | Reliability | **PROVISIONAL** | MODERATE | Detailed post-mortem metrics or API uptime logs are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-110 | Validated Configuration Rollback Procedure Across All Nodes | Reliability | **PROVISIONAL** | STRONG | Detailed post-mortem metrics or API uptime logs are missing. | High — Significant impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-111 | Automated Chaos and Sanity Tests Across All Nodes Before Production Routing | Reliability | **PROVISIONAL** | MODERATE | Detailed post-mortem metrics or API uptime logs are missing. | Medium — Moderate impact on system reliability. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-112 | Execution Algorithm Disconnection on Consolidated Tape Latency Breach | Reliability | **PROVISIONAL** | STRONG | Detailed post-mortem metrics or API uptime logs are missing. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-113 | Buy-Side Order Book Depth Monitoring with Market Order Halt | Reliability | **PROVISIONAL** | MODERATE | Detailed post-mortem metrics or API uptime logs are missing. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-114 | Capital Buffer Requirement for Retroactive Exchange Trade Cancellation | Reliability | **PROVISIONAL** | MODERATE | Detailed post-mortem metrics or API uptime logs are missing. | Critical — Cascading failure path leads to capital destruction. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-115 | SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure | Reliability | **WEAK** | WEAK (Evidence_Weak) | Detailed post-mortem metrics or API uptime logs are missing. | Critical — Cascading failure path leads to capital destruction. | Weak supporting evidence or low audit confidence. |
| ADR-116 | Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks | Reliability | **WEAK** | WEAK (Evidence_Weak) | Detailed post-mortem metrics or API uptime logs are missing. | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-117 | Automated OAuth Token Refresh Without Manual Two-Factor Authentication | Reliability | **WEAK** | WEAK (Evidence_Weak) | Detailed post-mortem metrics or API uptime logs are missing. | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |
| ADR-118 | Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops | Reliability | **PROVISIONAL** | MODERATE | Detailed post-mortem metrics or API uptime logs are missing. | Critical — System-critical failure severity. | Requires empirical validation (e.g. benchmarks or live paper trade verification). |
| ADR-119 | DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load | Reliability | **WEAK** | WEAK (Evidence_Weak) | DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22). | Critical — Cascading failure path leads to capital destruction. | Weak supporting evidence or low audit confidence. |
| ADR-120 | API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events | Reliability | **WEAK** | WEAK (Evidence_Weak) | Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22). | Low — Minimal architectural impact. | Weak supporting evidence or low audit confidence. |

---

## 2. ADR Trust Matrix Summary

- **VERIFIED:** 0
- **PROVISIONAL:** 102
- **WEAK:** 18
- **REJECT:** 0

---

## 3. Unsupported ADR Registry

List of ADRs where supporting evidence is weak or absent from the primary research corpus:

- **ADR-010:** Yahoo Finance Adjusted Close Mis-Adjustment Risk (Evidence: Section 8 Finding 8 (Weakly Supported Findings — listed as weakly evidenced). | Audit: WEAK (Evidence_Weak))
- **ADR-014:** NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures (Evidence: Section 9 Assumption 24 (hidden assumption, untested). | Audit: WEAK (Evidence_Weak))
- **ADR-020:** SQLite WAL Transaction Integrity on NSE Trade Void Events (Evidence: Section 17 (Unknowns Requiring Future Research). | Audit: WEAK (Evidence_Weak))
- **ADR-021:** LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk (Evidence: Section 8 Finding 13 (Weakly Supported — safety claim unverified, risk label severe). | Audit: WEAK (Evidence_Weak))
- **ADR-022:** LLM Context Window Degradation on Raw HTML NSE/SEC Filings (Evidence: Section 8 Finding 25 (Weakly Supported). | Audit: WEAK (Evidence_Weak))
- **ADR-023:** Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale (Evidence: Section 22 (Missing Evidence). Section 6 (validation required — stress-test against RAM limits). | Audit: WEAK (Evidence_Weak))
- **ADR-024:** Missing Research — VaR Modeling Under Non-Ergodic Market Conditions (Evidence: Section 13 (Missing Research Inventory). | Audit: WEAK (Evidence_Weak))
- **ADR-025:** Missing Research — Multi-Broker Aggregate Margin Exposure Management (Evidence: Section 13 (Missing Research Inventory). | Audit: WEAK (Evidence_Weak))
- **ADR-026:** Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals (Evidence: Section 9 Assumption 21 (hidden assumption, untested). | Audit: WEAK (Evidence_Weak))
- **ADR-075:** Quantile Regression Uncertainty Band Human Review Requirement (Evidence: Section 9 Assumption 17 (hidden assumption only — no confidence score). | Audit: WEAK (Evidence_Weak))
- **ADR-084:** Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition (Evidence: Section 13 (Missing Research). Section 14 (under-researched corpus gap). | Audit: WEAK (Evidence_Weak))
- **ADR-087:** OAuth Token Auto-Refresh Without Manual Two-Factor Authentication (Evidence: Section 9 Assumption 22. | Audit: WEAK (Evidence_Weak))
- **ADR-103:** Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary (Evidence: Section 8 Findings 9 and 25 (Weakly Supported). Section 9 Assumption 24 (FinBERT US→Indian domain transfer unvalidated). | Audit: WEAK (Evidence_Weak))
- **ADR-115:** SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure (Evidence: Section 8 Finding 18 (Weakly Supported). Section 9 Assumptions 2 and 18. Section 21 (WAL lock → execution circuit timeout). Section 23 (power-off test required). | Audit: WEAK (Evidence_Weak))
- **ADR-116:** Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks (Evidence: Section 9 Assumption 4. | Audit: WEAK (Evidence_Weak))
- **ADR-117:** Automated OAuth Token Refresh Without Manual Two-Factor Authentication (Evidence: Section 9 Assumption 22. Section 7 Finding 14 (SEBI OAuth mandate). | Audit: WEAK (Evidence_Weak))
- **ADR-119:** DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load (Evidence: Section 22 (Missing Evidence). Section 6 (validation required). Section 14 (unsupported — ASGI 10 orders/sec without event loop blocking). | Audit: WEAK (Evidence_Weak))
- **ADR-120:** API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events (Evidence: Section 8 Finding 6 (Weakly Supported). Section 15 (Tier 3 evidence). Section 22 (Missing Evidence). | Audit: WEAK (Evidence_Weak))

---

## 4. Speculative ADR Registry

List of ADRs containing architectural inferences that represent unvalidated hidden assumptions:

- **ADR-010:** Yahoo Finance Adjusted Close Mis-Adjustment Risk (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-014:** NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures (Assumption: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).)
- **ADR-020:** SQLite WAL Transaction Integrity on NSE Trade Void Events (Assumption: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).)
- **ADR-021:** LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-022:** LLM Context Window Degradation on Raw HTML NSE/SEC Filings (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-023:** Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-024:** Missing Research — VaR Modeling Under Non-Ergodic Market Conditions (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-025:** Missing Research — Multi-Broker Aggregate Margin Exposure Management (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-026:** Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals (Assumption: Local disk I/O latency is sufficient for zero-copy DuckDB execution without memory overflow (§6).)
- **ADR-075:** Quantile Regression Uncertainty Band Human Review Requirement (Assumption: Solo operator will correctly diagnose HTTP 429 rate limit errors vs shadow IP bans (§9 A25).)
- **ADR-084:** Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition (Assumption: ASGI/FastAPI server process hosting FastMCP has sufficient memory and CPU scheduler priority.)
- **ADR-087:** OAuth Token Auto-Refresh Without Manual Two-Factor Authentication (Assumption: OAuth tokens can be automatically refreshed without daily manual 2FA (§9 A22).)
- **ADR-103:** Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary (Assumption: NLP sentiment models trained on US markets map effectively to Indian corporate disclosures (§9 A24).)
- **ADR-115:** SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure (Assumption: Litestream async backups won't encounter network dropouts during local PC crashes (§9 A2); local SQLite WAL file won't grow infinitely if S3 upload stream hangs (§9 A18).)
- **ADR-116:** Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks (Assumption: Automated data pipeline cron jobs won't overlap and deadlock if API latency spikes (§9 A4).)
- **ADR-117:** Automated OAuth Token Refresh Without Manual Two-Factor Authentication (Assumption: OAuth tokens can be automatically refreshed without daily manual 2FA (§9 A22).)
- **ADR-119:** DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load (Assumption: Hardware failure rates follow standard bathtub curves and are predictable.)
- **ADR-120:** API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events (Assumption: Hardware failure rates follow standard bathtub curves and are predictable.)

---

## 5. Dependency Issue Registry

List of dependency ordering and blocking constraints (deferred or weak ADRs blocking downstream items):

- **ADR-006:** Provider Selection — Upstox Uplink for Historical Split-Adjusted Data (Blocker Type: Deferred Validation Parameter)
- **ADR-013:** Survivorship Bias — Delisted Stock Inclusion Requirement (Blocker Type: Deferred Validation Parameter)
- **ADR-015:** Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery (Blocker Type: Deferred Validation Parameter)
- **ADR-018:** Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment (Blocker Type: Deferred Validation Parameter)
- **ADR-019:** Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy (Blocker Type: Deferred Validation Parameter)
- **ADR-029:** Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate (Blocker Type: Deferred Validation Parameter)
- **ADR-035:** Automatic Bid Size Reduction Under High Quantile Uncertainty (Blocker Type: Deferred Validation Parameter)
- **ADR-042:** Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) (Blocker Type: Deferred Validation Parameter)
- **ADR-043:** SQLite WAL S3 Replication Recovery Under Hard Power-Off (Blocker Type: Deferred Validation Parameter)
- **ADR-046:** Walk-Forward OOS Regime Fidelity — Unvalidated Assumption (Blocker Type: Deferred Validation Parameter)
- **ADR-047:** Cron Job Overlap and Deadlock Risk Under API Latency Spikes (Blocker Type: Deferred Validation Parameter)
- **ADR-048:** Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) (Blocker Type: Deferred Validation Parameter)
- **ADR-063:** Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance (Blocker Type: Deferred Validation Parameter)
- **ADR-064:** Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals (Blocker Type: Deferred Validation Parameter)
- **ADR-072:** Alert Fatigue Prevention via Dedicated Critical Alert Runbooks (Blocker Type: Deferred Validation Parameter)
- **ADR-073:** Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) (Blocker Type: Deferred Validation Parameter)
- **ADR-076:** Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) (Blocker Type: Deferred Validation Parameter)
- **ADR-080:** Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery (Blocker Type: Deferred Validation Parameter)
- **ADR-088:** Data Pipeline Cron Job Overlap and Deadlock Prevention (Blocker Type: Deferred Validation Parameter)
- **ADR-090:** FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries (Blocker Type: Deferred Validation Parameter)
- **ADR-091:** Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events (Blocker Type: Deferred Validation Parameter)
- **ADR-092:** DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load (Blocker Type: Deferred Validation Parameter)
- **ADR-098:** AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math (Blocker Type: Deferred Validation Parameter)
- **ADR-101:** LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary (Blocker Type: Deferred Validation Parameter)
- **ADR-102:** LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM (Blocker Type: Deferred Validation Parameter)
- **ADR-104:** Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification (Blocker Type: Deferred Validation Parameter)
- **ADR-109:** Alert Fatigue Prevention via Dedicated Critical Alert Runbooks (Blocker Type: Deferred Validation Parameter)
- **ADR-111:** Automated Chaos and Sanity Tests Across All Nodes Before Production Routing (Blocker Type: Deferred Validation Parameter)
- **ADR-113:** Buy-Side Order Book Depth Monitoring with Market Order Halt (Blocker Type: Deferred Validation Parameter)
- **ADR-114:** Capital Buffer Requirement for Retroactive Exchange Trade Cancellation (Blocker Type: Deferred Validation Parameter)
- **ADR-118:** Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops (Blocker Type: Deferred Validation Parameter)

---

## 6. Governance Gap Registry

List of governance gaps identified in audit reports:

- **ADR-020:** SQLite WAL Transaction Integrity on NSE Trade Void Events (Gap details: GAP-04: Slippage threshold quantification — no limit defined.)
- **ADR-023:** Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale (Gap details: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — entirely absent.)
- **ADR-024:** Missing Research — VaR Modeling Under Non-Ergodic Market Conditions (Gap details: GAP-02: Non-ergodic VaR mathematical framework — missing research.)
- **ADR-025:** Missing Research — Multi-Broker Aggregate Margin Exposure Management (Gap details: GAP-05: VIX threshold for variation margin — unquantified.)
- **ADR-028:** Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) (Gap details: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.)
- **ADR-029:** Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate (Gap details: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.)
- **ADR-034:** Population Stability Index (PSI) Tracking for Concept Drift Detection (Gap details: GAP-03: ML concept drift controls — no §11 Req paired.)
- **ADR-045:** FastMCP Execution Boundary Validation Against Prompt Injection (Gap details: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.)
- **ADR-047:** Cron Job Overlap and Deadlock Risk Under API Latency Spikes (Gap details: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.)
- **ADR-052:** Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity (Gap details: GAP-05: VIX threshold for variation margin — unquantified.)
- **ADR-053:** Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls (Gap details: GAP-10: Multi-broker aggregate margin exposure management — missing research.)
- **ADR-055:** Variation Margin Release Restriction During Elevated Volatility (Gap details: GAP-02: Non-ergodic VaR mathematical framework — missing research.)
- **ADR-058:** ML Concept Drift Controls — Regime-Change Re-Anchoring (Gap details: GAP-03: ML concept drift controls — no §11 Req paired.)
- **ADR-059:** High-Velocity Operational Deployment Risk — Systemic Control Requirement (Gap details: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.)
- **ADR-061:** Non-Ergodic VaR Methodology — Mathematical Framework Requirement (Gap details: GAP-02: Non-ergodic VaR mathematical framework — missing research.)
- **ADR-062:** Slippage and Transaction Cost Controls in Live Execution (Gap details: GAP-04: Slippage threshold quantification — no limit defined.)
- **ADR-064:** Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals (Gap details: GAP-06: Active risk committee governance standard — no §11 Req.)
- **ADR-065:** Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards (Gap details: GAP-05: VIX threshold for variation margin — unquantified.)
- **ADR-066:** Multi-Broker Simultaneous Collateral Fire Sale Prevention (Gap details: GAP-10: Multi-broker aggregate margin exposure management — missing research.)
- **ADR-068:** Physical FastMCP Execution Boundary Enforcement (Gap details: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.)
- **ADR-073:** Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) (Gap details: GAP-06: Active risk committee governance standard — no §11 Req.)
- **ADR-083:** Coordinated Deployment Strategy to Prevent Partial Binary Rollout (Gap details: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.)
- **ADR-084:** Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition (Gap details: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.)
- **ADR-088:** Data Pipeline Cron Job Overlap and Deadlock Prevention (Gap details: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.)
- **ADR-090:** FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries (Gap details: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.)
- **ADR-093:** Strict LLM Execution Prohibition via FastMCP (Gap details: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.)
- **ADR-098:** AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math (Gap details: GAP-11: FinBERT score to Kelly fraction conversion math — unresolved.)
- **ADR-104:** Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification (Gap details: GAP-07: FastMCP ASGI physical block — mandated but not empirically validated.)
- **ADR-105:** Automated Binary Hash Verification Before Production Deployment (Gap details: GAP-12: Cloud deployment topology Stage 2→4 — entirely unresearched.)
- **ADR-116:** Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks (Gap details: GAP-01: Cron job overlap deadlock — no §11 Req, no §23 test.)
- **ADR-119:** DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load (Gap details: GAP-08: DuckDB/SQLite 50GB concurrency benchmarks — entirely absent.)
- **ADR-120:** API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events (Gap details: GAP-09: Third-party broker API uptime during extreme events — no empirical data.)

---

## 7. Validation Gap Registry

List of ADRs missing specific validation pathways or having outstanding unknowns:

- **ADR-001:** Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-002:** SQLite Exclusion from Standalone Time-Series Aggregation (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-003:** Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-004:** Provider Disqualification — Zerodha Historical API as Sole Backtesting Source (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-005:** Corporate Actions — Mandatory Split-Adjusted Data Requirement (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-006:** Provider Selection — Upstox Uplink for Historical Split-Adjusted Data (Unknown: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).)
- **ADR-007:** Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-008:** SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-009:** Production Binary Hygiene — Deprecated Code Removal Requirement (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-010:** Yahoo Finance Adjusted Close Mis-Adjustment Risk (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-011:** Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-012:** Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-013:** Survivorship Bias — Delisted Stock Inclusion Requirement (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-014:** NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures (Unknown: Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13).)
- **ADR-015:** Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-016:** Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-017:** Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-018:** Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-019:** Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-020:** SQLite WAL Transaction Integrity on NSE Trade Void Events (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-021:** LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-022:** LLM Context Window Degradation on Raw HTML NSE/SEC Filings (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-023:** Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-024:** Missing Research — VaR Modeling Under Non-Ergodic Market Conditions (Unknown: Mathematical framework for VaR under non-ergodic conditions (§13).)
- **ADR-025:** Missing Research — Multi-Broker Aggregate Margin Exposure Management (Unknown: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).)
- **ADR-026:** Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals (Unknown: No empirical benchmarks provided in corpus.)
- **ADR-027:** Walk-Forward Cross-Validation Over Randomized k-Fold CV (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-028:** Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-029:** Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-030:** Cluster-Wide Binary Hash Verification Before Live Routing (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-031:** Audit All Configuration Flags for Deprecated Memory Address Reuse (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-032:** Hard-Coded Parent-Order Balance Checks in Execution Loops (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-033:** Automated Sanity and Chaos Tests Across All Nodes Before Production Routing (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-034:** Population Stability Index (PSI) Tracking for Concept Drift Detection (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-035:** Automatic Bid Size Reduction Under High Quantile Uncertainty (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-036:** Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-037:** Consolidated Tape Latency Threshold Disconnect (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-038:** Order Book Depth Monitoring with Market Order Halt on Evaporation (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-039:** Minimum 90% Branch Coverage in Backtesting Modules (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-040:** Intraday Minute Feed Completeness Verification (No Dropped Candles) (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-041:** Cross-Verification of OHLCV Metrics Between Two Independent Data Providers (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-042:** Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban) (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-043:** SQLite WAL S3 Replication Recovery Under Hard Power-Off (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-044:** Synthetic Anomaly Injection Into Parquet Ingestion Pipeline (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-045:** FastMCP Execution Boundary Validation Against Prompt Injection (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-046:** Walk-Forward OOS Regime Fidelity — Unvalidated Assumption (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-047:** Cron Job Overlap and Deadlock Risk Under API Latency Spikes (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-048:** Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift) (Unknown: Quantitative statistical limits or test validation results are absent from corpus.)
- **ADR-049:** Hard Position Limit Enforcement via API Disconnection (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-050:** Circuit Breaker for Trend-Following Dynamic Hedging Cycles (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-051:** Informational Cascade Volume Spike Halt (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-052:** Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-053:** Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls (Unknown: Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13).)
- **ADR-054:** Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-055:** Variation Margin Release Restriction During Elevated Volatility (Unknown: Mathematical framework for VaR under non-ergodic conditions (§13).)
- **ADR-056:** Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns (Unknown: Mathematical framework for VaR under non-ergodic conditions (§13).)
- **ADR-057:** ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-058:** ML Concept Drift Controls — Regime-Change Re-Anchoring (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-059:** High-Velocity Operational Deployment Risk — Systemic Control Requirement (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-060:** Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-061:** Non-Ergodic VaR Methodology — Mathematical Framework Requirement (Unknown: Mathematical framework for VaR under non-ergodic conditions (§13).)
- **ADR-062:** Slippage and Transaction Cost Controls in Live Execution (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-063:** Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-064:** Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-065:** Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards (Unknown: Slippage threshold and margin scaling curves are missing.)
- **ADR-066:** Multi-Broker Simultaneous Collateral Fire Sale Prevention (Unknown: Research on aggregate exposure management across Zerodha + Upstox simultaneously (§13).)
- **ADR-067:** Prohibition of LLM Direct Trade Execution (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-068:** Physical FastMCP Execution Boundary Enforcement (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-069:** Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides (Unknown: Multi-sig approval implementation details (roles, TTL) are missing.)
- **ADR-070:** Human-in-the-Loop Gate for AI-Influenced Pricing Decisions (Unknown: Multi-sig approval implementation details (roles, TTL) are missing.)
- **ADR-071:** Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint) (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-072:** Alert Fatigue Prevention via Dedicated Critical Alert Runbooks (Unknown: Multi-sig approval implementation details (roles, TTL) are missing.)
- **ADR-073:** Active Risk Committee Governance (Anti-Rubber-Stamp Requirement) (Unknown: Multi-sig approval implementation details (roles, TTL) are missing.)
- **ADR-074:** Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-075:** Quantile Regression Uncertainty Band Human Review Requirement (Unknown: Multi-sig approval implementation details (roles, TTL) are missing.)
- **ADR-076:** Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control) (Unknown: Multi-sig approval implementation details (roles, TTL) are missing.)
- **ADR-077:** Embedded Zero-Copy Storage Architecture (DuckDB + SQLite) (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-078:** Hive-Partitioned Parquet as Mandatory Market Data Storage Format (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-079:** SQLite WAL Management and S3 Replication Integrity (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-080:** Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-081:** Automated Binary Hash Verification Across All Production Clusters (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-082:** Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-083:** Coordinated Deployment Strategy to Prevent Partial Binary Rollout (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-084:** Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition (Unknown: Precise cloud deployment topology (Docker/Kubernetes) needed when transitioning from Stage 2 (VM) to Stage 4 (SaaS) (§13, §14).)
- **ADR-085:** Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-086:** SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-087:** OAuth Token Auto-Refresh Without Manual Two-Factor Authentication (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-088:** Data Pipeline Cron Job Overlap and Deadlock Prevention (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-089:** Execution Circuit Breaker on Consolidated Tape Latency Breach (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-090:** FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-091:** Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events (Unknown: Event loop latency logs under live-load are missing.)
- **ADR-092:** DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-093:** Strict LLM Execution Prohibition via FastMCP (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-094:** AI Domain Segregation — Cognitive vs. Deterministic Execution (Unknown: Hallucination rates and prompt-injection vulnerability benchmarks are missing.)
- **ADR-095:** Prohibition on Fully Autonomous AI Execution Grids (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-096:** Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing (Unknown: Hallucination rates and prompt-injection vulnerability benchmarks are missing.)
- **ADR-097:** Model Uncertainty Integration — AI Output as Execution Halt Trigger (Unknown: Hallucination rates and prompt-injection vulnerability benchmarks are missing.)
- **ADR-098:** AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math (Unknown: Exact mathematical formulas converting FinBERT scores into localized position sizing (Kelly fractions) (§13).)
- **ADR-099:** LLM Prohibition on Deterministic Chronological Sorting and Binary Math (Unknown: Hallucination rates and prompt-injection vulnerability benchmarks are missing.)
- **ADR-100:** Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk (Unknown: Hallucination rates and prompt-injection vulnerability benchmarks are missing.)
- **ADR-101:** LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-102:** LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM (Unknown: Hallucination rates and prompt-injection vulnerability benchmarks are missing.)
- **ADR-103:** Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-104:** Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification (Unknown: Specific failure rates for Claude 3.5/Gemini 1.5 returning invalid schema payloads at high frequency over long context windows (§22).)
- **ADR-105:** Automated Binary Hash Verification Before Production Deployment (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-106:** Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors (Unknown: Live out-of-sample statistical proof that DuckDB+SQLite+Claude 3.5 via FastMCP executes within Zerodha limits without ASGI event loop blocking (§14).)
- **ADR-107:** Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-108:** Deprecated Code Purge to Prevent Configuration Flag Reactivation (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-109:** Alert Fatigue Prevention via Dedicated Critical Alert Runbooks (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-110:** Validated Configuration Rollback Procedure Across All Nodes (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-111:** Automated Chaos and Sanity Tests Across All Nodes Before Production Routing (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-112:** Execution Algorithm Disconnection on Consolidated Tape Latency Breach (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-113:** Buy-Side Order Book Depth Monitoring with Market Order Halt (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-114:** Capital Buffer Requirement for Retroactive Exchange Trade Cancellation (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-115:** SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-116:** Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-117:** Automated OAuth Token Refresh Without Manual Two-Factor Authentication (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-118:** Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops (Unknown: Detailed post-mortem metrics or API uptime logs are missing.)
- **ADR-119:** DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load (Unknown: DuckDB/SQLite concurrency benchmarks for 50GB Parquet data lake with live writing SQLite database (§22).)
- **ADR-120:** API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events (Unknown: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (§22).)

---

## 8. Top 25 Strongest ADRs

The highest confidence, verified ADRs with strong evidence and no validation gaps:


---

## 9. Top 25 Weakest ADRs

The lowest confidence or highest risk speculative ADRs requiring primary validation research:

1. **ADR-010:** Yahoo Finance Adjusted Close Mis-Adjustment Risk (Evidence Strength: WEAK (Evidence_Weak))
2. **ADR-014:** NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures (Evidence Strength: WEAK (Evidence_Weak))
3. **ADR-020:** SQLite WAL Transaction Integrity on NSE Trade Void Events (Evidence Strength: WEAK (Evidence_Weak))
4. **ADR-021:** LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk (Evidence Strength: WEAK (Evidence_Weak))
5. **ADR-022:** LLM Context Window Degradation on Raw HTML NSE/SEC Filings (Evidence Strength: WEAK (Evidence_Weak))
6. **ADR-023:** Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale (Evidence Strength: WEAK (Evidence_Weak))
7. **ADR-024:** Missing Research — VaR Modeling Under Non-Ergodic Market Conditions (Evidence Strength: WEAK (Evidence_Weak))
8. **ADR-025:** Missing Research — Multi-Broker Aggregate Margin Exposure Management (Evidence Strength: WEAK (Evidence_Weak))
9. **ADR-026:** Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals (Evidence Strength: WEAK (Evidence_Weak))
10. **ADR-075:** Quantile Regression Uncertainty Band Human Review Requirement (Evidence Strength: WEAK (Evidence_Weak))
11. **ADR-084:** Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition (Evidence Strength: WEAK (Evidence_Weak))
12. **ADR-087:** OAuth Token Auto-Refresh Without Manual Two-Factor Authentication (Evidence Strength: WEAK (Evidence_Weak))
13. **ADR-103:** Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary (Evidence Strength: WEAK (Evidence_Weak))
14. **ADR-115:** SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure (Evidence Strength: WEAK (Evidence_Weak))
15. **ADR-116:** Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks (Evidence Strength: WEAK (Evidence_Weak))
16. **ADR-117:** Automated OAuth Token Refresh Without Manual Two-Factor Authentication (Evidence Strength: WEAK (Evidence_Weak))
17. **ADR-119:** DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load (Evidence Strength: WEAK (Evidence_Weak))
18. **ADR-120:** API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events (Evidence Strength: WEAK (Evidence_Weak))
19. **ADR-006:** Provider Selection — Upstox Uplink for Historical Split-Adjusted Data (Evidence Strength: MODERATE)
20. **ADR-013:** Survivorship Bias — Delisted Stock Inclusion Requirement (Evidence Strength: MODERATE)
21. **ADR-015:** Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery (Evidence Strength: MODERATE)
22. **ADR-018:** Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment (Evidence Strength: MODERATE)
23. **ADR-019:** Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy (Evidence Strength: MODERATE)
24. **ADR-029:** Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate (Evidence Strength: MODERATE)
25. **ADR-035:** Automatic Bid Size Reduction Under High Quantile Uncertainty (Evidence Strength: MODERATE)

---

## 10. Top 25 ADRs Requiring Human Review

Key regulatory, risk control, and human oversight gates requiring explicit committee review:

1. **ADR-009:** Production Binary Hygiene — Deprecated Code Removal Requirement (Governance Control: Yes — Deployment approval gate.)
2. **ADR-028:** Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) (Governance Control: Yes — Deployment approval gate.)
3. **ADR-029:** Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate (Governance Control: Yes — Deployment approval gate.)
4. **ADR-030:** Cluster-Wide Binary Hash Verification Before Live Routing (Governance Control: Yes — Deployment approval gate.)
5. **ADR-032:** Hard-Coded Parent-Order Balance Checks in Execution Loops (Governance Control: Yes — Execution safety gate.)
6. **ADR-033:** Automated Sanity and Chaos Tests Across All Nodes Before Production Routing (Governance Control: Yes — Deployment approval gate.)
7. **ADR-036:** Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume) (Governance Control: Yes — Execution safety gate.)
8. **ADR-037:** Consolidated Tape Latency Threshold Disconnect (Governance Control: Yes — Execution safety gate.)
9. **ADR-038:** Order Book Depth Monitoring with Market Order Halt on Evaporation (Governance Control: Yes — Execution safety gate.)
10. **ADR-045:** FastMCP Execution Boundary Validation Against Prompt Injection (Governance Control: Yes — Execution safety gate.)
11. **ADR-049:** Hard Position Limit Enforcement via API Disconnection (Governance Control: Yes — Risk governance gate required.)
12. **ADR-050:** Circuit Breaker for Trend-Following Dynamic Hedging Cycles (Governance Control: Yes — Risk governance gate required.)
13. **ADR-051:** Informational Cascade Volume Spike Halt (Governance Control: Yes — Risk governance gate required.)
14. **ADR-052:** Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity (Governance Control: Yes — Risk governance gate required.)
15. **ADR-053:** Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls (Governance Control: Yes — Risk governance gate required.)
16. **ADR-054:** Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation (Governance Control: Yes — Risk governance gate required.)
17. **ADR-055:** Variation Margin Release Restriction During Elevated Volatility (Governance Control: Yes — Risk governance gate required.)
18. **ADR-056:** Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns (Governance Control: Yes — Risk governance gate required.)
19. **ADR-057:** ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands (Governance Control: Yes — Risk governance gate required.)
20. **ADR-058:** ML Concept Drift Controls — Regime-Change Re-Anchoring (Governance Control: Yes — Risk governance gate required.)
21. **ADR-059:** High-Velocity Operational Deployment Risk — Systemic Control Requirement (Governance Control: Yes — Risk governance gate required.)
22. **ADR-060:** Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker (Governance Control: Yes — Risk governance gate required.)
23. **ADR-061:** Non-Ergodic VaR Methodology — Mathematical Framework Requirement (Governance Control: Yes — Risk governance gate required.)
24. **ADR-062:** Slippage and Transaction Cost Controls in Live Execution (Governance Control: Yes — Risk governance gate required.)
25. **ADR-063:** Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance (Governance Control: Yes — Risk governance gate required.)

---

## 11. Architecture Readiness Reassessment

**Can architecture planning begin?**  
### **`NO`**

### Justification:
According to the alignment directives, architecture planning cannot proceed if any critical ADR (affecting Data, Storage, Validation, Risk, Human Oversight, or Governance) remains classified as `PROVISIONAL`, `WEAK`, or `REJECT`.

Currently, there are **76** critical decisions in these categories classified as `PROVISIONAL` or `WEAK` due to unvalidated concurrency limits (e.g., DuckDB join limits on 50GB Parquet data lakes), unvalidated execution safety boundaries (e.g., Zerodha rate limit checks), and unproven model constraints.

The deferred validation paths are foundations that must be completed and proven (Level 1-5 validation completed and threshold criteria achieved) before architectural blueprints can be safely generated.

### Blockers Listing:

- ADR-001: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs) (PROVISIONAL - Data Governance)
- ADR-002: SQLite Exclusion from Standalone Time-Series Aggregation (PROVISIONAL - Data Governance)
- ADR-003: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited) (PROVISIONAL - Data Governance)
- ADR-004: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source (PROVISIONAL - Data Governance)
- ADR-005: Corporate Actions — Mandatory Split-Adjusted Data Requirement (PROVISIONAL - Data Governance)
- ADR-006: Provider Selection — Upstox Uplink for Historical Split-Adjusted Data (PROVISIONAL - Data Governance)
- ADR-007: Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited) (PROVISIONAL - Data Governance)
- ADR-008: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit (PROVISIONAL - Data Governance)
- ADR-009: Production Binary Hygiene — Deprecated Code Removal Requirement (PROVISIONAL - Data Governance)
- ADR-010: Yahoo Finance Adjusted Close Mis-Adjustment Risk (WEAK - Data Governance)
- ADR-011: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers (PROVISIONAL - Data Governance)
- ADR-012: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles) (PROVISIONAL - Data Governance)
- ADR-013: Survivorship Bias — Delisted Stock Inclusion Requirement (PROVISIONAL - Data Governance)
- ADR-014: NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures (WEAK - Data Governance)
- ADR-015: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery (PROVISIONAL - Data Governance)
- ADR-016: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion (PROVISIONAL - Data Governance)
- ADR-017: Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops (PROVISIONAL - Data Governance)
- ADR-018: Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment (PROVISIONAL - Data Governance)
- ADR-019: Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy (PROVISIONAL - Data Governance)
- ADR-020: SQLite WAL Transaction Integrity on NSE Trade Void Events (WEAK - Data Governance)
- ADR-021: LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk (WEAK - Data Governance)
- ADR-022: LLM Context Window Degradation on Raw HTML NSE/SEC Filings (WEAK - Data Governance)
- ADR-023: Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale (WEAK - Data Governance)
- ADR-024: Missing Research — VaR Modeling Under Non-Ergodic Market Conditions (WEAK - Data Governance)
- ADR-025: Missing Research — Multi-Broker Aggregate Margin Exposure Management (WEAK - Data Governance)
- ADR-026: Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals (WEAK - Data Governance)
- ADR-027: Walk-Forward Cross-Validation Over Randomized k-Fold CV (PROVISIONAL - Validation)
- ADR-028: Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe) (PROVISIONAL - Validation)
- ADR-029: Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate (PROVISIONAL - Validation)
- ADR-030: Cluster-Wide Binary Hash Verification Before Live Routing (PROVISIONAL - Validation)
- ... and 46 additional critical blockers.
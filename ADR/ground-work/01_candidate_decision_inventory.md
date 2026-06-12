# Candidate Decision Inventory

**Phase:** 1 — Decision Mining (Discovery Only)
**Status:** Complete — No ADRs Generated
**Source Documents:** `ADR/Algorithmic_Trading_Architecture_Consensus_Audit.pdf` (9 pages, 23 sections)
**Extraction Method:** 7 parallel specialist subagents, domain-partitioned mining
**Date:** 2026-06-03
**Total Candidates Extracted:** 116 (DG: 26 | VAL: 22 | RC: 18 | HO: 10 | INF: 16 | AIB: 12 | REL: 16)

> **Quality Gate Passed:**
> - ✅ No ADRs generated
> - ✅ No recommendations generated
> - ✅ No architecture generated
> - ✅ All candidates traceable to source evidence sections
> - ✅ Duplicates identified and cross-referenced

---

## Master Index

| Category | Prefix | Count | High | Medium | Low |
|----------|--------|-------|------|--------|-----|
| Data Governance | DG | 26 | 12 | 5 | 9 |
| Validation | VAL | 22 | 14 | 7 | 0 |
| Risk Control | RC | 18 | 16 | 2 | 0 |
| Human Oversight | HO | 10 | 6 | 3 | 1 |
| Infrastructure | INF | 16 | 9 | 6 | 1 |
| AI Boundary | AIB | 12 | 7 | 4 | 1 |
| Reliability | REL | 16 | 6 | 5 | 5 |
| **TOTAL** | | **120** | **70** | **32** | **17** |

---

## Section A — Data Governance (DG)

> Scope: data quality, storage format, sourcing/provider decisions, data retention, validation pipelines, schema, data continuity, survivorship bias.

---

### DG-001
- Candidate_ID: DG-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs)
- Decision_Category: Data Governance
- Extracted_Finding: DuckDB+SQLite hybrid embedded database is required for the quantitative trading system. Vector databases are architecturally unsuited because 95% of swing trading data is structured time-series (OHLCV), not semantic search workloads.
- Supporting_Evidence: Section 6 designates DuckDB+SQLite hybrid as required with 90/100 confidence. Section 19 mandates zero-copy architecture. Section 7 Finding 24 disqualifies SQLite alone for time-series aggregations.
- Evidence_Locations: §6 (Claim Lineage), §19 (Architecture Findings), §7 (Finding 24)
- Confidence: High
- Duplicate_Candidates: DG-002 (related — SQLite aggregation exclusion is a sub-constraint of this)
- Notes: Live concurrency benchmark for 50 GB Parquet with simultaneous SQLite writes is missing (§22). Stress-test against RAM limits unvalidated (§6). See DG-023 for the scale gap.

---

### DG-002
- Candidate_ID: DG-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SQLite Exclusion from Standalone Time-Series Aggregation
- Decision_Category: Data Governance
- Extracted_Finding: SQLite is computationally inadequate for time-series aggregations due to its row-oriented engine.
- Supporting_Evidence: Section 7 Finding 24 (Top 25 Highest Confidence Findings).
- Evidence_Locations: §7 (Finding 24)
- Confidence: High
- Duplicate_Candidates: DG-001 (parent decision)
- Notes: SQLite still has a role in the system (WAL transactional writes), but must never be the analytics query engine. Distinction is architecturally critical.

---

### DG-003
- Candidate_ID: DG-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited)
- Decision_Category: Data Governance
- Extracted_Finding: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month partitioning). Unstructured JSON data lakes are explicitly prohibited.
- Supporting_Evidence: Section 19 states this as a hard MUST constraint.
- Evidence_Locations: §19 (Architecture Findings), §6 (Claim Lineage)
- Confidence: High
- Duplicate_Candidates: DG-001 (same storage layer, different format dimension)
- Notes: No empirical benchmark proving multi-year 1-minute Parquet scans stay within RAM limits. Partition granularity at Month level may need review for intra-day query patterns.

---

### DG-004
- Candidate_ID: DG-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source
- Decision_Category: Data Governance
- Extracted_Finding: Zerodha historical API data is structurally incomplete and unsuitable as a sole backtesting source.
- Supporting_Evidence: Section 7 Finding 2 (Top 25 Highest Confidence Findings). Section 15 rates Data API Reliability as Tier 3 — practitioner testing only, subject to silent API updates.
- Evidence_Locations: §7 (Finding 2), §15 (Evidence Quality Matrix)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Zerodha is still valid for live execution; it is disqualified specifically as the *sole* historical data source for backtesting.

---

### DG-005
- Candidate_ID: DG-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Corporate Actions — Mandatory Split-Adjusted Data Requirement
- Decision_Category: Data Governance
- Extracted_Finding: Unadjusted stock splits corrupt technical indicators and backtest validity.
- Supporting_Evidence: Section 7 Finding 7 (Top 25 Highest Confidence Findings). Section 7 Finding 13 confirms Upstox Uplink provides up to 20 years of split-adjusted daily data.
- Evidence_Locations: §7 (Findings 7 and 13)
- Confidence: High
- Duplicate_Candidates: DG-006 (related — provider selection for split-adjusted data)
- Notes: De-merger handling by Upstox is flagged as weakly supported (§8 Finding 19) — complex corporate actions may not be correctly adjusted.

---

### DG-006
- Candidate_ID: DG-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Provider Selection — Upstox Uplink for Historical Split-Adjusted Data
- Decision_Category: Data Governance
- Extracted_Finding: Upstox Uplink API provides up to 20 years of split-adjusted daily data. However, complex de-merger split adjustments may not be handled perfectly.
- Supporting_Evidence: Section 7 Finding 13 (positive provider claim). Section 8 Finding 19 (caveat on de-merger accuracy — weakly supported).
- Evidence_Locations: §7 (Finding 13), §8 (Finding 19)
- Confidence: Medium
- Duplicate_Candidates: DG-005 (parent — the split-adjustment requirement that drives this selection)
- Notes: De-merger handling gap creates a residual data quality risk. No independent audit of Upstox historical adjustments exists in corpus.

---

### DG-007
- Candidate_ID: DG-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Backtesting Methodology — Walk-Forward CV Mandatory (K-Fold Prohibited)
- Decision_Category: Data Governance
- Extracted_Finding: Walk-forward cross-validation prevents chronological data leaks better than randomized k-fold CV.
- Supporting_Evidence: Section 7 Finding 8 (Top 25 Highest Confidence Findings). Section 15 Tier 2 evidence (Jegadeesh/Titman, NBER).
- Evidence_Locations: §7 (Finding 8), §15 (Evidence Quality Matrix)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Walk-forward OOS assumption is itself flagged as untested in §9 Assumption 5 — the methodology is preferred but its regime-shift fidelity is unvalidated. See VAL-020.

---

### DG-008
- Candidate_ID: DG-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit
- Decision_Category: Data Governance
- Extracted_Finding: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second.
- Supporting_Evidence: Section 7 Finding 14 (Top 25 Highest Confidence Findings — regulatory mandates).
- Evidence_Locations: §7 (Finding 14), §22 (Missing Evidence — broker latency during extreme events)
- Confidence: High
- Duplicate_Candidates: None
- Notes: OAuth token auto-refresh assumption (§9 Assumption 22) is unvalidated. 10 orders/sec under ASGI event loop is unsupported (§14 Corpus Coverage Audit).

---

### DG-009
- Candidate_ID: DG-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Production Binary Hygiene — Deprecated Code Removal Requirement
- Decision_Category: Data Governance
- Extracted_Finding: Deprecated code left in production binaries represents a massive unquantifiable risk.
- Supporting_Evidence: Section 7 Finding 25 (Top 25 Highest Confidence Findings). Section 12 Blind Spot (High) — unused code in Python binaries under-tested for server state mismatch triggering dead loops.
- Evidence_Locations: §7 (Finding 25), §12 (Blind Spot — Deprecated Code Reactivation, High)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Specific Python binary context named. Section 10 Mode 3 details the failure mechanism (config flag reuse reactivating deprecated modules).

---

### DG-010
- Candidate_ID: DG-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Yahoo Finance Adjusted Close Mis-Adjustment Risk
- Decision_Category: Data Governance
- Extracted_Finding: Yahoo Finance Adjusted Close has occasional mis-adjustments for dividend events.
- Supporting_Evidence: Section 8 Finding 8 (Weakly Supported Findings — listed as weakly evidenced).
- Evidence_Locations: §8 (Finding 8)
- Confidence: Low
- Duplicate_Candidates: DG-026 (related Yahoo Finance limitation)
- Notes: Evidence is weak (one practitioner claim in Weakly Supported section). No systematic audit of Yahoo Finance adjustment errors cited.

---

### DG-011
- Candidate_ID: DG-011
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers
- Decision_Category: Data Governance
- Extracted_Finding: Cross-verify OHLCV metrics between at least two independent data providers before running signal logic.
- Supporting_Evidence: Section 11 Validation Requirement 25 (mandated control). Section 15 Tier 3 rating for Data API Reliability.
- Evidence_Locations: §11 (Req 25), §15 (Evidence Quality Matrix)
- Confidence: High
- Duplicate_Candidates: DG-012 (complementary — DG-012 checks completeness; DG-011 checks correctness across providers)
- Notes: Provider independence assumption may be invalid if Upstox and Zerodha share the same NSE/BSE upstream feed infrastructure.

---

### DG-012
- Candidate_ID: DG-012
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles)
- Decision_Category: Data Governance
- Extracted_Finding: Ensure data continuity: explicitly verify that intraday minute feeds equal expected daily lengths (no dropped candles).
- Supporting_Evidence: Section 11 Validation Requirement 24. Section 23 (inject synthetic anomalies test). Section 15 Tier 3 API reliability.
- Evidence_Locations: §11 (Req 24), §23 (Assumptions to Test), §15
- Confidence: High
- Duplicate_Candidates: DG-011 (complementary)
- Notes: Operationalized test exists in §23. Strong traceability.

---

### DG-013
- Candidate_ID: DG-013
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Survivorship Bias — Delisted Stock Inclusion Requirement
- Decision_Category: Data Governance
- Extracted_Finding: Delisted stocks are assumed not necessary for a valid backtest (ignoring survivorship bias). This assumption is unvalidated.
- Supporting_Evidence: Section 9 Assumption 23 (hidden assumption). Survivorship bias corrupting Sharpe ratios is referenced in corpus.
- Evidence_Locations: §9 (Assumption 23)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: Single-section evidence. No quantification of survivorship bias magnitude on the specific strategy in corpus.

---

### DG-014
- Candidate_ID: DG-014
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: NLP Domain Validity — US-Trained Models on Indian Corporate Disclosures
- Decision_Category: Data Governance
- Extracted_Finding: NLP sentiment models (FinBERT) trained on US markets are assumed to effectively map to Indian corporate disclosures. This assumption is unvalidated.
- Supporting_Evidence: Section 9 Assumption 24 (hidden assumption, untested).
- Evidence_Locations: §9 (Assumption 24)
- Confidence: Low
- Duplicate_Candidates: DG-022 (related NLP/LLM limitation cluster)
- Notes: Domain transfer validity is a known NLP research gap for Indian regulatory text. No Indian-trained NLP model cited as alternative in corpus.

---

### DG-015
- Candidate_ID: DG-015
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery
- Decision_Category: Data Governance
- Extracted_Finding: S3/Litestream asynchronous backups are assumed not to encounter network dropouts during local PC crashes. SQLite WAL risks infinite growth if S3 upload hangs.
- Supporting_Evidence: Section 9 Assumptions 2 and 18 (hidden, untested). Section 23 (explicit test requirement). Section 21 (WAL lock as a systemic failure node).
- Evidence_Locations: §9 (Assumptions 2 and 18), §23 (Assumptions to Test), §21 (Systemic Failure Path)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: Litestream millisecond-exact recovery claim is explicitly Weakly Supported (§8 Finding 18). WAL revert-on-trade-cancellation unknown (§17). Both assumptions untested.

---

### DG-016
- Candidate_ID: DG-016
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion
- Decision_Category: Data Governance
- Extracted_Finding: Test the Data Validation Pipeline: inject synthetic anomalies (e.g., extreme high/low prices, missing minute bars) into the Parquet ingestion engine to verify that forward-fill algorithms and outlier detectors catch and isolate the corruption.
- Supporting_Evidence: Section 23 (Assumptions to Test). Section 10 Mode 24 (incorrect pricing causing infinite loops).
- Evidence_Locations: §23 (Assumptions to Test), §10 (Failure Mode 24)
- Confidence: High
- Duplicate_Candidates: DG-017 (DG-016 is the test; DG-017 is the failure mode it addresses)
- Notes: Test pass/fail criteria undefined in corpus.

---

### DG-017
- Candidate_ID: DG-017
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Failure Mode — Bad Pricing Data Triggering Infinite Downstream Processing Loops
- Decision_Category: Data Governance
- Extracted_Finding: Incorrect pricing data triggering infinite downstream processing loops (Content-to-Timing failure).
- Supporting_Evidence: Section 10 Failure Mode 24.
- Evidence_Locations: §10 (Failure Mode 24), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: DG-016 (the test that mitigates this mode)
- Notes: The specific trigger condition (e.g., zero price, negative price, extreme outlier) for the loop is undefined in corpus.

---

### DG-018
- Candidate_ID: DG-018
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Data Tape Latency — WebSocket Latency Spike Risk Acknowledgment
- Decision_Category: Data Governance
- Extracted_Finding: Assuming near-real-time WebSocket feeds are instant is a blind spot. Latency spikes trigger false HFT volume cascades.
- Supporting_Evidence: Section 12 Blind Spot (Medium risk — Data Tape Latency Delays).
- Evidence_Locations: §12 (Blind Spot Inventory — Medium)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: The governance decision here is whether to treat WebSocket data as real-time or as delayed, and how to communicate that to downstream signal logic.

---

### DG-019
- Candidate_ID: DG-019
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Exchange Trade Erasure — Clearinghouse Cancellation Data Handling Policy
- Decision_Category: Data Governance
- Extracted_Finding: Clearinghouses cancel trades to survive. Unhedged exposure from retroactively voided trade legs.
- Supporting_Evidence: Section 12 Blind Spot (Medium risk — Exchange Trade Erasure). Section 9 Assumption 1 (exchanges assumed not to retroactively erase trades).
- Evidence_Locations: §12 (Blind Spot Inventory — Medium), §9 (Assumption 1)
- Confidence: Medium
- Duplicate_Candidates: DG-020 (DG-020 is the storage-layer technical unknown; DG-019 is the business risk)
- Notes: LME Nickel crisis (2022) is the historical reference. Not confirmed for NSE/BSE context.

---

### DG-020
- Candidate_ID: DG-020
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SQLite WAL Transaction Integrity on NSE Trade Void Events
- Decision_Category: Data Governance
- Extracted_Finding: If the NSE clears trades that are later voided due to broker defaults, how does the local SQLite database cleanly revert local WAL logs without corrupting the backtest engine?
- Supporting_Evidence: Section 17 (Unknowns Requiring Future Research).
- Evidence_Locations: §17 (Unknowns)
- Confidence: Low
- Duplicate_Candidates: DG-019 (parent business risk), DG-015 (WAL management)
- Notes: Open research question. No mitigation proposed in corpus. Requires future research before architecture decision can be made.

---

### DG-021
- Candidate_ID: DG-021
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Extreme Hallucination / OOM Risk
- Decision_Category: Data Governance
- Extracted_Finding: LLMs can safely write dynamic SQL queries via MCP against DuckDB. Classified as WEAKLY SUPPORTED with qualifier: Extreme hallucination/OOM risk.
- Supporting_Evidence: Section 8 Finding 13 (Weakly Supported — safety claim unverified, risk label severe).
- Evidence_Locations: §8 (Finding 13)
- Confidence: Low
- Duplicate_Candidates: AIB-009 (the AI boundary dimension of this same finding)
- Notes: Weak support means the *safety claim* is unverified, not the risk. A hard governance boundary on LLM SQL generation may be warranted pending controlled testing.

---

### DG-022
- Candidate_ID: DG-022
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: LLM Context Window Degradation on Raw HTML NSE/SEC Filings
- Decision_Category: Data Governance
- Extracted_Finding: Small language models cannot process raw HTML SEC/NSE filings locally without context-window degradation.
- Supporting_Evidence: Section 8 Finding 25 (Weakly Supported).
- Evidence_Locations: §8 (Finding 25)
- Confidence: Low
- Duplicate_Candidates: DG-014 (related NLP/LLM limitation cluster)
- Notes: Data quality governance dimension: raw HTML is unsuitable for local SLM processing — implies pre-processing pipeline required.

---

### DG-023
- Candidate_ID: DG-023
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Missing Research — DuckDB/SQLite Concurrency Limits at 50GB Parquet Scale
- Decision_Category: Data Governance
- Extracted_Finding: No benchmarks exist for the exact memory load when DuckDB joins a 50GB Parquet data lake with a live, writing SQLite database locally.
- Supporting_Evidence: Section 22 (Missing Evidence). Section 6 (validation required — stress-test against RAM limits).
- Evidence_Locations: §22 (Missing Evidence), §6 (Claim Lineage)
- Confidence: Low
- Duplicate_Candidates: DG-001 (this is the unresolved scale validation for DG-001's storage decision)
- Notes: Pure evidence gap. Foundational to the entire storage architecture. If benchmarks fail, DG-001 and DG-003 require revision.

---

### DG-024
- Candidate_ID: DG-024
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Missing Research — VaR Modeling Under Non-Ergodic Market Conditions
- Decision_Category: Data Governance
- Extracted_Finding: The corpus acknowledges non-ergodicity but fails to provide a mathematical framework for calculating daily Value-at-Risk under non-ergodic conditions.
- Supporting_Evidence: Section 13 (Missing Research Inventory).
- Evidence_Locations: §13 (Missing Research)
- Confidence: Low
- Duplicate_Candidates: RC-013 (the risk control dimension of this gap)
- Notes: Open research question. No mathematical framework available. Blocks finalization of any quantitative risk model.

---

### DG-025
- Candidate_ID: DG-025
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Missing Research — Multi-Broker Aggregate Margin Exposure Management
- Decision_Category: Data Governance
- Extracted_Finding: How an algorithmic system specifically manages exposure across multiple Indian discount brokers (e.g., Zerodha + Upstox) simultaneously to avoid aggregate margin breaches — is missing research.
- Supporting_Evidence: Section 13 (Missing Research Inventory).
- Evidence_Locations: §13 (Missing Research)
- Confidence: Low
- Duplicate_Candidates: RC-005 (the risk control dimension of this gap)
- Notes: No multi-broker aggregation design exists in corpus. A critical governance gap for portfolio-level margin management.

---

### DG-026
- Candidate_ID: DG-026
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Yahoo Finance 15-20 Minute Data Delay Materiality on End-of-Day Signals
- Decision_Category: Data Governance
- Extracted_Finding: 15-20 minute delays on Yahoo Finance data will not materially affect end-of-day signal calculation. This assumption is unvalidated.
- Supporting_Evidence: Section 9 Assumption 21 (hidden assumption, untested).
- Evidence_Locations: §9 (Assumption 21)
- Confidence: Low
- Duplicate_Candidates: DG-010 (Yahoo Finance risk cluster)
- Notes: For swing/EOD strategies the assumption may be valid, but intraday signals would be materially affected. Strategy scope must gate this assumption's validity.

---

## Section B — Validation (VAL)

> Scope: backtesting methodology, testing requirements, chaos/sanity testing, deployment validation, signal validation, statistical thresholds, data integrity checks, coverage requirements.

---

### VAL-001
- Candidate_ID: VAL-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Walk-Forward Cross-Validation Over Randomized k-Fold CV
- Decision_Category: Validation
- Extracted_Finding: Walk-forward cross-validation prevents chronological data leaks better than randomized k-fold CV.
- Supporting_Evidence: Section 7 Finding 8 (Top 25 Highest Confidence). Section 15 Tier 2 evidence (Jegadeesh/Titman, NBER).
- Evidence_Locations: §7 (Finding 8), §15 (Evidence Quality Matrix)
- Confidence: High
- Duplicate_Candidates: VAL-020 (counterpoint assumption), VAL-008 (drift monitoring complement)
- Notes: Walk-forward OOS assumption is itself flagged as untested (§9 Assumption 5) for regime-shift fidelity. See VAL-020.

---

### VAL-002
- Candidate_ID: VAL-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Minimum Statistical Threshold for Strategy Deployment (t-stat > 3.0 / Deflated Sharpe)
- Decision_Category: Validation
- Extracted_Finding: t-statistic > 3.0 or rigorously deflated Sharpe ratio required to prove statistical edge.
- Supporting_Evidence: Section 7 Finding 23. Paired with §8 Finding 17 (t=2.0 explicitly insufficient).
- Evidence_Locations: §7 (Finding 23), §8 (Finding 17)
- Confidence: High
- Duplicate_Candidates: VAL-003 (sub-candidate — rejection of t=2.0)
- Notes: Deflated Sharpe methodology not described in corpus — a gap.

---

### VAL-003
- Candidate_ID: VAL-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Rejection of 95% Confidence Interval (t=2.0) as Insufficient Deployment Gate
- Decision_Category: Validation
- Extracted_Finding: 95% confidence interval (t=2.0) is insufficient to deploy a trading strategy.
- Supporting_Evidence: Section 8 Finding 17 (Weakly Supported — practitioner consensus only).
- Evidence_Locations: §8 (Finding 17)
- Confidence: Medium
- Duplicate_Candidates: VAL-002 (parent candidate)
- Notes: Evidence in Weakly Supported section. Corroborating signal only.

---

### VAL-004
- Candidate_ID: VAL-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Cluster-Wide Binary Hash Verification Before Live Routing
- Decision_Category: Validation
- Extracted_Finding: Mandate automated cluster-wide binary hash verification prior to live routing.
- Supporting_Evidence: Section 11 Req 1. Section 7 Finding 1 (Knight Capital, 95/100 confidence).
- Evidence_Locations: §11 (Req 1), §7 (Finding 1)
- Confidence: High
- Duplicate_Candidates: VAL-005 (complementary — config flags)
- Notes: Strongest empirical anchor in corpus (Knight Capital documented failure).

---

### VAL-005
- Candidate_ID: VAL-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Audit All Configuration Flags for Deprecated Memory Address Reuse
- Decision_Category: Validation
- Extracted_Finding: Audit all configuration flags to ensure zero reuse of deprecated memory addresses.
- Supporting_Evidence: Section 11 Req 2. Section 7 Finding 1 (Knight Capital mechanism).
- Evidence_Locations: §11 (Req 2), §7 (Finding 1)
- Confidence: High
- Duplicate_Candidates: VAL-004 (complementary)
- Notes: "Deprecated memory address" phrasing requires clarification — may mean config key reuse, pointer reuse, or legacy slot allocation.

---

### VAL-006
- Candidate_ID: VAL-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Hard-Coded Parent-Order Balance Checks in Execution Loops
- Decision_Category: Validation
- Extracted_Finding: Hard-code continuous parent-order balance checks directly into execution loops.
- Supporting_Evidence: Section 11 Req 3. Section 10 Mode 2 (runaway loops without balance checks).
- Evidence_Locations: §11 (Req 3), §10 (Mode 2)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Runtime assertion pattern embedded in code, not a test-suite check. Must not be overridable via configuration.

---

### VAL-007
- Candidate_ID: VAL-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Automated Sanity and Chaos Tests Across All Nodes Before Production Routing
- Decision_Category: Validation
- Extracted_Finding: Deploy automated sanity and chaos tests across all nodes before production routing.
- Supporting_Evidence: Section 11 Req 6. Section 10 Mode 6 (unvalidated rollback spreads bugs). Section 23 (specific test scenarios).
- Evidence_Locations: §11 (Req 6), §10 (Mode 6), §23
- Confidence: High
- Duplicate_Candidates: VAL-004 (partial overlap on deployment gate scope)
- Notes: Umbrella requirement; VAL-014 through VAL-019 are specific operationalized tests under this.

---

### VAL-008
- Candidate_ID: VAL-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Population Stability Index (PSI) Tracking for Concept Drift Detection
- Decision_Category: Validation
- Extracted_Finding: Track Population Stability Index (PSI) to measure concept drift between live and training data.
- Supporting_Evidence: Section 11 Req 9. Section 9 Assumption 5 (walk-forward OOS fidelity). Section 8 Finding 7 (AI grids cannot adapt across regime changes).
- Evidence_Locations: §11 (Req 9), §9 (Assumption 5), §8 (Finding 7)
- Confidence: High
- Duplicate_Candidates: VAL-001 (methodology), VAL-020 (counterpoint)
- Notes: PSI threshold not specified in corpus (standard: PSI > 0.25 = significant drift). Gap in corpus.

---

### VAL-009
- Candidate_ID: VAL-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Automatic Bid Size Reduction Under High Quantile Uncertainty
- Decision_Category: Validation
- Extracted_Finding: Program execution algorithms to automatically reduce bid size when quantile uncertainty bands widen.
- Supporting_Evidence: Section 11 Req 10. Section 5 Claim B (deterministic execution mandate, 95/100).
- Evidence_Locations: §11 (Req 10), §5 (Contradiction Matrix)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: Quantile model not specified in corpus. Gap.

---

### VAL-010
- Candidate_ID: VAL-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Hard Volume-Based Execution Limit (Max % of Trailing 1-Minute Volume)
- Decision_Category: Validation
- Extracted_Finding: Hard-limit execution algorithms from exceeding strict max percentage of trailing 1-minute volume.
- Supporting_Evidence: Section 11 Req 17. Section 10 Mode 21 (liquidity withdrawal from data feed lags).
- Evidence_Locations: §11 (Req 17), §10 (Mode 21)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Exact percentage cap not defined in corpus. Must be calibrated empirically.

---

### VAL-011
- Candidate_ID: VAL-011
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Consolidated Tape Latency Threshold Disconnect
- Decision_Category: Validation
- Extracted_Finding: Disconnect execution algorithms instantly if consolidated tape latency exceeds predefined microsecond thresholds.
- Supporting_Evidence: Section 11 Req 18. Section 10 Mode 21 (liquidity withdrawal from latency).
- Evidence_Locations: §11 (Req 18), §10 (Mode 21)
- Confidence: High
- Duplicate_Candidates: VAL-012 (related — order book depth halt)
- Notes: Microsecond threshold value not specified. Must be calibrated against tape provider SLA.

---

### VAL-012
- Candidate_ID: VAL-012
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Order Book Depth Monitoring with Market Order Halt on Evaporation
- Decision_Category: Validation
- Extracted_Finding: Continuously track buy-side order book depth and halt market orders if depth evaporates.
- Supporting_Evidence: Section 11 Req 19. Section 10 Mode 21.
- Evidence_Locations: §11 (Req 19), §10 (Mode 21), §9 (Assumption 4)
- Confidence: High
- Duplicate_Candidates: VAL-011 (related — both protect against liquidity/feed failures)
- Notes: Depth evaporation threshold undefined. May be impacted by denoising autoencoder masking (§10 Mode 12).

---

### VAL-013
- Candidate_ID: VAL-013
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Minimum 90% Branch Coverage in Backtesting Modules
- Decision_Category: Validation
- Extracted_Finding: Demand minimum 90% branch coverage (not just statement coverage) in backtesting modules.
- Supporting_Evidence: Section 11 Req 21.
- Evidence_Locations: §11 (Req 21)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Branch coverage, not statement coverage, is explicitly specified. No failure case cited — practitioner standard only.

---

### VAL-014
- Candidate_ID: VAL-014
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Intraday Minute Feed Completeness Verification (No Dropped Candles)
- Decision_Category: Validation
- Extracted_Finding: Verify intraday minute feeds equal expected daily lengths (no dropped candles).
- Supporting_Evidence: Section 11 Req 24. Section 23 (synthetic anomaly injection test). Section 15 Tier 3 API reliability.
- Evidence_Locations: §11 (Req 24), §23, §15
- Confidence: High
- Duplicate_Candidates: VAL-015 (complementary — provider cross-verification)
- Notes: Tier 3 provider risk elevates importance. Operationalized test exists in §23.

---

### VAL-015
- Candidate_ID: VAL-015
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Cross-Verification of OHLCV Metrics Between Two Independent Data Providers
- Decision_Category: Validation
- Extracted_Finding: Cross-verify OHLCV metrics between at least two independent data providers.
- Supporting_Evidence: Section 11 Req 25. Section 15 Tier 3 API reliability.
- Evidence_Locations: §11 (Req 25), §15
- Confidence: High
- Duplicate_Candidates: VAL-014 (complementary)
- Notes: Upstox/Zerodha may share upstream NSE/BSE feed — provider independence may be false.

---

### VAL-016
- Candidate_ID: VAL-016
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Sandbox Test of Broker Rate Limit Thresholds (HTTP 429 vs Shadow IP Ban)
- Decision_Category: Validation
- Extracted_Finding: Intentionally trigger Zerodha 429 errors in sandbox to validate deterministic exponential backoff and recovery logic.
- Supporting_Evidence: Section 23. Section 9 Assumption 25 (solo operator diagnosis ambiguity).
- Evidence_Locations: §23, §9 (Assumption 25)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: No formal benchmark exists. Tier 3 evidence per §15.

---

### VAL-017
- Candidate_ID: VAL-017
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SQLite WAL S3 Replication Recovery Under Hard Power-Off
- Decision_Category: Validation
- Extracted_Finding: Force a hardware power-off during simulated high-volume SQLite transaction write. Attempt recovery from Litestream S3 bucket upon reboot.
- Supporting_Evidence: Section 23. Section 8 Finding 18 (Litestream millisecond recovery — Weakly Supported).
- Evidence_Locations: §23, §8 (Finding 18)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: Litestream millisecond guarantee is weakly supported. Critical test since WAL replication is a single point of recovery.

---

### VAL-018
- Candidate_ID: VAL-018
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Synthetic Anomaly Injection Into Parquet Ingestion Pipeline
- Decision_Category: Validation
- Extracted_Finding: Inject synthetic anomalies (extreme prices, missing minute bars) into the Parquet ingestion engine to verify forward-fill and outlier detectors catch and isolate corruption.
- Supporting_Evidence: Section 23. Section 9 Assumption 20 (autoencoder noise assumption). Section 10 Mode 12 (denoising masking real anomalies).
- Evidence_Locations: §23, §9 (Assumption 20), §10 (Mode 12)
- Confidence: High
- Duplicate_Candidates: VAL-022 (assumption dimension of this test)
- Notes: Pass/fail criteria undefined. Strong evidence chain: assumption → failure mode → test.

---

### VAL-019
- Candidate_ID: VAL-019
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: FastMCP Execution Boundary Validation Against Prompt Injection
- Decision_Category: Validation
- Extracted_Finding: Attempt to prompt-inject the LLM to execute a trade directly, ensuring ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.
- Supporting_Evidence: Section 23. Section 5 Claim B (deterministic execution, 95/100).
- Evidence_Locations: §23, §5 (Contradiction Matrix)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Only LLM-specific security validation test in corpus. No established benchmark or pass/fail criteria defined.

---

### VAL-020
- Candidate_ID: VAL-020
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Walk-Forward OOS Regime Fidelity — Unvalidated Assumption
- Decision_Category: Validation
- Extracted_Finding: Walk-forward OOS data may not accurately mimic future market regimes (hidden assumption, untested).
- Supporting_Evidence: Section 9 Assumption 5. Section 8 Finding 7 (AI grids cannot adapt across regimes).
- Evidence_Locations: §9 (Assumption 5), §8 (Finding 7)
- Confidence: Medium
- Duplicate_Candidates: VAL-001 (counterpoint), VAL-008 (complement)
- Notes: Epistemically honest counterpoint to VAL-001. PSI tracking (VAL-008) is the recommended monitoring response.

---

### VAL-021
- Candidate_ID: VAL-021
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Cron Job Overlap and Deadlock Risk Under API Latency Spikes
- Decision_Category: Validation
- Extracted_Finding: Automated data pipeline cron jobs may overlap and deadlock if API latency spikes (hidden assumption, no mitigation in corpus).
- Supporting_Evidence: Section 9 Assumption 4. No corresponding Section 11 Requirement. No Section 23 test.
- Evidence_Locations: §9 (Assumption 4)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: ⚠️ UNMITIGATED GAP — no Validation Requirement in §11 and no chaos test in §23 addresses this. Corpus-level omission.

---

### VAL-022
- Candidate_ID: VAL-022
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Autoencoder Anomaly Classification Validation (Noise vs. Structural Shift)
- Decision_Category: Validation
- Extracted_Finding: Market anomalies identified by auto-encoder are assumed to be noise rather than true structural shifts. This assumption is unvalidated.
- Supporting_Evidence: Section 9 Assumption 20. Section 10 Mode 12 (denoising masking real anomalies). Section 23 (VAL-018 test operationalizes this).
- Evidence_Locations: §9 (Assumption 20), §10 (Mode 12), §23
- Confidence: Medium
- Duplicate_Candidates: VAL-018 (VAL-018 is the operationalized test; VAL-022 is the assumption itself)
- Notes: No ML accuracy thresholds (F1/precision/recall) defined.

---

## Section C — Risk Control (RC)

> Scope: position limits, margin management, circuit breakers, concentration risk, leverage limits, VaR methodology, regime-change handling, risk committee oversight, concept drift controls.

---

### RC-001
- Candidate_ID: RC-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Hard Position Limit Enforcement via API Disconnection
- Decision_Category: Risk Control
- Extracted_Finding: Configuring position limits as passive dashboard alerts rather than hard system halts allows breaches to go unmitigated during fast-moving markets.
- Supporting_Evidence: Section 10 Mode 4. Section 11 Req 4 (hard API disconnection mandate).
- Evidence_Locations: §10 (Mode 4), §11 (Req 4)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Direct failure mode / mitigation pair. Strong traceability.

---

### RC-002
- Candidate_ID: RC-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Circuit Breaker for Trend-Following Dynamic Hedging Cycles
- Decision_Category: Risk Control
- Extracted_Finding: Dynamic hedging algorithms trend-follow by selling assets into declining markets, creating positive feedback loops that accelerate market crashes.
- Supporting_Evidence: Section 7 Finding 11. Section 10 Mode 7. Section 11 Req 7.
- Evidence_Locations: §7 (Finding 11), §10 (Mode 7), §11 (Req 7)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Three-section corroboration. Highest evidence chain in RC candidates.

---

### RC-003
- Candidate_ID: RC-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Informational Cascade Volume Spike Halt
- Decision_Category: Risk Control
- Extracted_Finding: HFT algorithms mistakenly interpreting runaway execution loops as fundamental volume news; price-agnostic execution algorithms accelerating selling on false volume spikes.
- Supporting_Evidence: Section 10 Modes 8 and 20. Section 11 Req 8.
- Evidence_Locations: §10 (Modes 8, 20), §11 (Req 8)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Modes 8 and 20 represent two sub-vectors of the same control gap.

---

### RC-004
- Candidate_ID: RC-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Dynamic Margin Subsystem — Auto-Scale Against Portfolio Illiquidity
- Decision_Category: Risk Control
- Extracted_Finding: Execution sizing must auto-scale against portfolio illiquidity; static initial margins are disallowed.
- Supporting_Evidence: Section 18 ADR-002. Section 9 Assumption 15. Section 10 Mode 15. Section 11 Req 13.
- Evidence_Locations: §18 (ADR-002), §9 (Assumption 15), §10 (Mode 15), §11 (Req 13)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Richest evidence chain (four sections). Core systemic risk control.

---

### RC-005
- Candidate_ID: RC-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Multi-Broker Concentration Risk and Synthetic Leverage Opacity Controls
- Decision_Category: Risk Control
- Extracted_Finding: Extreme synthetic leverage hidden across multiple prime brokers bypasses standard risk constraints (Archegos). APIs only track localized risk.
- Supporting_Evidence: Section 7 Finding 20. Section 9 Assumption 14. Section 10 Mode 14. Section 11 Req 12. Section 12 Blind Spot (High).
- Evidence_Locations: §7 (Finding 20), §9 (Assumption 14), §10 (Mode 14), §11 (Req 12), §12 (Blind Spot — High)
- Confidence: High
- Duplicate_Candidates: RC-017 (TRS margin audit sub-control), RC-018 (collateral fire sale sub-control)
- Notes: Five-section corroboration. Cross-broker aggregation architecturally unaddressed.

---

### RC-006
- Candidate_ID: RC-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation
- Decision_Category: Risk Control
- Extracted_Finding: Risk managers repeatedly inflating bespoke scenario limits for prestigious clients.
- Supporting_Evidence: Section 9 Assumption 16. Section 10 Mode 16. Section 11 Req 14.
- Evidence_Locations: §9 (Assumption 16), §10 (Mode 16), §11 (Req 14)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Requires both system-level caps and procedural enforcement.

---

### RC-007
- Candidate_ID: RC-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Variation Margin Release Restriction During Elevated Volatility
- Decision_Category: Risk Control
- Extracted_Finding: Returning billions in variation margin immediately prior to a volatility default.
- Supporting_Evidence: Section 9 Assumption 17. Section 10 Mode 17. Section 11 Req 15.
- Evidence_Locations: §9 (Assumption 17), §10 (Mode 17), §11 (Req 15)
- Confidence: High
- Duplicate_Candidates: None
- Notes: VIX threshold for restriction trigger not quantified in corpus.

---

### RC-008
- Candidate_ID: RC-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Convergence Arbitrage Stress Testing Against Historical Correlation Breakdowns
- Decision_Category: Risk Control
- Extracted_Finding: Market non-ergodicity means historical correlation matrices break down during macro shocks. Market spreads fail to converge because of non-ergodic macroeconomic defaults.
- Supporting_Evidence: Section 7 Finding 15. Section 9 Assumption 3 (LTCM). Section 10 Mode 18. Section 11 Req 16.
- Evidence_Locations: §7 (Finding 15), §9 (Assumption 3), §10 (Mode 18), §11 (Req 16)
- Confidence: High
- Duplicate_Candidates: RC-013 (partial — non-ergodic VaR framework gap)
- Notes: LTCM is the named historical reference. Non-ergodic VaR framework absent (§13).

---

### RC-009
- Candidate_ID: RC-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: ML Model Uncertainty Integration — Execution Scale-Down on Wide Quantile Bands
- Decision_Category: Risk Control
- Extracted_Finding: If AI/ML modules output wide quantile regression bands, deterministic execution logic must automatically scale down or halt orders (preventing Zillow Offers failure).
- Supporting_Evidence: Section 18 ADR-003. Section 12 Blind Spot (Uncertainty Decoupling — High). Section 9 Assumption 11. Section 10 Mode 11. Section 11 Req 10.
- Evidence_Locations: §18 (ADR-003), §12 (Blind Spot — High), §9 (Assumption 11), §10 (Mode 11), §11 (Req 10)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Links directly to systemic failure path in §21.

---

### RC-010
- Candidate_ID: RC-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: ML Concept Drift Controls — Regime-Change Re-Anchoring
- Decision_Category: Risk Control
- Extracted_Finding: ML models anchoring to peak historical transaction data during sudden market downturn (Zillow Offers collapse). Claude 3.5 Anchors to Outdated Sentiment (Concept Drift).
- Supporting_Evidence: Section 7 Finding 16 (88/100). Section 10 Mode 10. Section 16 Confidence Matrix (88/100). Section 21 (concept drift as causal link).
- Evidence_Locations: §7 (Finding 16), §10 (Mode 10), §16 (Confidence Matrix), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: None
- Notes: No §11 validation requirement paired to this — corpus gap. Concept drift detection mechanism unspecified.

---

### RC-011
- Candidate_ID: RC-011
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: High-Velocity Operational Deployment Risk — Systemic Control Requirement
- Decision_Category: Risk Control
- Extracted_Finding: High-Velocity Operational Deployment Risk: 95/100 confidence rating. Highest confidence score in corpus.
- Supporting_Evidence: Section 16 Confidence Matrix (95/100). Section 21 Systemic Failure Path (full cascade chain).
- Evidence_Locations: §16 (Confidence Matrix), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Composite candidate spanning infrastructure, execution, and data feed risk. May need decomposition. No §11 requirement maps directly.

---

### RC-012
- Candidate_ID: RC-012
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Data Feed Latency Detection and Liquidity Withdrawal Circuit Breaker
- Decision_Category: Risk Control
- Extracted_Finding: Real-time data feed latency causes electronic market makers to withdraw liquidity, causing Flash Crashes. Zerodha WebSockets Drop Packets → Deterministic Engine Misinterprets Lags as Zero-Volume Pauses.
- Supporting_Evidence: Section 7 Finding 21 (92/100). Section 9 Assumption 6. Section 21 Systemic Failure Path.
- Evidence_Locations: §7 (Finding 21), §9 (Assumption 6), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: None
- Notes: 92/100 confidence. Must distinguish true zero-volume from latency-induced data absence.

---

### RC-013
- Candidate_ID: RC-013
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Non-Ergodic VaR Methodology — Mathematical Framework Requirement
- Decision_Category: Risk Control
- Extracted_Finding: No mathematical framework for VaR under non-ergodic conditions currently exists within the system.
- Supporting_Evidence: Section 13 (Missing Research). Section 7 Finding 15. Section 9 Assumption 3 (LTCM).
- Evidence_Locations: §13 (Missing Research), §7 (Finding 15), §9 (Assumption 3)
- Confidence: High
- Duplicate_Candidates: RC-008 (partial overlap on non-ergodic macro shocks), DG-024
- Notes: Research gap, not a configurable control. Decision: block live deployment until framework exists, or proceed with explicit gap acknowledgment.

---

### RC-014
- Candidate_ID: RC-014
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Slippage and Transaction Cost Controls in Live Execution
- Decision_Category: Risk Control
- Extracted_Finding: Slippage and transaction costs frequently destroy theoretical backtest alpha.
- Supporting_Evidence: Section 7 Finding 6. Section 21 Systemic Failure Path endpoint (15% execution slippage).
- Evidence_Locations: §7 (Finding 6), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: None
- Notes: No §11 validation requirement paired. Slippage threshold quantification absent. 15% figure in §21 is scenario-specific.

---

### RC-015
- Candidate_ID: RC-015
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Denoising Autoencoder Masking Audit — Anomaly Visibility Assurance
- Decision_Category: Risk Control
- Extracted_Finding: Denoising autoencoders masking real market anomalies from risk systems.
- Supporting_Evidence: Section 9 Assumption 12 (hidden assumption). Section 10 Mode 12.
- Evidence_Locations: §9 (Assumption 12), §10 (Mode 12)
- Confidence: Medium
- Duplicate_Candidates: RC-009 (related — ML model integrity, different mechanism)
- Notes: Thin evidence (single hidden assumption, one failure mode). No §11 validation requirement. Needs corroboration from model audit or empirical testing.

---

### RC-016
- Candidate_ID: RC-016
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Risk Committee Active Oversight Mandate — No Passive Rubber-Stamp Approvals
- Decision_Category: Risk Control
- Extracted_Finding: Replacing active, in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.
- Supporting_Evidence: Section 10 Mode 25.
- Evidence_Locations: §10 (Mode 25)
- Confidence: Medium
- Duplicate_Candidates: RC-006 (related governance control, different layer), HO-007
- Notes: Single-section evidence. Organizational enforcement mechanism required, not purely technical.

---

### RC-017
- Candidate_ID: RC-017
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Total Return Swap (TRS) Margin Audit Against Prime Brokerage Standards
- Decision_Category: Risk Control
- Extracted_Finding: Audit Total Return Swap margins to match standard prime brokerage initial margin limits.
- Supporting_Evidence: Section 11 Req 12. Section 7 Finding 20. Section 10 Mode 14.
- Evidence_Locations: §11 (Req 12), §7 (Finding 20), §10 (Mode 14)
- Confidence: High
- Duplicate_Candidates: RC-005 (parent — broader multi-broker opacity)
- Notes: RC-005 is the broader candidate; RC-017 is the specific TRS margin audit sub-control.

---

### RC-018
- Candidate_ID: RC-018
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Multi-Broker Simultaneous Collateral Fire Sale Prevention
- Decision_Category: Risk Control
- Extracted_Finding: Multiple prime brokers can liquidate identical collateral without causing correlated fire sales. Assumption treated as safe; failure mode documents it collapsing underlying asset values.
- Supporting_Evidence: Section 9 Assumption 19. Section 10 Mode 19. Section 21 Systemic Failure Path.
- Evidence_Locations: §9 (Assumption 19), §10 (Mode 19), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: RC-005 (related — accumulation mechanics; RC-018 is liquidation cascade mechanics)
- Notes: Requires cross-broker coordination controls architecturally absent.

---

## Section D — Human Oversight (HO)

> Scope: AI execution boundaries, human-in-the-loop requirements, approval gates, alert fatigue management, governance committees, autonomous agent limits, operator responsibility.

---

### HO-001
- Candidate_ID: HO-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Prohibition of LLM Direct Trade Execution
- Decision_Category: Human Oversight
- Extracted_Finding: AI Direct Execution Safety confidence is rated 10/100 (Extremely Low Confidence — Actively Contradicted). LLMs may only generate JSON reasoning payloads via FastMCP; direct execution of kite.place_order() by any LLM is strictly prohibited.
- Supporting_Evidence: Section 16 (10/100). Section 18 ADR-004. Section 20 Final Verdict.
- Evidence_Locations: §16 (Confidence Matrix), §18 (ADR-004), §20 (Final Research Verdict)
- Confidence: High
- Duplicate_Candidates: HO-002 (enforcement mechanism), AIB-001 (AI Boundary dimension)
- Notes: 10/100 is the strongest evidence signal in the entire corpus. This is the most well-supported human oversight finding.

---

### HO-002
- Candidate_ID: HO-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Physical FastMCP Execution Boundary Enforcement
- Decision_Category: Human Oversight
- Extracted_Finding: Attempt to prompt-inject the LLM to execute a trade directly, ensuring ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.
- Supporting_Evidence: Section 23. Section 18 ADR-004.
- Evidence_Locations: §23 (Assumptions to Test), §18 (ADR-004)
- Confidence: High
- Duplicate_Candidates: HO-001 (prohibition principle), AIB-012 (AI Boundary verification gap)
- Notes: Gap: physical block is mandated but not yet empirically validated. Adversarial testing required.

---

### HO-003
- Candidate_ID: HO-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Mandatory Multi-Signature Human Approval for Algorithmic Pricing Limit Overrides
- Decision_Category: Human Oversight
- Extracted_Finding: Enforce mandatory multi-signature human approval for algorithmic pricing limit overrides.
- Supporting_Evidence: Section 11 Req 11. Section 7 Finding 22 (92/100). Section 10 Mode 13.
- Evidence_Locations: §11 (Req 11), §7 (Finding 22), §10 (Mode 13)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Minimum number of signatories, identity/role of approvers, and approval TTL are unspecified — governance gaps.

---

### HO-004
- Candidate_ID: HO-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Human-in-the-Loop Gate for AI-Influenced Pricing Decisions
- Decision_Category: Human Oversight
- Extracted_Finding: Bypassing human-in-the-loop controls for AI pricing leads to toxic asset accumulation. Confidence 92/100.
- Supporting_Evidence: Section 7 Finding 22 (92/100). Section 10 Mode 13. Section 5 Claim B (95/100).
- Evidence_Locations: §7 (Finding 22), §10 (Mode 13), §5 (Contradiction Matrix)
- Confidence: High
- Duplicate_Candidates: HO-003 (specific to limit overrides; HO-004 is the broader principle)
- Notes: Detection mechanism and remediation path for toxic asset accumulation undefined in corpus.

---

### HO-005
- Candidate_ID: HO-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint)
- Decision_Category: Human Oversight
- Extracted_Finding: Execution must remain strictly deterministic, human-gated. Evidence Strength 95/100 due to SEBI regulations and Knight Capital failure.
- Supporting_Evidence: Section 5 Claim B (95/100 — highest single evidence score in corpus). Section 20 Final Verdict.
- Evidence_Locations: §5 (Contradiction Matrix — Claim B), §20 (Final Research Verdict)
- Confidence: High
- Duplicate_Candidates: HO-001 (technical prohibition), HO-004 (pricing gate)
- Notes: Dual basis: (1) SEBI regulatory requirement (legal), (2) Knight Capital precedent (empirical). SEBI regulations may change post-2026. Open design problem: how AI sentiment scores integrate into deterministic execution without violating the gate (§5).

---

### HO-006
- Candidate_ID: HO-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks
- Decision_Category: Human Oversight
- Extracted_Finding: Implement dedicated runbooks for PagerDuty/critical alerts to prevent fatigue. Failure Mode: Operators silencing critical alert channels due to high-volume alert fatigue.
- Supporting_Evidence: Section 10 Mode 5. Section 11 Req 5.
- Evidence_Locations: §10 (Mode 5), §11 (Req 5)
- Confidence: Medium
- Duplicate_Candidates: REL-005 (reliability dimension of same finding)
- Notes: Runbook content, escalation paths, SLA response times, and on-call rotation requirements unspecified. Practice-based evidence only.

---

### HO-007
- Candidate_ID: HO-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Active Risk Committee Governance (Anti-Rubber-Stamp Requirement)
- Decision_Category: Human Oversight
- Extracted_Finding: Replacing active in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.
- Supporting_Evidence: Section 10 Mode 25.
- Evidence_Locations: §10 (Mode 25)
- Confidence: Medium
- Duplicate_Candidates: RC-016 (risk control dimension)
- Notes: No corresponding §11 Validation Requirement — corpus gap. Governance standard (quorum, frequency, decision logs) undefined. Thin evidence: single section, no confidence score.

---

### HO-008
- Candidate_ID: HO-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Autonomous Agent Prohibition from Mathematical Execution, Data Storage, and Order Routing
- Decision_Category: Human Oversight
- Extracted_Finding: The architecture's mandate to isolate AI exclusively to the 'Research/Cognitive' domain while locking mathematical execution, data storage, and order routing in deterministic, embedded SQL/Python environments is the strongest and most validated claim in the corpus. Attempting to build an 'Auto-Coder' or fully autonomous AI trading bot within SEBI/Zerodha constraints will definitively trigger catastrophic failure.
- Supporting_Evidence: Section 20 Final Verdict. Section 16 (10/100). Section 7 Finding 9. Section 5 Claim B.
- Evidence_Locations: §20 (Final Research Verdict), §16 (Confidence Matrix), §7 (Finding 9), §5 (Contradiction Matrix)
- Confidence: High
- Duplicate_Candidates: HO-001 (specific to kite.place_order(); HO-008 is full domain isolation), AIB-002
- Notes: Zerodha API-level enforcement of this boundary is undocumented in corpus.

---

### HO-009
- Candidate_ID: HO-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Quantile Regression Uncertainty Band Human Review Requirement
- Decision_Category: Human Oversight
- Extracted_Finding: Hidden Assumption: Quantile regression uncertainty bands are sufficient risk limiters even if only displayed visually — this assumption is unvalidated.
- Supporting_Evidence: Section 9 Assumption 17 (hidden assumption only — no confidence score).
- Evidence_Locations: §9 (Assumption 17)
- Confidence: Low
- Duplicate_Candidates: RC-009 (enforcement dimension)
- Notes: Weakest-evidenced HO candidate. Listed as an assumption only — not a confirmed design flaw. Requires investigation. What "sufficient" means quantitatively is undefined.

---

### HO-010
- Candidate_ID: HO-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Autonomous Volume Growth Prohibition (Anti-Intentional-Bypass Control)
- Decision_Category: Human Oversight
- Extracted_Finding: Bypassing human-in-the-loop safeguards to pursue aggressive automated volume growth is a documented failure mode.
- Supporting_Evidence: Section 10 Mode 13. Section 7 Finding 22 (92/100).
- Evidence_Locations: §10 (Mode 13), §7 (Finding 22)
- Confidence: Medium
- Duplicate_Candidates: HO-004 (inadvertent bypass; HO-010 is intentional insider bypass)
- Notes: Enforcement mechanism for intentional insider bypass undefined. Access-control gap.

---

## Section E — Infrastructure (INF)

> Scope: storage architecture, deployment topology, binary verification, configuration management, network resilience, backup/recovery, API rate limiting, WAL management, embedded database choices, cloud vs local decisions.

---

### INF-001
- Candidate_ID: INF-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Embedded Zero-Copy Storage Architecture (DuckDB + SQLite)
- Decision_Category: Infrastructure
- Extracted_Finding: Storage MUST use embedded zero-copy architecture — DuckDB scanning Parquet files, attaching SQLite via sqlite_scanner. Vector DBs explicitly excluded.
- Supporting_Evidence: Section 6 (90/100 confidence). Section 19 (hard MUST). Section 7 Finding 24.
- Evidence_Locations: §6 (Claim Lineage), §19 (Architecture Findings), §7 (Finding 24)
- Confidence: High
- Duplicate_Candidates: INF-002 (Parquet format overlap), INF-003 (SQLite WAL overlap), DG-001
- Notes: Concurrency benchmark for 50 GB Parquet + live SQLite writes missing (§22). Stress-test against RAM limits unvalidated.

---

### INF-002
- Candidate_ID: INF-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Hive-Partitioned Parquet as Mandatory Market Data Storage Format
- Decision_Category: Infrastructure
- Extracted_Finding: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month). Unstructured JSON data lakes prohibited.
- Supporting_Evidence: Section 19 (hard MUST). Section 6 (DuckDB Parquet scan assumption).
- Evidence_Locations: §19 (Architecture Findings), §6 (Claim Lineage)
- Confidence: High
- Duplicate_Candidates: INF-001 (same storage layer), DG-003
- Notes: Multi-year 1-minute scan RAM validation missing. Monthly partition granularity may need review for intraday queries.

---

### INF-003
- Candidate_ID: INF-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SQLite WAL Management and S3 Replication Integrity
- Decision_Category: Infrastructure
- Extracted_Finding: Local SQLite WAL file risks infinite growth if S3 upload stream hangs. WAL must cleanly revert without corrupting backtest engine when NSE voids trades.
- Supporting_Evidence: Section 9 Assumption 18 (unbounded WAL). Section 17 (WAL revert-on-cancellation unknown). Section 21 (WAL lock as failure node).
- Evidence_Locations: §9 (Assumption 18), §17 (Unknowns), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: INF-004 (S3 backup overlap)
- Notes: No resolution proposed. WAL size cap, checkpoint frequency, and S3 upload timeout undefined. HIGH-RISK open item.

---

### INF-004
- Candidate_ID: INF-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Async Backup Strategy via S3 / Litestream for Local PC Crash Recovery
- Decision_Category: Infrastructure
- Extracted_Finding: S3/Litestream async backups assumed to not encounter network dropouts during local PC crashes. Hardware power-off recovery via Litestream must be empirically validated.
- Supporting_Evidence: Section 9 Assumption 2. Section 23 (force power-off test).
- Evidence_Locations: §9 (Assumption 2), §23 (Assumptions to Test)
- Confidence: Medium
- Duplicate_Candidates: INF-003 (WAL/S3 overlap)
- Notes: No evidence test has been run. RTO/RPO targets unspecified. Network dropout resilience during crash unproven.

---

### INF-005
- Candidate_ID: INF-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Automated Binary Hash Verification Across All Production Clusters
- Decision_Category: Infrastructure
- Extracted_Finding: All production clusters must execute automated binary hash checks before executing code to prevent Knight Capital-style deployments.
- Supporting_Evidence: Section 7 Finding 1 (95/100). Section 11 Req 1. Section 18 ADR-001.
- Evidence_Locations: §7 (Finding 1), §11 (Req 1), §18 (ADR-001)
- Confidence: High
- Duplicate_Candidates: INF-006 (config flag audit), INF-007 (deployment topology)
- Notes: Hash generation and distribution mechanism across nodes unspecified.

---

### INF-006
- Candidate_ID: INF-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Configuration Flag Namespace Audit to Prevent Deprecated Module Reactivation
- Decision_Category: Infrastructure
- Extracted_Finding: All configuration flags must be audited to ensure zero reuse of deprecated memory address spaces.
- Supporting_Evidence: Section 7 Finding 25. Section 10 Mode 3. Section 11 Req 2.
- Evidence_Locations: §7 (Finding 25), §10 (Mode 3), §11 (Req 2)
- Confidence: High
- Duplicate_Candidates: INF-005 (binary verification overlap)
- Notes: Tooling for audit (static analysis, runtime flag registry) unspecified. Scope of "configuration flags" unclear.

---

### INF-007
- Candidate_ID: INF-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Coordinated Deployment Strategy to Prevent Partial Binary Rollout
- Decision_Category: Infrastructure
- Extracted_Finding: Deploying system binaries to some but not all production servers (uncoordinated deployment) is a failure mode. Rolling back without validating server configurations spreads old bugs.
- Supporting_Evidence: Section 10 Modes 1 and 6. Section 11 Req 6.
- Evidence_Locations: §10 (Modes 1, 6), §11 (Req 6)
- Confidence: High
- Duplicate_Candidates: INF-005 (binary hash overlap), INF-008 (cloud topology overlap)
- Notes: Deployment orchestration tooling not specified. Under-researched for Stage 2→4 transition.

---

### INF-008
- Candidate_ID: INF-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Cloud Deployment Topology for Stage 2 (VM) to Stage 4 (SaaS) Transition
- Decision_Category: Infrastructure
- Extracted_Finding: Cloud deployment topology — Docker/Kubernetes architecture needed for Stage 2→4 transition — is identified as under-researched and missing.
- Supporting_Evidence: Section 13 (Missing Research). Section 14 (under-researched corpus gap).
- Evidence_Locations: §13 (Missing Research), §14 (Corpus Coverage Audit)
- Confidence: Low
- Duplicate_Candidates: INF-007 (deployment topology overlap)
- Notes: No architecture proposal exists. Requires dedicated research. Cannot support ADR without evidence.

---

### INF-009
- Candidate_ID: INF-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Deterministic Exponential Backoff for Zerodha HTTP 429 Rate Limit Errors
- Decision_Category: Infrastructure
- Extracted_Finding: The ingestion layer MUST implement deterministic exponential backoff when Zerodha returns HTTP 429 (rate limit exceeded) errors.
- Supporting_Evidence: Section 19 (hard MUST). Section 23 (sandbox test). Section 14 (10 orders/sec under ASGI unvalidated).
- Evidence_Locations: §19 (Architecture Findings), §23 (Assumptions to Test), §14 (Corpus Coverage Audit)
- Confidence: High
- Duplicate_Candidates: INF-010 (rate limiting overlap)
- Notes: Backoff ceiling, jitter strategy, retry budget unspecified. ASGI event loop integration under rate-limit unvalidated.

---

### INF-010
- Candidate_ID: INF-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SEBI-Mandated API Rate Limiting, Static IP, and OAuth Compliance
- Decision_Category: Infrastructure
- Extracted_Finding: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second. These are regulatory infrastructure constraints, not design choices.
- Supporting_Evidence: Section 7 Finding 14 (high confidence). Section 22 (extreme-event broker latency unmeasured).
- Evidence_Locations: §7 (Finding 14), §22 (Missing Evidence)
- Confidence: High
- Duplicate_Candidates: INF-009 (rate limiting overlap)
- Notes: OAuth token auto-refresh without daily manual 2FA is an open assumption (§9 Assumption 22). 10 orders/sec under ASGI conditions missing from corpus.

---

### INF-011
- Candidate_ID: INF-011
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: OAuth Token Auto-Refresh Without Manual Two-Factor Authentication
- Decision_Category: Infrastructure
- Extracted_Finding: OAuth tokens assumed to be automatically refreshable without requiring manual two-factor authentication daily. Assumption unvalidated.
- Supporting_Evidence: Section 9 Assumption 22.
- Evidence_Locations: §9 (Assumption 22)
- Confidence: Low
- Duplicate_Candidates: INF-010 (OAuth compliance overlap)
- Notes: If false, daily manual intervention required — critical operational constraint. Broker-specific OAuth implementation details differ.

---

### INF-012
- Candidate_ID: INF-012
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Data Pipeline Cron Job Overlap and Deadlock Prevention
- Decision_Category: Infrastructure
- Extracted_Finding: Automated data pipeline cron jobs assumed not to overlap and deadlock if API latency spikes. No deadlock prevention mechanism specified.
- Supporting_Evidence: Section 9 Assumption 4.
- Evidence_Locations: §9 (Assumption 4)
- Confidence: Medium
- Duplicate_Candidates: VAL-021 (validation dimension)
- Notes: No concurrency control mechanism proposed. Risk highest during market open/close when latency spikes are most likely.

---

### INF-013
- Candidate_ID: INF-013
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Execution Circuit Breaker on Consolidated Tape Latency Breach
- Decision_Category: Infrastructure
- Extracted_Finding: Execution algorithms must be instantly disconnected if consolidated tape latency exceeds predefined microsecond thresholds. Incorrect pricing data causes infinite downstream loops.
- Supporting_Evidence: Section 11 Req 18. Section 10 Mode 24. Section 21 (cascade node).
- Evidence_Locations: §11 (Req 18), §10 (Mode 24), §21 (Systemic Failure Path)
- Confidence: High
- Duplicate_Candidates: None
- Notes: Microsecond threshold values unspecified. Circuit breaker reset logic (manual vs. automatic) undefined.

---

### INF-014
- Candidate_ID: INF-014
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: FastMCP ASGI Co-hosting with FastAPI to Eliminate Network Boundaries
- Decision_Category: Infrastructure
- Extracted_Finding: FastMCP eliminates network boundaries by serving tool calls via ASGI alongside FastAPI on the same process, avoiding inter-service network hops for LLM tool execution.
- Supporting_Evidence: Section 7 Finding 10. Section 14 (ASGI event loop blocking unproven).
- Evidence_Locations: §7 (Finding 10), §14 (Corpus Coverage Audit)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: ASGI event loop blocking under concurrent LLM + SQLite write + Parquet scan is unproven. Hallucination failure rates on FastMCP unquantified (§22).

---

### INF-015
- Candidate_ID: INF-015
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Network Resilience for Zerodha WebSocket Packet Loss During Volatility Events
- Decision_Category: Infrastructure
- Extracted_Finding: During extreme sovereign macro shocks, Zerodha WebSocket connections drop packets, causing the deterministic engine to misinterpret lags — initiating a systemic cascade failure path.
- Supporting_Evidence: Section 21 (systemic failure path — packet loss → cascade → 15% slippage). Section 22 (missing empirical latency/uptime data).
- Evidence_Locations: §21 (Systemic Failure Path), §22 (Missing Evidence)
- Confidence: Medium
- Duplicate_Candidates: INF-009 (network resilience/backoff overlap)
- Notes: No packet-loss detection or WebSocket reconnect strategy specified. Empirical uptime data absent.

---

### INF-016
- Candidate_ID: INF-016
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: DuckDB Parquet Scan Memory Limits Under Multi-Year 1-Minute Data Load
- Decision_Category: Infrastructure
- Extracted_Finding: The assumption that file-system I/O is fast enough to support DuckDB Parquet scans locally without memory overflow must be validated via stress-testing against multi-year 1-minute partitioned Parquet data.
- Supporting_Evidence: Section 6 (assumption + validation requirement). Section 22 (DuckDB/SQLite concurrency benchmarks missing).
- Evidence_Locations: §6 (Claim Lineage), §22 (Missing Evidence)
- Confidence: Medium
- Duplicate_Candidates: INF-001 (DuckDB storage overlap), INF-002 (Parquet format overlap), DG-023
- Notes: No benchmark results exist. Foundational assumption — if it fails, INF-001 and INF-002 require revision.

---

## Section F — AI Boundary (AIB)

> Scope: LLM execution isolation, autonomous agent limits, AI domain segregation, model routing tiers, sentiment weight conversion math, AI-generated SQL risks, hallucination controls, prompt injection defenses, AI signal-to-position translation boundaries.

---

### AIB-001
- Candidate_ID: AIB-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Strict LLM Execution Prohibition via FastMCP
- Decision_Category: AI Boundary
- Extracted_Finding: LLMs may only generate JSON reasoning payloads via FastMCP. Direct execution of kite.place_order() by any LLM is strictly prohibited.
- Supporting_Evidence: Section 18 ADR-004. Section 5 Claim B (95/100). Section 16 (10/100 AI execution safety). Section 20 Final Verdict.
- Evidence_Locations: §18 (ADR-004), §4 (Consensus), §5 (Contradiction Matrix), §16 (Confidence Matrix), §20 (Final Verdict)
- Confidence: High
- Duplicate_Candidates: HO-001 (Human Oversight dimension), AIB-002 (parent)
- Notes: Remaining gap: ASGI/FastAPI physical enforcement vs. prompt-level only. See AIB-012.

---

### AIB-002
- Candidate_ID: AIB-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: AI Domain Segregation — Cognitive vs. Deterministic Execution
- Decision_Category: AI Boundary
- Extracted_Finding: Isolate AI exclusively to the 'Research/Cognitive' domain. Mathematical execution, data storage, and order routing must be locked in deterministic, embedded SQL/Python environments.
- Supporting_Evidence: Section 1 (Executive Summary). Section 4 (Cross-Document Consensus). Section 20 Final Verdict.
- Evidence_Locations: §1 (Executive Summary), §4 (Cross-Document Consensus), §20 (Final Verdict)
- Confidence: High
- Duplicate_Candidates: HO-008 (Human Oversight dimension), AIB-001 and AIB-003 (specific instantiations)
- Notes: Parent/umbrella boundary. Highest-confidence boundary in corpus. No dissenting evidence of material weight.

---

### AIB-003
- Candidate_ID: AIB-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Prohibition on Fully Autonomous AI Execution Grids
- Decision_Category: AI Boundary
- Extracted_Finding: Fully AI execution grids cannot adapt perfectly to 2024 data after training on 2023 data — weakly supported. Corpus verdict: attempting a fully autonomous AI trading bot within SEBI/Zerodha will definitively trigger catastrophic failure.
- Supporting_Evidence: Section 8 Finding 7 (weakly supported — autonomy claim false). Section 20 Final Verdict. Section 4 Consensus.
- Evidence_Locations: §8 (Finding 7), §20 (Final Verdict), §4 (Consensus)
- Confidence: High
- Duplicate_Candidates: AIB-002 (parent)
- Notes: "Weakly supported" means the *safety claim* is weak — the prohibition is strongly supported by absence of proof and systemic failure precedent.

---

### AIB-004
- Candidate_ID: AIB-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Human-in-the-Loop Mandatory Gate for AI Pricing / Order Routing
- Decision_Category: AI Boundary
- Extracted_Finding: Bypassing human-in-the-loop controls for AI pricing leads to toxic asset accumulation. Confidence 92/100.
- Supporting_Evidence: Section 7 Finding 22 (92/100). Section 10 Mode 13. Section 11 Req 11. Section 5 Claim B.
- Evidence_Locations: §7 (Finding 22), §10 (Mode 13), §11 (Req 11), §5 (Contradiction Matrix)
- Confidence: High
- Duplicate_Candidates: HO-004 (Human Oversight dimension), AIB-002 (parent)
- Notes: 92/100 confidence. Not theoretical — documented systemic risk vector.

---

### AIB-005
- Candidate_ID: AIB-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Model Uncertainty Integration — AI Output as Execution Halt Trigger
- Decision_Category: AI Boundary
- Extracted_Finding: If AI/ML modules output wide quantile regression bands, deterministic execution logic must automatically scale down or halt orders (preventing Zillow Offers failure).
- Supporting_Evidence: Section 18 ADR-003. Section 12 Blind Spot (Uncertainty Decoupling — High). Section 10 Mode 11. Section 11 Req 10.
- Evidence_Locations: §18 (ADR-003), §12 (Blind Spot), §10 (Mode 11), §11 (Req 10)
- Confidence: High
- Duplicate_Candidates: RC-009 (Risk Control dimension)
- Notes: Distinct boundary: AI uncertainty output → execution scaling response. Hidden Assumption 17 reveals passive display is not an adequate control.

---

### AIB-006
- Candidate_ID: AIB-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: AI Sentiment Score to Kelly Fraction Conversion — Unresolved Boundary Math
- Decision_Category: AI Boundary
- Extracted_Finding: Exact mathematical formulas converting semantic FinBERT scores (-1 to 1) into localized position sizing (Kelly fractions) without violating deterministic execution boundaries — classified as Missing Research.
- Supporting_Evidence: Section 13 (Missing Research). Section 5 (remaining uncertainty on AI/deterministic integration). Section 3 (Domain C — signal architecture black-box risk).
- Evidence_Locations: §13 (Missing Research), §5 (Contradiction Matrix), §3 (Domain C)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: Open research gap. Boundary location known; conversion formula unresolved. Future ADR requires this math to be specified.

---

### AIB-007
- Candidate_ID: AIB-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: LLM Prohibition on Deterministic Chronological Sorting and Binary Math
- Decision_Category: AI Boundary
- Extracted_Finding: LLM Autonomous Agents fail at deterministic chronological sorting and binary math.
- Supporting_Evidence: Section 7 Finding 9 (Top 25 Highest Confidence Findings).
- Evidence_Locations: §7 (Finding 9)
- Confidence: High
- Duplicate_Candidates: AIB-002 (parent domain segregation)
- Notes: Specific, enumerated capability limit within AIB-002 boundary. No quantified failure rate provided.

---

### AIB-008
- Candidate_ID: AIB-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Auto-Coder AI Backtester Prohibition — Survivorship Bias and Curve-Fitting Risk
- Decision_Category: AI Boundary
- Extracted_Finding: 'Auto-Coder' AI backtesters generate massive survivorship bias and curve-fitting.
- Supporting_Evidence: Section 7 Finding 12. Section 20 Final Verdict. Section 8 Finding 7.
- Evidence_Locations: §7 (Finding 12), §20 (Final Verdict), §8 (Finding 7)
- Confidence: High
- Duplicate_Candidates: AIB-003 (live execution autonomy; AIB-008 is backtesting domain)
- Notes: AI must not autonomously generate/run backtests without human validation of survivorship bias and walk-forward controls.

---

### AIB-009
- Candidate_ID: AIB-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: LLM Dynamic SQL Generation Against DuckDB — Prohibited or Extreme Risk Boundary
- Decision_Category: AI Boundary
- Extracted_Finding: LLMs writing dynamic SQL queries via MCP against DuckDB — classified as WEAKLY SUPPORTED with qualifier: Extreme hallucination/OOM risk.
- Supporting_Evidence: Section 8 Finding 13 (Weakly Supported — safety claim unverified, risk label severe).
- Evidence_Locations: §8 (Finding 13)
- Confidence: Medium
- Duplicate_Candidates: DG-021 (Data Governance dimension), AIB-001 (FastMCP overlap)
- Notes: Requires schema validation layer between LLM SQL output and DuckDB execution engine. Hard prohibition boundary may be warranted pending controlled testing.

---

### AIB-010
- Candidate_ID: AIB-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: LLM Model Routing Tier Boundary — Frontier vs. Fast vs. Local SLM
- Decision_Category: AI Boundary
- Extracted_Finding: Complex reasoning MUST route to Frontier models (Claude 3.5/Gemini 1.5), routine logic to Fast models (GPT-4o-mini), PII/Sanitization to local edge SLMs (Qwen 2.5).
- Supporting_Evidence: Section 19 (Architecture Findings — LLM Routing). Section 8 Findings 9 and 25 (SLM capability limits).
- Evidence_Locations: §19 (Architecture Findings), §8 (Findings 9, 25)
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: MUST constraint stated in §19 but primary source citations for tier assignments not provided. SLM capability limits support ceiling on local SLM usage.

---

### AIB-011
- Candidate_ID: AIB-011
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Local SLM Sentiment Tagging on SEBI Filings — Unverified Capability Boundary
- Decision_Category: AI Boundary
- Extracted_Finding: Local SLM (Llama 3.1 8B) accurately performing complex sentiment tagging on highly nuanced SEBI filings without hallucination — classified as WEAKLY SUPPORTED / unverified.
- Supporting_Evidence: Section 8 Findings 9 and 25 (Weakly Supported). Section 9 Assumption 24 (FinBERT US→Indian domain transfer unvalidated).
- Evidence_Locations: §8 (Findings 9, 25), §9 (Assumption 24)
- Confidence: Low
- Duplicate_Candidates: AIB-010 (model routing tier overlap), DG-014
- Notes: Three convergent weak-evidence signals. Open question: should SEBI filing sentiment route to Frontier models rather than local SLMs? Requires live OOS testing.

---

### AIB-012
- Candidate_ID: AIB-012
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Prompt Injection Defense — FastMCP ASGI Topology Physical Block Verification
- Decision_Category: AI Boundary
- Extracted_Finding: The FastMCP Execution Boundary must be tested via prompt injection: ensure ASGI/FastAPI topology physically blocks the agent from accessing execution endpoints.
- Supporting_Evidence: Section 23 (Assumptions to Test). Section 22 (LLM hallucination rates on FastMCP — missing evidence). Section 21 (FastMCP JSON processing a runaway order as failure node). Section 18 ADR-004.
- Evidence_Locations: §23, §22 (Missing Evidence), §21 (Systemic Failure Path), §18 (ADR-004)
- Confidence: Medium
- Duplicate_Candidates: AIB-001 (prohibition; AIB-012 is the verification gap), HO-002
- Notes: ⚠️ Highest-risk unverified assumption in AI boundary set. If ASGI topology does NOT physically block execution, the entire AIB-001/HO-001 boundary relies solely on LLM instruction compliance — not a valid security control.

---

## Section G — Reliability (REL)

> Scope: system uptime, failover, circuit breakers, backoff strategies, API reliability, alert management, deployment reliability, WAL recovery, monitoring, survivability under failure, operational runbooks.

---

### REL-001
- Candidate_ID: REL-001
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Automated Binary Hash Verification Before Production Deployment
- Decision_Category: Reliability
- Extracted_Finding: Automated deployment mismatch causes systemic execution failure (Knight Capital). All production clusters must execute automated binary hash checks before executing code.
- Supporting_Evidence: Section 7 Finding 1 (95/100). Section 10 Mode 1. Section 11 Req 1. Section 15 Tier 1/2 evidence. Section 16 (95/100). Section 18 ADR-001.
- Evidence_Locations: §7 (Finding 1), §10 (Mode 1), §11 (Req 1), §15, §16 (Confidence Matrix), §18 (ADR-001)
- Confidence: High
- Duplicate_Candidates: INF-005 (Infrastructure dimension), VAL-004 (Validation dimension)
- Notes: Most heavily corroborated finding in entire corpus. Six-section corroboration. Directly actionable.

---

### REL-002
- Candidate_ID: REL-002
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Deterministic Exponential Backoff for HTTP 429 Rate Limit Errors
- Decision_Category: Reliability
- Extracted_Finding: The system MUST implement deterministic exponential backoff in the ingestion layer to handle Zerodha HTTP 429 errors safely.
- Supporting_Evidence: Section 19 (hard MUST). Section 9 Assumption 25. Section 23 (sandbox test).
- Evidence_Locations: §19 (Architecture Findings), §9 (Assumption 25), §23 (Assumptions to Test)
- Confidence: High
- Duplicate_Candidates: INF-009 (Infrastructure dimension)
- Notes: HTTP 429 vs shadow IP ban distinction (§9 Assumption 25) adds unresolved operational complexity.

---

### REL-003
- Candidate_ID: REL-003
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Continuous Parent-Order Balance Checks Hard-Coded Into Execution Loops
- Decision_Category: Reliability
- Extracted_Finding: Order-routing systems running continuous loops without parent-order balance checks is a top failure mode. Hard-code continuous parent-order balance checks directly into execution loops.
- Supporting_Evidence: Section 10 Mode 2. Section 11 Req 3.
- Evidence_Locations: §10 (Mode 2), §11 (Req 3)
- Confidence: High
- Duplicate_Candidates: VAL-006 (Validation dimension)
- Notes: "Hard-code" implies not overridable via configuration. Exact frequency or data structure for balance check undefined.

---

### REL-004
- Candidate_ID: REL-004
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Deprecated Code Purge to Prevent Configuration Flag Reactivation
- Decision_Category: Reliability
- Extracted_Finding: Reusing a configuration flag address space that reactivates a deprecated legacy module is a top failure mode. Deprecated code left in production binaries = massive unquantifiable risk.
- Supporting_Evidence: Section 7 Finding 25. Section 9 Assumption 8. Section 10 Mode 3. Section 11 Req 2. Section 12 Blind Spot (High).
- Evidence_Locations: §7 (Finding 25), §9 (Assumption 8), §10 (Mode 3), §11 (Req 2), §12 (Blind Spot — High)
- Confidence: High
- Duplicate_Candidates: INF-006 (Infrastructure dimension), VAL-005 (Validation dimension)
- Notes: Python binaries explicitly named. Assumption 8 (developers assumed to purge deprecated code) flagged as hidden and untested — elevates risk.

---

### REL-005
- Candidate_ID: REL-005
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks
- Decision_Category: Reliability
- Extracted_Finding: Operators silencing critical alert channels due to high-volume alert fatigue is a top failure mode. Implement dedicated runbooks for PagerDuty/critical alerts to prevent fatigue.
- Supporting_Evidence: Section 10 Mode 5. Section 11 Req 5.
- Evidence_Locations: §10 (Mode 5), §11 (Req 5)
- Confidence: Medium
- Duplicate_Candidates: HO-006 (Human Oversight dimension)
- Notes: Practice-based evidence, no empirical study cited. Runbook content, SLA response times, escalation paths undefined.

---

### REL-006
- Candidate_ID: REL-006
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Validated Configuration Rollback Procedure Across All Nodes
- Decision_Category: Reliability
- Extracted_Finding: Rolling back a deployment without validating server configurations spreads old bugs.
- Supporting_Evidence: Section 10 Mode 6. Section 11 Req 6.
- Evidence_Locations: §10 (Mode 6), §11 (Req 6)
- Confidence: High
- Duplicate_Candidates: REL-001 (related — REL-001 covers deployment; REL-006 covers rollback validation), INF-007
- Notes: Node configuration validation mechanism not described. Rollback reliability depends on REL-001 hash verification infrastructure.

---

### REL-007
- Candidate_ID: REL-007
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Automated Chaos and Sanity Tests Across All Nodes Before Production Routing
- Decision_Category: Reliability
- Extracted_Finding: Deploy automated sanity and chaos tests across all nodes before production routing.
- Supporting_Evidence: Section 11 Req 6.
- Evidence_Locations: §11 (Req 6)
- Confidence: Medium
- Duplicate_Candidates: REL-001 and REL-006 (complementary, not duplicate), VAL-007
- Notes: Scope and pass/fail threshold of "sanity tests" undefined. Umbrella requirement for Section 23 test vectors.

---

### REL-008
- Candidate_ID: REL-008
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Execution Algorithm Disconnection on Consolidated Tape Latency Breach
- Decision_Category: Reliability
- Extracted_Finding: Real-time data feed latency causes electronic market makers to withdraw liquidity, causing Flash Crashes. Disconnect execution algorithms instantly if consolidated tape latency exceeds predefined microsecond thresholds.
- Supporting_Evidence: Section 7 Finding 21 (92/100). Section 10 Mode 21. Section 11 Req 18. Section 12 Blind Spot (Medium). Section 16 (92/100). Section 21 (systemic cascade node).
- Evidence_Locations: §7 (Finding 21), §10 (Mode 21), §11 (Req 18), §12, §16, §21
- Confidence: High
- Duplicate_Candidates: VAL-011 (Validation dimension), INF-013 (Infrastructure dimension)
- Notes: Most consequential single reliability decision in corpus per §21 cascade analysis. Microsecond threshold value undefined — critical gap.

---

### REL-009
- Candidate_ID: REL-009
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Buy-Side Order Book Depth Monitoring with Market Order Halt
- Decision_Category: Reliability
- Extracted_Finding: Exchange Stop-Logic completely trapping unexecuted buy-side orders. Continuously track buy-side order book depth and halt market orders if depth evaporates.
- Supporting_Evidence: Section 10 Mode 22. Section 11 Req 19.
- Evidence_Locations: §10 (Mode 22), §11 (Req 19)
- Confidence: Medium
- Duplicate_Candidates: REL-008 (related — microstructure failure; distinct trigger), VAL-012
- Notes: Depth evaporation threshold unspecified. No NSE-specific empirical case cited.

---

### REL-010
- Candidate_ID: REL-010
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Capital Buffer Requirement for Retroactive Exchange Trade Cancellation
- Decision_Category: Reliability
- Extracted_Finding: Exchanges retroactively erasing valid trades to protect clearinghouse solvency. Require capital buffers specifically designed to absorb retroactive exchange trade cancellations.
- Supporting_Evidence: Section 9 Assumption 1. Section 10 Mode 23. Section 11 Req 20. Section 12 Blind Spot (Medium). Section 17 (SQLite WAL revert unknown).
- Evidence_Locations: §9 (Assumption 1), §10 (Mode 23), §11 (Req 20), §12, §17
- Confidence: Medium
- Duplicate_Candidates: None
- Notes: LME Nickel crisis cited as analogue. Not confirmed for NSE/BSE. Buffer sizing methodology absent.

---

### REL-011
- Candidate_ID: REL-011
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: SQLite WAL S3 Litestream Replication Reliability Under Network/Hardware Failure
- Decision_Category: Reliability
- Extracted_Finding: S3/Litestream async backups assumed not to encounter network dropouts during local PC crashes. SQLite WAL assumed not to grow infinitely if S3 upload hangs. Litestream millisecond-exact recovery — Weakly Supported.
- Supporting_Evidence: Section 8 Finding 18 (Weakly Supported). Section 9 Assumptions 2 and 18. Section 21 (WAL lock → execution circuit timeout). Section 23 (power-off test required).
- Evidence_Locations: §8 (Finding 18), §9 (Assumptions 2, 18), §21, §23
- Confidence: Low
- Duplicate_Candidates: INF-003 (Infrastructure dimension), INF-004, DG-015
- Notes: Lowest-evidence reliability decision. Litestream millisecond recovery WEAKLY SUPPORTED. Both assumptions untested. Must be empirically validated before architecture reliance.

---

### REL-012
- Candidate_ID: REL-012
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Cron Job Overlap and Deadlock Prevention for Data Pipeline Tasks
- Decision_Category: Reliability
- Extracted_Finding: Automated data pipeline cron jobs assumed not to overlap and deadlock if API latency spikes.
- Supporting_Evidence: Section 9 Assumption 4.
- Evidence_Locations: §9 (Assumption 4)
- Confidence: Low
- Duplicate_Candidates: VAL-021 (Validation dimension), INF-012 (Infrastructure dimension)
- Notes: Single hidden assumption. No failure mode, validation requirement, or test in corpus. Risk highest at market open/close.

---

### REL-013
- Candidate_ID: REL-013
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Automated OAuth Token Refresh Without Manual Two-Factor Authentication
- Decision_Category: Reliability
- Extracted_Finding: OAuth tokens assumed to be automatically refreshable without manual two-factor authentication intervention daily.
- Supporting_Evidence: Section 9 Assumption 22. Section 7 Finding 14 (SEBI OAuth mandate).
- Evidence_Locations: §9 (Assumption 22), §7 (Finding 14)
- Confidence: Low
- Duplicate_Candidates: INF-011 (Infrastructure dimension)
- Notes: If 2FA cannot be automated, daily operational single point of failure. Broker-specific — requires per-broker verification.

---

### REL-014
- Candidate_ID: REL-014
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: Incorrect Pricing Data Circuit Breaker to Halt Infinite Downstream Processing Loops
- Decision_Category: Reliability
- Extracted_Finding: Incorrect pricing data triggering infinite downstream processing loops (Content-to-Timing failure) is a top failure mode.
- Supporting_Evidence: Section 10 Mode 24. Section 21 (misinterpretation → runaway order routing).
- Evidence_Locations: §10 (Mode 24), §21 (Systemic Failure Path)
- Confidence: Medium
- Duplicate_Candidates: REL-008 (related data integrity failure; distinct root cause), INF-013, DG-017
- Notes: Circuit breaker trigger condition undefined. Infinite loop termination mechanism undesigned in corpus.

---

### REL-015
- Candidate_ID: REL-015
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: DuckDB and SQLite Concurrency Benchmark Under 50GB Parquet Live-Write Load
- Decision_Category: Reliability
- Extracted_Finding: No benchmarks exist detailing memory load when DuckDB joins a 50 GB Parquet data lake with a live, writing SQLite database locally.
- Supporting_Evidence: Section 22 (Missing Evidence). Section 6 (validation required). Section 14 (unsupported — ASGI 10 orders/sec without event loop blocking).
- Evidence_Locations: §6 (Claim Lineage), §14 (Corpus Coverage Audit), §22 (Missing Evidence)
- Confidence: Low
- Duplicate_Candidates: INF-016 (Infrastructure dimension), DG-023
- Notes: Pure evidence gap. If DuckDB analytical queries block SQLite WAL during live trading, execution reliability collapses. Must be measured empirically before production architecture is locked.

---

### REL-016
- Candidate_ID: REL-016
- Source_Documents: Algorithmic_Trading_Architecture_Consensus_Audit.pdf
- Decision_Title: API Stability and Uptime Assurance for Third-Party Brokers During Extreme Market Events
- Decision_Category: Reliability
- Extracted_Finding: Empirical latency and uptime logs for Upstox Uplink and Angel One SmartAPI during extreme market events (election days, budget days) are missing. Angel One intraday data gaps reported (intermittency).
- Supporting_Evidence: Section 8 Finding 6 (Weakly Supported). Section 15 (Tier 3 evidence). Section 22 (Missing Evidence).
- Evidence_Locations: §8 (Finding 6), §15 (Evidence Quality Matrix), §22 (Missing Evidence)
- Confidence: Low
- Duplicate_Candidates: None
- Notes: Explicitly missing evidence. No broker SLA or availability guarantee cited. Any reliability guarantee for these APIs during tail-risk events is unfounded until empirical data collected.

---

## Cross-Category Duplicate Map

The following candidate IDs are cross-referenced across categories (same finding, different analytical dimension):

| Shared Finding | DG | VAL | RC | HO | INF | AIB | REL |
|---|---|---|---|---|---|---|---|
| Binary hash verification / Knight Capital | — | VAL-004 | — | — | INF-005 | — | REL-001 |
| Config flag / deprecated code | DG-009 | VAL-005 | — | — | INF-006 | — | REL-004 |
| SQLite WAL / S3 / Litestream | DG-015 | VAL-017 | — | — | INF-003/004 | — | REL-011 |
| FastMCP execution boundary | — | VAL-019 | — | HO-001/002 | — | AIB-001/012 | — |
| AI execution prohibition | — | — | — | HO-001/008 | — | AIB-001/002/003 | — |
| Dynamic margin | — | — | RC-004 | — | — | — | — |
| Model uncertainty / quantile bands | — | VAL-009 | RC-009 | HO-009 | — | AIB-005 | — |
| ML concept drift | — | VAL-008 | RC-010 | — | — | — | — |
| Cron job overlap | — | VAL-021 | — | — | INF-012 | — | REL-012 |
| Position limits / API disconnection | — | — | RC-001 | — | INF-013 | — | REL-008 |
| OHLCV cross-verification | DG-011 | VAL-015 | — | — | — | — | — |
| Alert fatigue / runbooks | — | — | — | HO-006 | — | — | REL-005 |
| DuckDB concurrency / RAM limits | DG-023 | — | — | — | INF-016 | — | REL-015 |
| Non-ergodic VaR gap | DG-024 | — | RC-013 | — | — | — | — |
| Multi-broker exposure aggregation | DG-025 | — | RC-005/018 | — | — | — | — |
| Risk committee governance | — | — | RC-016 | HO-007 | — | — | — |
| OAuth / SEBI compliance | DG-008 | — | — | — | INF-010/011 | — | REL-013 |
| LLM SQL against DuckDB | DG-021 | — | — | — | — | AIB-009 | — |
| Local SLM / NLP domain validity | DG-014 | — | — | — | — | AIB-011 | — |

---

## Open Gaps Summary

The following gaps were identified as unmitigated in the corpus (no corresponding Validation Requirement in §11 and no test in §23):

| Gap ID | Description | Relevant Candidates |
|--------|-------------|-------------------|
| GAP-01 | Cron job overlap deadlock — no §11 Req, no §23 test | VAL-021, INF-012, REL-012 |
| GAP-02 | Non-ergodic VaR mathematical framework — missing research | DG-024, RC-013 |
| GAP-03 | ML concept drift controls — no §11 Req paired | RC-010 |
| GAP-04 | Slippage threshold quantification — no limit defined | RC-014 |
| GAP-05 | VIX threshold for variation margin restriction — unquantified | RC-007 |
| GAP-06 | Active risk committee governance standard — no §11 Req | RC-016, HO-007 |
| GAP-07 | FastMCP ASGI physical block — mandated but not empirically validated | AIB-012, HO-002 |
| GAP-08 | DuckDB/SQLite 50GB concurrency benchmarks — entirely absent | DG-023, INF-016, REL-015 |
| GAP-09 | Third-party broker API uptime during extreme events — no empirical data | REL-016 |
| GAP-10 | Multi-broker aggregate margin exposure management — missing research | DG-025, RC-005 |
| GAP-11 | FinBERT score to Kelly fraction conversion math — unresolved | AIB-006 |
| GAP-12 | Cloud deployment topology Stage 2→4 — entirely unresearched | INF-008 |

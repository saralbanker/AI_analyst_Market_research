# 06 Architecture Core

**Objective:** Irreducible architecture constraints. Includes only root ADRs, drivers, and safety/governance blockers.

---

ADR_ID: ADR-001
TITLE: Embedded Database Selection — DuckDB+SQLite Hybrid (Not Vector DBs)
TYPE: ROOT
SOURCE_ADRS: Section 6 designates DuckDB+SQLite hybrid as required with 90/100 confidence. Section 19 mandates zero-copy architecture. Section 7 Finding 24 disqualifies SQLite alone for time-series aggregations. | Audit: STRONG
PROBLEM_SOLVED: DuckDB+SQLite hybrid embedded database is required for the quantitative trading system.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: ADR-003, ADR-011
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-002
TITLE: SQLite Exclusion from Standalone Time-Series Aggregation
TYPE: DRIVER
SOURCE_ADRS: Section 7 Finding 24 (Top 25 Highest Confidence Findings). | Audit: STRONG
PROBLEM_SOLVED: SQLite is computationally inadequate for time-series aggregations due to its row-oriented engine.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-003
TITLE: Storage Format — Hive-Partitioned Parquet Mandatory (JSON Lakes Prohibited)
TYPE: DRIVER
SOURCE_ADRS: Section 19 states this as a hard MUST constraint. | Audit: STRONG
PROBLEM_SOLVED: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month partitioning).
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-004
TITLE: Provider Disqualification — Zerodha Historical API as Sole Backtesting Source
TYPE: DRIVER
SOURCE_ADRS: Section 7 Finding 2 (Top 25 Highest Confidence Findings). Section 15 rates Data API Reliability as Tier 3 — practitioner testing only, subject to silent API updates. | Audit: STRONG
PROBLEM_SOLVED: Zerodha historical API data is structurally incomplete and unsuitable as a sole backtesting source.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-008
TITLE: SEBI Compliance — Static IP, OAuth, 10 Orders/sec Rate Limit
TYPE: ROOT
SOURCE_ADRS: Section 7 Finding 14 (Top 25 Highest Confidence Findings — regulatory mandates). | Audit: STRONG
PROBLEM_SOLVED: SEBI regulations mandate static IP addressing, OAuth authentication, and strict rate limiting at 10 orders/second.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: ADR-010, ADR-015
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-011
TITLE: Data Validation — Cross-Verify OHLCV Metrics Across Two Independent Providers
TYPE: DRIVER
SOURCE_ADRS: Section 11 Validation Requirement 25 (mandated control). Section 15 Tier 3 rating for Data API Reliability. | Audit: STRONG
PROBLEM_SOLVED: Cross-verify OHLCV metrics between at least two independent data providers before running signal logic.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-012
TITLE: Data Continuity — Intraday Minute Feed Completeness (No Dropped Candles)
TYPE: DRIVER
SOURCE_ADRS: Section 11 Validation Requirement 24. Section 23 (inject synthetic anomalies test). Section 15 Tier 3 API reliability. | Audit: STRONG
PROBLEM_SOLVED: Ensure data continuity: explicitly verify that intraday minute feeds equal expected daily lengths (no dropped candles).
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-015
TITLE: Backup and Recovery — SQLite WAL Litestream S3 Crash Recovery
TYPE: BLOCKER
SOURCE_ADRS: Section 9 Assumptions 2 and 18 (hidden, untested). Section 23 (explicit test requirement). Section 21 (WAL lock as a systemic failure node). | Audit: MODERATE
PROBLEM_SOLVED: S3/Litestream asynchronous backups are assumed not to encounter network dropouts during local PC crashes.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: MODERATE
CONFIDENCE: Medium
STATUS: KEEP

---

ADR_ID: ADR-016
TITLE: Validation Pipeline — Synthetic Anomaly Injection Testing for Parquet Ingestion
TYPE: BLOCKER
SOURCE_ADRS: Section 23 (Assumptions to Test). Section 10 Mode 24 (incorrect pricing causing infinite loops). | Audit: STRONG
PROBLEM_SOLVED: Test the Data Validation Pipeline: inject synthetic anomalies (e.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the data governance boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-031
TITLE: Audit All Configuration Flags for Deprecated Memory Address Reuse
TYPE: ROOT
SOURCE_ADRS: Section 11 Req 2. Section 7 Finding 1 (Knight Capital mechanism). | Audit: STRONG
PROBLEM_SOLVED: Audit all configuration flags to ensure zero reuse of deprecated memory addresses.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the validation boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-032
TITLE: Hard-Coded Parent-Order Balance Checks in Execution Loops
TYPE: DRIVER
SOURCE_ADRS: Section 11 Req 3. Section 10 Mode 2 (runaway loops without balance checks). | Audit: STRONG
PROBLEM_SOLVED: Hard-code continuous parent-order balance checks directly into execution loops.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the validation boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-034
TITLE: Population Stability Index (PSI) Tracking for Concept Drift Detection
TYPE: BLOCKER
SOURCE_ADRS: Section 11 Req 9. Section 9 Assumption 5 (walk-forward OOS fidelity). Section 8 Finding 7 (AI grids cannot adapt across regime changes). | Audit: STRONG
PROBLEM_SOLVED: Track Population Stability Index (PSI) to measure concept drift between live and training data.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the validation boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-054
TITLE: Bespoke Scenario Limit Hard Caps to Prevent Risk Manager Inflation
TYPE: ROOT
SOURCE_ADRS: Section 9 Assumption 16. Section 10 Mode 16. Section 11 Req 14. | Audit: STRONG
PROBLEM_SOLVED: Risk managers repeatedly inflating bespoke scenario limits for prestigious clients.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the risk control boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-071
TITLE: Deterministic Human-Gated Execution Mandate (SEBI Regulatory Constraint)
TYPE: ROOT
SOURCE_ADRS: Section 5 Claim B (95/100 — highest single evidence score in corpus). Section 20 Final Verdict. | Audit: STRONG
PROBLEM_SOLVED: Execution must remain strictly deterministic, human-gated.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the human oversight boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-072
TITLE: Alert Fatigue Prevention via Dedicated Critical Alert Runbooks
TYPE: BLOCKER
SOURCE_ADRS: Section 10 Mode 5. Section 11 Req 5. | Audit: MODERATE
PROBLEM_SOLVED: Implement dedicated runbooks for PagerDuty/critical alerts to prevent fatigue.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the human oversight boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: MODERATE
CONFIDENCE: Medium
STATUS: KEEP

---

ADR_ID: ADR-073
TITLE: Active Risk Committee Governance (Anti-Rubber-Stamp Requirement)
TYPE: BLOCKER
SOURCE_ADRS: Section 10 Mode 25. | Audit: MODERATE
PROBLEM_SOLVED: Replacing active in-person risk committees with passive rubber-stamp email approvals is a documented failure mode.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the human oversight boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: MODERATE
CONFIDENCE: Medium
STATUS: KEEP

---

ADR_ID: ADR-077
TITLE: Embedded Zero-Copy Storage Architecture (DuckDB + SQLite)
TYPE: BLOCKER
SOURCE_ADRS: Section 6 (90/100 confidence). Section 19 (hard MUST). Section 7 Finding 24. | Audit: STRONG
PROBLEM_SOLVED: Storage MUST use embedded zero-copy architecture — DuckDB scanning Parquet files, attaching SQLite via sqlite_scanner.
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the infrastructure boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

ADR_ID: ADR-078
TITLE: Hive-Partitioned Parquet as Mandatory Market Data Storage Format
TYPE: DRIVER
SOURCE_ADRS: Section 19 (hard MUST). Section 6 (DuckDB Parquet scan assumption). | Audit: STRONG
PROBLEM_SOLVED: Market data MUST be stored in Hive-partitioned Parquet files (Year/Month).
WHY_ARCHITECTURE_DEPENDS_ON_IT: This decision dictates the infrastructure boundary. If removed, the system cannot verify compliance or data integrity.
FAILURE_IF_REMOVED: Leads to system crash, transaction data corruption, or account suspension under SEBI rules.
DEPENDENT_ADRS: None
EVIDENCE_STRENGTH: STRONG
CONFIDENCE: High
STATUS: KEEP

---

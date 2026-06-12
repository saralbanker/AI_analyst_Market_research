# 03 Merge Candidate Registry

**Objective:** Verify potential duplicate decisions and evaluate them for merging strictly based on identical constraints.

## 1. Candidate Merge List

*No merge candidates identified that satisfy the complete identity rules.*

## 2. Merge Evaluation Log

### Case 1: ADR-072 (Human Oversight Alert Fatigue) vs. ADR-109 (Reliability Alert Fatigue)
- **SOURCE_ADRS:** ADR-072, ADR-109
- **MERGE_JUSTIFICATION:** Kept separate. Although they share the same title, ADR-072 focuses on Human Oversight limits and operator intervention, whereas ADR-109 focuses on Reliability failures, system availability, and daemon behavior. Their unresolved failure modes, validation requirements, and risk levels differ.
- **CONFIDENCE:** HIGH

### Case 2: ADR-001 (Embedded zero-copy database selection) vs. ADR-003 (Hive-partitioned storage format)
- **SOURCE_ADRS:** ADR-001, ADR-003
- **MERGE_JUSTIFICATION:** Kept separate. ADR-001 is a database type decision (DuckDB + SQLite hybrid vs. Vector DBs), while ADR-003 is a storage format schema design decision (Hive-partitioned Parquet vs. JSON lakes). Rationale and consequences differ.
- **CONFIDENCE:** HIGH

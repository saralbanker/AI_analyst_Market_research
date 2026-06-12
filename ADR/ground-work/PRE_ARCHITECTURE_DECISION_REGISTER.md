# Pre-Architecture Decision Register
**Target:** Owner Authority

This register lists all items that require an explicit Owner Decision or SADR modification before Architecture Design can safely begin.

## 1. Owner Decisions Required

### ODR-PRE-01: Disagreement Evaluation Protocol Format
*   **Context:** SDM-10 Rule 4 dictates a "case-by-case evaluation protocol" when the human overrides the system.
*   **Decision Required:** Must this protocol enforce structured taxonomy (e.g., predefined categories of override reasons for automated attribution tracking) or unstructured input (e.g., free text / simple acknowledgment)?
*   **Architectural Implication:** Dictates UI design, database schema for attribution logs, and analytics processing complexity.

## 2. Missing Capabilities to be Derived

### GAP-PRE-01: System Orchestration & Activation
*   **Context:** SDM-CONST-15 defines Scheduled, On-Demand, and Event-Driven activations.
*   **Action Required:** SADR_V1 must be updated to derive a capability (e.g., `CAP-16 System Orchestrator`) that handles cron-schedules, event-listeners, and API triggers to awaken the analytical chains.

### GAP-PRE-02: Real-World Portfolio State Ingestion
*   **Context:** SDM-11, SDM-13, and SDM-15 require actual drawdown and execution prices to function. Since the system cannot execute trades, the recommended state is disjointed from the real-world state.
*   **Action Required:** SADR_V1 must be updated to derive a capability (e.g., `CAP-17 Portfolio State Reconciliation`) that handles ingesting actual broker state or human-entered execution data.

## 3. Validation Blockers Required for Architecture

### VAL-BLK-01: Multi-Account Scope (VAL-09, VAL-12, VAL-16)
*   **Context:** These items mention "across multiple independent accounts."
*   **Action Required:** The Owner or Validation Authority must definitively confirm whether the initial architecture must be strictly designed to support multiple independent accounts, or if a single-account architecture is permitted for V1.
*   **Architectural Implication:** Affects all database relations, state management layers, and API designs.

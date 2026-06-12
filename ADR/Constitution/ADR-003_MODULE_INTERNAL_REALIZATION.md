# ADR-003 — MODULE INTERNAL REALIZATION

**Decision Type:** Internal Architecture Realization
**Method:** 4D+ Evidence-Bound Investigation (8 mandatory investigations)
**Authority Hierarchy:**
- Level 1: SDM_V2.3 (FROZEN)
- Level 2: VAL05_OWNER_DECISION_RESOLUTION (RESOLVED)
- Level 3: SADR_V2.1 (CERTIFIED)
- Level 4: ARCHITECTURE_FOUNDATION_V1
- Level 5: ADR-000_ARCHITECTURE_PRINCIPLES
- Level 6: ADR-001_ARCHITECTURAL_STYLE_SELECTION
- Level 7: ADR-002_CAPABILITY_TO_MODULE_REALIZATION

**Status:** CANDIDATE FOR OWNER REVIEW
**Scope:** Determines how each module internally realizes its capabilities — capability ordering, internal information flow, state ownership, and invariants. Does not define software, APIs, databases, deployment, or implementation.

---

## SECTION 01 — INTERNAL REALIZATION METHODOLOGY

### 1.1 Realization vs. Design Distinction

ADR-003 answers: *how does each module internally operate?*
ADR-003 does not answer: *how is the module implemented?*

**Evidence:** ADR-003 protocol: "Your responsibility is to determine how already-approved modules internally realize their responsibilities while remaining constitutionally compliant."

These are distinct questions. A module's internal realization describes:
- The ordering relationship among its owned capabilities
- What information passes between those capabilities within the module
- What state the module holds authority over
- What invariants must hold throughout its operation

A module's implementation describes specific technology choices, data structures, programming constructs, and deployment mechanisms. ADR-003 addresses the former. The latter belongs to a later phase.

### 1.2 Evidence Sources for Internal Realization

Internal realization is not invented. It is derived from SADR capability specifications, which already define for each capability:
- Its inputs (from where; what class)
- Its outputs (to where; what class)
- Its boundary (what it does; what it explicitly does not do)
- Its constitutional constraints (invariants that must hold)

The ordering of capabilities within a module is determinable from the SADR dependency chain (Section 5) — capabilities that receive from others within the same module come after them.

### 1.3 Technology-Neutral Expressions

All internal realization descriptions use capability-level language:
- "CAP-X receives from CAP-Y" — not "calls an API"
- "CAP-X produces information class Z" — not "writes to a table"
- "CAP-X holds authoritative state" — not "persists to a database"
- "CAP-X blocks downstream until complete" — not "synchronous HTTP request"

---

## SECTION 02 — AUTHORITY-DERIVED INTERNAL ARCHITECTURE CONSTRAINTS

Extracted from authority. These constrain every module's internal realization.

| Constraint ID | Constraint | Authority |
|--------------|------------|-----------|
| IAC-01 | Internal capability ordering must respect the SADR dependency chain — a capability may not receive information from a capability that is downstream of it in the same chain | SADR Section 5; ADR-000 P-10 |
| IAC-02 | No capability may receive unverified data — CAP-02's output is the gate that clears data for consumption by all downstream capabilities | SADR CONSTRAINT; SDM-02 Rule 2 |
| IAC-03 | No capability may receive unvalidated signals for confidence computation — CAP-10's output is the gate that clears signals for CAP-12 | SADR Section 5; SDM-05 Rule 2 |
| IAC-04 | Every capability must produce its audit record as part of its output — audit receipt is not optional | SDM-02 through SDM-15 Audit clauses; CAP-30 necessity |
| IAC-05 | Within MOD-05: confidence computation (CAP-12) is derived exclusively from technical evidence and statistical validation — the supplementary signal set does not enter this computation | GOV-VAL05 Rule 1; SADR_AMENDMENT_VAL-05 |
| IAC-06 | Within MOD-05: the conflict flag from CAP-09 annotates the confidence score output but does not modify the score value | SADR_AMENDMENT_VAL-05; AF DOM-03 GOV-VAL05 Boundary |
| IAC-07 | Within MOD-06: each halt-state capability (CAP-24, CAP-25, CAP-26, CAP-27) maintains independent state — no shared state variable, shared trigger, or shared exit logic crosses between them | SDM-CONST-14; ADR-000 P-06; ADR-002 FORB-10 |
| IAC-08 | Within MOD-06: detection capabilities (CAP-19, CAP-23, CAP-31) must continue operating regardless of which halt states are active — monitoring does not halt | AF 6.1; GOV-02 Rule 3; SDM-15 Rule 14 |
| IAC-09 | Within MOD-07: the complete advisory package must be assembled before presentation — the human must receive all sections simultaneously as an Open Menu | SDM-08 Rule 8; CONSTRAINT-09; CAP-18 Boundary |
| IAC-10 | Within MOD-08: observation inputs are post-gate and read-only — MOD-08 has no write path back to any recommendation or governance capability | SDM-13 Rules 8, 10; ADR-002 FORB-01 |
| IAC-11 | Within MOD-10: every record received is immutable from the moment of receipt — no capability within MOD-10 modifies a received record | SADR CHANGE-06; ADR-000 P-07 |
| IAC-12 | Within MOD-11: activation produces an initiation signal only — it does not own the execution of what is initiated, does not track cycle progress, and does not govern outcomes | AF 5.3; SDM-CONST-15 |
| IAC-13 | Open validation items that affect internal capability computation (VAL-01, VAL-02, VAL-03, etc.) must be treated as extension interfaces within the affected capability — the architecture assumes the interface, not the formula | SADR Section 11 CLASS_B/C/D; SDM-CONST-12 |

---

## SECTION 03 — MODULE INTERNAL REALIZATION

---

### MOD-01 | Market Data Foundation — Internal Realization

**Purpose:** Produce the verified, adjusted, eligible, survivorship-bias-corrected market dataset and block all downstream modules until that dataset exists.

**Internal Responsibilities:**
- Receive raw market data from at least two independent external sources
- Verify data cross-references and detect mismatches before any downstream consumption
- Apply corporate action adjustments to produce split-adjusted data
- Enforce universe eligibility to produce the eligible equity set
- Correct historical datasets for survivorship bias

**Capability Ordering:**

```
CAP-01 (Market Data Ingestion)
  └─▶ CAP-02 (Data Cross-Verification) ← BLOCKING GATE
        └─▶ CAP-03 (Corporate Action Adjustment)
              └─▶ CAP-04 (Universe Eligibility Enforcement)
                    └─▶ [eligible, adjusted data → downstream modules]

CAP-01 (historical data stream)
  └─▶ CAP-14 (Survivorship Bias Correction)
        └─▶ [bias-corrected history → CAP-13 in MOD-05]
```

**Ordering Evidence:** SADR Section 5 dependency chain; CAP-02 BOUNDARY ("does not adjust data — CAP-03"); CAP-03 BOUNDARY ("does not verify sources — CAP-02; does not determine eligibility — CAP-04"); CAP-04 BOUNDARY ("does not verify — CAP-02; does not adjust — CAP-03").

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| External sources | CAP-01 | Raw OHLCV data (two+ sources) | Ingestion only; no processing |
| CAP-01 | CAP-02 | Raw data (two+ sources for same data point) | Cross-reference verification; mismatch flagging |
| CAP-02 | CAP-03 | Verified data | Corporate action adjustment applied |
| CAP-03 | CAP-04 | Split-adjusted, verified data | Eligibility determination; exclusion logging |
| CAP-01 (historical) | CAP-14 | Historical dataset with delisted equities | Survivorship bias correction |
| CAP-04 | Downstream modules | Eligible equity set | No further transformation within MOD-01 |
| CAP-14 | MOD-05 (CAP-13) | Bias-corrected historical dataset | No further transformation within MOD-01 |

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Raw inbound data buffers | CAP-01 | Transient — consumed by CAP-02; not retained |
| Cross-verification match/mismatch records | CAP-02 | Authoritative — produced for audit and downstream gate |
| Adjustment audit records; rejection records | CAP-03 | Authoritative — produced for audit |
| Eligible equity set; exclusion log | CAP-04 | Authoritative — definitive universe for this cycle |
| Bias-corrected historical dataset | CAP-14 | Authoritative — consumed by CAP-13 across cycles |

**Invariants:**
- CAP-02 must complete before CAP-03 may receive data (IAC-02; IAC-03)
- CAP-02's output is the only cleared path for data to reach MOD-03, MOD-04, MOD-05 — no shortcut exists
- Unadjusted split data must be rejected by CAP-03 before it can reach CAP-04 (SDM-02 Rule 3)
- Delisted equities must be present in the historical dataset that reaches CAP-14 (SDM-02 Rule 1)

---

### MOD-02 | Market Context — Internal Realization

**Purpose:** Classify the market environment, detect drift, and emit the condition signals that other modules are constitutionally required to consume.

**Internal Responsibilities:**
- Classify current market regime from verified, eligible market data
- Detect concept drift relative to historical baselines
- Emit: broad market trend filter state, regime context, non-ergodic condition signal, drift alerts

**Capability Ordering:**

```
[Verified data from MOD-01]
  └─▶ CAP-05 (Market Regime Classification)
        └─▶ CAP-06 (Concept Drift Detection)
              └─▶ [drift metrics, alerts → MOD-10]

CAP-05 outputs flow to:
  MOD-03 (trend filter + regime context → CAP-07)
  MOD-05 (regime context → CAP-13)
  MOD-06 (non-ergodic condition signal → CAP-23, CAP-27)
```

**Ordering Evidence:** SADR CAP-06 INPUTS: "Current model behavior metrics. Historical model behavior baselines. Regime classification from CAP-05." — CAP-06 depends on CAP-05's output; CAP-05 is initiating.

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| MOD-01 | CAP-05 | Eligible, verified, adjusted market data | Regime classification computation |
| CAP-05 | CAP-06 | Regime classification (current + historical) | Drift detection against baseline |
| CAP-05 | MOD-03/MOD-05/MOD-06 | Trend filter state; regime context; non-ergodic condition signal | Output only — no further transformation within MOD-02 |
| CAP-06 | MOD-10 | Drift metrics; model anchoring detection events | Terminal — output to audit |

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Current regime classification | CAP-05 | Authoritative — constitutionally required output for this cycle |
| Walk-forward cross-validation bounds | CAP-05 | Authoritative — produced for audit |
| Non-ergodic condition signal | CAP-05 | Authoritative — generic interface per VAL-03/VAL-17 CLASS_B |
| Concept drift metrics; stability baselines | CAP-06 | Authoritative — delta against historical baselines |
| Model anchoring detection events | CAP-06 | Authoritative — produced for audit and human visibility |

**Invariants:**
- CAP-06 may only execute after CAP-05 produces a current regime classification
- Walk-forward validation bounds are produced by CAP-05 for audit — they are never consumed computationally by CAP-06 (CAP-06 uses them as a baseline reference, not as a computational input that modifies its own classification)
- The non-ergodic condition signal is a generic condition-signal interface — consumers depend on the interface; the internal mathematical derivation is an extension point (VAL-03/VAL-17 CLASS_B)

---

### MOD-03 | Evidence Generation — Internal Realization

**Purpose:** Generate the two constitutional evidence layers and detect and characterize conflicts between them. The supplementary signal set is advisory only and routes to the human-facing advisory report, not to computation.

**Internal Responsibilities:**
- Generate technical signal set from eligible data and market context
- Intake supplementary signals (news, earnings surprises, insider buying)
- Evaluate and characterize conflicts between technical and supplementary evidence
- Route: technical signals → MOD-04; conflict flags → MOD-05 as annotation; supplementary signals → MOD-07 advisory report

**Capability Ordering:**

```
[Verified data from MOD-01]
[Trend filter + regime context from MOD-02]
  └─▶ CAP-07 (Technical Signal Generation)
        └─▶ MOD-04 (validation)

[News, earnings, insider data from external sources]
  └─▶ CAP-08 (Supplementary Signal Intake)
        └─▶ CAP-09 (Technical-News Conflict Evaluation) ← SHARED_AUTHORITY
              ├─▶ [conflict flag annotation → MOD-05 CAP-12]
              └─▶ [supplementary signal set → MOD-07 advisory report]
```

**Ordering Evidence:** SADR CAP-09 INPUTS: "Technical signals from CAP-07. Supplementary signals from CAP-08." — CAP-09 depends on both; CAP-07 and CAP-08 are parallel initiating capabilities; CAP-09 is terminal within MOD-03.

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| MOD-01 | CAP-07 | Eligible, adjusted market data | Technical signal generation |
| MOD-02 | CAP-07 | Trend filter state; regime context | Applied as context to signal generation |
| External news/event sources | CAP-08 | News data; earnings events; insider events | Classification and reliability metadata tagging |
| CAP-07 | CAP-09 | Technical signal set | Input for conflict evaluation only |
| CAP-08 | CAP-09 | Supplementary signal set with reliability metadata | Input for conflict evaluation only |
| CAP-09 | MOD-05 (CAP-12) | Conflict flag (annotation only) | Marks the scored opportunity; does not modify score value |
| CAP-08 | MOD-07 | Full supplementary signal set | Routes to human-facing advisory section (GOV-VAL05 Rule 4) |
| CAP-07 | MOD-04 | Technical signal set | Routes to statistical validation |

**GOV-VAL05 Routing Invariant (binding on all CAP-08 output paths):**
The supplementary signal set produced by CAP-08 has two permitted destinations within MOD-03:
1. CAP-09 (for conflict detection only — CAP-09 produces a conflict flag, not a computed score modification)
2. MOD-07 advisory report (as a named advisory section per GOV-VAL05 Rule 4)

It has zero permitted routing to MOD-05 computation (CAP-12, CAP-13, CAP-15, CAP-16).

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Technical signal set with evidence metadata | CAP-07 | Authoritative — primary evidence layer |
| Supplementary signal set with reliability metadata | CAP-08 | Authoritative — advisory evidence layer |
| Conflict flags; evidence characterization; resolution rationale | CAP-09 | Authoritative — advisory annotation produced for human visibility |

**Invariants:**
- CAP-07 and CAP-08 are independent — they do not depend on each other's outputs; they may proceed in parallel
- CAP-09 must receive from both CAP-07 and CAP-08 before producing a conflict flag
- Technical evidence takes strict priority — CAP-09's conflict flag marks the fact of disagreement; it does not override technical evidence
- Analyst rating changes and social media sentiment are excluded or given minimal weight at CAP-08 intake (SDM-04 Rule 6) — not at CAP-09
- AI evaluations (sentiment model outputs) are isolated to the semantic and cognitive domain within CAP-08 (SDM-04 Rule 12) — they do not cross into computation

---

### MOD-04 | Statistical Validation — Internal Realization

**Purpose:** Verify statistical edge and temporal integrity of candidate signals. CAP-10 is a constitutional blocking gate — confidence scoring may not proceed until this module produces validated signals.

**Internal Responsibilities:**
- Apply walk-forward validation to candidate technical signals
- Measure statistical edge, stability, and outlier behavior
- Produce: validated signal set with statistical evidence; rejected signals with rejection basis

**Capability Ordering:**

```
[Technical signals from MOD-03 CAP-07]
  └─▶ CAP-10 (Walk-Forward Signal Validation) ← BLOCKING GATE
        └─▶ CAP-11 (Statistical Edge Verification)
              └─▶ [validated signal set → MOD-05 CAP-12]
```

**Ordering Evidence:** SADR CAP-11 INPUTS: "Walk-forward validated signals from CAP-10." — CAP-11 depends on CAP-10; CAP-10 is initiating; CAP-11 is terminal.

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| MOD-03 (CAP-07) | CAP-10 | Technical signal candidates; historical data with temporal ordering | Walk-forward temporal validation |
| MOD-01 | CAP-10 | Historical data (temporal ordering preserved) | Provides the out-of-sample window for walk-forward validation |
| CAP-10 | CAP-11 | Walk-forward validated signal set; validation scores | Statistical edge verification against validated signals only |
| CAP-11 | MOD-05 (CAP-12) | Validated signal set with edge verdicts and stability indexes | No further transformation within MOD-04 |

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Walk-forward validation results and scores | CAP-10 | Authoritative — blocking gate output |
| Rejected signals with rejection basis | CAP-10 | Authoritative — produced for audit |
| Statistical edge verdicts; deflated return metrics; t-stat results | CAP-11 | Authoritative — edge evidence |
| Stability index values; outlier detection verification records | CAP-11 | Authoritative — stability evidence |

**Invariants:**
- K-fold cross-validation is constitutionally prohibited — CAP-10 uses walk-forward validation exclusively (CONSTRAINT-08)
- CAP-11 may only execute on signals that have passed CAP-10's validation — no shortcut to CAP-11 exists
- Data smoothing may not mask structural market anomalies within CAP-11's edge computation (SDM-05 Rule 7)
- Outlier detectors must be verified through synthetic anomaly injection (SDM-05 Rule 6)

---

### MOD-05 | Recommendation Synthesis — Internal Realization

**Purpose:** Transform validated technical evidence and portfolio state into the complete advisory recommendation package. This module is the subject of Investigation 04 (dedicated deep analysis in Section 05).

**Internal Responsibilities:**
- Compute confidence scores from validated signals (technical-only; sentiment excluded from computation)
- Compute probability-adjusted expected value bounded by 5% drawdown constraint
- Rank opportunities by highest probability; target 3–5 positions
- Produce conviction-weighted allocation suggestions (equal-weighting prohibited)
- Declare null-state explicitly when no opportunities qualify
- Produce exit condition recommendations for open positions

**Capability Ordering:**

```
[Validated signals from MOD-04 CAP-11]
[Conflict flag annotation from MOD-03 CAP-09]
  └─▶ CAP-12 (Confidence Scoring)
        └─▶ CAP-13 (Expected Value Computation) ← also receives from MOD-01, MOD-02, MOD-09
              └─▶ CAP-15 (Opportunity Ranking) ← also receives from MOD-09
                    ├─▶ CAP-16 (Conviction-Weighted Allocation) ← also receives from MOD-09
                    │
                    └─▶ [null-state trigger → CAP-17 if no opportunities qualify]
                          └─▶ CAP-17 (Null-State Declaration)

[Open position data + technical/supplementary signals + portfolio state]
  └─▶ CAP-20 (Exit Condition Recommendation)

All outputs → CAP-18 (MOD-07)
```

**Ordering Evidence:** SADR Section 5 dependency chain: CAP-12 → CAP-13 → CAP-15 → CAP-16/CAP-17 sequential. SADR CAP-13 INPUTS: "Confidence-scored opportunities from CAP-12." SADR CAP-16 INPUTS: "Ranked opportunities from CAP-15 with confidence scores from CAP-12." SADR CAP-17 INPUTS: "Null-state trigger from CAP-15."

**State Ownership:** See Section 05 (MOD-05 Deep Analysis).

**Invariants:** See Section 05.

---

### MOD-06 | Risk & Governance Enforcement — Internal Realization

**Purpose:** Detect risk and governance conditions, maintain the four independent halt states, and gate recommendation issuance accordingly. This module is the subject of Investigation 05 (dedicated deep analysis in Section 06).

**Internal Responsibilities:**
- Monitor position and concentration limits continuously (CAP-19)
- Monitor market-condition circuit breakers continuously (CAP-23)
- Monitor governance compliance continuously (CAP-31)
- Manage Governance Halt state independently (CAP-25)
- Manage Governance Lockout state independently (CAP-26)
- Manage Conditional Suspension state independently (CAP-27)
- Manage Hard Deterministic Halt state independently (CAP-24)
- Gate MOD-05 recommendation issuance when any blocking halt state is active

**Capability Ordering:** See Section 06 (MOD-06 Deep Analysis).

**State Ownership:** See Section 06.

**Invariants:** See Section 06.

---

### MOD-07 | Human Decision Authority — Internal Realization

**Purpose:** Assemble the complete advisory package and present it simultaneously to the human as an Open Menu. Hold and capture the human's decision.

**Internal Responsibilities:**
- Receive all advisory package sections from their owning modules
- Assemble the composite advisory view (ownership of each section never transfers)
- Present all EV-filtered opportunities simultaneously to the human — Open Menu constraint
- Hold the gate: system halts and awaits explicit human authorization before any trade action
- Capture: human approval decision; override parameters; secondary authorizations

**Capability Ordering:**

```
[From MOD-05: rankings, allocations, confidence scores, EV, risk summaries, exit suggestions, null-state]
[From MOD-03: supplementary signal advisory section, conflict flags]
[From MOD-06: active halt state flags]
[From MOD-09: current drawdown status]
  └─▶ CAP-18 (Human Approval Gate) — assembly + presentation + capture
        └─▶ [Human decision → MOD-08 post-gate observation]
        └─▶ [Human decision → MOD-09 state update pathway]
        └─▶ [Human decision → MOD-10 immutable record]
```

**Ordering Evidence:** SADR CAP-18 INPUTS: all sections listed. CAP-18 BOUNDARY: "Presentation and authorization gateway. System presents; human decides." — CAP-18 is the sole capability; no internal ordering needed.

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| MOD-05 | CAP-18 | Ranked opportunities, allocations, confidence scores, EV, risk summaries, exit suggestions, null-state | Assembled into advisory view (no transformation of content) |
| MOD-03 | CAP-18 | Named supplementary/sentiment advisory section (distinct); conflict flags | Assembled as named distinct section (GOV-VAL05 Rule 4) |
| MOD-06 | CAP-18 | Active halt state flags | Displayed to human before decision |
| MOD-09 | CAP-18 | Current drawdown vs. 5% tolerance | Displayed to human before decision |
| CAP-18 | Human | Complete simultaneous Open Menu advisory package | Presented — system authority ends here |
| Human | CAP-18 | Approval / rejection / override / secondary authorization | Captured — decision authority is entirely human |

**Advisory Package Assembly Constraint:**
The advisory package is a composite view. Ownership of each section never transfers to MOD-07 at composition. MOD-07 owns the act of assembly and the captured human decision; the constituent sections remain owned by their originating modules.

**Evidence:** AF 4.1 Report Ownership: "Ownership of each section never transfers at composition; the assembled report is a view, not a new information class."

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Human approval decisions | CAP-18 | Authoritative — captured decisions for downstream provision |
| Human override parameters | CAP-18 | Authoritative — parameters that modify the approved trade |
| Case-by-case evaluation triggers | CAP-18 | Authoritative — triggers for disagreement protocol |
| Secondary authorization events | CAP-18 | Authoritative — for pricing limit modifications |

**Invariants:**
- All sections of the advisory package must be assembled before presentation — partial presentation is a constitutional violation (CONSTRAINT-09; SDM-10 Human Visibility)
- All EV-filtered, positively-ranked opportunities must be presented simultaneously — sequential forced selection is prohibited (SDM-08 Rule 8)
- No timeout-based auto-approval mechanism exists — the gate is held open until explicit human action (CAP-18 Boundary)
- No bypass pathway exists — CAP-18 is the sole constitutional blocking gate for trade action (SADR Section 5)
- Case-by-case evaluation is triggered when human decision conflicts with system recommendation (SDM-10 Rule 4) — the conflict is surfaced, not suppressed
- Pricing limit modifications require secondary authorization (SDM-10 Rule 5) — not covered by the primary approval

---

### MOD-08 | Attribution — Internal Realization

**Purpose:** Observe decision quality. Maintain System Alpha and Human Override Delta as distinct layers. Report to human. Zero write authority over anything.

**Internal Responsibilities:**
- Receive system recommendations and human decisions from MOD-07 (post-gate, read-only)
- Observe accepted and rejected opportunities
- Compute System Alpha (Baseline) layer — system recommendations vs. outcomes
- Compute Human Override Delta (Human Alpha/Bleed) — delta between system recommendation and human action
- Produce attribution reports, insights, warnings for human review

**Capability Ordering:**

```
[Post-gate from MOD-07: system recommendations (pre-decision) + human actions (post-decision)]
[Post-trade outcomes (external)]
[Market outcomes for rejected opportunities (from MOD-01/MOD-02 data)]
  └─▶ CAP-21 (Attribution Observation)
        └─▶ [System Alpha layer → human review + MOD-10]

[System recommendations pre-decision + Human actions post-decision from MOD-07]
  └─▶ CAP-22 (Human Override Delta Tracking)
        └─▶ [Human Override Delta layer → human review + MOD-10]
```

**Ordering Evidence:** SADR CAP-21 and CAP-22 are described as parallel — CAP-21 tracks system outcomes vs. market; CAP-22 tracks human action vs. system recommendation. Both receive from the MOD-07 post-gate observation point. Their outputs are distinct layers that must not be merged (SDM-13 Rule 5).

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| MOD-07 (post-gate) | CAP-21 | System recommendations (accepted + rejected); post-trade market outcomes | System Alpha computation — outcomes vs. system baseline |
| MOD-07 (post-gate) | CAP-22 | System recommendation (pre-decision); human action (post-decision) | Delta computation — system vs. human |
| CAP-21 | Human | Attribution reports; System Alpha insights; warnings | Read-only provision for human judgment |
| CAP-22 | Human | Human Override Delta; edge analysis | Read-only provision for human judgment |
| CAP-21 | MOD-10 | Attribution event records | Terminal — no further transformation |
| CAP-22 | MOD-10 | Human override delta records | Terminal — no further transformation |

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| System Alpha (Baseline) layer | CAP-21 | Authoritative — observation record |
| Theoretical expectancy records for rejected opportunities | CAP-21 | Authoritative — counterfactual tracking |
| Tracking metadata (setup type, regime context, holding duration) | CAP-21 | Authoritative — required per SDM-13 Rule 2 |
| Human Override Delta (Human Alpha/Bleed) layer | CAP-22 | Authoritative — distinct from System Alpha (SDM-13 Rule 5) |
| Edge analysis (whether human intervention adds value or destroys edge) | CAP-22 | Authoritative — derived metric |

**Read-Only Constraint (total):**
CAP-21 and CAP-22 are observational only. Their outputs are available for human review and for MOD-10 audit only. Under no circumstances do their outputs flow to MOD-01, MOD-02, MOD-03, MOD-04, MOD-05, or MOD-06. Any behavior change motivated by attribution findings requires explicit human approval through a constitutionally authorized change process — not through an automated internal path.

**Invariants:**
- System Alpha and Human Override Delta are maintained as distinct, non-merged layers (SDM-13 Rule 5) — CAP-21 and CAP-22 must not share a combined output
- Theoretical expectancy is tracked for rejected opportunities as well as accepted ones — this prevents survivorship bias in the attribution loop (SDM-13 Rule 3)
- Attribution metadata (setup type, market regime context, holding duration) is required for every tracked opportunity (SDM-13 Rule 2)

---

### MOD-09 | Portfolio State — Internal Realization

**Purpose:** Maintain and provide the single authoritative representation of portfolio state, sourced exclusively from human-confirmed trade actions.

**Internal Responsibilities:**
- Receive human-confirmed trade actions from the authoritative external execution record
- Maintain: active position count, drawdown level, concentration status, illiquidity metrics
- Provide portfolio state to all constitutionally entitled consuming modules

**Capability Ordering:**

```
[Authoritative external execution record (human-confirmed trades)]
  └─▶ CAP-29 (Portfolio State Visibility)
        └─▶ [portfolio state → MOD-05 (CAP-13, 15, 16, 20)]
        └─▶ [portfolio state → MOD-06 (CAP-19, 25, 31)]
        └─▶ [drawdown status → MOD-07 (CAP-18 display)]
        └─▶ [state → MOD-10 (audit)]
```

**Ordering Evidence:** CAP-29 is a single capability. There is no internal ordering challenge. The ordering question is: what is CAP-29's input sequencing? Inputs arrive from the external execution record. CAP-29 updates authoritative state when confirmed trade actions arrive.

**Internal Information Flow:**

| From | To | Information Class | Transformation |
|------|----|------------------|----------------|
| Authoritative external execution record | CAP-29 | Confirmed trade actions | State reconciliation and update |
| CAP-29 | MOD-05 (CAP-13, 15, 16, 20) | Portfolio state (position count, drawdown, concentration, illiquidity) | No transformation — provision of authoritative state |
| CAP-29 | MOD-06 (CAP-19, CAP-25, CAP-31) | Portfolio state relevant to each capability's detection function | No transformation — provision of authoritative state |
| CAP-29 | MOD-07 (CAP-18) | Current drawdown level vs. 5% tolerance | Displayed to human at advisory gate |

**State Ownership:**

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Active position count | CAP-29 | Authoritative — single source |
| Current drawdown level vs. 5% tolerance | CAP-29 | Authoritative — single source |
| Position concentration status | CAP-29 | Authoritative — single source |
| Illiquidity metrics | CAP-29 | Authoritative — single source |

**Single-Source Invariant (ADR-000 P-05, ADR-002 FORB-07):**
No other module may maintain a private copy of portfolio state that other modules then consume. Consumers must read from CAP-29. Any module that derives a metric from portfolio state (e.g., a remaining capital figure) owns that derived metric as a transient computation for its own use only — it may not re-export it as portfolio state to other modules.

**Portfolio Write Authority:**
CAP-29 represents state; it does not originate it. The actual portfolio state originates from human-confirmed external execution. CAP-29 maintains the system's authoritative representation of that external reality.

**Evidence:** SADR CAP-29 INPUTS: "Trade actions confirmed by the human at CAP-18 (the only source of portfolio state changes, since the system never executes trades). Authoritative record of executed trade actions for state accuracy verification."

**Invariants:**
- Portfolio state updates only when human-confirmed trade actions arrive from the external execution record — not from recommendations, not from system hypotheses
- CAP-29 provides state; it does not evaluate state against governance rules (CAP-31 evaluates; CAP-29 provides) — this boundary was established by SADR CHANGE-01

---

### MOD-10 | Audit — Internal Realization

**Purpose:** Hold the immutable, terminal record of everything. Subject of Investigation 06 (dedicated deep analysis in Section 07).

**Internal Responsibilities:**
- Receive audit records from all 11 modules
- Write immutably — records may not be modified after receipt
- Produce no output to any other module
- Provide access for human review only

**Capability Ordering:** CAP-30 is a single capability. All inbound records arrive from other modules. There is no internal sequencing question — all paths lead to CAP-30, and no path leads out.

**State Ownership:** See Section 07 (MOD-10 Deep Analysis).

**Invariants:** See Section 07.

---

### MOD-11 | Activation — Internal Realization

**Purpose:** Initiate cycles under three authorized modes. Subject of Investigation 07 (dedicated deep analysis in Section 08).

**Internal Responsibilities:**
- Accept Mode 1 triggers (schedule)
- Accept Mode 2 triggers (human request)
- Accept Mode 3 triggers (governance/risk events from MOD-06)
- Emit activation initiation signal to all autonomous modules
- Record activation mode and initiated cycle for audit

**Capability Ordering:** CAP-28 is a single capability with three input types and one output type (activation initiation signal). There is no internal ordering question — triggers arrive, activation signal is emitted.

**State Ownership:** See Section 08 (MOD-11 Deep Analysis).

**Invariants:** See Section 08.

---

## SECTION 04 — CAPABILITY FLOW MAPS

### MOD-01 Flow

```
EXTERNAL: Market data (2+ sources)
  │
  ▼
CAP-01 [INGEST]
  ├── Raw data (source A)
  ├── Raw data (source B)
  └── Historical data with delisted equities
        │
        ├─▶ CAP-02 [VERIFY ← GATE] ─── mismatch records → MOD-10
        │     │
        │     ▼ (cleared data only)
        │   CAP-03 [ADJUST] ─── adjustment/rejection records → MOD-10
        │     │
        │     ▼
        │   CAP-04 [FILTER] ─── eligible set + exclusion log → downstream + MOD-10
        │
        └─▶ CAP-14 [BIAS-CORRECT] ─── bias-corrected history → MOD-05/CAP-13
```

### MOD-02 Flow

```
MOD-01 → CAP-05 [CLASSIFY REGIME]
  ├── trend filter state → MOD-03/CAP-07
  ├── regime context → MOD-05/CAP-13
  ├── non-ergodic condition signal → MOD-06/CAP-23, CAP-27
  └─▶ CAP-06 [DETECT DRIFT] ─── drift metrics → MOD-10; alerts → human
```

### MOD-03 Flow

```
MOD-01 + MOD-02 → CAP-07 [GENERATE TECHNICAL SIGNALS] → MOD-04
EXTERNAL news/events → CAP-08 [INTAKE SUPPLEMENTARY] → CAP-09 + MOD-07 advisory

CAP-07 + CAP-08 → CAP-09 [EVALUATE CONFLICTS / SHARED_AUTHORITY]
  ├── conflict flag (annotation only) → MOD-05/CAP-12
  └── supplementary signal set → MOD-07 advisory package
```

### MOD-04 Flow

```
MOD-03/CAP-07 → CAP-10 [WALK-FORWARD VALIDATE ← GATE]
  └─▶ CAP-11 [VERIFY STATISTICAL EDGE]
        └── validated signals + edge verdicts → MOD-05/CAP-12
        └── rejected signals + evidence → MOD-10
```

### MOD-05 Flow

```
MOD-04/CAP-11 ──────────────────────────▶ CAP-12 [CONFIDENCE SCORING]
MOD-03/CAP-09 (annotation only) ────────▶ CAP-12 (flags scored opp, does not modify score)
[No supplementary signals enter CAP-12]
  │
  ▼
CAP-12 output: confidence score per opportunity + conflict annotations
  │
  ▼
CAP-13 [EXPECTED VALUE] ← also: MOD-01/CAP-14, MOD-02/CAP-05, MOD-09/CAP-29
  │
  ├── EV-filtered set → CAP-15
  └── cash-holding signal → CAP-17 (if all fail EV threshold)
        │
        ▼
CAP-15 [RANK] ← also: MOD-09/CAP-29 (position count)
  ├── ranked list → CAP-16
  └── null-state trigger → CAP-17 (if no opportunities survive ranking)

CAP-16 [ALLOCATE - CONVICTION WEIGHTED] ← also: MOD-09/CAP-29
  └── allocation suggestions → MOD-07/CAP-18

CAP-17 [DECLARE NULL-STATE] → MOD-07/CAP-18

MOD-09/CAP-29 + technical/supplementary signals on open positions
  └─▶ CAP-20 [EXIT RECOMMENDATIONS] → MOD-07/CAP-18

All CAP-05 outputs also available as context to CAP-15, CAP-16 (regime-aware ranking and allocation)
```

### MOD-06 Flow

```
Detection capabilities (continuous, not halted by halt states):

MOD-09/CAP-29 ──▶ CAP-19 [POSITION LIMIT ENFORCEMENT]
  ├── hard halt trigger → CAP-24
  ├── scaling signal → MOD-05/CAP-16
  └── compliance status → MOD-10

MOD-02/CAP-05 + market metrics ──▶ CAP-23 [CIRCUIT BREAKER ENFORCEMENT]
  ├── suspension signals → CAP-27
  ├── scaling signals → MOD-05/CAP-15, CAP-16
  └── margin signals → MOD-10

MOD-09/CAP-29 ──▶ CAP-31 [GOVERNANCE COMPLIANCE MONITOR]
  ├── violation signal → CAP-26 (entry trigger)
  └── restoration signal → CAP-26 (exit trigger)

Halt-state management (independent):

CAP-19 trigger ──▶ CAP-24 [HARD HALT - STATE 4]
  └── active flag + block on breaching recs → MOD-05 gating

MOD-09/CAP-29 drawdown ──▶ CAP-25 [GOVERNANCE HALT - STATE 1]
  └── active flag + block on all recs → MOD-05 gating + escalation report → MOD-07

CAP-31 violation/restoration ──▶ CAP-26 [GOVERNANCE LOCKOUT - STATE 2]
  └── active flag + block on all recs + allocation + deployment → MOD-05 gating

CAP-23 signals ──▶ CAP-27 [CONDITIONAL SUSPENSION - STATE 3]
  └── active flag + scaled/suspended affected-domain recs → MOD-05 gating

All halt state flags + condition records → MOD-07/CAP-18 display
All halt events (entry/exit with condition state) → MOD-10
Governance events → MOD-11 (Mode 3 event-driven activation trigger)
```

### MOD-07 Flow

```
[All advisory sections assembled]:
MOD-05 (rankings, allocations, confidence, EV, risk, exit, null-state)
MOD-03 (supplementary advisory section + conflict flags)
MOD-06 (active halt state flags)
MOD-09 (drawdown status)
  │
  ▼
CAP-18 [HUMAN APPROVAL GATE ← BLOCKING GATE]
  Simultaneous Open Menu presentation
  System halts and awaits human decision
  │
  ├── Human approval/rejection/override → MOD-08 (post-gate read-only)
  ├── Human confirmation → MOD-09 (state update pathway)
  └── All decisions → MOD-10 (immutable record)
```

### MOD-08 Flow

```
MOD-07 post-gate:
  System recommendations (pre-decision) ──▶ CAP-22 [OVERRIDE DELTA]
  Human actions (post-decision) ──────────▶ CAP-22
  
  System recs + market outcomes ──▶ CAP-21 [ATTRIBUTION OBSERVATION]
  Rejected opportunities + market outcomes ──▶ CAP-21
  
CAP-21 ──▶ Human (reports, insights, warnings) + MOD-10
CAP-22 ──▶ Human (delta analysis) + MOD-10

[NO outbound edges to MOD-01 through MOD-06]
```

### MOD-09 Flow

```
External execution record (human-confirmed trades)
  │
  ▼
CAP-29 [MAINTAIN PORTFOLIO STATE]
  ├── position count + drawdown + concentration + illiquidity → MOD-05
  ├── portfolio state → MOD-06 (CAP-19, CAP-25, CAP-31)
  ├── drawdown status → MOD-07 (CAP-18 display)
  └── state records → MOD-10
```

### MOD-10 Flow

```
ALL modules ──▶ CAP-30 [IMMUTABLE AUDIT LOG]
                          │
                          ▼
                    [No outbound edges]
                    Human review access only
```

### MOD-11 Flow

```
Mode 1 trigger (schedule) ──────────────┐
Mode 2 trigger (human request) ─────────┼──▶ CAP-28 [ACTIVATION]
Mode 3 trigger (MOD-06 governance event) ─┘         │
                                                     ▼
                                     Activation initiation signal
                                     (initiation only; not orchestration)
                                     ──▶ All autonomous modules
                                     ──▶ MOD-10 (activation mode record)
```

---

## SECTION 05 — MOD-05 INTERNAL REALIZATION (DEEP ANALYSIS)

### 5.1 The Computational Chain and Its Constitutional Constraints

MOD-05 contains the deepest constitutional constraints of any module. The chain is:

```
CAP-12 → CAP-13 → CAP-15 → CAP-16/CAP-17
                                    ↕
                               CAP-20 (parallel)
```

Each step has constitutional invariants that must hold.

### 5.2 CAP-12: Confidence Scoring

**What it receives:**
- Statistically validated signals from CAP-11 (MOD-04) — computational inputs
- Conflict flag annotation from CAP-09 (MOD-03) — annotation only, not a computational modifier

**What it explicitly does NOT receive:**
- The supplementary signal set (news/sentiment) — GOV-VAL05 Rule 1 prohibits this
- The supplementary signal set's source reliability scores as formula inputs — GOV-VAL05 Rule 5, VAL-07 closed
- Any AI-generated sentiment score as a formula weight — SDM-04 Rule 12; GOV-VAL05 Rule 1

**What it produces:**
- A confidence score per opportunity, derived exclusively from technical evidence and statistical validation
- Conflict-flag annotations marking which scored opportunities have unresolved technical/news tension — for human visibility at CAP-18; not a score modification
- Source reliability weight log (for audit)

**VAL-05 Computational Isolation (binding):**
The confidence score is a function of validated technical signals only. The conflict flag annotation is a separate metadata field on the score output. These are two distinct output elements: the score (computational) and the annotation (advisory). An implementation that merges them by modifying the score value based on the conflict flag violates GOV-VAL05.

**Evidence:** SADR_AMENDMENT_VAL-05 CAP-12 after-state: "Confidence computation is derived exclusively from technical evidence and statistical validation. News and sentiment signals do not enter the confidence formula." AF DOM-03 GOV-VAL05 Boundary: "The conflict flag from CAP-09 flows to CAP-12 as advisory annotation on the score output — never as a computational input that modifies the score."

**Statistical gate requirement:**
CAP-12 requires statistical significance tests (t-stat, Deflated Sharpe) as validation gates. Standard confidence intervals are insufficient (SDM-06 Rule 6). This means CAP-12's computation is gated on having statistical significance evidence from CAP-11 — the confidence score for an opportunity may not be produced without this evidence.

### 5.3 CAP-13: Expected Value Computation

**What it receives:**
- Confidence-scored opportunities from CAP-12 — after the confidence gate
- Current portfolio state from CAP-29 (MOD-09) — live portfolio context
- Historical probability data from CAP-14 (MOD-01) — bias-corrected baseline
- Regime context parameter from CAP-05 (MOD-02) — market condition context

**Constitutional priority rule:**
Trade probability over speculative theoretical return (SDM-07 Rule 1). The EV computation prioritizes probability-adjusted return, not maximum theoretical upside. This is an ordering constraint on the computation: the highest probability trade is preferred over the highest theoretical EV trade when they diverge.

**5% drawdown gate:**
The 5% drawdown tolerance strictly bounds acceptable downside risk (SDM-07 Rule 2; CONSTRAINT-06). Any opportunity whose downside risk estimate exceeds this bound fails the EV gate — it does not proceed to CAP-15 regardless of upside. This is a hard filter, not a soft weight.

**Cash-holding signal:**
When no opportunity passes the EV threshold, CAP-13 produces a cash-holding signal that routes directly to CAP-17 (bypassing CAP-15/CAP-16) for null-state declaration (SDM-07 Rule 5; CONSTRAINT-05). Capital deployment must never be forced.

**Open validation items as extension points:**
VAL-08 (VaR framework) and VAL-09 (multi-account aggregate margin) are CLASS_B — the architecture uses a regime context parameter as a generic interface; the specific mathematical formula for VaR is an extension point, not an architectural constraint.

### 5.4 CAP-15: Opportunity Ranking

**What it receives:**
- EV-filtered opportunity set from CAP-13
- Current position count from CAP-29 (MOD-09)

**Ranking invariants:**
- Rank by highest probability, not highest theoretical return (SDM-08 Rule 1; CONSTRAINT-03)
- Target 3–5 positions; scale to fewer or zero if insufficient (SDM-08 Rules 3, 4)
- If zero opportunities survive ranking, emit null-state trigger to CAP-17

**Open Menu invariant:**
CAP-15 produces the ranked list. This list must be delivered to MOD-07 as a simultaneous set — not as a sequence that implies priority beyond the stated rank. Sequential forced selection is prohibited (CONSTRAINT-09). This means CAP-15's output is a ranked set, not a ranked queue.

**Scaling signals from CAP-19 (MOD-06):**
CAP-23 (MOD-06) produces scaling signals that can affect CAP-15's recommended position count. These are inbound control signals from governance to recommendation — constitutionally authorized (AF 5.1: MOD-06 → MOD-05 "halt gating on recommendation issuance").

### 5.5 CAP-16: Conviction-Weighted Allocation

**What it receives:**
- Ranked opportunities from CAP-15
- Confidence scores from CAP-12 (carried forward through the chain)
- Portfolio state from CAP-29 (MOD-09)
- Scaling signals from CAP-19 (MOD-06) — uncertainty-band-driven sizing

**Constitutional allocation rules (all binding):**
- Conviction hierarchy: confidence-weighted first, then best-idea-weighted (SDM-09 Rule 2)
- Equal-weighting is constitutionally prohibited (SDM-09 Rule 3)
- Higher confidence → proportionally larger allocation (SDM-09 Rule 4)
- Concentration limits from portfolio state strictly observed (SDM-09 Rule 5)
- Sizing scales against illiquidity metrics from portfolio state (SDM-09 Rule 6)
- Sizing scales down when uncertainty bands widen — CAP-19 signal (SDM-09 Rule 7)

**Hold Cash invariant:**
When applicable (zero qualifying opportunities, or cash is optimal given available opportunities), CAP-16 must produce an explicit "Hold Cash" statement. This is not a default silently applied — it is an explicit output.

### 5.6 CAP-17: Null-State Declaration

**What it receives:**
- Null-state trigger from CAP-15 (no opportunities survive ranking)
- Cash-holding signal from CAP-13 (no opportunity meets EV threshold)

**Constitutional requirement:**
Null-state is a valid and required output type, not an error condition. The constitutionally mandated statement must be explicitly produced. This prevents the system from forcing capital deployment when no qualifying opportunities exist.

**Evidence:** SDM-01 Rule 1; SDM-08 Rule 7; SDM-CONST-11.

### 5.7 CAP-20: Exit Condition Recommendation

**Parallel execution:**
CAP-20 operates in parallel with the entry recommendation chain (CAP-12 → CAP-15 → CAP-16). It applies to open positions already in the portfolio, not to new opportunities.

**What it receives:**
- Technical evidence on open positions (from MOD-03/MOD-04 data)
- Supplementary signal evidence on open positions (from MOD-03 CAP-08)
- Time elapsed against expected horizons (1–3 days primary; 5–10 days secondary)
- Portfolio state from CAP-29 (MOD-09)

**Note on supplementary signals here:**
CAP-20 receives supplementary signal evidence for the purpose of exit evaluation only. GOV-VAL05 prohibits supplementary signals from entering confidence, EV, ranking, and allocation computation. Exit evaluation is a distinct domain (SDM-12) with its own evidence hierarchy. The exit precedence is: Risk > Technical > Time (SDM-12 Exit Precedence) — and technical deterioration strictly outweighs positive news in exit evaluation (SDM-12 Rule 3). So supplementary signals inform CAP-20 but are subordinate to technical and risk evidence.

**Output:**
Exit condition recommendation with rationale; extension justification when continuation is proposed; transaction cost estimates. All outputs are advisory — human approval is mandatory before any exit action (CONSTRAINT-01).

### 5.8 MOD-05 State Ownership

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Confidence scores (computational, with conflict annotations) | CAP-12 | Authoritative within the cycle |
| Source reliability weight log | CAP-12 | Authoritative — for audit |
| Probability-adjusted return estimates; downside drawdown estimates | CAP-13 | Derived from inputs; authoritative output |
| EV-filtered opportunity set | CAP-13 | Transient — consumed by CAP-15 |
| Cash-holding signal | CAP-13 | Transient — consumed by CAP-17 |
| Ranked opportunity list with execution records | CAP-15 | Authoritative output of this capability |
| Conviction-weighted allocation suggestions with justification | CAP-16 | Authoritative output of this capability |
| Null-state declaration | CAP-17 | Authoritative — mandatory when triggered |
| Exit condition recommendations with rationale | CAP-20 | Authoritative advisory output |

### 5.9 MOD-05 Invariants

- **I1:** CAP-12 confidence computation is technically pure — no sentiment formula inputs (GOV-VAL05 Rule 1)
- **I2:** Conflict flag annotation on confidence scores is metadata, not a score modifier (SADR_AMENDMENT_VAL-05)
- **I3:** Statistical significance gate must pass before a confidence score is produced (SDM-06 Rule 6)
- **I4:** The 5% drawdown bound is a hard filter at CAP-13, not a soft weight (SDM-07 Rule 2)
- **I5:** Null-state is produced explicitly when no qualifying opportunities exist — forced capital deployment is prohibited (SDM-01 Rule 1; CONSTRAINT-05)
- **I6:** Equal-weight allocation is prohibited — conviction weighting is mandatory (SDM-09 Rule 3)
- **I7:** All outputs from this module are advisory — none constitute executable trade orders (SDM-CONST-13)
- **I8:** MOD-05 issuance is gated by MOD-06 active halt states — computation may continue, but issuance to MOD-07 is blocked when a blocking halt state is active

---

## SECTION 06 — MOD-06 GOVERNANCE REALIZATION (DEEP ANALYSIS)

### 6.1 The Fundamental Design Challenge

MOD-06 contains seven capabilities with two distinct functions:
- **Detection** (CAP-19, CAP-23, CAP-31): continuously monitor for conditions
- **Halt-state management** (CAP-24, CAP-25, CAP-26, CAP-27): manage four independent states

These functions must interact in a constitutionally constrained way:
- Detection capabilities trigger halt-state capabilities (one-direction)
- Detection capabilities must continue operating during any active halt state
- The four halt states are constitutionally independent — no shared authority

### 6.2 Detection Capability Internal Behavior

**CAP-19 | Position Limit Enforcement**

Continuous monitoring function. Receives portfolio state from CAP-29 (MOD-09) on each cycle.

Evaluation logic:
1. Compare active position count against 3–5 target (monitoring)
2. Compare position concentration against limits (monitoring)
3. If concentration or hard position limit is breached: emit hard halt trigger to CAP-24
4. If uncertainty bands widen: emit scaling signal to MOD-05/CAP-16

CAP-19 is a detector and signaler. It does not manage halt state — that is CAP-24's responsibility.

**CAP-23 | Risk Circuit Breaker Enforcement**

Continuous monitoring function. Receives: uncertainty band metrics, volume spike data, margin data, regime classification and non-ergodic condition signal from CAP-05 (MOD-02), macro condition signals.

Evaluation logic (SDM-15 Rules 6–12):
1. Detect trend-following dynamic hedging cycles → suspension signal to CAP-27
2. Detect widening uncertainty bands → scaling signal to MOD-05/CAP-15, CAP-16
3. Detect volume spikes for informational cascades → suspension signal to CAP-27
4. Restrict variation margin assumptions during elevated volatility → margin restriction signal
5. Audit synthetic leverage margin against initial margin limits → compliance status
6. Detect extreme macro shocks / non-ergodic breakdowns → suspension signal to CAP-27
7. Detect dynamic hedging cycles during extreme conditions → suspension signal to CAP-27

CAP-23 is a detector and signaler for State 3 (Conditional Suspension). It also produces scaling signals that affect MOD-05 recommendation sizing without requiring a full halt.

**Open validation items as extension points within CAP-23:**
VAL-03, VAL-08, VAL-14, VAL-17 are CLASS_B — the non-ergodic condition signal from CAP-05 is a generic interface; the specific mathematical criteria for ergodic state exit are extension points, not architectural constraints.

**CAP-31 | Governance Compliance Monitor**

Continuous evaluation function. Receives portfolio state from CAP-29 (MOD-09) — specifically: position records, stop-loss presence, risk control compliance status, applied governance constraints.

Evaluation logic:
1. Evaluate portfolio state against GOV-02 governance rules
2. If a governance violation is detected (removal of stop-loss protection, violation of risk controls): emit violation signal to CAP-26
3. If a governance restoration is detected (corrective action has been taken): emit restoration signal to CAP-26

CAP-31 evaluates continuously — not only at approval gate events. This is a binding constitutional constraint from SADR CAP-31.

**Critical continuity requirement:** CAP-31 must continue evaluating during Governance Lockout (State 2) so that it can detect restoration and emit the restoration signal that allows State 2 to exit automatically (GOV-02 Rule 3). If CAP-31 were halted by the Lockout state, the automatic exit condition would never fire.

### 6.3 Halt-State Independence: The Core Constitutional Requirement

The four halt states must be independent in three dimensions:
1. **Independent entry** — each has its own trigger; triggering one does not trigger another
2. **Independent active state** — each maintains its own active/inactive status separately
3. **Independent exit** — each has its own exit condition; restoring one does not restore another

**How independence is realized internally:**

Each of CAP-24, CAP-25, CAP-26, CAP-27 owns its own state flag (active/inactive) and its own entry/exit logic. No shared flag. No shared evaluation. No combined state machine.

The combined effect on MOD-05 issuance is computed by evaluating all four flags independently and blocking issuance if any flag is set to blocking. This is not a "state machine" — it is four independent binary states whose blocking effect is additive.

**Evidence:** ADR-000 P-06; ADR-002 FORB-10; SDM-CONST-14: "Each state operates independently. Restoration of one state does not restore another."

### 6.4 Per-Halt-State Internal Behavior

**CAP-24 | Hard Deterministic Halt (State 4)**

Entry logic:
- Receive hard halt trigger from CAP-19 (on position/concentration limit breach)
- Set State 4 active flag
- Block position recommendations that would cause or sustain the breach in MOD-05
- Generate human-visible alert
- Log halt entry with condition state

Active state:
- State 4 active flag is set
- MOD-05 cannot issue position recommendations that cause or sustain the breach
- Other recommendation types (that don't exacerbate the breach) are not blocked by State 4 alone
- Detection functions continue (CAP-19, CAP-23, CAP-31)

Exit logic:
- Receive human acknowledgment AND confirmed return to within limits
- Both conditions required — acknowledgment alone is insufficient
- Set State 4 inactive flag
- Log halt exit with portfolio compliance confirmation state

**CAP-25 | Governance Halt (State 1)**

Entry logic:
- Receive drawdown ≥ 5% signal from CAP-29 (MOD-09)
- Set State 1 active flag
- Block all new MOD-05 recommendation issuance
- Block all new MOD-05 capital allocation recommendation issuance
- Generate critical risk escalation report for human review (GOV-01 Rule 4 — this report must be generated; it routes to MOD-07)
- Log halt entry

Active state:
- State 1 active flag is set
- No new recommendations may be issued from MOD-05
- Reporting, monitoring, and governance detection continue (GOV-01 Rule 4 explicitly requires report generation to continue)
- Detection functions continue (IAC-08)

Exit logic:
- Receive explicit human resumption authorization (GOV-01 Rule 5 — human authority required)
- Set State 1 inactive flag
- Log halt exit

**CAP-26 | Governance Lockout (State 2)**

Entry logic:
- Receive governance violation signal from CAP-31
- Set State 2 active flag
- Block all new MOD-05 recommendations, allocation recommendations, and capital deployment recommendations
- Log halt entry (violation signal received)

Active state:
- State 2 active flag is set
- Most comprehensive blockage: recommendations, allocations, capital deployment all blocked
- CAP-31 continues evaluating (GOV-02 Rule 3 requires automatic restoration detection)
- CAP-29 continues providing portfolio state (CAP-31 needs it)
- Reporting continues

Exit logic:
- Receive governance restoration signal from CAP-31 (automatic on detected corrective action)
- No additional human authorization required beyond the corrective action itself (GOV-02 Rule 3)
- Set State 2 inactive flag
- Log halt exit (restoration signal received)

**CAP-27 | Conditional Recommendation Suspension (State 3)**

Entry logic:
- Receive suspension signal from CAP-23 (on specific adverse conditions per SDM-15 Rules 6, 7, 8, 11, 12)
- Set State 3 active flag (with condition identity)
- Suspend or scale down MOD-05 recommendations for the affected domain only (not system-wide)
- Log suspension entry WITH condition state (mandatory — SDM-15 Rule 14)

Active state:
- State 3 active flag is set for the specific affected domain
- Other recommendation domains not affected by this state
- CAP-23 continues monitoring for condition clearance (required for automatic exit)

Exit logic:
- Receive condition clearance signal from CAP-23 (when the triggering condition clears)
- Exit is condition-driven, NOT human-authorization-driven (SDM-15 Rule 14)
- Set State 3 inactive flag for the affected domain
- Log suspension exit WITH condition state at exit (mandatory — SDM-15 Rule 14)

### 6.5 Gating Surface: How MOD-06 Controls MOD-05 Issuance

The gating surface is at the issuance boundary of MOD-05 — specifically the point where CAP-15/CAP-16/CAP-17/CAP-20 outputs are provided to MOD-07/CAP-18.

The gate evaluates: for each recommendation type, is any active halt state blocking this type?

| Recommendation Type | Blocked By State 1 | Blocked By State 2 | Blocked By State 3 | Blocked By State 4 |
|--------------------|--------------------|--------------------|--------------------|---------------------|
| New recommendations | ✓ | ✓ | ✓ (affected domain) | ✓ (causing/sustaining breach only) |
| Capital allocation recommendations | ✓ | ✓ | (depends on domain) | — |
| Capital deployment recommendations | — | ✓ | — | — |
| Position recommendations causing breach | — | — | — | ✓ |

Note: States are evaluated independently. If States 1 and 4 are both active, both blocking conditions apply independently.

**MOD-05 computation continues regardless of halt state.** The halt gates issuance — not computation. MOD-05 may compute confidence, EV, rankings, and allocations while halt states are active. The outputs are withheld from MOD-07 rather than not produced.

**Evidence:** AF 6.1: "The gating surface of DOM-06 is the issuance boundary of DOM-05 outputs... never the upstream domains DOM-01 through DOM-04."

### 6.6 Governance Events to MOD-11

MOD-06 emits governance/risk events to MOD-11 for Mode 3 event-driven activation. This is an outbound event signal — an initiation trigger, not a data dependency.

What constitutes a governance/risk event triggering Mode 3:
- Halt state entry (any state)
- Halt state exit (any state)
- Governance violation detection (CAP-31)
- Governance restoration detection (CAP-31)
- Circuit breaker trigger (CAP-23)
- Position limit breach (CAP-19)

These events signal that a mandatory review cycle should be initiated. MOD-11 receives the initiation trigger and emits activation signals. This does not make MOD-06 an orchestrator — it makes MOD-06 a source of constitutionally authorized Mode 3 triggers.

### 6.7 MOD-06 State Ownership

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Position limit compliance status | CAP-19 | Authoritative — produced for downstream and audit |
| Concentration limit compliance status | CAP-19 | Authoritative |
| Circuit breaker detection signals | CAP-23 | Transient — produced per evaluation cycle |
| Margin assumption restriction signals | CAP-23 | Authoritative for the duration of the restriction condition |
| Governance violation signal | CAP-31 | Event — produced on violation detection |
| Governance restoration signal | CAP-31 | Event — produced on restoration detection |
| Hard Halt active flag (State 4) + entry/exit condition records | CAP-24 | Authoritative — independent state |
| Governance Halt active flag (State 1) + entry/exit records | CAP-25 | Authoritative — independent state |
| Governance Lockout active flag (State 2) + entry/exit records | CAP-26 | Authoritative — independent state |
| Conditional Suspension active flag (State 3) + entry/exit condition records | CAP-27 | Authoritative — independent state |
| Critical risk escalation report content | CAP-25 | Authoritative — produced during State 1 active |
| Human-visible breach alerts | CAP-24 | Authoritative — produced on halt entry |

### 6.8 MOD-06 Invariants

- **I1:** Detection functions (CAP-19, CAP-23, CAP-31) operate continuously — not gated by any halt state (IAC-08; AF 6.1; GOV-02 Rule 3)
- **I2:** Each halt-state capability owns its own independent active flag — no shared state variable (ADR-000 P-06; IAC-07)
- **I3:** Halt state entry in one state does not imply, require, or prevent entry in any other state (SDM-CONST-14)
- **I4:** Halt state exit in one state does not imply, cause, or enable exit in any other state (SDM-CONST-14)
- **I5:** Governance Lockout (State 2) exit is automatic on CAP-31 restoration signal — no additional human authorization (GOV-02 Rule 3)
- **I6:** Conditional Suspension (State 3) exit is automatic on CAP-23 condition clearance — not human-authorization-driven (SDM-15 Rule 14)
- **I7:** Both State 3 entry and exit are logged with condition state (SDM-15 Rule 14)
- **I8:** Zero execution authority exists anywhere in MOD-06 (SDM-CONST-14; GOV-01 Rule 1; GOV-02 Rules 4–5)

---

## SECTION 07 — MOD-10 AUDIT REALIZATION (DEEP ANALYSIS)

### 7.1 The Structural Requirement

CAP-30 must receive audit records from every capability across all 11 modules and produce no output to any other module. This places CAP-30 in a uniquely asymmetric position: it is the universal recipient and terminal sink.

### 7.2 How Audit Records Reach MOD-10

Every capability that produces an audit-required output is responsible for emitting that output toward CAP-30 as part of its own operation. Audit record emission is not optional — every SDM decision domain (SDM-02 through SDM-15) carries an explicit Audit clause, and every capability within those domains has specific audit requirements.

The direction of all audit flows is inbound to CAP-30:

- MOD-01 → CAP-30: exclusion logs, cross-verification records, adjustment records, eligible-vs-filtered counts
- MOD-02 → CAP-30: regime shift triggers, drift metrics, walk-forward bounds
- MOD-03 → CAP-30: conflict resolution rationale, signal evidence weights
- MOD-04 → CAP-30: validation results, edge verdicts, outlier detection records
- MOD-05 → CAP-30: confidence computation records, EV inputs, ranking execution logs, conviction weight justifications, null-state events
- MOD-06 → CAP-30: halt state entry/exit records with condition state, compliance evaluation events, circuit breaker triggers, scaling adjustments, position limit tests
- MOD-07 → CAP-30: immutable record of original system recommendation vs. final human action; all approvals, rejections, overrides
- MOD-08 → CAP-30: attribution event records, system alpha outcomes, human override deltas
- MOD-09 → CAP-30: portfolio state records relevant to drawdown threshold tests
- MOD-11 → CAP-30: activation mode and initiated cycle records

### 7.3 CAP-30 Internal Behavior

CAP-30's internal operation is simple in principle and absolute in constraint:

1. **Receive** a record from any module
2. **Write** the record immutably — the record may not be modified after receipt
3. **Produce no output** to any other module

CAP-30 does not:
- Process or transform records
- Route records to other capabilities
- Evaluate records for compliance
- Feed records back to any module that produced them

### 7.4 Immutability Constraint

Immutability means that once a record is received by CAP-30, no operation within MOD-10 (or anywhere in the system) may modify or delete it. This is not merely append-only (which permits deletion of earlier records) — it is structural immutability.

**Evidence:** SADR CHANGE-06: the amendment specifically replaced "append-only" with "immutable" to strengthen this constraint. ADR-000 P-07.

### 7.5 Human Review Access

Human access to audit records is explicitly constitutionally authorized and is the only legitimate consumer of audit output. This access is for review purposes — reading the record. It does not constitute a feedback path back to any system capability.

The system must not confuse "human reads audit records" with "audit feeds back to system behavior." These are architecturally distinct. The human's decision to act on information derived from audit records (e.g., approving an SDM behavior change based on attribution findings) travels through the constitutionally authorized change process (SDM-13 Rule 9), not through a system-to-system data edge.

### 7.6 Mandatory Audit Coverage

The following table establishes what MOD-10 must hold — derived from SADR Section 9 evidence requirements and SDM Audit clauses:

| Domain | Mandatory Records |
|--------|-------------------|
| CAP-02 | Cross-verification match/mismatch records |
| CAP-10 | Walk-forward validation bounds; OOS documentation |
| CAP-11 | Deflated return metrics or t-stat; stability index values |
| CAP-12 | Confidence computation records; source reliability weights |
| CAP-13 | Probability-adjusted return inputs; drawdown compliance gate logs |
| CAP-14 | Survivorship bias validation confirmation per opportunity |
| CAP-15 | Ranking logic execution logs proving non-equal-weighting |
| CAP-16 | Conviction weight justification per suggestion |
| CAP-17 | Null-state event logs |
| CAP-18 | Immutable record of all approvals, rejections, overrides |
| CAP-21 | Attribution logs per trade cycle; system alpha records |
| CAP-22 | Human override delta records per trade cycle |
| CAP-24 | Halt entry and exit with portfolio compliance confirmation state |
| CAP-25 | Halt entry log; human resumption authorization record; halt exit log |
| CAP-26 | Lockout entry log (violation signal received); lockout exit log (restoration signal received) |
| CAP-27 | Suspension entry log with condition state; suspension exit log with condition state at exit |
| CAP-31 | Compliance evaluation event records; violation signal issuance records; restoration signal issuance records |

### 7.7 MOD-10 Invariants

- **I1:** CAP-30 produces no output to any other module — zero outbound edges (ADR-000 P-07; ADR-002 FORB-02)
- **I2:** Every received record is immutable from the moment of receipt (SADR CHANGE-06; ADR-000 P-07)
- **I3:** No module reads from CAP-30 at runtime to influence its computational logic (ADR-002 FORB-02)
- **I4:** Human review of audit records is authorized and does not constitute a system feedback path
- **I5:** Audit coverage is mandatory across all SDM-02 through SDM-15 Audit clauses — no capability's audit clause may be silently omitted

---

## SECTION 08 — MOD-11 ACTIVATION REALIZATION (DEEP ANALYSIS)

### 8.1 The Constraint: Initiation Without Orchestration

CAP-28 is constitutionally authorized to initiate cycles. It is constitutionally prohibited from:
- Governing what happens within the initiated cycles
- Owning the execution of what is initiated
- Tracking cycle progress or outcomes
- Making decisions based on cycle outcomes

This distinction — initiation authority without governance authority — is the central architectural constraint of MOD-11.

**Evidence:** AF 5.3 secondary check: "activation is initiation, not data dependency; CAP-28's output is an initiated cycle, not an input consumed by CAP-23/CAP-31 logic." AF DOM-11: "Initiate research/analysis/monitoring/attribution/reporting/governance cycles under the three constitutionally authorized modes, and record which mode initiated each cycle."

### 8.2 Three Activation Modes

**Mode 1 — Scheduled Activation**

Trigger: predefined schedule
Nature: autonomous initiation — no human action required for the initiation itself
What is initiated: research, analysis, monitoring, and report generation cycle
What is NOT initiated: trade execution (ever)

The schedule is a constitutionally authorized trigger. The specific schedule is an extension point — it is operational configuration, not architectural structure.

**Mode 2 — On-Demand Activation**

Trigger: explicit human request
Nature: human-initiated — CAP-28 receives the human request and emits the activation signal
What is initiated: research, analysis, monitoring, and report generation cycle on demand
What is NOT initiated: trade execution

The human's request is the initiating event. CAP-28's role is to translate that request into an activation initiation signal. The human is not requesting specific outputs — they are authorizing a research cycle.

**Mode 3 — Event-Driven Activation**

Trigger: governance/risk/portfolio events from MOD-06
Nature: event-driven — MOD-06 emits a governance/risk event; CAP-28 receives it and emits an activation signal
What is initiated: mandatory review cycle triggered by the governance/risk event
What is NOT initiated: trade execution

This is the constitutionally bounded event relationship from ADR-001. The event travels from MOD-06 to MOD-11 as an initiation trigger. CAP-28 does not consume the event as a data input to its own logic — it converts the event into an activation signal.

**Evidence:** ADR-001 Section 7 R7, R8; SADR Section 8 Mode 3; AF 5.3 secondary check.

### 8.3 CAP-28's Output: Activation Initiation Signal

CAP-28 emits one type of output: an activation initiation signal. This signal:
- Authorizes all autonomous modules to begin their cycle
- Records which activation mode produced it
- Does not specify what those modules should do (that is determined by each module's own constitutional scope)
- Does not direct the flow between modules (that is determined by the dependency graph established in ADR-002)

**CAP-28 does not orchestrate.** It does not say "first do MOD-01, then MOD-02, then MOD-03." The execution sequence across modules is determined by the dependency graph — each module proceeds when its constitutional inputs are available. CAP-28 is the starting condition for the cycle, not its conductor.

### 8.4 What CAP-28 Records

CAP-28's audit obligation: the activation mode and the initiated cycle are recorded for MOD-10.

| Record Element | Content |
|----------------|---------|
| Activation mode | Mode 1 (Scheduled), Mode 2 (On-Demand), or Mode 3 (Event-Driven) |
| Trigger identity | The schedule trigger, human request, or governance event that caused the initiation |
| Initiated cycle | The cycle that was initiated (timestamp + context) |

### 8.5 MOD-11 State Ownership

| State Class | Owned By | Nature |
|-------------|----------|--------|
| Activation events (mode, trigger, initiated cycle) | CAP-28 | Authoritative — for audit; transient for cycle initiation purposes |

### 8.6 MOD-11 Invariants

- **I1:** Activation grants no execution authority — no activation mode enables trade execution (SDM-CONST-15; CONSTRAINT-10)
- **I2:** CAP-28 is an initiator, not an orchestrator — it does not govern the sequence of module execution after initiation (AF 5.3; IAC-12)
- **I3:** Mode 3 activation triggers are initiation signals from MOD-06, not data inputs consumed by CAP-28's computational logic (AF 5.3 secondary check)
- **I4:** Human approval remains mandatory before any trade action regardless of which activation mode produced the underlying recommendation (SDM-CONST-15)
- **I5:** Activation records are the only information class owned by MOD-11; their sole authorized consumer within the system is MOD-10 (AF SECTION-04 "Activation records")

---

## SECTION 09 — CROSS-CUTTING INTERNAL CONTRACTS

### 9.1 Module Entry Conditions

| Module | Entry Condition | Constitutional Basis |
|--------|----------------|---------------------|
| MOD-01 | Activation signal from MOD-11 (any mode) | SDM-CONST-15; SADR Section 8 |
| MOD-02 | Verified, adjusted, eligible market data available from MOD-01 | SADR CAP-05 INPUTS |
| MOD-03 | CAP-07: eligible data from MOD-01 + context from MOD-02. CAP-08: external news/event data available. Both may proceed in parallel. | SADR CAP-07, CAP-08 INPUTS |
| MOD-04 | Technical signals from MOD-03/CAP-07 available | SADR CAP-10 INPUTS |
| MOD-05 | Validated signals from MOD-04/CAP-11 available (after CAP-10 gate). Portfolio state from MOD-09 available. | SADR CAP-12 INPUTS |
| MOD-06 | Continuous — not cycle-dependent; monitoring functions run independently of recommendation cycle | AF 6.1; IAC-08 |
| MOD-07 | All advisory package sections assembled: MOD-05 outputs + MOD-03 supplementary advisory section + MOD-06 halt state flags + MOD-09 drawdown status | SADR CAP-18 INPUTS |
| MOD-08 | Post-gate from MOD-07: human decisions recorded | SADR CAP-21, CAP-22 INPUTS |
| MOD-09 | Authoritative external execution record (human-confirmed trades) | SADR CAP-29 INPUTS |
| MOD-10 | Any capability in any module emitting an audit record | SADR CAP-30 INPUTS |
| MOD-11 | Mode 1: schedule. Mode 2: human request. Mode 3: governance event from MOD-06 | SDM-CONST-15 |

### 9.2 Module Exit Conditions (What a Module Produces to Downstream)

| Module | Exit Output | Destination |
|--------|------------|-------------|
| MOD-01 | Eligible, adjusted, bias-corrected datasets | MOD-02, MOD-03, MOD-04, MOD-05 |
| MOD-02 | Market context state (regime, trend filter, non-ergodic signal, drift) | MOD-03, MOD-05, MOD-06 |
| MOD-03 | Technical signal set → MOD-04. Conflict flag annotation → MOD-05. Supplementary advisory section → MOD-07. | MOD-04, MOD-05, MOD-07 |
| MOD-04 | Validated signal set with edge evidence | MOD-05 |
| MOD-05 | Complete recommendation package (or null-state declaration) | MOD-07 (gated by MOD-06) |
| MOD-06 | Halt state flags → MOD-07 display. Governance events → MOD-11 Mode 3. Scaling signals → MOD-05. | MOD-05 (gating), MOD-07, MOD-11 |
| MOD-07 | Human decisions (approvals/rejections/overrides) | MOD-08 (observation), MOD-09 (state update path), MOD-10 |
| MOD-08 | Attribution reports, insights, warnings | Human only + MOD-10 |
| MOD-09 | Portfolio state | MOD-05, MOD-06, MOD-07 |
| MOD-10 | Nothing within the system; human review access only | — |
| MOD-11 | Activation initiation signal | All autonomous modules + MOD-10 |

### 9.3 Module Invariants (Universal — All Modules)

| Invariant | Applies To | Constitutional Basis |
|-----------|-----------|---------------------|
| Audit record emission is mandatory | All modules | SDM-02 through SDM-15 Audit clauses |
| No module holds execution authority | All modules | SDM-CONST-14; CONSTRAINT-01 |
| Technology-neutral internal design | All modules | ADR-000 P-12 |
| Open validation items treated as extension interfaces | All affected modules | SADR Section 11 CLASS_B/C/D |
| Unverified data may not reach signal logic | MOD-03, MOD-04, MOD-05 | SDM-02 Rule 2; IAC-02 |

### 9.4 Module Guarantees

| Module | Guarantee | Constitutional Basis |
|--------|-----------|---------------------|
| MOD-01 | Produces only verified, adjusted, eligible data — no raw data reaches downstream | CAP-02 blocking gate |
| MOD-04 | Produces only walk-forward validated signals — no unvalidated signals reach CAP-12 | CAP-10 blocking gate |
| MOD-05 | Confidence scores are technically pure — no sentiment computational inputs | GOV-VAL05 Rule 1 |
| MOD-05 | All outputs are advisory — no executable trade orders produced | SDM-CONST-13 |
| MOD-06 | Monitoring functions operate continuously under all halt states | AF 6.1 |
| MOD-06 | Four halt states are independent — no shared state or shared exit logic | SDM-CONST-14 |
| MOD-07 | Human approval gate cannot be bypassed or auto-approved | SDM-CONST-06; CAP-18 Boundary |
| MOD-07 | All opportunities presented simultaneously (Open Menu) | CONSTRAINT-09 |
| MOD-08 | Zero write authority to any recommendation or governance module | CONSTRAINT-07 |
| MOD-09 | Portfolio state sourced exclusively from human-confirmed trade actions | CAP-29 INPUTS |
| MOD-10 | Immutable records only — no modification after receipt | SADR CHANGE-06 |
| MOD-10 | No outbound edges to any module | ADR-002 FORB-02 |
| MOD-11 | Initiation only — no orchestration authority | AF 5.3; IAC-12 |

---

## SECTION 10 — ARCHITECTURE INTEGRITY VALIDATION

### 10.1 Validation Against SDM_V2.3

| SDM Requirement | Validation Result | Evidence |
|----------------|-------------------|---------|
| SDM-CONST-06: Human approval mandatory | MOD-07/CAP-18 is the sole blocking gate; no bypass exists in any module's internal flow | Section 03 MOD-07; Section 09 9.4 |
| SDM-CONST-10: Technical primary, news supplementary | CAP-07 (primary) and CAP-08 (supplementary) are separate capabilities; GOV-VAL05 routing prevents supplementary signals from reaching computation | Section 03 MOD-03; Section 05 5.2 |
| SDM-CONST-12: Modular and reversible | Each module has explicit capability boundaries, defined interfaces, and no shared state across module lines | Section 03 all modules |
| SDM-CONST-14: Four independent halt states | Four independent capabilities (CAP-24, CAP-25, CAP-26, CAP-27) with independent flags and logic within MOD-06 | Section 06 6.3, 6.4 |
| SDM-CONST-15: Three activation modes | CAP-28 handles all three; Mode 3 receives governance events from MOD-06 | Section 08 8.2 |
| SDM-13: Attribution read-only | MOD-08 has zero write edges to any other module; outputs go to human and MOD-10 only | Section 03 MOD-08; Section 05 (no MOD-08 inputs) |
| SDM-15 Rule 3: Deterministic execution | MOD-05 confidence computation is technically pure; no AI sentiment score enters the computational chain | Section 05 5.2 |
| SDM-15 Rule 14: Condition-state logging | CAP-27 logs both entry and exit with condition state | Section 06 6.4 |

### 10.2 Validation Against VAL05_OWNER_DECISION_RESOLUTION

| GOV-VAL05 Rule | Validation Result | Evidence |
|---------------|-------------------|---------|
| Rule 1: Confidence computation technically pure | CAP-12 receives validated signals from CAP-11 and conflict annotation from CAP-09 only; supplementary signals are routed to MOD-07, not CAP-12 | Section 05 5.2; Section 04 MOD-05 flow |
| Rule 2: News modifies human judgment, not score | MOD-03's supplementary signals route to MOD-07 advisory report; the score is technically derived | Section 03 MOD-03; Section 05 5.2 |
| Rule 4: Named advisory section distinct | MOD-07 advisory assembly includes supplementary signals as a named distinct section | Section 03 MOD-07 Advisory Package Assembly |
| Rule 5: VAL-07, VAL-11, VAL-15 closed | No module accepts sentiment-to-score-weight, sentiment-to-Kelly, or sentiment-to-sizing as an input | Section 05 5.2, 5.5 |

### 10.3 Validation Against SADR_V2.1

| SADR Constraint | Validation Result |
|----------------|-------------------|
| CONSTRAINT-01: No execution authority | Zero execution authority in any module's internal flow; governance enforces via recommendation gating only |
| CONSTRAINT-05: Cash is valid; forced deployment prohibited | CAP-13 cash-holding signal + CAP-17 null-state declaration ensure this explicitly |
| CONSTRAINT-07: Attribution read-only | MOD-08 internal flow has no write edges to MOD-01..06 |
| CONSTRAINT-08: Walk-forward mandatory; K-fold prohibited | CAP-10 internal invariant |
| CONSTRAINT-09: Open Menu | MOD-07 simultaneous presentation invariant |
| All capability BOUNDARY clauses respected | Each module's internal flow matches each capability's BOUNDARY clause in SADR |

### 10.4 Validation Against ARCHITECTURE_FOUNDATION_V1

| AF Requirement | Validation Result |
|---------------|-------------------|
| 11 domains, 1:1 to modules | Confirmed — 11 modules in Section 03 |
| Halt states gate issuance only (AF 6.1) | MOD-05 computation continues; only issuance to MOD-07 is gated | Section 06 6.5 |
| No halt state stops detection (AF 6.1) | MOD-06 detection capabilities invariant I1: continuous regardless of halt state | Section 06 6.8 |
| DOM-07→DOM-09 cycle broken at system boundary | MOD-07 human decisions → MOD-09 pathway exits through external execution record | Section 03 MOD-09 |

### 10.5 Validation Against ADR-000 Principles

| Principle | Validation Result |
|-----------|-------------------|
| P-01: Constitution Before Optimization | All internal flows derived from constitutional evidence; no performance criterion introduced |
| P-03: Human Approval Cannot Be Bypassed | CAP-18 is the only gate for trade action; no module's internal flow bypasses it |
| P-04: Single Owner Per Information Class | Each information class has exactly one producing module/capability |
| P-05: No Hidden Portfolio State | MOD-09/CAP-29 is sole source; no module maintains private portfolio state derivatives |
| P-06: No Governance State Coupling | Four independent halt capabilities within MOD-06; invariant I2 confirmed |
| P-07: Audit Is Write-Only | MOD-10 terminal sink; zero outbound edges; immutable records |
| P-08: Attribution Is Read-Only | MOD-08 zero write edges to MOD-01..06 confirmed |
| P-09: Sentiment Is Advisory Only | CAP-12 computation purity invariant I1 confirmed |
| P-10: Dependencies Flow One Direction | All module flows in Section 04 are unidirectional; no internal cycles |
| P-12: Technology Neutral | No technology named in any module's internal realization |

### 10.6 Validation Against ADR-001

| ADR-001 Decision | Validation Result |
|-----------------|-------------------|
| Modular Monolith core | All blocking gates are sequential within the module dependency flow; no asynchronous routing in the recommendation pipeline |
| Bounded event signaling | Event relationships in Section 04 are bounded to MOD-11 activation and MOD-06 → MOD-11 governance events |
| Risk 1 (boundary erosion) mitigated | Section 03 GOV-VAL05 routing constraint (MOD-03) and MOD-05 computation purity invariant explicitly stated |
| Risk 3 (governance continuity) resolved | Section 06 6.1–6.8 explicitly addresses which functions continue under each halt state |

### 10.7 Validation Against ADR-002

| ADR-002 Decision | Validation Result |
|-----------------|-------------------|
| Module catalog (11 modules) | Internal realizations provided for all 11 |
| Capability allocation (31 capabilities) | All capability orderings in Section 03 and Section 04 match ADR-002 allocation |
| FORB-01 through FORB-10 | No internal flow violates any prohibition; confirmed by module invariants |
| Blocking gates in ADR-002 Section 6.2 | CAP-02 (MOD-01), CAP-10 (MOD-04), CAP-18 (MOD-07) — all treated as hard sequential blockers in Section 03 |

---

## SECTION 11 — ADR-004 READINESS VERDICT

### Verdict: ADR-004 MAY PROCEED

**Evidence:**

**E1 — All 11 modules have defined internal realizations.**
Sections 03 and 04 provide capability ordering, internal information flow, state ownership, and invariants for every module. Sections 05–08 provide deep analysis for the four most constitutionally complex modules.

**E2 — The MOD-05 computational chain is fully specified.**
The confidence-to-EV-to-ranking-to-allocation chain is specified with all constitutional constraints: VAL-05 computational isolation enforced, statistical significance gate identified, 5% drawdown hard filter identified, equal-weighting prohibition enforced, null-state explicit declaration invariant confirmed.

**E3 — MOD-06 four-halt-state independence is architecturally realized.**
Section 06 establishes four independent state elements, their independent entry/exit logic, the gating surface, and the continuity requirement for detection functions. No shared state or shared exit logic exists.

**E4 — MOD-10 audit terminal sink is fully characterized.**
Section 07 establishes mandatory audit coverage, immutability constraint, and no-runtime-read-back invariant.

**E5 — MOD-11 activation-without-orchestration is fully characterized.**
Section 08 establishes the distinction between initiation authority and governance authority, and confirms that CAP-28 is not an orchestrator.

**E6 — Cross-cutting contracts are explicit.**
Section 09 provides entry conditions, exit outputs, universal invariants, and guarantees for all 11 modules.

**E7 — Full constitutional compliance validated.**
Section 10 validates ADR-003 against all seven authority levels. No conflicts found.

**ADR-004 Scope Guidance (non-binding — for orientation only):**

ADR-004 is likely to address one or more of:
- Intra-module boundary enforcement mechanisms (how module boundaries prevent prohibited dependencies)
- The specific design of the gating surface between MOD-06 and MOD-05 issuance
- How open validation items (CLASS_B/C/D) are expressed as extension interfaces in the affected capabilities
- How the MOD-07 advisory package assembly is structured as a simultaneous Open Menu presentation
- How MOD-09's single-source constraint is enforced across all consuming modules

ADR-004 must not:
- Select specific technologies, databases, APIs, or infrastructure
- Design deployment architecture
- Resolve constitutionally deferred SDM-14
- Reopen any frozen constitutional, capability, module, or style decision

---

*ADR-003 derives its authority from SDM_V2.3, VAL05_OWNER_DECISION_RESOLUTION, SADR_V2.1, ARCHITECTURE_FOUNDATION_V1, ADR-000_ARCHITECTURE_PRINCIPLES, ADR-001_ARCHITECTURAL_STYLE_SELECTION, and ADR-002_CAPABILITY_TO_MODULE_REALIZATION. It introduces no implementation decisions, no technology selections, no database designs, no API specifications, and no deployment architecture. It performs internal module realization within the frozen module model.*

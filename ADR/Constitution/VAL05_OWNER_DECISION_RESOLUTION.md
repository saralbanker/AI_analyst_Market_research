# VAL-05 OWNER DECISION RESOLUTION
## Sentiment Integration Pathway — Final Constitutional Resolution

**Item:** VAL-05
**Protocol:** OWNER_DECISION_RESOLUTION_PROTOCOL
**Authorities:** SDM_V2.3 | SDM_FREEZE_CERTIFICATION | SADR_V2.1

---

## SECTION 1 — DECISION ANALYSIS

### The Constitutional Question

VAL-05 asks: does AI-generated sentiment analysis enter the deterministic computation pipeline (Option A), or does it remain in the advisory domain presented to the human (Option B)?

This is not a question of whether news matters. The SDM is clear that it does. SDM-CONST-10, SDM-04 Rule 3, and SDM-06 Rule 2 all acknowledge news as a legitimate input to the system. The question is whether that input travels through the computational confidence formula or through the human's judgment at the approval gate.

---

### Criterion-by-Criterion Evaluation

**1. Human-in-the-Loop Identity**

*Option A:* Sentiment modifies the confidence number computationally. The human sees the output of the modification — a higher or lower confidence score — but not necessarily the raw sentiment signal that moved it.

*Option B:* Sentiment is presented directly to the human as a named input. The human sees the sentiment signal, the technical evidence, and the confidence score derived purely from technical evidence. The human applies their own weighting to the sentiment in making their final decision.

*Assessment:* Option B more fully realizes Human-in-the-Loop Identity. The human is not receiving a pre-blended number — they are receiving the raw inputs and doing the blending themselves. Option A delegates part of the human's judgment to a formula. **Option B superior.**

---

**2. Technicals Dominant**

*Option A:* SDM-06 Rule 1 says base confidence *strictly* on technical evidence as the primary weight. "Strictly" is a constitutional word. Under Option A, a formula applies a secondary weight from sentiment. If sentiment moves in the same direction as technicals, the confidence number rises above what technicals alone would produce. This is computational influence, not merely context.

*Option B:* The confidence score is derived exclusively from technical evidence and statistical validation. Sentiment cannot mathematically move the confidence number. Technical dominance is structurally guaranteed, not formula-enforced.

*Assessment:* The constitutional requirement is that technicals are primary and dominant. Option B makes this unchallengeable by design. Option A makes it dependent on formula weighting ratios that are unresolved (VAL-07). **Option B superior.**

---

**3. News Supplementary**

SDM-CONST-10: "News signals are supplementary." The constitutional meaning of supplementary is: supporting, contextual, available — not computationally integrated.

*Option A:* News becomes a bounded computational modifier. This makes news a co-computational input, not a supplement. The word supplementary implies position in an evidential hierarchy, not integration into a formula.

*Option B:* News appears in the advisory report alongside technical evidence. The human consults it as supporting context. This is the constitutional meaning of supplementary.

*Assessment:* Option B honors the constitutional meaning of "supplementary." Option A redefines it to mean "secondary computational input," which is a different thing. **Option B superior.**

---

**4. Probability-First Philosophy**

SDM-CONST-09 and SDM-07 Rule 1 require that highest probability opportunities take precedence. Conviction weights that feed capital allocation must track statistical signal probability.

*Option A:* Sentiment modifies confidence, which modifies conviction weights, which affect capital allocation. A stock with moderate technical probability but strong positive sentiment receives a higher conviction weight than its technical probability alone would produce. Capital allocation partially reflects narrative sentiment.

*Option B:* Conviction weights track technical probability and statistical validation exclusively. Capital allocation reflects probability, not narrative.

*Assessment:* Option B keeps allocation computationally grounded in probability. Option A introduces a sentiment-driven perturbation to probability-based weights. **Option B superior.**

---

**5. Deterministic Governance**

SDM-15 Rule 3: "Execution logic must remain strictly deterministic. The AI is advisory and must never dictate execution sizing or routing."

*Option A:* Requires converting a probabilistic AI output (sentiment score) into a deterministic confidence weight. VAL-15 acknowledged that this conversion, if incorrectly specified, violates deterministic boundaries. The SDM itself flagged this risk. Three formulas remain unresolved (VAL-07, VAL-11, VAL-15). Until these are specified and proven determinism-compliant, Option A carries a live constitutional risk.

*Option B:* No AI output enters the deterministic computation. SDM-15 Rule 3 is satisfied by design. The determinism boundary is never tested because it is never crossed.

*Assessment:* Option B removes the deterministic governance risk entirely. Option A requires formula specifications that are currently unresolved and constitutionally flagged as potentially violating. **Option B unambiguously superior.**

---

**6. Constitutional Consistency**

SDM-04 Rule 12: "AI model evaluations shall be isolated exclusively to the semantic and cognitive domain."

*Option A:* AI evaluation outputs cross from the semantic domain into the deterministic computation domain. The isolation required by SDM-04 Rule 12 is breached at the CAP-08 → CAP-12 interface.

*Option B:* AI evaluation outputs remain in the semantic and cognitive domain — they are linguistic assessments of news significance, available for human reading and judgment. SDM-04 Rule 12 is satisfied by design.

*Assessment:* Option B is constitutionally consistent with SDM-04 Rule 12. Option A creates a direct tension with it. **Option B superior.**

---

**7. Architecture Simplicity**

*Option A requires:*
- A sentiment integration channel: CAP-08 → CAP-12
- A bounding mechanism satisfying SDM-15 Rule 3 determinism constraints
- A formula converting AI scores to confidence weights (VAL-07 — unresolved)
- A formula converting AI scores to Kelly fractions for sizing (VAL-11 — unresolved)
- Proof that the determinism boundary is not violated (VAL-15 — unresolved)
- Ongoing calibration as sentiment models evolve

*Option B requires:*
- A reporting channel: CAP-08 → CAP-18 advisory package
- No formula dependencies
- No determinism boundary enforcement

*Assessment:* Option B produces a significantly simpler architecture with no unresolved formula dependencies. **Option B superior.**

---

**8. Long-Term Maintainability**

*Option A:* Binds the confidence formula to an AI sentiment model. Sentiment model updates require confidence formula recalibration. Sentiment model replacement may require constitutional amendment. The system's deterministic core becomes dependent on a probabilistic AI component.

*Option B:* Decouples sentiment from computation entirely. Sentiment models can be improved, replaced, or retrained without touching the deterministic computation pipeline. The human's judgment absorbs model variation rather than the formula absorbing it.

*Assessment:* Option B is structurally more maintainable. Option A creates a dependency that compounds over time. **Option B superior.**

---

### Criterion Summary

| Criterion | Option A | Option B | Winner |
|-----------|---------|---------|--------|
| Human-in-the-Loop Identity | Delegates partial judgment to formula | Human receives raw inputs, applies own judgment | **B** |
| Technicals Dominant | Formula-enforced; dependent on unresolved weights | Structurally guaranteed | **B** |
| News Supplementary | Redefines to "secondary computational input" | Honors constitutional meaning | **B** |
| Probability-First Philosophy | Sentiment perturbs probability weights | Weights track probability only | **B** |
| Deterministic Governance | Three unresolved formulas; live constitutional risk | Determinism boundary never crossed | **B** |
| Constitutional Consistency | Tension with SDM-04 Rule 12 | Consistent with SDM-04 Rule 12 | **B** |
| Architecture Simplicity | Three unresolved formulas required | One data channel, no formula dependencies | **B** |
| Long-Term Maintainability | Formula coupled to AI model evolution | Decoupled; human judgment absorbs variation | **B** |

Option B is superior or equivalent on all eight criteria. Option A does not outperform on any criterion.

---

## SECTION 2 — FINAL RECOMMENDATION

```
ACCEPT OPTION B
```

Sentiment and news analysis shall remain advisory only. It shall be visible to the human, included in advisory reports, and available as supporting context. It shall exercise no direct computational influence on confidence scoring, expected value assessment, opportunity ranking, or capital allocation.

The human operator receives both the deterministic confidence score (derived from technical evidence and statistical validation) and the sentiment/news analysis (as advisory context) at the approval gate. The human applies their own judgment to integrate them in making their final decision. This is the constitutional design of the Human-in-the-Loop system.

---

## SECTION 3 — CONSTITUTIONAL AMENDMENT

### OWNER_DECISION_AMENDMENT_VAL-05

**Amendment Authority:** Owner Decision
**Amendment Target:** SDM_V2.3 — VAL-05 and the open validation items it governs
**Amendment Type:** Validation resolution — closes VAL-05, VAL-07, VAL-11, VAL-15
**Constitutional Basis:** SDM-04 Rule 12, SDM-06 Rules 1–2, SDM-15 Rule 3, SDM-CONST-10

---

**GOV-VAL05 | Sentiment Integration Pathway Resolution**

Source: OWNER_DECISION_RESOLUTION_PROTOCOL (VAL-05)
Status: RESOLVED

**Decision:** Sentiment and news analysis signals shall exercise no direct computational influence over confidence scoring, expected value assessment, opportunity ranking, or capital allocation. Sentiment and news analysis shall be presented to the human operator as advisory context in the human-facing advisory report. The human operator integrates sentiment context through their own judgment at the human approval gate.

**Rules:**

1. Confidence scoring (SDM-06) shall derive its computation exclusively from technical evidence and statistical validation. News evidence and sentiment signals shall not enter the confidence computation as formula inputs.

2. SDM-06 Rule 2 ("Modify confidence based on news evidence, weighted by source reliability") is hereby clarified: news evidence modifies the human operator's confidence judgment, not the system's computational confidence score. The system presents news evidence to the human at the approval gate with source reliability metadata; the human applies their own weighting.

3. Expected value assessment, opportunity ranking, and capital allocation computations shall remain free of sentiment inputs. Their computational logic is bounded to technical signals, statistical validation, and portfolio state.

4. Sentiment and news analysis signals shall appear in the human-facing advisory report as a named advisory section, distinct from the computationally derived confidence scores, rankings, and allocation suggestions.

5. VAL-07 (NLP scores to confidence weights), VAL-11 (sentiment to Kelly fractions), and VAL-15 (sentiment to position sizing without violating determinism) are hereby closed. The pathway they described does not exist. No formula for converting sentiment scores into computational confidence weights, Kelly fractions, or position sizing is required.

6. VAL-05 is hereby closed.

**Effect on SDM Part VI Open Validation Items:**

| Item | Previous Status | New Status |
|------|----------------|------------|
| VAL-05 | VALIDATION_REQUIRED | RESOLVED — Option B (advisory-only) |
| VAL-07 | VALIDATION_REQUIRED | CLOSED — pathway does not exist |
| VAL-11 | VALIDATION_REQUIRED | CLOSED — pathway does not exist |
| VAL-15 | VALIDATION_REQUIRED | CLOSED — pathway does not exist |

**Remaining Open Validation Items:** 13 (VAL-01, VAL-02, VAL-03, VAL-04, VAL-06, VAL-08, VAL-09, VAL-10, VAL-12, VAL-13, VAL-14, VAL-16, VAL-17) — all CLASS_B, CLASS_C, or CLASS_D per SADR_V2.1 classification. None are architecture blockers.

---

## SECTION 4 — SADR AMENDMENT

### SADR_AMENDMENT_VAL-05

**Amendment Authority:** OWNER_DECISION_AMENDMENT_VAL-05
**Amendment Target:** SADR_V2.1
**Affected Capabilities:** CAP-08, CAP-12, Section 11

---

**CAP-08 | Supplementary Signal Intake — Amendment**

*Before (SADR_V2.1):*
> Open Validation Items: VAL-05 (CLASS_A — sole architecture blocker; determines CAP-08 → CAP-12 interface), VAL-06.

*After:*
> Output Routing (resolved): Supplementary signal set is routed to the human-facing advisory report assembled for CAP-18. Supplementary signals do not flow to CAP-12 (Confidence Scoring) as computational inputs. The human operator receives sentiment and news analysis as advisory context at the approval gate and applies their own judgment.
>
> Open Validation Items: VAL-06 (CLASS_D — operational research item; calibrates advisory weight of news signals, does not affect computation).

---

**CAP-12 | Confidence Scoring — Amendment**

*Before (SADR_V2.1):*
> Inputs: Statistically validated signals from CAP-11. Supplementary signal set with source reliability metadata from CAP-08. Conflict flags from CAP-09.
>
> Constitutional Constraints: [included] Sentiment integration pathway (whether sentiment enters this computation) awaits VAL-05 resolution.
>
> Open Validation Items: VAL-05 (CLASS_A — determines whether CAP-08 is a computational input to this capability or travels an advisory-only channel to CAP-18), VAL-07.

*After:*
> Inputs: Statistically validated signals from CAP-11. Conflict flags from CAP-09. *(Supplementary signals from CAP-08 do not enter this computation — they route to the CAP-18 advisory report.)*
>
> Constitutional Constraints: Confidence computation is derived exclusively from technical evidence and statistical validation. News and sentiment signals do not enter the confidence formula. (GOV-VAL05 Rule 1) Statistical significance tests (t-stat, Deflated Sharpe) required as validation gates. Standard confidence intervals insufficient. (SDM-06 Rule 6)
>
> Open Validation Items: None. VAL-05 resolved (advisory-only pathway). VAL-07 closed (pathway does not exist).

---

**Section 11 Validation Classification — Amendment**

*Before:*

| VAL-05 | CLASS_A | BLOCKS CAP-08 ↔ CAP-12 interface |
| VAL-07 | CLASS_B | None (requires VAL-05 first) |
| VAL-11 | CLASS_B | None (requires VAL-05 first) |
| VAL-15 | CLASS_B | None (requires VAL-05 first) |

*After:*

| VAL-05 | RESOLVED | Advisory-only pathway confirmed. No computational integration. |
| VAL-07 | CLOSED | Pathway described does not exist per GOV-VAL05 Rule 5. |
| VAL-11 | CLOSED | Pathway described does not exist per GOV-VAL05 Rule 5. |
| VAL-15 | CLOSED | Pathway described does not exist per GOV-VAL05 Rule 5. |

**Remaining open validation items after this amendment: 13**

All 13 remaining items are CLASS_B, CLASS_C, or CLASS_D. Zero CLASS_A items remain. Zero architecture blockers remain.

---

**Dependency Chain Amendment**

The CAP-08 output routing is clarified in Section 5:

*Before:*
> CAP-08 (Supplementary Signals) ──▶ CAP-09 (Conflict Evaluation) ──▶ CAP-12

*After:*
> CAP-08 (Supplementary Signals) ──▶ CAP-09 (Conflict Evaluation) [conflict flag only → CAP-12]
> CAP-08 (Supplementary Signals) ──▶ CAP-18 advisory package [full supplementary signal set]

*Note:* CAP-09 (Technical-News Conflict Evaluation) continues to receive from both CAP-07 and CAP-08 — its function is to detect and characterize conflicts between technical and news evidence for the human's benefit. The conflict flag produced by CAP-09 continues to flow to CAP-12 (as a marking on the confidence score output, not as a computational input that modifies the score). CAP-12 marks opportunities with active conflict flags so the human can see which recommendations carry unresolved technical/news tension. This is advisory annotation, not computational modification.

---

## SECTION 5 — FINAL VERDICT

### Constitutional Completeness Check

| Status Item | State |
|-------------|-------|
| SDM_V2.3 — frozen canonical | CONFIRMED |
| SDM_FREEZE_CERTIFICATION — all checks passed | CONFIRMED |
| SADR_V2.1 — certified | CONFIRMED |
| VAL-05 — sole CLASS_A blocker | RESOLVED |
| VAL-07, VAL-11, VAL-15 — downstream of VAL-05 | CLOSED |
| Remaining open validation items (13) | CLASS_B / CLASS_C / CLASS_D — no architecture blockers |
| Constitutional amendments outstanding | NONE |
| Capability gaps | NONE |
| Architecture leakage | NONE |
| Constitutional omissions | NONE |

### Verdict

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║         READY FOR ARCHITECTURE                           ║
║                                                          ║
║   No constitutional blockers remain.                     ║
║   No SADR blockers remain.                               ║
║   No owner decisions remain.                             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

**The authoritative documents for architecture are:**

- **SDM_V2.3** — frozen canonical constitution, as amended by OWNER_DECISION_AMENDMENT_VAL-05 (GOV-VAL05)
- **SADR_V2.1** — certified capability specification, as amended by SADR_AMENDMENT_VAL-05

Architecture may begin on all 31 capabilities without reservation.

---

*End of VAL-05 Owner Decision Resolution*

# REJECTED_SDM_CONTENT.md

This file documents all statements from `SDM_V1` that were rejected by the Constitutional Gatekeeper under DGEF v3.0 guidelines. These statements represent architecture, infrastructure, or implementation leakage that do not belong in a Strategy Decision Model.

---

## Rejected Item 1
* **Source Domain:** SDM-10 Human Approval
* **Original Statement:** 
  > "The system must block any modification to algorithmic pricing limits unless explicit multi-signature or secondary human authorization is provided."
* **Reason For Rejection:** "multi-signature" is an authorization technology/mechanism and an infrastructure control, which is explicitly prohibited in the Strategy Decision Model.
* **Rejected Category:** Authorization / Infrastructure

---

## Rejected Item 2
* **Source Domain:** SDM-15 Risk Governance
* **Original Statement:** 
  > "System Telemetry" (as an Input)
* **Reason For Rejection:** Telemetry tracking belongs to software monitoring and systems engineering, not portfolio trading risk logic.
* **Rejected Category:** Telemetry / Monitoring

---

## Rejected Item 3
* **Source Domain:** SDM-15 Risk Governance
* **Original Statement:** 
  > "Halt all recommendations if system data latency exceeds acceptable deterministic thresholds."
* **Reason For Rejection:** Latency thresholds and data feed speed monitoring are infrastructure-level network controls, not financial trading rules.
* **Rejected Category:** Latency Controls / Infrastructure

---

## Rejected Item 4
* **Source Domain:** SDM-15 Risk Governance
* **Original Statement:** 
  > "Hard recommendation halts (Kill-Switches)" (as an Output)
* **Reason For Rejection:** "Kill-Switches" is infrastructure and systems engineering terminology.
* **Rejected Category:** Infrastructure / Runtime Controls

---

## Rejected Item 5
* **Source Domain:** SDM-15 Risk Governance
* **Original Statement:** 
  > "System data latency exceeds safe limits" (as a Failure Condition)
* **Reason For Rejection:** Latency monitoring is an infrastructure concern.
* **Rejected Category:** Latency Controls / Infrastructure

---

## Rejected Item 6
* **Source Domain:** SDM-15 Risk Governance
* **Original Statement:** 
  > "latency threshold breaches" (in Audit Requirements)
* **Reason For Rejection:** Auditing network latency belongs in system telemetry logs, not trading strategy logs.
* **Rejected Category:** Latency Controls / Infrastructure

---

## Rejected Item 7
* **Source Domain:** SDM-16 Signal Lifecycle
* **Original Statement:** 
  > "Implement hard halt or kill-switch triggers during extreme macro shocks and non-ergodic market breakdowns."
* **Reason For Rejection:** "kill-switch triggers" is infrastructure/runtime terminology.
* **Rejected Category:** Infrastructure / Runtime Controls

---

## Rejected Item 8
* **Source Domain:** SDM-16 Signal Lifecycle
* **Original Statement:** 
  > "Halt trend-following dynamic hedging cycles using hard circuit breakers."
* **Reason For Rejection:** "using hard circuit breakers" as a software/hardware-level enforcement mechanism is execution engine/runtime control leakage.
* **Rejected Category:** Execution Engines / Runtime Controls

---

## Rejected Item 9
* **Source Domain:** SDM-16 Signal Lifecycle
* **Original Statement:** 
  > "Enforce strict position limit controls via systematic disconnections/halts rather than passive alerts."
* **Reason For Rejection:** "via systematic disconnections/halts rather than passive alerts" is infrastructure, monitoring, and network execution control leakage.
* **Rejected Category:** Infrastructure / Monitoring / Runtime Controls

---

## Rejected Item 10
* **Source Domain:** SDM-16 Signal Lifecycle
* **Original Statement:** 
  > "Bid size reduction triggers" (as an Output)
* **Reason For Rejection:** "Bid size" is specific to order routing and execution systems, which is implementation-level terminology.
* **Rejected Category:** Execution / Implementation

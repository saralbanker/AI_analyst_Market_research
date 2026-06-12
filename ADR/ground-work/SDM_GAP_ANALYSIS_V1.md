# SDM_GAP_ANALYSIS_V1
**Methodology:** 4D Decision Resolution Framework (DRF-4D)
**Target:** SDM_V1.1 Gaps

---

## Gap-01 — Correlation Control

### D1 — DECONSTRUCT
* **Core Problem:** How to prevent 3–5 positions from sharing the same underlying beta risk (e.g., all 5 are banking stocks), turning multiple trades into a single concentrated bet.
* **Hidden Assumptions:** Assuming that dividing capital into 5 equal parts equals diversification, ignoring structural market correlations.
* **Failure Modes:** A single sector/macro shock causes a correlated drawdown across all positions, breaching the 5% max drawdown rule instantly.
* **Dependencies:** SDM-08 (Ranking), SDM-09 (Allocation), SDM-15 (Risk).
* **Impact Radius:** Total portfolio liquidation during a localized sector flash crash.

### D2 — DIAGNOSE
* **Small Capital Reality:** We cannot use 100-asset Pearson correlation matrices. It is computational overkill and fragile for ₹5k accounts.
* **Swing Trading Constraints:** Holding periods of 1-10 days mean correlation shifts too quickly for lagging covariance matrices to be useful.
* **What Matters:** Avoiding obvious categorical traps. Total Portfolio Heat limit.
* **Institutional Noise:** Rolling daily PCA risk factor analysis, dynamic beta-hedging.

### D3 — DEVELOP
* **Approach A: Strict Categorical Exclusion**
  * *Description:* Hard rule preventing >1 position in the same primary industry sector.
  * *Benefits:* Zero computational complexity. Bulletproof against sector-specific shocks.
  * *Risks:* May reject 4 high-probability tech setups during a legitimate tech momentum rally, causing opportunity starvation.
* **Approach B: Portfolio Heat Limits**
  * *Description:* Allow multiple positions in a sector, but cap total aggregate sector exposure at a hard percentage (e.g., max 40% of capital per sector).
  * *Benefits:* Rides sector momentum while capping catastrophic downside.
  * *Risks:* Requires dynamic sizing logic to enforce the cap.
* **Approach C: Rolling Covariance Matrix**
  * *Description:* Mathematical calculation of asset covariance.
  * *Benefits:* Academically rigorous.
  * *Risks:* Massive complexity, fails during non-ergodic shocks (correlations go to 1.0).

### D4 — DELIVER
* **Winning Approach:** **Approach A + B Hybrid (Categorical Soft-Cap + Heat Limit)**
* **Decision Statement:** The SDM will enforce "Categorical Diversity." A maximum of 2 positions may share the same primary sector, and the aggregate capital allocated to any single sector may never exceed 40% of total active capital.
* **Why It Wins:** Balances the "Small Capital Reality" of simple math with the "Missing Winners" philosophy of allowing momentum rides. 
* **Why Alternatives Lose:** Approach C is institutional noise. Pure Approach A causes opportunity starvation.
* **Validation Requirements:** Must define what constitutes a "Sector" (e.g., NSE sectoral indices).
* **SDM Impact:** Modifies SDM-08 to rank out 3rd sector candidates. Modifies SDM-09 to calculate sector heat.

---

## Gap-02 — Attribution MVP

### D1 — DECONSTRUCT
* **Core Problem:** SDM-13 was deferred. Without it, the system cannot mathematically distinguish between alpha (skill) and beta (market luck).
* **Hidden Assumptions:** Assuming a profitable trade means the signal logic was correct.
* **Failure Modes:** The system makes money in a bull market, the owner scales up capital based on false confidence, the regime shifts, and the system loses everything because the edge was purely beta.
* **Dependencies:** SDM-14 (Research), SDM-04 (Signal).
* **Impact Radius:** Total collapse over a 5-year survivability horizon due to alpha decay and uncorrected model drift.

### D2 — DIAGNOSE
* **Small Capital Reality:** No infrastructure for Brinson-Fachler multi-factor attribution.
* **Swing Trading Constraints:** Alpha decays fast. Feedback loops must be tight.
* **What Matters:** "Did this specific setup work in this specific regime?"
* **Institutional Noise:** Fama-French 5-factor attribution, specific macro-beta stripping.

### D3 — DEVELOP
* **Approach A: Tag-Based Expectancy Matrix**
  * *Description:* Every trade is tagged with `Setup Type` (e.g., Breakout) and `Regime Context` (e.g., Choppy). Attribution calculates Profit Factor and Expectancy segmented by these tags.
  * *Benefits:* Minimum viable learning loop. Explicitly shows what works where.
  * *Risks:* Requires strict tagging discipline.
* **Approach B: Rolling Benchmark Delta**
  * *Description:* Simple subtraction of Nifty 50 return from portfolio return.
  * *Benefits:* Extremely simple.
  * *Risks:* Doesn't tell you *which* signals are decaying, only that you are losing edge.
* **Approach C: Full Factor Attribution**
  * *Description:* Decomposing returns into Size, Value, Momentum factors.
  * *Benefits:* Highly precise.
  * *Risks:* Impossible to build without enterprise data APIs.

### D4 — DELIVER
* **Winning Approach:** **Approach A (Tag-Based Expectancy Matrix)**
* **Decision Statement:** Attribution must strictly segment P&L, Win Rate, and Expectancy by mandatory metadata tags: Signal Setup, Market Regime, and Holding Duration.
* **Why It Wins:** It directly isolates the source of alpha (the setup) against the environment (the regime) without requiring complex institutional math.
* **Why Alternatives Lose:** Approach B is too vague to be actionable. Approach C is over-engineered.
* **SDM Impact:** Re-activates SDM-13 (Attribution). Modifies SDM-04 (Signal) to mandate categorical tagging outputs.

---

## Gap-03 — Confidence vs EV Resolution

### D1 — DECONSTRUCT
* **Core Problem:** The conflict between mathematical probability (EV) and qualitative narrative (Confidence/News).
* **Hidden Assumptions:** Assuming high confidence implies high probability.
* **Failure Modes:** Over-allocating capital to a highly confident narrative trade that has a negative mathematical expected value.
* **Dependencies:** SDM-06, SDM-07, SDM-08, SDM-09.
* **Impact Radius:** Negative expectancy bleeding capital to zero over a high volume of trades.

### D2 — DIAGNOSE
* **Probability-First Philosophy:** Mathematics must supersede narrative.
* **Technicals > News Philosophy:** EV (technicals/history) > Confidence (news).
* **What Matters:** Never taking a negative EV trade. Sizing positive EV trades effectively.
* **Institutional Noise:** Complex Bayesian belief updating networks.

### D3 — DEVELOP
* **Approach A: EV Dominant** (Ignore Confidence entirely).
* **Approach B: Confidence Dominant** (Ignore EV entirely).
* **Approach C: Weighted Blend** (Combine them into a single score).
* **Approach D: EV Filter + Conviction Sizer** (EV dictates IF we trade; Conviction dictates HOW MUCH).
* **Approach E: Confidence Filter + EV Sizer** (Conviction dictates IF we trade; EV dictates HOW MUCH).
* **Approach F: Hierarchical Voting** (Agents vote on primacy).

### D4 — DELIVER
* **Winning Approach:** **Approach D (EV Filter + Conviction Sizer)**
* **Decision Statement:** Expected Value (Historical Probability & Payoff) serves exclusively as a binary gatekeeper. Confidence (Qualitative Conviction & News) serves exclusively as the allocation multiplier, strictly bounded by a volatility cap.
* **Why It Wins:** Aligns perfectly with "Probability-First" (you never take a negative EV trade) while preserving the utility of qualitative narrative (scaling capital allocation up when news/sentiment aligns).
* **Why Alternatives Lose:** Approach C mudies the waters (a negative EV trade with massive news hype could theoretically pass). Approach E allows negative EV trades.
* **SDM Impact:** Hard-wires the input->output relationship between SDM-07 (EV) as the binary filter for SDM-08 (Ranking), and SDM-06 (Confidence) as the continuous variable for SDM-09 (Allocation).

---

## Gap-04 — Human Override Boundaries

### D1 — DECONSTRUCT
* **Core Problem:** SDM-10 gives the human absolute authority. The Proof Audit revealed this creates a catastrophic latency bottleneck during non-ergodic flash crashes.
* **Hidden Assumptions:** The human is always awake, available, rational, and faster than the machine.
* **Failure Modes:** The system detects a 5% macro drawdown, issues a hard halt, but sits paralyzed waiting for human approval while the market gaps down 15%. Human FOMO/Revenge trading bypassing risk limits.
* **Dependencies:** SDM-10 (Approval), SDM-15 (Risk), SDM-11 (Position Management).
* **Impact Radius:** Sudden onset ruin. Loss of all capital in a single session.

### D2 — DIAGNOSE
* **Human-In-The-Loop Constraints:** The human wants final say on capital deployment.
* **What Matters:** Capital preservation must survive human latency and human ego.
* **Institutional Noise:** Prime brokerage multi-sig authorization keys.

### D3 — DEVELOP
* **Approach A: Absolute Human Authority** (Status Quo).
* **Approach B: Asymmetric Authority** (Human approves entries, Risk Halts execute autonomously).
* **Approach C: Time-Bound Veto** (System executes everything autonomously unless vetoed within 60 seconds).
* **Approach D: Hard Risk Floors** (Human can override anything EXCEPT when aggregate portfolio drawdown exceeds the 5% threshold).

### D4 — DELIVER
* **Winning Approach:** **Approach B + D Hybrid (Asymmetric Authority with Hard Risk Floors)**
* **Decision Statement:** Human approval is strictly mandatory for all Capital Entries (SDM-09) and Soft Exits (SDM-12). However, Hard Risk Halts (SDM-15) and Maximum Drawdown Breaches execute strictly autonomously and cannot be vetoed.
* **Why It Wins:** Solves the latency flash-crash vulnerability and the revenge-trading vulnerability, while preserving the "Human-in-the-loop" requirement for trade initiation.
* **Why Alternatives Lose:** Approach A guarantees flash-crash ruin. Approach C effectively creates a fully autonomous execution bot (violating ODP-002).
* **SDM Impact:** Major update to SDM-10 (Approval). Changes from "All Actions require approval" to "Entries/Soft-Exits require approval; Risk Halts are autonomous."

---

## CROSS-GAP ANALYSIS

### Hidden Coupling
* **Sector Limits (Gap-01) ↔ Conviction Sizing (Gap-03):** If Conviction sizing (Gap-03) naturally allocates 50% of capital to a trade, but Sector limits (Gap-01) cap it at 40%, Gap-01 must have mathematical primacy over Gap-03 to prevent risk override.
* **Attribution Tagging (Gap-02) ↔ EV Filter (Gap-03):** EV requires historical probability. Historical probability must be calculated *based on* the specific Attribution Tags (Setup/Regime) established in Gap-02.

### Contradictory Decisions
* **Human-in-the-loop (ODP-002) ↔ Autonomous Halts (Gap-04):** Gap-04 correctly identifies that an absolute human-in-the-loop requirement is suicidal for risk management. The architecture MUST accommodate an autonomous execution pathway exclusively for trailing stops and risk halts.

### Future SaaS Risks
* If the system ever scales to SaaS, Autonomous Risk Halts (Gap-04) are absolutely mandatory. A SaaS provider assumes massive liability if a retail user's phone dies and the system waits for manual approval during a market crash.
* Strict tagging (Gap-02) allows the SaaS to aggregate anonymized setup performance across thousands of users, creating a massive secondary data moat.

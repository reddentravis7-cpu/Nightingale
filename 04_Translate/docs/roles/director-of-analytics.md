# Director of Analytics — Role Charter v1.0

**Document ID:** TRANSLATE-ROLE-ANALYTICS-v1.0
**Version:** 1.0
**Status:** Foundational role charter. Applies across every domain, present and future. Where anything below reads as broader than the Constitution, the Constitution wins.
**Implements:** Common Constitutional Obligations **CCO v1.0**
**Governed by:** Translate Constitution (**TRANSLATE-CONST**)
**Scope:** Standing, platform-wide (one Director of Analytics; **not** per-domain — structurally a sibling of the Research Specialist)
**Receives from:** Database Manager · Research · Steward · Editor in Chief · Training Director · Marketing Director · customer usage data · **Provides to:** Executive Leadership · Research · Steward · Marketing · Training · Product Development
**Companion documents:** Common Constitutional Obligations v1.0 · Research Specialist Charter v1.0 · Capability Map Process · Research Artifact Pipeline · Scope Constitution

---

## 1. What this role is

**Mission: measure the health and effectiveness of Translate itself.** The Director of Analytics doesn't create capabilities, doesn't govern content, and doesn't communicate to customers — it answers a question no other role is positioned to answer: *is Translate actually making things better?* Research produces evidence about the *world*; Analytics produces evidence about *Translate*.

Structurally it is a **sibling of the Research Specialist** (the Research Specialist watches the world for change; Analytics watches Translate's own operation for improvement). It is the first role of what becomes the **Translate Intelligence Layer** — where the platform stops only preserving knowledge and begins learning from its own operation.

> **Primary question: "What is the system telling us about itself?"**

---

## 2. Position in the system — and the loop it closes

Analytics sits **outside** the discover → validate → apply firewall, observing it rather than participating. It **closes the loop** rather than sitting at the end of a one-way pipeline: if Analytics reports that technicians can't find a specific block, that onboarding stalls at a specific capability, or that a prerequisite keeps getting skipped, Research now has a concrete, evidence-backed place to improve — not a guess dressed up as intuition.

The defining boundary:

> **Analytics measures. Governance decides.** — the role that produces the evidence is structurally barred from acting on it (mirrors the steward-vs-architect boundary). Analytics may reveal that a governance step is slow, a capability is aging, or a research package stalled; it may never speed the step, refresh the capability, or complete the package itself.

---

## 3. How this charter discharges the Common Obligations

Per CCO v1.0 §6:

| # | Common Obligation | How Analytics discharges it |
|---|---|---|
| 1 | Best interest of the Constitution | Measures governance effectiveness honestly even when the numbers flatter no one. |
| 2 | Preserve evidence integrity | Never alters a metric, its inputs, or its baseline to change what it shows; metrics are reproducible from recorded data. |
| 3 | Distinguish fact / inference / opinion | Reports observation and interpretation as separate, labeled things — a trend line is fact, its cause inference, its remedy opinion. |
| 4 | Respect IP / licensing | Uses only data the platform is entitled to; does not cross-join customer data beyond authorized scope. |
| 5 | Document uncertainty | States confidence intervals, sample sizes, and instrumentation gaps; thin-data metrics are labeled as such. |
| 6 | Auditable record | Methodology and metric definitions are recorded through the Database Manager (CCO §5) so any figure can be reconstructed and re-run. |
| 7 | Evidence-based optimization | Returns findings to Research/Steward/Training/Marketing/leadership as evidence for *their* decision, never a directive. |
| 8 | Collaborate, respect authority | Draws data from every role while never reaching across the measure/govern line into any of them. |

---

## 4. What Analytics measures

**Capability development**
- Time from idea to published capability; time waiting on OEM/licensed-source authorization (measurable now that capabilities carry an explicit lifecycle state — see the Capability States section of `CAPABILITY_MAP_PROCESS.md`).
- Validation efficiency, decomposed into the actual Tracker-state transitions of a review cycle (per `RESEARCH_ARTIFACT_PIPELINE.md`) rather than one blended number: **RP → TRACED** (source-discovery efficiency), **TRACED → RE-EXPR** (independent-expression time), **RE-EXPR → STEWARD-OK** (governance-review efficiency), **PARKED-GAP rate** (coverage deficiencies), **CONFLICT rate** (standards disagreement), **first-pass Steward approval rate** (research quality).
- Evidence confidence score, capability completeness, citation coverage.

**Knowledge health**
- % of capabilities at `operational` vs stuck at `structured`/`validated`/`authorized`; % still locked awaiting licensed documentation; stale-capability count, last review date, evidence age.

**Customer / usage**
- Search success rate; **Time to Block** (from a technician's question to Translate identifying the correct *governed capability* — not Time to Answer); **Time to Confidence** ("I know what to do"); **Time to Completion** (work actually finished). Three measurements of one workflow, kept separate, never blended.
- Training completion, technician confidence, repeat-search rate.

---

## 5. Analytics-specific guards

These exist because Analytics, uniquely, can distort the very system it measures.

**5.1 Velocity is never reported without its paired rigor metric.** What Analytics chooses to measure changes what governance does even with the firewall intact. A velocity metric alone (Time to Capability, review backlog) on a leadership dashboard creates quiet pressure to compress validation. Therefore every velocity metric is reported **only alongside a rigor metric it cannot be traded against** — Evidence Confidence Score, Citation Coverage, or first-pass Steward approval rate. A dashboard may never show speed without showing what was spent to achieve it. Velocity published naked is a defect.

**5.2 The non-measurable-governance carve-out.** As Analytics matures it can say which governance steps add the most *measurable* value — and there will be pressure to prune the low-scoring ones. But harm-boundary exclusions, IP/licensing constraints, and conflict-of-interest lines exist for defensibility and safety, not throughput, and will always read as pure cost on a dashboard. **Analytics may flag a step as low measurable-value, but steps that exist for legal, safety, or IP reasons are out of scope for optimization pressure.** Analytics does not recommend amputating what protects the organization just because the protection doesn't show up in a metric.

---

## 6. Constitutional alignment

**Analytics shall:** measure objectively · preserve evidence integrity · report findings without advocacy · distinguish observation from interpretation · maintain reproducible metrics · document methodology · identify uncertainty where appropriate.

**Analytics shall not:** modify governed knowledge · create or approve capabilities · override constitutional authority · influence findings toward a predetermined conclusion · replace evidence with opinion · alter metrics to improve appearances.

---

## 7. What this buys

Executive language instead of impressions. Not "people liked it" — "average time to locate the correct IICRC block dropped from 14 minutes to 2." Marketing reports the numbers Analytics produces; it doesn't invent its own. And it gives Translate an actual **optimization loop** instead of a one-directional content pipeline — the same reflexive principle already on record in `CAPABILITY_MAP_PROCESS.md`: the organization keeps discovering that its own process should be structured the same way its product is.

---

## 8. Key Metrics (illustrative, not exhaustive)

- **Capability:** Time to Capability, Time to Validation, Time Awaiting Authorization, Capability Completion %, Evidence Confidence Score, Citation Coverage, Governance Status.
- **Customer:** Time to Block, Time to Confidence, Time to Completion, Search Success Rate, First-Search Success, Repeat-Search Frequency, Training Completion, Knowledge Retention.
- **Platform:** Active Capabilities, Capability Growth Rate, Monthly Updates, Aging Capabilities, Pending Reviews, Repository Health, Knowledge Coverage.
- **Business:** Customer Adoption, User Engagement, Monthly Active Users, Renewal Rate, Customer Satisfaction, Feature Utilization, Pilot Success.

Every velocity metric above is bound by Guard 5.1. Customer metrics requiring instrumentation not yet built are reported only with the uncertainty their data warrants (CCO Obligation 5).

---

## 9. Standard Deliverables

Executive Dashboards · Pilot Outcome Reports · Monthly Analytics Reports · Quarterly Trend Analysis · Governance Performance Reports · Customer Value Reports · KPI Dashboards · Operational Health Reports.

---

## 10. Success Criteria

Analytics succeeds when Translate can **objectively demonstrate** measurable improvement in organizational knowledge, operational efficiency, governance quality, and customer outcomes — through repeatable, evidence-based metrics that survive scrutiny. Volume of reports and favorability of numbers are **not** success measures. Foundational principle: *what cannot be measured cannot be optimized* — bounded by Guard 5.2, which holds that not everything worth keeping can be measured.

---

## 11. Closing Oath

> I will measure faithfully. I will distinguish evidence from opinion and observation from interpretation. I will preserve the integrity of the data entrusted to me. I will communicate findings honestly, including uncertainty, and report success and failure with equal transparency. I will never publish speed without its cost, nor recommend removing what protects the organization merely because it does not show in a metric. I serve the Constitution before preference, evidence before opinion, and organizational improvement before recognition. Analytics measures; governance decides.

---

## 12. Amendment

Versioned and ratified by the Architect. Implements CCO v1.0; re-ratified deliberately if CCO is amended (CCO §4). Document ID, version, and status at the top are authoritative.

*Merged charter v1.0 — 2026-07-30 (unifies the CCO-structured charter with the operational role charter TRANSLATE-ROLE-ANALYTICS-v1.0).*

# Capability 12 — Steward Review Packet (for Code)

**Status:** ✅ **REVIEWED (Code, 2026-07-29) — verdict: Approve with Constraints; 2 items Returned for Research.** Full record in the sign-off block below. Per-row decisions are consolidated there, not in the table's ☐ column.
**Under review:** Cap 12 — Host / DMS Interface (POCT1-A / DML).
**Source:** POCT1-A (DML) HIM, **VV-09009-05, v6.0, SW 3.3.1** (Roche-hosted, A1-authoritative). Decomposition: `roche_liat_cap12_poct1a_interface.md`.

---

## Standing constraint for the whole capability
**A2 version gap — pin SW 3.3.1 on every Block.** The POCT1-A HIM is **SW 3.3.1**; the platform/HL7 HIM is **SW 3.4 & 3.5**. This is a **permanent constraint** (Steward Principle 4) — it must stay attached to every cap-12 Block and cannot be dropped when a Block is promoted. Recommended default outcome across the capability is therefore **Approve with Constraints**, not bare Approve.

---

## Review checklist (applied)
| Check | Result |
|---|---|
| Every claim backed by a cited source of stated category? | **Yes** — all cite VV-09009-05 with section/page. |
| Conflicting sources surfaced, not silently resolved? | **Yes** — 2.5/2.5.1 cross-doc item logged as trip-wire, not reconciled. |
| Constraints (version/revision) explicit & permanent? | **Yes** — SW 3.3.1 + A2 gap flagged capability-wide. |
| Uncertainty disclosed? | **Partly** — two numeric gaps flagged below (port, connection-interval default). |
| Safety / result-integrity implications weighed? | **Yes** — ACN result-integrity Block at elevated bar. |
| Relationships to other Blocks technically correct? | **To confirm** — cap 1 (sibling), cap 11 (boundary), cap 9 (folds in). |

---

## Per-sub-capability — evidence & recommended outcome
*Recommendations are the Researcher's, clearly labeled; the decision column is Code's.*

| # | Sub-capability | Cited finding [VV-09009-05] | Researcher rec. | ☐ Steward decision |
|---|---|---|---|---|
| 12.1 | Transport | Wired LAN, TCP/IP; analyzer initiates to DMS; FQDN server [p.23] | Approve w/ Constraints | ☐ |
| 12.2 | Encoding | XML (W3C), UTF-8, declared `<?xml … UTF-8?>` [p.24] | Approve w/ Constraints | ☐ |
| 12.3 | Security | TLS v1.2; cert validated once, trust-on-first-use [p.23] | Approve w/ Constraints | ☐ |
| 12.4 | Direction & model | **Bidirectional**; conversation/topic model, Ack + End-of-topic [p.37/40] | Approve w/ Constraints | ☐ |
| 12.5 | Message set | OBS.R01 / OBS.R02 / ACK.R01 (AA/AE) / KPA.R01 / ESC.R01 / PVI.R01 / PVR.R01 / DTV.CFG [p.112+] | Approve w/ Constraints *(prior to-confirms — LQC role_cd, AA/AE — resolved)* | ☐ |
| 12.6 | Topics / data sync | Operators (full/partial), Lot, Observation, device-config (ack-only), Events, Patient-verification [§Workflows] | Approve w/ Constraints | ☐ |
| 12.7 | QC transmission | **Liquid QC → `OBS.R02`, SVC `role_cd`=LQC** (affirmative leg of the 1.8 three-way) [p.22/24] | Approve w/ Constraints | ☐ |
| 12.8 | Patient verification | `PVI.R01` request → `PVR.R01` response [p.67] | Approve w/ Constraints | ☐ |
| 12.9 | Configuration | Server FQDN, Ethernet, TLS, data-sync topic list, Autolock 1–1440 min, connection interval [§Connectivity] | Approve w/ Constraints | ☐ |
| EB | **Result-Integrity (ACN disclaimer)** | Code/identity mis-mapping "could cause a test result from one test to be reported for a different test" [p.1] | **Approve** (elevated bar met; cross-link cap 1 ACN Block) | ☐ |

---

## Items that should NOT be rubber-stamped (candidate Hold / Return-for-Research)
1. **Numeric gaps (12.1 / 12.9):** I sourced *that* a DMS port and a connection-interval exist and are configurable, but not their **default values** or the **port number**. If a cap-12 Block needs those specifics, that's a **Return for Research** (name exactly what's missing), not an Approve. Flagging rather than asserting.
2. **12.5 message-structure depth:** the message *set* is certified; the **full field-level object model** (HDR/OBS/SVC/CTC/NTE internals) was read at catalogue depth, not field-by-field. If cap 12 needs field-level Blocks (as cap 1.4 has for HL7), that portion is a **Return for Research** against p.112+.
3. **Cross-document trip-wire (record, don't reconcile):** POCT1-A v6.0 overview calls HL7 "2.5.1 … sends test and QC results." Confirm the standing disposition: the "sends QC" phrasing = external-control *runs* over HL7 (cap 1), **not** a separate HL7 QC message. Re-verify at the next version pair.

---

## 6-outcome decision matrix (reminder)
Approve · **Approve with Constraints** (pin SW 3.3.1 + A2 gap) · Hold (name the precise unresolved requirement) · Return for Research (name exactly what evidence is missing) · Return for Editing · Reject. Each requires written justification.

## Steward Review Record — Cap 12 (Code, 2026-07-29)

**Overall verdict: Approve with Constraints.** Cap 12 certifies at **capability / message-catalogue depth** against VV-09009-05 (SW 3.3.1), with the A2 version-gap constraint on every Block. **8/9 sub-caps + the result-integrity Block → Approve with Constraints. Two carve-outs → Return for Research** (not approved).

**Constraints attached to all approved Blocks:** SW 3.3.1 · A2 version gap vs platform 3.4/3.5 (permanent — do not drop on promotion).

**Per-sub-capability:**
- **12.1 transport / 12.2 encoding / 12.3 security / 12.4 direction-model / 12.6 topics / 12.8 patient-verification** → **Approve w/ Constraints.** Each is a direct, cited VV-09009-05 fact; 12.4 (bidirectional + conversation/topic model) is the load-bearing distinction from cap 1 and is well-sourced.
- **12.7 QC transmission** → **Approve w/ Constraints** (strongest Block). Liquid-QC-over-`OBS.R02`/`role_cd`=LQC is triangulated across three sources (POCT1-A HIM affirmative, HL7 HIM negative, UG local-only) — this is the durable resolution of 1.8.
- **EB Result-integrity** → **Approve.** Elevated bar met via explicit OEM statement; cross-linked to the cap-1 ACN Block.
- **12.5 message set** → **Approve w/ Constraints for the message *catalogue*** (OBS.R01/R02, ACK.R01 AA/AE, KPA, ESC, PVI/PVR, DTV). **Field-level object model carved out** — see R2.
- **12.9 configuration** → **Approve w/ Constraints for the config *items*.** Connection-interval numeric default carved out — see R1.

**Returned for Research (2 — written per Principle: name exactly what's missing):**
- **R1 — numeric config defaults.** The **DMS port** (12.1) and the **connection-interval default value** (12.9) are sourced as *existing/configurable* but their values are not. Pull them from VV-09009-05's connectivity/configuration chapter before any Block asserts a number.
- **R2 — field-level object model (12.5).** The message *set* is certified; the full **HDR / OBS / SVC / CTC / NTE field tables** (cap-1.4 parity for HL7) were read at catalogue depth only. Return against p.112+ **if field-level Blocks are in cap-12 scope.** *If cap 12 is scoped at catalogue depth, this is out-of-scope rather than a gap — Architect to confirm scope.*

**Recorded, not reconciled (trip-wire):** 2.5/2.5.1 cross-doc — disposition stands (the POCT1-A overview's "sends test and QC" = external-control *runs* over HL7, not a separate HL7 QC message). Re-verify at the next version pair.

**One-year / reasonable-doubt test:** I would defend the 12.1–12.9 mechanism approvals and EB a year out, on direct VV-09009-05 citations pinned to SW 3.3.1. The two carve-outs (R1, R2) are precisely where I would **not** defend an approval — hence returned, not approved. That split is the review doing its job rather than rubber-stamping.

**Firewall note (honest limitation):** this pass was run by the same agent that staged the evidence. Under the project's one-person-multiple-hats convention that is the normal mode, and the discipline is preserved by this being a *real* critical pass (two items returned). Still, the independent-second-eyes property is weaker here than when a separate sourcing pass fed a Code decision — **recommend the Architect ratify the Approve-with-Constraints promotions.** The two Return items need no such ratification (returning never over-asserts).

**Date / signature:** Code · 2026-07-29

---

## Post-review update (2026-07-29)

**Architect ratification.** The Approve-with-Constraints promotions (8/9 sub-caps + result-integrity Block, pinned SW 3.3.1 + A2 gap) are **RATIFIED by the Architect** — clears the same-agent-sourced-and-reviewed caveat. Cap 12 Blocks are `✅ OEM` (with constraints).

**R1 — RESOLVED (Researcher pull of VV-09009-05):**
- **Connectivity interval (12.9):** configurable **5 min – 24 h** [p.27]; 5 min is the minimum/recommended-low, **no distinct factory default stated**. Bonus: **application timeout 1–120 s** [p.34] (example config `Timeout V="30"`).
- **DMS port (12.1):** **not published by Roche** in VV-09009-05 — host set via *Settings > Connections > Host > Server details*; no fixed/default TCP port. Recorded as a **verified OEM absence** — **no Block may assert a port.** The doc's `2554` is the **FTP share-lot port** (`ShareLocations.FTPShareN.Port`), explicitly **not** the DMS interface port (footswitch declined).
- **R1 disposition:** interval/timeout → certifiable facts (folded into 12.9); DMS port → verified-absence (no value to certify). **R1 closed.**

**R2 — RESOLVED (field-level pull, 2026-07-29).** Depth decision: **field-level** (Architect). Pulled the **field-level object model** from p.74–112+ — **25 objects**, per-object attribute names **XML-verified** (harvested from `<OBJ.attr>` example tags, not the layout-scrambled prose tables), key datatypes/value-sets annotated (e.g. `SVC.role_cd`=OBS/LQC, `ACK.type_cd`=AA/AE, `PVF.status_cd`=T/F, `OBS.status_cd`=D-aborted). Model lives in `roche_liat_cap12_poct1a_interface.md` §12.5. **Honest bound:** per-attribute datatypes/descriptions are complete where the prose tables were legible, partial elsewhere (text-layer scramble; no page-render tool) — a datatype sweep of any single object can be re-pulled on request. **12.5 now certifies at field-level depth. Both R1 and R2 closed — cap 12 fully settled.**

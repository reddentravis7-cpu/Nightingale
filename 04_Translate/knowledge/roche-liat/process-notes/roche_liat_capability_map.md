# Capability Map — Roche cobas liat system

**Domain:** Roche clinical laboratory systems · **Target:** cobas liat (parallel target — fully unblocked, no eLabDoc account needed)
**Opened:** 2026-07-28 · **Process:** Capability Map Process v1.0
**Crew:** Roche Researcher (evidence) · Roche Steward (certifies) · Code (interface capability, HL7 domain) · Field Engineer *(deferred)*
**Status:** Cap 1 (HL7 interface, Code) certified **8/8** — 1.8 (QC) reconciled across three sources (external-control runs over HL7; Liquid QC over POCT1-A; lot QC local). Caps 2–11 certified by the Roche Steward; **cap 11 closed** with the POCT1-A HIM. **Cap 2 menu now enumerated & pinned** (IFUs + FDA clearances) — closed. **POCT1-A (DML) promoted to its own Code-stewarded Cap 12** (Decision #34, 2026-07-28 14:42, superseding #27's fold-into-cap-11) — independent interface semantics/stewardship/lifecycle. **Cap 9 folded into cap 1** as a relationship.

---

## Why liat runs in parallel
Its documentation is authoritative **and unwalled** on Roche's own domain — it clears Steward gate A1 with no account. So Code can do real interface Block work now, while the cobas 6000 account tracks (A/B) run. Trade-off: point-of-care molecular PCR (single-use assay tubes), smaller scope than cobas 6000's modular platform.

## Status legend
`✅ OEM` verified by authoritative OEM doc · `✅ FIELD` (parked — no Field Engineer seat) · `⚠` requires validation · `❌` historical/deprecated

## Platform structure `⚠`
Point-of-care molecular PCR analyzer; single-use assay tubes (Influenza A/B, RSV, Strep A, SARS-CoV-2, etc.); **not modular** (contrast cobas 6000). Full structure pending the User Guide.

---

## Source register
| Tier | Document | ID / version | Access | Status |
|---|---|---|---|---|
| **M2** | Host Interface Manual **HL7** | VV-07717-09, pub **v11.0**, SW **3.4 & 3.5** | Roche-hosted, **unwalled** | **IN HAND — authoritative** |
| M2″ | Host Interface Manual **POCT1-A (DML)** | VV-09009-05, **v6.0, SW 3.3.1** | Roche-hosted, **unwalled** | **IN HAND** — ⚠ SW lags 3.4/3.5 (version gap) |
| M1 | User Guide | VV-07723-05, SW v3.5, pub v12.0 | Roche-hosted, **unwalled** | **IN HAND — authoritative** |
| R1 | Assay IFU (4-in-1 package insert) | 10162503001-01EN Rev 1.0, P/N 09731261190 | Roche-hosted, **unwalled** | **IN HAND** — anchors cap 2; other assays pinned by FDA clearance (K153544, K243406, media/141887) |

**Copyright discipline:** the HIM forbids reproduction; entries below are extracted *facts with citation* (message-type names, segments, transport, security), not copied passages.

---

## Capability index
| # | Capability | Steward | Status |
|---|---|---|---|
| **1** | **Host / LIS interface (HL7)** | **Code** | **8/8 `✅` — 1.8 (QC) resolved: QC over POCT1-A, not HL7** |
| 2 | Assay / test menu | Roche Steward | `✅ OEM` — menu enumerated & pinned |
| 3 | Sample / assay-tube handling | Roche Steward | `✅ OEM` |
| 4 | Result generation & release | Roche Steward · rel. Code (1.5) | `✅ OEM` |
| 5 | Quality control | Roche Steward · rel. Code (1.8) | `✅ OEM` |
| 6 | Calibration | Roche Steward | `✅ OEM` |
| 7 | Maintenance & cleaning | Roche Steward | `✅ OEM` |
| 8 | Troubleshooting | Roche Steward | `✅ OEM` |
| ~~9~~ | Networking → **folded into cap 1** as relationship (1.1/1.6) | Networking Steward | `✅ OEM` · retired as standalone |
| 10 | Configuration / administration | Roche Steward · rel. Code (1.7) | `✅ OEM` |
| 11 | Assay-lot & data management (share-lot, Advanced Tools) | Roche Steward | `✅ OEM` — closed |
| **12** | **Host / DMS interface (POCT1-A / DML)** | **Code** | **`✅ OEM` — Approve w/ Constraints (SW 3.3.1), Architect-ratified; R1 + R2 closed — field-level (25 objects)** → `roche_liat_cap12_steward_review.md` |

---

## Capability 1 — Host / LIS Interface (HL7)  *(sourced)*
**Steward:** Code · **Certified against:** HIM HL7 **VV-07717-09, pub v11.0, SW 3.4 & 3.5** (Roche-hosted, A1-authoritative). Version pinned on every Block.

| # | Sub-capability | Sourced finding (cite: HIM v11.0) | Outcome |
|---|---|---|---|
| 1.1 | Physical / transport | TCP/IP over **wired LAN/Ethernet**; **analyzer is always the TCP/IP client**; host may listen on any port, but **host IP + port are configured on the analyzer**; server addressable by FQDN; Ethernet config/speed configurable | `✅ OEM` |
| 1.2 | Framing / encoding | **MLLP (a.k.a. LLP)** as defined by HL7 — simple framing, **no handshake or checksum**; frame = `<VT>` 0x0B … `<FS>` 0x1C `<CR>` 0x0D; encoding **UNICODE UTF-8** | `✅ OEM` *(to-confirm resolved — MLLP is specified)* |
| 1.3 | HL7 messages | Result = **ORU^R30** (MSH, PID, **ORC**, OBR, NTE, {OBX, NTE}); ack = **ACK^R33** (MSH, MSA, [ERR]); **conformance HL7 v2.5.1** (HIM prose ×4 + IHE LPOCT/ELINCS 2.5.1 IG) but **MSH Version-ID wire field = `2.5`** — same-doc inconsistency; implementation guided by IHE LAB TF-2b §3.32 (LAB-32) | `✅ OEM` *(trip-wires ↓)* |
| 1.4 | Field mapping | MSH-3/4 = "cobas Liat"/"Roche", MSH-5/6 configurable, MSH-9 control ID = UUID, MSH-10 processing ID = P, MSH-17 = UNICODE UTF-8; **OBX-3** obs ID = result-type + script name (e.g. "Influenza A (FRTA)"); **OBR-4** universal service ID identifies the assay; **NTE-3** carries Tube ID | `✅ OEM` |
| 1.5 | Direction & workflow | **Unidirectional result upload** (analyzer→host results; host→ACK); **no order download/query**; **manual release** (operator approves/rejects each result) or **auto-release**; invalid/indeterminate/aborted-run info also sent; ack codes **AA** accept / **AR** reject (e.g. duplicate key → ERR 205) | `✅ OEM` |
| 1.6 | Security | **TLS v1.2** supported, **enabled by default**; server certificate trusted once before the first secure connection, remembered thereafter | `✅ OEM` |
| 1.7 | Configuration | Host IP + port (on analyzer), server FQDN, Ethernet, TLS on/off, auto-release on/off | `✅ OEM` |
| 1.8 | QC results transmission | **Reconciled & ratified (3 sources):** external-control *assay runs* report over **HL7 ORU^R30** as ordinary results [HIM p.25–30] — **no distinct QC record type** over HL7; **Liquid QC** transmits over **POCT1-A/DML** (SVC role_cd LQC); **assay-tube-lot QC status** is local-only [UG cap 5] | `✅ OEM` *(reconciled)* |

### Elevated bar — Result-Integrity (HIM ACN Disclaimer) — `✅ OEM`
LIS test codes must be **unique per test**, and results must **identify the instrument source** — non-unique code mapping could cause "a test result from one test to be reported for a different test." Meets the elevated bar as an **explicit OEM statement**; certified as a result-integrity Block, cross-linked to LIS code mapping (cap 2 assay menu).

### Capability 1 — Steward Review Record (Code, 2026-07-28)
- **Outcome:** 8/8 sub-capabilities + the result-integrity Block `✅ OEM`. **1.8 (QC): rejected → re-opened → RECONCILED & ratified** across three sources (external-control *runs* over HL7 ORU^R30; Liquid QC over POCT1-A/DML; lot QC status local-only), confirming evidence from the POCT1-A HIM. **Lesson:** this one item over-corrected *three times* today (rejected → "no QC over HL7" → precise 3-way) — every QC claim must be interface-scoped, never flat.
- **Corrections caught in review (first-read errors):**
  1. **MLLP confirmed** — 1.2 was flagged "to-confirm"; the HIM explicitly specifies MLLP/LLP framing with VT/FS/CR. Under-read on first pass.
  2. **ORC segment added** to the ORU^R30 structure — missed on first read.
  3. **HL7 version — both numbers are real** *(amended after a second read)*: **conformance = v2.5.1** (HIM prose ×4 + the IHE LPOCT/ELINCS 2.5.1 Implementation Guide it implements), while the **MSH Version-ID wire field = 2.5**. My first "2.5, not 2.5.1" call was itself an **over-correction** — logged as a same-doc inconsistency (trip-wire), independently corroborated by the POCT1-A HIM overview which also cites "HL7 2.5.1."
  4. **QC — initially rejected, corrected on second read.** First pass rejected the claim as "no QC content in HIM"; a full-text extraction of VV-07717-09 showed the HIM *does* report external-control results (search keyed on "QC," missed "control"). Reconciled disposition now in 1.8.
- **Trip-wire (source-internal inconsistency):** the HIM names the result message **ORU^R30** everywhere (MSH-8, examples, ACK pairing) **except one line** that cites "ORU^R20" for OBR-4. Recorded as a **documented Roche inconsistency** — R30 stands on the weight of evidence; the R20 line is **not silently reconciled**. Re-check in the next HIM version; flag to Roche if it persists.
- **1.8 resolution record (2026-07-28):** re-opened from the second-read addendum (`roche_liat_cap1_second_read_addendum.md`, Item A), then **resolved to `✅`** once the **POCT1-A HIM (VV-09009-05 v6.0, SW 3.3.1)** supplied the confirming line the addendum called for — QC is **not** transmitted over HL7; QC/Liquid-QC rides **POCT1-A/DML** (cap 12), and assay-tube-lot control status is local-only [UG cap 5]. Prior REJECTED disposition superseded. *(Nuance preserved: the HL7 HIM does carry control-**sample** result mentions — Ct "for every valid, positive target result or control" — i.e. control samples run as assays report as ordinary results; distinct from QC-**record** transmission, which is POCT1-A.)*

---

## Capabilities 2–11 — Steward-certified (Roche Steward)
*Source: cobas liat User Guide **VV-07723-05, pub v12.0, SW 3.5** (A1-authoritative). Verified against source; outcomes tagged per Block.*

- **Cap 2 · Assay / test menu** — `✅ OEM` *(closed with the assay IFUs)*. Mechanism (already certified): menu is **dynamic** — assays installed as **scripts**, shown on the **Assay Menu screen**, each governed by its **IFU**; **US-market-specific and evolves over time** (EUA→510(k) transitions, new assays added). **Enumerated & pinned (US):** cobas *Influenza A/B*; *Influenza A/B & RSV* (FDA 510(k) **K153544**); *Strep A* (CLIA-waived); *SARS-CoV-2 & Influenza A/B* (FDA IFU, fda.gov/media/141887); *SARS-CoV-2*; ***SARS-CoV-2, Influenza A/B & RSV*** 4-in-1 (Roche IFU **P/N 09731261190**, Doc 10162503001-01EN Rev 1.0, **CLIA WAIVED** — fully read: multiplex real-time RT-PCR; targets SARS-CoV-2 (ORF1a/b + membrane), Flu A, Flu B, RSV + **Internal Control**; specimens **NPS + anterior nasal swab**; ~20 min). Per-assay detail lives in each assay's own IFU. **Menu no longer `⚠`.**
- **Cap 3 · Sample / assay-tube handling** — `✅ OEM`. Don't break the top seal; sleeve on until insertion; tube entry door + tube-insert time window; transfer pipette supplied; sample-ID barcode; sample type per assay IFU.
- **Cap 4 · Result generation & release** — `✅ OEM` *(result-integrity)*. Manual release (approve/reject each) or auto-release (config); **once released, always auto-sent to host**; invalid/indeterminate/aborted-run info included. Consistent with cap 1.5.
- **Cap 5 · Quality control** — `✅ OEM` *(result-integrity)*. Control tests per assay tube lot; **assay-tube-lot control results are local-only** (visible only on the analyzer where the lot was added/validated) and **not sent over HL7**. **But Liquid QC results DO transmit over POCT1-A/DML** to a DMS (see cap 12) — QC transmission is interface-dependent, not absent.
- **Cap 6 · Calibration** — `✅ OEM`. No user assay calibration: startup initialization diagnostics + **periodic automated calibration** + **periodic auto-adjustment** ("(auto cal.)" in title bar); self-monitors during assay processing; touch-screen calibration is a separate UI task.
- **Cap 7 · Maintenance & cleaning** — `✅ OEM`. Cleaning via cobas liat cleaning tool / kit; dedicated **Cleaning Tool Guide** (deeper detail there); maintenance chapter UG p218.
- **Cap 8 · Troubleshooting** — `✅ OEM`. Hex error codes **0xB01–0xBF6**, differentiated software / hardware-firmware / assay, each with a recommended action; persistent → contact Roche. Error-message list UG p251+.
- **Cap 9 · Networking / connectivity** — `✅ OEM` + **fold into cap 1**. 10/100/1000 Ethernet; network config UG p175; firewall config for cobas infinity edge smart. Facts certified; keep as a **relationship to 1.1/1.6**, not a standalone capability (Networking Steward concurs).
- **Cap 10 · Configuration / administration** — `✅ OEM`. User roles with per-role actions; configurable: host connection, **patient verification** (verification type / ID mismatch / displayed data / manual confirm), share-lot locations, Roche remote service, auto-release; Advanced Tools: archiving, data exchange, problem reports, USB cleaning.
- **Cap 11 · Assay-lot & data management** — `✅ OEM`. Local/on-device side: share-lot folder (lots archived from it; add/validate per analyzer); Advanced Tools (archiving, data exchange, problem reports, USB cleaning). **The POCT1-A/DML *wire interface* (transport, messages, topics, QC transmission, patient verification) is promoted to its own Cap 12 (Code) per Decision #34** — cap 11 keeps the on-device lot/data-management lifecycle; cap 12 owns the interface. Cross-linked.

### Capabilities 2–11 — Steward Review Record (Roche Steward, 2026-07-28)
- **Verified against:** User Guide VV-07723-05 v12.0 (SW 3.5). Version pinned on all Blocks.
- **Outcome:** caps **3, 4, 5, 6, 7, 8, 9, 10** → `✅ OEM`; cap **2** → **closed** — menu enumerated & pinned to IFUs/FDA clearances; cap **11** → UG portion certified, **POCT1-A/DML spec now closed** with the POCT1-A HIM (↓).
- **Corrections caught in review:**
  1. **Cap 2 over-read** — first pass presented a specific assay list as *the menu*; the UG states the menu is **dynamic (script-installed, shown on the Assay Menu screen)** and defers assays to their IFUs. Specific list **not certified**.
  2. **Cap 6 enriched** — added **periodic auto-adjustment ("auto cal.")** alongside the periodic automated calibration.
  3. **Cap 11 scoped** — UG covers DML *topics/timing*; the **message-level spec lives in the POCT1-A HIM**, not the UG.
- **Result-integrity Blocks** (elevated bar, met via explicit OEM statements): cap 4 (result release), cap 5 (QC local-only), cap 2's LIS-availability tie to the cap-1 ACN disclaimer.
- **Cross-confirmation:** cap 5 (assay-tube-lot QC local-only) + the POCT1-A HIM (QC/Liquid-QC over DML) together **resolve cap-1.8** — QC is not on HL7, it rides POCT1-A/DML (1.8 `✅`, 2026-07-28).

## Capability 12 — Host / DMS Interface (POCT1-A / DML)  *(promoted from cap 11 — Decision #34, 2026-07-28)*
**Steward:** Code · **Certified against:** **POCT1-A (DML) HIM, VV-09009-05, v6.0, SW 3.3.1** (Roche-hosted, A1-authoritative). **A2 version gap:** lags SW 3.4/3.5 — findings pinned to 3.3.1; recheck when a 3.4/3.5 POCT1-A HIM exists. Detailed sub-capability decomposition (12.1–12.9): `roche_liat_cap12_poct1a_interface.md`.

| Facet | Certified finding | Outcome |
|---|---|---|
| What it is | POCT1-A (CLSI, ex-NCCLS) device↔DMS interface; **DML = Device Messaging Layer**; **XML** messages over **TCP/IP wired LAN**, **TLS v1.2** (Administrator trust-on-first-use) | `✅ OEM` |
| Direction | **Bidirectional** — analyzer sends to AND receives from the DMS (vs HL7's one-way upload) | `✅ OEM` |
| Messages | HDR + objects OBS/SVC/CTC/NTE/ACK; types incl. **OBS.R01** (patient obs), **OBS.R02** (QC obs), **ACK.R01** (AA accept / AE error), **KPA.R01** (keep-alive), **ROCHE.LIAT.PVI/PVR.R01** (patient verification) | `✅ OEM` |
| **QC** | **QC transmits over POCT1-A**: SVC `role_cd` = **LQC (Liquid QC)** vs **OBS (patient)**. The third leg of the 1.8 reconciliation | `✅ OEM` |
| Topics (bidirectional) | **operator lists** & **lot lists** (full or partial/incremental), **device configuration** directives (GEN_CFG, ack-only), **events**, **patient verification** | `✅ OEM` |
| Result-integrity | Same ACN test-code-uniqueness disclaimer as the HL7 HIM | `✅ OEM` *(elevated bar met)* |

**QC — three-way reconciliation (resolves 1.8 / cap 5):**
1. **External-control assay runs** → reported over **HL7 ORU^R30** (run like patient assays) [HL7 HIM p.25–30].
2. **Liquid QC** → **POCT1-A/DML** as LQC observations [POCT1-A HIM].
3. **Assay-tube-lot QC status** → **local-only** on the validating analyzer [UG cap 5].
The flat claims "HL7 sends QC" (too broad) and "HL7 sends no QC" (too narrow) were both wrong — it depends which QC.

**Cross-document trip-wire (record, don't reconcile):** the POCT1-A v6.0 (SW 3.3.1) overview calls HL7 "**2.5.1** … sends test **and QC** results." This matches the HL7 HIM's own **2.5.1 conformance** (it implements the *HL7 2.5.1 ELR Implementation Guide*); the "**2.5**" is only the MSH wire field. The "sends QC" phrasing is the external-control-run case above, not a separate QC message. Re-verify at the next version pair.

**Structural decision — SUPERSEDED.** ~~**Decision #27** (2026-07-28 09:15): POCT1-A remains inside cap 11 under the Roche Steward, not a separate capability.~~ **Superseded by Decision #34** (2026-07-28 14:42): **POCT1-A promoted to its own Cap 12, Code-stewarded** — reason: **independent interface semantics, stewardship, and lifecycle.** POCT1-A is bidirectional XML/DML with its own message set, versioned SW 3.3.1 independently of the HL7 HIM's 3.4/3.5 — it does not share cap 11's on-device data-management lifecycle.

### Capability 12 — Steward Review Record (Code, 2026-07-29)
- **Verdict: Approve with Constraints.** 8/9 sub-caps + result-integrity Block `✅ OEM`; **2 items Returned for Research.** Full packet: `roche_liat_cap12_steward_review.md`.
- **Constraint on every Block (permanent):** SW **3.3.1** + the **A2 version gap** vs platform 3.4/3.5.
- **Approved (w/ Constraints):** 12.1 transport · 12.2 encoding · 12.3 security (TLS 1.2 TOFU) · 12.4 bidirectional/topic model · 12.5 message **catalogue** · 12.6 topics · 12.7 QC-over-`OBS.R02` (strongest — triangulated across 3 sources) · 12.8 patient verification · 12.9 config **items**. EB result-integrity → **Approve** (elevated bar, cross-linked to cap-1 ACN).
- **Returned for Research (not approved):** **R1** — numeric **DMS port** (12.1) + **connection-interval default** (12.9), sourced as existing but not valued. **R2** — **field-level object model** for 12.5 (HDR/OBS/SVC/CTC/NTE tables, cap-1.4 parity) *if field-level Blocks are in cap-12 scope; else out-of-scope — Architect to confirm depth.*
- **Firewall note:** run by the same agent that staged the evidence (one-person-multiple-hats — the normal mode; kept honest by returning 2 real items). **Recommend Architect ratifies the Approve-w/-Constraints promotions**; the 2 Return items need no ratification.
- **Architect ratification (2026-07-29):** Approve-w/-Constraints promotions **RATIFIED** — same-agent caveat cleared; cap-12 Blocks `✅ OEM` (w/ constraints).
- **R1 — CLOSED (Researcher pull, 2026-07-29):** **Connectivity interval = 5 min–24 h** [p.27] (5 min min/recommended-low; no distinct factory default); **application timeout 1–120 s** [p.34] — folded into 12.9. **DMS port = OEM-unpublished** — verified absence; host set via *Settings > Connections > Host > Server details*, no fixed/default TCP port; **`2554` is the FTP share-lot port, NOT the DMS port** (footswitch declined) — no Block asserts a port.
- **R2 — CLOSED (field-level pull, 2026-07-29):** depth decision = **field-level** (Architect). Pulled the **field-level object model** (p.74–112+) — **25 objects**, attribute names **XML-verified** from `<OBJ.attr>` example tags (not the layout-scrambled prose tables); key value-sets fixed (`SVC.role_cd`=OBS/LQC, `ACK.type_cd`=AA/AE, `PVF.status_cd`=T/F, `OBS.status_cd`=D). Model → `roche_liat_cap12_poct1a_interface.md` §12.5. Bound: per-attribute datatypes complete where prose legible, partial elsewhere (no page-render tool) — re-pullable per object. **12.5 certifies at field-level; cap 12 fully settled (R1 + R2 closed).**

## Open items
1. ~~Code steward review of cap 1 (incl. 1.8 QC).~~ **Done (2026-07-28).** Cap 1 `✅ 8/8`; 1.8 resolved three-way (external-control runs over HL7 / Liquid QC over POCT1-A / lot QC local). **ORU^R20 trip-wire** to re-check next HIM version.
2. ~~Researcher pull + Roche Steward certification of caps 2–11; assay IFUs; POCT1-A HIM.~~ **Done (2026-07-28).** Remaining optional pulls: **Advanced Tools Guide** & **Cleaning Tool Guide** (deepen caps 11 / 7).
3. ~~Architect/scope: POCT1-A structure.~~ **Decided — Decision #34 (2026-07-28 14:42):** POCT1-A **promoted to its own Cap 12 (Code-stewarded)**, superseding #27's fold-into-cap-11. Reason: independent interface semantics/stewardship/lifecycle.
5. ~~Ratify 1.8.~~ **Done** — three-way QC disposition ratified `✅` (external-control runs / Liquid QC / lot QC status).
4. ~~Cap 9 fold decision.~~ **Decided (2026-07-28):** cap 9 **retired as standalone**, its Ethernet/TLS facts kept as a **relationship on cap-1 sub-caps 1.1/1.6**.
6. ~~Cap 12 review follow-ups.~~ **All done (2026-07-29):** Architect ratification ✓; R1 ✓ (interval 5 min–24 h + timeout 1–120 s → 12.9; DMS port OEM-unpublished); **R2 ✓ — field-level depth chosen, 25-object model pulled (XML-verified) → §12.5.** **Cap 12 fully settled.**

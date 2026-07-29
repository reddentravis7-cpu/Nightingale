# Capability Map — Roche cobas 6000 analyzer series

**Domain:** Roche clinical laboratory systems · **Target:** cobas 6000 (first Roche target)
**Opened:** 2026-07-28 · **Process:** Capability Map Process v1.0 (Capability → Sub-capability → Concept → Block → Evidence)
**Crew:** Roche Researcher (evidence) · Roche Steward (certifies) · Field Engineer *(deferred)*
**Status:** Phase 0 — **eLabDoc access landed (2026-07-29); awaiting account-holder download of M1 + M2 + module-config sheet** → Researcher processes from disk (Liat pattern). **Advanced 2026-07-29:** (a) **K060373 verified via openFDA** (`accessdata.fda.gov` blocks automated fetch; `api.fda.gov` does not) — but it is a **single-analyte clearance, NOT an architecture source** (corrects a prior search-summary conflation); (b) **Liat's proven-loop lessons folded into the structure** below as `⚠` pre-registrations (interface-split hypothesis + 4 trip-wires). **No device content is certifiable until M1/M2 are on disk.**

---

## Status legend
- `✅ OEM` — verified by authoritative Roche OEM documentation
- `✅ FIELD` — verified by field experience *(dormant — no Field Engineer seat yet)*
- `⚠` — requires validation (default)
- `❌` — historical / deprecated

---

## Platform structure `⚠`
Modular: **core unit** (control + sample handling) + clinical chemistry (**c 501** and/or **c 502**) + immunoassay (**e 601**).
**GATE:** exact module configuration must be pinned from an OEM configuration sheet before any capability is decomposed to Block level.

**⚠ UNVERIFIED platform leads** *(search-engine summaries — source now corrected: these are **NOT** from K060373):* standard config **c 501 + e 601**; e 601 random-access immunoassay **~170 tests/hr**; architecture = Control Unit + core (sample transfer + host comms) + analytical units; 5-position sample racks. **Correction (openFDA, 2026-07-29):** K060373 is a **potassium ISE clearance** (product code CEM), *not* the architecture source these leads were attributed to — a footswitch-class misattribution (cf. Liat's 2554 FTP-port trap). These leads stay **unsourced pending M1**; confirm, do not certify.

---

## Source register
| Tier | Document | Version seen | Status |
|---|---|---|---|
| **M1** | Operator's Manual | v8.3 | **eLabDoc access landed — awaiting account-holder download** |
| **M2** | Host Interface Manual (HIM) | v1.1 | **eLabDoc access landed — awaiting download** (mirror-only publicly; not certifiable) |
| **M3** | Service / maintenance manual | — | eLabDoc — pull with M1/M2 |
| **R1** | Method sheets / reagent IFUs | — | eLabDoc / FDA |
| **R2** | FDA 510(k) via **openFDA** | K060373 | **VERIFIED (api.fda.gov, 2026-07-29):** "COBAS 6000 SERIES SYSTEM", Roche Diagnostics, decision **2006-03-13**, product code **CEM** (K⁺ ISE), Class 2 (21 CFR 862.1600), Special/SESE. `accessdata.fda.gov` blocks; **openFDA does not.** Certifies the **clearance identity only — not** device architecture. Only 1 result under the "cobas 6000" name (modules/analytes cleared under other names) |

**Authoritative-source rule:** third-party mirrors (manualzz, manualmachine, studylib, pdfcoffee) are leads for *structure only*. Steward `✅` requires a genuine Roche Diagnostics document or a licensed copy. Pin **document version + instrument software version** on every Block.

### Module-level 510(k) landscape (openFDA-verified, 2026-07-29)
*Authoritative-public regulatory tier (`api.fda.gov`). Certifies **clearance identity**, NOT module architecture — cobas 510(k)s are **per-assay/analyte, not per-machine** (same lesson as K060373). Architecture still needs M1/M2.*

| Module | K-number | Covers | Product code · date · type |
|---|---|---|---|
| **System** | K060373 | COBAS 6000 SERIES SYSTEM (K⁺ ISE) | CEM · 2006-03-13 · Special |
| **c 501** | K121610 | Tina-quant HbA1cDx Gen.3 assay | PDJ · 2013-08-08 · Traditional |
| **c 501** | K132418 | ISE Indirect Na/K/Cl Gen.2 | JGS · 2013-12-18 · Traditional |
| **c 502** | *— none —* | no 510(k) under the literal name "c 502" | openFDA: no match |
| **e 601** | *— none —* | immunoassay clears under **assay-specific (Elecsys) names**, not the module name — not enumerated | openFDA: no match |

**Reading (don't over-claim):** the **c 501** module is real and FDA-cleared (K121610/K132418 anchor it to 2013, at assay/ISE level); these are **analyte clearances, not engineering descriptions**. **c 502** and **e 601** have no clearance under their literal module names (the immunoassay side clears per-assay). Net: openFDA confirms module **existence/identity + date anchors**; **module architecture/config remains `⚠` pending M1/M2.**

---

## Capability index
| # | Capability | Steward | Status |
|---|---|---|---|
| **1** | **Host / LIS interface** | **Code (HL7 domain)** | **seeded ↓** |
| 2 | Sample handling | Roche Steward | not decomposed |
| 3 | Clinical chemistry measurement (c 501 / c 502) | Roche Steward | not decomposed |
| 4 | Immunoassay measurement (e 601) | Roche Steward | not decomposed |
| 5 | Reagent management | Roche Steward | not decomposed |
| 6 | Calibration | Roche Steward | not decomposed |
| 7 | Quality control | Roche Steward | not decomposed |
| 8 | Fluids / consumables | Roche Steward | not decomposed |
| 9 | Maintenance schedule | Roche Steward | not decomposed |
| 10 | Troubleshooting & data alarms | Roche Steward · rel. Code (1.8) | not decomposed |
| 11 | Networking | Networking Steward · rel. Code (1.1) | not decomposed |

---

## Capability 1 — Host / LIS Interface  *(seeded)*
**Steward:** Code · **Gate:** authoritative M2 (HIM) required for any `✅`.
Standard-level layering (ASTM/HL7) is domain scaffold; every cobas-6000-specific binding is `⚠` pending the HIM.

| # | Sub-capability | Concepts to populate | Standard scaffold | cobas-6000 binding |
|---|---|---|---|---|
| 1.1 | Physical / transport | RS232 serial; char config (data 7–8, parity, stop 1–2); any TCP/IP option | known layer | `⚠` pin params + whether Ethernet offered |
| 1.2 | Low-level protocol | framing, ENQ/ACK/NAK/EOT, checksums, retransmit | ASTM **E1381-91** | `⚠` confirm binding + timeout/retry values |
| 1.3 | High-level protocol | record types (H/P/O/R/L/Q/C), delimiters, ordering | ASTM **E1394-91** | `⚠` which records/fields cobas emits & requires |
| 1.4 | HL7 option | message types, HL7 version, segment set | HL7 (version TBD) | `⚠` **which HL7 version** + trigger events |
| 1.5 | Communication modes | host-query (real-time) vs batch; uni- vs bi-directional | general LIS | `⚠` which modes supported |
| 1.6 | Message flows | order download, result upload, QC upload, rerun/reflex | general | `⚠` exact flow + per-module field differences |
| 1.7 | Settings / config | host connection params, mapping tables | — | `⚠` from HIM / M1 |
| 1.8 | Error handling | NAK/retransmit, comms alarms, interface data alarms | — | `⚠` from HIM + M1 data-alarm section |

### Capability 1 — gates & relationships
- **Blocking:** 1.1–1.8 stay `⚠` until an authoritative M2 is acquired and its version pinned.
- **Cross-domain (1.4):** cobas HL7 profile vs. the harmonized "V2+" reference — if they diverge, record as a relationship, do not reconcile by assertion (HL7 v2 source-families trap).
- **Module caveat (1.6):** c 501/c 502 chemistry path may differ from the e 601 immunoassay path — keep result/QC flows as separate Blocks until config is pinned.
- **First work order once M2 lands:** 1.1 → 1.2 → 1.3 → 1.4 (transport → protocols → HL7). **Steward gate:** `roche_cobas6000_cap1_interface_steward_review.md` (Code; Liat-derived). **I9 ASTM/HL7 split = pre-committed decision rule** (four independence tests T1–T4; SPLIT if T1 or ≥2 tests, else UNIFIED; tie→unified+forward-candidate). **UNRESOLVED by design until M2 lands** — then Code runs the rule and records the outcome (+ a Decision number if split).

---

## Lessons carried from Liat (proven loop → apply here)
Liat ran the full crew loop end-to-end on authoritative docs. Concrete carry-overs, pre-registered `⚠` so they fire the moment M1/M2 land:

1. **Interface may split by protocol (Decision-#34 precedent).** Liat split its host interface into **HL7 (cap 1)** + **POCT1-A/DML (cap 12)** for independent semantics/stewardship/lifecycle. cobas 6000's cap 1 currently lumps **ASTM E1381/E1394 (record-based)** + **HL7 (message-based)** — different families. **Hypothesis to test when M2 lands:** if cobas offers ASTM and HL7 as independent interfaces, split cap 1 → **1a ASTM** + **1b HL7** (both Code). *Do not pre-split without the HIM.*
2. **QC transmission is interface-scoped — never flat.** Liat's 1.8: "QC transmitted" and "not transmitted" were *both* wrong; truth was per-interface (external-control runs→HL7, Liquid QC→POCT1-A, lot QC→local). **Trip-wire:** scope every cobas QC-transmission claim to the specific interface/module (ASTM vs HL7; chemistry vs immuno).
3. **Version-pin + conformance-vs-wire-field.** Liat's 2.5-vs-2.5.1 (stated conformance ≠ MSH wire value). **Trip-wire:** pin doc-version + SW-version on every Block; watch for a conformance-vs-actual-field split in cobas's HIM.
4. **Anti-footswitch on tempting numbers/sources.** Liat declined the `2554` FTP port as the DMS port. **Live instance here:** the K060373→architecture misattribution (above). Trace every plausible number/source to what it *actually* supports.
5. **If M2's tables extract scrambled, use the doc's own examples as the attribution key.** Liat's POCT1-A prose field-tables came out layout-scrambled; the HIM's own XML `<OBJ.attr>` examples were the authoritative field map. For cobas's ASTM HIM the equivalent is its own **example H/P/O/R records** — attribute fields from those, not scrambled tables.

**First work order when M1/M2 land (Liat-proven sequence):** `pypdf`-extract → confirm authoritative + pin version/SW → source cap 1 (1.1 transport → 1.2 E1381 → 1.3 E1394 → 1.4 HL7) at `⚠` → **test the 1a/1b split hypothesis (#1)** → Steward certifies → carry trip-wires #2–#5 through every capability.

---

## Open items
1. **Acquire authoritative M1 + M2 + module-config sheet** — eLabDoc access landed; **account-holder to download** so the Researcher can process from disk. *(Blocker is now the download, not access.)* Pin versions on arrival.
2. Confirm module configuration (c 501 / c 502 / both). *(Researcher)*
3. ~~Assign stewards to capabilities 2–11.~~ Done — caps 2–10 → Roche Steward; cap 11 → Networking Steward. **Architect to confirm** whether to split chemistry (c 501/c 502) vs immunoassay (e 601) to specialist sub-stewards once volume justifies it.
4. Field-experience (`✅ FIELD`) tier remains parked until a Roche Field Engineer seat exists.

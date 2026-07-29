# Cap 1 — Second-Read Addendum (⚠ Researcher → Code/Steward)

**Status:** `⚠` Researcher second read — **pending Code's adjudication.** Nothing here is self-promoted; the discover side drafts, the Steward decides.
**Re-read of:** cobas® liat System Host Interface Manual **HL7, VV-07717-09, pub v11.0, SW 3.4 & 3.5** (A1-authoritative, Roche-hosted).
**Method (auditable):** full text layer extracted from the saved authoritative PDF via `pypdf` — 36 pages, 48,107 chars (the WebFetch text-layer parse had failed; direct extraction succeeded). Line numbers below refer to that extracted text; section/page names are the HIM's own.
**Trigger:** the three first-read to-confirms (1.2 MLLP, 1.3 R30/R20, 1.8 QC). Second read corroborated two and surfaced two disposition issues in the certified review.

---

## Corroborated by independent second read — no action
- **1.2 MLLP** → agrees with `✅`. "MLLP or LLP protocol as defined by HL7," no handshake/checksum; frame `<VT>`0x0B / `<FS>`0x1C / `<CR>`0x0D. [§Minimal layer protocol, p.24 · line 932–940]
- **1.3 ORU^R30 / ORC / R20 erratum** → agrees with `✅` and the logged trip-wire. R30 is fixed text in MSH + all 3 examples; ORC present in structure; lone "ORU^R20" at the universal-service line only. [§Message types p.21–22 · line 827, 890, 971]

---

## Item A — Re-open 1.8 (QC transmission)

**Certified disposition:** `⚠ REJECTED / open` — basis recorded as "no QC content in HIM v11.0 (full-text search)."

**Second-read evidence contradicting that basis** — the HIM *does* carry external-control content (search missed it because the doc says "control," not "QC"/"quality control"):
- Line 1087: Ct values reported in an OBX segment "for every valid, positive target result **or control**."
- Line 1099: "**Invalid external control assay runs** are able to report valid target results."
→ External-control **assay runs** are reported through the standard `ORU^R30` result message. [§Result message details, p.25–29]

**Apparent cross-document conflict:**
| Source | Says | Cite |
|---|---|---|
| HIM v11.0 | External-control assay results **are transmitted** (Ct in OBX; invalid-control handling defined) | lines 1087, 1099 |
| User Guide v12.0 (cap 5) | Control results are **local-only, not host-transmitted** | UG p217 |

**Reconciliation hypothesis (offered, not asserted — two different "control" notions):**
- **HIM "control"** = an external control *sample* run as an assay → produces a normal transmitted result.
- **UG "QC"** = *lot-validation QC status* tied to assay-tube lots → stored/visible locally, not sent.

**Proposed disposition (Steward to decide):** move 1.8 from "REJECTED — no QC content" to —
> *No dedicated QC-transmission mechanism; assay-tube **lot QC status is local-only** (UG cap 5). **However**, external-control **assay results** transmit via the standard `ORU^R30` result report — Ct reported for control, invalid-external-control runs handled (HIM p.25–29).*

☑ **Steward decision (1.8) — RESOLVED (Code, 2026-07-28):** re-opened, then closed `✅` via the **POCT1-A HIM (VV-09009-05 v6.0, SW 3.3.1)** — the confirming line this item called for. HL7 carries **no QC records** (certified negative); QC/Liquid-QC travels over **POCT1-A/DML**. Cap 1 now **8/8**. *(Nuance retained: the HL7 HIM does report control-**sample** results as ordinary results — distinct from QC-record transmission.)*

---

## Item B — Refine the HL7-version line (review-record item 3)

**Certified note:** "HL7 version = 2.5 (MSH-11), **not** the 2.5.1 the web-search snippet claimed."

**Second-read finding — both numbers are real and in the HIM; they refer to different things:**
- **Wire value (you're correct):** MSH Version ID is fixed **`2.5`** in every example (`…|P|2.5|…`) and the field table. [lines 974, 1213, 1243, 1254, 1356 · p.25/30]
- **Conformance target (not a web-search artifact):** the HIM prose states **HL7 v2.5.1** four times — "according to the HL7 Version 2.5.1 standard" (line 815) and the IHE/ELINCS **2.5.1** Implementation Guide it implements (lines 484, 564, 663). [§Message types p.21; §References/Intro]

**Proposed disposition (Steward to decide):** replace "2.5, not 2.5.1" with —
> *Conformance = **HL7 v2.5.1** (standard + IHE LPOCT / ELINCS 2.5.1 Implementation Guide); **MSH-12 Version ID transmitted = `2.5`** (fixed text). Both correct; they describe conformance vs. the wire field.*

**Memory note:** the "corrected in memory" entry that says 2.5-not-2.5.1 is half-true and understates the conformance target — recommend updating it to carry both facts.

☑ **Steward decision (version) — ADOPTED (Code, 2026-07-28):** map & memory now carry both — **conformance v2.5.1**, **MSH wire field 2.5** — logged as a same-doc trip-wire, independently corroborated by the POCT1-A HIM overview also citing "HL7 2.5.1."

---

## Trip-wire candidates
1. **ORU^R20 vs R30** — *already logged by Code.* Single-line internal inconsistency; R30 stands on weight of evidence. Re-check next HIM version.
2. **HL7 2.5 vs 2.5.1 (new)** — same class: single-document internal inconsistency (prose conformance 2.5.1 vs MSH Version-ID 2.5). Not an error to "resolve" — a definitional split to record. Recommend logging as the next trip-wire.

---

## Firewall note
Both Item A and Item B are cases of a Steward pass under-covering, caught by a downstream second read — exactly the gap-check the map already anticipates. Drafted at `⚠` by the discover side; **no `✅` or reject was altered.** Code owns the folding-in.

# Roche Researcher — Acquisition Brief: cobas 6000 authoritative sources

**Owner:** Roche Researcher · **Consumers:** Roche Steward (caps 2–10), Code (cap 1)
**Goal:** put authoritative, version-pinned M1/M2 (then M3/R1) into hand so the capability map can advance past `⚠`.
**Status gate:** nothing in the map promotes to `✅` until an authoritative source clears Steward gate **A1** and its versions are pinned (**A2**).

> **UPDATE (2026-07-29): eLabDoc access LANDED.** The account-provisioning blocker is cleared. The gate is now the **authenticated download onto disk** — see the M2 playbook in **§2b**. The crew loop is proven end-to-end on Liat; cobas 6000 is staged to run it the instant M2 is in `~/Downloads`.

---

## 1 · What counts as "authoritative" (Steward gate A1)
**Accept:** documents pulled from Roche's official technical-document channels —
- **eLabDoc** — Roche Diagnostics' official document library (operator manuals, method/data sheets, bulletins, troubleshooting), 24/7, **customer login required**. Entry: diagnostics.roche.com → e-service → technical documents; host `elabdoc-prod.roche.com`.
- **DiaLog** — Roche customer portal that fronts eLabDoc / e-Library Self Service.
- **e-Library Self Service** — offline-loadable variant (data pushed to DiaLog for download into analyzer systems).

**Reject (leads only, never evidence):** manualzz, manualmachine, studylib, pdfcoffee, scribd and any other third-party mirror. Use them to *predict* a document's structure/existence, not to source a Block.

---

## 2 · Access — RESOLVED (2026-07-29); the gate is now the DOWNLOAD
eLabDoc/DiaLog access **landed 2026-07-29**. The account-provisioning wall (the GE-OEC-style "needs a real account") is cleared. **The remaining gate is purely the authenticated download** — the account-holder pulls the PDFs from eLabDoc onto disk, then the Researcher processes them (the Liat process-from-disk pattern).
- [ ] **Account-holder action:** download the target docs (§2b, §3) from eLabDoc → save to `~/Downloads`. The account-holder performs the authenticated download; per standing rules the assistant never touches credentials or logs in.
- **Access ≠ acquisition:** a capability stays `⚠` until its source doc is actually **on disk**, not merely reachable.

## 2b · M2 download — the immediate action (Host Interface Manual → Code's cap 1)
**Target:** cobas 6000 **Host Interface Manual (HIM)** — the sole source for capability 1.
- **In eLabDoc:** cobas 6000 → technical documents → Host Interface / connectivity manual. v1.1 was seen before — **confirm the current version and take the latest.**
- **Onto disk:** save the PDF to `~/Downloads` (any filename), then tell me it's there — I process it exactly like Liat's HIMs.
- **Pin on arrival (A2):** exact title, document/part number, **document version**, and the **instrument SW version** the HIM describes. If the HIM's SW version lags M1's, **flag the gap** — a permanent constraint on every cap-1 Block *(Liat precedent: POCT1-A HIM SW 3.3.1 vs platform 3.4/3.5 = an "A2 gap")*.
- **Identity cross-check (openFDA anchors, already verified):** K060373 (system, 2006) + c 501 K121610/K132418 (2013) anchor *device identity/era only* — use them to confirm the HIM is the right device/generation, **not** to source interface Blocks.

**First actions the moment M2 is on disk (Liat-proven sequence):**
1. `pypdf`-extract the text; confirm it's the authoritative Roche HIM for **cobas 6000** (not a sibling like the 8000); pin versions.
2. **Read the connectivity/protocol chapter FIRST — it settles the I9 ASTM/HL7 split.** Run the four-test rule from `roche_cobas6000_cap1_interface_steward_review.md`; record SPLIT/UNIFIED + M2 evidence; mint a Decision number if it splits.
3. Source cap 1 at `⚠`: 1.1 transport → 1.2 ASTM E1381 → 1.3 ASTM E1394 (H/P/O/R/L/Q/C) → 1.4 HL7 (version + segments).
4. **If the field tables extract scrambled, attribute fields from the HIM's own example messages/records** — not the prose tables *(Liat XML-key lesson)*.
5. Hand the sourced `⚠` Blocks to **Code**, who runs the cap-1 review checklist.

*Parallel pulls (don't block M2 on them): M1 (Operator's Manual) + the module-config sheet — the config sheet fixes gate A3 (module scoping) and is co-critical for caps 2–10 (see §3–§4).*

---

## 3 · Document acquisition list
Pull in this priority order. For each: record exact **title, document/part number, document version, and the instrument software version it describes**.

| Prio | Doc | Tier | Pin | Extract for |
|---|---|---|---|---|
| 1 | **Operator's Manual** (v8.3 seen — confirm current) | M1 | doc ver + SW ver | caps 2, 5–10 (handling, reagent, cal, QC, fluids, maintenance, alarms) |
| 2 | **Host Interface Manual** (v1.1 seen — confirm) | M2 | doc ver + SW ver | cap 1 (Code): ASTM E1381/E1394 + HL7 bindings |
| 3 | **Service / maintenance manual** | M3 | doc ver + SW ver | caps 9–10 (service-level maintenance, alarm codes) |
| 4 | **Method sheets / reagent IFUs** (per assay) | R1 | doc ver + lot/assay | caps 3–4 (per-analyte principle, range, units) |

**Copyright discipline:** extract *facts with citations* (doc + section/page), do not paste manual text into Blocks. Blocks are transformed knowledge, not reproductions.

---

## 4 · Configuration confirmation (unblocks decomposition)
- [ ] From an official **configuration / specification sheet**, confirm the exact module set in view: **core + c 501 and/or c 502 + e 601**.
- [ ] Record which chemistry module(s) are present — this fixes gate **A3** (module scoping) for every cap-3 Block and prevents the chemistry↔immunoassay over-generalization.

---

## 5 · Version-pinning protocol (gate A2)
For every document acquired, log:
1. Title + document/part number
2. Document revision/version
3. **Instrument software version** the document describes
4. Acquisition date + source channel (eLabDoc/DiaLog)

If M1 (v8.3) and M2 (v1.1) describe different software generations, **flag the mismatch** rather than assuming continuity — do not let a claim from one version silently cover another.

---

## 6 · Hand-off deliverables
On acquisition, the Researcher returns:
- [ ] The pinned source register (updates the map's Source register table).
- [ ] Confirmed module configuration (updates the Platform-structure gate).
- [ ] M2 routed to **Code** to begin cap 1 sub-capabilities 1.1→1.4.
- [ ] M1/M3/R1 staged for the **Roche Steward** to begin caps 2–10 against the review checklist.

---

## 7 · Contingency (account wall now cleared)
Access has landed, so the GE-OEC-style wall no longer applies. Residual contingencies:
- **Target doc older than the platform SW** (e.g. HIM v1.1 lags M1's SW generation): pull the closest authoritative version, pin it, and **flag the version gap** — do not mirror-backfill to fake currency.
- **A doc is access-restricted even within eLabDoc:** record it as *doc-scoped-blocked*, let the Architect decide (hold vs. proceed on what's available). Never substitute a mirror for a Block source.
- **openFDA remains the authoritative-public fallback** for regulatory identity/date anchors (it worked where `accessdata.fda.gov` blocked) — identity only, never interface content.

---

**One-line status:** access is landed and the loop is proven on Liat — the single remaining gate is the **§2b download of M2 (plus M1 + config sheet) onto disk.** The moment M2 is in `~/Downloads`, cap-1 sourcing and the I9 split decision execute immediately.

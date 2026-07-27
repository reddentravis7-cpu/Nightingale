# HL7 Knowledge Blocks — Block-by-Block Steward Review

**Reviewer:** Code (Domain Steward, HL7/FHIR — interim assignment)
**Scope:** All 15 blocks in `hl7-knowledge-blocks.json`.

## What this covers

The CTO's original review brief for this pass asked for, per block: `dataType` confirmed against a version-pinned source, `cardinality` confirmed the same way, `exampleInstance` sanity-checked for syntactic validity, `fieldNotes` checked for claims needing citation, `prerequisites`/`relatedBlocks` referential integrity, and `sourceOfTruth` checked for family/version consistency. That brief assumed 16 blocks already existed in this repo; in practice, only 3 (`hl7v2.pid-segment`, `fhir.patient-resource`, `fhir.read-patient-instance`) had ever been fully authored anywhere prior to this pass — the rest existed only as individual field-level facts scattered across prior review threads. The other 12 were authored fresh in this pass, to the same standard, not assumed from memory.

## Disposition per block

All 15 blocks: `dataType` confirmed against version-pinned sources (`hl7.eu/HL7v2x/v251/std251/ch02.html`, `ch03.html`, `ch04.html`, `ch07.html` for v2; `hl7.org/fhir/R4/*.html` for FHIR). `exampleInstance` values hand-checked for correct field-position/delimiter shape (v2) or valid resource shape (FHIR JSON). `prerequisites`/`relatedBlocks` verified to resolve within this file (script-checked, zero dangling references). `sourceOfTruth.url` verified to belong to the correct documentation family for the version claimed.

**Cardinality:** confirmed with the same rigor as `dataType` for fields where the source returned an explicit R/O/C table cell (all of ORC, OBR, OBX; EVN, PV1, NK1's core fields). For MSH-1, MSH-2, MSH-9 through MSH-12, and MSA-1/MSA-2, the source described repeatability but not an explicit required/optional cell — cardinality there is standards-consistent inference, flagged as such directly in each block's field `description` rather than presented as independently confirmed. This mirrors the same disclosure discipline used in the prior sourcing-correction pass — a field left honestly inferred, not silently asserted.

**Every block is `reviewStatus: needs-review`.** None promoted to `current` in this pass. Per `KNOWLEDGE_BLOCK_MODEL.md`, promotion requires `sourceOfTruth.reviewedBy` and `dateReviewed` to be set — that's a distinct, deliberate act of promotion authority, not something that happens automatically once content is sourced. This pass did the technical review; promotion is a separate step for whoever holds that authority to execute once they're satisfied with this review.

## Resolved from prior passes

- `hl7v2.pid-segment`: PID-7 and PID-8 corrected to `TS`/`IS` (from an initially-reported `DTM`/`CWE`).
- `hl7v2.nk1-segment`, `hl7v2.obr-segment`: NK1-3 and OBR-4 corrected to `CE` (from `CWE`).
- `hl7v2.obx-segment`: OBX-3 — previously left flagged as contradictory/unresolved — now confirmed `CE` against the version-pinned Chapter 7 table.

## Referential integrity fix

`fhir.patient-resource` and `fhir.read-patient-instance` originally listed `fhir.restful-interactions-overview` as a prerequisite — a block ID that was never actually authored anywhere. Repointed both to `fhir.capabilitystatement-discovery`, a real, sourced block created in this pass that concretely represents capability 7's discovery mechanism (`GET [base]/metadata`). Noted here rather than silently changed, since it's a correction to previously-shared content, not just new authoring.

## Out of scope, unchanged

Capability 10 (v2-to-FHIR mapping) — untouched. The `StructuralContent` shape as an architectural choice — not reviewed here, that's a schema question for Founder/CTO. Cisco's remaining blocks — separate, later effort.

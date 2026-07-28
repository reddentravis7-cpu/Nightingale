# HL7 Knowledge Blocks — Block-by-Block Steward Review Brief

**Handoff to:** Code (Domain Steward)
**From:** CTO
**Status:** Ready to kick off — capability-level review (Phase 5) and two
rounds of field-level spot-checks are already done. This brief is for the
next level down: a full pass over every field in every block, not just the
ones already flagged.

---

## Files involved

- `hl7-knowledge-blocks.json` — 16 blocks, the actual review target.
- `hl7-collections.json` — directories/categories; check only if a block
  change affects tag membership.
- `KNOWLEDGE_BLOCK_MODEL.md` — schema. `StructuralContent` shape (elements
  with `name`/`position`/`dataType`/`cardinality`/`description`,
  `exampleInstance`, `fieldNotes`) is what every v2 segment and FHIR
  resource block uses.
- `HL7_PHASE4_CONCEPT_DECOMPOSITION.md` — full history of what's already
  been checked, fixed, and flagged. Read this before starting so nothing
  gets rediscovered from scratch.

---

## What's already been done (don't redo this part)

- Capability-level dependency graph and concept decomposition: reviewed,
  confirmed, locked (capabilities 1–9). Capability 10 (v2-to-FHIR mapping)
  is intentionally untouched — out of scope for this pass.
- Field-level spot-checks so far, all independently re-verified: PID-7
  (`TS`, not `DTM`), PID-8 (`IS`, not `CWE`), NK1-3 (`CE`, not `CWE`),
  OBR-4 (`CE`, not `CWE`). All four already corrected in the file.
- OBX-3 is flagged with a confidence note in its `description` — sourcing
  came back genuinely contradictory. Leave it flagged, don't resolve it on
  weak evidence just to close it out.

## The known trip-wire — apply this to every field, not just the ones above

There are two live HL7 documentation families online that look
interchangeable and aren't:

- **Version-pinned original standard text** — `hl7.eu/HL7v2x/v2XX/std2XX/...`
  — the real historical text for a specific version (this project cites
  2.5.1 where a version is claimed).
- **HL7's "V2+" harmonized/refactored reference** — `v2plus.hl7.org`, its
  NIST mirror, `hl7.eu/refactored` (no version number in the URL is the
  tell) — a newer, consolidated reference that modernizes data types
  across the whole v2 line.

Three confirmed instances so far (PID-7/8, NK1-3, OBR-4) all follow the
same pattern: a harmonized-family source reports a newer type (`DTM`,
`CWE`) where the version-pinned text reports the older one (`TS`, `CE`).
Default to suspicion on any `CWE` or `DTM` result until it's confirmed
against a URL that actually encodes the cited version number.

---

## The task

For every block in `hl7-knowledge-blocks.json`, field by field:

1. Confirm `dataType` against a version-pinned source, watching for the
   trip-wire above. Note which specific URL confirmed it.
2. Confirm `cardinality` the same way — this hasn't been checked with the
   same rigor as `dataType` yet and may have the same class of risk.
3. Sanity-check `exampleInstance` — does it parse as a syntactically valid
   instance of what the block describes (right delimiters, right field
   count, right shape for a FHIR JSON snippet)?
4. Check `fieldNotes` for factual claims that need their own citation, not
   just plausible-sounding practical color.
5. Check `prerequisites` and `relatedBlocks` still point at real block ids
   (already verified once with a script, but re-check after any edits).
6. Check `sourceOfTruth` itself — does the `title`/`publisher`/`version`
   actually match the `url`, and does the `url` belong to the correct
   documentation family for what's being claimed?

## Disposition per block

- **Fully confirmed, nothing outstanding:** set `sourceOfTruth.reviewedBy`
  and `sourceOfTruth.dateReviewed`, and set `reviewStatus` to `current`.
  This is real promotion authority — use it, don't just leave everything
  at `needs-review` by default once it's actually been checked.
- **Fixable issue found:** fix it directly in the file, note what changed
  and why (same pattern as the PID/NK1/OBR fixes already in the doc), and
  leave `reviewStatus` at `needs-review` until the fixed version gets its
  own confirming pass.
- **Genuinely unresolved / contradictory sourcing:** leave it flagged in
  the block's `description` or `fieldNotes`, same as OBX-3. Don't force a
  resolution to close out a checklist item.

## Out of scope for this pass

- Capability 10 (v2-to-FHIR mapping) — untouched, stays untouched.
- The `StructuralContent` shape as an architectural choice — this is a
  content review, not a schema review. That's a separate, still-open item
  (whether the shape itself is the right container) and shouldn't be
  folded into this pass just because it's adjacent.
- Cisco's 77 blocks — a real next step, agreed on separately, but
  sequenced after this closes out, not in parallel with it.

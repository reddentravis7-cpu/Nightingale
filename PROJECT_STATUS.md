# Project Status

**Last confirmed:** 2026-07-28, midday. Snapshot, not a permanent fact —
re-verify against the real repo before quoting these numbers much
further out. See `KNOWLEDGE_MAINTENANCE_PLAN.md` for why promotion isn't
a one-way ratchet.

## Important: canonical content now lives under `04_Translate/knowledge/`

Three placement decisions happened in one day (0001 → 0002 → 0003) —
each caught by checking real evidence instead of trusting the previous
proposal. 0003 is current and verified working:

- `04_Translate/knowledge/cisco-ios/` — confirmed live, contains the
  real corrected content (router-ospf's process-id as "any positive
  integer," plus `CISCO_IOS_CITATION_INDEX.md`).
- `04_Translate/knowledge/hl7-fhir/` — confirmed live, contains the real
  corrected content (EVN-2 at cardinality "1..1"/required).
- `04_Translate/knowledge/acl-top-350/` and
  `04_Translate/knowledge/ge-oec-one-cfd/` — relocated placeholders, no
  numbering-scheme question needed anymore since `04_Translate/` is
  already the correct, confirmed root.

**Stale, pending cleanup — do not read as current:**
`01_Networking/Cisco_IOS/`, `03_Clinical_Integration/HL7/`, and the
repo-root `knowledge/`, `docs/`, `tools/`, `services/` folders are all
now duplicated inside `04_Translate/`. Nothing has been deleted yet —
copies were verified correct first, deliberately, before any cleanup
decision. See
`04_Translate/docs/decisions/0003-nest-translate-content-under-04-translate.md`
for the full reasoning, including why 0002's premise (that
`01_Networking`/`03_Clinical_Integration` were Code's deliberate
convention) turned out to be wrong — they're Travis's personal archive
folders, confirmed directly against `Translate-Git-Repository.zip`'s
real skeleton.

Same citation-index note as before: `CISCO_IOS_CITATION_INDEX.md` came
along automatically in the `04_Translate/knowledge/cisco-ios/` copy —
no separate pull needed this time.

## Cisco IOS — 76/77 confirmed (as of `main` @ `21519eb`)

Closed since this morning: `router-ospf` (real syntax confirmed —
process-id is "any positive integer," no 1-65535 bound as previously
assumed; also gained an optional `vrf vrf-name` keyword) and `show-clock`
(`show clock [detail]`, found via direct DOM extraction bypassing a
text-truncation failure). Still held: `show-users` — genuinely absent
from the sourced chapter, proven by the chapter's own alphabetical
heading list skipping directly from "show usbtoken" to "show version."
Not a truncation artifact, a documented negative.

Separately: a Cisco IOS Quick Reference app (Next.js + Supabase) was
built, seeded (77 blocks / 45 collections, row counts verified live),
and tested end-to-end in a real browser. Committed through `21519eb`.
**Vercel deployment has not happened** — explicitly held pending
Travis's go-ahead. One known content gap: `vlan` and `router-ospf` are
missing a `global-configuration` tag the Figma spec expects; should be
checked against all 77 blocks before treating the category complete.

## HL7 v2 / FHIR — 15/15 confirmed, fully closed

All 5 previously-held blocks resolved with real corrections: `MSH-12`
and `EVN-2` are actually `R` (required), not optional as previously
written; `PV1-7` and `NK1-2` are actually repeating (`RP/#=Y`), not
single-occurrence. Root cause: text-extraction truncating before
reaching the real attribute tables — see the DOM-extraction technique
below.

## ACL TOP 350 — 9 blocks, all needs-review

Unchanged, expected for a domain this early. IP posture on manufacturer
spec-sheet data still needs real legal review, not an engineering call.

## GE OEC One CFD — 12/12 capabilities approved; Phase 6 STILL NOT canonical

**Unchanged — flagging explicitly rather than letting this slide.**
Three independent, uncoordinated attempts at this domain's Knowledge
Block layer still exist, unreconciled:

- CTO's own single consolidated block (`ge-oec.system-identity`)
- Steward's 35-block manifest — includes 2 blocks using an unreviewed
  `Procedural` blockType (one safety-critical) and 5 using a non-schema
  `IndustryPracticeContext` type
- Research's separate 37-block file, different id scheme, sent only
  partially — the paste was cut off mid-file and never completed

CTO still needs the complete, literal file content from both Steward and
Research — not summaries — before this can be merged into one canonical
file. Nothing new should be built on this domain until that happens.
Also still access-gated: `SM-7888001-1EN-17` (service manual) and
`DOC2198430` (DICOM conformance statement), both behind a GE account
nobody on the team holds.

## New reusable technique — DOM extraction over text-truncation

Both HL7 and Cisco's held blocks shared one root cause: page-text
extraction tools truncating before reaching real data (attribute
tables, command sections) deep in a long reference page. The fix —
query the page's DOM directly between heading anchors — closed every
held block it was tried on. Written into `KNOWLEDGE_MAINTENANCE_PLAN.md`
as a standing technique for any domain sourcing from long reference
pages.

## Scope review — cleared 2026-07-28

`scope_check_array.py`'s keyword scanner flags watch-list terms for
human sentence-level review; it does not resolve them itself. These 5
were actually read in context and cleared as in-scope — noted here so
the next run of the tool (or the next person/session reading a fresh
flag list) doesn't have to redo this judgment call from nothing:

- `cisco-ios.erase-startup-config` (flagged: "recommended") — refers to
  CLI syntax currency (`erase nvram:` vs. the older `erase
  startup-config`), not professional judgment. Cleared.
- `hl7v2.evn-segment` (flagged: "treat") — "treat MSH-9 as the source of
  truth" is interface-parsing guidance (which field to trust when two
  conflict), not clinical decision-making. Cleared.
- `hl7v2.pv1-segment` (flagged: "treating") — "who's treating them"
  describes what data the segment carries, doesn't instruct on patient
  treatment. Cleared.
- `hl7v2.nk1-segment` (flagged: "treat") — "never treat an absent NK1 as
  an error" is parsing guidance for an optional segment, not clinical
  judgment. Cleared.
- `hl7v2.obx-segment` (flagged: "treat") — "treat a corrected result as
  superseding a prior final one" is result-reconciliation logic for
  system builders, not medical interpretation of the result. Cleared.

## Cross-cutting open items, unchanged

- Researcher constitution's full text still never actually supplied —
  "Principle 6" and the "Reasonable Doubt Test" remain cited, unverified.
- M1–U1 source-hierarchy backport still sized, not started, still
  deferred until a domain forces it.
- Ask for Code: what should ultimately happen to the stale duplicates
  at `01_Networking/Cisco_IOS/`, `03_Clinical_Integration/HL7/`, and the
  repo-root `knowledge/`/`docs/`/`tools/`/`services/` folders —
  deliberate deletion is still an open, unexecuted decision.

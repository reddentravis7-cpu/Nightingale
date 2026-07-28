(sandbox only — not on repo, paste this in)

**To:** Steward
**From:** CTO
**Re:** Real schema, one conflict to resolve first, answers to your three questions

Good instinct flagging the reconstructed-from-fragments problem rather
than plowing ahead on it. Here's the actual schema, pulled directly from
`KNOWLEDGE_BLOCK_MODEL.md` — not re-derived from memory, quoted:

```
KnowledgeBlock
  id                string     unique, stable, never reused even if deprecated
  title             string
  aliases           [string]
  domain            string     e.g. "ge-oec-one-cfd"
  blockType         enum       "invokable" | "structural" | "procedural" |
                                 "conceptual" | "entity" | "specification"
  tags              [string]
  summary           string
  difficulty        enum       "beginner" | "intermediate" | "advanced" —
                                 editorial default only, not authoritative
  prerequisites     [blockId]  relationship, not a gate
  relatedBlocks     [blockId]  symmetric see-also graph
  sourceOfTruth     object     see below
  reviewStatus      enum       "current" | "needs-review" | "deprecated"
  lastReviewed      date
  content           <shape>    matches blockType

sourceOfTruth
  title             string
  publisher         string
  version           string?
  url               string
  reviewedBy        string     required alongside url + dateReviewed before
                                 reviewStatus can be "current" — a hard gate,
                                 added after six Cisco blocks were found
                                 `current` on placeholder urls with no reviewer
  dateReviewed      date

SpecificationContent   -- the shape most of this domain will likely use:
                           manufacturer capability/config facts, not
                           something invoked, not a typed message field
  specifications    [{label, value, note}]
  fieldNotes        string
```

`StructuralContent` (typed fields with position/dataType/cardinality) and
`InvokableContent` (commands/RESTful calls) both exist too — capability 8
may need `InvokableContent` if DICOM's operations end up documented as
verb+response pairs, same shape FHIR's RESTful layer used. `procedural`
is a reserved enum value with no shape defined yet — likely what
capability 11 (troubleshooting) will force into existence, same way HL7
forced `structural` and ACL TOP 350 forced `specification`. Don't invent
its shape ahead of need.

## The thing to resolve before capability 2 gets this same treatment

Phase 6 is CTO territory per the process doc, and I already did it once,
independently, before this thread reached me — one consolidated block,
`ge-oec.system-identity`, covering 1.1/1.2/1.3/1.5/1.6 from K253269
directly. You've now built five separate blocks for the same capability
from a different angle (Research's concept decomposition). Those two
outputs almost certainly don't match — different granularity by
construction (one block vs. five) — and need reconciling, not both kept.
Paste your five here before capability 2 proceeds; I'll diff against mine
the same way the LAB_EQUIPMENT_DOMAIN_TEMPLATE capability-12 provenance
question got resolved — by actually comparing, not assuming either
version is right.

Worth naming plainly: this is a real coordination gap, not a fault on
either side — nobody told you capability 1 already had a Phase 6 pass, and
I didn't know you were starting one. Same shape as the Cisco repo
confusion earlier in this project. Catching it now, before it propagates
across 11 more capabilities, is exactly the right instinct behind going
capability-by-capability instead of batching.

## Your three questions

**Granularity — split when evidence tiers genuinely differ within a
concept.** Agree with your instinct, and it corrects something I got
wrong on my own capability-1 pass: 1.3's null-field-with-a-note handling
doesn't actually let `reviewStatus` mean what it's supposed to mean once
promotion starts — a block can't honestly be `current` if one of its rows
is still Research Pending, and it can't honestly be `needs-review` if
most of its rows are solid. This is the exact pressure point the schema
doc already named as unsolved — "one row sourced from a datasheet sitting
next to a row that's expert-observed... stays single-sourced per block
until an actual domain produces a block that needs mixed-class rows" —
capability 4 is that domain, arriving right on schedule.

Don't fix the schema for this yet, though — same "ceiling, not inventory"
discipline as everywhere else in this model. Split blocks when tiers
genuinely differ (your proposal, adopted), and if this keeps happening
across the remaining capabilities — three or four more times — that's the
trigger to actually add per-row status to `specifications`/`elements`
rather than keep splitting indefinitely. I'll go back and fix 1.3 to
match once the capability-1 reconciliation above is settled.

**`needs-review` concepts — publish with visible status, don't omit.**
This is already established practice elsewhere in the project: HL7's five
held blocks and Cisco's three held blocks are real entries in their block
files, `needs-review`, not promoted — never omitted. Omitting 1.4 would
be a real deviation from precedent, not a neutral choice between two
defensible options. Your stated worry — a normal-looking published block
burying an unresolved conflict — is a product-presentation concern, not a
data-modeling one; the schema doc's own standing principle says exactly
this: "the schema describes reality; the application decides how to use
it." The fix is making sure whatever renders these blocks actually
surfaces `reviewStatus` visibly, not hiding the block from the dataset.
An omitted block also can't be safely pointed at by `relatedBlocks` later
without becoming a dangling reference — which is your third question.

**`relatedBlocks` forward-references to ids that don't exist yet — don't.**
This will fail `scope_check_array.py`'s referential-integrity check the
moment it runs, and it'll read as a real dangling reference because it is
one at that point in time. I hit the identical situation with 1.7→capability
8 and 1.4→capability 7 and used a prose forward-pointer inside `fieldNotes`
instead of a structural `relatedBlocks` id — same information, no
integrity-check false positive. Recommend switching to that convention
for consistency rather than inventing a second one.

Also flagging separately: predicted ids like `5.1`, `4.2`, `3.1`, `2.1`
are bare concept numbers, not domain-prefixed descriptive slugs. They'd
technically pass the naming-convention regex, but every other domain in
Translate uses ids that mean something read in isolation —
`cisco-ios.show-ip-route`, not `cisco-ios.14`. Worth fixing before it's
70+ ids to rename instead of a handful.

Hold capability 2 until the capability-1 diff is resolved.

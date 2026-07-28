# Knowledge Maintenance Plan (v1.0)

**Status:** Adopted, evidence-based — generalized from the HL7 block-by-
block review brief, itself prompted by three confirmed sourcing errors
found in a single domain in a single day.

---

## Why this needs to exist as its own standing thing

Every domain so far has treated "build the blocks" as the finish line.
It isn't. Standards get revised. Sourcing that was right when a block was
written can turn out to have been wrong all along, the way PID-7/PID-8
were. A block marked `current` is a claim about a point in time, not a
permanent fact — and nothing in the process so far has said what happens
after that point in time passes. This plan is that missing piece.

This isn't hypothetical scope creep. It's already happened once, inside
one domain, before the domain was even finished: three fields wrong for
the same root cause, caught only because someone went back and checked
instead of trusting the first pass.

---

## What triggers a maintenance pass

- **A new instance of a known trip-wire is found.** When an error class
  shows up more than once (see registry below), every other block that
  could plausibly share it gets checked, not just the one that got
  flagged. This is what just happened with CE/CWE — three hits made it a
  pattern worth checking everywhere, not a one-off fix.
- **An external standard changes.** A new HL7 version, a new FHIR release,
  a Cisco IOS end-of-life notice — anything that means the actual ground
  truth moved out from under a block that was correct when written.
- **A scheduled interval.** How often is an open decision, not yet made —
  noting that explicitly rather than picking a number that sounds right
  and asserting it as settled. Worth deciding once there's more than one
  domain's worth of experience to base a cadence on.

## The known trip-wire registry

Kept here so future reviews don't have to rediscover what's already been
learned. Add to this list; don't let it live only inside one domain's docs.

1. **HL7 CE→CWE, TS→DTM (harmonized vs. version-pinned families).**
   `v2plus.hl7.org`, its NIST mirror, and `hl7.eu/refactored` describe a
   later, harmonized data-type scheme that doesn't match a specific
   historical version like 2.5.1. `hl7.eu/HL7v2x/v2XX/std2XX/...` is the
   actual version-pinned text. Confirmed three times (PID-7, PID-8,
   NK1-3, OBR-4) before being written down here.

2. **AI-generated search synthesis isn't a citation.** A search tool's
   summary sentence can read exactly like a direct quote — confident,
   specific, plausible — without being one. Caught on GE OEC One CFD:
   a search summary stated the device "features a motorized column and
   brake system," which sounded like sourced fact but was the tool's own
   synthesis, not a quoted line from any document. Applies to every
   domain that does web research, not just device domains — check
   whether a claim is inside quotation marks from an actual fetched
   page before treating it as evidence, not just whether it sounds
   authoritative.

3. **Page-text extraction truncates before the real data — go to the DOM,
   not the summary.** Caught on both HL7 and Cisco: whatever tool reads a
   source page as flattened text (`get_page_text`-style extraction) can
   cut off before reaching attribute tables or command-reference sections
   that sit deep in a long page — reading that truncation as "the source
   doesn't have this" is wrong, not just incomplete. The fix that worked
   twice now: query the page's actual DOM directly, between heading
   anchors or by container, instead of relying on a flattened text dump.
   This closed HL7's entire held-block list and found 4 real corrections
   (MSH-12, EVN-2, PV1-7, NK1-2) that text-extraction had been silently
   hiding. Applies to any domain sourcing from long reference pages, not
   just HL7 or Cisco specifically.

## The review checklist (per block, generalized from the HL7 brief)

- `dataType` / equivalent typed fields — confirmed against a source that
  actually matches what `sourceOfTruth.version` claims, not just a source
  that's topically relevant.
- `cardinality` / equivalent structural constraints — same rigor as
  `dataType`; this hasn't historically gotten the same scrutiny and may
  carry the same undiscovered risk.
- `exampleInstance` — does it actually parse as a valid instance of what
  the block describes.
- `fieldNotes` — factual claims get their own check, not just a plausible-
  sounding read.
- `prerequisites` / `relatedBlocks` — still resolve to real block ids.
- `sourceOfTruth` itself — title/publisher/version actually match the url,
  and the url belongs to the right documentation family for what's being
  claimed.

## Risk-calibrated verification tiers

Added during Cisco's audit, when full body-text confirmation on every
block proved to cost meaningfully more effort than HL7's per-block pass
did — Cisco's command-reference books are large, multi-hundred-command
chapters with no per-command URLs, so finding the right page is real
trial-and-error, not a lookup. Uniform maximum rigor on every claim
regardless of stakes was never really the goal; proportionate confidence
was.

**The test:** does the claim include a specific number, parameter, range,
or exact behavior a reader might act on directly? If yes, full body-text
confirmation against the source is required — same as VLAN ID range
(1–4094), same as OBX-3's data type. If the claim is just "this command
exists and does roughly X," with no specific fact to get wrong, a real,
quoted, cisco.com-sourced search snippet is proportionate evidence — same
as confirming `show history` takes no parameters.

**Non-negotiable part:** which tier applied has to be visible per block,
not silently blended into a uniform "confirmed" status. Report it the
same way the Cisco batch reports already do — a table naming which
blocks got full-page confirmation and which got snippet-tier evidence.
Reviewer or Founder should be able to tell, without re-deriving it, which
blocks carry stronger evidence than others.

This is the same discipline as the Scope Constitution's differently-tight
promotion bar for ACL TOP 350 versus Cisco or HL7 — rigor should track
what's actually at stake in being wrong, stated explicitly rather than
applied uniformly by default or loosened silently under time pressure.

**Precedence, stated explicitly — caught on GE OEC One CFD:** a domain's
own tighter promotion bar overrides this generic tier test; it does not
sit alongside it as a second, potentially-looser path to the same claim.
"The footswitch triggers exposure" has no number in it — read against
the generic test alone, it could pass as snippet-tier, "this control
exists and does roughly X." But it's a claim about what triggers
radiation exposure, which GE OEC's own tightened bar (Principle 6 —
Safety Before Convenience) requires full-tier confirmation on regardless
of whether the claim happens to be parameterized. The stakes come from
what the claim controls, not from whether it contains a number. Any
future domain that declares its own tighter bar for a content category
inherits this same precedence rule automatically — the generic test
never gets to override a domain-specific one.

## Disposition per block

- **Confirmed clean:** set `reviewedBy` and `dateReviewed`, promote to
  `current`.
- **Confirmed stale or wrong:** fix it, record what changed and why, leave
  at `needs-review` until the fix itself gets checked.
- **Genuinely unresolved:** flag it in place (same as OBX-3) rather than
  force a resolution to close out a checklist.
- **A previously-`current` block fails a later pass:** demote it back to
  `needs-review`. Promotion is not a one-way ratchet — `dateReviewed`
  means confirmed as of that date, not confirmed permanently. A block that
  was right in 2026 can be wrong once a standard moves.

---

## Known cost: sentence-level scope review doesn't scale for free

Added after the Scope Constitution's enforcement clause (sentence-level
re-review of every drafted block, not just charter-level capability
compliance — see `TRANSLATE_SCOPE_CONSTITUTION.md`). That review is real
work, and it scales with block count, not with capability count. Fine at
ACL TOP 350's current size. A real capacity question once this hits a
domain Cisco's size — 77+ blocks each needing the same pass.

**Update:** a first attempt at making this cheaper now exists —
`scope_check_array.py`, five checks (referential integrity, schema
completeness, source-family trip-wire, scope-constitution keyword scan,
id naming convention), four of which are fully automated with zero human
input needed. Tested against both live files: Cisco's 77 blocks came
back clean on all five checks in under a second — zero blocks needed a
human look. HL7's 16 blocks produced 3 keyword-scan flags, each resolved
in about thirty seconds as false positives ("FHIR treats care as..." is
not a treatment plan). That's the intended shape of this tool: it
narrows the review surface, it doesn't replace judgment, and it's fine
for most flags to turn out to be nothing — a false positive costs
seconds, a missed real one doesn't.

This doesn't close the underlying cost — the keyword scan is a first
pass, not a guarantee, and dataType/cardinality accuracy against source
text still has to be checked by a human either way. It does mean the
mechanical parts (integrity, schema gates, naming) never need a human at
all going forward, and the scope check only surfaces what's actually
worth a second look instead of demanding a cold re-read of everything.

## Scope: every domain, not just HL7

This plan isn't domain-specific — nothing above mentions HL7 by name
except the one trip-wire currently on file. Cisco's 77 blocks are the
obvious next application (already agreed on, sequenced after HL7's pass
closes out), and every future domain should get this built in from day
one rather than discovered as a gap after the fact, the way it was here.

Worth noting the schema was already set up for exactly this, even before
this plan existed: `sourceOfTruth.dateReviewed` was added specifically
because "it's what makes future staleness-checking automatable instead of
requiring a full migration later to parse it back out." This plan is that
staleness-checking finally getting a defined process instead of just a
field waiting for one.

---

## Reference implementation

`HL7_BLOCK_BY_BLOCK_REVIEW_BRIEF.md` is the first concrete application of
this plan — written before the plan itself existed as a standing document,
generalized into this one once it was clear the same shape would be needed
again.

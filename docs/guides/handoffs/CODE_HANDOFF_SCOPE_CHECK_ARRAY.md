**To:** Code
**From:** CTO
**Re:** `scope_check_array.py` — automated first pass for block review

Built in response to your resourcing observation on
`TRANSLATE_SCOPE_CONSTITUTION.md`'s sentence-level enforcement clause —
that checking every sentence in every block doesn't scale for free, and
gets real at Cisco's size. This doesn't remove that cost, but it narrows
it. Referenced from `KNOWLEDGE_MAINTENANCE_PLAN.md` under "Known cost:
sentence-level scope review doesn't scale for free."

## What it does

Five checks, run as one pass over any blocks JSON file:

1. **Referential integrity** — every `prerequisites`/`relatedBlocks` id
   resolves to a real block. (Same check that's been run ad hoc via
   one-off scripts for HL7 and Cisco — now standing tooling.)
2. **Schema completeness** — `reviewStatus: current` requires `url`,
   `reviewedBy`, and `dateReviewed` all populated, per the gate rule in
   `KNOWLEDGE_BLOCK_MODEL.md`.
3. **Source-family trip-wire** — flags a block whose `sourceOfTruth.url`
   matches a known no-version documentation family (`v2plus.hl7.org`,
   `hl7.eu/refactored`, the NIST mirror) while also claiming a specific
   version. Generalized from the CE/CWE trip-wire; the pattern list is a
   parameter, so a future domain registers its own look-alike sources.
4. **Scope constitution keyword scan** — flags any block whose text
   fields contain a short watch-list of clinical-judgment-adjacent terms
   (diagnose, treat, recommend, "should not be used," dosage, etc.). Not
   a verdict — a "look here" for the Alarm-327-style sentence test.
5. **Id naming convention** — flags ids that don't match a domain's
   declared dotted convention.

Checks 1, 2, 3, and 5 are fully mechanical — no human input needed
either way, pass or fail. Check 4 is a filter, not a resolution: it
narrows what needs the sentence-level test, it doesn't perform it.

## Results against the real files

- **Cisco, 77 blocks:** clean on all five checks, under a second to run.
  Zero blocks needed a human look.
- **HL7, 16 blocks:** clean on checks 1, 2, 3, 5. Check 4 flagged three
  blocks — `hl7v2.ack-nack-model`, `fhir.terminology-binding-model`,
  `fhir.encounter-resource`. Reviewed each in about thirty seconds: all
  three are false positives (e.g. "FHIR treats care as happening inside
  an encounter" — treats meaning considers, not a treatment plan). Real
  matches on the watch-list, no actual scope violation.

That false-positive result is the intended behavior, not a shortcoming —
the tool's job is to make most flags cost thirty seconds each instead of
letting a real one slip through unflagged.

## Suggested use

Run as a fast pre-check before any Steward block-by-block pass — lets
review time go to what the scan actually surfaced and to the parts it
can't touch (dataType/cardinality accuracy against source text, which
still needs a human either way) instead of re-reading everything cold.
Watch-list in check 4 is meant to grow the same way the trip-wire
registry does — add a pattern the moment a real instance is found, don't
wait to build a comprehensive list up front.

Not a gate, not a replacement for judgment — first pass only.

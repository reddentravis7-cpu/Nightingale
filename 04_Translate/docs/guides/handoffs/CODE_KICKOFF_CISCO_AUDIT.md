(sandbox only — not on repo, paste this in)

**To:** Code
**From:** CTO
**Re:** Kick off Cisco's 77-block audit — sequenced after HL7's pass, as agreed

Cisco's known state, for context rather than as a claim to verify blind:
all 77 blocks were previously fixed from `[TBD]` sourceOfTruth placeholders
to real cisco.com command-reference-guide URLs, and 6 blocks that were
incorrectly marked `current` with no real reviewer got demoted back to
`needs-review`. As of that fix, every block sits at `needs-review` with a
real citation and `reviewedBy: null` — zero blocks have had an actual
promotion decision made against them yet. This is a fresh full audit, same
shape as HL7's, not a continuation of partial work.

## Step 1 — run the array

python3 tools/scope_check_array.py cisco-ios-knowledge-blocks.json

Same five checks. Cisco is pure networking/CLI content, so the scope
keyword scan should come back clean — worth confirming that's still true
against the real file rather than assuming it from the earlier sandbox
run.

## Step 2 — the check the array can't do

For Cisco this is command syntax and parameter accuracy against the
citation, not dataType/cardinality — does `syntax` actually match what
the cited Cisco command reference guide shows, do the `parameters` match
what that guide documents as valid, does `sampleOutput` look like a real
device would actually produce it. Same trip-wire posture as HL7: don't
assume a plausible-looking command is a confirmed one.

## Step 3 — apply the same disposition rules as the HL7 pass

- Confirmed clean: set `sourceOfTruth.reviewedBy` and `dateReviewed`,
  promote `reviewStatus` to `current`.
- Fixable: fix it, note what changed and why, leave at `needs-review`
  until the fix gets its own confirming pass.
- Genuinely unresolved: flag in place rather than force a resolution.

## Report back

Real counts — how many of 77 actually got promoted, how many fixed, how
many still flagged and why. Same standard as the HL7 report: promotion
decisions, not just confirmation the scan ran.

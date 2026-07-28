**To:** Code
**From:** CTO
**Re:** Kick off the actual HL7 block-by-block pass — brief and tool both already exist

`HL7_BLOCK_BY_BLOCK_REVIEW_BRIEF.md` and `scope_check_array.py` are both
already on `main`. What hasn't happened yet is running them together and
making real promotion calls — every HL7 block is still sitting at
`needs-review` even after the confirmed PID-7/8 and NK1-3/OBR-4
spot-checks.

## Step 1 — run the array

```
python3 tools/scope_check_array.py hl7-knowledge-blocks.json
```

Whatever passes all five checks clean doesn't need a cold re-read.
Whatever gets flagged is where the sentence-level human check actually
goes.

## Step 2 — the check the array can't do

`dataType`/`cardinality` accuracy against the version-pinned source isn't
automatable — same trip-wire discipline as PID-7/8: confirm against a URL
that actually encodes the cited version, not a harmonized/no-version
family source.

## Step 3 — apply the disposition rules already written in the brief

- **Confirmed clean:** set `sourceOfTruth.reviewedBy` and `dateReviewed`,
  promote `reviewStatus` to `current`. Real authority — use it where it's
  earned.
- **Fixable:** fix it, note what changed and why, leave at `needs-review`
  until the fix itself gets a confirming pass.
- **Genuinely unresolved:** flag in place, same as OBX-3. Don't force a
  resolution to close out a checklist.

## Report back

Which blocks actually got promoted to `current`, which got fixed, which
stayed flagged and why. That's the real output of this pass — not just
confirmation the scan ran clean.

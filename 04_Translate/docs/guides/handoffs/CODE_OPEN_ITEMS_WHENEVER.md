(sandbox only — not on repo, paste this in)

**To:** Code
**From:** CTO
**Re:** Three small open items — no rush, pick up whenever

Nothing urgent, nothing blocking. Three loose ends from the HL7/Cisco
passes, queued here so they don't get lost, not because they're due now.

## 1. HL7's 5 held blocks — cardinality source

`hl7v2.msh-segment`, `hl7v2.msa-segment`, `hl7v2.evn-segment`,
`hl7v2.pv1-segment`, `hl7v2.nk1-segment` are all still `needs-review`,
stuck on the same root cause: `ch02.html` truncates before the
cardinality table for these segments. Need either a different page in
the same doc family or a different mirror that isn't truncated. No new
research needed beyond finding a page that actually renders the table.

## 2. Cisco's 3 held blocks — citation not pinned

- `show-users` — command confirmed, exact citation not pinned
- `show-clock` — same
- `router-ospf` — process-id range (1–65535) stated but unconfirmed
  against the actual command reference page

All three are "probably right, not yet proven" — same bar as everything
else that got promoted, just not closed out yet.

## 3. Citation index — still empty

`CITATION_INDEX_TEMPLATE.md` exists but has nothing in it. Idea was to
log Cisco command → book/chapter/anchor as you go, so the next pass
doesn't re-search pages you already found. Worth populating retroactively
from the 74 already-promoted blocks whenever there's a slow stretch —
not a new research task, just capturing navigation you already did.

No deadline on any of these. Flagging so they're visible, not so they're
next.

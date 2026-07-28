(sandbox only — not on repo, paste each section into the relevant thread)

**From:** CTO
**Re:** Yesterday's punch list, in priority order — three separate items, two different recipients

---

## 1. To: Stewie + Sheldon — GE OEC Phase 6 reconciliation (highest priority)

This is first because it's the only item touching safety-critical content
that was never actually reviewed.

Nothing new gets built on this domain until both of you send the real
files:

- **Stewie:** the actual JSON for the 2 blocks using `Procedural`
  (`cap6.exposure-control-behavior`, `cap12.radiation-safety-best-practices`)
  and the 5 blocks using `IndustryPracticeContext`. Neither of those is a
  reviewed blockType — `Procedural` has no defined shape yet, and
  `IndustryPracticeContext` isn't in the schema at all. Send the raw JSON,
  not a summary — I need to see the actual structure before either can be
  approved or fixed.
- **Sheldon:** the full `ge_oec_one_cfd_knowledge_blocks.json` file as it
  actually stands, with your id scheme (`geoc-onecfd.1.1.device-identity`
  style) intact. Don't reconcile toward Stewie's version yourself — I'll
  do the diff once I have both real files side by side.

Once I have both, I'll merge to one canonical file, one id scheme, and
tell you where the file lives going forward so this doesn't fork a third
time.

## 2. To: Code — HL7's 5 held blocks

Still `needs-review`: `hl7v2.msh-segment`, `hl7v2.msa-segment`,
`hl7v2.evn-segment`, `hl7v2.pv1-segment`, `hl7v2.nk1-segment`. Same root
cause on all five — `ch02.html` truncates before the cardinality table.
Find a page in the same version-pinned family that actually renders the
table, or a different mirror that isn't truncated. No new sourcing
judgment needed, just a page that works.

## 3. To: Code — Cisco's 3 held blocks

`show-users`, `show-clock` — citations not pinned. `router-ospf` —
process-id range (1–65535) stated but unconfirmed against the actual
reference page. All three are "probably right," same bar as the other 74,
just not closed out.

Also, whenever there's a slow stretch: `CITATION_INDEX_TEMPLATE.md` is
still empty. Worth populating retroactively from the 74 already-promoted
Cisco blocks so the next pass doesn't re-search pages already found.

---

## Not delegated — flagging, not assigning

- **ACL TOP 350's 9 blocks are still needs-review** — this is expected
  for a domain this early, not a gap. No action needed yet.
- **ACL TOP 350's IP posture on manufacturer spec data** is a real,
  separate question that needs qualified legal review, not engineering
  judgment. Sitting with you and Ledger, not Code or Stewie/Sheldon.
- **The Researcher constitution's full text** — Principle 6, the
  Reasonable Doubt Test — still hasn't been pasted into any thread I can
  see. Only you can pull that one loose; nobody downstream can self-serve
  it.

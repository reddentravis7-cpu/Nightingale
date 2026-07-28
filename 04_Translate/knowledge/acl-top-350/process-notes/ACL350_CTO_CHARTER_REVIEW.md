# CTO Review — ACL TOP 350 CTS Research Charter v0.1

**Status:** Charter approved. Research may proceed. Three items below are
flagged for Research/Steward to carry forward — not blockers, but decisions
that should be made on purpose rather than discovered mid-production, the
way HL7's content-shape mismatch was.

---

## What's strong, worth keeping as-is

- The M1/R1/E1/O1/I1/U1 source hierarchy is a real upgrade over HL7's
  single `sourceOfTruth` object — it gives Steward a way to compare expert
  field knowledge against manufacturer text without either silently
  overwriting the other.
- Capability 6 explicitly declines to claim internal measurement sequence,
  optical channels, or calculation algorithms until the manuals or expert
  input support it. That's the right instinct — same discipline that kept
  OBX-3 flagged instead of forced to a resolution on weak HL7 evidence.
- Citations are real and checked (GUDID record, Werfen's own product page),
  not asserted from memory.

## Three open items for Research to resolve

**1. Block ID convention.** HL7 uses `hl7v2.msh-segment`, Cisco uses
`cisco-ios.show-ip-interface-brief` — dotted, domain-prefixed. The
charter's candidates (`ACL350-SYS-001`, etc.) are hyphenated code-style.
Cross-domain tooling — the referential-integrity checks already run
against HL7 and Cisco — assumes one convention. Pick one on purpose before
the first real block file gets written, not after.

**2. Watch for a third content shape.** Capabilities 2, 3, 5, 10, and 11
(startup, sample handling, test execution, maintenance, error recovery)
describe procedures — preconditions, steps, failure branches — not
commands (`InvokableContent`) or named/typed field sets
(`StructuralContent`). Section 4's vertical-slice dependency chain is
close to what that content actually looks like. Forcing these into one of
the two existing shapes is the same trap PID/OBR nearly fell into before
`StructuralContent` got designed. Flag it explicitly once real blocks are
drafted rather than rediscovering it partway through a mass-production
pass.

**3. IP posture, stated plainly.** This is a live commercial device, and
the stated use case includes presenting Translate back to Werfen. Building
structured content decomposed from Werfen's own copyrighted manuals, then
pitching that product to Werfen, is a different situation than HL7 (open
standard) or Cisco (public reference docs, no pitch-back to the vendor).
Probably fine — but the access-classification discipline in charter
section 2 needs to stay real, not pro forma, so there's a clear answer
ready if the question of authorized-derivative-use vs. redistribution ever
comes up.

## Disposition

Charter approved. None of the above blocks Research from starting the
capability decomposition or beginning the expert-interview process in
section 6. All three are process notes to carry into block production,
the same way the CE/CWE trip-wire got carried into HL7's maintenance
discipline once it was found once.

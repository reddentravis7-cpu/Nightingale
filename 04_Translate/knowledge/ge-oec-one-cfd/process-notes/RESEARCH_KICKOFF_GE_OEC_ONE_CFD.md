(sandbox only — not on repo, paste this in)

**To:** Research (new pairing)
**From:** CTO
**Re:** Kick off GE OEC One CFD — new domain, testing the reusable template for real

This is the first domain built by a Research/Steward pairing that didn't
build the standing documents themselves. That's deliberate — if this
kickoff works without everything needing to be re-explained from
scratch, that's real evidence the process generalizes. If something's
missing or unclear, that's useful too: it means a gap in the documents,
not a gap in you.

## Start here, don't start from scratch

Read, in order:
1. `TRANSLATE_SCOPE_CONSTITUTION.md` — non-negotiable, governs everything
   below it. The core test: does a piece of content directly decide an
   action with meaningful risk to a person, animal, or significant
   property. If yes, it's out of scope, no exceptions, no disclaimers
   substitute for it.
2. `LAB_EQUIPMENT_DOMAIN_TEMPLATE.md` — the reusable skeleton. Copy its
   12-capability structure (Define the analyzer → ... → Protect
   operational integrity) as the starting point for GE OEC One CFD's
   capability map. Validate and adjust it, don't re-derive it from zero.
3. `CAPABILITY_MAP_PROCESS.md` — the phase sequence: Research proposes
   capabilities → Steward validates → Research decomposes into concepts
   → Steward validates → CTO represents as Knowledge Blocks.
4. `KNOWLEDGE_MAINTENANCE_PLAN.md` — the review discipline once real
   blocks exist, including the risk-calibrated verification tiers
   (full confirmation for specific/parameterized claims, lighter
   evidence for low-stakes ones — disclose which tier applies, per
   block, always).

## Two things specific to this domain — bake these into the charter itself, don't leave them implicit

**No E1 source available.** ACL TOP 350's charter had an expert-interview
source (real field-service background) to draw on. This domain doesn't —
nobody on the team has hands-on experience with this device. The charter
should say this plainly, not just end up with thinner coverage that
nobody explained. Source hierarchy here leans on M1 (manufacturer) and
R1 (regulatory/GUDID) primarily; O1 only becomes available later, if
this ever reaches real field use.

**Radiation and high voltage need their own, tighter promotion bar.**
This device emits ionizing radiation — describing its interlocks,
exposure-fault behavior, and beam-on state is legitimately in scope
(it's equipment behavior, not patient interpretation), but a wrong claim
here, acted on by a technician, causes real physical harm in a way
nothing in Cisco or HL7 could. Name this explicitly in the charter as a
capability-level promotion bar, tighter than the domain's general one —
same pattern as ACL TOP 350's charter naming its own tighter bar instead
of assuming the general constitution covers it by default.

## What "done" looks like for this first step

A Research Charter v0.1 — capability map (adapted from the template),
source hierarchy applied with the E1 gap stated, the radiation/high-voltage
promotion bar named, a first vertical slice (one real workflow end to
end, same pattern as ACL TOP 350's "routine PT sample" slice), and first
Knowledge Block candidates. Ready for CTO review before any block
production starts — same sequencing every domain so far has followed.

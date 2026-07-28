(sandbox only — not on repo, paste this in)

**To:** Research
**From:** CTO / Steward
**Re:** GE OEC One CFD — Phase 3 return, two scoped questions + one gap-check

Capabilities 1, 2, 4, 6, 8–11 are confirmed and move forward as-is. Two
items are returned as scoped questions, not resolved by inference — same
discipline Research's own constitution requires:

## 1. Capability 3 — "independent of electronics" is unconfirmed

Whether GE OEC One's orbital/angular positioning is manual (brake-and-
push) or motor-assisted is a real fact about this specific model, not
something either CTO or Steward should guess. If it's motorized,
capability 3 partially depends on capability 2 (power), and the map
needs to say so. Find the actual answer before this gets finalized —
don't resolve it by assumption either direction.

## 2. Capability 12 — split confirmed, mechanism specified

Agreed this shouldn't be pure capstone. Radiation/electrical-safety
grounding is load-bearing for capability 5 (footswitch is the exposure
trigger) and capability 6 (acquisition itself) — a technician
conceptually reaching "operate the UI" or "acquire images" before any
safety grounding exists is the wrong order.

Mechanism, not just placement: baseline radiation/electrical-safety
becomes an explicit `prerequisites` relationship on capabilities 5 and 6
specifically — not folded into capability 2's neighborhood. This is
structurally closer to how MSH functioned in HL7 (foundational, everything
downstream explicitly depends on it) than to ACK/NACK (a shared utility
referenced from several places). Capability 12 stays as the deeper
capstone — regulatory considerations, emergency procedures, full hazard
catalog — built on that earlier foundation, not replacing it.

## Gap-check still open

CTO's original structural pass also flagged two other things: a possible
boundary overlap between capability 9 (maintain image quality) and
capability 10 (preventive maintenance) — is calibration part of PM or
separate on this device — and capability 7 (manage software and
configuration) reading like it could become a catch-all overlapping 5,
6, 8, and 12. Steward's Phase 3 review said "everything else... is
sound" without addressing these two explicitly. Confirm they were
actually checked and passed, not just outside this pass's focus, before
treating them as settled.

## One process item, not domain-specific

"Principle 6 (Safety Before Convenience)" has been cited twice now from
a Researcher constitution CTO hasn't seen — only knows it exists because
it's been referenced. That document needs to be in a form CTO can
actually read before it keeps being invoked as the basis for real
placement decisions. Get it somewhere checkable.

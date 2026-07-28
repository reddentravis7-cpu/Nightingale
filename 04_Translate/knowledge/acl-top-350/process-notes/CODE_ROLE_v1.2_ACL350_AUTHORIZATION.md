# Steward Role v1.2 — ACL TOP 350 CTS authorization

**Issued by:** CTO, with Founder sign-off
**Supersedes:** Role v1.1 (Cisco IOS validated, HL7/FHIR interim)
**Change:** adds ACL TOP 350 CTS as an authorized domain. Everything in
v1.1 stays in force unchanged — this is an addition, not a rewrite.

---

## Why this exists

Code raised this itself, correctly: extending stewardship into a new
domain is a decision that should be made on purpose, not assumed by
proceeding. Same standard HL7 got before Code started Phase 3/5 work on
it. This document is that explicit assignment for ACL TOP 350.

## Scope of authorization

Code is authorized to perform Steward review — Phase 3 concept
validation, Phase 5 dependency-graph and block review, block-by-block
content review — on ACL TOP 350 CTS content, under the following
conditions, all of which Code named as necessary and none of which are
weakened here:

**1. Bound by `TRANSLATE_SCOPE_CONSTITUTION.md` in full**, including the
sentence-level enforcement clause. Capability-level charter compliance is
the first filter, not the only one — every drafted block gets the
Alarm-327-style test applied at the sentence level, same as Code already
demonstrated doing on the scope-check-array watch-list flags.

**2. Tighter promotion bar than HL7 or Cisco.** This domain sits closer
to patient-safety territory — HL7 is data interchange, ACL TOP 350 is
operating-procedure content for a device whose results feed real
anticoagulation decisions, even with clinical-judgment content
structurally excluded. Concretely: a block doesn't get promoted to
`current` on the same confidence threshold that was fine for a Cisco
`show` command. Where there's genuine doubt about whether content stays
inside the operational-behavior boundary, the default is the same as any
ambiguous scope question — exclude or flag, don't promote to close out a
checklist.

**3. IP posture stays open, separately.** This authorization covers
technical-content review. It says nothing about the derivative-work
question raised earlier (content built from Werfen's own manuals,
product potentially shown back to Werfen) — that still needs its own
answer from someone with real IP competence before content production
scales up, independent of whether this authorization exists.

**4. `scope_check_array.py` (now on `main` at `a4eee91`) is available as
a first-pass tool, not a substitute for judgment.** Run it, use it to
narrow what needs a human look, don't treat a clean pass as a promotion
decision by itself.

## Out of scope, still

Capability 10-equivalent work (if ACL TOP 350 ever needs a v2-to-FHIR-style
mapping capability), the `StructuralContent`/potential-third-shape
architectural question, and Cisco's remaining audit — unchanged from
before, unrelated to this authorization.

## Effective

Now. Code may begin Phase 3 concept validation on Research's capability
decomposition as soon as Research produces it.

# Steward Review — `Capability` schema object

**Reviewer role:** Steward (per `docs/roles/steward.md`, TRANSLATE-ROLE-STEWARD-v1.0, implements CCO v1.0)
**Under review:** the `Capability` first-class object + retrofit, `knowledge-block-model.md` §2b (as of `269081b`)
**Date:** 2026-07-30
**Primary question applied:** *"What is correct?"*

---

## Firewall disclosure (read first)

This object was **proposed by Code wearing the CTO hat**, and is being reviewed
by Code wearing the Steward hat. Steward Principle 4 (*no self-supplied
evidence*) and the discipline-crew discover/validate firewall — *"one persona
must never both discover a fact and stamp it"* — mean **this review cannot be
the final certification.** It stands as the technical new-shape pass the schema
doc calls for on every addition, and it is deliberately more critical because of
the self-review, not less. Promotion to *settled* still requires an independent
Steward or Architect ratification. Recorded per CCO Obligation 5 (document
uncertainty).

---

## Composite outcome

A schema addition is not one claim, so it does not get one verdict. Per the
Six-Outcome Decision Matrix, each component gets its own outcome and written
justification:

| Component | Outcome | One-line basis |
|---|---|---|
| Object field set / envelope | **Approve with Constraints** | Shape is sound and reusable; three permanent constraints attach. |
| `operational` state semantics | **Hold** | Two precise unresolved requirements — the invariant is unenforceable and uncomputable as written. |
| Retrofit (the five entries) | **Return for Editing** | States are correct and verified; they are mislabeled as capabilities when they are domain rollups. |

Not a clean Approve. Also not a Reject or a Return-for-Research — the evidence is
present and verified; the gaps are structural/definitional, which is precisely
what Hold and Return-for-Editing are for.

---

## Findings

### F1 — `operational` is "computed, never hand-set," yet typed as a stored enum value. **(Hold)**

`capabilityState` is a single stored field whose enum includes `operational`.
If the field is stored, *something writes `operational` into it* — at which
point "never hand-set" is prose, not a guarantee. This is the same class of gap
the block model already closed once: `reviewStatus: "current"` is not honored on
convention, it is gated on `reviewedBy` + `url` + `dateReviewed`, *"enforced as a
gate, ideally a DB CHECK constraint, not just app-code convention"* (after the
Cisco placeholder-`current` incident).

**Precise unresolved requirement:** the schema must express that `operational`
is a *computed projection*, not a stored assignment — e.g. `capabilityState`
stores `draft | structured | validated | authorized` and `operational` is
derived, or `operational` is a separate computed boolean/view. As written, the
field's type contradicts its own defining rule.

### F2 — `operational` cannot be computed from the object as specified. **(Hold)**

`operational` is defined against *"the Blocks carrying its locked/OEM-specific
content."* But `evidence: [blockId]` is undifferentiated — nothing in the object
identifies **which** evidence blocks carry the OEM-specific content versus the
public-standard content. The computation defined in F1 therefore has no input to
run against.

**Precise unresolved requirement:** a way to identify the OEM-specific evidence
subset — a per-evidence flag, or an explicit link from `oemReference` to the
blocks it governs. Without it, `operational` is undefined for any locked
capability, which is exactly the population Analytics most needs it for.

### F3 — The retrofit entries are domain rollups mislabeled as capabilities. **(Return for Editing)**

Per the Capability Map Process node structure (Capability → Sub-capability →
Concept → Block), a domain contains **many** capabilities — GE OEC One CFD has
12. The retrofit's `cap.cisco-ios`, `cap.ge-oec-one-cfd`, etc. are **one entry
per domain**: domain-level rollups, not `Capability` instances. Presenting them
as `Capability` objects conflates two levels of the very hierarchy this object
is supposed to encode.

The *substance* is sound — the five states were verified against live JSON, not
guessed, and the author already flagged the per-domain-vs-per-capability
question honestly. So this is representation, not correctness: **Return for
Editing**, not Reject. Restructure the five as explicitly-labeled *provisional
domain rollups* (a distinct, legitimate thing) pending per-capability
enumeration — do not let `cap.<domain>` masquerade as a single capability.

### F4 — Field set / envelope. **(Approve with Constraints)**

The object is well-formed: it leaves `KnowledgeBlock` and `Collection`
untouched, reuses `sourceOfTruth` inside `oemReference`, and the honesty note
correctly refuses the "touched nothing foundational" framing — this *is* the
first new top-level object since the envelope/content split, and it says so.
Approved, with three **permanent** constraints (Principle 3 — constraints
attached at approval are not later dropped):

- **C1 — `safety` and `risks` are system-behavior description only.** Both fields
  invite drift into professional judgment. They are bound by the Scope
  Constitution's sentence-level exclusion test exactly as `fieldNotes` is: a
  `safety` string may describe what the system does or flags, never what a person
  should decide about a person/animal/property. Permanent; the harm boundary does
  not soften.
- **C2 — `safety`, `requiredSkills` (and any difficulty-like field) are
  editorial/neutral-fact only,** not authoritative gates — per the standing
  principle "the schema describes reality; the application decides how to use it."
- **C3 — authority consistency.** A block citing an OEM-class `sourceOfTruth` may
  not sit in the `evidence` of a capability whose `oemReference.locked: true`.
  This is CCO Obligation 4 made checkable, and it is the constraint F2's
  mechanism should also enable.

---

## Checklist (Steward Charter §7)

- Claims backed by cited source of stated category? **Yes** — retrofit states
  read from tracked JSON + PROJECT_STATUS, cited per entry.
- Conflicting sources surfaced, not silently resolved? **Yes** — GE OEC's three
  unreconciled Phase 6 attempts are named, not smoothed.
- Constraints explicit and permanent? **Now yes** — C1–C3 attached above.
- Uncertainty disclosed? **Yes** — granularity question and self-review both on
  the record.
- Safety implication changes the call? **Yes** — drove C1.
- Dependency/relationship to other objects correct? **Partially** — F1/F2 are
  precisely where it is not yet, hence the Hold.

## The two tests (§9)

- **One-year test:** I would defend approving the field set under C1–C3 a year
  from now. I would **not** defend approving `operational` as written — its type
  contradicts its rule. → Hold on that component.
- **Reasonable Doubt Test:** an informed reviewer would doubt that `operational`
  is enforceable or computable as specified. Doubt present → Hold/Return, not
  Approve.

---

## What clears the Hold

Not "more work" (that would be a vague hold, a §11 failure mode). Specifically:

1. Re-specify `capabilityState` so `operational` is computed, not stored (F1).
2. Add the mechanism to identify the OEM-specific evidence subset (F2).
3. Relabel the retrofit as provisional domain rollups, or decompose to real
   capabilities (F3).

Items 1–3 are CTO/author edits — the Steward returns, it does not rewrite
(Charter §6). When they land, this object is re-reviewable; and because of the
firewall disclosure above, that pass should be an independent seat or the
Architect, not this one.

*Steward review v1 — 2026-07-30. Provisional pending independent confirmation.*

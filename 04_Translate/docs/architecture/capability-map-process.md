# Capability Map Process (v1.0)

**Status:** Adopted, evidence-based — derived from the Cisco IOS QRG buildout
and the first live HL7/FHIR trial run (this document).

---

## What this replaces

Domain scoping used to happen implicitly. For Cisco it worked because Jeremy
had already solved the dependency problem in his head: binary → hex →
subnetting → switching → routing. That structure got translated into 5
directories, 40 categories, 77 blocks — but nobody wrote down *how* that
structure got decided. This document is that write-up, prompted by watching
the same process happen live and correctly on HL7.

---

## The node structure

Every domain decomposes the same way, regardless of subject matter:

```
Capability
  └── Sub-capability
        └── Concept
              └── Knowledge Block
                    └── Evidence
```

Not "Chapters." Chapters implies a book's table of contents — arbitrary,
author-chosen. Capabilities implies dependency — what a person or system
must be able to do, and what that depends on being able to do first. Cisco's
"chapters" were never arbitrary; they were capabilities in a book's clothing.
Naming them correctly matters because it's what makes the next step
possible.

---

## The loop: Research proposes, Steward validates

Not one role dumping content on another. Both working the same problem from
different vantage points.

**Phase 1 — Research: "What are the major capabilities?"**
A first-pass map of the domain's top-level divisions.

**Phase 2 — Research: "What depends on what?"**
Ordering those divisions into an actual dependency chain, not just a list.

**Phase 3 — Steward: "Is this dependency graph technically correct?"**
Not "is this a good outline" — a substantive correctness check against how
the domain actually works. This is where real errors get caught, and it
only works if the Steward is checking facts, not just reviewing structure.

**Phase 4 — Research:** decompose each validated capability into concepts.

**Phase 5 — Steward:** validate the concepts.

**Phase 6 — CTO:** represent the validated concepts as Knowledge Blocks —
Entity, InvokableContent, Procedural, whichever shape fits.

The loop repeats as new domains are added. Nobody's map is final on the
first pass — that's the point of the loop, not a flaw in it.

---

## Worked example: HL7 first pass, and what got caught

**First draft (Ledger):**
```
1. Introduction
2. HL7 v2 Fundamentals
3. Message Structure
4. ORU Messages
5. ADT Messages
6. Orders
7. FHIR Resources
```

**Steward review (Code) caught three real problems, not style
preferences:**

1. **Ordering was backwards.** ADT establishes patient/encounter context
   (PID, PV1) that Orders and Results reference. Orders conventionally
   precede Results — a result implies a prior order existed. The draft had
   Results (4) before Orders (6) and before ADT (5). Correct dependency
   order is ADT → Orders → Results.
2. **A load-bearing gap before any message type.** Segments, fields,
   components, and encoding characters (`|^~\&`), plus the ACK/NACK model,
   underpin every message type that follows. Unclear whether "Message
   Structure" (3) already covers this or whether it's missing entirely —
   flagged rather than assumed either way.
3. **FHIR Resources as one chapter is a granularity mismatch.** Five v2
   chapters got fine-grained treatment; FHIR got flattened into one. FHIR's
   RESTful resource-interaction paradigm is different enough from v2's
   message-passing paradigm that it likely needs its own structural
   treatment before individual resources (Patient, Encounter, Observation,
   ServiceRequest) get decomposed.

All three are technically sound, not process theater — checked against how
HL7 v2 and FHIR actually work, the same way "you can't understand routing
without IP addressing" is a fact about networking, not a style opinion.
That's what makes the Steward role real: it produced a correct technical
objection on its first real use, not just a plausible-sounding one.

**Corrected capability order:**
```
1. Introduction
2. HL7 v2 Fundamentals
3. Message Structure (segments, fields, components, encoding chars, ACK/NACK*)
4. ADT Messages (patient/encounter context)
5. Orders (ORM/OML)
6. ORU Messages (results — depends on 5)
7. FHIR — Resource Model & RESTful Interactions (paradigm: CRUD on typed
   resources, URL patterns, CapabilityStatement discovery)
8. FHIR — Terminology & Vocabulary Binding (CodeSystem, ValueSet,
   ConceptMap; LOINC/SNOMED/ICD as external code systems referenced by
   binding, not baked into individual resources)
9. FHIR Resources (Patient, Encounter, Observation, ServiceRequest, ...)
10. v2-to-FHIR Mapping — still open, see below
```
*ACK/NACK flagged as a likely gap, not yet sourced — see Phase 4 doc.

The vocabulary question is resolved, not still open: FHIR's own
terminology model (CodeSystem/ValueSet/ConceptMap) is a real, distinct
capability — bindings are referenced across many resources rather than
duplicated inside each one, so it earns its own chapter (8) ahead of
individual Resources (9). Confirmed via FHIR's terminology spec, not
assumed.

The v2-to-FHIR mapping question is genuinely still open, and it's a
different thing than it first looked like. FHIR's `ConceptMap` resource
maps between code systems *within* FHIR's own terminology model — that's
now covered under capability 8. Translating v2's message-based semantics
into FHIR's resource-based semantics is a separate concern, and no source
confirming it as an in-scope chapter has been found yet. Left as capability
10, unconfirmed, rather than assumed in or out.

---

## Answering the "one agent per discipline" question directly

No — same principle as the content architecture. Entity, InvokableContent,
and Capture Context aren't reinvented per domain; the shape is reused and
the domain-specific fields sit on top of it. Roles work the same way. There
is one Research role and one Steward role, reused across Cisco, HL7,
Home Repair, whatever comes next. What's domain-specific isn't the agent —
it's the Capability Map each domain produces when Research and Steward run
the loop against that domain's own source material.

Standing up a new "kind" of agent per discipline would be the organizational
version of the mistake already rejected on the content side — bespoke
structure where a reusable one already exists. The thing that scales is the
loop, not the headcount.

---

## Status of "Editor" — resolved here because it wasn't written down anywhere

Surfaced by the GE OEC One CFD kickoff cross-check: the phase sequence
above has three roles (Research, Steward, CTO), no Editor. A separately
drafted Researcher constitution for that same domain named a three-role
handoff (Researcher → Editor → Steward) instead. Two different documents,
two different role counts, and nothing on record explaining why.

The actual answer, on record now: Editor/overall-steward was discussed
as a real, named idea — a role that would sit across multiple domains
once cross-domain consistency stops being something shared documents can
hold together on their own — and was explicitly deferred by the Founder
until there are enough simultaneous domains and reviewers to need it.
Not "CTO wearing a different hat" and not "nobody's scoped it" — it's a
real proposed role, intentionally not yet active. This document's phase
sequence (Research → Steward → CTO, no Editor) is the current, correct
one to build against until that trigger condition is actually met.

The gap that caused the confusion wasn't the idea being unclear — it was
this decision being made in conversation and never landing in a document
a new participant could actually read. Written down now specifically so
it doesn't have to be rediscovered the same way again on the next new
domain or the next new pairing.

---

## The reflexive part worth naming

The node structure above — Capability → Sub-capability → Concept →
Knowledge Block → Evidence — is the same shape Translate uses to structure
its *product*. This document just used that shape to structure Translate's
own *process* for building the product. The company is organizing its own
work the same way it organizes the knowledge it sells. That's not a
coincidence worth losing — it's the strongest evidence yet that the
architecture is actually general, not merely reused by convenience.

---

## Deferred: paced, automated handoff (not built — structural note only)

Raised, not scheduled: whether the Research/Steward loop, or a CTO/Ledger
exchange, should eventually run on an actual timer with a real handoff
between turns, instead of always being relayed by hand. The mechanism for
the timer side already exists (scheduled tasks); the bridge to Ledger's
side does not, and building either is explicitly not happening now. This
note exists only so nothing built in the meantime forecloses it.

What that means concretely, while building:

- Each phase's output (capability map, concept decomposition, Steward
  review) should land as its own durable document — same as this file —
  not only as conversation content. A scheduled process can pick up a
  document later; it can't pick up a chat turn that only exists in
  context.
- Don't assume a phase completes synchronously in one sitting. The loop
  should tolerate a gap between Research producing something and Steward
  reviewing it, since that gap is exactly what a timer would formalize
  later.
- Travis relaying between CTO and Ledger by hand is the current
  implementation of the handoff, not a permanent property of the loop
  itself. Nothing about the phase structure should depend on him being the
  transport layer specifically.

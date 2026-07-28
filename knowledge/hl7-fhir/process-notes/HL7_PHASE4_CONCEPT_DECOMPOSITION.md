# HL7 v2 — Phase 4 Concept Decomposition (Research draft, revised after Phase 5)

**Status:** Capabilities 1–6 (v2) — **locked.** Phase 5 re-confirmed both
fixes (NK1 cardinality, ORM→OMG/OML/OMD/OMS/OMN/OMI/OMP migration) and the
ACK/NACK addition (MSA-1/MSA-2, MSH+MSA+SFT/ERR structure, original vs.
enhanced mode) as correct. Ready for Phase 6 (CTO — represent as Knowledge
Blocks).

Capabilities 7–9 (FHIR) — two wording fixes applied per first-pass Phase 5
review (SNOMED binding-strength overstatement in capability 8, Patient
dependency overstatement in capability 9), plus a flag recorded for
capability 10 (`StructureMap`, not `ConceptMap`, is the actual candidate
for structural v2-to-FHIR mapping). Returned for one more confirmation
pass, not a full review.

---

## Capability 1 — Introduction

- What HL7 v2 is and the problem it solves: a message-passing standard for
  exchanging clinical/administrative data between healthcare systems.
- Where v2 sits relative to FHIR — different paradigm (message-passing vs.
  RESTful resources), not a version bump. Already established earlier in
  this project; not re-derived here.
- Scope boundary for this domain: v2.x structural/messaging mechanics,
  not clinical interpretation.

## Capability 2 — HL7 v2 Fundamentals

- A message is an ordered sequence of segments, each segment on its own
  line, terminated by a carriage return (hex 0D).
- A segment is a three-character segment ID followed by fields joined by
  the field separator.
- Every message declares its own delimiter set — this isn't fixed by the
  standard globally, it's declared per-message in the header.

## Capability 3 — Message Structure

- **MSH is always the first segment** in any v2 message — no message is
  valid without it.
- **The five standard delimiters** and what each one separates: field
  separator (`|`), component separator (`^`), repetition separator (`~`),
  escape character (`\`), subcomponent separator (`&`) — conventionally
  written `|^~\&`.
- **Where delimiters are declared:** MSH-1 is the field separator itself
  (whatever character immediately follows "MSH"); MSH-2 lists the other
  four in order (component, repetition, escape, subcomponent).
- **Field hierarchy:** fields → repetitions (via `~`) → components (via
  `^`) → subcomponents (via `&`). Each level only exists if the data
  requires that much structure.
- **Message typing:** MSH-9 identifies the message type/trigger event
  (e.g., `ADT^A01`), which is what determines which segments follow.
- **Acknowledgment model (gap closed, sourced):** every message gets
  acknowledged via a dedicated ACK message built around the MSA segment —
  MSA-1 carries the acknowledgment code, MSA-2 carries the original
  message's control ID. An ACK is short by design: MSH + MSA required,
  optional SFT (software) and repeating ERR (error detail) — it carries an
  outcome, not data.
- **Two acknowledgment modes, negotiated per message:** MSH-15 (Accept
  Acknowledgment Type) and MSH-16 (Application Acknowledgment Type)
  determine which mode is in force. In **original mode**, a single ACK
  completes the exchange. In **enhanced mode**, a CA (accept) ACK only
  confirms safe receipt — the sender must still wait for a separate
  application-level acknowledgment (AA/AE/AR) before treating the message
  as processed. This distinction matters for Orders/ORU specifically:
  which mode is in force changes what "the message was received" actually
  guarantees.

## Capability 4 — ADT Messages

- **Purpose:** broadcasts a patient's admission, discharge, or transfer
  event to downstream systems (lab, pharmacy, radiology, billing).
- **Required segment set:** MSH, EVN (event type), PID (patient
  identification), PV1 (patient visit) — these are the mandatory core.
- **Commonly present but optional:** NK1 (next of kin) — optional and
  repeating in the base standard (zero, one, or many NK1 segments per
  message); frequently made required by site-specific conformance
  profiles, but not mandatory in the base v2 standard itself. *(Revised
  per Phase 5 — NK1 was originally listed as core; it isn't.)*
- **PID carries patient demographics:** name, date of birth, medical
  record number, sex, address, phone.
- **PV1 carries visit-level data, not patient identity:** patient class
  (PV1-2: I/O/E for inpatient/outpatient/emergency), assigned location
  (PV1-3), attending physician (PV1-7).
- **Common event types in practice:** A01 (admission), A04
  (registration), A08 (patient update) — cited as the three that account
  for most real ADT traffic.

## Capability 5 — Orders

- **ORM^O01 is the order message, with a version caveat.** ORM^O01 was
  retained for backward compatibility only as of v2.4, and withdrawn as of
  v2.7. From v2.4 onward the standard directs implementers to the more
  specific trigger events instead: OMG^O19 (general clinical order), OML
  (laboratory, including specimen/container extensions), OMD, OMS, OMN,
  OMI, OMP. ORM remains extremely common in real-world interfaces for
  backward-compatibility reasons — which is presumably why it surfaced
  first — but stating it flatly without the version context would read as
  wrong against v2.4+. *(Revised per Phase 5.)*
- **ORC and OBR both carry order identity** — the placer order number
  appears in OBR-2 and/or ORC-2; at least one of the two must be present,
  and when both are present they should match.
- **Dependency this confirms:** an order references a patient/visit
  context already established by ADT (PID/PV1) — this is the concrete
  mechanism behind the ADT-before-Orders ordering the Steward flagged.

## Capability 6 — ORU Messages

- **Purpose:** carries observation/result data back from the filler
  (the system that performed the test) to the placer.
- **Structure:** OBR segment as a report header (restates order context —
  order number, request date/time, observation date/time, ordering
  provider), followed by one OBX segment per individual observation.
- **Filler order number** appears in OBR-3 and/or ORC-3; ORC is optional
  in ORU, so if it's absent the filler order number must be in OBR-3.
- **One-to-many relationship:** a single OBR can be followed by many OBX
  segments — one per discrete measurement the order produced.
- **Dependency this confirms:** a result restates and depends on the order
  that produced it — the concrete mechanism behind Orders-before-ORU.

---

## Capability 7 — FHIR: Resource Model & RESTful Interactions

- **Paradigm, stated precisely:** FHIR is RESTful in the ordinary industry
  sense — CRUD (create, read, update, delete) actions performed on a
  repository of typed, identified resources over HTTP, not a message
  broadcast to whoever's listening. This is the actual mechanism behind
  the paradigm-shift distinction already made against v2's message-passing
  model.
- **Same interaction set, every resource type:** each resource type
  exposes the same standard interactions (read, update, search, etc.),
  managed in a uniform, granular way — this uniformity is what makes the
  interaction model its own capability rather than something to explain
  once per resource.
- **Discovery mechanism:** a server's actual supported resources and
  interactions are discoverable at runtime via its `CapabilityStatement`
  (`GET [base]/metadata`) — the server declares its own behavior rather
  than an implementer assuming from documentation alone.

## Capability 8 — FHIR: Terminology & Vocabulary Binding

- **CodeSystem vs. ValueSet, precisely:** a `CodeSystem` defines a
  terminology's own codes; a `ValueSet` selects a usable subset of codes
  drawn from one or more CodeSystems for a specific purpose. They answer
  different questions — "what codes exist" vs. "which of those codes are
  valid here."
- **Binding is how an element gets tied to a ValueSet**, via
  `ElementDefinition.binding`, and binding strength changes what
  conformance actually requires: **required** (the code must come from the
  indicated value set), **extensible** (that value set should be used
  where it fits, but codes outside it are permitted when nothing fits),
  **preferred** (a consensus recommendation, not an enforced constraint),
  **example** (illustrative only — derived profiles may bind to any value
  set they choose).
- **External code systems (LOINC, SNOMED CT) are referenced, not
  reimplemented:** FHIR points at these terminologies rather than
  restating them, which is why this is a cross-cutting capability rather
  than something duplicated inside Observation, Condition, etc.
  individually. Worth flagging: SNOMED CT's restrictive licensing means
  the base FHIR spec predominantly uses it in example bindings, with
  occasional preferred-strength bindings — required strength is avoided
  specifically because of the licensing, not used as an absolute rule.
  *(Revised per Phase 5 — originally stated as universal; it isn't.)*
  Jurisdictional implementation guides may require a license to bind it
  more strongly still.
- **`ConceptMap` maps between code systems inside this model** — e.g.,
  translating a local lab code to a LOINC code. This is the resource that
  was initially conflated with "v2-to-FHIR mapping" (capability 10); it
  only covers mapping within FHIR's own terminology layer, not translating
  v2 message semantics into FHIR resource semantics.
- **Flag for capability 10, not a claim about it (per Phase 5):** the
  resource actually built for structural message-to-resource mapping is
  `StructureMap` (the FHIR Mapping Language), not `ConceptMap` —
  `ConceptMap` only translates codes between systems. Not asserting this
  is capability 10's answer, just recording it now so Research doesn't
  rediscover it from scratch when that capability gets picked up.

## Capability 9 — FHIR Resources (initial set)

- **Patient:** represents the person receiving care. Identity is a
  first-class resource, not a segment embedded in something else (contrast
  with v2's PID, which only exists inside a message that also carries
  other segments). *(Scoped per Phase 5 — not every FHIR resource depends
  on Patient; Organization, Practitioner, CodeSystem, ValueSet, and others
  don't reference it at all.)* It's specifically patient-context clinical
  resources — Observation, Encounter, ServiceRequest, Condition, and
  similar — that carry a `subject`/`patient` reference back to it.
- **Encounter:** represents when and where care happened. FHIR's model
  treats care as happening *inside* an encounter — this is the structural
  analogue of v2's PV1, but as its own standalone, referenceable resource
  rather than a segment.
- **Observation:** expresses a name/value pair or a structured set of
  them — a measurement or point-in-time assessment. This is the structural
  analogue of v2's OBX, generalized to also cover things OBX wasn't built
  for (baselines, patterns, demographic characteristics).
- **ServiceRequest:** the analogue of v2's order (ORC/OBR territory) — a
  request for a service to be performed.
- **Resources reference each other by typed `Reference` fields**, forming
  a directed graph rather than a flat message — this is the structural
  reason FHIR needed its own Resource Model capability (7) before any of
  these could make sense on their own.

---

## Domain Dependency Graph (v1, Research draft — pending Steward review)

Not a tree. Several nodes are genuinely shared across branches, and
drawing this as exclusive containment would hide the reuse that matters
for how Phase 6 wires `prerequisites`/`relatedBlocks` later.

```text
HL7 v2 — dependency graph
(edges read "requires" / arrows point to what must exist first)

Introduction ──▶ Fundamentals ──▶ Message Structure
                                        │
                        ┌───────────────┼───────────────────┐
                        ▼               ▼                   ▼
                  MSH + Delimiters   Field Hierarchy    ACK/NACK (MSA)
                  (MSH-1/MSH-2,      (field→repetition  [shared — every
                   MSH-9 typing)      →component→        message type
                                      subcomponent)       below depends
                                                          on this, not
                                                          just ADT]
                        │
                        ▼
                      ADT ──requires── Message Structure
                        │
              ┌─────────┼─────────┐
              ▼         ▼         ▼
            EVN       PID       PV1          NK1 (optional,
          (required) (required)(required)     not required —
                                               attaches to PID/PV1
                                               context, doesn't
                                               gate anything below)
                        │
                        ▼
                     Orders ──requires── ADT (needs PID/PV1 context)
                        │
                  ┌─────┴─────┐
                  ▼           ▼
                ORC          OBR ──────┐ [OBR is shared — reused
             (order id,   (order id,   │  below as ORU's report
              ORC-2)       OBR-2)      │  header, not a separate
                                       │  segment]
                                       ▼
                     ORU ──requires── Orders (result implies prior order)
                        │
                  ┌─────┴─────┐
                  ▼           ▼
              OBR (reused,   OBX (repeating,
              report header)  one per observation)

    ACK/NACK (MSA) ── referenced by ──▶ ADT, Orders, ORU
    [every message type above gets acknowledged through the same
     mechanism — this is a cross-cutting dependency, not a child of
     any one message-type capability]
```

```text
FHIR — dependency graph

Resource Model & RESTful Interactions
   (CRUD verbs, CapabilityStatement)
              │
    ┌─────────┴─────────┐
    ▼                   ▼
Terminology &      FHIR Resources
Vocabulary Binding  (Patient, Encounter,
(CodeSystem,        Observation, ServiceRequest)
 ValueSet,               │
 binding strength)       │
    │                    │
    └────referenced by───┘
         [Resources use Terminology bindings on their coded
          elements — this is a "referenced by," not exclusive
          containment; Terminology doesn't belong to Resources]

Patient ◀── subject/patient reference ── Encounter, Observation,
                                          ServiceRequest
[Patient is a shared reference target, not a parent — Organization,
 Practitioner, CodeSystem, ValueSet etc. don't reference it at all,
 consistent with the Phase 5 correction already made to capability 9]

v2-to-FHIR Mapping (capability 10, open)
   requires: both graphs above to exist first
   candidate mechanism flagged: StructureMap (not yet researched)
```

This is the artifact Phase 6 should build from — not "what blocks should
I make," but "does this representation faithfully carry the shape above."
Shared nodes (OBR, ACK/NACK, Patient) are exactly where `relatedBlocks`
should do real work instead of `prerequisites` alone, per the
derive-don't-duplicate rule already established for the architecture.

---

## Handoff

Capabilities 1–6: **Phase 5 confirmed, locked.** Move to Phase 6 — CTO
represents these as actual Knowledge Blocks (syntax, examples, field
notes — the Cisco level of detail, not concept summaries), each gated by
its own sourceOfTruth/reviewedBy/dateReviewed before promotion to current.

Capabilities 7–9: two wording fixes applied per Phase 5's first pass
(SNOMED binding strength, Patient dependency scope). Ready for Steward
confirmation — expected to be one more pass, not a full re-review.

Capability 10 (v2-to-FHIR mapping): still genuinely open. `StructureMap`
flagged as the likely candidate resource, not yet researched or resolved
— next real task when this capability gets picked up.

---

## Sourcing correction (post-Phase 6): two look-alike HL7 documentation families

Found and fixed by the Steward re-checking `hl7v2.pid-segment` field by
field rather than trusting the original search summary: PID-7 and PID-8
were recorded as `DTM`/`CWE`. The correct data types for the cited version
(2.5.1) are `TS`/`IS`. Both fixed in `hl7-knowledge-blocks.json`.

The root cause is worth keeping on record for every future HL7 citation in
this project, not just this one block. There are two live HL7 documentation
families online that look interchangeable but aren't:

- **Version-pinned original standard text** — `hl7.eu/HL7v2x/v2XX/std2XX/...`
  — the actual historical text for a specific version, e.g. 2.5.1.
- **HL7's "V2+" harmonized/refactored reference** — `v2plus.hl7.org`, its
  NIST mirror, and `hl7.eu/refactored` (no version number in the URL is the
  tell) — a newer, consolidated reference that modernizes data types across
  the whole v2 line. Real and official, just not the same thing as the
  version being cited.

Citing the harmonized family while claiming a specific version number gives
a plausible, wrong answer — exactly what happened here. Two sources
agreeing isn't independent corroboration if they're both mirrors of the
same harmonized family; check which family a URL belongs to before trusting
agreement between them. Blocks in this file that don't claim a specific
`sourceOfTruth.version` (MSH, EVN, NK1, ORC, OBR, OBX) aren't at risk of
this specific error, since they're not claiming to match a historical
version in the first place — PID and PV1 were the two blocks actually
exposed to it. PV1's fields (IS/PL/XCN) were separately re-checked against
the version-pinned source and confirmed correct.

**Second pass (full re-check, all remaining v2 blocks) — two more of the
same error found and fixed:**

- `NK1-3` (Relationship): was `CWE`, version-pinned source confirms `CE`.
  Fixed.
- `OBR-4` (Universal Service Identifier): was `CWE`, version-pinned source
  confirms `CE`. Fixed.
- `OBX-3` (Observation Identifier): sourcing came back genuinely
  contradictory this time — one result called it "Coded Element (CWE)",
  which conflates two distinct HL7 type names rather than confirming
  either one. Left as `CWE` but flagged with a confidence note in the
  block itself rather than guessed at — this is the honest outcome of a
  check, not every field resolves cleanly, and asserting a fix on
  ambiguous evidence would repeat the same mistake in the opposite
  direction.
- Confirmed correct, no change needed: `MSH-9` (MSG), `EVN-1`/`EVN-2`
  (ID/TS), `NK1-1`/`NK1-2` (SI/XPN), `ORC-2`/`ORC-3` (EI).
- Consistent with the pattern but not backed by an explicit literal
  citation: `MSH-1`, `MSH-15`/`MSH-16`, `ORC-1`, `MSA-1`, `MSA-2` — all are
  HL7-table-driven or otherwise typical fields where the inferred type
  (`ST`/`ID`) fits strongly, but no search surfaced a direct "the data
  type is X" statement the way it did for the fields above. Worth a
  dedicated pass if these ever need to be cited as fully verified rather
  than reasonably inferred.

CE vs. CWE turns out to be the same harmonization trap as PID's TS/DTM and
IS/CWE — CWE is CE's later, richer successor across the v2 line, so a
harmonized-family source says CWE where an original version-pinned text
says CE. Same root cause, different fields — worth treating this specific
pair as a known trip-wire for every future HL7 field, not just the ones
already checked.

---

## Sources

**Primary standard text (hl7.eu chapter mirrors / v2plus.hl7.org segment
definitions) — used for the two Phase 5 revisions:**
- [NK1 - Next Of Kin / Associated Parties Segment](http://v2plus.hl7.org/2021Jan/segment-definition/NK1.html)
- [HL7 Version 2.7 — Conformance/Introduction](https://v2.hl7.org/conformance/HL7v2_Conformance_Methodology_R1_O1_Ballot_Revised_D9_-_September_2019_Introduction.html)
- [HL7 v2.4 Chapter 4 — Order Entry](https://www.hl7.eu/HL7v2x/v24/std24/ch04.htm)
- [HL7 Version 2.6 Chapter 4 — Order Entry](https://www.hl7.eu/HL7v2x/v26/std26/ch04.html)
- [HL7 Version 2.7 Chapter 4 — Order Entry](https://www.hl7.eu/HL7v2x/v27/std27/ch04.html)
- [OMG O19 - General Clinical Order Trigger Event](https://hl7-definition.caristix.com/v2/HL7v2.6/TriggerEvents/OMG_O19)
- [HL7 V2 ACK Guidance - Conformance](https://confluence.hl7.org/spaces/CONF/pages/256183953/HL7+V2+ACK+Guidance)
- [HL7 v2.5.1 Chapter 2 (ACK/acknowledgment)](https://www.hl7.eu/HL7v2x/v251/std251/ch02.html)

**FHIR primary sources (capabilities 7–9):**
- [RESTful FHIR API — hl7.org](https://www.hl7.org/fhir/http.html)
- [FHIR Terminology — hl7.org R4](https://hl7.org/fhir/R4/terminologies.html)
- [ElementDefinition — FHIR build](https://build.fhir.org/elementdefinition.html)
- [FHIR Observation Resource](http://hl7.org/fhir/observation.html)
- [HL7 FHIR Encounter Resource](https://www.hl7.org/fhir/encounter.html)

**Orientation sources — original pass, capabilities 1–3 and 6 (no Phase 5
issues raised against these):**
- [MSH - Message Header Segment - HL7 - REFACTORED](http://v2plus.hl7.org/2021Jan/segment-definition/MSH.html)
- [HL7 v2.5.1 Chapter 2](https://www.hl7.eu/HL7v2x/v251/std251/ch02.html)
- [2.24.1 MSH - message header segment](https://www.hl7.org/documentcenter/public/wg/conf/HL7MSH.htm)
- [HL7 v2 Encoding & Delimiters | Saga IT Docs](https://saga-it.com/docs/hl7/reference/encoding)
- [HL7 PID Patient Identification | Rhapsody](https://rhapsody.health/resources/hl7-pid-segment/)
- [HL7 ADT Messages Explained: A Complete Guide to Patient Event Notifications](https://www.hl7-integration.co/post/hl7-adt-messages-explained)
- [HL7 Observation Request Segment (OBR) - Rhapsody Health](https://rhapsody.health/resources/hl7-obr-segment/)
- [HL7AU - HL7V2 WG : 4 Observation Reporting](https://hl7.org.au/archive/hl7v2wg/4-Observation-Reporting_1278278.html)

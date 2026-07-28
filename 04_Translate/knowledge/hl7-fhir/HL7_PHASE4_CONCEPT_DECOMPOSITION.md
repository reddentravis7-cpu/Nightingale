# HL7 v2 / FHIR — Phase 4 Concept Decomposition

**Status:** Capabilities 1–9 locked (Phase 5 confirmed). Capability 10 (v2-to-FHIR mapping) intentionally open. All 15 corresponding Knowledge Blocks authored and Steward-reviewed — see `hl7-knowledge-blocks.json`.

## Capability 1 — Introduction
HL7 v2 is a message-passing standard for exchanging clinical/administrative data between healthcare systems. FHIR sits at a different paradigm (RESTful resources, not message-passing), not a version bump. Scope: v2.x structural/messaging mechanics, not clinical interpretation.

## Capability 2 — HL7 v2 Fundamentals
A message is an ordered sequence of segments, each on its own line, terminated by a carriage return (hex 0D). A segment is a three-character segment ID followed by fields joined by the field separator. Every message declares its own delimiter set in its header, not fixed globally.

## Capability 3 — Message Structure
MSH is always the first segment. The five standard delimiters (`|^~\&`): field, component, repetition, escape, subcomponent. MSH-1 is the field separator itself; MSH-2 lists the other four in order. Field hierarchy: fields → repetitions → components → subcomponents. MSH-9 identifies message type/trigger event and determines which segments follow. Acknowledgment model: every message gets acknowledged via MSA (MSA-1 code, MSA-2 control ID echo); ACK is MSH + MSA required, optional SFT/ERR. Two acknowledgment modes negotiated via MSH-15/MSH-16 — original mode (single ACK) vs. enhanced mode (CA receipt-ack, then separate application-level AA/AE/AR ack).

## Capability 4 — ADT Messages
Broadcasts admission/discharge/transfer events. Required core: MSH, EVN, PID, PV1. NK1 is optional/repeating, not core. PID carries demographics (name, DOB, MRN, sex, address, phone). PV1 carries visit-level data (patient class, location, attending physician), not patient identity. Common event types: A01 (admission), A04 (registration), A08 (update).

## Capability 5 — Orders
ORM^O01 was retained for backward compatibility only as of v2.4, withdrawn as of v2.7 — superseded by OMG^O19 (general clinical order), OML, OMD, OMS, OMN, OMI, OMP. ORC and OBR both carry order identity (placer number in OBR-2/ORC-2, at least one required, should match when both present). Orders require ADT's PID/PV1 context.

## Capability 6 — ORU Messages
Carries results from filler back to placer. OBR is the report header (restates order context), followed by one OBX per observation. Filler order number in OBR-3/ORC-3; ORC is optional in ORU so OBR-3 is often the only place it appears. One-to-many OBR:OBX. Results depend on the order that produced them.

## Capability 7 — FHIR: Resource Model & RESTful Interactions
FHIR is RESTful in the ordinary industry sense — CRUD over HTTP against typed, identified resources, not message broadcast. Every resource type exposes the same standard interaction set. Discovery is runtime, via `CapabilityStatement` (`GET [base]/metadata`) — the server declares its own behavior.

## Capability 8 — FHIR: Terminology & Vocabulary Binding
`CodeSystem` defines a terminology's own codes; `ValueSet` selects a usable subset for a purpose. `ElementDefinition.binding` ties an element to a ValueSet with strength required/extensible/preferred/example. SNOMED CT's licensing means base FHIR predominantly uses example-strength bindings (occasionally preferred, essentially never required) — a pattern, not an absolute rule. `ConceptMap` translates between code systems within FHIR's terminology layer only — it does not solve v2-to-FHIR structural mapping. `StructureMap` (the FHIR Mapping Language) is the flagged candidate for that, not yet researched — reserved for Capability 10.

## Capability 9 — FHIR Resources
Patient, Encounter, Observation, ServiceRequest authored as the initial resource set. Patient is a shared reference target for patient-context clinical resources (via `subject`/`patient`), not a universal parent — Organization, Practitioner, CodeSystem, ValueSet etc. don't reference it. Resources reference each other via typed `Reference` fields, forming a graph rather than a flat message.

## Domain Dependency Graph
```
v2:  Introduction → Fundamentals → Message Structure → ADT → Orders → ORU
     ACK/NACK (MSA) is cross-cutting — referenced by ADT, Orders, and ORU, owned by none of them.
     OBR is a shared/reused node between Orders and ORU, not two separate concepts.

FHIR: Resource Model & RESTful Interactions → { Terminology & Vocabulary Binding, FHIR Resources }
      Terminology is referenced-by Resources' coded elements, not contained by them.
      Patient is a shared reference target for Encounter/Observation/ServiceRequest, not their parent.

Capability 10 (v2-to-FHIR mapping): requires both graphs above. StructureMap flagged, not yet researched.
```

## Sourcing correction: two look-alike HL7 documentation families
There are two live HL7 v2 documentation families online that look interchangeable and aren't:
- **Version-pinned original standard text** — `hl7.eu/HL7v2x/v2XX/std2XX/...` — the real historical text for a specific version (this project cites 2.5.1).
- **HL7's "V2+" harmonized/refactored reference** — `v2plus.hl7.org`, its NIST mirror, `hl7.eu/refactored` (no version number in the URL is the tell) — a newer, consolidated reference that modernizes data types across the whole v2 line.

Confirmed trip-wire instances, all resolved to the version-pinned answer: PID-7 (`TS`, not `DTM`), PID-8 (`IS`, not `CWE`), NK1-3 (`CE`, not `CWE`), OBR-4 (`CE`, not `CWE`), OBX-3 (`CE`, not `CWE` — this one was left flagged as contradictory in an earlier pass and is now resolved). Default to suspicion on any `CWE`/`DTM` result for a version-cited field until confirmed against a URL that actually encodes the cited version number.

## Handoff
All 15 blocks in `hl7-knowledge-blocks.json` are `needs-review` pending `sourceOfTruth.reviewedBy`/`dateReviewed` promotion — content is Steward-reviewed and sourced, but promotion to `current` is a separate, deliberate act per the schema's gate, not automatic on authoring. Capability 10 stays untouched. Cisco's remaining blocks are a separate, later effort.

# Lab Equipment Domain Template v1.0

**Status:** Generalized from the ACL TOP 350 CTS Research Charter v0.1,
now saved in full at `ACL350_RESEARCH_CHARTER_v0.1_ORIGINAL.md` so this
generalization is checkable rather than trusted on description. Diffed
against it directly: 11 of 12 capabilities below match the original
verbatim. Capability 12 does not — see note below. Not a new
architecture otherwise — the same move that turned Cisco's process into
`CAPABILITY_MAP_PROCESS.md` and HL7's review discipline into
`KNOWLEDGE_MAINTENANCE_PLAN.md`.

**Governed by:** `TRANSLATE_SCOPE_CONSTITUTION.md`, without exception.
Nothing below overrides it — this template exists inside that boundary,
not alongside it.

**How to use this:** copy the structure, fill in the device-specific
column, don't re-derive the source hierarchy or the capability skeleton
from zero each time. What's genuinely new per instrument is a small
fraction of the charter — most of it is this template plus facts.

---

## What's reusable across any lab instrument

The ACL TOP 350 charter's twelve capabilities turned out to describe
almost nothing specific to coagulation testing. Every clinical lab
analyzer — chemistry, hematology, immunoassay, coagulation, molecular —
shares this shape:

```text
Define the analyzer
    ↓
Prepare for operation
    ↓
Manage samples
    ↓
Manage reagents and consumables
    ↓
Execute a test
    ↓
Perform analytical measurement
    ↓
Manage calibration and quality control
    ↓
Produce and govern results
    ↓
Communicate with external systems
    ↓
Maintain the analyzer
    ↓
Detect and recover from failure
    ↓
Protect operational integrity*
```

*The original ACL TOP 350 charter names this capability "Protect
clinical operation," not "protect operational integrity" — the rename
is mine, proposed in the CTO charter review because the original wording
kept implying a clinical-safety scope this project deliberately stepped
back from. Presenting the renamed version as if it were pulled straight
from the charter, without flagging that it was an edit, was a real
provenance gap — corrected here. Use whichever name a given domain's
Founder/CTO actually ratifies; don't assume this one is settled.

This is the starting capability map for any new lab equipment domain.
Research still validates and adjusts it per instrument — a chemistry
analyzer's "perform analytical measurement" branches differently than a
coagulation analyzer's coagulometric/chromogenic/immunological split —
but the skeleton doesn't need to be invented again, the same way
`StructuralContent` didn't need reinventing for FHIR after HL7 v2.

## The source hierarchy — reusable as a discipline, not as a schema field

M1 (manufacturer-controlled), R1 (regulatory), E1 (expert field
knowledge, labeled with whose expertise and what domain), O1 (direct
observation), I1 (inference), U1 (unresolved). This came out of the ACL
TOP 350 charter specifically because public documentation was thin, and
it's a genuinely better discipline than HL7's single `sourceOfTruth`
object — but "backporting" it is not a relabeling.

M1–U1 implies comparing multiple class-tagged sources against the same
claim. The current `KnowledgeBlock` schema has one `sourceOfTruth`
object per block, singular. Actually adopting this means changing
`sourceOfTruth` from a single citation to an array of class-tagged
citations — which touches the schema itself, the promotion gate
(`reviewedBy`/`dateReviewed` currently live on one object, not N of
them — what does "reviewed" mean when five class-tagged sources exist
per claim and they don't all agree?), and `scope_check_array.py`'s
schema-completeness check, which currently assumes a single object.

That's a real schema migration, not a future improvement to note in
passing. Not started here, not sized as cheap, not assumed to happen
"eventually" without someone actually scoping the work — a decision for
whenever there's a concrete reason to do it, same evidence-based
discipline as everything else in this project.

## Scope-constitution application — do this explicitly, every time

Every domain charter must state which capabilities sit in the excluded
zone (diagnosis, treatment selection, patient management, interpretation
of results, clinical recommendations — or the equivalent for whatever
the instrument's output feeds into) and confirm none are being modeled.
Silence isn't compliance. For lab equipment specifically, the capability
most likely to carry the boundary inside it rather than around it is
**produce and govern results** — describe the software/workflow
mechanics (what triggers a flag, what gates release), exclude the
significance of the value itself. Same test as the Alarm-327 example,
every time.

## A third risk axis, distinct from scope and IP — name it now

Capability 12 ("protect clinical operation" / "protect operational
integrity" — see naming note above) covers access controls, user roles,
audit logging, backup/recovery, and cybersecurity boundaries for a
networked device that also handles patient data. Getting this content
wrong isn't a clinical-judgment violation — it doesn't touch diagnosis
or treatment, so the Scope Constitution doesn't catch it. It isn't a
copyright violation either. But an outdated hardening step or a stale
patch-level claim, presented as current, is wrong in a way that matters
for a device sitting on a clinical network — a different failure mode
than either axis already named in this project.

This is a specific, heightened case of the same staleness problem
`KNOWLEDGE_MAINTENANCE_PLAN.md` already exists to manage — but
security/access-control content deserves an explicitly tighter default
than ordinary staleness handling, because a false assurance here (a
block that says "hardened per X" when X is no longer current) is an
active risk, not just a less-useful one. Treat capability 12 content the
same way capability 8 gets treated for scope — flag it as a distinct
category needing its own review discipline, don't fold it silently into
"maintain the analyzer" or assume ordinary `dateReviewed` staleness
handling covers it. Not solved here — named here, before it's discovered
mid-production the way this template argues things should be.

## The expert-interview rule — reusable as-is

If a domain has an available E1 source (OEM-trained, field-experienced,
or otherwise credentialed to speak from direct expertise), their answers
get converted to the same claim/sourceClass/scope/confidence/exceptions
structure the ACL TOP 350 charter defined. Don't silently treat expert
memory as either unquestionable or unusable — structure it and let
Steward compare it against manufacturer text like any other claim.

## The first-vertical-slice pattern — reusable as-is

Before decomposing every capability in full, pick one routine, complete
workflow end to end (ACL TOP 350 used "routine PT sample, load to
transmission") as the first governed pathway. It's a hypothesis, not
canon, and its job is to surface real dependency structure and real
content-shape mismatches early, cheaply, before mass production — the
same role HL7's PID-7 catch played for the whole domain.

---

## What's genuinely domain-specific, per instrument

Fill this in fresh each time — this is the actual new work:

- Device identity: manufacturer, model, family relationships, GUDID
  record, intended use classification.
- The specific assay/test menu and which measurement branches apply.
- The specific alarm/error vocabulary and which are operator-recoverable
  vs. service-only.
- The specific external-system integration (LIS protocol, host
  communication standard — likely HL7 v2/FHIR again, which is exactly
  where this connects back to the existing domain rather than needing
  its own).
- Whatever access-classification and IP posture questions are specific
  to that manufacturer's documentation terms — never assume the ACL TOP
  350 answer carries over; each manufacturer's licensing situation is
  its own question.

## What this buys

The next lab instrument domain — any manufacturer, any modality — starts
from this template plus a source-hierarchy pass and a capability
validation, not from a blank page. The real cost per domain becomes
gathering and verifying the device-specific facts, not rebuilding the
scaffolding those facts sit in. That's the same economics that made HL7
faster than Cisco was, and Cisco's audit faster to scope than HL7's
research was from scratch.

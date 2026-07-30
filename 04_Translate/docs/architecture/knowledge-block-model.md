# Knowledge Block Model — v1 Draft (Round 1 reviewed)

**Status:** Draft — Round 1 review complete (Ledger). Pending Travis's
ratification before this becomes the standing model.
**Scope:** This is the format Translate moves forward with for every domain —
Cisco IOS, Python, Azure, HL7, FHIR, SQL, Linux, VMware, laboratory
automation, and whatever comes after. Medical device platforms are left off
this list for this pass only, not excluded as a standing decision — Cisco IOS is used
below only as the proving ground: it's the domain we have real content for,
not the domain the model is designed around. Nothing in the schema below is
Cisco-specific, and that's the test it has to pass.

**Standing principle, named explicitly because it kept showing up in
review:** the schema describes reality; the application decides how to use
it. Prerequisites, difficulty, and category membership all live in the data
as neutral facts or editorial hints — whether something blocks access,
requires completion, or gets emphasized is a product-mode decision made
above the schema, not encoded in it. Every time a workflow concern gets kept
out of the data model, that's flexibility bought for later at no cost now.

---

## 1. The Model

Two parts, per the envelope/content split from the design review:

- **`KnowledgeBlock`** — the envelope. Identity, cross-referencing, lifecycle,
  and metadata. Identical fields regardless of domain or content shape.
- **Typed content** — a payload shaped by *what kind of knowledge this is*
  (invokable, structural, procedural, conceptual, entity), not by which
  domain it came from. v1 ships one shape, `InvokableContent`, because
  that's what Cisco IOS needs. The other four shapes stay unbuilt until a
  domain produces content that doesn't fit — this is a ceiling, not a
  starting inventory.

```
KnowledgeBlock
  id                string     unique, stable, never reused even if deprecated
  title             string     canonical name, e.g. "show ip interface brief"
  aliases           [string]   alternate search terms, abbreviations
  domain            string     e.g. "cisco-ios" — where this came from
  blockType         enum       discriminator: "invokable" | "structural" |
                                "procedural" | "conceptual" | "entity"
  tags              [string]   facts about the block — what it's about, not
                                which UI container it lives in. Collections
                                (below) query against these; a block never
                                declares which Directory/Category it's "in"
  summary           string     one line, used in lists and search results
  difficulty        enum       "beginner" | "intermediate" | "advanced" —
                                EDITORIAL DEFAULT ONLY. Not derived, not
                                personalized, not authoritative in v1. A
                                later version may compute an actual value
                                per reader from prerequisite depth,
                                dependency count, or feedback signals — this
                                field is a placeholder opinion, not a fact.
  prerequisites     [blockId]  concepts a reader benefits from knowing first.
                                A RELATIONSHIP, NOT A GATE — the block is
                                always accessible regardless of whether
                                prerequisites are met. Learning Mode may
                                recommend them, Certification Mode may
                                require them, search ignores them entirely.
                                Same data, different behavior per product
                                surface — none of that logic lives here.
  relatedBlocks     [blockId]  see-also graph, symmetric, cross-domain allowed
  sourceOfTruth     object     see below — structured, not free text
  reviewStatus      enum       "current" | "needs-review" | "deprecated"
  lastReviewed      date
  content           <shape>    the typed payload, matches blockType

sourceOfTruth
  title             string     name of the authoritative spec/doc
  publisher         string     e.g. "Cisco", "HL7 International"
  version           string?    optional — spec/doc version if versioned
  url               string
  reviewedBy        string     stable identity of the human/role who
                                confirmed this citation — added post-Cisco,
                                after six blocks were found marked `current`
                                on a placeholder url with no reviewer of
                                record. Required, alongside url and
                                dateReviewed, before reviewStatus can be
                                "current" — enforced as a gate, ideally a DB
                                CHECK constraint, not just app-code convention.
  dateReviewed      date       when this citation was last confirmed current

InvokableContent                 -- content shape: commands, functions, queries,
                                     RESTful operations — anything you *invoke*
  syntax            string     e.g. "Router# show ip interface brief" or
                                "GET [base]/Patient/{id}"
  parameters        [{name, description, required}]
  sampleOutput      string     realistic example output/response, monospace
  fieldNotes        string     the "use this when..." callout — practical
                                context a syntax reference alone doesn't give

StructuralContent                -- second content shape, added when HL7/FHIR
                                     proved InvokableContent didn't fit: message
                                     formats, segment definitions, resource
                                     models — anything that's a named, ordered
                                     set of fields with a type and cardinality,
                                     not something you run
  elements          [{name, position, dataType, cardinality, description}]
                                position uses the domain's own notation
                                (e.g. "PID-3", "Patient.identifier") rather
                                than an invented numbering scheme
  exampleInstance   string     a realistic populated example — a real
                                segment line, or a resource JSON snippet
  fieldNotes        string     same practical "use this when..." callout as
                                InvokableContent — kept identical across
                                shapes on purpose, so the two only differ
                                where the content actually differs
```

**Why this is a second shape and not a reshaped `InvokableContent`:** a
segment or resource definition doesn't have a "sample output" — it has an
example of itself, populated. It doesn't take "parameters" — it has fields,
each with its own type and how many times it can repeat. Renaming the same
four fields would hide that these are different kinds of knowledge, which
defeats the reason the envelope/content split exists in the first place.
`InvokableContent` still fits FHIR's RESTful interactions (capability 7) —
verb, URL, example response, field notes is genuinely the same shape as a
Cisco command. It doesn't fit the segments or the resources themselves.

**Note — iteration, not evolution (observed, 2026-07-27):** worth recording
plainly, since it's evidence about the model rather than just a content
update. Adding `StructuralContent` touched nothing foundational — the
envelope (`KnowledgeBlock`) is unchanged, `blockType: "structural"` was
already a reserved enum value from v1, and `Collection`,
`prerequisites`/`relatedBlocks`, and `reviewStatus` all still work exactly
as designed. The schema anticipated this exact situation on purpose — "a
ceiling, not a starting inventory" — and when a real domain needed it, the
new shape slotted in without a redesign. That's the second time this has
held (Kid Translate's `Entity` shape was the first): a new content shape
appearing without the envelope moving. Recorded as evidence the foundation
generalizes, found the way it was designed to be found — because a real
domain needed it, not anticipated as a hypothetical. Not asserted as a
permanent guarantee; if a future domain needs a new relationship type, or
breaks `Collection`'s AND-only tag query, or needs an envelope field that
doesn't exist, that would be the actual evolve — and this note is exactly
the kind of claim that should get revised the day that happens, not
defended past its evidence.

SpecificationContent             -- third content shape, added for ACL TOP 350:
                                     manufacturer capability/configuration
                                     facts (a spec sheet) — a labeled value
                                     with an optional note, not something you
                                     invoke and not a named/typed/cardinality
                                     field of a message or resource instance
  specifications    [{label, value, note}]
                                label + value taken directly from the source
                                (e.g. "Samples onboard" / "40 (10/sample
                                rack)"), note only when context is needed
                                beyond the label itself
  fieldNotes        string     same practical callout as the other two
                                shapes — kept identical on purpose
```

**Why this is a third shape and not a reshaped `StructuralContent`:** a
capability fact like "continuous operation: YES" isn't a field inside a
message or resource instance — it has no `position`, no `dataType`, no
`cardinality`, because it isn't part of a data structure at all. It's an
attribute of the device itself, asserted once by the manufacturer.
Forcing it into `StructuralContent`'s element shape would mean inventing
a fake position and a fake type for every row, which is exactly the kind
of shape-mismatch this project has already caught twice before doing it.

**Honesty note, unlike the `StructuralContent` addition:** that shape's
`blockType: "structural"` value was already reserved in the v1 enum before
HL7 needed it. `"specification"` is not — this is a genuine, if small,
extension to the `blockType` discriminator enum, not a value that was
sitting pre-anticipated. Worth being precise about that distinction rather
than reusing the "touched nothing foundational" framing verbatim when it
isn't quite as true this time.

```
blockType         enum    "invokable" | "structural" | "procedural" |
                            "conceptual" | "entity" | "specification"
```

Proposed by CTO, used for the first ACL TOP 350 blocks below — pending the
same Steward review any new shape gets, not yet ratified as settled.

**Known open question, named now rather than found mid-production:**
`specifications` is a list, but the block still carries one `sourceOfTruth`
object. A manufacturer spec sheet bundling several facts under one
citation is fine — one source covers the whole row set. It's easy to
imagine a block where that breaks: one row sourced from a datasheet (M1)
sitting next to a row that's expert-observed (E1), no manufacturer
document behind it at all. That's the same tension as backporting the
M1–U1 source hierarchy generally (noted above under "source hierarchy —
reusable as a discipline, not as a schema field" in
`LAB_EQUIPMENT_DOMAIN_TEMPLATE.md"), just surfacing concretely here first.
Not solved in v1 — matches "ceiling, not inventory": stays single-sourced
per block until an actual domain produces a block that needs mixed-class
rows, at which point this is the first place that pressure will show up.

---

`sourceOfTruth` moved from free text to a structured object this round —
even with only `title` and `url` populated at first, structure compounds in
a way free text doesn't: it's what makes future staleness-checking
automatable instead of requiring a full migration later to parse it back out.

---

## 2. Collection — Directory and Category Are the Same Object

Earlier drafts treated Directory and Category as either a hardcoded tree or
pure tag queries. Neither is quite right. A Directory needs things a tag
can't express — a title, a description, an icon, an ordering, featured
blocks, onboarding text — and those are product concerns, not facts about
the knowledge itself. But membership still has to be query-driven, or we're
back to the duplication bug from the first prototype (`show ip route`
hardcoded as two separate copies under SHOW and ROUTE).

The resolution: one object, `Collection`, used at two levels.

```
Collection
  id                string
  title             string     e.g. "SHOW", "Interfaces"
  description        string
  icon              string?
  color             string?
  ordering          number     display order among siblings
  domain            string     which domain this collection belongs to
  parentCollectionId string?   absent = Directory (root level)
                                present = Category (nested under a Directory)
  query             object     { tags: [string], blockType?: string }
                                AND-only for v1 — a block matches if it
                                carries every listed tag. No boolean
                                expressiveness beyond that yet; add it if a
                                domain proves flat AND isn't enough, not
                                before.
  featuredBlocks    [blockId]? optional manual override — pin specific
                                blocks above the query-derived order
  onboardingText    string?
  learningGoals     [string]?
```

`parentCollectionId` technically supports unlimited nesting depth, but only
two levels are actually used right now — Directory (no parent) and Category
(has a parent). Same discipline as the content shapes: the capability exists
in the schema so a third level isn't a migration if a domain needs it, but
nothing is built for it until one does.

A block never declares its own category membership. It carries `tags`;
`Collection.query` decides which blocks match. This is what makes cross-
listing free instead of duplicative — see the `show ip route` example below.

---

## 2b. Capability — a first-class object, with a lifecycle

Until now `Capability` was a planning-level node in the Research→Steward loop
(see `CAPABILITY_MAP_PROCESS.md`), not a stored object — `KnowledgeBlock` and
`Collection` were the only real types here. The Director of Analytics role
changes that: Analytics can't measure "time waiting on OEM authorization" or
"% of capabilities at `operational`" unless a capability is a thing that
exists, carries a state, and can be counted. So `Capability` becomes a stored
object.

**Honesty note — this is bigger than the last three additions, and shouldn't
borrow their reassurance.** `StructuralContent`, `SpecificationContent`, and
Kid Translate's `Entity` were all *content shapes* — new payloads hanging off
the unchanged `KnowledgeBlock` envelope, which is why "a new shape slotted in
without the envelope moving" held each time. `Capability` is **not** a content
shape; it is a **third top-level object**, a sibling of `KnowledgeBlock` and
`Collection`. The iteration-not-evolution evidence recorded above does not
cover this case — this is the first genuinely new top-level object since the
envelope/content split, and it earns the heavier scrutiny that implies, not
the "touched nothing foundational" framing. Flagged to Steward on exactly
those terms.

```
Capability
  id                string      unique, stable
  title             string
  domain            string
  purpose           string
  function          string
  relationships     [capabilityId]
  inputs            [string]
  outputs           [string]
  risks             [string]
  safety            string?
  requiredSkills    [string]
  dependencies      [capabilityId]
  evidence          [blockId]   Knowledge Blocks that back this capability
  oemReference      object      { locked: bool, source: sourceOfTruth?, note: string }
                                 locked stays true until a real licensed/OEM
                                 source is in hand — see the Authority Boundary
                                 section of CAPABILITY_MAP_PROCESS.md
  capabilityState   enum        "draft" | "structured" | "validated" |
                                 "authorized" | "operational"
```

**State composition — the mapping, stated explicitly** (per the Analytics
requirement that `operational` be *computed*, not eyeballed). `capabilityState`
is a capability-level axis. `reviewStatus` (on `KnowledgeBlock`) and the
provisional/published pipeline are separate, block-level axes. They compose;
they do not stack:

- A capability may be `structured` while its Blocks are still `needs-review`
  or provisional — expected, not a defect.
- A capability reaches `authorized` when `oemReference.locked` flips to
  `false` (a real source is in hand, or none is needed), independent of
  whether any Block has been promoted.
- A capability reaches `operational` only once it is `authorized` **and** the
  Blocks carrying its locked/OEM-specific content have themselves reached
  `reviewStatus: "current"` under the existing gate (`reviewedBy` +
  `dateReviewed` + a real `url`). `operational` is downstream of both axes —
  it is **computed, never hand-set**. (Same rule stated from the process side
  in `CAPABILITY_MAP_PROCESS.md` § Capability States; restated here because
  the schema is where a consumer reads it.)

**Open question, named now rather than found mid-production:** `capabilityState`
is written per-capability, but the retrofit below assigns it per-*domain* — a
whole domain rolled up to one state. That's a defensible v1 simplification (a
domain is only as `operational` as its weakest OEM-locked capability), but it's
a real granularity decision for Steward: per-capability with a computed domain
rollup, or per-domain until capabilities are enumerated individually? Left
per-domain for the retrofit; flagged, not silently resolved.

### Retrofit — the five existing domains, states assigned against live evidence

Not guessed. Each state was checked against the live repo, not the founding
memo's assertion — `reviewStatus` counts read from the tracked JSON, domain
posture read from `PROJECT_STATUS.md`. `oemReference.source` omitted where
locked or absent.

```json
[
  {
    "id": "cap.cisco-ios",
    "title": "Cisco IOS operational command reference",
    "domain": "cisco-ios",
    "capabilityState": "operational",
    "oemReference": { "locked": false, "note": "Public command references; no OEM-licensed source gates this domain." },
    "evidenceNote": "76/77 Blocks reviewStatus:current with real http url + reviewedBy (verified in cisco-ios-knowledge-blocks.json). The one non-current, show-users, is a documented negative — absent from the sourced chapter — not a pending review."
  },
  {
    "id": "cap.hl7-fhir",
    "title": "HL7 v2 / FHIR interface structures",
    "domain": "hl7-fhir",
    "capabilityState": "operational",
    "oemReference": { "locked": false, "note": "Public standards (HL7 v2.5.1, FHIR R4); no OEM lock." },
    "evidenceNote": "15/15 Blocks reviewStatus:current with real url + reviewedBy (verified in hl7-knowledge-blocks.json)."
  },
  {
    "id": "cap.acl-top-350",
    "title": "ACL TOP 350 CTS serviceable system",
    "domain": "acl-top-350",
    "capabilityState": "structured",
    "oemReference": { "locked": false, "note": "Manufacturer spec-sheet data; IP posture pending legal review (PROJECT_STATUS), which is a copyright question, not an OEM-document access lock." },
    "evidenceNote": "9/9 Blocks needs-review (verified). Blocked at validated — nothing Steward-promoted yet."
  },
  {
    "id": "cap.ge-oec-one-cfd",
    "title": "GE OEC One CFD serviceable system",
    "domain": "ge-oec-one-cfd",
    "capabilityState": "structured",
    "oemReference": { "locked": true, "note": "Service manual SM-7888001-1EN-17 and DICOM conformance DOC2198430 sit behind a GE account nobody on the team holds." },
    "evidenceNote": "12/12 capabilities cleared Phase 4, but explicitly NOT validated: repo carries only 1 draft-only Block (needs-review), three uncoordinated Phase 6 attempts still unreconciled (PROJECT_STATUS, README_NOT_CANONICAL). Held at structured deliberately — do not advance past where PROJECT_STATUS says this domain actually is."
  },
  {
    "id": "cap.iicrc-s500",
    "title": "IICRC S500 water-restoration serviceable methods",
    "domain": "iicrc-s500",
    "capabilityState": "structured",
    "oemReference": { "locked": true, "note": "Real, edition-confirmed IICRC S500 standard not yet obtained — the canonical locked case the state model was built to describe." },
    "evidenceNote": "Facts-and-methods build authorized under IP constraint; postdates the 2026-07-28 PROJECT_STATUS snapshot, so grounded in the S500 crew charters. Stays locked until the edition-confirmed standard is in hand."
  }
]
```

**Status.** `Capability` object proposed by CTO; retrofit states assigned by
Code against live evidence. **Steward-reviewed 2026-07-30** (see
`capability-object-steward-review.md`) — composite outcome: *Approve with
Constraints* on the field set (C1–C3 attached), **Hold** on `operational`
semantics (two precise unresolved requirements: it is typed as a stored value
but defined as computed, and its OEM-specific evidence subset is
unidentifiable), *Return for Editing* on the retrofit (the five entries are
domain rollups mislabeled as capabilities). Self-review firewall flagged in the
review: **not** final certification — pending an independent Steward or Architect
ratification. Deliberately **not** yet built into the app: no `capabilities`
table, no
migration, no seed. That's the downstream step, gated on this review, exactly
as the founding memo required ("don't build against it mid-domain without that
pass").

---

## 3. Worked Examples — Cisco IOS

### Collections

```json
{
  "id": "cisco-ios.show",
  "title": "SHOW",
  "description": "IOS verification and monitoring commands.",
  "icon": "ti-terminal-2",
  "ordering": 1,
  "domain": "cisco-ios",
  "parentCollectionId": null,
  "query": { "tags": ["show"] },
  "featuredBlocks": ["cisco-ios.show-ip-interface-brief"]
}
```

```json
{
  "id": "cisco-ios.show.interfaces",
  "title": "INTERFACES",
  "description": "Interface status and configuration visibility.",
  "ordering": 1,
  "domain": "cisco-ios",
  "parentCollectionId": "cisco-ios.show",
  "query": { "tags": ["show", "interfaces"] }
}
```

### Knowledge Blocks

Six real blocks, chosen to exercise the parts of the model that matter most:
a duplicate-membership case, a prerequisites chain, and a cross-category
`relatedBlocks` graph.

```json
{
  "id": "cisco-ios.show-ip-interface-brief",
  "title": "show ip interface brief",
  "aliases": ["sh ip int br", "show ip int brief"],
  "domain": "cisco-ios",
  "blockType": "invokable",
  "tags": ["show", "interfaces", "troubleshooting", "layer3"],
  "summary": "Quick status summary of all IP interfaces on a device.",
  "difficulty": "beginner",
  "prerequisites": [],
  "relatedBlocks": ["cisco-ios.show-interfaces", "cisco-ios.show-controllers"],
  "sourceOfTruth": {
    "title": "Cisco IOS Interface and Hardware Command Reference",
    "publisher": "Cisco",
    "version": null,
    "url": "[TBD]",
    "dateReviewed": "2026-07-26"
  },
  "reviewStatus": "current",
  "lastReviewed": "2026-07-26",
  "content": {
    "syntax": "Router# show ip interface brief",
    "parameters": [],
    "sampleOutput": "Interface            IP-Address   OK? Method Status  Protocol\nGigabitEthernet0/1   10.10.10.1   YES manual up      up\nGigabitEthernet0/2   unassigned   YES NVRAM  down    down",
    "fieldNotes": "Use during outage triage to quickly verify which interfaces are up/down and have valid IPs before diving into deeper diagnostics."
  }
}
```

```json
{
  "id": "cisco-ios.show-ip-route",
  "title": "show ip route",
  "aliases": ["sh ip route"],
  "domain": "cisco-ios",
  "blockType": "invokable",
  "tags": ["show", "routing", "troubleshooting", "layer3"],
  "summary": "Displays the current IP routing table.",
  "difficulty": "beginner",
  "prerequisites": [],
  "relatedBlocks": ["cisco-ios.router-ospf", "cisco-ios.ip-route-static"],
  "sourceOfTruth": {
    "title": "Cisco IOS IP Routing Command Reference",
    "publisher": "Cisco",
    "version": null,
    "url": "[TBD]",
    "dateReviewed": "2026-07-26"
  },
  "reviewStatus": "current",
  "lastReviewed": "2026-07-26",
  "content": {
    "syntax": "Router# show ip route",
    "parameters": [
      {"name": "[ip-address]", "description": "Show the route for a specific destination only", "required": false}
    ],
    "sampleOutput": "Gateway of last resort is 192.168.1.1 to network 0.0.0.0\nO    10.0.0.0/8 [110/2] via 192.168.1.2, GigabitEthernet0/1\nC    192.168.1.0/24 is directly connected, GigabitEthernet0/1",
    "fieldNotes": "The letter prefix (O, C, S, R) tells you how the route was learned — OSPF, connected, static, or RIP. Start here whenever traffic isn't reaching a destination it should."
  }
}
```

*(Duplicate-membership proof: this block carries both `"show"` and
`"routing"` tags. It matches the `cisco-ios.show` Collection's query and
would also match a `cisco-ios.route` Collection's query — one block, two
Collections, zero duplication.)*

```json
{
  "id": "cisco-ios.configure-terminal",
  "title": "configure terminal",
  "aliases": ["conf t"],
  "domain": "cisco-ios",
  "blockType": "invokable",
  "tags": ["config", "global-configuration"],
  "summary": "Enters global configuration mode.",
  "difficulty": "beginner",
  "prerequisites": [],
  "relatedBlocks": ["cisco-ios.hostname", "cisco-ios.copy-running-config-startup-config"],
  "sourceOfTruth": {
    "title": "Cisco IOS Fundamentals Command Reference",
    "publisher": "Cisco",
    "version": null,
    "url": "[TBD]",
    "dateReviewed": "2026-07-26"
  },
  "reviewStatus": "current",
  "lastReviewed": "2026-07-26",
  "content": {
    "syntax": "Router# configure terminal",
    "parameters": [],
    "sampleOutput": "Router(config)#",
    "fieldNotes": "The prompt change to Router(config)# is the confirmation you're in the right mode. Almost every configuration block in this library assumes you're starting from here."
  }
}
```

```json
{
  "id": "cisco-ios.router-ospf",
  "title": "router ospf",
  "aliases": ["router ospf process-id"],
  "domain": "cisco-ios",
  "blockType": "invokable",
  "tags": ["route", "ospf", "config"],
  "summary": "Enables OSPF routing and enters router configuration mode for it.",
  "difficulty": "intermediate",
  "prerequisites": ["cisco-ios.configure-terminal"],
  "relatedBlocks": ["cisco-ios.show-ip-route", "cisco-ios.show-ip-protocols"],
  "sourceOfTruth": {
    "title": "Cisco IOS IP Routing: OSPF Command Reference",
    "publisher": "Cisco",
    "version": null,
    "url": "[TBD]",
    "dateReviewed": "2026-07-26"
  },
  "reviewStatus": "current",
  "lastReviewed": "2026-07-26",
  "content": {
    "syntax": "Router(config)# router ospf <process-id> [vrf vrf-name]",
    "parameters": [
      {"name": "process-id", "description": "Locally significant identifier, any positive integer — doesn't need to match between routers", "required": true}
    ],
    "sampleOutput": "Router(config)# router ospf 1\nRouter(config-router)#",
    "fieldNotes": "The process-id is local only — it's a common misconception that it needs to match across the network. What has to match is the area number on the network statements that follow."
  }
}
```

**Correction note (added 2026-07-28, after Code confirmed this block against the
real command reference page via direct DOM extraction):** this worked
example previously stated the process-id range as "1-65535" — a value
that had never actually been confirmed against source, only carried
forward from assumed/recalled knowledge when this worked example was
first written. The real source states "any positive integer," with no
stated upper bound, and adds an optional `vrf vrf-name` keyword this
example didn't have. Fixed here to match what's actually live in the
repo (`main` at `21519eb`), same discipline as the earlier PID-7/PID-8
correction — a worked example is only as good as its weakest unverified
claim, including ones that originated in this document rather than
downstream of it.

```json
{
  "id": "cisco-ios.vlan",
  "title": "vlan",
  "aliases": ["vlan vlan-id"],
  "domain": "cisco-ios",
  "blockType": "invokable",
  "tags": ["switch", "vlan-configuration", "config"],
  "summary": "Creates a VLAN and enters VLAN configuration mode.",
  "difficulty": "beginner",
  "prerequisites": ["cisco-ios.configure-terminal"],
  "relatedBlocks": ["cisco-ios.switchport-access-vlan", "cisco-ios.show-vlan-brief"],
  "sourceOfTruth": {
    "title": "Cisco IOS LAN Switching Command Reference",
    "publisher": "Cisco",
    "version": null,
    "url": "[TBD]",
    "dateReviewed": "2026-07-26"
  },
  "reviewStatus": "current",
  "lastReviewed": "2026-07-26",
  "content": {
    "syntax": "Router(config)# vlan <vlan-id>",
    "parameters": [
      {"name": "vlan-id", "description": "Numeric identifier, 1-4094", "required": true}
    ],
    "sampleOutput": "Router(config)# vlan 10\nRouter(config-vlan)#",
    "fieldNotes": "Creating the VLAN here doesn't assign it to any port — that's a separate step on the interface itself."
  }
}
```

```json
{
  "id": "cisco-ios.show-logging",
  "title": "show logging",
  "aliases": ["sh log"],
  "domain": "cisco-ios",
  "blockType": "invokable",
  "tags": ["troubleshooting", "logging"],
  "summary": "Displays the contents of the logging buffer and current logging configuration.",
  "difficulty": "beginner",
  "prerequisites": [],
  "relatedBlocks": ["cisco-ios.show-ip-interface-brief"],
  "sourceOfTruth": {
    "title": "Cisco IOS Network Management Command Reference",
    "publisher": "Cisco",
    "version": null,
    "url": "[TBD]",
    "dateReviewed": "2026-07-26"
  },
  "reviewStatus": "current",
  "lastReviewed": "2026-07-26",
  "content": {
    "syntax": "Router# show logging",
    "parameters": [],
    "sampleOutput": "Syslog logging: enabled\n*Jul 26 14:02:11: %LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to down",
    "fieldNotes": "This is usually the first command to run when something changed and nobody knows why — the timestamped events often show the root cause directly."
  }
}
```

---

**Correction note (added after Code caught this section presenting
regressed values):** this section previously showed PID-7 as `DTM`, PID-8
as `CWE`, and both FHIR examples pointing at a `fhir.restful-interactions-overview`
prerequisite — all three already found wrong, fixed, and pushed to `main`
at `d423102` earlier in this project (`TS`/`IS` per the version-pinned
v2.5.1 text; prerequisite repointed to `fhir.capabilitystatement-discovery`).
This document had drifted back to the pre-correction draft — corrected
here to match what's actually live in the repo, not re-derived from
memory. If this ships as an ADR, it ships with these values, not the ones
that were briefly back in this file.

## 3b. Worked Examples — HL7 v2 / FHIR (Phase 6, first pass)

Three blocks, chosen to prove the shape split works, not to represent full
coverage: one `StructuralContent` block from v2, one `StructuralContent`
block from FHIR, and one `InvokableContent` block from FHIR's RESTful
layer — showing both shapes coexisting inside a single domain family, and
a cross-shape `relatedBlocks` link between them. `reviewStatus` is
`needs-review` on all three — concept-level validation happened in the
Research/Steward loop, but block-level `sourceOfTruth.reviewedBy` hasn't
been set by anyone with promotion authority yet, so none of these are
`current`. That gate applies here exactly as it did after the Cisco
placeholder-url incident — no exception for being the second domain.

```json
{
  "id": "hl7v2.pid-segment",
  "title": "PID — Patient Identification Segment",
  "aliases": ["PID"],
  "domain": "hl7-v2",
  "blockType": "structural",
  "tags": ["hl7v2", "adt", "segment", "patient-identity"],
  "summary": "Carries patient demographic identity — the segment every ADT, Order, and Result message references back to.",
  "difficulty": "beginner",
  "prerequisites": ["hl7v2.msh-segment"],
  "relatedBlocks": ["hl7v2.pv1-segment", "hl7v2.evn-segment", "fhir.patient-resource"],
  "sourceOfTruth": {
    "title": "HL7 Version 2.5.1 Standard, Chapter 5 — Patient Administration",
    "publisher": "HL7 International",
    "version": "2.5.1",
    "url": "https://www.vico.org/HL7_V2_5/v251/std251/ch05.html",
    "reviewedBy": null,
    "dateReviewed": null
  },
  "reviewStatus": "needs-review",
  "lastReviewed": "2026-07-27",
  "content": {
    "elements": [
      {"name": "Patient Identifier List", "position": "PID-3", "dataType": "CX", "cardinality": "1..*", "description": "One or more identifiers (e.g. MRN) for the patient — required, repeating."},
      {"name": "Patient Name", "position": "PID-5", "dataType": "XPN", "cardinality": "1..*", "description": "Legal name and any aliases — required, repeating."},
      {"name": "Date/Time of Birth", "position": "PID-7", "dataType": "TS", "cardinality": "0..1", "description": "Optional, non-repeating. Confirmed TS (not DTM) against the version-pinned v2.5.1 text — DTM comes from a harmonized/no-version documentation family, see the sourcing correction in HL7_PHASE4_CONCEPT_DECOMPOSITION.md."},
      {"name": "Administrative Sex", "position": "PID-8", "dataType": "IS", "cardinality": "0..1", "description": "Optional, non-repeating, coded value. Confirmed IS (not CWE) against the same version-pinned text — same trip-wire as PID-7."}
    ],
    "exampleInstance": "PID|1||446-53||SURNAME^GIVEN||19800101|M",
    "fieldNotes": "PID-3 and PID-5 are the two fields every downstream system actually depends on — everything else on this segment is context, not identity. Missing or malformed PID-3 is the single most common cause of a failed patient match downstream."
  }
}
```

```json
{
  "id": "fhir.patient-resource",
  "title": "Patient",
  "aliases": ["FHIR Patient"],
  "domain": "hl7-fhir",
  "blockType": "structural",
  "tags": ["fhir", "resource", "patient-identity"],
  "summary": "The person receiving care — a standalone, referenceable resource, not a segment embedded in a message.",
  "difficulty": "beginner",
  "prerequisites": ["fhir.capabilitystatement-discovery"],
  "relatedBlocks": ["fhir.encounter-resource", "fhir.observation-resource", "hl7v2.pid-segment"],
  "sourceOfTruth": {
    "title": "HL7 FHIR Patient Resource, Release 4",
    "publisher": "HL7 International",
    "version": "R4",
    "url": "https://hl7.org/fhir/R4/patient.html",
    "reviewedBy": null,
    "dateReviewed": null
  },
  "reviewStatus": "needs-review",
  "lastReviewed": "2026-07-27",
  "content": {
    "elements": [
      {"name": "identifier", "position": "Patient.identifier", "dataType": "Identifier", "cardinality": "0..*", "description": "Business identifiers (MRN, SSN, etc.) — the FHIR analogue of PID-3, generalized to any identifier scheme."},
      {"name": "name", "position": "Patient.name", "dataType": "HumanName", "cardinality": "0..*", "description": "Repeating — supports multiple names/aliases."},
      {"name": "birthDate", "position": "Patient.birthDate", "dataType": "date", "cardinality": "0..1"},
      {"name": "gender", "position": "Patient.gender", "dataType": "code", "cardinality": "0..1", "description": "Bound to a required-strength ValueSet — administrative gender, not clinical sex."}
    ],
    "exampleInstance": "{ \"resourceType\": \"Patient\", \"identifier\": [{\"value\": \"446-53\"}], \"name\": [{\"family\": \"Surname\", \"given\": [\"Given\"]}], \"birthDate\": \"1980-01-01\", \"gender\": \"male\" }",
    "fieldNotes": "Same identity function as v2's PID, but as its own addressable resource other resources reference by URL rather than a segment that only exists inside one message. `gender` here is administrative, not a clinical/biological claim — a common point of confusion worth calling out explicitly."
  }
}
```

```json
{
  "id": "fhir.read-patient-instance",
  "title": "GET [base]/Patient/{id}",
  "aliases": ["read Patient", "FHIR Patient read"],
  "domain": "hl7-fhir",
  "blockType": "invokable",
  "tags": ["fhir", "restful-interaction", "read"],
  "summary": "Retrieves a single Patient resource instance by its logical id.",
  "difficulty": "beginner",
  "prerequisites": ["fhir.capabilitystatement-discovery"],
  "relatedBlocks": ["fhir.patient-resource"],
  "sourceOfTruth": {
    "title": "RESTful API — FHIR Release 4",
    "publisher": "HL7 International",
    "version": "R4",
    "url": "https://www.hl7.org/fhir/http.html",
    "reviewedBy": null,
    "dateReviewed": null
  },
  "reviewStatus": "needs-review",
  "lastReviewed": "2026-07-27",
  "content": {
    "syntax": "GET [base]/Patient/{id}",
    "parameters": [
      {"name": "id", "description": "The resource's logical id, assigned by the server on create", "required": true}
    ],
    "sampleOutput": "HTTP/1.1 200 OK\nContent-Type: application/fhir+json\n\n{ \"resourceType\": \"Patient\", \"id\": \"123\", \"name\": [...] }",
    "fieldNotes": "This is the same shape as a Cisco `show` command — a request and a real response — which is why this specific corner of FHIR stayed InvokableContent instead of needing the Structural shape the resources themselves required."
  }
}
```

Cross-shape proof: `hl7v2.pid-segment` and `fhir.patient-resource` are
linked via `relatedBlocks` despite being different `blockType`s in
different domains — exactly the cross-domain, cross-shape flexibility the
model was designed to allow without a schema change.

---

## 4. Round 1 Review Log

| # | Question | Resolution | Owner |
|---|---|---|---|
| 1 | Prerequisites: hard gate or soft suggestion? | Soft relationship in the data model. Gating is a product-mode decision (Learning Mode, Certification Mode), never schema-enforced. | Ledger |
| 2 | Category/Directory: tags or records? | Neither alone — `Collection`, curated metadata over a query. Directory and Category are the same object at different nesting depth. | Ledger (concept) / Claude (schema) |
| 3 | `sourceOfTruth` format | Structured object (title, publisher, version, url, dateReviewed) from v1, not free text. | Ledger |
| 4 | Difficulty calibration | Kept as a field, explicitly editorial-only — not derived, not personalized, not authoritative until a future signal-based version. | Ledger |

No open product-level questions remain from this round. One implementation
decision made without a review question, since it's execution rather than
model: `Collection.query` is AND-only over tags for v1 — no boolean
expressiveness until a domain proves it's needed.

Ready for Travis's ratification. Once ratified, this becomes ADR material —
`docs/decisions/0001-knowledge-block-model.md` — rather than a living draft.

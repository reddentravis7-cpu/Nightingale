# Knowledge Block Model — v1

**Status:** Adopted for Translate, proven across two domains (Cisco IOS, HL7 v2/FHIR).
**Standing principle:** the schema describes reality; the application decides how to use it. Prerequisites, difficulty, and category membership all live in the data as neutral facts or editorial hints — whether something blocks access, requires completion, or gets emphasized is a product-mode decision made above the schema, not encoded in it.

## 1. The Model

Two parts, envelope and typed content:

- **`KnowledgeBlock`** — the envelope. Identity, cross-referencing, lifecycle, metadata. Identical fields regardless of domain or content shape.
- **Typed content** — a payload shaped by *what kind of knowledge this is*, not by which domain it came from. Two shapes exist: `InvokableContent` (commands, functions, RESTful operations — anything you invoke) and `StructuralContent` (message formats, segment definitions, resource models — a named, ordered set of fields with a type and cardinality, not something you run). Three more blockType values (`procedural`, `conceptual`, `entity`) are reserved but unbuilt — a ceiling, not a starting inventory.

```
KnowledgeBlock
  id                string     unique, stable, never reused even if deprecated
  title             string     canonical name
  aliases           [string]   alternate search terms, abbreviations
  domain            string     e.g. "hl7-v2", "hl7-fhir", "cisco-ios"
  blockType         enum       "invokable" | "structural" | "procedural" | "conceptual" | "entity"
  tags              [string]   facts about the block — what it's about, not which UI container it lives in
  summary           string     one line, used in lists and search results
  difficulty        enum       "beginner" | "intermediate" | "advanced" — editorial default only, not derived or authoritative
  prerequisites     [blockId]  a relationship, not a gate — always accessible regardless of whether met
  relatedBlocks     [blockId]  see-also graph, symmetric, cross-domain allowed
  sourceOfTruth     object     see below — structured, not free text
  reviewStatus      enum       "current" | "needs-review" | "deprecated"
  lastReviewed      date
  content           <shape>    the typed payload, matches blockType

sourceOfTruth
  title             string     name of the authoritative spec/doc
  publisher         string     e.g. "HL7 International"
  version           string?    optional — spec/doc version if versioned
  url               string
  reviewedBy        string     stable identity of the human/role who confirmed this citation.
                                Required, alongside url and dateReviewed, before reviewStatus can be
                                "current" — enforced as a gate, not just app-code convention.
  dateReviewed      date       when this citation was last confirmed current

InvokableContent
  syntax            string     e.g. "GET [base]/Patient/{id}"
  parameters        [{name, description, required}]
  sampleOutput      string     realistic example output/response, monospace
  fieldNotes        string     the "use this when..." callout

StructuralContent
  elements          [{name, position, dataType, cardinality, description}]
                                position uses the domain's own notation (e.g. "PID-3", "Patient.identifier")
  exampleInstance   string     a realistic populated example — a real segment line, or a resource JSON snippet
  fieldNotes        string     same practical callout as InvokableContent, kept identical across shapes on purpose
```

## 2. Collection — Directory and Category Are the Same Object

One object, `Collection`, used at two levels via `parentCollectionId` (absent = Directory/root, present = Category/nested). Membership is query-driven over `tags`, never hardcoded — a block never declares its own category membership.

```
Collection
  id                 string
  title              string
  description        string
  icon               string?
  color              string?
  ordering           number
  domain             string
  parentCollectionId string?
  query              object   { tags: [string], blockType?: string } — AND-only for v1
  featuredBlocks     [blockId]?
  onboardingText     string?
  learningGoals      [string]?
```

## 3. Provenance

This document reconstructs the schema as agreed during the Translate Knowledge Block Model design review (Round 1, Ledger/CTO/Founder), for the HL7 v2 / FHIR domain buildout. See `HL7_PHASE4_CONCEPT_DECOMPOSITION.md` for the capability-level dependency graph this domain's blocks are derived from, and the block-review history at the bottom of `hl7-knowledge-blocks.json`-adjacent documentation for the Steward review trail (sourcing corrections, the CE/CWE and TS/DTM harmonized-vs-version-pinned trip-wire, and per-field confidence notes).

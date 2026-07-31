# Translate — Knowledge Roles Reference (Index)

**Rev 3 — 2026-07-30.** Converted from a verbatim bundle into an **index**. Earlier revisions stitched the full text of each role document into this one file; that embedded copy drifted from the standalone charters (it still carried a pre-renumber Steward snapshot). This reference now **points to** the canonical standalone documents instead of duplicating them — one authoritative copy per document, no drift.

**Canonical location:** the governance repo, `04_Translate/docs/architecture/` (base documents) and `04_Translate/docs/roles/` (role charters). `~/Downloads` holds the working/staging copies.

---

## The base every role sits on

| Document | ID | What it is |
|---|---|---|
| Translate Scope Constitution | `TRANSLATE-CONST` (v2.0 draft) | The foundational document. Its first half is the injury/harm scope boundary (what content may exist); as of v2.0 the common obligations are extracted to CCO. |
| Common Constitutional Obligations | `CCO v1.0` (draft) | The eight obligations every governance role implements. Roles cite the CCO version they implement and hold only their delta. |
| Discipline Crew Model | v1.0 | How the per-domain seats (Researcher · Steward · Field Engineer) fit together across the discover → validate → apply firewall. |

*Constitution and CCO ratify **atomically**; both are DRAFT pending Architect ratification, with TRANSLATE-CONST-v1.0 operative until then.*

---

## The role charters

Each charter implements CCO v1.0 and carries a `TRANSLATE-ROLE-*` Document ID. Reading order follows the pipeline: discover → validate → represent → record → apply → teach → communicate → measure.

| Role | Document ID | Scope | One line |
|---|---|---|---|
| **Researcher** | `TRANSLATE-ROLE-RESEARCH-v1.0` | per-domain | Evidence-gatherer; discovers what a discipline contains and drafts it for validation — stops at evidence. |
| **Research Specialist** | `TRANSLATE-ROLE-RSPEC-v1.0` | cross-cutting | Standing watcher; finds what has changed across all domains and routes it to the owning Steward. |
| **Steward** | `TRANSLATE-ROLE-STEWARD-v1.0` | per-domain | Guardian of truth; the harm-boundary gate — decides what is safe to exist and promotes `⚠ → ✅`. |
| **Editor in Chief** | `TRANSLATE-ROLE-EIC-v1.0` | platform-wide | Form, never substance; makes cleared content clear, consistent, usable — never changes what it means. |
| **Database Manager** | `TRANSLATE-ROLE-DBM-v1.0` | platform-wide | Custodian, never author; keeps the record durable, versioned, recoverable — discharges CCO Obligation 6 for everyone. |
| **Field Engineer (FSE)** | `TRANSLATE-ROLE-FSE-v1.0` | per-domain | Applier of truth + the FSE reader-persona; turns validated Blocks into safe, sourced, repeatable action and closes the field-report loop. |
| **Training Director** | `TRANSLATE-ROLE-TRAIN-v1.0` | platform-wide | Builder of competency; teaches only validated content, certifies only demonstrated competency. |
| **Marketing Director** | `TRANSLATE-ROLE-MKTG-v1.0` | platform-wide | Communicates value, never inflates it; no claim outruns the evidence. |
| **Director of Analytics** | `TRANSLATE-ROLE-ANALYTICS-v1.0` | platform-wide | Measures the system itself; velocity never reported without its paired rigor metric. |

*CTO is named in the CCO roster as a governance role but does not yet have a standalone charter.*

---

## How the pieces relate

- **Base → implementation:** the Constitution is the immutable foundation; CCO is the shared floor; each charter implements CCO and adds only its role-specific delta (the same relationship a Knowledge Block's typed content has to its shared envelope in `knowledge-block-model.md`).
- **The firewall:** Researcher / Research Specialist **discover**; Steward **validates** (one persona never both discovers and certifies); Field Engineer **applies** and reports reality back — a cycle, not a pipeline.
- **The standing platform roles** (Editor in Chief, Database Manager, Training Director, Marketing Director, Director of Analytics) are not per-domain seats; they span every discipline.

To read any role in full, open its charter file listed above. This index is deliberately thin so it never has to be kept in sync with the charters' contents — only their existence and identity.

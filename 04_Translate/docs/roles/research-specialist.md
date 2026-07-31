# Research Specialist Charter

**Version:** 1.0
**Status:** Ratified — **re-ratified onto CCO v1.0 (Architect, 2026-07-31).**
**Document ID:** TRANSLATE-ROLE-RSPEC-v1.0
**Implements:** Common Constitutional Obligations **CCO v1.0**
**Scope:** Cross-cutting (one watcher across all disciplines)
**Reports findings to:** Domain Stewards (e.g. Sheldon)
**Companion documents:** Steward Charter v1.0 · Researcher Charter v1.0 · Discipline Crew Model · Knowledge Maintenance Plan v1.0

---

> **Implements CCO v1.0.** The eight Common Constitutional Obligations (act in the Constitution's best interest, preserve evidence integrity, distinguish fact/inference/opinion, respect IP & licensing, document uncertainty, leave an auditable record, evidence-based optimization, collaborate within constitutional authority) are inherited from that base document and are authoritative for the shared floor. The principles and duties below are this role's domain-specific expression of, and additions to, that floor — not a re-declaration of it.

**Re-ratified onto CCO v1.0 — Architect, 2026-07-31.** Per CCO §6, how this charter discharges each of the eight obligations (referencing this role's own sections):

| # | Common Obligation | How the Research Specialist discharges it |
|---|---|---|
| 1 | Best interest of the Constitution | Expands and maintains the frontier before knowledge becomes organizational; decides what is worth a Steward's attention, not what is true (§2). |
| 2 | Preserve evidence integrity | Captures each finding with source, date, and confidence; never assumes (§6.3, §8). |
| 3 | Distinguish fact / inference / opinion | The Evidence Package keeps Finding, Interpretation, and Uncertainty in separate fields (§7). |
| 4 | Respect IP / licensing | Cites exact document, revision, and section; preserves the source context that makes a quote true (§6.3, §8). |
| 5 | Document uncertainty | Confidence is stated, not implied; low confidence is a finding, not a failure (§7, §8). |
| 6 | Auditable record | Evidence Packages and change logs are the recorded unit; provenance is preserved via the Database Manager (§7, §10). |
| 7 | Evidence-based optimization | Routes change-findings to the owning Steward for re-review — the standing engine of the Knowledge Maintenance Plan (§9). |
| 8 | Collaborate, respect authority | Routes, does not rule; assesses relevance and impact, never truth; hands each package to the owning Steward (§4, §5, §8). |

---

## 1. Identity

**Role:** Research Specialist

**One line:** The Explorer of truth — the standing watcher who finds what has changed before it becomes organizational knowledge.

The Research Specialist is a **single, cross-cutting role**. There is one across the whole knowledge system, not one per discipline. Where each discipline is staffed by its own Researcher, Steward, and (eventually) Field Engineer, the Research Specialist stands above the disciplines and watches the frontier of all of them.

---

## 2. Mission

Continuously discover, evaluate, and organize new knowledge across every discipline **before** it becomes organizational knowledge — then hand it, cleanly packaged, to the Steward who owns it.

The Research Specialist expands and maintains the frontier. They do not decide what is true. They decide what is **worth a Steward's attention**.

---

## 3. Primary Question

> **"What has changed, and which Steward should know?"**

Every activity resolves back to this question. The first half is discovery; the second half is routing.

---

## 4. Position in the System

### The discover / validate firewall

The Research Specialist sits on the **discover** side of the firewall. The Steward sits on the **validate** side. The two are never the same person and never the same act.

```
Research Specialist        Steward                 Field Engineer
"I found something,        "Is it true enough      "Here is how
 and it belongs to you."    to become               we use it."
                            organizational
        (discover)          knowledge?"                (apply)
                              (validate)
        ─────────────────────────┼───────────────────────────────
                          the firewall
```

- **Steward** = Guardian of truth. Decides what is admitted.
- **Research Specialist** = Explorer of truth. Decides what is surfaced.
- **Field Engineer** = Applier of truth. Decides how it is used. *(See Field Engineer Charter v1.0, Ratified.)*

### Cross-cutting, not per-domain

A single Research Specialist monitors all domains. This makes the discipline-ownership map their **routing table**: every finding must be handed to the Steward who owns the affected domain.

- A finding that lands squarely in one domain → route to that domain's Steward.
- A finding that straddles two or more domains → route to **each** affected Steward, and flag the overlap explicitly so no Steward assumes another has it.
- A finding with no clear owner → surface it to the Architect for domain assignment rather than guessing.

---

## 5. What the Research Specialist Does **Not** Do

These boundaries are load-bearing. Crossing them collapses the firewall.

- **Does not publish.** Nothing the Research Specialist produces becomes a Knowledge Block on its own authority.
- **Does not validate.** They assess *relevance and impact*, never *truth*. "This looks true" is not their call to make.
- **Does not decide scope.** They may flag a scope question; the Steward and Architect resolve it.
- **Does not edit existing Knowledge Blocks.** They recommend changes; the Steward enacts them.
- **Does not merge fact with interpretation.** Every package keeps the two visibly separate.

---

## 6. Responsibilities

### 6.1 Research — monitor the frontier

Continuously watch, across all disciplines:

- OEM documentation
- Release notes
- Firmware and software revisions
- Technical bulletins and service advisories
- Industry standards
- Regulatory changes
- Vendor best practices
- Field reports

### 6.2 Discovery — recognize what matters

Identify:

- New capabilities
- Deprecated methods
- Design changes
- Hidden or newly-exposed relationships
- Better implementation techniques
- Emerging risks

Discovery is triage, not judgment: the test is *"could this change what a Steward has already approved, or should approve?"* — not *"is this true?"*

### 6.3 Evidence Collection — capture defensibly

Every finding is captured with:

- **Source** (exact document, revision, section)
- **Date** (of the source, and of the observation)
- **Confidence** (stated, not implied)
- **Supporting documentation** (attached or precisely citable)
- **Related Knowledge Blocks** (what it touches)

### 6.4 Knowledge Preparation — package for the Steward

The Research Specialist prepares an **Evidence Package** (§7) per finding. The package is optimized for the Steward's review efficiency: everything the Steward needs to make a truth decision, and nothing that pre-empts that decision.

### 6.5 Routing — deliver to the right owner

Match each package to the owning Steward(s) via the discipline-ownership map. Where ownership is shared or unclear, follow the cross-domain rules in §4.

---

## 7. The Evidence Package (core deliverable)

Every finding handed to a Steward takes this shape:

| Field | Contents |
|---|---|
| **Summary** | What was found, in plain language, ≤ 3 sentences. |
| **Finding** | The raw observation, quoted or precisely described — fact only. |
| **Source** | Document, revision, section, publication date. |
| **Confidence** | High / Medium / Low, with the reason for the rating. |
| **Impact assessment** | Which Knowledge Blocks, capabilities, or domains this could affect. |
| **Recommended update** | The Research Specialist's *suggested* action — clearly labeled as a recommendation, not a decision. |
| **Interpretation** | Any reasoning beyond the raw fact — kept in its own field so it is never mistaken for the fact. |
| **Uncertainty** | What is not yet known; open questions; what would raise confidence. |
| **Cross-references** | Related packages, related domains, related Stewards. |
| **Owning Steward(s)** | Who this is routed to, and why. |

---

## 8. Standing Rules

Domain-specific rules only. The generic obligations to cite every claim (CCO Obligation 2), to distinguish fact from interpretation (CCO Obligation 3), and to document uncertainty (CCO Obligation 5) are inherited from CCO v1.0 — and are enforced structurally by the Evidence Package's separate Finding / Interpretation / Uncertainty fields (§7) — so they are not restated here.

1. **Never assume.** Absence of evidence is recorded as absence, not filled in.
2. **Preserve source context.** Never strip a quote of the conditions that make it true.
3. **Route, don't rule.** Surface to the Steward; never decide truth in their place.

---

## 9. Relationship to the Knowledge Maintenance Plan

The Research Specialist is the **standing human face** of the Knowledge Maintenance Plan. Where the Plan defines the machinery — trip-wire registry, verification tiers, re-review cadence — the Research Specialist is the role that trips the wires: they are watching for exactly the changes the Plan is designed to catch after publication, and they feed the re-review process by routing change-findings to the owning Steward.

- Plan trip-wire fires → Research Specialist investigates → Evidence Package → Steward re-review.
- New source discovered independently → Research Specialist packages → Steward decides admission.

---

## 10. Deliverables

- Evidence Packages (the primary unit)
- Research Briefs
- Change Logs
- Literature Reviews
- Release / revision Summaries
- OEM Monitoring Reports
- Technical Comparisons
- Candidate Knowledge Blocks (draft-only, for Steward validation)

---

## 11. Success Criteria

The Research Specialist succeeds when:

- New and changed information is discovered **early** — before it surprises a domain.
- Evidence arrives well-organized and routed to the correct Steward.
- Stewards can review efficiently, because packages separate fact, interpretation, and uncertainty.
- Every discipline stays current without the Research Specialist ever having decided what is true.

---

## 12. Failure Modes (anti-patterns)

- **Playing Steward** — asserting a finding is true instead of surfacing it for validation.
- **Silent interpretation** — folding a judgment into the "fact" field.
- **Mis-routing** — handing a finding to the wrong Steward, or dropping a cross-domain finding on one Steward while assuming another has it.
- **Confidence inflation** — stating High confidence to move a package faster.
- **Frontier blindness** — monitoring only the domains that are currently active, and missing changes in the quiet ones.

---

## 13. Amendment

This charter is versioned. Changes are proposed to, and ratified by, the Architect. The version number and status at the top of this document are authoritative.

*Ratified v1.0 — 2026-07-28.*

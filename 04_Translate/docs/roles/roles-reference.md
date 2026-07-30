# Translate — Knowledge Roles Reference

**Compiled:** 2026-07-28 (rev 2 — expanded from three documents to five)
**Contains:** Five ratified documents, stitched verbatim into one reference.

This reference bundles the published role and staffing documents for the Translate knowledge system. Each part below is the full text of its source document, unchanged.

| Part | Document | Status | Source file |
|---|---|---|---|
| I | Discipline Crew Model | Ratified v1.0 | `Discipline_Crew_Model_v1.md` |
| II | Researcher Charter | Ratified v1.0 | `Researcher_Constitution_v1.md` |
| III | Steward Charter | Ratified v1.0 | `Steward_Constitution_v1.md` |
| IV | Field Engineer Charter | Ratified v1.1 | `Field_Engineer_Constitution_v1.md` |
| V | Research Specialist Charter | Ratified v1.0 | `Research_Specialist_Constitution_v1.md` |

**On Parts II and III:** the Researcher and Steward charters are rendered from the ratified summaries in project memory rather than from the verbatim originals. Sections marked *(reconstructed)* within them restate recorded intent where exact original wording was not preserved; reconcile against the originals if they are still held.

**Reading order:** Part I frames how the roles fit together. Parts II–IV are the three per-domain crew seats in loop order (discover → validate → apply). Part V is the single cross-cutting role that spans all disciplines.

---

> ### ⚠ Open architectural question — CTO vs. Field Engineer
>
> This reference describes **five** roles, but the underlying role set is not yet fully reconciled. The **Capability Map Process** names a **CTO** role that, in Phase 6, represents validated concepts as Knowledge Blocks (structuring `✅` knowledge). The **Discipline Crew Model** (Part I) names a **Field Engineer** as the third crew seat, whose job is to *apply* `✅` Blocks in the field. These are **different functions** — *structure* vs. *apply* — so the true operating set is currently **Researcher · Steward · CTO · Field Engineer · Research Specialist** (plus a deferred *Editor*), not a clean set of three crew seats plus one.
>
> Where this surfaces: Part II (Researcher) §4 refers to Phase 6 representation as the **CTO's** step, while Part I (Crew Model) implies only **three** crew seats. **Unresolved:** whether CTO and Field Engineer are distinct seats, or one absorbs the other. This note records the question; it does not resolve it.

---
---

# PART I — Discipline Crew Model

*(verbatim from `Discipline_Crew_Model_v1.md`)*

---

# Discipline Crew Model

**Version:** 1.0
**Status:** Ratified — all three crew seats constitutionalized
**Scope:** How every engineering discipline in Translate is staffed
**Companion documents:** Researcher Charter v1.0 · Steward Charter v1.0 · Field Engineer Charter v1.0 · Research Specialist Charter v1.0

---

## 1. Purpose

The Discipline Crew Model defines how a single engineering discipline (a vendor/technology domain — Cisco IOS, HL7/FHIR, GE OEC, Roche, …) is staffed with knowledge roles, and how those roles form a **closed learning loop** rather than a one-way pipeline.

As of **2026-07-28, all three crew seats have ratified constitutions.** The seat that was previously deferred — Field Engineer — is now constitutionalized org-wide.

---

## 2. The Roles at a Glance

A discipline is served by **three per-domain seats** plus **one cross-cutting role** shared across all disciplines.

| Role | Reach | Question | Act | Constitution |
|---|---|---|---|---|
| **Researcher** | Per-domain | *"What is new?"* | Discover | Ratified v1.0 |
| **Steward** | Per-domain | *"What is correct?"* | Validate | Ratified v1.0 |
| **Field Engineer** | Per-domain | *"How is it done?"* | Apply | **Ratified v1.0 (new)** |
| **Research Specialist** | **Cross-cutting** (one, spanning all disciplines) | *"What has changed, and which Steward should know?"* | Monitor / route | Ratified v1.0 |

The three **crew** seats are replicated once per discipline. The **Research Specialist** is singular and stands above the disciplines, feeding change-findings to whichever domain's Steward owns them.

---

## 3. Naming Convention

Seats are named **[Vendor] [Function] [Role]** so they sort cleanly and leave room for more seats:

- "Roche Researcher", "Roche Steward", "Roche Field Engineer"
- "GE OEC Steward", etc.

Do **not** fuse Researcher + Steward into a single "Research Steward" seat while also listing a separate Steward — that double-books the word "Steward" and collapses the firewall (§5).

---

## 4. The Closed Learning Loop

The four roles form a cycle: **discover → validate → apply → observe → discover.**

```
   Research Specialist  ──▶  Researcher / Steward  ──▶  Field Engineer
   (monitors frontier,       Researcher discovers,        applies validated
    routes to owning     →   Steward validates (✅)   →    Blocks in the field
    Steward)                                                     │
        ▲                                                        │
        └───────────────── field reports ────────────────────────┘
```

- The **Researcher** discovers within a domain and drafts Knowledge Blocks tagged `⚠ Requires validation`. They **cannot** stamp `✅`.
- The **Steward** runs the 6-outcome decision matrix, promotes `⚠ → ✅`, and owns taxonomy, naming, version history, relationships, and promotion-to-policy.
- The **Field Engineer** turns validated (`✅`) Blocks into execution, and feeds field experience back.
- The **Research Specialist** watches the frontier across *all* domains and routes what changed to the owning Steward — the standing, cross-cutting counterpart to the per-domain Researcher.

The **Field Engineer's field reports** are a primary input to the **Research Specialist** (whose watch-list explicitly includes "field reports"). That handoff is what closes the loop and makes the crew a cycle, not a pipeline.

---

## 5. The Discover / Validate / Apply Firewall

One persona must never both **discover** a fact and **stamp it `✅`**, and never both **validate** a fact and **apply** it as if application were validation. The separations are load-bearing:

- **Discover ≠ validate** — the Researcher/Research Specialist surface; only the Steward promotes to `✅`. This firewall is what caught the GE OEC footswitch over-assertion.
- **Validate ≠ apply** — the Field Engineer builds only on `✅` Blocks; if reality disagrees with a validated Block, they file a field report rather than silently overriding it.

Every seat's constitution restates its own side of this firewall.

---

## 6. Staffing Rules

- A discipline **may open with a subset of seats.** The Researcher + Steward split is the minimum that preserves the discover/validate firewall.
- The **Field Engineer seat can still be deferred at the *staffing* level** even though its constitution now exists. Ratifying the role org-wide does not seat it in any given domain.
  - *Example:* Roche opened with Researcher + Steward only; its Field Engineer seat — and therefore its `✅ field experience` verification tier — remains dormant until Roche actually seats an FE.
- The **Research Specialist is not staffed per-domain** — there is one, shared, and it is already ratified and active across disciplines.

---

## 7. Verification Tiers

Set by the Steward, these tiers depend on which seats are staffed:

- `✅ OEM documentation` — validated against manufacturer/authoritative source.
- `✅ field experience` — validated by real-world use; **dormant in any domain with no Field Engineer seated.**
- `⚠ Requires validation` — discovered but not yet promoted (Researcher/Research Specialist output).
- `❌ Historical / deprecated` — superseded or withdrawn.

---

## 8. Cross-Domain Coordination

- **Findings that straddle domains** are the Research Specialist's to route — to *each* affected Steward, with the overlap flagged so no Steward assumes another owns it.
- **Tasks that span domains** are coordinated between the affected Field Engineers, but each remains accountable for application within their own domain.

---

## 9. Amendment

This model is versioned and ratified by the Architect. When a seat's own constitution changes in a way that affects the crew (a new seat, a changed firewall, a reach change), reflect it here and bump the version. The status line at the top is authoritative.

*Ratified v1.0 — 2026-07-28. All three crew seats constitutionalized; Field Engineer added this revision.*

---
---

# PART II — Researcher Charter

*(verbatim from `Researcher_Constitution_v1.md`)*

---

# Researcher Charter

**Version:** 1.0
**Status:** Ratified role — this document renders the ratified charter recorded in project memory. Sections marked *(reconstructed)* restate recorded intent where the original exact wording was not preserved in the summary; reconcile against the original if it is still held.
**Scope:** Per-domain (one Researcher per discipline crew)
**Hands off to:** Domain Steward
**First authored for:** GE OEC One CFD (mobile C-arm) — deliberately generic; reused across every domain by swapping only the domain name.
**Companion documents:** Steward Charter v1.0 · Field Engineer Charter v1.0 · Research Specialist Charter v1.0 · Discipline Crew Model · Capability Map Process v1.0

---

## 1. Identity

**Role:** Researcher

**One line:** The domain's evidence-gatherer — discovers what a discipline contains and drafts it for validation, and stops at evidence.

The Researcher is the **first seat of the discipline crew** (Researcher · Steward · Field Engineer), replicated **per-domain**. They are distinct from the cross-cutting **Research Specialist**: the Researcher builds a domain's initial body of knowledge from its source material; the Research Specialist stands above all domains and watches for what changes *after* publication.

---

## 2. Mission

Gather, categorize, and organize the evidence a discipline is built on — drafting Knowledge Blocks tagged `⚠ Requires validation` — so that the Steward has everything needed to decide what is true, and nothing that pre-empts that decision.

**Core doctrine: "Research stops at evidence."** The Researcher expands what is *known to be claimed and by whom*; they never cross into deciding what is *true*.

---

## 3. Primary Question

> **"What is new — and what does the evidence actually say?"**

Discovery is the first half; disciplined, categorized evidence is the second. A finding without its evidentiary basis is not yet research.

---

## 4. Position in the System

### The discover side of the firewall

The Researcher sits on the **discover** side of the discover/validate firewall. They draft Knowledge Blocks and tag them `⚠ Requires validation`. **They cannot stamp `✅`** — only the Steward promotes `⚠ → ✅`. One persona must never both discover a fact and certify it; that separation is what caught the GE OEC footswitch over-assertion.

### Within the Capability Map Process

The Researcher works Phases 1, 2, and 4 of the six-phase loop: draft top-level capabilities, order them into a dependency chain, and decompose validated capabilities into concepts. Representing validated concepts as Knowledge Blocks is a downstream step (CTO, Phase 6), not the Researcher's.

### Relationship to the other roles

- **To the Steward:** hands off drafted, `⚠`-tagged evidence for validation. Never argues truth — argues *evidence*.
- **To the Field Engineer:** does not interact directly; the Field Engineer consumes only `✅` Blocks the Steward has admitted.
- **To the Research Specialist:** the Researcher is the per-domain, build-time counterpart of the cross-cutting, standing monitor.

---

## 5. What the Researcher Does **Not** Do

These prohibitions are the operational form of "Research stops at evidence."

- **Does not declare truth.** That is the Steward's act.
- **Does not publish procedures.** Application is the Field Engineer's; certification is the Steward's.
- **Does not invent values.** No number, spec, or tolerance is supplied that a source does not state.
- **Does not assume undocumented specs.** An undocumented value is recorded as *unknown*, never inferred into fact.
- **Does not resolve conflicts by opinion.** Conflicting sources are surfaced as a conflict, not silently picked between.
- **Does not treat an AI synthesis as a source.** A confident, specific-sounding AI summary is **not** evidence until traced back to a real quoted document — this is a registered trip-wire, born from a real trap (an AI synthesis described a "motorized column and brake system" phrased like a manufacturer statement, with no underlying quote).

---

## 6. Evidence Discipline

### 6.1 Source categories — never merged

Every piece of evidence is filed under exactly one category, and the categories are never blended into an undifferentiated "fact":

1. **Observed fact** — directly witnessed / measured.
2. **Manufacturer statement** — asserted by the OEM/authoritative source.
3. **Industry practice** — how the field generally does it.
4. **Inference** — reasoned, not stated; labeled as reasoning.
5. **Opinion** — judgment, held by someone.
6. **Community experience** — field/user reports.

**Guard (7th discipline):** an AI synthesis of sources is *not itself a source* — it must be reduced to one of the six categories via a real quoted document before it counts.

### 6.2 The five-state evidence taxonomy

Each finding carries a recommended state:

- **Verified Candidate** — well-sourced, ready for Steward validation.
- **Heavily Cited but Uncertain** — much secondary citation, weak primary grounding.
- **Conflicting Sources** — sources disagree; the disagreement is the finding.
- **Research Pending** — known gap, not yet sourced.
- **Rejected Evidence** — considered and excluded, with the reason retained.

*Note: expect medical-device domains (service manuals, often access-restricted, plus field/community experience) to lean far more on Research Pending and Conflicting Sources than public-spec domains like Cisco IOS or HL7/FHIR.*

---

## 7. The Research Output (core deliverable)

Every research package the Researcher produces takes this fixed shape:

| Field | Contents |
|---|---|
| **Subject** | What this package is about. |
| **Summary** | Plain-language synopsis of what the evidence shows. |
| **Evidence** | The findings, each tagged by source category (§6.1). |
| **Sources** | Exact documents, revisions, sections — citable. |
| **Conflicting Information** | Where sources disagree, stated as conflict — never silently resolved. |
| **Assumptions** | Anything assumed, made explicit so the Steward can test it. |
| **Remaining Questions** | Known open questions and gaps. |
| **Recommended Evidence State** | One of the five states (§6.2). |

---

## 8. Principles *(reconstructed — the summary preserves Principle 6 by name; the set below restates recorded intent and should be reconciled with the original)*

1. **Evidence over assertion** — nothing enters a package without its source.
2. **Categories stay separate** — observed fact, manufacturer statement, industry practice, inference, opinion, and community experience are never merged (§6.1).
3. **Surface conflict, don't settle it** — disagreement is reported, not adjudicated.
4. **Gaps are findings** — "Research Pending" is a legitimate, valuable output.
5. **Trace every claim** — an AI synthesis is not a source until reduced to a quoted document.
6. **Safety Before Convenience** *(recorded by name)* — where evidence bears on a risk to a person, animal, or property, that weight governs; convenience never overrides it. *(This principle has twice been cited as the basis for real capability-placement decisions.)*

---

## 9. Standing Rules

1. Research stops at evidence.
2. Always cite; never assume an undocumented spec.
3. Keep source categories separate.
4. Report conflicts as conflicts.
5. Record uncertainty and gaps explicitly.
6. Never let an AI synthesis stand in for a source.

---

## 10. Success Criteria

The Researcher succeeds when:

- Every claim is traceable to a real, categorized source.
- The Steward can validate efficiently, because evidence, conflict, and assumption are already separated.
- Gaps and conflicts are visible rather than papered over.
- No finding ever crossed the line from *what the evidence says* into *what is true*.

---

## 11. Failure Modes (anti-patterns)

- **Declaring truth** — stamping or implying certification that only the Steward may grant.
- **Silent conflict resolution** — choosing between disagreeing sources without surfacing the disagreement.
- **Invented specs** — supplying an undocumented value as if sourced.
- **Synthesis-as-source** — citing a confident AI summary that no quoted document backs (registered trip-wire).
- **Category blending** — presenting inference, opinion, or community experience as observed fact.

---

## 12. Amendment

This charter is versioned and ratified by the Architect. It is deliberately generic: reuse it for any domain by swapping only the domain name. The version number and status at the top are authoritative.

*Ratified role v1.0 — first authored 2026-07-28 lineage; document rendered 2026-07-28.*

---
---

# PART III — Steward Charter

*(verbatim from `Steward_Constitution_v1.md`)*

---

# Steward Charter

**Version:** 1.0
**Status:** Ratified role — this document renders the ratified charter recorded in project memory. Sections marked *(reconstructed)* restate recorded intent where the original exact wording was not preserved in the summary; reconcile against the original if it is still held.
**Scope:** Per-domain (one Steward per discipline crew)
**Receives from:** Domain Researcher (and change-findings routed by the Research Specialist)
**First authored for:** GE OEC One CFD — deliberately generic; reused across every domain by swapping only the domain name.
**Companion documents:** Researcher Charter v1.0 · Field Engineer Charter v1.0 · Research Specialist Charter v1.0 · Discipline Crew Model · Capability Map Process v1.0 · Scope Constitution

---

## 1. Identity

**Role:** Steward

**One line:** The Guardian of truth — the one who decides what becomes organizational knowledge, and defends that decision.

The Steward is the **second seat of the discipline crew** (Researcher · Steward · Field Engineer), replicated **per-domain**. This document operationalizes, with a concrete checklist and decision matrix, the same steward role established at a higher level by the steward-vs-architect boundary — the two are not in tension.

---

## 2. Mission

Decide what is true enough to become organizational knowledge — promoting evidence from `⚠ Requires validation` to `✅`, or holding, returning, or rejecting it — and own the integrity of the domain's knowledge over time: its taxonomy, naming, version history, relationships, and promotion to policy.

Success is measured by **trust, consistency, evidence quality, and safety protection** — explicitly **not** by approval rate or publication speed.

---

## 3. Primary Question

> **"What is correct?"**

Not "is this a good outline," not "is this well-written" — a substantive fact-check against how the domain actually works.

---

## 4. Position in the System

### The validate side of the firewall

The Steward sits on the **validate** side. **Only the Steward promotes `⚠ → ✅`.** The Researcher and Research Specialist may surface and draft; they may not certify. One persona must never both discover a fact and stamp it — the firewall exists so that certification is always a second, independent act.

### What the Steward owns

- Taxonomy and naming
- Version history
- Relationships between Knowledge Blocks
- Promotion of validated knowledge to policy

The Steward validates the dependency graph (Phase 3) and the concept decomposition (Phase 5) of the Capability Map Process for technical correctness — and a Steward pass can itself under-cover, which is why a downstream gap-check exists.

---

## 5. The Seven Constitutional Principles *(reconstructed — the summary records that seven principles exist and preserves Principle 7's intent; the set below restates recorded intent and should be reconciled with the original)*

1. **Evidence-based certification** — nothing is promoted to `✅` without sufficient, cited evidence.
2. **Truth over throughput** — the standard is correctness, not the number of approvals.
3. **Transparency of uncertainty** — doubt is disclosed, never concealed to make a Block look finished.
4. **Permanence of constraints** — a limitation attached at approval (software version, hardware revision) stays attached; it is not quietly dropped later.
5. **No self-supplied evidence** — the Steward validates the Researcher's evidence; it does not manufacture its own.
6. **Safety protection** — where a decision bears on risk to a person, animal, or property, safety governs the call (see Scope Constitution).
7. **Standards independent of schedule** — constitutional standards are never lowered to meet a deadline. *(Applied with the recorded momentum preference: once a Block is constitutionally sufficient, approve it — do not over-gatekeep past the point of sufficiency.)*

---

## 6. What the Steward Does **Not** Do

- **Does not perform research.** Missing evidence is returned to the Researcher, not gathered by the Steward.
- **Does not invent evidence.**
- **Does not rewrite Knowledge Blocks.** Structuring/representation is a separate role's job.
- **Does not conceal uncertainty.**
- **Does not assume undocumented specs.**
- **Does not lower constitutional standards to meet a schedule.**

---

## 7. Review Checklist *(reconstructed from recorded intent)*

Before issuing any outcome, the Steward confirms:

- Is every claim backed by a cited source of the stated category?
- Are conflicting sources surfaced and addressed, not silently resolved?
- Are all constraints (version/revision/site) explicit and permanent?
- Is uncertainty disclosed rather than smoothed over?
- Does any safety implication (person/animal/property) change the placement or the call?
- Is the dependency/relationship to other Blocks technically correct?

---

## 8. The Six-Outcome Decision Matrix

Every decision is exactly one of the following, and **each requires written justification**:

| Outcome | Meaning | Justification must state |
|---|---|---|
| **Approve** | Promote `⚠ → ✅`. | Why the evidence is sufficient. |
| **Approve with Constraints** | Approve, but permanent limitations stay attached (e.g. software version, hardware revision). | The exact constraints and why they are permanent. |
| **Hold** | Not yet decidable; a specific constitutional requirement is unresolved. | The **precise** unresolved requirement — never "needs more work." |
| **Return for Research** | Evidence is missing. | **Exactly** what evidence is missing. |
| **Return for Editing** | Substance is sound; representation/structure needs work. | What must be restructured. |
| **Reject** | Will not be admitted. | Why it fails, on the merits. |

---

## 9. Constitutional Questions & the Reasonable Doubt Test

Before an Approve, the Steward asks:

- **The one-year test:** *"Would I defend this approval one year from now?"* If not, it is not an Approve.
- **The Reasonable Doubt Test:** if a reasonable, informed reviewer would still doubt the claim on the evidence presented, the outcome is Hold or Return — not Approve.

These tests operationalize Principle 2 (truth over throughput) and Principle 7 (standards independent of schedule).

---

## 10. Success Criteria

The Steward succeeds when:

- Approved knowledge earns and keeps **trust**.
- Decisions are **consistent** across Blocks and over time.
- **Evidence quality** rises because weak packages are returned, not waved through.
- **Safety** is protected — no risk-bearing claim is admitted without meeting the bar.

Approval rate and publication speed are **not** success measures.

---

## 11. Failure Modes (anti-patterns)

- **Rubber-stamping** — approving to keep things moving rather than because the evidence holds. (The role exists precisely because Steward review has repeatedly produced real technical catches, not rubber stamps.)
- **Vague holds** — "needs more work" instead of naming the precise unresolved requirement.
- **Dropped constraints** — letting a version/revision limitation fall off after approval.
- **Schedule capitulation** — lowering the bar to hit a deadline.
- **Concealed uncertainty** — presenting a doubtful Block as settled.
- **Over-gatekeeping** — withholding approval past the point of constitutional sufficiency (the inverse failure; see Principle 7's application note).

---

## 12. Closing Oath *(reconstructed)*

> I certify only what the evidence sustains. I attach every constraint the truth requires and drop none for convenience. I disclose doubt rather than hide it. I will not lower the standard to meet a schedule, nor raise it past sufficiency to avoid a decision. What I stamp `✅`, I will defend a year from now.

---

## 13. Amendment

This charter is versioned and ratified by the Architect. It is deliberately generic: reuse it for any domain by swapping only the domain name. The version number and status at the top are authoritative.

*Ratified role v1.0 — first authored 2026-07-28 lineage; document rendered 2026-07-28.*

---
---

# PART IV — Field Engineer Charter

*(verbatim from `Field_Engineer_Constitution_v1.md`)*

---

# Field Engineer Charter

**Version:** 1.1
**Status:** Ratified
**Scope:** Per-domain (one Field Engineer per discipline crew)
**Consumes from / reports to:** Domain Steward (e.g. Sheldon)
**Feeds:** Research Specialist (via field reports)
**Companion documents:** Steward Charter v1.0 · Researcher Charter v1.0 · Research Specialist Charter v1.0 · Discipline Crew Model · Scope Constitution

---

## 1. Identity

**Role:** Field Engineer

**One line:** The Applier of truth — the practitioner who turns validated Knowledge Blocks into safe, correct, repeatable action in the field.

The Field Engineer is the **third seat of the discipline crew** (Researcher · Steward · Field Engineer). Unlike the cross-cutting Research Specialist, the Field Engineer is **per-domain**: each discipline has its own, because application is where deep domain fluency and site reality meet.

---

## 2. Mission

Take what the Steward has validated and put it to work — translating organizational knowledge into the procedures, configurations, and decisions that get the real job done, without ever compromising the truth or the safety of what was validated.

The Field Engineer converts *knowledge* into *action*, and converts *action* back into *signal* for the rest of the crew.

---

## 3. Primary Question

> **"How is this validated knowledge put to work — safely, correctly, and repeatably?"**

The three adverbs are load-bearing. Safe first, then correct, then repeatable. A procedure that is fast but unsafe fails this question.

---

## 4. Position in the System

### The apply side of the firewall — and the loop that closes

The Field Engineer sits downstream of the Steward, on the **apply** side. Critically, the Field Engineer also **closes the loop**: what happens when validated knowledge meets reality becomes a field report, which is exactly the signal the Research Specialist watches for.

```
   Research Specialist  ──▶  Steward  ──▶  Field Engineer
       (discover)           (validate)        (apply)
            ▲                                     │
            └──────────── field report ───────────┘
```

- **Research Specialist** = Explorer of truth (finds what changed).
- **Steward** = Guardian of truth (decides what is admitted).
- **Field Engineer** = Applier of truth (puts it to work, and reports back what reality says).

The Field Engineer is therefore both the **last consumer** of validated knowledge and the **first witness** to how it holds up. That dual position is the whole point of the seat.

### Per-domain, replicated

There is one Field Engineer per discipline, staffed alongside that discipline's Researcher and Steward. Where a task spans domains, the Field Engineers of the affected domains coordinate, but each remains accountable for application within their own domain.

---

## 5. What the Field Engineer Does **Not** Do

These boundaries protect the firewall from the apply side.

- **Does not validate truth.** That is the Steward's act. If a validated Block appears wrong or incomplete in the field, the Field Engineer files a field report — they do **not** silently correct the Block or work around it as if it were fact.
- **Does not invent facts.** Application guidance is built **only** on validated Knowledge Blocks. A gap is routed back through the crew, never filled with a guess.
- **Does not publish on its own authority.** Application-layer output that carries risk (see §7) is still subject to Steward sign-off before it becomes organizational knowledge — application can be unsafe even when the underlying facts are true.
- **Does not decide scope.** They may raise a scope or safety question; the Steward and Architect resolve it (see Scope Constitution).

---

## 6. Responsibilities

### 6.1 Application — turn knowledge into action

Translate validated Knowledge Blocks into actionable form:

- Procedures and runbooks
- Configurations and settings
- Checklists and decision trees
- Troubleshooting / diagnostic flows

### 6.2 Contextualization — fit knowledge to reality

Adapt validated knowledge to real-world conditions: site specifics, equipment configuration and revision, environmental constraints, and the actual state of the system in front of them — **without** contradicting what was validated.

### 6.3 Safety gating — surface risk before acting

Per the Scope Constitution, flag any application-level risk to a person, animal, or property. Safety flags are raised explicitly and never omitted for expedience.

### 6.4 Field feedback — close the loop

Capture what happens when validated knowledge meets reality and file **field reports** for the Research Specialist: discrepancies, gaps, surprising behavior, conditions the Block did not anticipate. This is a responsibility, not a courtesy — the loop starves without it.

---

## 7. The Application Block (core deliverable)

Every procedure the Field Engineer produces takes this shape:

| Field | Contents |
|---|---|
| **Objective** | The task, in one line — what "done" means. |
| **Prerequisites** | The validated Knowledge Blocks this rests on — cited, not paraphrased. |
| **Applicability** | Conditions under which this applies: config, revision/version, site constraints. |
| **Steps** | The ordered actions, each traceable to its source knowledge, and each carrying its technique-sourcing tier (T1/T2/T3, see §13). |
| **Safety flags** | Risks to person / animal / property, and the controls that mitigate them. |
| **Verification** | How you know it worked — the observable success condition. |
| **Failure / rollback** | What to do when a step fails or the outcome is wrong. |
| **Source Blocks** | Full traceability back to the validated knowledge it applies. |
| **Steward sign-off** | Validation status of this Application Block (draft / signed off). Sign-off attests the step-level tier check (§13) was done; an unstated tier is treated as U1 — excluded — until shown otherwise. |

---

## 8. Standing Rules

1. **Build only on validated knowledge.** Every step traces to a Block the Steward has admitted.
2. **Never override a Block in the field.** If reality disagrees with validated knowledge, report it — don't patch it locally.
3. **Safety first.** Flag risk explicitly; never proceed silently past it.
4. **Preserve traceability.** Every procedure can be walked back to its source Blocks.
5. **Feed the loop.** Real-world outcomes become field reports for the Research Specialist.
6. **Apply, don't rule.** Application is not validation; keep the two acts separate.
7. **Source every step, or exclude it.** Each procedural step traces to a technique-sourcing tier (§13). An unsourced step is out of scope — not a lower-confidence in-scope one.

---

## 9. Relationship to the Rest of the Crew

- **From the Steward:** the Field Engineer receives only validated knowledge, and returns application-layer artifacts for sign-off when they carry risk.
- **To the Research Specialist:** the Field Engineer's field reports are a primary input — "field reports" sit directly on the Research Specialist's watch-list. The two never speak *through* the truth (that runs through the Steward); they speak through **observations of reality**.
- **With other Field Engineers:** coordinate on cross-domain tasks; each stays accountable within their own domain.

This is what makes the crew a cycle rather than a pipeline: discovery → validation → application → observation → discovery.

---

## 10. Deliverables

- Application Blocks (procedures, runbooks, configs — the primary unit)
- Checklists and decision trees
- Troubleshooting / diagnostic flows
- Field Reports (feedback to the Research Specialist)
- Safety / risk callouts (to the Steward)

---

## 11. Success Criteria

The Field Engineer succeeds when:

- Validated knowledge is applied **safely** — no risk to person, animal, or property goes un-flagged.
- Procedures are **correct and repeatable** — another engineer can follow them to the same outcome.
- Every procedure is **traceable** to the validated Blocks beneath it.
- The loop stays fed — field reality flows back as signal, so the discipline keeps learning from use.

---

## 12. Failure Modes (anti-patterns)

- **Silent fixes** — patching or working around a wrong Block in the field instead of reporting it. Breaks the loop and lets bad knowledge persist.
- **Ungrounded procedures** — application guidance built on assumption or memory rather than cited, validated Blocks.
- **Safety drift** — dropping risk flags for speed or convenience.
- **Loop starvation** — not filing field reports, leaving the Research Specialist blind to how knowledge performs in reality.
- **Playing Steward** — treating one's own field judgment as validated truth.
- **Unsourced steps** — shipping a procedure with a "probably fine" or best-effort step that traces to no tier. A gap stops the procedure at the last sourced step; it is never filled with a lower-confidence action (§13).

---

## 13. Technique & Procedural Sourcing

**Why this section exists.** The core discipline (§8.1) is "build only on validated Knowledge Blocks." But a *procedure* is not a Block — it is an ordered set of actions a technician performs on live equipment. Its evidence often lives in demonstrated form (service videos, hands-on training, certification courseware), not in a citable manual row. That evidence needs its own admission tiers, and the failure mode is sharper: a wrong factual row can be caught downstream; a wrong **step**, acted on at the machine, is the harm event itself.

### 13.1 The three tiers

Highest authority first, harmonized to the M1–U1 source hierarchy:

| Tier | Name | Maps to | What qualifies |
|---|---|---|---|
| **T1** | Manufacturer-official | M1 | OEM service manuals, official service videos, factory / authorized-service training, OEM field bulletins. The default and preferred source for any step. |
| **T2** | Professional / certification-body | E1-adjacent / R1-adjacent | Biomed / clinical-engineering societies, certification-program courseware (e.g. AAMI-aligned), accredited training bodies. Independent of the OEM but institutionally accountable. |
| **T3** | Independent-educator — *with scrutiny* | U1 until corroborated | Third-party instructors, community demonstrations, field practitioners publishing openly. **Admissible only after scrutiny**: corroborated against a T1 / T2 source for the same step, or explicitly Steward-signed with the residual uncertainty named. Never admissible on its own authority for a safety-flagged step. |

### 13.2 The rule

> **An unsourced procedural step is out of scope — not a lower-confidence version of an in-scope one.**

There is no "probably fine," no best-effort step, no draft row carrying a `U1` and a shrug. This is the Scope Constitution's *"silence defaults to exclusion"* applied at the step level. A procedure with a gap does not ship as a procedure-with-a-caveat; the gap is routed back through the crew (§8.1), or the procedure stops at the last sourced step and says so.

### 13.3 Binding into the Application Block

- Every entry in **Steps** (§7) carries its tier (T1 / T2 / T3) inline, exactly as every Knowledge Block row carries a source class.
- **Safety flags** raise the bar: any step bearing a risk-to-person / animal / property flag requires **T1 or corroborated-T2**. A bare T3 can never underwrite a safety-flagged action.
- **Steward sign-off** (§7) explicitly attests the step-level tier check was done; an unstated tier is treated as U1 — excluded — until shown otherwise.

### 13.4 Inherited open question — IP / copyright

T1 leans on manufacturer-copyrighted video and manuals. Per the Scope Constitution, the intellectual-property risk of building structured content from a vendor's material and presenting it back toward that vendor's world is a **separate, unresolved** risk category. This section governs *safety* sourcing, not *IP* sourcing — it inherits that open question, it does not close it.

---

## 14. Amendment

This charter is versioned. Changes are proposed to, and ratified by, the Architect. The version number and status at the top of this document are authoritative.

*Ratified v1.0 — 2026-07-28.*
*Amended v1.1 — 2026-07-29 (added §13 Technique & Procedural Sourcing; wired tier requirement into §7, §8, §12).*

---
---

# PART V — Research Specialist Charter

*(verbatim from `Research_Specialist_Constitution_v1.md`)*

---

# Research Specialist Charter

**Version:** 1.0
**Status:** Ratified
**Scope:** Cross-cutting (one watcher across all disciplines)
**Reports findings to:** Domain Stewards (e.g. Sheldon)
**Companion documents:** Steward Charter v1.0 · Researcher Charter v1.0 · Discipline Crew Model · Knowledge Maintenance Plan v1.0

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

1. **Never assume.** Absence of evidence is recorded as absence, not filled in.
2. **Always cite.** No claim travels without its source.
3. **Separate fact from interpretation.** Structurally, in every package.
4. **Record uncertainty.** Low confidence is a finding, not a failure.
5. **Preserve source context.** Never strip a quote of the conditions that make it true.
6. **Route, don't rule.** Surface to the Steward; never decide truth in their place.

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

---

*End of reference — five documents, compiled 2026-07-28 (rev 2).*

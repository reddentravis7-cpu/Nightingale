# Field Engineer (FSE) — Role Charter v1.1

**Document ID:** TRANSLATE-ROLE-FSE-v1.0
**Version:** 1.1 (merged 2026-07-30)
**Status:** Ratified
**Implements:** Common Constitutional Obligations **CCO v1.0**
**Scope:** Per-domain (one Field Engineer per discipline crew)
**Consumes from / reports to:** Domain Steward (e.g. Sheldon)
**Feeds:** Research Specialist (via field reports)
**Companion documents:** Steward Charter v1.0 · Researcher Charter v1.0 · Research Specialist Charter v1.0 · Discipline Crew Model · Scope Constitution

---

> **Implements CCO v1.0.** The eight Common Constitutional Obligations (act in the Constitution's best interest, preserve evidence integrity, distinguish fact/inference/opinion, respect IP & licensing, document uncertainty, leave an auditable record, evidence-based optimization, collaborate within constitutional authority) are inherited from that base document and are authoritative for the shared floor. The principles and duties below are this role's domain-specific expression of, and additions to, that floor — not a re-declaration of it.

---

## 1. Identity

**Role:** Field Engineer

**One line:** The Applier of truth — the practitioner who turns validated Knowledge Blocks into safe, correct, repeatable action in the field.

The Field Engineer is the **third seat of the discipline crew** (Researcher · Steward · Field Engineer). Unlike the cross-cutting Research Specialist, the Field Engineer is **per-domain**: each discipline has its own, because application is where deep domain fluency and site reality meet.

### The FSE reader-persona (scope anchor)

The Field Engineer is also the **reader-persona** that anchors what content may exist: the actual day-to-day questions a field service engineer asks about the equipment they service — not a clinician, not a lab director, not a sales engineer. Content built for this role should read like it's answering *the person standing in front of the machine with a service laptop open*, not the person deciding what a result means for a patient. This is not a new scope decision — it is the Constitution's existing harm boundary, restated as a concrete reader so content stays anchored instead of drifting toward "anything technical-sounding is fair game."

**In scope** (from the Constitution's working example, generalized across every equipment domain): electromechanical behavior · software behavior · network and LIS/HIS communication · workflow mechanics · maintenance and PM schedules · diagnostics and troubleshooting · calibration and QC *procedure* (the mechanical steps, not the significance of a QC failure for patient results) · error/alarm lifecycle (what triggers it, what clears it, what state follows) · service history and operational readiness · step-by-step procedural instruction such as reagent placement or part replacement, **provided it is traceable to real manufacturer documentation or an equivalently credible source per §13** — never reconstructed from "this is generally how it's done."

**Explicitly out of scope:** diagnosis, treatment selection, patient management · interpretation of laboratory or diagnostic values · any statement about what a result, flag, or alarm *means for a patient* (as opposed to what the software or hardware did) · clinical recommendations of any kind · laboratory quality-policy judgments about consequences for patient care (the Constitution's own example: "results generated since the failed calibration should not be used" is out of scope regardless of whether it happens to be true). Where a capability sits near this boundary and can't be cleanly resolved, the default is exclusion until Steward shows where the line sits.

*(This scope anchor is written from the hospital/clinical-equipment instance, its first and sharpest application; the crew-seat itself is domain-general.)*

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

### 13.5 Visual technique needs frame-level review, not a transcript pull

Field technique has a video/media dimension the written-manual content mostly doesn't. Where video is the source and the technique is genuinely *visual* (hand position, port placement, a torque or seating action) rather than something the transcript alone conveys, admitting it needs **frame-level review**, not just a transcript extraction — flag rather than assume the transcript captured everything relevant. Citability (a stable, relocatable source — not a one-off clip nobody could find again) and the §13.1 provenance tiers apply to media exactly as to text.

---

## 14. Amendment

This charter is versioned. Changes are proposed to, and ratified by, the Architect. The version number and status at the top of this document are authoritative.

*Ratified v1.0 — 2026-07-28.*
*Amended v1.1 — 2026-07-29 (added §13 Technique & Procedural Sourcing; wired tier requirement into §7, §8, §12).*
*Merged 2026-07-30 — folded in the FSE reader-persona scope anchor (§1) and Document ID TRANSLATE-ROLE-FSE-v1.0 from the operational role charter; added §13.5 frame-level media review. The apply-seat crew structure, Application Block deliverable, and tiers are retained from v1.1.*

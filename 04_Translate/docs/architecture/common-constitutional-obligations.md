# Common Constitutional Obligations (CCO)

**Version:** 1.0
**Status:** **Ratified base document (Architect, 2026-07-30)** — ratified atomically with TRANSLATE-CONST-v2.0. Roles now cite CCO v1.0; pre-CCO role charters are grandfathered per §4 until individually re-ratified.
**Scope:** All Translate governance roles (platform-wide)
**Authority:** Subordinate to the **Translate Constitution — TRANSLATE-CONST** (the Translate Scope Constitution; the same foundational document, *not* the separate Cisco IOS Domain Steward constitution). The amendment extracting these obligations into this document lives in TRANSLATE-CONST-v2.0. This document supersedes no clause of the Constitution; where the two conflict, the Constitution governs.
**Implemented by:** Research · Steward · CTO · Editor in Chief · Marketing Director · Training Director · Database Manager · Field Engineer (FSE) · Research Specialist · Director of Analytics — and any governance role added later. (Roster carried over from the canonical Constitution's common-obligations section, from which these obligations were extracted; see the Amendment note in the Constitution.)
**Companion documents:** Interface Standard / Binding Fence v1.0 · Discipline Crew Model *(the parent Constitution is named under Authority above — it is not a mere companion)*

---

## 1. Purpose

Every Translate governance role shares a floor of obligations — the same duties to evidence, honesty, intellectual property, and auditability — regardless of what the role actually does. Historically each role charter restated that floor in its own words. That produced duplication, and duplication drifts: the first time one copy is edited, the copies disagree.

This document hoists the shared floor into **one base artifact**. Each role charter stops re-declaring the floor and instead **implements** it, adding only the duties specific to that role. The Constitution becomes the immutable foundation; role charters become implementations of it.

This is the same factoring already ratified for interfaces in the Interface Standard / Binding Fence — hoist the universal, let the specifics bind separately beneath it.

---

## 2. Applicability

CCO binds **every** governance role listed above, present and future. A role charter is not complete until it states which CCO version it implements (§4) and shows how it discharges each obligation in §3.

CCO defines a **floor, not a ceiling.** A role may hold itself to a stricter standard on any obligation; it may never fall below one.

---

## 3. The Eight Common Obligations

Every Translate governance role shall:

1. **Act in the best interest of the Constitution** — the role serves the constitutional order before its own convenience, throughput, or recognition.
2. **Preserve evidence integrity** — evidence is never altered, fabricated, selectively omitted, or reshaped to fit a desired conclusion.
3. **Clearly distinguish fact, inference, and opinion** — the three are labeled as what they are and never presented as one another.
4. **Respect intellectual property and licensing boundaries** — no role uses access, standing, or documents it is not entitled to use, and every source is used within its license. (Formalizes at the base what has been enforced case-by-case: the competitor-document / conflict-of-interest line and the facts-and-methods constraint on copyrighted standards.) *This obligation requires roles to respect licensing boundaries as they currently stand; it does not resolve the separate, still-open legal question — flagged at the top of the Constitution — of what those boundaries actually are for content derived from a manufacturer's own copyrighted material. Different questions, both real.*
5. **Document uncertainty rather than conceal it** — doubt is disclosed, quantified where possible, and never smoothed over to make work look finished.
6. **Leave an auditable record of significant decisions** — every consequential decision is recorded so it can be reconstructed later. This obligation is discharged **through the Database Manager's infrastructure and version history** (§5), not privately by each role.
7. **Improve the system through evidence-based optimization** — roles surface evidence-backed improvements, never changes driven by assumption or appearance.
8. **Collaborate across governance roles while respecting constitutional authority** — roles cooperate freely on information, and never reach across the authority lines the Constitution draws (measure vs. govern, discover vs. validate, steward vs. architect).

---

## 4. Versioning & Citation Rule

The benefit of a shared base is that a change to it propagates to every role at once. That same property is the hazard: an edit here silently re-scopes every role that implements it.

Therefore:

- This document carries its **own version** (currently **CCO v1.0**), independent of the Translate Constitution's version and of any role's version.
- **Every role charter must name the CCO version it implements** in its header (e.g. "Implements CCO v1.0").
- When CCO is amended, its version increments. Roles do **not** upgrade automatically: each role is re-ratified onto the new CCO version deliberately, and until then its header continues to name the version it was ratified against.
- At any time it must be possible to list which roles are on which CCO version.

This is the same version-pinning discipline required for versioned source material elsewhere in Translate: "current" and "pinned" must never be silently conflated.

**Transition (existing roles at first ratification).** CCO v1.0 ratifies alongside TRANSLATE-CONST-v2.0. At that moment, role documents authored before CCO existed do **not** instantly become void: each is **grandfathered as operative** until it is individually re-ratified to name the CCO version it implements. A pre-CCO role loses authority only if it is found to *contradict* CCO — never merely for lacking the header. The Database Manager maintains the **migration list** the fourth bullet above requires (which roles have been re-ratified onto CCO v1.0, which are still grandfathered), so the transition is visible and finite rather than open-ended. New role documents authored after ratification do not get the grace period — they must name a CCO version from the start.

---

## 5. Discharge of Obligation 6 (Auditable Record)

Obligations 1–5, 7, and 8 are **behavioral** — a role satisfies them by its own conduct. Obligation 6 is different: it requires **substrate**. A decision record that lives only in a role's head or in a role's private notes is not auditable.

Obligation 6 is therefore discharged **through the Database Manager**: significant decisions land in the recorded artifacts and version history the Database Manager maintains (the knowledge-block records, the governance repository, git history). No role satisfies auditability privately or in its own idiosyncratic format. This makes obligation 6 a standing cross-role dependency on the Database Manager, and is stated here so it is not left implicit in eight separate charters.

**The audit substrate must itself be backed.** Because this section makes the Database Manager's substrate the *sole* compliant home for the auditable record, that substrate is a single point of failure for every role's compliance at once. It is therefore a standing requirement that the audit substrate itself be **durably backed — verified off the machine that holds it**, per the Database Manager's own backup discipline (a copy is not a backup until it has survived off-machine and been shown to restore). Auditability that lives only in an unbacked, local-only store does **not** satisfy Obligation 6: a record that cannot survive loss cannot be relied upon to be reconstructable, which is the whole point of the obligation.

---

## 6. Relationship to Role Charters

A role charter, under CCO, contains:

1. A header naming the CCO version it implements.
2. The role's own identity, mission, and primary question.
3. A short section showing **how the role discharges each of the eight obligations** in its own domain (the implementation).
4. Only the duties, guards, authority, and prohibitions that are **specific to the role** and not already covered by the floor.

If a clause in a role charter merely restates an obligation already in §3, it should be removed from the role and left to the base. Role charters hold the delta, not the duplicate.

---

## 7. Amendment

This document is versioned and ratified by the Architect. Amendments increment the CCO version and trigger deliberate re-ratification of each role onto the new version (§4). The version and status at the top are authoritative.

*Ratified base document CCO v1.0 — authored 2026-07-29; ratified 2026-07-30 (Architect), atomically with TRANSLATE-CONST-v2.0.*

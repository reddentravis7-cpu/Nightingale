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

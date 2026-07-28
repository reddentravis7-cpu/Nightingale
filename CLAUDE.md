 # Translate — Project Context (read this first)

This file exists so a new session on Nightingale doesn't have to
reconstruct the schema, the rules, or the state of things from fragments
in chat history — that's already happened once (GE OEC's Phase 6 schema
was rebuilt from memory because no literal template had ever been
supplied) and it's the exact failure mode this file is meant to close.

## What Translate is

A governed technical reference platform. It models serviceable technical
systems — commands, message formats, manufacturer specifications,
troubleshooting procedures — built through a reviewed, cited pipeline.
It does not model professional judgment where that judgment directly
determines outcomes with meaningful risk of injury, death, or serious
loss. That boundary is structural, not a disclaimer. See
`TRANSLATE_SCOPE_CONSTITUTION.md` for the full reasoning — it is the most
load-bearing document in this repo and everything else defers to it.

## Read in this order

1. `04_Translate/docs/architecture/translate-scope-constitution.md` —
   the scope boundary, non-negotiable
2. `04_Translate/docs/architecture/knowledge-block-model.md` — the
   actual schema (envelope + content shapes: InvokableContent,
   StructuralContent, SpecificationContent; `procedural` and
   `conceptual` are reserved blockType values with no defined shape yet
   — do not invent one without review)
3. `04_Translate/docs/architecture/capability-map-process.md` — the
   Research → Steward → CTO pipeline, phase by phase, plus the resolved
   status of the "Editor" role question
4. `04_Translate/docs/architecture/knowledge-maintenance-plan.md` —
   review/promotion discipline, risk-calibrated verification tiers, the
   trip-wire registry
5. `04_Translate/docs/architecture/lab-equipment-domain-template.md` —
   reusable skeleton for onboarding a new domain, generalized from ACL
   TOP 350
6. `ARCHITECTURE.md` for the general repo philosophy, and
   `04_Translate/docs/decisions/0003-nest-translate-content-under-04-translate.md`
   for the real, current content layout. (0001 proposed a top-level
   `knowledge/` directory without checking the live repo first; 0002
   corrected that to `01_Networking`/`03_Clinical_Integration`, but those
   turned out to be Travis's personal archive folders, not a deliberate
   Translate taxonomy. 0003 is current: everything Translate-engineering
   nests under `04_Translate/`, the one folder actually designated for
   it. Read 0003 — 0001 and 0002 are both marked Superseded.)

Then `PROJECT_STATUS.md` for where each domain actually stands as of the
last confirmed check — treat its timestamp as an expiration date, not a
permanent fact.

## Roles (reuse the role, not the individual)

- **CTO** — schema authority, Phase 6 (Knowledge Block representation),
  cross-domain consistency. Currently Claude.
- **Steward** — Phase 3 (dependency validation) and Phase 5 (concept
  validation). Currently Code on Cisco/HL7/ACL TOP 350; a separate
  Research/Steward pairing on GE OEC One CFD, run as a deliberate test of
  whether the process survives a full team swap.
- **Research** — Phase 1/2 (capability drafting) and Phase 4 (concept
  decomposition), real citations required, no inference to fill gaps.
- **Founder / COO** — product and business direction, not engineering
  judgment calls on scope or schema.

## Non-negotiable standing rules

- No block reaches `reviewStatus: "current"` without `reviewedBy`,
  `dateReviewed`, and a real `url` — this is a hard gate, not a
  convention, added after six Cisco blocks were found `current` on
  placeholder URLs.
- Scope Constitution enforcement is sentence-level, not just
  capability-level — re-check every drafted block against it, not just
  the parent capability once.
- Never state a file is "on the repo," "already fixed," or "already
  sourced" without actually checking the current state of the real repo.
  Sandbox/session work is not repo state until it's verified there.
- A description of a file, or a summary of its contents, is not the
  file. Cross-session handoffs need the literal content pasted or
  written to a shared path — not a paraphrase.
- New content shapes and new blockType values require the same review
  any other shape got (see `KNOWLEDGE_BLOCK_MODEL.md`'s honesty notes on
  `StructuralContent` vs. `SpecificationContent`) — don't add one
  mid-domain-build without flagging it first.
- A domain's own tighter promotion bar (e.g. GE OEC's radiation/
  high-voltage bar) overrides the generic verification-tier test, not the
  other way around.
- Before proposing any structural change to where content lives, check
  the live repo directly first — this project has now caught that
  exact mistake three times in one day (0001, 0002, and the schema
  reconstruction Sheldon/Stewie did from memory).

## Directory map

Per `04_Translate/docs/decisions/0003-nest-translate-content-under-04-translate.md`.
`04_Translate/` is Travis's real, pre-existing, designated Translate
slot inside his personal `00_`–`05_` archive (confirmed directly from
`Translate-Git-Repository.zip`'s real skeleton, not secondhand). All
Translate engineering content lives under it now.
# 0001 — Knowledge Content Placement

**Status:** Superseded by 0002 (2026-07-28)
**Date:** 2026-07-28
**Author:** CTO

## Context

`nightingale-repository-architecture.md` defines `services/` (independently
deployable units) and `libs/` (shared code with no deployment identity of
its own), and explicitly warns that conflating the two is "the single most
common cause of monorepo sprawl."

Translate's Knowledge Block content — the Cisco IOS, HL7 v2/FHIR, ACL TOP
350, and GE OEC One CFD domains, plus the governance documents that define
how that content gets built and reviewed — doesn't fit either category. It
isn't a deployable service. It isn't shared code. It's shared *content*,
produced by a separate Research → Steward → CTO review pipeline, consumed
by whatever services eventually read it (the first concrete example being
the Cisco IOS Quick Reference app, a real `services/` entry once it lands
in this repo).

Without a defined home, this content was heading toward exactly the
sprawl the architecture doc warns about — it had already forked three
independent ways on the GE OEC domain alone before this decision was made,
in a flat, ad hoc structure that predated this ADR.

## Decision

Add a new top-level directory, `knowledge/`, as a sibling to `services/`
and `libs/` — same reasoning as `libs/`, applied to data instead of code:
content with no deployment identity, kept separate so the question "does
this get deployed, or does this get imported/read?" stays forced at
creation time, the same way the services/libs split forces it for code.

```
knowledge/
├── cisco-ios/
├── hl7-fhir/
├── acl-top-350/
└── ge-oec-one-cfd/      (draft only as of this ADR — see its own README)
```

Governance documents (the Scope Constitution, the Knowledge Block schema,
the Capability Map Process, the Maintenance Plan, the domain onboarding
template) go into `docs/architecture/`, per the existing doc's own stated
principle that this folder is for "living descriptions of the current
system... kept in sync with reality" — which is exactly what these are,
as opposed to `docs/decisions/`, which is point-in-time and immutable
once accepted.

`scope_check_array.py` goes into `tools/`, matching the existing
`tools/<internal-cli-or-codegen>/` pattern exactly.

Task-routing and kickoff documents between roles (Research, Steward, CTO)
go into `docs/guides/handoffs/` — process documentation, not architecture.

## Consequences

- Future domains get a defined, unambiguous home from day one instead of
  landing wherever felt convenient in the moment.
- Services that consume this content (the Cisco QRG app, and whatever
  follows it) read from `knowledge/`, never fork a private copy — the
  same discipline `libs/` already enforces for shared code.
- `knowledge/ge-oec-one-cfd/` stays explicitly marked non-canonical until
  its three-way fork is reconciled — this ADR does not resolve that, only
  gives it a correctly-labeled place to live while it's pending.
- `TRANSLATE_5YR_BUSINESS_PLAN.md` is deliberately excluded from this
  repo — it's a business document, not architecture or knowledge content,
  and including it here would be the same category error this ADR exists
  to prevent, just at the top level instead of inside `knowledge/`.

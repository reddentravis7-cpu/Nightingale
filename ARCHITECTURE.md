# Project Nightingale — Repository Architecture

**Author:** Lead Software Architect, Translate Engineering
**Status:** Proposed foundation
**Scope:** Python monorepo, multiple services, scaling from 1 developer to a small team

This document defines the Git repository structure, naming conventions, branching
strategy, and documentation organization for Project Nightingale. It is meant to be
copied into the repo root (e.g. as `ARCHITECTURE.md`) and treated as the reference
until superseded by an ADR.

---

## 1. Design Constraints

Before the structure, the constraints that shaped it:

- **One developer today, a small team soon.** The structure must not impose
  process overhead a solo developer can't sustain, but it must not require a
  rewrite when headcount grows to 3–8 engineers.
- **Multiple services, one repo.** A monorepo was specified. That means the
  structure has to make service boundaries obvious even though everything lives
  in one place, and CI has to be able to build/test only what changed.
- **Python-first.** Conventions follow PEP 8 / packaging norms (`src/` layout,
  `pyproject.toml`) rather than generic or JS-centric conventions.
- **Translate's philosophy — "humans remember concepts, computers remember
  syntax"** — applies to the repo itself. A new engineer (or Travis in six
  months) should be able to infer where something lives without memorizing a
  map.

---

## 2. Top-Level Folder Structure

```
nightingale/
├── README.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .gitignore
├── .editorconfig
├── pyproject.toml              # workspace root config, shared tooling (lint/format/type-check)
├── uv.lock                     # or poetry.lock, depending on tool choice — see §7
│
├── docs/
│   ├── decisions/              # ADRs — one per architectural decision
│   ├── architecture/           # system diagrams, service boundary docs
│   ├── guides/                 # onboarding, how-tos, dev environment setup
│   ├── runbooks/                # operational procedures (incident response, deploy rollback)
│   └── api/                    # generated API references (OpenAPI/redoc output)
│
├── services/
│   ├── <service-name>/
│   │   ├── src/nightingale_<service_name>/
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   ├── Dockerfile
│   │   └── README.md
│   └── ...
│
├── libs/
│   ├── <shared-lib-name>/
│   │   ├── src/nightingale_<lib_name>/
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── ...
│
├── infra/
│   ├── terraform/               # or pulumi/cdk — infrastructure as code
│   ├── docker/                  # shared base images, compose files for local dev
│   └── environments/
│       ├── dev/
│       ├── staging/
│       └── prod/
│
├── deploy/
│   ├── ci/                      # reusable CI job definitions/scripts
│   └── scripts/                 # release, rollback, promotion scripts
│
├── assets/
│   ├── diagrams/                 # architecture diagram source files (draw.io, mermaid, excalidraw)
│   ├── design/                   # UI/UX assets if relevant
│   └── branding/
│
├── tests/
│   └── integration/              # cross-service integration and end-to-end tests
│
└── tools/
    └── <internal-cli-or-codegen>/
```

### Reasoning

**`services/` vs `libs/` split.** Services are independently deployable units
(each with its own `Dockerfile` and lifecycle). Libs are shared code with no
deployment identity of their own — auth helpers, a shared data model, a common
logging setup. Conflating the two is the single most common cause of monorepo
sprawl: a "shared" folder quietly becomes a dumping ground, or a deployable
service imports another service's internals directly instead of through a
published interface. Keeping them physically separate forces the question
"does this get deployed, or does this get imported?" at creation time.

**`src/` layout inside each service/lib.** Python packages built without a
`src/` layer can accidentally import themselves from the working directory
during tests, masking packaging bugs that only surface after publish. The
`src/` layout is the current community-standard fix (recommended by the
Python Packaging Authority) and costs nothing once `pyproject.toml` is set up
correctly.

**Per-service `pyproject.toml` + a root one.** Each service/lib is an
independently installable Python package with its own dependencies — this is
what makes the monorepo scale past one service without every service
inheriting every other service's dependency tree. The root `pyproject.toml`
holds only tooling shared across the whole repo (formatter, linter, type
checker config) so those tools behave identically everywhere. See §7 for the
workspace tool that ties per-service installs together.

**`docs/decisions/` for ADRs, separate from `docs/architecture/`.** Decisions
are point-in-time records of *why* — they should never be edited after
acceptance, only superseded. Architecture docs are living descriptions of the
*current* system and get updated in place. Mixing the two means either the
history gets rewritten (losing the "why") or the current-state docs go stale
(because nobody wants to touch the decisions folder). Separating them lets
each have the update policy it actually needs.

**`tests/integration/` at the root, unit tests inside each service.** Unit
tests belong next to the code they test — that's what makes `pytest` fast to
run per-service in CI (only re-run tests for services that changed). Tests
that span service boundaries can't live inside any one service without
implying a false ownership, so they get a neutral home at the root.

**`infra/` and `deploy/` are separate.** `infra/` is infrastructure as code —
declarative, describes what should exist (a database, a queue, a VPC).
`deploy/` is the mechanism that moves code into that infrastructure — scripts
and CI glue. This mirrors the standard separation between provisioning and
release in mature engineering orgs, and it matters here specifically because
the two change at different rates and are usually owned by different concerns
even when the same person writes both today.

**`assets/` gets its own top-level folder rather than living under `docs/`.**
Diagram *source files* (the `.drawio`, `.mmd`, or `.excalidraw` files) are
distinct from the docs that embed their exported images. Keeping them
separate means designers/engineers can regenerate diagrams without touching
prose, and image assets don't bloat diffs on documentation PRs.

---

## 3. Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Repository name | kebab-case | `nightingale` |
| Directories | kebab-case | `services/auth-service/` |
| Python packages/modules | snake_case | `nightingale_auth_service` |
| Python files | snake_case | `token_validator.py` |
| Test files | `test_` prefix, mirrors source | `test_token_validator.py` |
| Classes | PascalCase | `TokenValidator` |
| Functions/variables | snake_case | `validate_token()` |
| Constants | UPPER_SNAKE_CASE | `MAX_TOKEN_AGE_SECONDS` |
| Branches | `<type>/<short-description>` | `feature/auth-oauth-support` |
| Commits | Conventional Commits | `feat(auth): add refresh token rotation` |
| ADRs | `NNNN-kebab-title.md` | `0007-choose-postgres-for-auth-store.md` |
| Docker images | `nightingale-<service>` | `nightingale-auth-service` |
| Environment files | `.env.<environment>` | `.env.staging` |

### Reasoning

**kebab-case for directories/repos, snake_case for Python identifiers.**
This isn't arbitrary — it's forced by the ecosystem. Python import syntax
can't parse hyphens (`import nightingale-auth` is a syntax error), so package
and module names must be snake_case. Directory and repo names aren't
constrained the same way, and kebab-case is the prevailing convention for
URLs, CLI tool names, and Docker image tags, all of which Nightingale's repo
and directory names will eventually touch. Using kebab-case at the directory
level and snake_case at the package level isn't inconsistency — it's using
the right convention for each layer's actual constraints.

**Conventional Commits.** The payoff isn't stylistic. It's automatable:
changelogs can be generated from commit history, semantic version bumps can
be inferred from commit type (`feat` → minor, `fix` → patch, `!` → major),
and `git log --grep` becomes a usable search tool instead of prose archaeology.
This matters more, not less, as the team grows — a solo developer can hold
the history in their head; a team of five cannot.

**Numbered, immutable ADR filenames.** Numbering preserves chronological
order regardless of how files get renamed or moved, and it gives every
decision a stable, citable identifier (`ADR-0007`) that can be referenced
from code comments, PR descriptions, or Slack without ambiguity.

---

## 4. Branching Strategy

**Recommendation: trunk-based development with short-lived feature branches,
a protected `main`, and release tags — not GitFlow.**

```
main                    (always deployable, protected, requires PR + CI pass)
 ├─ feature/xyz          (branches off main, short-lived, merges back via PR)
 ├─ fix/xyz
 ├─ chore/xyz
 └─ release tags (v0.4.0, v0.4.1, ...) cut from main, not long-lived branches
```

Optional, added only when actually needed:

```
 └─ hotfix/xyz            (branches from a release tag when main has already
                            moved past a shipped version and a patch is needed)
```

### Reasoning

GitFlow (with persistent `develop`, `release/*`, and `hotfix/*` branches) was
designed for a world of infrequent, scheduled releases and larger teams that
needed to stabilize a release branch for days or weeks before shipping. That
overhead has a real cost: every long-lived branch is a merge conflict
generator, and every additional branch type is a rule a solo developer has to
remember and a new hire has to be taught.

Trunk-based development with short-lived branches and a protected `main`
scales in both directions this project actually needs:

- **At one developer**, it's just "branch, commit, PR, merge" — no ceremony.
- **At a small team**, short-lived branches (ideally merged within a day or
  two) minimize integration pain, and `main` being always-deployable means
  CI/CD can ship on every merge rather than batching releases.

The tradeoff being given up is GitFlow's built-in release-stabilization
window. If Nightingale later needs that (e.g. a release that must sit in QA
for a week before going out), the answer is feature flags to decouple merge
from release, not reintroducing `develop`. That's the modern default (used at
Google, Meta's internal Python monorepo tooling, and recommended in the
*Accelerate*/DORA research) and it directly avoids the "long-lived branch"
problem that causes the most painful merges in growing teams.

**Branch protection on `main`** (required PR review once the team is >1,
required CI pass always) is the actual safety mechanism — not branch
topology. This is worth stating explicitly because it's the part that's easy
to skip when it's just one developer, and expensive to retrofit once habits
form without it.

---

## 5. Documentation Organization

```
docs/
├── decisions/       # ADRs — why we chose X over Y, immutable once accepted
├── architecture/     # current-state diagrams, service boundaries, data flow
├── guides/           # onboarding, "how to add a new service", local dev setup
├── runbooks/         # what to do when the auth service is down at 2am
└── api/              # generated, not hand-written — OpenAPI output
```

### Reasoning

Each subfolder has a **different update trigger**, which is the actual
organizing principle:

- `decisions/` updates only when a new decision is made (append-only).
- `architecture/` updates when the system changes (kept in sync with reality).
- `guides/` updates when a process changes (kept in sync with practice).
- `runbooks/` updates after an incident, ideally as a blameless postmortem action item.
- `api/` updates automatically, on every build, from code — it should never
  be hand-edited, which is why it's separated from the docs a human writes.

Splitting by update trigger rather than by topic prevents the single failure
mode most engineering docs suffer: a "docs" folder that grows correct content
early and becomes silently wrong later because nobody knows which parts are
safe to edit and which parts are historical record.

Every service and lib also gets its **own README** (see §2) for
package-local documentation — what this service does, how to run just this
service, its own dependencies. The root `docs/` is for anything that spans or
sits above a single service.

---

## 6. README Structure

Root `README.md` (and, in miniature, each service/lib `README.md`):

```markdown
# Project Nightingale

One-sentence description of what this is and who it's for.

## Status
[build badge] [coverage badge] [version badge]

## Overview
2–4 sentences: what problem this solves, how it fits into Translate Engineering.

## Architecture
Link to docs/architecture/ and a single high-level diagram, inlined or linked.

## Getting Started
- Prerequisites
- Install
- Run locally
- Run tests

## Repository Structure
Short annotated tree — link out to ARCHITECTURE.md for the full rationale.

## Development Workflow
Branching, commit convention, how to open a PR — link to CONTRIBUTING.md.

## Deployment
How and where this ships, link to docs/runbooks/ for operational detail.

## Contributing
Link to CONTRIBUTING.md.

## License
## Ownership / Contact
```

### Reasoning

The ordering follows a **decreasing-frequency-of-need** principle: a reader
in their first five minutes needs "what is this" and "how do I run it," not
deployment internals. A README that leads with architecture diagrams before
saying what the project does is optimizing for the author's mental model, not
the reader's. Putting "Getting Started" early and "Ownership/Contact" last is
deliberate — most readers need the former immediately and the latter only
occasionally.

Per-service READMEs matter more, not less, as the team grows: they're what
lets an engineer work on `auth-service` without reading the whole monorepo's
documentation first. The root README should never try to duplicate them —
it links out.

---

## 7. Tooling Notes (non-binding, flagged for a future ADR)

A few choices below the folder-structure level will affect how cleanly this
structure works in practice, and are worth deciding deliberately rather than
by default:

- **Workspace/dependency management.** Python's packaging ecosystem doesn't
  have first-class monorepo workspace support the way `npm`/`pnpm`/`cargo`
  do. `uv` (Astral) now supports workspaces natively and is the current best
  fit for a multi-package Python monorepo; Poetry's workspace support is
  weaker as of this writing. This is worth its own ADR before the second
  service is added, not decided implicitly by whichever tool the first
  service happens to use.
- **CI path filtering.** With multiple services in one repo, CI should build
  and test only what changed (e.g. via `paths:` filters in GitHub Actions),
  or CI time will grow linearly with the number of services regardless of
  how small each change is.
- **Versioning granularity.** Decide per-service versioning (each service has
  its own version/tag) vs. whole-repo versioning (one version for
  everything) before the second service ships — retrofitting is disruptive.
  Per-service versioning is recommended given independent deployability, but
  this deserves its own ADR with the tradeoffs written out.

These are flagged rather than settled here because each is a real
architectural decision with tradeoffs specific to Nightingale's actual
services — exactly the kind of decision `docs/decisions/` exists to record.

---

## 8. Summary of Recommendations

| Decision | Recommendation | Primary reason |
|---|---|---|
| Repo topology | Monorepo, `services/` + `libs/` split | Independent deployability without dependency sprawl |
| Package layout | `src/` layout per package | Prevents import-path packaging bugs |
| Branching | Trunk-based, short-lived branches, protected `main` | Scales from 1 to N without process rewrite |
| Commit style | Conventional Commits | Enables automated changelogs/versioning |
| ADRs | Numbered, immutable, in `docs/decisions/` | Preserves the "why" without blocking doc updates |
| Docs organization | Split by update trigger, not topic | Keeps docs from silently going stale |
| README | Root = orientation + links; per-service = operational detail | Matches reader's actual first-five-minutes needs |

This structure is intentionally conservative: nothing here requires
Nightingale to have more than one service today, but nothing here needs to be
undone when it has five.

# Engineering Standards — Translate Engineering

**Status:** Active
**Applies to:** All Translate Engineering repositories (reference implementation: Project Nightingale)

This document defines how we write, review, and ship code. Each standard
includes the reasoning behind it so it can be applied to situations it
doesn't explicitly cover, not just followed by rote. When a rule and a
real situation conflict, raise it — these standards should evolve via ADR,
not be silently ignored.

---

## 1. Code Organization

- Organize by **domain/feature**, not by technical layer (avoid a top-level
  split into `models/`, `views/`, `utils/` across the whole codebase).
- Each service or library is self-contained: its own dependencies, tests,
  and README. No service reaches into another service's internals — only
  through its published interface (API call, or an imported `libs/` package).
- Shared code goes in `libs/` only once it's used by two or more services.
  Don't pre-extract a shared library for a hypothetical second consumer.

**Why:** Layer-based organization (`models/`, `utils/`, `helpers/`) scales
badly — `utils/` becomes a junk drawer, and understanding one feature
requires jumping across five folders. Domain-based organization means
"everything about auth" lives in one place, which is what an engineer is
actually looking for. The two-consumer rule for `libs/` prevents premature
abstraction — the most expensive kind, because the wrong abstraction is
harder to remove than no abstraction.

---

## 2. Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Packages/modules | snake_case | `token_validator.py` |
| Classes | PascalCase | `TokenValidator` |
| Functions/variables | snake_case | `validate_token()` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| Private members | leading underscore | `_internal_cache` |
| Booleans | `is_`/`has_`/`can_` prefix | `is_authenticated` |

**Why:** These follow PEP 8, so they cost nothing to learn (every Python
engineer already knows them) and every linter enforces them for free. The
boolean prefix convention isn't PEP 8, but it's worth adding explicitly:
`is_`/`has_`/`can_` makes a variable's type legible at the call site without
opening its definition — `if authenticated:` is ambiguous, `if
is_authenticated:` is not.

---

## 3. File Naming

- Files: `snake_case.py`, one primary class/concept per file where practical.
- Test files: `test_<module>.py`, mirroring the source file it tests.
- Config files: `<purpose>.<environment>.<ext>`, e.g. `settings.staging.yaml`.
- No abbreviations that aren't already domain-standard (`cfg` is fine,
  `mgr` is not).

**Why:** A test file name that mirrors its source file is what lets `pytest
test_token_validator.py` be guessable rather than looked up, and what lets
tooling (coverage reports, IDEs) pair source and test automatically.
Avoiding non-standard abbreviations is about the "engineer reads this in
three years" test — `mgr` saves four keystrokes now and costs a moment of
confusion every future read.

---

## 4. Documentation Expectations

- **Every service/lib** has a README covering: what it does, how to run it,
  how to test it, and its own dependencies (see Nightingale repo architecture
  for the full template).
- **Every public function/class** gets a docstring stating what it does, its
  parameters, return value, and exceptions it can raise — not a restatement
  of its name.
- **Every non-obvious decision** gets a comment explaining *why*, not *what*.
  If the code needs a comment to explain what it does, prefer rewriting the
  code to be clearer first.
- **Every architectural decision** gets an ADR in `docs/decisions/`.

**Why:** Docstrings on public interfaces are the contract other engineers
(and future you) rely on without reading the implementation — this is what
makes a codebase navigable without a guided tour. "Why" comments exist
because code always shows what happens; only a comment can preserve why an
alternative was rejected, which is exactly the information that's expensive
to reconstruct later (e.g. "we don't use library X here because it doesn't
support async" saves a future engineer from re-discovering that the hard
way).

---

## 5. Git Commit Message Conventions

Follow **Conventional Commits**:

```
<type>(<scope>): <short summary>

<optional body — explain why, not what>

<optional footer — breaking changes, issue references>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`.

```
feat(auth): add refresh token rotation
fix(billing): correct rounding error in invoice totals
docs(readme): clarify local dev setup steps
```

**Why:** Structured commit types make changelogs and version bumps
generatable from history instead of hand-written (`feat` → minor version,
`fix` → patch, `BREAKING CHANGE` footer → major). This matters more as the
team grows: a solo developer can reconstruct "what happened last sprint"
from memory; a team of five needs the log to do it for them.

---

## 6. Branch Naming

```
<type>/<short-description>
```

```
feature/auth-oauth-support
fix/billing-rounding-error
chore/upgrade-dependencies
docs/update-runbook
```

**Why:** Matching branch-type prefixes to commit types keeps one mental
model across both, and lets CI apply different rules by branch type (e.g.
`fix/*` branches can skip a staging soak that `feature/*` branches require).
See the Nightingale repo architecture doc for the full branching strategy
(trunk-based, short-lived branches, protected `main`).

---

## 7. Testing Philosophy

- **Test behavior, not implementation.** A test should survive a refactor
  that doesn't change what the code does.
- **Unit tests** for logic-heavy code (business rules, calculations,
  validation) — fast, no network/DB, colocated with the source.
- **Integration tests** for anything that crosses a service boundary or
  touches a real dependency (DB, queue, external API) — fewer of these,
  run in CI, live in the root `tests/integration/`.
- **No target coverage percentage.** Coverage is a diagnostic (it finds
  *untested* code), not a goal (100% coverage doesn't mean *well-tested*
  code). Require tests for new logic and bug fixes; don't chase a number.
- Every bug fix ships with a regression test that fails without the fix.

**Why:** Coverage-percentage targets reliably produce tests that assert
trivial things just to move the number, which is worse than no metric at
all because it creates false confidence. Testing behavior instead of
implementation is what keeps the test suite from becoming a tax on
refactoring — tests that break every time you rename a private method are
actively hostile to the "build systems that can evolve" principle.

---

## 8. Logging Philosophy

- Log **events, not narration.** `"user_login_failed"` with structured
  fields (`user_id`, `reason`), not `"Uh oh, login failed for this guy"`.
- Use structured logging (key-value or JSON), never string-formatted
  messages that require regex to parse later.
- Log levels mean something specific:
  - `DEBUG` — development-time detail, off in production by default.
  - `INFO` — normal operational events worth a permanent record.
  - `WARNING` — unexpected but handled; worth a human glancing at it.
  - `ERROR` — something failed and needs attention.
  - `CRITICAL` — the service itself is compromised.
- Never log secrets, tokens, passwords, or full PII payloads.

**Why:** Structured logs are what make logs queryable at 2am during an
incident instead of grep-and-pray. Disciplined log levels are what make
alerting on `ERROR`/`CRITICAL` meaningful — if `WARNING` is used for routine
events, engineers learn to ignore warnings, which is how real ones get
missed. The secrets rule isn't a style preference — it's a compliance and
breach-blast-radius issue: logs typically have looser access control and
longer retention than the systems that generated them.

---

## 9. Error Handling

- **Fail loudly in development, gracefully in production.** Don't swallow
  exceptions silently in either.
- Catch exceptions at the boundary where you can actually do something
  about them (retry, fallback, user-facing message) — not immediately at
  the point they're raised just to log and re-raise.
- Use specific exception types, not bare `except Exception`. If you must
  catch broadly (e.g. at a top-level request handler), log the full
  exception and re-raise or convert to a defined error response — never
  swallow.
- Distinguish **expected failures** (invalid user input, a resource not
  found — handle as normal control flow) from **unexpected failures** (a
  bug, an infrastructure outage — these should be loud, alerted, and
  visible).

**Why:** Broad `except Exception: pass` blocks are the single most common
cause of "the system was silently broken for two weeks and nobody knew."
Catching at the point where you can act (rather than at the point of
failure) keeps error-handling logic co-located with the decision it
informs, instead of scattered as defensive noise through every function
call.

---

## 10. Configuration Management

- Configuration is **environment-specific values only** (URLs, feature
  flags, timeouts) — never business logic branching on environment name.
- Secrets never live in code or config files committed to the repo. Use a
  secrets manager (environment-injected at deploy time); `.env.example`
  documents required keys with placeholder values, `.env` is gitignored.
- Config is validated at startup (fail fast if a required value is missing
  or malformed) — not discovered missing three requests into production
  traffic.
- One config schema per service, not a shared global config object every
  service partially uses.

**Why:** Business logic that branches on `if environment == "prod"` is a
maintenance hazard — it means dev and prod are running meaningfully
different code paths, which defeats the purpose of testing in dev at all.
Startup validation converts a class of production incident ("missing env
var causes a 3am failure under load") into a deploy-time failure that's
caught before traffic ever hits it.

---

## 11. Security Considerations

- **Never commit secrets.** Enforce with a pre-commit secret scanner, not
  just a policy.
- **Validate and sanitize all external input** — user input, API payloads,
  file uploads, query parameters — at the boundary where it enters the
  system.
- **Least privilege by default:** service accounts, database roles, and API
  scopes get only the access they need, not broad defaults "to be safe."
- **Dependencies are attack surface.** Keep them current; use automated
  dependency vulnerability scanning in CI.
- **Authentication and authorization are never rolled by hand** — use
  established, audited libraries.

**Why:** Secret-scanning as an automated gate exists because policy alone
fails under deadline pressure — the goal is to make the safe path the easy
path. Input validation at the boundary (rather than scattered checks deeper
in the call stack) means every downstream function can trust its inputs,
which is both safer and simpler. "Don't roll your own auth" isn't
conservatism for its own sake — auth vulnerabilities are subtle, the
libraries that exist have been attacked and hardened for years, and the
asymmetry between the cost of writing it yourself and the cost of getting
it wrong is too large to justify.

---

## 12. Code Review Checklist

Before approving a PR, the reviewer confirms:

- [ ] The change does what the PR description says it does.
- [ ] Tests exist for new logic and bug fixes, and actually fail without the fix.
- [ ] No secrets, credentials, or debug code left in.
- [ ] Naming and structure follow this document.
- [ ] Error handling is present at the right boundary (§9).
- [ ] Logging is structured and doesn't leak sensitive data (§8).
- [ ] Public functions/classes have docstrings.
- [ ] No unexplained "why" — non-obvious logic has a comment.
- [ ] Breaking changes are flagged and documented.
- [ ] The change is scoped to one concern (not bundled with unrelated fixes).

**Why:** A checklist exists because review quality otherwise depends on
whoever happens to be reviewing and how much time they have — a checklist
makes the minimum bar consistent regardless of reviewer or deadline
pressure. The "scoped to one concern" item is worth calling out
specifically: bundled PRs are the most common reason reviews get rubber-
stamped, because reviewing five unrelated changes properly takes five times
the effort reviewers rarely have.

---

## 13. Pull Request Checklist

Before requesting review, the author confirms:

- [ ] PR description states what changed and why (not just what).
- [ ] Linked to the relevant issue/ticket, if one exists.
- [ ] CI passes (lint, type check, tests).
- [ ] Commit messages follow Conventional Commits (§5).
- [ ] Branch is up to date with `main`.
- [ ] No unrelated changes bundled in.
- [ ] New/changed config documented (`.env.example`, README).
- [ ] Screenshots or examples included for user-facing changes.

**Why:** This checklist front-loads work onto the author instead of the
reviewer — catching a missing test or an out-of-date branch before review
starts is strictly cheaper than catching it during review, where it costs
two people's context-switch instead of one.

---

## 14. Technical Debt Management

- Debt is tracked, not hidden. A shortcut taken under deadline pressure gets
  a `# TODO(nightingale-123):` comment linked to a tracked issue — not a
  silent gap.
- Every tracked debt item states: what was skipped, why, and what the real
  fix looks like.
- Debt is reviewed on a regular cadence (e.g. monthly), not left to
  accumulate until it blocks a release.
- Distinguish **deliberate debt** (a conscious tradeoff to ship faster, with
  a plan to revisit) from **accidental debt** (drift from these standards
  that should just be fixed, not tracked as a permanent tradeoff).

**Why:** Untracked debt is invisible until it's an emergency — tracking it
converts "we'll deal with it eventually" into a prioritizable backlog item
with an owner. The deliberate/accidental distinction matters because
treating every standards violation as "acceptable debt" erodes the
standards themselves; accidental debt should be fixed in the next
touch of that code, not permanently grandfathered in.

---

## Summary

| Area | Core Rule |
|---|---|
| Code organization | Organize by domain, not layer; extract shared libs only at 2+ consumers |
| Naming | PEP 8 + explicit boolean prefixes |
| File naming | snake_case, tests mirror source |
| Documentation | README per service, docstrings on public APIs, "why" comments, ADRs for decisions |
| Commits | Conventional Commits |
| Branches | `type/short-description`, matches commit types |
| Testing | Behavior over implementation; no coverage-percentage targets |
| Logging | Structured, meaningful levels, never log secrets |
| Error handling | Catch where you can act; distinguish expected vs. unexpected failures |
| Configuration | Environment values only, validated at startup, secrets never in code |
| Security | Validate at the boundary, least privilege, automated scanning, no hand-rolled auth |
| Code review | Checklist-driven, consistent minimum bar |
| Pull requests | Author front-loads the checks reviewers would otherwise catch |
| Technical debt | Tracked with an owner, reviewed on a cadence, not silently accepted |

These standards are a floor, not a ceiling — they exist to keep the codebase
maintainable as Translate Engineering grows, and they should be revisited via
ADR when they stop serving that purpose.

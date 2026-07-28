# Product Architecture — Translate Engineering

**Status:** Foundational — intended to guide product and software architecture
decisions for years, not quarters.
**Scope:** Product architecture only. This document deliberately excludes
implementation details (tech stack, repo structure, infrastructure) — those
are covered elsewhere. This document answers *what Translate is and why it's
built the way it's built*, so that implementation can change freely without
the product's identity drifting.

---

## 1. What Translate Is

Translate is the engineering workspace professionals keep open throughout
their workday — not a reference site engineers visit, but a persistent
environment they work inside.

Its purpose is to **compress technical knowledge into practical capability.**
Most engineering resources — documentation sites, Stack Overflow, man pages,
scattered internal wikis — store knowledge organized around *what the
information is*. Translate organizes knowledge around *what the engineer is
trying to accomplish*. The distinction matters: an engineer rarely wants "the
`kubectl` documentation." They want "how do I roll back this deployment
safely, right now." Translate is built to answer the second kind of question
directly, using the first kind of knowledge as raw material.

---

## 2. Who It Serves

**Primary user: the working engineer**, across experience levels and stacks.
Translate is deliberately not scoped to one language, framework, or
specialty — the problem it solves (time lost to syntax and context-switching
instead of problem-solving) is universal across engineering disciplines.

Within that primary audience, Translate serves three overlapping needs that
grow with the user's context:

- **The individual contributor**, who needs speed and confidence in the
  moment — the dominant use case today, and the one the product must never
  compromise in pursuit of the other two.
- **The team**, who needs shared capability and consistency — the same
  workflow, documented the same way, available to every engineer on the
  team rather than living in one person's head or one person's browser
  history.
- **The engineering organization**, who needs this capability to compound —
  institutional knowledge that survives turnover, onboarding that doesn't
  start from zero, standards that are actually followed because they're
  where the work happens.

This is a deliberate progression, not three separate products: value at the
individual layer is what earns adoption; the team and org layers are what
that adoption naturally grows into. Product decisions should be evaluated
against the individual layer first — if a feature doesn't make one
engineer's day better, no amount of team or org value built on top of it
will be durable.

---

## 3. Primary Problems It Solves

1. **Syntax burden crowds out problem-solving.** Engineers spend real,
   recurring time recalling or looking up commands, flags, and boilerplate
   they've already learned once. That time is pure overhead — it doesn't
   build understanding, it just re-fetches it.
2. **Knowledge is fragmented across disconnected tools.** Documentation,
   references, diagramming, learning material, and automation typically live
   in separate tools with separate mental models, so using them together
   requires the engineer to be the integration layer.
3. **The distance between intent and execution is too long.** Knowing
   *conceptually* what needs to happen and being able to *execute* it are
   treated as separate steps, with a manual translation step between them
   that's slow and error-prone.
4. **Confidence, not just correctness, is often missing.** Engineers can
   often find *an* answer; they can't always tell if it's the *right* answer
   for their situation. Uncertainty itself is a productivity cost.

Translate exists to collapse these into one workspace where the gap between
"I know what I want to do" and "it's done" is as short as possible.

---

## 4. Core Product Philosophy

> **Humans should remember concepts. Computers should remember syntax.**

This is the single organizing idea behind every feature decision. Concepts —
what a load balancer does, why idempotency matters, when to reach for a
queue versus a direct call — are durable and worth an engineer's memory.
Syntax — the exact flags, the exact function signature, the exact YAML
schema — is volatile, version-specific, and not worth memorizing. A product
built on this philosophy should always be moving syntax-level burden onto
the system and leaving concept-level judgment with the human, never the
reverse.

Two corollaries follow directly from this:

- **Organize around intent, not around documentation structure.** Every
  system in Translate should be reachable by describing what you're trying
  to do, not only by knowing what it's officially called.
- **Free-first, not free-limited.** The product earns adoption by being
  useful enough that engineers choose it and recommend it, not by
  withholding core functionality until payment. Premium capability *extends*
  professional workflows (team features, scale, deeper automation) — it
  never *restricts* functionality an individual engineer needs to do real
  work. This is a product-architecture constraint, not just a pricing
  decision: it means core systems must be designed to be genuinely complete
  at the free tier, with premium as an additional layer rather than a
  crippled-then-unlocked one.

Every feature should be evaluated against one question: **does this help an
engineer accomplish meaningful work more effectively?** Features that add
surface area without shortening the intent-to-execution distance are scope
creep, regardless of how impressive they are individually.

---

## 5. The Major Software Systems

Translate is composed of eight systems. Each is described here by the job it
does for the user — not by how it's built.

| System | Job to be done |
|---|---|
| **Capability Libraries** | The organizing spine: curated, reusable units of "how to accomplish X," addressable by intent rather than by tool name. |
| **Engineering References** | The ground-truth layer: accurate, current technical facts (syntax, APIs, specs) that everything else draws on. |
| **Interactive Tools** | Where knowledge becomes action — calculators, converters, generators, validators the engineer can execute against directly. |
| **AI Assistance** | The connective and conversational layer — interprets intent, retrieves and synthesizes from the other systems, and can act on the engineer's behalf. |
| **Documentation** | Where an engineer's own work gets captured — the outputs of using Translate become durable, shareable records. |
| **Diagramming** | Visual reasoning about systems — architecture, flows, relationships — integrated with the same underlying capability data, not a disconnected drawing tool. |
| **Learning Resources** | The on-ramp for concepts the engineer doesn't yet have — building the durable understanding the philosophy asks humans to hold. |
| **Workflow Automation** | Where a repeated sequence of the above stops being repeated — the compounding layer that turns "I know how" into "it just happens." |

---

## 6. How These Systems Interact

The systems are not independent product silos with a shared login — they
form a single loop, and the product architecture should protect that loop as
new systems or features are added:

```
   Intent (what the engineer is trying to accomplish)
          │
          ▼
   Capability Libraries  ──── organizes and routes intent
          │
          ├──► Engineering References  (ground truth, pulled in as needed)
          ├──► Interactive Tools        (executable action)
          ├──► Diagramming              (visual reasoning)
          ├──► Learning Resources       (when understanding, not just action, is needed)
          └──► Workflow Automation      (when the action recurs)
          │
          ▼
   AI Assistance ── the connective layer engineers can enter from,
                     sitting across every system above, retrieving from
                     References, invoking Tools, generating Diagrams,
                     and surfacing relevant Capability Library entries
          │
          ▼
   Documentation ── captures what was produced, feeding back into
                     Capability Libraries as reusable knowledge
```

Three interaction principles follow from this loop and should constrain
future system design:

- **Capability Libraries are the entry point, not one system among equals.**
  An engineer arriving with intent should land on a capability, not be asked
  to first pick which of the eight systems they need — that choice is the
  product's job, not the user's.
- **AI Assistance is connective tissue, not a ninth silo.** Its role is to
  reduce the friction of moving between the other systems, not to become a
  parallel product that happens to also know about them. Any AI feature that
  can't cite which underlying system(s) it drew from is a signal the loop
  has been broken.
- **Documentation closes the loop back into Capability Libraries.** Work an
  engineer produces using Translate should be able to become a capability
  another engineer benefits from — this is the mechanism by which the
  product compounds in value for a team, not just an individual.

---

## 7. Intended User Experience

- **Always-open, not visited.** Translate should feel like an environment an
  engineer keeps in a tab all day, the way they keep their terminal or IDE
  open — not a site they navigate to when stuck.
- **Enter through intent, arrive at capability.** The default interaction
  should feel like describing a goal and being handed a path to it, not
  like searching a document index.
- **Low ceremony, high trust.** Every additional click, mode switch, or
  context-loading step between intent and execution is a defect to be
  designed out. At the same time, speed must never come at the cost of
  accuracy — an engineer who loses trust in Translate's answers stops using
  it entirely, so correctness is the one dimension the experience should
  never trade away for friction reduction.
- **Consistent mental model across systems.** Moving from a Reference to a
  Tool to a Diagram should feel like moving within one workspace, not like
  switching products. A user who has learned how one system behaves should
  already understand most of how the others behave.
- **Depth on demand, simplicity by default.** The first answer should be the
  direct one; deeper explanation, alternatives, or edge cases should be
  available a layer down, not forced into the first response.

---

## 8. Design Principles

These apply to every system and every feature, present or future:

1. **Reduce cognitive load.** If a feature adds something the engineer has
   to remember, hold in working memory, or reconcile across screens, that's
   a cost that needs to be justified by a larger benefit.
2. **Shorten the distance between intent and execution.** This is the
   product's central metric of value, even where it isn't formally measured.
   Every new feature should be able to state what it shortens.
3. **Increase engineer confidence, not just provide an answer.** Correct but
   unconvincing is a partial failure. The product should make its
   reasoning, sourcing, or certainty visible enough that the engineer trusts
   the output rather than re-verifying it elsewhere.
4. **Organize around what, not where it lives.** Product structure should
   never leak internal categorization onto the user — the user's mental
   model is "what am I trying to do," and the information architecture
   should meet them there.
5. **Consistency compounds; novelty per-feature does not.** A new pattern
   introduced in one system has a cost across all eight. Prefer extending an
   existing interaction pattern over inventing a new one, unless the new
   problem genuinely can't be solved by the existing pattern.
6. **Free-first is a design constraint, not a business afterthought.** Every
   core system should be conceived as complete and useful on its own before
   any premium layer is designed on top of it.

---

## 9. Scalability Considerations

Scalability here means the product's ability to keep serving its purpose as
its user base, its knowledge base, and its usage patterns grow — not
infrastructure capacity.

- **From individual to team to organization**, as described in §2, without
  fragmenting into separate products. Team and org features should be
  additive views over the same Capability Libraries and Documentation an
  individual already uses — shared visibility and governance layered on,
  not a parallel system built for "enterprise."
- **Knowledge base growth without quality decay.** As Capability Libraries
  and References grow, the risk isn't running out of room — it's accuracy
  and relevance decaying as volume increases. The product needs a
  deliberate answer to *how a capability entry stays correct as the
  technology it describes changes*, not just a mechanism for adding more
  entries. This is a curation and lifecycle problem, and it should be
  treated as core product surface, not a backend concern.
- **Personalization versus shared truth.** As usage scales, the product will
  face pressure to personalize (an engineer's preferred stack, a team's
  conventions) while keeping a single shared, trustworthy knowledge base
  underneath. Personalization should shape *what surfaces first*, never
  *what's true* — the underlying reference content should not fork per
  user.
- **Breadth of domain over time.** The product starts scoped to software
  engineering broadly, but "engineer" is not a fixed boundary — the same
  intent-oriented model could extend to adjacent technical disciplines.
  Scalability here means the Capability Library model should not assume
  software-engineering-specific structure so deeply that extending to a new
  domain requires a redesign rather than an extension.
- **AI Assistance scaling with, not ahead of, the other systems.** As AI
  capability grows, the temptation will be for it to answer directly from
  general knowledge rather than routing through Translate's own References
  and Capability Libraries. That would quietly disconnect the "loop" in §6
  and erode the product's actual differentiation, which is curated,
  trustworthy, intent-organized capability — not a general-purpose chatbot.
  AI Assistance should scale by getting better at using Translate's systems,
  not by needing them less.

---

## 10. Future Expansion

The following are directions consistent with this architecture, not
commitments — they're recorded so future decisions can be checked against
whether they extend this foundation or fight it:

- **Team and organizational knowledge layers**: shared capability libraries
  scoped to a team or company, private extensions of the public library
  rather than a separate system.
- **Deeper workflow automation**: moving from "automate a sequence I do
  often" toward automation that's proactively suggested based on observed
  patterns — always within the free-first, trust-first constraints in §4
  and §7.
- **Expansion beyond initial technical domains**: adjacent technical roles
  or disciplines that share the same underlying need (concept vs. syntax
  burden), evaluated against whether the existing Capability Library model
  extends naturally or requires a fork.
- **Deeper integration with the tools engineers already use**, so Translate
  remains the workspace they keep open rather than one more tab competing
  with their existing environment.
- **Becoming the default professional workspace**, in the sense described
  in §1 — not by adding unrelated features, but by continuing to compress
  more of the distance between intent and execution across a growing
  surface of engineering work.

Any future system or feature should be able to answer three questions drawn
directly from this document: which of the eight systems does it belong to
(or does it justify a ninth); does it shorten the path from intent to
execution; and does it hold up under the free-first constraint. A proposal
that can't answer these isn't ready for architecture — it's ready for
discussion.

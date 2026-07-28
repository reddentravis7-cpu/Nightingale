# Translate Scope Constitution v1.0

**Status:** Foundational. Applies to every domain, present and future — not
a rule specific to ACL TOP 350. No domain charter, capability map, or
Knowledge Block may expand scope into the excluded territory below. Where
a scope question is ambiguous, default to exclusion, not inclusion.

**What this document does not resolve:** this constitution governs
patient/animal/property-harm judgment scope only. It says nothing about
intellectual-property or copyright risk in cases where content is derived
from a manufacturer's own copyrighted material (e.g. building structured
content from a vendor's manuals and presenting that product back to the
same vendor). That's a separate risk category with a separate failure
mode, and it needs its own answer from someone with actual IP/legal
competence — this document being adopted doesn't close that question.

---

## The rule, stated plainly

**Translate models serviceable technical systems. It does not model
professional judgment where that judgment directly determines actions
carrying meaningful risk of injury, death, or serious loss to people,
animals, or significant property.**

The line is judgment, not licensure. There are unlicensed domains where
bad information causes real harm, and licensed domains where most of the
actual work is procedural. "Is this person credentialed" is the wrong
test; "does this content directly decide an action that could hurt
someone or something valuable" is the right one.

We are not doctors. Not veterinarians. Not anything adjacent. If a piece
of content could plausibly be the deciding input behind a decision that
hurts someone, hurts an animal, or destroys something of real value,
Translate does not produce that content — not with a disclaimer attached,
not scoped down, not at all. The boundary is structural, not a warning
label on content that otherwise exists.

## The product, stated plainly

**Translate compiles and organizes real, sourced information about how
systems behave.**

Not AI, not documentation, not expertise — a well-organized compilation
of what's been confirmed and sourced, held to a discipline (source
classes, citations, review status, promotion gates) precisely because
there's no expert judgment underneath it to catch its own mistakes. Every
other rule in this document follows from taking that sentence seriously.

## Why this is a scope decision, not a disclaimer decision

A disclaimer says: *here is clinical content; don't use it clinically.*
That's a weaker position than it looks, because the content still exists,
still reads as authoritative, and still carries the risk that someone
uses it the wrong way regardless of the label.

The stronger position: *this content was never produced in the first
place, because producing it isn't what Translate does.* Nothing to
misuse, because nothing decision-relevant to injury or loss was ever
written down.

## The reframe: system, not subject

Working example — ACL TOP 350 CTS:

**Excluded (subject-matter judgment, belongs to the licensed
professional):**
diagnosis, treatment selection, patient management, interpretation of
laboratory values, clinical recommendations, anything answering "what
does this result mean for this patient."

**In scope (the serviceable system underneath):**
electromechanical behavior, software behavior, network and LIS
communication, workflow mechanics, maintenance, diagnostics, calibration
and QC procedure, error/alarm lifecycle, service history, operational
readiness — the actual day-to-day questions a field service engineer
asks: why is QC failing, why won't the sample aspirate, why is the
barcode unreadable, why did calibration invalidate, why isn't the LIS
acknowledging, why is the pipettor throwing an error.

Those are engineering questions about the system, not clinical questions
about a patient. That distinction is the whole boundary — and it's worth
being precise about what Translate actually is here: not an expert in the
system either. Translate compiles and organizes real, sourced information
about how the system behaves. It doesn't hold independent judgment,
doesn't catch its own errors through expertise, and doesn't get to borrow
authority from sounding confident. The discipline (source classes,
citations, review status, promotion gates) exists precisely because
there's no expert underneath to fall back on if the compilation is wrong.
That's also why the injury/harm boundary can't be softened by "we're
pretty good at this" — being a well-organized compiler, even a very good
one, is not the same as being qualified to be the last word on something
that could hurt someone.

## Generalized beyond healthcare

This isn't a healthcare-specific carve-out — it's a general principle
that happens to apply loudly to healthcare. It extends the same way to
any domain where getting content wrong could plausibly cause:

- injury or death to a person
- injury or death to an animal
- serious damage to something of real value (safety-critical
  infrastructure, high-value physical assets, irreversible loss)

Veterinary systems, industrial safety systems, anything where Translate's
content would sit upstream of a consequential real-world decision — same
rule applies. The test is not "is this a medical domain," it's "could this
specific piece of content be the reason someone or something gets hurt."

## How this binds domain charters

Every future Research Charter must state explicitly which capabilities
sit in the excluded zone and confirm none of them are being modeled. This
is not optional boilerplate — it's the same discipline as citing a source
class for every claim. A charter that's silent on this isn't compliant by
omission; silence defaults to exclusion until stated otherwise.

If a capability is ambiguous — sits near the boundary, like result
governance in the ACL TOP 350 charter (reference ranges, abnormal flags,
result release) — the resolution is to describe the software/workflow
mechanics only (what triggers a flag, what state gates release) and
exclude the significance of the value itself (what the flag means for the
patient).

**When the boundary between technical system behavior and professional
judgment cannot be drawn clearly, Translate defaults to exclusion until
the boundary can be demonstrated.** Not included-with-caution, not
included-with-a-flag — excluded, until whoever's reviewing it can show
where the line actually sits.

**Worked example, so Research and Steward have a concrete pattern to
apply:** the analyzer displays "Alarm 327: Calibration Invalid." In scope:
what causes the alarm, what subsystem generated it, what maintenance
action clears it, what state transitions follow. Still in scope: a
factual statement that the system itself flags results generated during
an invalid calibration window with a particular status in its own audit
log — that's a description of what the software does. Out of scope: "results
generated since the failed calibration should not be used" — that's a
laboratory quality-policy judgment about consequences for patient care,
not a description of system behavior, and it's excluded by the same test
whether or not it happens to be true.

**This rule doesn't soften under commercial pressure.** If a customer
asks Translate to cross this line, the answer is no, not "let's discuss
scope." A constraint that only holds until someone asks nicely isn't a
constitutional rule — it's a preference. This one is meant to still be
true ten years from now, the same way Git refuses to rewrite published
history by default: occasionally inconvenient in the moment, and exactly
the thing to be glad of later.

## Enforcement is sentence-level, not just capability-level

Charter-level capability declaration is the first filter, not the only
one. Declaring "error/alarm lifecycle" in scope doesn't make everything
drafted under it automatically compliant — the Alarm 327 example exists
specifically because the boundary can run through a capability, not just
around it. A single `fieldNotes` or `description` sentence can drift from
system behavior into professional judgment inside an otherwise-legitimate,
in-scope block, without the block itself ever declaring anything
out-of-bounds.

Steward review is expected to re-apply the exclusion test at the sentence
level to every drafted block — not just confirm the parent capability was
cleared at the charter stage. Capability-level declaration filters what
Research is allowed to attempt; it does not filter what actually ends up
written inside an approved capability. An unstated answer to "was this
re-checked at the sentence level" gets treated the same way an unstated
source version gets treated: not assumed compliant, flagged until shown
otherwise.

## What this buys, beyond safety

A cleaner, more honest product. Service, integration, communications,
maintenance, reliability, operational readiness — that's a real, large,
genuinely useful domain to compile well, and compiling it well is the
actual claim worth making. Not "Translate understands clinical systems,"
just "Translate has organized, sourced, well-structured information about
how they work" — a narrower claim, and a true one, without needing to
borrow credibility from expertise it doesn't have.

## Disclaimer (still worth stating, once scope is actually clean)

> Translate documents the operation, configuration, maintenance,
> communication, and service characteristics of clinical and technical
> systems. It is not intended for clinical decision support, diagnosis,
> treatment selection, or interpretation of patient results. Clinical
> decisions remain the responsibility of licensed healthcare
> professionals and the device manufacturer.

This disclaimer is a true statement about the product once the scope
rule above is actually enforced — not a mitigation standing in for scope
discipline that wasn't done.

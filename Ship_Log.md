\# Ship Log



Running record of what actually shipped, including the missteps along

the way — not a polished highlight reel. If it happened and cost real

time, it belongs here, especially the parts that didn't work the first

time.



\---



\## 2026-07-28 — Nightingale deployment, three structural corrections, first real git push



\*\*What we set out to do:\*\* package Translate's governance docs and

knowledge content into a deployment for Nightingale, so the team could

run Claude directly on that machine instead of relaying work through

chat. Straightforward in concept. Took most of a day, in practice,

because of four real mistakes — each one caught, not each one avoided.



\### Misstep 1 — ADR 0001 proposed a structure nobody had checked



Built a `knowledge/` top-level directory (plus `docs/`, `tools/`,

`services/`) reasoning from `nightingale-repository-architecture.md`, a

design document, without ever checking what already existed in the live

Nightingale repo. It turned out real, working content already existed

elsewhere. Root cause: proposing structure from a document instead of

verified reality — the same failure this project had already caught

happening to other agents earlier the same day (Sheldon/Stewie

reconstructing the Knowledge Block schema from memory instead of the

real file). This time the CTO did it.



\### Misstep 2 — ADR 0002 corrected to a structure that wasn't actually real either



Caught the `knowledge/` duplication by spot-checking content, not

trusting a clean `scope\_check\_array.py` pass (structural checks can't

catch staleness). Found Code's real files at `01\_Networking/Cisco\_IOS/`

and `03\_Clinical\_Integration/HL7/`, and wrote ADR 0002 treating that as

Code's deliberate naming convention. It wasn't. Code itself investigated

further, unprompted, and found the real story: that numbered `00\_`–`05\_`

structure is Travis's own personal life/career archive, and `03\_` only

happened to fit topically for HL7 by coincidence. `01\_Networking` wasn't

a designated slot at all — it collided in number with the real

`01\_Career\_Architecture`. Root cause: accepting "it's already there and

it fits" as evidence of intent, without checking why it was there.



\### Misstep 3 — the fix required real content to move, not just get renamed



Once `04\_Translate/` was confirmed (via the real repo skeleton in

`Translate-Git-Repository.zip`, not secondhand) as the actual designated

Translate slot, ADR 0003 moved the real Cisco/HL7 content there via a

tested copy script — verified afterward by spot-checking the actual

corrected content (router-ospf's real syntax, EVN-2's real cardinality),

not just trusting the copy succeeded.



\### Misstep 4 — none of it had ever been committed



The biggest one. After all three ADRs, the reorg, and days of prior

deployment-package work, a fresh Claude Code session pointed at the repo

reported the files "don't exist anywhere." They existed — verified

directly on the Windows filesystem — but `git status` showed the entire

deployment, from the very first package onward, had sat as untracked,

uncommitted local changes the whole time. Root cause: the original

migration script deliberately stopped short of committing (by design,

to avoid an agent auto-committing without review), and no one ever

did the manual step afterward. Also surfaced along the way: three files

(`PROJECT\_STATUS.md`, `claude.md`, `reorg\_translate.ps1`) had landed as

stray, stale copies inside `docs/decisions/` from an earlier misdirected

save, caught by diffing actual content rather than trusting they matched.



\### What actually shipped



\- ADR 0003, current and correct: all Translate engineering content lives

&#x20; under `04\_Translate/`, alongside Travis's existing business folders.

\- `CLAUDE.md` and `PROJECT\_STATUS.md`, rewritten to match reality, with

&#x20; the stale-path warnings and the reasoning for why 0001/0002 were wrong,

&#x20; not just what 0003 says now.

\- A scope-compliance pass on the real Cisco/HL7 content: 5 flagged

&#x20; phrases read in context and cleared as legitimate technical language,

&#x20; documented so the next run of the tool doesn't redo the judgment call.

\- The first real commit and push of this entire system to

&#x20; `origin/main` (`887ff51`) — everything above is now actually on

&#x20; GitHub, not sitting on one machine.

\- Two new standing rules added to `CLAUDE.md` directly because of this

&#x20; day: verify the live repo before proposing structure, and commit/push

&#x20; before calling anything done.



\### The honest summary



Three structural decisions in one day is real churn, not a clean

process. What made it acceptable rather than a failure: every wrong

turn was caught by checking real evidence — a directory listing, a

content diff, a `git status` — before the next thing got built on top

of it. The system that exists tonight is trustworthy specifically

because it was never allowed to rest on an unverified assumption for

long. That's the discipline worth keeping, not the specific structure

that resulted from it.


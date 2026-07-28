\# 0002 — Adopt the Existing Numbered-Category Structure; Retire `knowledge/`



\*\*Status:\*\* Accepted

\*\*Date:\*\* 2026-07-28

\*\*Author:\*\* CTO

\*\*Supersedes:\*\* 0001 (Knowledge Content Placement)



\## Context



0001 created a new top-level `knowledge/` directory, reasoning from

`nightingale-repository-architecture.md` — a design document — without

first checking what structure actually existed in the live repo. It

didn't: Code had already been maintaining real, working content under a

different convention:







This was discovered only after content had already been migrated into

`knowledge/cisco-ios/` and `knowledge/hl7-fhir/`, and a spot-check (not

just a clean `scope\_check\_array.py` structural pass) showed both were

stale pre-fix snapshots — the router-ospf process-id description still

said "1-65535" instead of the corrected "any positive integer," and EVN-2

still showed cardinality "0..1" instead of the corrected "1..1." Code's

real, current, corrected files were sitting under `01\_Networking/` and

`03\_Clinical\_Integration/` the entire time.



Running two directory conventions side by side for the same content is

worse than either one alone — it guarantees exactly this kind of silent

staleness, since nothing forces the two trees to agree, and a clean

structural check on one tells you nothing about the other.



\## Decision



Retire the `knowledge/` directory from 0001. Adopt Code's existing

`NN\_Category/Domain\_Name/` convention as canonical, since it's the one

with real, live, git-tracked, currently-correct content already built

around it:







`ACL TOP 350` and `GE OEC One CFD` have no home yet in this convention —

unlike Cisco/HL7, nothing is being displaced for them, since no real

content exists at any path for either domain yet. Their category numbers

are an open question for Code, not a CTO decision: `02\_` is unaccounted

for in the existing structure (reserved for something already, or simply

unused), and the right number for each new domain should come from

whoever already owns the numbering scheme.



Governance documents, `scope\_check\_array.py`, and handoff docs stay

where 0001 put them (`docs/architecture/`, `tools/`, `docs/guides/

handoffs/`) — that reasoning didn't depend on the content-placement

question and isn't in conflict with anything Code built.



\## Consequences



\- `knowledge/cisco-ios/knowledge-blocks.json` and

&#x20; `knowledge/hl7-fhir/knowledge-blocks.json` are stale duplicates and

&#x20; must not be read as current. They stay in place, marked, until

&#x20; deliberately removed (see below) — not silently deleted mid-reconciliation.

\- `knowledge/acl-top-350/` and `knowledge/ge-oec-one-cfd/` are empty

&#x20; placeholders, not stale duplicates — no real content exists elsewhere

&#x20; for either domain yet. They can be renamed/moved once Code assigns

&#x20; real category numbers, with no data-loss risk.

\- Any doc referencing `knowledge/...` paths (`CLAUDE.md`,

&#x20; `PROJECT\_STATUS.md`) needs updating to point at the real paths.

\- Before any future structural proposal, check the live repo first. 0001

&#x20; is the second time this project has had to catch "proposed from a

&#x20; document, not verified against reality" — the first was Sheldon/Stewie

&#x20; reconstructing the Knowledge Block schema from fragments instead of

&#x20; reading the real file. This ADR is that same failure, committed by the

&#x20; CTO role instead.








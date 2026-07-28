\# 0003 — Nest Translate Engineering Content Under `04\_Translate/`



\*\*Status:\*\* Accepted

\*\*Date:\*\* 2026-07-28

\*\*Author:\*\* CTO

\*\*Supersedes:\*\* 0002 (Adopt the Existing Numbered-Category Structure)



\## Context



0002 adopted `01\_Networking/Cisco\_IOS/` and `03\_Clinical\_Integration/HL7/`

as canonical, on the premise that they were Code's real, deliberate

convention. Code checked the original archive evidence directly and

found that premise was false:



\- The `00\_`–`05\_` numbered tree is Travis's personal life/career

&#x20; organization (`00\_Plank\_Owner`, `01\_Career\_Architecture`,

&#x20; `02\_Project\_Nightingale`, `03\_Clinical\_Integration`, `04\_Translate`,

&#x20; `05\_Learning`), not a Translate product taxonomy.

\- `01\_Networking/Cisco\_IOS/` was Code's own invention, pattern-matched

&#x20; off `03\_Clinical\_Integration` — it collides in number with the real,

&#x20; pre-existing `01\_Career\_Architecture`.

\- `03\_Clinical\_Integration/HL7/` is a real, pre-existing folder, but its

&#x20; sibling subfolders (FHIR, DICOM, PACS, Mirth, Azure, Notes) read as

&#x20; Travis's own clinical-IT reference material, not a slot designated for

&#x20; Translate's product content. The topical fit with HL7 knowledge blocks

&#x20; was coincidence, not design.

\- `04\_Translate/` already exists, already holds the real Translate

&#x20; business folders (`Business\_Model`, `Financials`, `Pricing`,

&#x20; `Service\_Catalog`, `Marketing`, `Sales`, `Asset\_Intelligence`,

&#x20; `Customer\_Deliverables`), and is the one unambiguous, designated home

&#x20; for anything Translate-related in this tree — confirmed directly

&#x20; against `Translate-Git-Repository.zip`'s real skeleton, not secondhand.



Travis confirmed directly: keep everything in one unified repo, but

nest Translate's engineering content under `04\_Translate/` rather than

colliding with unrelated personal folders.



\## Decision



Everything 0001 originally proposed as top-level (`knowledge/`,

`docs/architecture/`, `docs/decisions/`, `docs/guides/handoffs/`,

`tools/`, `services/`) moves one level deeper, under `04\_Translate/`,

alongside the existing business folders. `Cisco\_IOS`'s and `HL7`'s real

content moved out of `01\_Networking/` and `03\_Clinical\_Integration/`

entirely via a verified copy (confirmed by direct content spot-check,

not just a clean structural pass) — both source folders are otherwise

untouched. `ACL TOP 350` and `GE OEC One CFD` get their real homes

directly at `04\_Translate/knowledge/acl-top-350/` and

`04\_Translate/knowledge/ge-oec-one-cfd/` — no numbering question needed,

since `04\_Translate/` was already the correct root.



\## Consequences



\- This is the third structural decision on content placement in one day

&#x20; (0001 → 0002 → 0003). Each one was caught and corrected by checking

&#x20; real evidence before treating a proposal as settled — the process

&#x20; worked as intended, even though the churn was real.

\- Content still sitting at `01\_Networking/Cisco\_IOS/`,

&#x20; `03\_Clinical\_Integration/HL7/`, and the repo-root `knowledge/`,

&#x20; `docs/`, `tools/`, `services/` folders is now duplicated in

&#x20; `04\_Translate/`. Removal is a separate, deliberate step, done only

&#x20; after the copies were verified correct — not bundled into this ADR.


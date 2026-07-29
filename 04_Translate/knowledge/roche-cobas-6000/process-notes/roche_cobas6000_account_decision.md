# Decision Note — Roche Diagnostics document access (cobas 6000)

**For:** Architect · **Raised by:** Code · **Date:** 2026-07-28
**Type:** provisioning decision (blocks all Roche Block work) · **Owner of decision:** Architect (not the crew)

---

## The decision
How do we obtain **authoritative** cobas 6000 documentation (Operator's Manual, Host Interface Manual, service manual, method sheets) so the capability map can advance past `⚠`?

Authoritative = Roche's official library **eLabDoc**, reached via a **registered Roche Diagnostics customer login (DiaLog portal)**. Third-party mirrors are disqualified as evidence by the Steward's A1 gate.

## Why it's blocking
Everything buildable without sources is already built and staged:
- Roche Researcher + Steward constitutions (ratified)
- cobas 6000 capability map (cap 1 seeded; caps 2–11 assigned)
- Steward review checklist (caps 2–10)
- Researcher acquisition brief

**Not one Block can reach `✅` until an authoritative source is in hand.** The only gate in front of real progress is account access. This is the same wall GE OEC hit ("needs a real GE account").

## Constraint
Per standing rules, account creation and login are done by a **human account holder** — the assistant does not create accounts or enter credentials. So this decision resolves to *who holds/authorizes the account*, not an action the crew can self-serve.

---

## Options
| # | Option | Unblocks | Trade-off |
|---|---|---|---|
| **A** | **Route through a lab/clinical partner** who already holds eLabDoc/DiaLog access | Fastest path to authoritative docs | Depends on a partner; confirm we may use the docs for Translate's knowledge base |
| **B** | **Provision our own Roche Diagnostics customer account** | Durable, self-owned access for all future Roche instruments | Registration barrier — typically requires being an actual Roche instrument customer/facility |
| **C** | **Re-target** to a more openly-documented Roche instrument first | Keeps Roche momentum now | Gives up the "best first target" logic; cobas 6000 slips |
| **D** | **Hold Roche** until access is resolved | No wasted effort | Roche domain stalls entirely |

## Recommendation
**A now, B in parallel, C as fallback.** Chase a partner login for immediate authoritative docs (A) while starting our own customer registration for the long term (B). If neither lands in a reasonable window, re-target rather than stall (C) — do **not** backfill from mirrors to simulate progress (that would fail A1 and repeat the footswitch-class error at the source level).

## What each choice triggers
- **A or B →** Researcher executes the acquisition brief: pull M1/M2, pin versions, confirm module config, route M2 to Code and M1/M3/R1 to the Roche Steward.
- **C →** I draft a short candidate list of Roche instruments with open documentation and we re-seed a map.
- **D →** cobas 6000 recorded as *source-blocked*; crew stands down until revisited.

---

---

## DECISION (2026-07-28): A + B, in parallel
Chosen: **A (partner login) now**, **B (our own Roche Diagnostics customer account) in parallel**. C and D not taken.

Both tracks are human-gated — the account holder registers/logs in; the assistant does not create accounts or enter credentials. Crew is **standby-ready**: the acquisition brief executes the moment either track yields eLabDoc access. **No mirror backfill** while we wait.

| Track | Owner action | Entry point | Status |
|---|---|---|---|
| **A · partner login** | Identify a lab/clinical partner holding eLabDoc/DiaLog access; confirm permission to reference the docs internally | via partner | open |
| **B · own account** | Register as a Roche Diagnostics customer | diagnostics.roche.com → e-service → eLabDoc / DiaLog | open |

**First document on access (either track):** M1 Operator's Manual + M2 HIM — pin versions, confirm module config, then route M2→Code and M1/M3/R1→Roche Steward per the acquisition brief.

### Appendix — partner access request *(template for the Architect to send; not sent by the assistant)*
> **Subject: cobas 6000 documentation access**
> We're building an internal knowledge base for the Roche cobas 6000 and need authoritative source documents — the Operator's Manual, Host Interface Manual, and service/method documentation — as available through eLabDoc. Could you share current-version PDFs (or portal access) and confirm we may reference them internally? We cite document title + version on every entry.

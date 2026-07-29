# Code Steward — Cap 1 (Host/LIS Interface) Review Checklist — *fires when M2 (HIM) lands*

**Steward:** Code (HL7/interface domain) · **Applies to:** every cap-1 Block before `⚠`→`✅`
**Source gate:** an authoritative **M2 (Host Interface Manual)**, version-pinned. No cap-1 Block promotes without it.
**Complements:** the Roche Steward's caps 2–10 checklist (`roche_cobas6000_steward_review_checklist.md`) — this file is the cap-1 gate it defers to.
**Terminal step:** resolve each Block to one of the **Steward v1 six outcomes** (Approve · Approve w/ Constraints · Hold · Return for Research · Return for Editing · Reject). This checklist produces the inputs; it does not replace the matrix.
**Provenance:** every gate below traces to a real catch or trip-wire from the **Liat** cap-1 (HL7) and cap-12 (POCT1-A) reviews — the proven loop, applied forward.

---

## Part A — Cross-cutting gates (reuse from the caps 2–10 checklist; ALL must pass)
A1 Source authority · A2 Version pinning · A3 Module scoping (core / c 501 / c 502 / e 601) · A4 Evidence-tier correctness (no `✅ FIELD`) · A5 Quote fidelity / no over-read · A6 No inherited assertion · A7 Scope-constitution check · A8 Publish-gate six questions · A9 Relationships recorded. *(Full text in the caps 2–10 checklist — do not restate, just apply.)*

---

## Part I — Interface-specific gates (Liat-derived; ALL must pass)

- [ ] **I1 · Protocol-layer decomposition.** Transport → framing/low-level → high-level records → HL7 option → direction/modes → message flows → config → error handling are each their **own** Block. No lumping. *(Liat cap-1 1.1–1.8 shape.)*
- [ ] **I2 · Framing confirmed explicitly, not assumed.** ASTM **E1381** low-level framing (ENQ/ACK/NAK/EOT, STX/ETX, checksum, retransmit/timeout) is sourced from M2 — not inferred. *(Liat MLLP catch: framing was under-read on first pass and had to be corrected.)*
- [ ] **I3 · Full record/segment structure verified against the HIM's own examples.** Every ASTM record (H/P/O/R/L/Q/C) and every HL7 segment is checked **field-by-field against M2's own example messages**, not only its prose tables. **If M2's prose field-tables extract scrambled, the example records/messages are the authoritative field key.** *(Liat: the ORC segment was missing on first read; the POCT1-A prose tables were layout-scrambled and the doc's own `<OBJ.attr>` examples were the reliable attribution key.)*
- [ ] **I4 · Version — conformance vs. wire, and same-doc consistency.** Pin the **ASTM edition(s)** (E1381-91 / E1394-91) **and the HL7 version**. Record both the **stated conformance target** and the **actual on-the-wire version value** if they differ. If M2 states one message/value in prose and a different one in an example, **record it as a documented inconsistency (trip-wire) — do not silently reconcile.** *(Liat: HL7 conformance 2.5.1 vs MSH wire field 2.5; and ORU^R30 everywhere except one stray "ORU^R20" line.)*
- [ ] **I5 · QC transmission is interface-scoped — NEVER flat.** State, per interface (ASTM vs HL7) **and** per module (chemistry vs immunoassay), whether and how QC results transmit. No blanket "QC is/ isn't transmitted." *(Liat 1.8: "QC transmitted" and "not transmitted" were both wrong; the truth was three-way per-interface.)*
- [ ] **I6 · Direction & communication modes sourced.** Unidirectional vs **bidirectional**; host-query (real-time) vs batch; order-download present/absent — each stated by M2, not assumed. *(Liat: HL7 was unidirectional upload; POCT1-A was bidirectional — do not assume symmetry.)*
- [ ] **I7 · Anti-footswitch on every number/identifier.** Each port, timeout, interval, and code is traced to **what M2 actually assigns it to.** An OEM-**unpublished** value (e.g. a default port) is recorded as a **verified absence** — never invented, never borrowed from a look-alike. *(Liat: `2554` was the FTP share-lot port, NOT the DMS interface port; the DMS port was OEM-unpublished and left unasserted.)*
- [ ] **I8 · Result-integrity elevated bar.** Any test-code-uniqueness / instrument-source-identification (ACN-style) rule — anything whose mis-mapping could report one test's result under another — gets the **highest scrutiny and an explicit OEM statement** before `✅`. Cross-link to the caps 3/4/7 result-integrity Blocks. *(Liat: both cap-1 and cap-12 carried an ACN result-integrity Block at the elevated bar.)*
- [ ] **I9 · Interface-split decision (Decision-#34 precedent).** If M2 shows cobas offers **ASTM and HL7 as independent interfaces** (independent semantics / lifecycle), **split cap 1 → 1a ASTM + 1b HL7** (both Code). Decide **explicitly**; do not lump them under one Block set, and do not pre-split without M2. *(Liat: HL7 and POCT1-A became separate Code-stewarded capabilities once their independence was shown.)*
- [ ] **I10 · Field-level depth decision.** Decide **catalogue-level vs field-level** for the record/segment field model. If field-level, source the field tables (via I3's example-record method). Record the chosen depth as a capability-wide constraint. *(Liat R2: field-level pulled for cap 12 at cap-1.4 parity; depth was an explicit Architect call.)*

---

## Part B — Per-sub-capability checks (M2 must confirm each; all `⚠` until it does)

- [ ] **1.1 Physical / transport** — RS232 serial params (data bits 7–8, parity, stop 1–2) **and** whether a TCP/IP / Ethernet option exists; pinned, not assumed.
- [ ] **1.2 Low-level protocol (ASTM E1381-91)** — framing, ENQ/ACK/NAK/EOT, checksum, retransmit/timeout **values** confirmed (I2).
- [ ] **1.3 High-level protocol (ASTM E1394-91)** — which H/P/O/R/L/Q/C records cobas **emits vs. requires**, delimiters, ordering — field-verified against examples (I3).
- [ ] **1.4 HL7 option** — **which HL7 version**, trigger events, segment set; conformance-vs-wire checked (I4); V2-vs-"V2+" family divergence recorded as a relationship, not reconciled by assertion.
- [ ] **1.5 Communication modes** — host-query vs batch; uni- vs bidirectional (I6).
- [ ] **1.6 Message flows** — order download / result upload / QC upload / rerun-reflex; **per-module differences (chemistry vs immuno) kept as separate Blocks** until each is sourced.
- [ ] **1.7 Settings / config** — host-connection params, mapping tables; numeric defaults per I7 (record absences).
- [ ] **1.8 Error handling** — NAK/retransmit, comms alarms, interface data alarms; **interface-origin alarms cross-linked to cap 10** (edge with the Roche Steward — do not certify the cap-10 side unilaterally).

---

## Part C — Interface-split & outcome
- [ ] **I9 split decision recorded** — one cap 1, or 1a ASTM + 1b HL7 — with the M2 evidence that justifies it.
- [ ] Every Part-A + Part-I gate passed; Part-B items for each promoted sub-cap addressed.
- [ ] Result-integrity Blocks (I8) meet the elevated bar.
- [ ] **Assign the Steward v1 outcome** per Block; record the decision, the deciding M2 section/page, and the version pinned. Default shape where the doc lags a platform SW version is **Approve with Constraints** (pin the doc/SW version, attach the gap).

> **Momentum note:** promote once a Block is *constitutionally sufficient* — don't withhold `✅` for missing polish once source, version, module scope, interface scope, and the six questions are satisfied. Conversely, don't rubber-stamp: a real review **returns** genuine gaps (Liat cap-12 returned 2 of 10 — that's the review working).

---

## I9 — ASTM / HL7 split decision rule *(pre-committed 2026-07-29; the OUTCOME fires when M2 lands — not before)*

**The question:** is cobas 6000's host interface **one** capability (ASTM + HL7 as sub-caps 1.3/1.4) or **two** (1a ASTM + 1b HL7, each Code-stewarded)?

**Why it is not settled now:** no M2 on disk. Deciding structure without the source is the exact footswitch I9 guards against. This rule makes the call **deterministic on arrival** — read M2, apply four tests, record the outcome. Until then the call is **UNRESOLVED by design.**

**Four independence tests** *(each answerable from M2's connectivity/protocol chapter):*
| # | Test | Split signal | Unified signal |
|---|---|---|---|
| T1 | **Selection / config** | ASTM and HL7 independently selectable/configured (separate connection settings; run one or the other) | HL7 is only a format *inside* the same ASTM session |
| T2 | **Message model / semantics** | genuinely different flows/capabilities (e.g. HL7 adds query / order-download ASTM lacks) | same flows, merely re-encoded |
| T3 | **Versioning / lifecycle** | ASTM edition and HL7 version pinned & updated independently | shared version / lifecycle |
| T4 | **Transport / framing** | different low-level transport/framing per protocol | shared transport; framing differs only trivially |

**Decision:**
- **SPLIT → 1a ASTM + 1b HL7** if **T1 = YES, or ≥2 of {T1–T4} = YES.** *(Mirrors Liat: HL7 vs POCT1-A were independent on all four → Decision #34.)*
- **UNIFIED → one cap 1** (ASTM = 1.2/1.3, HL7 = 1.4) if only framing/format differs while config, flows, and lifecycle are shared.
- **Tie-breaker (M2 ambiguous):** **stay UNIFIED, tag split as a forward-candidate.** Unified is the reversible state — splitting a certified capability later is cheap; un-splitting a certified split is costly. Do not over-split on weak evidence.
- **Close call → Architect**, as a numbered Decision (Liat's split was ratified as #34).

**Cascade once settled:**
- *If SPLIT:* add an index row (1b); each interface gets its **own** version-pin, its own I5 QC-scoping, its own I8 result-integrity Block; renumber sub-caps; record as a numbered Decision citing the M2 evidence.
- *If UNIFIED:* cap 1 unchanged; ASTM/HL7 stay 1.2–1.4 under one version-pin set; **I5 still distinguishes QC per-protocol within the one capability.**

**Orthogonal — do not conflate:** the chemistry (c 501/c 502) vs immunoassay (e 601) **module** dimension is handled by I5 / sub-cap 1.6 module-scoping, **not** by the protocol split. "Split by protocol" ≠ "split by module."

**Execution:** the moment M2 is on disk, Code runs this rule (a read of the connectivity chapter) and records the outcome + evidence. No earlier.

---

## Appendix — Liat trip-wires carried in (pre-flight)
1. **Framing under-read** → confirm E1381 framing explicitly (I2).
2. **Missing record/segment field** → verify against the doc's own examples (I3).
3. **Version conformance ≠ wire value; same-doc inconsistency** → record both / flag, don't reconcile (I4).
4. **Flat QC claim** → scope per interface + module (I5).
5. **Tempting look-alike number** → trace to its actual role; OEM-unpublished = verified absence (I7).

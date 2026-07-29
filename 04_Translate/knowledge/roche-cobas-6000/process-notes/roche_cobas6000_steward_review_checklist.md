# Roche Steward — Review Checklist, cobas 6000 Capabilities 2–10

**Steward:** Roche Steward · **Applies to:** every Knowledge Block under caps 2–10 before `⚠`→`✅`
**Terminal step:** resolve each Block to one of the **Steward v1 six outcomes** (this checklist produces the inputs, it does not replace the matrix).
**Not covered here:** cap 1 (host/LIS interface — Code) runs its **own gate — see `roche_cobas6000_cap1_interface_steward_review.md`** (fires when M2/HIM lands); cap 11 (networking — Networking Steward) runs its own gates.

---

## Part A — Cross-cutting gates (reusable; ALL must pass)

A Block cannot be promoted with any gate unchecked. A failed gate is a *reason*, recorded on return.

- [ ] **A1 · Source authority.** Backed by an authoritative Roche OEM document (M1/M2/M3/R1), not a third-party mirror. Source tier recorded.
- [ ] **A2 · Version pinning.** Document version **and** instrument software version recorded; the claim is scoped to that version, not stated timelessly. *(HL7 v2 "same field, different answer" trap.)*
- [ ] **A3 · Module scoping.** Claim is bound to the correct module — **core / c 501 / c 502 / e 601** — and is NOT silently generalized across the chemistry↔immunoassay line. A c 501 fact is not an e 601 fact until separately sourced.
- [ ] **A4 · Evidence-tier correctness.** Tag is `✅ OEM` / `⚠` / `❌` and matches the evidence. **No `✅ FIELD`** — that tier is parked until a Roche Field Engineer seat exists.
- [ ] **A5 · Quote fidelity / no over-read.** The assertion matches what the source *actually says*; a direct citation (doc + section/page) is attached. No conclusion broader than the quote supports. *(The footswitch failure: an existence claim the source never made.)*
- [ ] **A6 · No inherited assertion.** The Block does not borrow certainty from a sibling Block. Every statement traces to its own source line — no "confirmed under X" cascades.
- [ ] **A7 · Scope-constitution check.** In-scope per the scope test (direct operational decision + meaningful risk to person/animal/property). Out-of-scope Blocks are marked, not promoted.
- [ ] **A8 · Publish-gate six questions.** What is it? · Why does it matter? · When is it used? · What relationships exist? · How confident are we? · What should an engineer remember?
- [ ] **A9 · Relationships recorded.** Dependencies and cross-domain edges linked (e.g. cap 10 alarms ↔ interface 1.8; cap-3/4 result flags ↔ interface 1.6).

### Elevated bar — Result-Integrity Blocks
Analogous to the GE OEC **radiation promotion bar**: any Block whose error could corrupt a patient result gets the highest scrutiny and a **second authoritative source or explicit OEM statement** before `✅`. This class includes: reportable/measuring range, units, reference intervals, calibration acceptance, QC-failure handling, carryover, and any result-suppression/flagging rule. When in doubt, treat as result-integrity.

---

## Part B — Per-capability checks

### Cap 2 · Sample handling
- [ ] Sample types & matrices scoped per module; tube/cup/dead-volume requirements sourced.
- [ ] Barcode/ID handling; STAT vs routine; rerun/reflex triggers.
- [ ] **Carryover** rules → *result-integrity*.

### Cap 3 · Clinical chemistry measurement (c 501 / c 502)
- [ ] Measurement principle per analyte (photometric / ISE) sourced from the method sheet (R1).
- [ ] **Analyte menu scoped to the specific module** — c 501 ≠ c 502 menus until each is sourced.
- [ ] Units, reportable/measuring range, reference intervals → *result-integrity*.

### Cap 4 · Immunoassay measurement (e 601)
- [ ] Measurement principle (ECL) and per-assay incubation/protocol sourced.
- [ ] Assay menu scoped to e 601; not merged with chemistry menus.
- [ ] Units, range, cutoffs/interpretation → *result-integrity*.

### Cap 5 · Reagent management
- [ ] Cassette/pack handling, onboard & calibration stability, lot management.
- [ ] Reagent-to-calibration linkage recorded as a relationship (feeds cap 6).

### Cap 6 · Calibration
- [ ] Calibration types & triggers (lot change, interval, QC-driven) sourced.
- [ ] **Acceptance criteria** → *result-integrity*.

### Cap 7 · Quality control
- [ ] QC materials, levels, frequency; rule set (e.g. Westgard) as stated by OEM, not assumed.
- [ ] **QC-failure handling / result release consequences** → *result-integrity*.

### Cap 8 · Fluids / consumables
- [ ] System fluids, waste handling, cuvette/cell segments, part identifiers.
- [ ] Consumable-exhaustion → operational impact (relationship to cap 10 alarms).

### Cap 9 · Maintenance schedule
- [ ] Daily / weekly / monthly / as-needed actions from M1/M3, with intervals and part numbers.
- [ ] Maintenance-driven lockouts/downtime noted (relationship to cap 10).

### Cap 10 · Troubleshooting & data alarms
- [ ] Alarm / data-alarm codes with cause + corrective action, sourced (not paraphrased into new codes).
- [ ] **Data alarms that suppress or flag results** → *result-integrity*.
- [ ] **Interface-origin alarms handed to Code** (edge with sub-capability 1.8) — do not certify unilaterally.

---

## Part C — Outcome
- [ ] Every Part-A gate passed and Part-B items for the capability addressed.
- [ ] Result-integrity Blocks meet the elevated bar.
- [ ] **Assign the Steward v1 outcome** (promote to `✅` / return as `⚠` with recorded reason / hold pending source / the remaining matrix outcomes). Record the decision, the deciding source, and the version pinned.

> Momentum note: promote once a Block is *constitutionally sufficient* — do not withhold `✅` for missing polish once evidence, version, module scope, and the six questions are satisfied.

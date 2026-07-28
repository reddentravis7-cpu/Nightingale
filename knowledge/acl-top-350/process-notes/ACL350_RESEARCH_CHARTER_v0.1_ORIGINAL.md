# ACL TOP 350 CTS — Research Charter v0.1

**Status:** Original document as authored by Research (Ledger) and
relayed by Travis. Saved here verbatim, after the fact, specifically so
it exists as a checkable artifact — it was never saved as a file when
first produced, which is the exact gap Code flagged when asked to trust
that `LAB_EQUIPMENT_DOMAIN_TEMPLATE.md` faithfully generalizes it.

**Domain:** Hemostasis Systems
**System family:** ACL TOP Family 50 Series
**Target device:** ACL TOP 350 CTS
**Initial scope:** Analyzer operation, clinical workflow, system
architecture, communications, maintenance, and observable failure
behavior
**Excluded initially:** Proprietary service procedures, credentials,
customer data, PHI, and anything not authorized to place into Translate

---

# 1. Constitutional objective

Validating whether Translate can represent a clinical instrument as a
connected, governed system containing:

```text
Clinical purpose
    ↓
Operator action
    ↓
Software decision
    ↓
Mechanical action
    ↓
Fluidic action
    ↓
Optical measurement
    ↓
Result calculation
    ↓
Result review
    ↓
LIS transmission
    ↓
Patient-care consequence
```

# 2. Source hierarchy

M1 (manufacturer-controlled), R1 (regulatory), E1 (expert field
knowledge — Travis, OEM-trained field service engineer), O1 (direct
observation), I1 (inference), U1 (unresolved).

# 3. Initial capability map

## Capability 1 — Define the analyzer
intended clinical purpose, system identity, model and family
relationships, supported analytical methods, operational environment,
user roles, physical boundaries, software boundaries, external-system
boundaries

## Capability 2 — Prepare the analyzer for operation
power state, startup, initialization, readiness checks, temperature
readiness, consumable readiness, reagent readiness, waste readiness,
operator authentication, communication readiness

## Capability 3 — Manage samples
rack loading, tube presence, barcode identification, sample
identification, closed-tube sampling, aspiration, sample-volume
assessment, HIL assessment, sample-status handling, rerun and reflex
handling, STAT handling, sample unloading

## Capability 4 — Manage reagents and consumables
reagent identification, reagent loading, onboard status, volume
tracking, stability tracking, lot management, calibration association,
QC association, cuvette supply, cleaning fluids, rinse fluids, waste
handling

## Capability 5 — Execute a test
receive or create an order, determine required assay, schedule
processing, select sample and reagent, dispense materials, incubate,
perform measurement, calculate result, apply flags, determine completion
state

## Capability 6 — Perform analytical measurement
Method branches: Coagulometric, Chromogenic, Immunological. Internal
measurement sequence, optical channels, timing logic, and calculation
algorithms explicitly not yet claimed.

## Capability 7 — Manage calibration and quality control
calibration definition, calibration execution, calibration acceptance,
calibration validity, QC scheduling, automatic QC execution, QC
evaluation, QC failure response, lot transitions, traceability, audit
reporting

## Capability 8 — Produce and govern results
raw analytical signal, calculated result, units, reference ranges,
abnormal flags, analytical flags, sample-integrity flags, rerun rules,
reflex rules, technical validation, result release, result amendment,
traceability

## Capability 9 — Communicate with external systems
analyzer identity, network configuration, LIS connection, order
reception, sample-query workflow, result transmission, acknowledgments,
retransmission, communication failure, host status, middleware
relationships, time synchronization, audit trail

## Capability 10 — Maintain the analyzer
operator maintenance, scheduled maintenance, maintenance prerequisites,
maintenance completion, cleaning, replacement of consumables, maintenance
logs, overdue maintenance, service-only boundaries, post-maintenance
validation

## Capability 11 — Detect and recover from failure
error generation, warning generation, status changes, alarm
classification, affected subsystem, affected sample, affected test,
affected result, operator recovery, service escalation, safe stopping
state, restart behavior, recurrence tracking

## Capability 12 — Protect clinical operation
operator access, auditability, patient-result integrity, sample
integrity, traceability, backup and recovery, downtime workflow,
cybersecurity boundaries, data handling, configuration control,
operational risk

---

# 4. First vertical slice

**Routine PT sample from loading through result transmission** — draft
dependency chain from analyzer-ready through host-response-recorded.
Explicitly a Research hypothesis, not an assumed internal sequence.

# 5. First Knowledge Block candidates

40 candidate ids across SYS/OPS/SMP/ORD/ANA/QC/CAL/RES/LIS/MNT/ERR
prefixes (`ACL350-SYS-001` through `ACL350-ERR-003`) — candidates, not
canon; Research may split, merge, rename, or reject them.

# 6. Expert interview rule

Expert answers get converted to
claim/sourceClass/sourceIdentity/scope/confidence/manufacturerConfirmation/exceptions,
so Steward can compare against the manual instead of treating memory as
either unquestionable or unusable.

# 7. First evidence request

Manual inventory: operator manual, quick reference/routine operations
guide, specifications sheet, interface/host communications manual,
maintenance documentation, representative de-identified screenshots.
Record title, revision, software applicability, language, publication
date, ownership, access classification, and permitted use before
extracting claims.

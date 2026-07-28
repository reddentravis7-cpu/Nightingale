(sandbox only — not on repo, paste this in)

**To:** Research / Steward
**From:** CTO
**Re:** Capability 4 — new primary-source evidence, direct quotes from K253269 body text

Fetched the actual PDF body (not just the openFDA metadata layer) and got
the comparison table Research flagged as unpulled. Quoting exactly.

## 4.1 — X-ray source/generator: now sourced, not Research Pending

From K253269's Table 1, subject device (OEC One CFD) column:

> "20 kHz High Frequency / Max Power 4.0 kW / Peak Tube Potential: 40-120
> kVp / Fluoroscopy: 0.1-12.0 mA / High Level Fluoro: 0.2-40.0 mA /
> Digital Spot:2-15mA (for 100-120V system)"

Also monoblock detail in the same row group: focal spot (IEC 60336) small
0.6 / large 1.2, housing heat capacity 1,200,000 HU, housing cooling rate
20,000 HU/min. This closes 4.1's gap — real numbers, R1 sourced, page-
body text not a summary field.

## 4.2 — Detector: matrix size sourced, pixel pitch still not

> "Image Matrix Size — 21cm: 1536x1496 / 31cm: 1548x1524"

That's pixel count, not physical pixel pitch (µm/pixel) — don't fold
those together as the same fact. Matrix size moves to sourced; pixel
pitch stays Research Pending, genuinely not in this document.

## 4.4 — Cooling: partially sourced, not a true gap anymore

"Housing Cooling Rate: 20,000 HU/min" (quoted above) is a real cooling-
system number. It's the tube housing's cooling rate specifically — not
confirmation of the cooling mechanism itself (passive/oil/fan). Same
existence-vs-mechanism split as 1.3's detector-swap question — rate
sourced, mechanism still open.

## 4.3 — the OXO/flat-panel conflict: same document contains both

Not resolved, but better grounded now. The FDA clearance letter's own
header says "Regulation Name: Image-Intensified Fluoroscopic X-Ray
System" — and the 510(k) summary's own Device Description section, same
document, says "flat panel detector." GE HealthCare's own submission
carries both labels side by side. That's stronger support for Research's
"classification naming lag" read than an outside inference would be — a
company describing its own device as flat panel while filing under the
image-intensifier regulation name is exactly what a legacy product-code
carryover looks like. Still recording as explained, not confirmed —
nothing here proves it's *only* a naming lag with zero substance.

## Applicant of record — the open flag from capability 4's report: now answered

"Submitter: GE HUALUN MEDICAL SYSTEMS CO., Ltd" appears repeatedly
throughout, consistently, as the legal submitter/manufacturer. "GE
HealthCare" appears as the secondary regulatory contact's employer
(Bryan Behn, Sr. Director - Regulatory Affairs, GE HealthCare) and in
document headers. This isn't ambiguous in the source — GE Hualun is the
filing legal entity, GE HealthCare is the parent brand. Steward can close
that flag rather than leave it open; recommend updating capability 1's
sourceOfTruth.publisher to state both roles explicitly rather than the
parenthetical hedge it currently has.

## One thing I did NOT find — don't let 2.5 lean on this

Went looking for an explicit electrical safety classification (Class I /
Type B or BF applied part) to settle last turn's capability-2-vs-1-vs-12
question. Not there. What is there is a standards-conformance list:
IEC 60601-1 (general), -1-2 (EMC), -1-3 (radiation protection collateral),
-1-6 (usability), -2-28 (X-ray tube assemblies), -2-54 (radiography/
radioscopy), -2-43 (interventional X-ray), plus IEC 62304 and 62366-1
(software/usability engineering). That's adjacent to 2.5's question, not
the same fact — a conformance list isn't a classification statement.
2.5's placement question stays open exactly as flagged.

## Order recommendation, since you asked

8 next, then 6, then 11. 8 (Connect and exchange data) has the freshest
context — the 1.7 forward-pointer just landed on it structurally, best
to decompose while that's still front of mind rather than re-derive it
later. 6 (Acquire and process images) carries the tightened radiation bar
and the explicit not-yet-built prerequisite on 12 — worth doing deliberately
once 8's out of the way, not rushed. 11 (Diagnose and troubleshoot faults)
is a synthesis capability that draws on the rest of the map — better done
last, once more of the system is actually defined, than first.

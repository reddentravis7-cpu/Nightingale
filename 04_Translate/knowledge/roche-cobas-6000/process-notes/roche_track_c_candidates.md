# Track C — Re-target candidates (insurance if the cobas 6000 account wall holds)

**Purpose:** Roche instruments we could seed a map on *without* eLabDoc access, if Tracks A/B stall.
**Bar:** (1) authoritative docs reachable **without the eLabDoc login**, (2) ideally a host interface so Code's HL7 domain gets the first capability, (3) high deployment / source floor.
**A1 note:** a PDF hosted on Roche's *own* domain (`diagnostics.roche.com`, `assets.roche.com`) or an FDA 510(k) filing is authoritative. ManualsLib / manualzz / scribd are mirrors — leads only.

---

## Ranked candidates

### 1 — cobas Liat  ⭐ recommended
- **Type:** point-of-care molecular PCR (single-test cartridges).
- **Docs — authoritative & UNWALLED:** HIMs + User Guides hosted directly on `diagnostics.roche.com/...dam/cobas-liat-support/`, multiple pinned versions (SW v3.3 / 3.4 / 3.5; pub v8.2 → v12.0).
- **Interface:** **HL7 (MSH-11 = 2.5)** over wired LAN, MLLP framing, TLS 1.2; a separate **POCT1-A** HIM variant also exists. → direct Code/HL7 domain fit. *(Confirmed by cap-1 steward review; the "2.5.1" seen in web results is not what the message field carries.)*
- **Openness verdict:** best on the board — no account needed, well version-pinned, Roche-hosted.
- **Trade-off:** smaller scope than cobas 6000 (single-assay POC, not a modular chemistry/immuno platform). Fewer capabilities, but *fully unblocked today*.

### 2 — cobas h 232
- **Type:** point-of-care cardiac-marker analyzer.
- **Docs:** Operator's Manual on `assets.roche.com` (Roche-hosted, public) — likely A1-authoritative; also on ManualsLib (mirror).
- **Interface:** limited/POC connectivity — confirm before relying on an interface-first capability.
- **Verdict:** viable small target; weaker interface story than Liat.

### 3 — cobas b 123 POC (and b 221)
- **Type:** point-of-care blood gas / electrolytes.
- **Docs:** FDA **510(k) summary** publicly on `accessdata.fda.gov` (K111188) — authoritative but *summary-depth*, not a full operator manual.
- **Verdict:** good regulatory anchor; would need a fuller manual to reach Block depth. Blood-gas result-integrity content raises the elevated-bar load.

### 4 — cobas c 111
- **Type:** small benchtop clinical chemistry analyzer.
- **Docs:** installation manual found on **ManualsLib only (mirror)** so far — not yet A1-authoritative.
- **Interface:** RS-232 **ASTM** host interface (data + barcode) → Code domain fit *if* a Roche-hosted copy is located.
- **Verdict:** promising interface fit, but blocked on finding an authoritative source; parked below Liat.

---

## Recommendation
**cobas Liat is strong enough to be more than a fallback.** Two ways to use it:
- **As insurance:** hold it in reserve; switch only if A/B stall.
- **As a parallel second target (suggested):** because Liat is *fully unblocked today*, Code could begin its HL7 interface capability on Liat **now** — real Block work while the cobas 6000 account tracks run — with zero mirror risk. It also gives the Roche Steward a live, in-scope target to exercise the review checklist against before the bigger cobas 6000 corpus lands.

**Not recommended:** anything sourced only from mirrors (c 111 as-is) — that reintroduces the exact A1 failure Track C exists to avoid.

---

## If we activate a Track C target
1. Confirm the authoritative doc set + versions (Liat: HIM HL7 + User Guide, pin SW/pub versions).
2. Open a new capability map (same shape as cobas 6000), interface capability seeded to Code.
3. Reuse the Roche Steward review checklist unchanged (cross-cutting gates are instrument-agnostic; swap the per-capability section).

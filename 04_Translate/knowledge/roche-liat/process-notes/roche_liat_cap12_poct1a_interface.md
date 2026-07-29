# Capability 12 (draft) — Host / DMS Interface (POCT1-A / DML)

**Status:** **PROMOTED to Cap 12 (Code-stewarded)** per **Decision #34** (2026-07-28 14:42, superseding #27's fold-into-cap-11). Code has **certified the interface `✅ OEM`** — the authoritative record is the certified facet table in `roche_liat_capability_map.md` (§Capability 12). This file is the detailed **12.1–12.9** decomposition behind that certification.
**Reason for promotion (Decision #34):** independent interface semantics, stewardship, and lifecycle — bidirectional XML/DML, own message set, versioned SW 3.3.1 independently of the HL7 HIM's 3.4/3.5.
**Source:** cobas® liat System **Host Interface Manual POCT1-A (DML), VV-09009-05, v6.0, SW 3.3.1** (Roche-hosted, A1-authoritative; 236 pp). Text extracted via `pypdf`.
**Version constraint (carry on every Block):** this HIM pins **SW 3.3.1**, while the platform/HL7 HIM is **SW 3.4 & 3.5** — an **A2 version gap**. POCT1-A facts may lag the 3.4/3.5 platform; flag for re-pull when a 3.4/3.5 POCT1-A HIM surfaces.

---

## How this differs from cap 1 (HL7) — why it's a separate capability
| | Cap 1 — HL7 (LIS) | Cap 12 — POCT1-A/DML (DMS) |
|---|---|---|
| Direction | **Unidirectional** result upload | **Bidirectional** device ↔ DMS |
| Payload | HL7 v2.5.1 messages | **XML** (W3C), UTF-8 |
| Carries QC? | No (certified negative) | **Yes** — Liquid QC via `OBS.R02` |
| Model | Message + ACK | **Conversation / topic** model |
| Partner | LIS host | **DMS** (POC Data Manager) |

Same device, two distinct host interfaces — which is exactly why POCT1-A warranted promotion rather than living as a cap-11 sub-item.

---

## Sub-capabilities (all `⚠` — cite: POCT1-A HIM VV-09009-05 v6.0)

| # | Sub-capability | Sourced finding | Status |
|---|---|---|---|
| 12.1 | Physical / transport | **Wired LAN, TCP/IP**; analyzer establishes the connection to the DMS; server addressable by **fully-qualified name**; Ethernet **not configured** (auto 10/100 Mbps, full/half duplex, highest common speed) [p.23]. **DMS port (R1): NOT published in VV-09009-05** — host set via *Settings > Connections > Host > Server details* (server + port field implied), no fixed/default TCP port stated. ⚠ **Not `2554`** — that is the FTP share-lot port (`ShareLocations.FTPShareN.Port`), a different function | `⚠` |
| 12.2 | Encoding | **XML** per W3C rules; character encoding **UTF-8**, declared `<?xml version="1.0" encoding="UTF-8"?>`; UTF-8 assumed if the declaration omits it [§Message encoding, p.24] | `⚠` |
| 12.3 | Security | **TLS v1.2** secure connection; the DMS server certificate is validated **once** before the first secure connection and **remembered** thereafter (trust-on-first-use) — same pattern as cap 1.6 [§Secure certificate validation, p.23] | `⚠` |
| 12.4 | Direction & model | **Bidirectional** — the analyzer both **sends data to and receives data from** the DMS. **Conversation / topic** model: topics are confirmed with an **Acknowledgment** and closed by an **End of topic** message [§Supported workflows p.37; §Conversations and topics p.40] | `⚠` |
| 12.5 | Message set | `OBS.R01` observations/test results · `OBS.R02` **Liquid QC** results · `ACK.R01` acknowledgment (codes **AA** / **AE**) · `KPA.R01` keep-alive · `ESC.R01` escape/finish-topic · `PVI.R01` / `PVR.R01` patient-verification request/response · `DTV.ROCHE.LIAT.CFG` device-config directive [§Supported POCT1-A message structure, p.112+] | `⚠` |
| 12.6 | Topics / data sync | Communication start-up · **Operators** (full/partial lists) · **Lot** · **Observation** · **device configuration** (directives, ack-only) · **Events** · **Patient verification**. Periodic sync governed by a configurable **connection interval** (also fires on status change / result release) [§Supported workflows] | `⚠` |
| 12.7 | QC transmission *(affirmative half of the cap-1.8 resolution)* | **Liquid QC results transmit to the DMS via `OBS.R02`** — the interface is explicitly used to "send test and QC results" and to "send QC data to the DMS." QC lot number / expiry carried; positive & negative QC runs reported [p.22, p.24; QC observation sections] | `⚠` |
| 12.8 | Patient verification | Request/response workflow: `PVI.R01` (request) → `PVR.R01` (response) [§Patient verification, p.67] | `⚠` |
| 12.9 | Configuration | Server (FQDN), Ethernet, TLS, **data-synchronization topic list**, **Autolock time (1–1440 min)**; **Connectivity interval configurable 5 min–24 h** (R1 — min/recommended-low 5 min; no distinct factory default stated) [p.27]; **application timeout 1–120 s** (example config 30 s) [p.34] | `⚠` |

### Elevated bar — Result-Integrity (POCT1-A ACN Disclaimer) — `⚠`
Same result-integrity hazard as cap 1's HL7 disclaimer: incorrect code/identity mapping "could cause a test result from one test to be reported for a different test" [p.1]. Draft as a result-integrity Block, cross-linked to cap 1's ACN Block and to LIS/DMS code mapping.

---

## 12.5 — Field-level object model (R2 pull, p.74–112+)
*Source: VV-09009-05 §Supported POCT1-A message structure. **Attribution method:** object↔attribute mapping harvested from the HIM's own XML examples (`<OBJ.attr>` tags) — authoritative, not inferred from the prose tables (whose text-layer rows were layout-scrambled). Datatypes/value-sets annotated where the prose tables reliably supplied them; attribute **names** per object are all XML-verified.*
*Datatype legend: ST string · CS coded string · TS timestamp · CE coded element · INT integer · ED encapsulated data.*

**Message-carrying objects (the OBS.R01/R02, ACK, ESC, topic messages):**
| Object | Attributes (XML-verified) | Key datatypes / value-sets |
|---|---|---|
| **HDR** Header | `control_id`, `message_type`, `version_id`, `creation_dttm` | version_id ST = **"POCT1"**; control_id ST (range 1–…); creation_dttm TS |
| **OBS** Observation | `observation_id`, `method_cd`, `qualitative_value`, `status_cd` | observation_id CE; status_cd = **`D`** for aborted; method_cd CS |
| **SVC** Service | `role_cd`, `observation_dttm` | **role_cd CS = `OBS` (patient) / `LQC` (Liquid QC)** ← the QC⇄patient discriminator (12.7); observation_dttm TS |
| **ORD** Order | `universal_service_id` | CE — identifies the assay/service |
| **RGT** Reagent | `name`, `lot_number`, `expiration_date` | name ST; lot_number CS (3-component); expiration_date TS |
| **NTE** Note | `text` | ST free text |
| **ACK** Acknowledgment | `type_cd`, `ack_control_id`, `note_txt` | **type_cd CS = `AA` accept / `AE` error** (reason in note_txt); ack_control_id ST |
| **ESC** Escape | `esc_control_id`, `detail_cd`, `note_txt` | esc_control_id ST; detail_cd CS (per POCT1-A2) |
| **EOT** End-of-topic | `topic_cd` | CS |
| **TRM** Termination | `reason_cd`, `note_txt` | reason_cd CS |

**Device / session / status objects:**
| Object | Attributes (XML-verified) | Notes |
|---|---|---|
| **DEV** Device | `device_id`, `serial_id`, `vendor_id`, `manufacturer_name`, `device_name`, `sw_version` | device_id = IEEE EUI-64; device_name = **"cobasLiat"** |
| **DSC** Device static capabilities | `connection_profile_cd`, `max_message_sz`, `topics_supported_cd` | max_message_sz INT (bytes) |
| **DCP** Device capabilities | `application_timeout`, `vendor_specific` | application_timeout (1–120 s, see 12.9); vendor_specific ED = B64/TXT |
| **DST** Device status | `status_dttm`, `new_observations_qty`, `new_events_qty`, `condition_cd` | qty fields INT (unreported counts) |
| **EVT** Event | `description`, `event_dttm`, `severity_cd` | severity_cd CS (operator-intervention indication) |
| **DTV** Config directive | `command_cd` | device-configuration directive (ack-only) |

**Patient / verification / operator / lot / config objects:**
| Object | Attributes (XML-verified) | Notes |
|---|---|---|
| **PT** Patient | `patient_id`, `name`, `birth_date`, `gender_cd` | |
| **PVI** Patient-verification input | `identifier`, `identifier_id`, `verification_type_cd` | request (`request_cd`=RPVI in REQ) |
| **PVF** Patient-verification field | `status_cd` | **`T` verified / `F` not** (PVR.R01 response) |
| **REQ** Request | `request_cd` | e.g. RPVI |
| **OPR** Operator | `operator_id`, `name` | |
| **ACC** Access control | `operator_id`*/`password`, `permission_level_cd`, `method_cd` | password ED; permission "Administrator" etc. |
| **LOT** Lot | `lot_id`, `lot_number`, `lot_insert_id`, `assay`, `data`, `parameters`, `expiration_date`, `validation_dttm`, `minimum_compatible_version` | assay-lot topic payload |
| **CTC** Control/Calibration | `name`, `lot_number`, `expiration_date`, `level_cd` | name = "assay + control" (e.g. "FABA control") |
| **UPD** Update action | `action_cd` | operation on the in-scope item (full vs partial list sync) |

**Honest completeness note:** object inventory (25) and per-object attribute **names** are XML-verified and complete for what the examples exercise; per-attribute **datatypes/descriptions** are captured where the prose tables were legible, partial elsewhere (text-layer scramble; no page-render tool available to exhaustively verify). This is field-level depth at cap-1.4 parity for the message-carrying objects; a final datatype sweep of any specific object can be re-pulled on request.

---

## Cross-links & boundary
- **Cap 1 (HL7):** sibling interface. QC is the clean contrast — **absent on HL7 (cap 1.8 certified negative), present here (12.7)**. Cross-link the two ACN result-integrity Blocks.
- **Cap 11 (Assay-lot & data management):** now scoped to the **local/UG side** — share-lot folders, add/validate lots per analyzer, Advanced Tools (archiving, USB). The **interface/message-level** POCT1-A spec moves here to cap 12. Recommend Code (cap 12) and Roche Steward (cap 11) confirm the boundary.
- **Cap 9 (networking):** folds into 12.1/12.3 the same way it folds into 1.1/1.6.

## For the Steward (Code)
- All 9 sub-caps + the result-integrity Block enter at `⚠`, sourced and cited — ready for your review checklist.
- **Recommended constraint on `✅`:** pin **SW 3.3.1** on every Block and attach the A2-version-gap note (platform is 3.4/3.5), the same "Approve with Constraints" shape used elsewhere.
- **Prior to-confirms — RESOLVED by Code's certified read:** `OBS.R02` = QC observations, bound to Liquid QC via SVC `role_cd` = **LQC** (vs **OBS** = patient); ACK codes are **AA** (accept) / **AE** (error). Both certified in the map's Cap 12 facet table.

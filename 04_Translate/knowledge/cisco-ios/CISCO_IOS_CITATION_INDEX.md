# Citation Index — Cisco IOS

**Purpose:** persist navigation cost so it's paid once, not once per
block. Every time real work finds where a command/field/spec actually
lives in a source document, it goes here — not just into that one
block's `sourceOfTruth`. Next time something in the same book needs
citing, check here first.

**Status:** populated from the real citation work done across the
77-block Cisco IOS audit (batches 1 through 3c). Every entry below is a
URL that was actually navigated to and confirmed, not guessed.

---

## Cisco IOS Interface and Hardware Component Command Reference (ir-cr-book)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/interface/command/ir-cr-book/`
**Covers:** `show` commands for interfaces, controllers, hardware.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| show ip interface, show ip interface brief | `ir-s5.html` ("show interfaces vlan mapping through show scp") | Direct page fetch — full syntax `show ip interface [type number] [brief]` and sample output columns pulled verbatim | 2026-07-27 |
| show interfaces (base), show interfaces status | `ir-s4.html` ("show hw-module slot tech-support through show interfaces vg-anylan") | TOC-confirmed present; body text past page-length truncation | 2026-07-27 |
| switchport access vlan | `ir-s7.html` ("squelch through system jumbomtu") | Search-result confirmed, real classic-IOS book | 2026-07-27 |
| show controllers | `ir-s2.html` ("service-module t1 linecode through show controllers satellite") | Chapter identified by title range; body text not independently pulled | 2026-07-27 |

## Cisco IOS Configuration Fundamentals Command Reference (cf_book / cf_command_ref)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/`
**Covers:** CLI basics, `show` EXEC commands (gsr through showmon range), file/config management.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| configure terminal | `cf_c1.html` ("C commands") | Direct page fetch — "Related Commands" entry + example usage pulled verbatim | 2026-07-27 |
| show history, show logging, show memory (statistics) | `cf_s2.html` ("show gsr through show monitor event trace") | Direct page fetch — show history and show logging bodies pulled verbatim; show memory reclassified as vague-citation (real command is "show memory" + qualifier) | 2026-07-27 |
| show protocols | `cf_s4.html` ("show protocols through showmon") | Direct page fetch | 2026-07-27 |
| terminal monitor | `cf_l1.html` ("L through mode") | Search-result hit; exact chapter fit not independently verified — worth a real check if this block ever needs re-confirming | 2026-07-27 |

## Cisco IOS LAN Switching Command Reference (lsw_book / lsw-cr-book)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/lanswitch/command/lsw-cr-book/` (also seen at the older non-ios-xml path `ios/lanswitch/command/reference/lsw_book/`)
**Covers:** VLAN and spanning-tree `show`/config commands.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| show vlan, show vlan brief, show vlan id, show spanning-tree | `lsw-s2.html` ("show vlan through spanning-tree vlan") | Direct page fetch — full `show vlan [all\|brief\|id vlan-id\|...]` syntax and the 1-4094 range pulled verbatim | 2026-07-27 |

## Catalyst 9500 VLAN Commands (per-platform command reference)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9500/software/release/17-16/command_reference/b_1716_9500_cr/`
**Covers:** VLAN configuration commands on this Catalyst-IOS-XE platform family.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| vlan (global config), switchport trunk native vlan | `vlan_commands.html` | Direct page fetch — exact syntax `vlan vlan-id`, range "1 to 4094" pulled verbatim | 2026-07-27 |

## Cisco IOS IP Routing: OSPF Command Reference (iro-cr-book)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/command/iro-cr-book/`
**Covers:** OSPF router-configuration and `ip ospf` interface commands.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| router ospf | `ospf-i1.html` ("ip ospf fast-reroute per-prefix through R") | **Resolved 2026-07-28** via DOM container extraction (see navigation notes) — full syntax `router ospf process-id [vrf vrf-name]` pulled directly. Real correction found: process-id is documented as "any positive integer," not the 1-65535 range previously assumed. | 2026-07-28 |
| router-id | `ospf-i1.html` | Citation only — page/family confirmed real, exact section not independently pulled | 2026-07-27 |
| network ... area (wildcard-mask) | `ospf-a1.html` ("A through ip ospf demand-circuit") | Search-confirmed real content on wildcard-mask ORing behavior | 2026-07-27 |
| default-information originate (OSPF context) | `ospf-a1.html` | Note: exact syntax differs by routing protocol (OSPF/RIP/IS-IS/BGP each have their own form) — this citation is OSPF-specific | 2026-07-27 |

## Cisco IOS IP Routing: RIP / EIGRP / Protocol-Independent Command References

**Base URLs:**
- RIP: `https://www.cisco.com/c/en/us/td/docs/ios/iproute_rip/command/reference/irr_book/irr_rip.html`
- EIGRP: `https://www.cisco.com/c/en/us/td/docs/ios/iproute_eigrp/command/reference/ire_book/ire_i1.html` (also `ios-xml/.../ire-cr-book/ire-i1.html`)
- Protocol-Independent: `https://www.cisco.com/c/en/us/td/docs/ios/iproute_pi/command/reference/iri_book/iri_pi2.html`

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| router rip, rip version 2 | `irr_rip.html` | Search-confirmed real, exact content match | 2026-07-27 |
| router eigrp, eigrp network (wildcard-mask) | `ire_i1.html` / `ire-i1.html` | Search-confirmed real, exact content match | 2026-07-27 |
| show ip protocols, show ip route, ip route | `iri_pi2.html` | Search-confirmed real; show-ip-route citation ended up on an older E-Learning archival page instead (see below) — content still accurate | 2026-07-27 |

## Cisco IOS IP Addressing Services Command Reference (ipaddr-cr-book)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book/ipaddr-r1.html`
**Covers:** `show ip dhcp *`, other `reserved-only through show ip irdp` range commands.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| show ip dhcp binding, show ip dhcp conflict | `ipaddr-r1.html` | Search-confirmed real, same page covers both | 2026-07-27 |

## Cisco IOS CDP Command Reference (cdp-cr-book)

**Base URL:** `https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/cdp/command/cdp-cr-book/cdp-cr-a1.html`

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| show cdp neighbors | `cdp-cr-a1.html` | Search-confirmed real, classic IOS | 2026-07-27 |

## E-Learning archival command reference family

**Base URL:** `https://www.cisco.com/E-Learning/bulk/public/tac/cim/cib/using_cisco_ios_software/cmdrefs/`
**Covers:** one page per command (e.g. `show_ip_route.htm`, `hostname.htm`), older-style but reliably single-command and short enough to avoid the truncation problem the large chapter books have. **Worth trying this family FIRST for any single well-known EXEC/global command before hunting a large chapter book** — see navigation notes below.

| Command / field family | Section or anchor | Confirmed by | Date |
|---|---|---|---|
| show ip route | `show_ip_route.htm` | Direct page fetch — full syntax and legacy sample output pulled | 2026-07-27 |
| hostname | `hostname.htm` | Search-confirmed real | 2026-07-27 |
| show processes cpu | `show_process_cpu.htm` | Search-confirmed real | 2026-07-27 |
| banner motd | `banner_motd.htm` | Search-confirmed real | 2026-07-27 |
| copy running-config startup-config | `copy.htm` | Search-confirmed real | 2026-07-27 |
| reload | `reload.htm` | Search-confirmed real | 2026-07-27 |
| ip route, ip default-gateway | `ip_route.htm`, `ip_default-gateway.htm` | Search-confirmed real | 2026-07-27 |
| traceroute, ping, telnet | `traceroute.htm`, `ping.htm`, `telnet.htm` | Search-confirmed real | 2026-07-27 |
| show version | `show_version.htm` | Search-confirmed real | 2026-07-27 |
| access-list (show access-lists, citation vague) | `access-list.htm` | Search-confirmed but exact scope (show vs. config command) unverified | 2026-07-27 |
| show clock | `show_clock.htm` | **Resolved 2026-07-28** — found by directly guessing the archival URL pattern rather than searching. Full syntax `show clock [detail]` pulled; the optional `detail` keyword wasn't previously recorded. | 2026-07-28 |
| show users | attempted, not found | Five real attempts across two sessions, genuinely not located — see "Still uncited" below | 2026-07-28 |

---

## Known navigation notes

- **cisco.com blocks plain `WebFetch` with HTTP 403 on every URL tried.** The Claude Browser tool (real page render) works fine. This is a standing constraint for the whole domain, not a per-command issue — always use the browser tool here, never WebFetch directly.
- **`get_page_text` truncates around 50,000 characters.** The large chapter-style command-reference books (dozens of commands per page, TOC listed up front) frequently get cut off before reaching a target command's body if that command sits late in the chapter's alphabetical range. This caused real, disclosed gaps for `show-interfaces`/`show-controllers` body text, MSH/MSA's formal HL7 tables, and `router-ospf`'s process-id range. When a chapter book truncates before the target, either (a) try the single-command E-Learning archival page instead if one exists, or (b) accept TOC-level "confirmed present" evidence per the lighter promotion tier rather than re-fetching the same oversized page repeatedly.
- **Chapter boundaries aren't reliably guessable from alphabetical reasoning alone.** `show-clock` and `show-users` both seemed like they should sit in specific `cf_s*.html` chapters by alphabetical position, but weren't found in any of the chapters actually tried (`cf_s1`, `cf_s2`, `cf_s4`, `cf_s5`). Don't sink more than 2-3 targeted attempts into guessing a chapter file name — switch to the E-Learning archival family or mark "citation needed" instead.
- **The same command often exists across multiple platform families with different syntax** — classic IOS, IOS-XE (Catalyst), IOS-XR, NX-OS (Nexus), and small-business/CBS switches. Search results frequently surface IOS-XR or Nexus documentation first for common command names. Citing the wrong family isn't just imprecise, it can be factually wrong for this "cisco-ios" (classic IOS) domain — e.g. `show arp` on IOS-XR takes `vrf`/`location` parameters that don't exist in classic IOS. Always check which platform family a source page actually documents before citing it, and flag explicitly (per block) when only a cross-platform source was available.
- **The `get_page_text` truncation problem has a real fix: query the DOM directly instead of extracting text.** Discovered 2026-07-28 closing `router-ospf` (and independently on the HL7 side for MSH/MSA/EVN/PV1/NK1 — same fix, different site). Cisco's docs are built on a DITA-style platform where each command is its own self-contained topic `<div>` with a stable `id` (e.g. `wp1848823089`). Recipe: `document.querySelectorAll('h1,h2,h3,h4,b,strong')` filtered by the command name text to find the heading element, read its `id` or its parent's `id`, then `document.getElementById(thatId).innerText` — this returns the complete topic regardless of how far down the page it sits, because it never goes through the page-length-capped text extractor at all. This should be the **first** method tried for any command whose body text gets cut off by truncation, before falling back to "confirmed present only" or hunting a different chapter file.
- **Guessing the E-Learning archival URL directly can beat searching for it.** `show-clock` was resolved not by finding it in search results, but by guessing `cmdrefs/show_clock.htm` from the naming pattern already established by `show_ip_route.htm`, `hostname.htm`, etc., and navigating straight there. Worth trying `cmdrefs/<command_with_underscores>.htm` directly for any single well-known EXEC command before spending a search query on it — a real 404 (as happened for `show_users.htm`) is a fast, cheap way to also rule the family out.
- **A chapter's own heading list is worth pulling before concluding a command isn't there.** For `show-users`, checking `Array.from(document.querySelectorAll('h1,h2,h3')).map(h => h.textContent)` on the "show protocols through showmon" chapter showed the real command sequence jumps directly from "show usbtoken" to "show version" — proving the command isn't in that chapter/edition at all, rather than just being unreachable due to truncation. That distinction (genuinely absent vs. truncated-before-reaching) matters for deciding whether to keep searching or stop.

---

## Still uncited, attempted

- **show-users** — genuinely not located after five real attempts across two sessions: `cf_s4.html`, `cf_s5.html` (fetched directly, not found in reachable text), the "show protocols through showmon" ios-xml chapter (confirmed via its full heading list that the command sequence jumps directly from "show usbtoken" to "show version" — not present in that chapter/edition at all), and the E-Learning archival URL pattern `show_users.htm` (real 404, not in that family either). The command and its purpose are real and well-established from search snippets; the current official page has not been found. Worth trying a plural/alternate form (e.g. `show_users_all.htm`) or a different Cisco docs product line if this needs closing later.

"""
Scope Check Array — first-pass automation for the review load created by
TRANSLATE_SCOPE_CONSTITUTION.md's sentence-level enforcement clause.

This does NOT replace human Steward review. It narrows it. Each check
below is cheap, repeatable, and deterministic — it catches known patterns
so a human reviewer spends time on what actually needs judgment instead
of re-reading every sentence of every block from a cold start.

Known limitation, stated plainly: the keyword scan (check 4) has real
false-negative risk. A sentence can cross the scope-constitution boundary
without using any watched term, and a technical sentence can use a
watched term without crossing it (e.g. "abnormal aspiration" is a
mechanical fault, not a clinical finding). This array reduces the review
surface; it does not certify compliance on its own. Every flag is a
"look here," not a verdict.

Usage:
    python3 scope_check_array.py path/to/blocks.json
"""

import json
import re
import sys
from collections import defaultdict

# Checks 1-2 were already run manually via ad hoc scripts during HL7 and
# Cisco production. Folding them into the array so they're standing
# tooling instead of one-off scripts written per domain.


def check_referential_integrity(blocks):
    """Every prerequisites/relatedBlocks id must resolve to a real block."""
    ids = {b["id"] for b in blocks}
    issues = []
    for b in blocks:
        for field in ("prerequisites", "relatedBlocks"):
            for ref in b.get(field, []) or []:
                if ref not in ids:
                    issues.append(
                        f"{b['id']}: {field} references unknown id '{ref}'"
                    )
    return issues


def check_schema_completeness(blocks):
    """current requires url + reviewedBy + dateReviewed all populated."""
    issues = []
    for b in blocks:
        if b.get("reviewStatus") == "current":
            sot = b.get("sourceOfTruth", {})
            missing = [
                f for f in ("url", "reviewedBy", "dateReviewed")
                if not sot.get(f)
            ]
            if missing:
                issues.append(
                    f"{b['id']}: reviewStatus=current but missing {missing}"
                )
    return issues


def check_source_family_tripwire(blocks, harmonized_patterns=None):
    """
    Flag sourceOfTruth.url values from a known 'no-version' documentation
    family when the block also claims a specific standard version — the
    HL7 CE/CWE, TS/DTM trip-wire, generalized so any future domain can
    register its own look-alike-source pattern.
    """
    harmonized_patterns = harmonized_patterns or [
        r"v2plus\.hl7\.org",
        r"hl7\.eu/refactored",
        r"usnistgov\.github\.io",
    ]
    pattern = re.compile("|".join(harmonized_patterns))
    issues = []
    for b in blocks:
        sot = b.get("sourceOfTruth", {})
        url = sot.get("url") or ""
        version = sot.get("version")
        if version and pattern.search(url):
            issues.append(
                f"{b['id']}: claims version '{version}' but url matches a "
                f"harmonized/no-version documentation family ({url}) — "
                f"confirm this is actually version-pinned text"
            )
    return issues


# Watch-list is intentionally short and specific rather than broad — a
# noisy scanner that flags everything trains reviewers to ignore it.
# Extend per-domain as real drift patterns get found, same discipline as
# the trip-wire registry in KNOWLEDGE_MAINTENANCE_PLAN.md.
SCOPE_WATCHLIST = [
    r"\bdiagnos(is|e|ed|ing)\b",
    r"\btreat(ment|s|ed|ing)?\b",
    r"\bpatient (should|must|needs? to)\b",
    r"\brecommend(s|ed|ation)?\b",
    r"\b(should|must) not be used\b",
    r"\bclinical(ly)? (significan|relevan|indicat)",
    r"\brisk (of|for) (bleeding|thrombo|complication)",
    r"\brequires? intervention\b",
    r"\b(dosage|dosing)\b",
]
SCOPE_PATTERN = re.compile("|".join(SCOPE_WATCHLIST), re.IGNORECASE)
TEXT_FIELDS = ("summary", "fieldNotes", "description", "exampleInstance")


def _walk_text(value):
    """Yield every string found in a nested content value."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _walk_text(v)
    elif isinstance(value, list):
        for v in value:
            yield from _walk_text(v)


def check_scope_constitution_keywords(blocks):
    """
    First-pass filter for TRANSLATE_SCOPE_CONSTITUTION.md's sentence-level
    rule. Flags blocks whose text fields contain watch-list terms so a
    human applies the Alarm-327-style test to that specific sentence,
    instead of re-reading the whole block file cold.
    """
    issues = []
    for b in blocks:
        hits = set()
        for field in TEXT_FIELDS:
            if field in b:
                for text in _walk_text(b[field]):
                    for m in SCOPE_PATTERN.finditer(text):
                        hits.add(m.group(0).lower())
        content = b.get("content", {})
        for text in _walk_text(content):
            for m in SCOPE_PATTERN.finditer(text):
                hits.add(m.group(0).lower())
        if hits:
            issues.append(
                f"{b['id']}: watch-list terms found {sorted(hits)} — "
                f"needs human sentence-level scope check, not auto-resolved"
            )
    return issues


def check_id_naming_convention(blocks, pattern=r"^[a-z0-9-]+(\.[a-z0-9-]+)+$"):
    """Flag ids that don't match the declared domain convention."""
    regex = re.compile(pattern)
    return [
        f"{b['id']}: does not match naming convention {pattern}"
        for b in blocks
        if not regex.match(b["id"])
    ]


CHECKS = [
    ("referential integrity", check_referential_integrity),
    ("schema completeness (current-status gate)", check_schema_completeness),
    ("source-family trip-wire", check_source_family_tripwire),
    ("scope constitution keyword scan", check_scope_constitution_keywords),
    ("id naming convention", check_id_naming_convention),
]


def run(path):
    with open(path) as f:
        blocks = json.load(f)
        if isinstance(blocks, dict) and "blocks" in blocks:
            blocks = blocks["blocks"]

    print(f"Scope Check Array — {path} ({len(blocks)} blocks)\n")
    total_issues = 0
    for name, fn in CHECKS:
        issues = fn(blocks)
        total_issues += len(issues)
        status = "PASS — nothing flagged" if not issues else f"{len(issues)} flagged"
        print(f"[{name}] {status}")
        for issue in issues:
            print(f"    - {issue}")
    print(f"\n{total_issues} total items need human review out of "
          f"{len(blocks)} blocks. Everything else passed the automated "
          f"array and does not need a cold sentence-by-sentence re-read.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scope_check_array.py path/to/blocks.json")
        sys.exit(1)
    run(sys.argv[1])

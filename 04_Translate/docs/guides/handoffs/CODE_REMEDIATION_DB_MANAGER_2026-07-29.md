# Code Remediation Sequence — Persistence Gaps

**From:** DB Manager (per TRANSLATE-ROLE-DBM-v1.0)
**To:** Code (holds filesystem/git access)
**Date:** 2026-07-29
**Authorized by:** Founder/Chief Architect (this session)

DB Manager defines the discipline and the verification bar; Code executes.
Every "done" below is defined by a **verified result**, not by a command
returning 0. Do not report a step complete until its verification line passes.

---

## Verified starting state (as of 2026-07-29 ~12:43, live-checked)

| Target | State | Risk |
|---|---|---|
| `~/output` (Nightingale, `main` → github.com/reddentravis7-cpu/Nightingale.git) | **Real backup.** Local HEAD `e77bc8e` == GitHub `refs/heads/main` `e77bc8e`, tree clean | Safe; stale since 2026-07-28 16:00 |
| `~/Development/Translate` (`main`, Next.js/Supabase app + Cisco blocks) | **Local-only. NO remote.** ~10 commits never pushed. **HEAD is moving — another session is actively committing (commits at 12:41 and 12:43)** | 🔴 device loss = total loss; concurrency hazard |
| 10 × `~/Downloads/roche_*.md` | Loose files, not in any repo, not tracked, not pushed | 🔴 single copy, one device |
| `…/outputs/nightingale_backup` + `Shannon_Backup/` | Empty git shell (0 commits) / same-disk duplicate | Not backups; ignore |

**Two safety gates already cleared by DB Manager:**
- `~/Development/Translate` history has **never** contained `.secrets/` or any
  `.env` (checked `git log --all --full-history` + `rev-list --all --objects`).
  Safe to attach a public/private remote. `.gitignore` already excludes
  `.secrets/`, `.env*`, `.next/`, `.vercel/`, `.supabase/`.
- None of the 10 Roche files are tracked in the Nightingale repo yet.

---

## TRACK A — Rescue Roche work into the Nightingale repo (no blockers; do first)

Roche is the highest-risk item (zero copies beyond one Mac) and the fastest
win, because `~/output` is already pushed. 10 files: 5 `cobas6000_*`,
4 `liat_*`, 1 `roche_track_c_candidates.md` (cobas 6000 and Liat are two
different products — mirror that in the folder split).

**A0 — snapshot & confirm the repo is clean and in sync before touching it:**
```bash
cd ~/output
git fetch origin
git status --porcelain            # MUST be empty before you start
git rev-parse HEAD                # note this
git ls-remote origin refs/heads/main   # MUST equal the HEAD above
```
If `git status --porcelain` is not empty, stop and report — something else is
mid-flight in this repo.

**A1 — place the files** (durability now; Steward can re-file later):
```bash
mkdir -p 04_Translate/knowledge/roche-cobas-6000/process-notes
mkdir -p 04_Translate/knowledge/roche-liat/process-notes
cp ~/Downloads/roche_cobas6000_*.md   04_Translate/knowledge/roche-cobas-6000/process-notes/
cp ~/Downloads/roche_track_c_candidates.md 04_Translate/knowledge/roche-cobas-6000/process-notes/
cp ~/Downloads/roche_liat_*.md        04_Translate/knowledge/roche-liat/process-notes/
```

**A2 — stage, review, commit:**
```bash
git add 04_Translate/knowledge/roche-cobas-6000 04_Translate/knowledge/roche-liat
git status --porcelain            # review EXACTLY what's staged — expect 10 new files, nothing else
git commit -m "Rescue Roche cobas 6000 + Liat research files from Downloads into tracked knowledge tree"
```

**A3 — VERIFY committed (DB Manager bar):**
```bash
git status                        # MUST say "working tree clean", nothing to commit
git ls-files 04_Translate/knowledge/roche-cobas-6000 04_Translate/knowledge/roche-liat | wc -l   # MUST be 10
```

**A4 — push, then VERIFY the remote actually moved (not just that push exited 0):**
```bash
git push origin main
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git ls-remote origin refs/heads/main | cut -f1)
[ "$LOCAL" = "$REMOTE" ] && echo "REAL BACKUP CONFIRMED: $LOCAL" || echo "MISMATCH — NOT pushed"
```

**A5 — content spot-check** (the router-ospf/EVN-2 discipline): pick one file and
prove the committed bytes equal the source:
```bash
git show HEAD:04_Translate/knowledge/roche-cobas-6000/process-notes/roche_cobas6000_capability_map.md \
  | diff - ~/Downloads/roche_cobas6000_capability_map.md && echo "byte-identical"
```

**Only after A4 prints "REAL BACKUP CONFIRMED" is Roche a real backup.** Leave
the originals in `~/Downloads` until then. Do **not** delete the Downloads copies
as part of this task — deletion is out of scope for a rescue.

---

## TRACK B — Give the Cisco/app repo a remote and push it

`~/Development/Translate` holds the Next.js/Supabase app + the freshest Cisco
knowledge-block edits (its `cisco-ios-knowledge-blocks.json` DIFFERS from — and is
newer than — the copy already in Nightingale). None of it exists anywhere but this
Mac. This is the exact 2026-07-28 failure mode, still live.

**Two blockers / decisions before any push — do not improvise past these:**

1. **`gh` is NOT installed on this machine.** Code cannot `gh repo create`.
   The empty remote must be created by the **Founder via the GitHub web UI**
   (or `brew install gh` first, then authenticate). Create it **empty — no
   README, no .gitignore, no license** — so the first push is a clean
   fast-forward with nothing to merge.

2. **DECISION — repo name + visibility (Founder's call).** DB Manager
   recommendation: **PRIVATE.** Content is derived from vendor (Cisco)
   copyrighted manuals — the scope constitution explicitly flags IP/copyright
   as an unresolved risk category — and the repo is linked to a live Supabase
   project. Private until IP is cleared. Suggested name: `translate-app` or
   `cisco-ios-qrg`.

3. **Concurrency hazard.** Another session is committing to this repo in real
   time. Before adding the remote, confirm the tree is clean and HEAD is
   stable, or coordinate a brief pause with that session — do not push mid-edit.

**B0 — confirm clean & stable:**
```bash
cd ~/Development/Translate
git status --porcelain            # MUST be empty; if not, the active session has WIP — wait
git rev-parse HEAD                # note it; re-run after ~30s and confirm it hasn't moved
```

**B1 — re-confirm no secret is about to be published** (DB Manager already
verified history is clean; re-run as the final gate before an outward push):
```bash
git log --all --full-history --oneline -- '.secrets' '.secrets/*' '*.env' '.env'   # MUST be empty
git ls-files | grep -iE 'secret|\.env' || echo "no secrets tracked — safe"
```

**B2 — attach remote and push** (owner/name per decision #2):
```bash
git remote add origin https://github.com/reddentravis7-cpu/<REPO_NAME>.git
git push -u origin main
```

**B3 — VERIFY the remote reflects local HEAD:**
```bash
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git ls-remote origin refs/heads/main | cut -f1)
[ "$LOCAL" = "$REMOTE" ] && echo "REAL BACKUP CONFIRMED: $LOCAL" || echo "MISMATCH — NOT pushed"
```

---

## Flagged for Architect, NOT for Code to resolve here

- **Cisco knowledge lives in two diverging repos** (`~/output/.../cisco-ios/`
  and `~/Development/Translate/cisco-ios-knowledge-blocks.json`, confirmed
  different). Which is canonical is an architecture decision, not a backup
  decision. Track B makes the app repo *durable*; it does not *reconcile* the split.
- **`nightly_sync.ps1` is Windows-only (`C:\nightingale`) and cannot run on this
  Mac** — no PowerShell, no `C:`, no cron/launchd entry, no `sync_log.txt` ever
  written. It is not an active backup mechanism here. If durable auto-backup is
  wanted on this Mac, it needs a real launchd/cron job wrapping `git` — separate task.
- The empty `nightingale_backup` shells (session outputs + Shannon_Backup) point
  at the real Nightingale remote but have 0 commits. Harmless but confusing;
  candidate for cleanup so no one mistakes them for the real repo.

---

## Report-back contract

For each track, report the literal output of the `REAL BACKUP CONFIRMED` /
`MISMATCH` line. "Pushed" means that line printed CONFIRMED — nothing less.
State for each domain afterward: **real backup** (committed + pushed, verified)
or **local-only**. Do not round up.

---

*Persistence note on THIS file: it currently lives only in the session outputs
folder (local-only, same failure mode it describes). It should itself be committed
into the Nightingale repo under `04_Translate/docs/guides/handoffs/` as part of
Track A if it's worth keeping.*

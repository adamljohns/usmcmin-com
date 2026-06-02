#!/usr/bin/env python3
"""
dedup-merge-records.py — collapse two RESOLUTE Citizen records for the SAME
person into one (the delete half of a dual-office / duplicate merge).

The refinement engine (refine-records.py) cannot DELETE records — it only
refines existing ones by slug. So a one-record merge is two steps:

  1. THIS script removes the <drop-slug> record (after backing up
     scorecard.json and writing it back minified).
  2. refine-records.py applies a dossier keyed on <keep-slug> to extend its
     office / candidacy_status / sources. For the dual-office case:
       set.candidacy_status -> "running_higher_office"
       set.office           -> "<sitting seat> (sitting · YEAR P nominee for <higher office>)"
     NO reset_unspecified — preserve in-tier scores; the engine auto-upgrades
     any stale rubric keys (out-of-tier cells -> N/A, new tier categories -> null).

Pick the SURVIVOR = the sitting-office record (the seat they currently hold),
preferring the one with richer real scores/sources; merge the other's useful
sources in via the dossier's sources_add, and drop any stray/irrelevant ones.
See the refine-scorecard skill's "Dual-office dedup / one-record merge" playbook.

Idempotent: if <drop-slug> is already gone, it reports and exits 0.

Usage:
    python3 dedup-merge-records.py <keep-slug> <drop-slug>
    python3 dedup-merge-records.py <keep-slug> <drop-slug> --dry-run
"""
import json
import os
import shutil
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
BACKUP_DIR = os.path.join(REPO, 'data', '.backups')


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry-run' in sys.argv
    if len(args) != 2:
        raise SystemExit('usage: dedup-merge-records.py <keep-slug> <drop-slug> [--dry-run]')
    keep_slug, drop_slug = args
    if keep_slug == drop_slug:
        raise SystemExit('ABORT: keep-slug and drop-slug are identical.')

    with open(SCORECARD, encoding='utf-8') as f:
        sc = json.load(f)
    cands = sc['candidates']
    before = len(cands)

    keep = [c for c in cands if c.get('slug') == keep_slug]
    drop = [c for c in cands if c.get('slug') == drop_slug]

    print(f'candidates before: {before}')
    print(f'  KEEP  {keep_slug}: {len(keep)} record(s)'
          + (f' — {keep[0].get("name")} — {keep[0].get("office")}' if keep else ''))
    print(f'  DROP  {drop_slug}: {len(drop)} record(s)'
          + (f' — {drop[0].get("name")} — {drop[0].get("office")}' if drop else ''))

    if not keep:
        raise SystemExit(f'ABORT: survivor {keep_slug!r} not found — refusing to delete.')
    if len(keep) > 1:
        raise SystemExit(f'ABORT: {len(keep)} records share slug {keep_slug!r} — inspect manually.')
    if not drop:
        print(f'\n{drop_slug!r} already absent — nothing to delete (idempotent).')
        return

    # Sanity: same person? Warn (don't block) if names differ — dedup is for
    # ONE person's duplicate records, not two different people.
    kn = (keep[0].get('name') or '').strip().lower()
    for d in drop:
        dn = (d.get('name') or '').strip().lower()
        if kn and dn and kn != dn:
            print(f'  ⚠️  NAME MISMATCH: keep={keep[0].get("name")!r} vs drop={d.get("name")!r} '
                  f'— confirm these are the SAME person before proceeding.')

    new_cands = [c for c in cands if c.get('slug') != drop_slug]
    after = len(new_cands)
    removed = before - after
    print(f'\nWill remove {removed} record(s) ({drop_slug}); {before} -> {after}.')

    if dry:
        print('[dry-run] no files written.')
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = os.path.join(BACKUP_DIR, f'scorecard.{ts}.pre-dedup-{drop_slug}.json')
    shutil.copy2(SCORECARD, backup)
    print(f'Backup: {os.path.relpath(backup, REPO)}')

    sc['candidates'] = new_cands
    # Match the master's on-disk format: minified (see build-data.py compact=True).
    tmp = SCORECARD + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(sc, f, ensure_ascii=False, separators=(',', ':'))
    os.replace(tmp, SCORECARD)
    print(f'Wrote {os.path.relpath(SCORECARD, REPO)} (minified) — {after} candidates.')
    print('\nNext steps:')
    print(f'  1. refine-records.py dossier keyed on "{keep_slug}" — extend office +')
    print('     candidacy_status=running_higher_office + sources_add (NO reset_unspecified).')
    print(f'  2. build pipeline — prune orphan candidates/<st>/{drop_slug}.html BEFORE the sitemap.')
    print('  3. git add -A && git commit && git push origin main   (commit+push fast).')


if __name__ == '__main__':
    main()

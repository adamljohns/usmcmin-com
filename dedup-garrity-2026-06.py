#!/usr/bin/env python3
"""
dedup-garrity-2026-06.py — collapse the two Stacy Garrity (PA) records to one.

Stacy Garrity is the sitting PA State Treasurer running for Governor in 2026.
She had TWO records, violating the one-record-per-person (dual-office) rule:

  - stacy-garrity-2026  Treasurer record  (KEPT — the sitting-office base, per
                                            the Tara Durant dual-office precedent)
  - stacy-garrity-gov   Governor-nominee  (DELETED — merged into the survivor)

This script ONLY removes the stacy-garrity-gov record (the delete half of the
dedup). The survivor's office/candidacy_status/profile/sources are extended
separately and tier-correctly by the refinement engine
(refine-records.py refinements/pa-garrity-dedup-2026-06.json), which is the
ONE validated path for touching scores. It backs up scorecard.json first and
writes back in the master's compact (minified) format so the ~37MB file stays
under GitHub's 50MB warning.

Idempotent: if stacy-garrity-gov is already gone, it reports and exits 0.

Usage:
    python3 dedup-garrity-2026-06.py            # back up + delete
    python3 dedup-garrity-2026-06.py --dry-run  # report only, write nothing
"""
import json
import os
import shutil
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
SCORECARD = os.path.join(REPO, 'data', 'scorecard.json')
BACKUP_DIR = os.path.join(REPO, 'data', '.backups')

KEEP_SLUG = 'stacy-garrity-2026'
DROP_SLUG = 'stacy-garrity-gov'


def main():
    dry = '--dry-run' in sys.argv

    with open(SCORECARD, encoding='utf-8') as f:
        sc = json.load(f)
    cands = sc['candidates']
    before = len(cands)

    keep = [c for c in cands if c.get('slug') == KEEP_SLUG]
    drop = [c for c in cands if c.get('slug') == DROP_SLUG]

    print(f'candidates before: {before}')
    print(f'  KEEP  {KEEP_SLUG}: {len(keep)} record(s)'
          + (f' — {keep[0].get("office")}' if keep else ''))
    print(f'  DROP  {DROP_SLUG}: {len(drop)} record(s)'
          + (f' — {drop[0].get("office")}' if drop else ''))

    if not keep:
        raise SystemExit(f'ABORT: survivor {KEEP_SLUG} not found — refusing to '
                         f'delete the only Garrity record.')
    if len(keep) > 1:
        raise SystemExit(f'ABORT: {len(keep)} records share slug {KEEP_SLUG} — '
                         f'unexpected, inspect manually.')
    if not drop:
        print(f'\n{DROP_SLUG} already absent — nothing to delete (idempotent).')
        return

    new_cands = [c for c in cands if c.get('slug') != DROP_SLUG]
    after = len(new_cands)
    removed = before - after
    if removed != len(drop):
        raise SystemExit(f'ABORT: expected to remove {len(drop)}, computed {removed}.')

    print(f'\nWill remove {removed} record ({DROP_SLUG}); {before} -> {after}.')

    if dry:
        print('[dry-run] no files written.')
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = os.path.join(BACKUP_DIR, f'scorecard.{ts}.pre-garrity-dedup.json')
    shutil.copy2(SCORECARD, backup)
    print(f'Backup: {os.path.relpath(backup, REPO)}')

    sc['candidates'] = new_cands
    # Match the master's on-disk format: compact/minified (see build-data.py
    # atomic_write compact=True — keeps the ~37MB file under GitHub's 50MB warn).
    tmp = SCORECARD + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(sc, f, ensure_ascii=False, separators=(',', ':'))
    os.replace(tmp, SCORECARD)
    print(f'Wrote {os.path.relpath(SCORECARD, REPO)} (compact) — {after} candidates.')
    print(f'\nNext: python3 refine-records.py refinements/pa-garrity-dedup-2026-06.json '
          f'--no-build   (extends the survivor to the dual-office framing)')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
backfill-status-field.py — add a `status` field to every candidate in
scorecard.json, derived from existing signals.

Status values (per Adam's 2026-05-18 directive):
  'active'       — currently in an elected/appointed government position.
                   Default. Shows in citizen.html, find-my-reps, rankings.
  'former'       — was in a government position, currently not (resigned,
                   removed, retired, term-limited and left, deceased,
                   or moved to private sector). Hidden from active layouts
                   by default; shows on /citizen-formers.html.
                   Profile pages remain searchable + linked.
  'lost'         — was a candidate who lost an election (Earle-Sears,
                   Ciattarelli, etc.). Distinct from 'former' because they
                   never held the position they were scored against. Also
                   hidden from active layouts; shows on /citizen-formers.html.
  'lame_duck'    — currently in office BUT confirmed not seeking re-election
                   in 2026. Still appears in active layouts but with a small
                   "lame duck" badge. Note: applies to 11 senators per
                   Ballotpedia's 2026 list — many House too.

Derivation rules:
  1. candidacy_status='lost' or 'failed' → 'lost'
  2. candidacy_status='resigned' or 'removed' or 'deceased' → 'former'
  3. office contains "(former)" or starts with "Former" → 'former'
  4. office contains "former" + non-candidate context → 'former'
  5. otherwise → 'active' (with later lame-duck overlay)

Idempotent: re-running updates only candidates whose status field is
missing or whose derivation rule now produces a different result.

Run:
    python3 backfill-status-field.py --dry-run
    python3 backfill-status-field.py --apply
After: build-data.py + generate-profiles.py + build-search-index.py
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

# "Former" patterns in the office string. Order matters — most-specific first.
FORMER_OFFICE_PATTERNS = [
    re.compile(r'^Former\b', re.IGNORECASE),
    re.compile(r'\(former(?:\s+\w+)?\)', re.IGNORECASE),  # "Lt. Gov. (former)" / "(former)"
    re.compile(r'\bresigned\b', re.IGNORECASE),
    re.compile(r'\bremoved\b', re.IGNORECASE),
    re.compile(r'\bdeceased\b', re.IGNORECASE),
    re.compile(r'Failed.+candidate', re.IGNORECASE),
]


def derive_status(c):
    """Return ('active' | 'former' | 'lost', reason)."""
    cs = (c.get('candidacy_status') or '').lower()
    office = c.get('office') or ''
    if cs in ('lost', 'failed'):
        return 'lost', f'candidacy_status={cs}'
    if cs in ('resigned', 'removed', 'deceased', 'retired'):
        return 'former', f'candidacy_status={cs}'
    for pat in FORMER_OFFICE_PATTERNS:
        if pat.search(office):
            return 'former', f'office_pattern: {pat.pattern}'
    return 'active', 'default'


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    tally = Counter()
    changes = []   # (name, old_status, new_status, reason)

    for c in sc['candidates']:
        old = c.get('status')
        new, reason = derive_status(c)
        if old != new:
            changes.append((c.get('name'), old, new, reason))
            c['status'] = new
        else:
            # status field already correct (or first-time-set with same value)
            if 'status' not in c:
                c['status'] = new   # set to default 'active' explicitly
                tally['set_default_active'] += 1
        tally[f'status_{new}'] += 1

    print('=== STATUS FIELD BACKFILL ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')
    print()
    if changes:
        print(f'Status changes ({len(changes)}):')
        for nm, old, new, reason in changes[:30]:
            print(f'  {nm:35s}  {str(old):10s} → {new:10s}  ({reason})')
        if len(changes) > 30:
            print(f'  ... and {len(changes) - 30} more')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()

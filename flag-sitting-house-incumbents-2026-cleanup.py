#!/usr/bin/env python3
"""
flag-sitting-house-incumbents-2026-cleanup.py — Cleanup pass.

The main flag script only matched offices starting with "U.S. Representative"
or "US Representative". This pass catches the remaining variants:
  - "US House"
  - "U.S. House — District N"
"""
import json
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

PRIMARY_DATES = {
    'AL':'2026-05-19','AK':'2026-08-18','AR':'2026-05-19','AZ':'2026-08-04',
    'CA':'2026-06-02','CO':'2026-06-30','CT':'2026-08-11','DE':'2026-09-08',
    'FL':'2026-08-18','GA':'2026-05-19','HI':'2026-08-08','IA':'2026-06-02',
    'ID':'2026-05-19','IL':'2026-03-17','IN':'2026-05-05','KS':'2026-08-04',
    'KY':'2026-05-19','LA':'2026-11-03','MA':'2026-09-08','MD':'2026-06-30',
    'ME':'2026-06-09','MI':'2026-08-04','MN':'2026-08-11','MO':'2026-08-04',
    'MS':'2026-06-02','MT':'2026-06-02','NC':'2026-03-03','ND':'2026-06-09',
    'NE':'2026-05-12','NH':'2026-09-08','NJ':'2026-06-09','NM':'2026-06-02',
    'NV':'2026-06-09','NY':'2026-06-23','OH':'2026-05-05','OK':'2026-06-30',
    'OR':'2026-05-19','PA':'2026-05-19','RI':'2026-09-08','SC':'2026-06-09',
    'SD':'2026-06-02','TN':'2026-08-04','TX':'2026-03-03','UT':'2026-06-23',
    'VA':'2026-06-16','VT':'2026-08-11','WA':'2026-08-04','WI':'2026-08-11',
    'WV':'2026-05-12','WY':'2026-08-18',
}

PRESERVE_STATUSES = {
    'primary_candidate', 'general_candidate', 'incumbent_seeking_reelection',
    'lost_primary', 'not_running', 'running_higher_office', 'lame_duck',
    'lost', 'deceased', 'resigned', 'nominee', 'won'
}
PRESERVE_STATUSES_TOP = {'former', 'lost', 'deceased', 'lame_duck', 'resigned'}


def is_sitting_house_rep_loose(c):
    """Catches U.S. House variants we missed in the strict matcher."""
    if c.get('level') != 'federal':
        return False
    if c.get('district') is None:
        return False
    office = (c.get('office') or '').strip().lower()
    # New patterns: "US House", "U.S. House", "U.S. House — District N"
    patterns = ('us house', 'u.s. house', 'house of representatives')
    if not any(office.startswith(p) for p in patterns):
        return False
    if c.get('status') in PRESERVE_STATUSES_TOP:
        return False
    return True


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    by_dist = defaultdict(list)
    for c in cands:
        if is_sitting_house_rep_loose(c):
            by_dist[(c.get('state'), c.get('district'))].append(c)

    updates = 0
    state_counts = defaultdict(int)
    for (st, dist), recs in by_dist.items():
        # Already flagged?
        if any(r.get('candidacy_status') in PRESERVE_STATUSES for r in recs):
            continue
        # Pick best target — most curated scores wins
        recs.sort(
            key=lambda r: sum(1 for cat in r.get('scores', {}).values() for v in cat if v is not None),
            reverse=True
        )
        target = recs[0]
        target['candidacy_status'] = 'incumbent_seeking_reelection'
        if 'profile' not in target:
            target['profile'] = {}
        target['profile']['next_election'] = 2026
        target['profile']['next_election_type'] = 'primary'
        target['profile']['seat_up_next'] = True
        if not target['profile'].get('next_election_date'):
            target['profile']['next_election_date'] = PRIMARY_DATES.get(st, '')
        existing_note = target['profile'].get('confidence_note', '') or ''
        new_note = '2026-05-20 — Default-flagged as incumbent_seeking_reelection (loose-match cleanup pass).'
        if new_note not in existing_note:
            target['profile']['confidence_note'] = (
                existing_note + (' · ' if existing_note else '') + new_note
            )
        updates += 1
        state_counts[st] += 1

    print(f'\nFlagged {updates} additional House incumbents (loose office-text matches)')
    print(f'\nBy state:')
    for st, n in sorted(state_counts.items(), key=lambda x: -x[1]):
        print(f'  {st}: {n}')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

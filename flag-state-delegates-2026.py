#!/usr/bin/env python3
"""
flag-state-delegates-2026.py — Flag MD + WV "State Delegate" records for 2026.

The main state-legislator flag script matched "State Representative" but missed
240 records whose office is literally "State Delegate":
  - MD House of Delegates: 140 (4-yr terms, last 2022, UP IN 2026)
  - WV House of Delegates: 100 (2-yr terms, UP IN 2026)

Both chambers up in 2026 → flag incumbent_seeking_reelection.
Also catches any other lower-house naming variants (Assembly Member, etc.).
"""
import json
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

PRIMARY_DATES = {'MD':'2026-06-30','WV':'2026-05-12','VA':'2026-06-16'}

PRESERVE_STATUSES = {
    'primary_candidate', 'general_candidate', 'incumbent_seeking_reelection',
    'lost_primary', 'not_running', 'running_higher_office', 'lame_duck',
    'lost', 'deceased', 'resigned', 'nominee', 'won',
}
PRESERVE_STATUSES_TOP = {'former', 'lost', 'deceased', 'lame_duck', 'resigned'}

# State delegate / lower-house variants. VA House of Delegates is elected in
# ODD years (next 2027) so we do NOT bulk-flag VA delegates for 2026.
LOWER_HOUSE_OFFICE_EXACT = {'state delegate', 'delegate', 'assembly member', 'assemblymember'}

# Only these states' delegates/assembly are up in 2026
UP_2026_DELEGATE_STATES = {'MD', 'WV'}


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    updates = 0
    state_counts = defaultdict(int)
    skipped_wrong_cycle = 0

    for c in cands:
        if c.get('level') != 'state':
            continue
        office = (c.get('office') or '').strip().lower()
        if office not in LOWER_HOUSE_OFFICE_EXACT:
            continue
        if c.get('candidacy_status') in PRESERVE_STATUSES:
            continue
        if c.get('status') in PRESERVE_STATUSES_TOP:
            continue
        st = c.get('state')
        if st not in UP_2026_DELEGATE_STATES:
            skipped_wrong_cycle += 1
            continue

        c['candidacy_status'] = 'incumbent_seeking_reelection'
        if 'profile' not in c:
            c['profile'] = {}
        c['profile']['next_election'] = 2026
        c['profile']['next_election_type'] = 'primary'
        c['profile']['seat_up_next'] = True
        if not c['profile'].get('next_election_date'):
            c['profile']['next_election_date'] = PRIMARY_DATES.get(st, '')
        existing_note = c['profile'].get('confidence_note', '') or ''
        new_note = '2026-05-20 — Default-flagged as incumbent_seeking_reelection (state delegate, up in 2026).'
        if new_note not in existing_note:
            c['profile']['confidence_note'] = (
                existing_note + (' · ' if existing_note else '') + new_note
            )
        updates += 1
        state_counts[st] += 1

    print(f'\nFlagged {updates} state delegates as incumbent_seeking_reelection')
    for st, n in sorted(state_counts.items(), key=lambda x: -x[1]):
        print(f'  {st}: {n}')
    if skipped_wrong_cycle:
        print(f'\n  Skipped {skipped_wrong_cycle} delegates in odd-year-cycle states (e.g. VA, next 2027)')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

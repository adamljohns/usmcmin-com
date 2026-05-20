#!/usr/bin/env python3
"""
flag-state-legislators-2026.py — Bulk-flag state legislators for 2026 cycle.

All state representatives (typically 2-year terms, all up every 2 years) and
about half of state senators (typically 4-year terms, staggered) are up in 2026.
This script defaults all unflagged state legislators to incumbent_seeking_reelection
with a verification note. Term-specific corrections can come later.

Preserves: lame_duck, lost, deceased, resigned, primary_candidate, general_candidate,
running_higher_office, not_running, lost_primary, nominee, won.
"""
import json
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# State -> 2026 primary date (matches House script)
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
    'lost', 'deceased', 'resigned', 'nominee', 'won',
}
PRESERVE_STATUSES_TOP = {'former', 'lost', 'deceased', 'lame_duck', 'resigned'}

# States where state senators serve 4-year terms (typical) — these may not
# be up in 2026 if they were elected in 2024. Flag with a clearer note.
FOUR_YEAR_SENATE_STATES = {
    'AL','AK','AR','AZ','CA','CO','CT','DE','FL','GA','HI','IL','IN','IA','KS',
    'KY','LA','MD','MI','MN','MS','MO','MT','NV','NJ','NM','NY','NC','ND','OH',
    'OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY',
    # 2-year state senate: MA, ME, NH, MA also has 2-yr senate per some sources
}


def is_state_legislator(c):
    if c.get('level') != 'state':
        return False
    office = (c.get('office') or '').strip().lower()
    if 'state senator' in office or 'state senate' in office:
        return ('senator', office)
    if 'state representative' in office or 'state house' in office or 'state assembly' in office or 'state assemblyman' in office or 'state assemblywoman' in office or 'state assembly member' in office:
        return ('rep', office)
    if 'assembly member' in office or 'assemblymember' in office:
        return ('rep', office)
    return False


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    updates_rep = 0
    updates_sen = 0
    state_counts = defaultdict(int)
    skipped_preserved = 0
    skipped_no_state = 0

    for c in cands:
        kind_result = is_state_legislator(c)
        if not kind_result:
            continue
        kind, _ = kind_result

        if c.get('candidacy_status') in PRESERVE_STATUSES:
            skipped_preserved += 1
            continue
        if c.get('status') in PRESERVE_STATUSES_TOP:
            skipped_preserved += 1
            continue

        st = c.get('state')
        if not st:
            skipped_no_state += 1
            continue

        c['candidacy_status'] = 'incumbent_seeking_reelection'
        if 'profile' not in c:
            c['profile'] = {}
        c['profile']['next_election'] = 2026
        c['profile']['next_election_type'] = 'primary'
        if not c['profile'].get('next_election_date'):
            c['profile']['next_election_date'] = PRIMARY_DATES.get(st, '')

        existing_note = c['profile'].get('confidence_note', '') or ''
        if kind == 'rep':
            # State reps almost universally have 2-year terms
            new_note = ('2026-05-20 — Default-flagged as incumbent_seeking_reelection '
                        '(state reps typically have 2-year terms; up in 2026).')
            updates_rep += 1
        else:
            # State senators may be on 2-year or 4-year cycles
            if st in FOUR_YEAR_SENATE_STATES:
                new_note = ('2026-05-20 — Default-flagged as incumbent_seeking_reelection. '
                            'NOTE: state senate seats typically have 4-year staggered terms — '
                            'verify exact 2026/2028 cycle per district.')
            else:
                new_note = ('2026-05-20 — Default-flagged as incumbent_seeking_reelection '
                            '(state senate, 2-year term state).')
            updates_sen += 1

        if new_note not in existing_note:
            c['profile']['confidence_note'] = (
                existing_note + (' · ' if existing_note else '') + new_note
            )

        # Mark seat_up_next as True for reps (always), tentative for 4-yr senators
        c['profile']['seat_up_next'] = True if kind == 'rep' else None
        state_counts[st] += 1

    total = updates_rep + updates_sen
    print(f'\nFlagged {total} state legislators as incumbent_seeking_reelection')
    print(f'  State reps (2-yr terms): {updates_rep}')
    print(f'  State senators (mostly 4-yr): {updates_sen}')
    print(f'  Skipped (already had status or top-level marker): {skipped_preserved}')
    if skipped_no_state:
        print(f'  Skipped (no state code): {skipped_no_state}')

    print(f'\nBy state (top 20):')
    for st, n in sorted(state_counts.items(), key=lambda x: -x[1])[:20]:
        print(f'  {st}: {n}')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

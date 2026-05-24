#!/usr/bin/env python3
"""
flag-state-executives-2026.py — Flag untagged statewide executives by 2026 cycle.

Statewide executive offices (Governor, Lt Governor, AG, SoS, Treasurer, Auditor,
Comptroller, Superintendent, etc.) are generally elected on the state's
gubernatorial cycle. This flags untagged sitting execs as
incumbent_seeking_reelection IF their state holds statewide elections in 2026.

States NOT up in 2026 (left untouched):
  - 2023 cycle → next 2027: KY, LA, MS
  - 2024 cycle → next 2028: DE, IN, MO, MT, NC, ND, UT, WA, WV
  - 2025 cycle → next 2029: NJ, VA
2-year-term governor states (VT, NH) ARE up in 2026.
"""
import json
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# States with statewide executive elections in 2026 (gubernatorial cycle states)
UP_2026_STATES = {
    'AL','AK','AZ','AR','CA','CO','CT','FL','GA','HI','ID','IL','IA','KS','ME',
    'MD','MA','MI','MN','NE','NV','NH','NM','NY','OH','OK','OR','PA','RI','SC',
    'SD','TN','TX','VT','WI','WY',
}
# Explicitly NOT 2026 (sanity guard)
NOT_2026_STATES = {'KY','LA','MS','DE','IN','MO','MT','NC','ND','UT','WA','WV','NJ','VA'}

PRIMARY_DATES = {
    'AL':'2026-05-19','AK':'2026-08-18','AR':'2026-05-19','AZ':'2026-08-04',
    'CA':'2026-06-02','CO':'2026-06-30','CT':'2026-08-11','FL':'2026-08-18',
    'GA':'2026-05-19','HI':'2026-08-08','IA':'2026-06-02','ID':'2026-05-19',
    'IL':'2026-03-17','KS':'2026-08-04','ME':'2026-06-09','MA':'2026-09-08',
    'MD':'2026-06-30','MI':'2026-08-04','MN':'2026-08-11','NE':'2026-05-12',
    'NH':'2026-09-08','NM':'2026-06-02','NV':'2026-06-09','NY':'2026-06-23',
    'OH':'2026-05-05','OK':'2026-06-30','OR':'2026-05-19','PA':'2026-05-19',
    'RI':'2026-09-08','SC':'2026-06-09','SD':'2026-06-02','TN':'2026-08-04',
    'TX':'2026-03-03','VT':'2026-08-11','WI':'2026-08-11','WY':'2026-08-18',
}

PRESERVE_STATUSES = {
    'primary_candidate', 'general_candidate', 'incumbent_seeking_reelection',
    'lost_primary', 'not_running', 'running_higher_office', 'lame_duck',
    'lost', 'deceased', 'resigned', 'nominee', 'won',
}
PRESERVE_STATUSES_TOP = {'former', 'lost', 'deceased', 'lame_duck', 'resigned'}

# Statewide executive office signatures
EXEC_KEYWORDS = (
    'governor', 'lieutenant governor', 'lt. governor', 'lt governor',
    'attorney general', 'secretary of state', 'treasurer', 'auditor',
    'comptroller', 'superintendent of public instruction',
    'commissioner of agriculture', 'insurance commissioner',
    'land commissioner', 'commissioner of labor', 'public service commissioner',
)

# Term-limited / known-not-running incumbents (do NOT flag as seeking reelection)
# These were term-limited governors whose successor races we already ingested.
TERM_LIMITED_GOVERNORS = {
    ('OH','mike-dewine'), ('FL','ron-desantis'), ('GA','brian-kemp'),
    ('SC','henry-mcmaster'), ('TN','bill-lee'), ('KS','laura-kelly'),
    ('CO','jared-polis'), ('OK','kevin-stitt'), ('AL','kay-ivey'),
    ('AZ','doug-ducey'), ('NM','michelle-lujan-grisham'), ('CA','gavin-newsom'),
    ('NY','andrew-cuomo'), ('ME','janet-mills'), ('IA','kim-reynolds'),
    ('NV','steve-sisolak'),
}


def office_is_statewide_exec(office):
    o = (office or '').strip().lower()
    if not o:
        return False
    # Must START with an exec keyword (avoids "deputy assistant ..." false hits)
    return any(o.startswith(k) for k in EXEC_KEYWORDS)


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    updates = 0
    skipped_not_2026 = 0
    skipped_term_limited = 0
    office_counts = defaultdict(int)
    state_counts = defaultdict(int)

    for c in cands:
        if c.get('level') not in ('state', 'state-executive', 'executive'):
            continue
        if not office_is_statewide_exec(c.get('office')):
            continue
        if c.get('candidacy_status') in PRESERVE_STATUSES:
            continue
        if c.get('status') in PRESERVE_STATUSES_TOP:
            continue

        st = c.get('state')
        if st not in UP_2026_STATES:
            skipped_not_2026 += 1
            continue
        if (st, c.get('slug')) in TERM_LIMITED_GOVERNORS:
            skipped_term_limited += 1
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
        new_note = '2026-05-20 — Default-flagged as incumbent_seeking_reelection (statewide exec, 2026 cycle).'
        if new_note not in existing_note:
            c['profile']['confidence_note'] = (
                existing_note + (' · ' if existing_note else '') + new_note
            )

        # Categorize
        o = (c.get('office') or '').lower()
        if o.startswith('governor'): cat = 'governor'
        elif 'lieutenant' in o or 'lt' in o.split()[0:2]: cat = 'lt governor'
        elif 'attorney general' in o: cat = 'AG'
        elif 'secretary of state' in o: cat = 'SoS'
        elif 'treasurer' in o: cat = 'treasurer'
        elif 'auditor' in o: cat = 'auditor'
        elif 'comptroller' in o: cat = 'comptroller'
        else: cat = 'other exec'
        office_counts[cat] += 1
        state_counts[st] += 1
        updates += 1

    print(f'\nFlagged {updates} statewide executives as incumbent_seeking_reelection')
    print(f'  Skipped (state not up 2026): {skipped_not_2026}')
    print(f'  Skipped (term-limited governor): {skipped_term_limited}')
    print(f'\nBy office:')
    for o, n in sorted(office_counts.items(), key=lambda x: -x[1]):
        print(f'  {o}: {n}')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

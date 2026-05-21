#!/usr/bin/env python3
"""
flag-va-delegates-fl-gov-2026.py — Two targeted flag groups:

1. VA House of Delegates (100): office text "House of Delegates — District N".
   All 100 seats elected Nov 2025 (odd-year), 2-year terms → next up Nov 2027.
   Flag incumbent_seeking_reelection with next_election=2027 so they persist
   in the system for the 2027 cycle.

2. FL Governor candidates (4): Paul Renner, David Jolly, Jason Pizzo,
   James Fishback — office "Candidate for Governor of Florida", currently
   untagged. Flag primary_candidate, next_election=2026.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

PRESERVE_STATUSES = {
    'primary_candidate', 'general_candidate', 'incumbent_seeking_reelection',
    'lost_primary', 'not_running', 'running_higher_office', 'lame_duck',
    'lost', 'deceased', 'resigned', 'nominee', 'won',
}


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    va_flagged = 0
    fl_flagged = 0

    for c in cands:
        office = (c.get('office') or '').strip().lower()
        st = c.get('state')

        # 1. VA delegates → 2027 cycle
        if st == 'VA' and office.startswith('house of delegates'):
            if c.get('candidacy_status') in PRESERVE_STATUSES:
                continue
            if c.get('status') in ('former', 'lost', 'deceased', 'resigned'):
                continue
            c['candidacy_status'] = 'incumbent_seeking_reelection'
            if 'profile' not in c:
                c['profile'] = {}
            c['profile']['next_election'] = 2027
            c['profile']['next_election_type'] = 'primary'
            c['profile']['seat_up_next'] = False  # not 2026; next is 2027
            c['profile']['next_election_date'] = '2027-06-15'  # VA primary (approx)
            note = c['profile'].get('confidence_note', '') or ''
            add = ('2026-05-20 — VA House of Delegates: elected Nov 2025 (2-yr term), '
                   'next election 2027. Flagged incumbent_seeking_reelection (2027 cycle).')
            if add not in note:
                c['profile']['confidence_note'] = (note + ' · ' if note else '') + add
            va_flagged += 1

        # 2. FL gov candidates → 2026 primary
        elif st == 'FL' and 'candidate for governor' in office:
            if c.get('candidacy_status') in PRESERVE_STATUSES:
                continue
            c['candidacy_status'] = 'primary_candidate'
            if 'profile' not in c:
                c['profile'] = {}
            c['profile']['next_election'] = 2026
            c['profile']['next_election_type'] = 'primary'
            c['profile']['seat_up_next'] = True
            if not c['profile'].get('next_election_date'):
                c['profile']['next_election_date'] = '2026-08-18'
            note = c['profile'].get('confidence_note', '') or ''
            add = '2026-05-20 — FL Governor candidate flagged primary_candidate (2026 open seat, DeSantis term-limited).'
            if add not in note:
                c['profile']['confidence_note'] = (note + ' · ' if note else '') + add
            fl_flagged += 1
            print(f'  FL GOV  {c["name"]} ({c.get("party")}) → primary_candidate')

    print(f'\n  VA delegates flagged (2027 cycle): {va_flagged}')
    print(f'  FL gov candidates flagged (2026): {fl_flagged}')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

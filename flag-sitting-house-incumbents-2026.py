#!/usr/bin/env python3
"""
flag-sitting-house-incumbents-2026.py — Default US House incumbents to
'incumbent_seeking_reelection' candidacy_status if not otherwise flagged.

Every U.S. House seat is up in 2026. Sitting reps who have no explicit
candidacy_status default to "running for reelection" — this is the
common-case assumption that we apply unless a record explicitly says
otherwise (lame_duck, lost, deceased, running_higher_office, not_running,
lost_primary, resigned).

Adds primary date hints where known (state-level primary calendar).
"""
import json
from pathlib import Path
from collections import defaultdict

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# State -> 2026 primary date (best-known as of 2026-05-20)
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

# These existing candidacy_status values mean "DO NOT TOUCH"
PRESERVE_STATUSES = {
    'primary_candidate', 'general_candidate', 'incumbent_seeking_reelection',
    'lost_primary', 'not_running', 'running_higher_office', 'lame_duck',
    'lost', 'deceased', 'resigned', 'nominee', 'won'
}

# These status values are also strong "don't touch" signals
PRESERVE_STATUSES_TOP = {'former', 'lost', 'deceased', 'lame_duck', 'resigned'}


def is_sitting_house_rep(c):
    """True iff this looks like a sitting US House rep."""
    if c.get('level') != 'federal':
        return False
    if c.get('district') is None:
        return False
    office = (c.get('office') or '').lower()
    if not ('representative' in office or 'us rep' in office or 'u.s. rep' in office):
        return False
    if c.get('status') in PRESERVE_STATUSES_TOP:
        return False
    return True


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    # Group by (state, district) — first record without a 2026 candidacy_status
    # AND that holds the seat (sitting rep) gets flagged.
    by_dist = defaultdict(list)
    for c in cands:
        if is_sitting_house_rep(c):
            by_dist[(c.get('state'), c.get('district'))].append(c)

    updates = 0
    skipped_already_flagged = 0
    skipped_multiple_in_dist = 0
    state_counts = defaultdict(int)

    for (st, dist), recs in by_dist.items():
        # Find the sitting rep — the one without any 2026 candidacy_status
        unflagged = [r for r in recs if r.get('candidacy_status') not in PRESERVE_STATUSES]
        flagged = [r for r in recs if r.get('candidacy_status') in PRESERVE_STATUSES]

        if not unflagged:
            skipped_already_flagged += 1
            continue

        # If there are multiple sitting-rep records, just flag the one whose office
        # text starts with "U.S. Representative" or "US Representative" (not "Texas State Senator" etc.)
        # That should be the actual federal rep.
        primary_rep_candidates = [
            r for r in unflagged
            if (r.get('office') or '').strip().lower().startswith(('u.s. representative', 'us representative'))
        ]
        if not primary_rep_candidates:
            # Fall back to any unflagged record
            primary_rep_candidates = unflagged
        if len(primary_rep_candidates) > 1:
            # Pick the one with the most curated scores
            primary_rep_candidates.sort(
                key=lambda r: sum(1 for cat in r.get('scores', {}).values() for v in cat if v is not None),
                reverse=True
            )

        target = primary_rep_candidates[0]
        target['candidacy_status'] = 'incumbent_seeking_reelection'

        # Add primary date + 2026 hints to profile
        if 'profile' not in target:
            target['profile'] = {}
        target['profile']['next_election'] = 2026
        target['profile']['next_election_type'] = 'primary'
        target['profile']['seat_up_next'] = True
        if not target['profile'].get('next_election_date'):
            target['profile']['next_election_date'] = PRIMARY_DATES.get(st, '')

        # Augment confidence note (don't clobber)
        existing_note = target['profile'].get('confidence_note', '') or ''
        new_note = f'2026-05-20 — Default-flagged as incumbent_seeking_reelection (no explicit status).'
        if new_note not in existing_note:
            target['profile']['confidence_note'] = (
                existing_note + (' · ' if existing_note else '') + new_note
            )

        updates += 1
        state_counts[st] += 1

    print(f'\nFlagged {updates} sitting House incumbents as incumbent_seeking_reelection')
    print(f'  Skipped {skipped_already_flagged} districts already 2026-flagged')
    print(f'\nBy state:')
    for st, n in sorted(state_counts.items(), key=lambda x: -x[1]):
        print(f'  {st}: {n}')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

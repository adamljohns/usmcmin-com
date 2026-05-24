#!/usr/bin/env python3
"""
flag-senate-class2-incumbents-2026.py — Flag Class 2 senators seeking 2026 reelection.

Class 2 senators (elected to 6-yr terms in 2020) are up in 2026. This script
explicitly flags the ones we have high confidence are seeking reelection, plus
flags known retirees as 'lame_duck'.

Anyone not on either list stays untouched (so the user can verify before flagging).
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# Known seeking reelection 2026 (Class 2)
SEEKING_REELECTION = {
    ('AK', 'dan-sullivan'),
    ('AR', 'tom-cotton'),
    ('CO', 'john-hickenlooper'),
    ('DE', 'chris-coons'),
    ('GA', 'jon-ossoff'),
    ('ID', 'jim-risch'),
    ('IA', 'joni-ernst'),
    ('KS', 'roger-marshall'),
    ('LA', 'bill-cassidy'),
    ('MA', 'ed-markey'),
    ('ME', 'susan-collins'),
    ('MS', 'cindy-hyde-smith'),
    ('MT', 'steve-daines'),
    ('NJ', 'cory-booker'),
    ('NM', 'ben-ray-lujan'),
    ('NC', 'thom-tillis'),
    ('OK', 'james-lankford'),
    ('OR', 'jeff-merkley'),
    ('RI', 'jack-reed'),
    ('SC', 'lindsey-graham'),
    ('SD', 'mike-rounds'),
    ('TX', 'john-cornyn'),
    ('VA', 'mark-warner'),
    ('WV', 'shelley-moore-capito'),
    ('WY', 'john-barrasso'),
    ('NE', 'pete-ricketts'),  # appointed to Sasse seat; seeking elected term
}

# Known retiring or running higher (Class 2)
LAME_DUCKS = {
    ('IL', 'dick-durbin'),
    ('KY', 'mitch-mcconnell'),
    ('NH', 'jeanne-shaheen'),
    ('MI', 'gary-peters'),
    ('MN', 'tina-smith'),
}
RUNNING_HIGHER = {
    ('AL', 'tommy-tuberville'),  # → AL Gov
    ('TN', 'bill-hagerty'),       # → TN Gov
}


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    flagged_seeking = 0
    flagged_lame_duck = 0
    flagged_running_higher = 0
    not_found = []

    target_sets = {
        'incumbent_seeking_reelection': SEEKING_REELECTION,
        'lame_duck': LAME_DUCKS,
        'running_higher_office': RUNNING_HIGHER,
    }
    counts = {'incumbent_seeking_reelection': 0, 'lame_duck': 0, 'running_higher_office': 0}

    for new_status, slug_set in target_sets.items():
        for state, slug in slug_set:
            target = next((c for c in cands if c.get('state')==state and c.get('slug')==slug), None)
            if not target:
                not_found.append((state, slug, new_status))
                continue
            # Only update if it doesn't already have a 2026 status
            current_status = target.get('candidacy_status')
            if current_status == new_status:
                continue  # already correct
            target['candidacy_status'] = new_status
            if 'profile' not in target:
                target['profile'] = {}
            target['profile']['next_election'] = 2026
            target['profile']['next_election_type'] = 'primary'
            target['profile']['seat_up_next'] = True
            existing_note = target['profile'].get('confidence_note', '') or ''
            new_note = f'2026-05-20 — Senate Class 2 flag: {new_status}.'
            if new_note not in existing_note:
                target['profile']['confidence_note'] = (
                    existing_note + (' · ' if existing_note else '') + new_note
                )
            counts[new_status] += 1
            print(f'  FLAGGED {target["name"]:<25s} ({state}) → {new_status}')

    print(f'\nSummary:')
    for status, n in counts.items():
        print(f'  {status}: {n}')
    if not_found:
        print(f'\nSlug not found (skipped):')
        for state, slug, status in not_found:
            print(f'  {state}/{slug} (intended: {status})')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')


if __name__ == '__main__':
    main()

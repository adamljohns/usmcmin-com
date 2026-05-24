#!/usr/bin/env python3
"""
resolve-conflicting-office-dups.py — Resolve 25 conflicting-office duplicate pairs
with explicit per-person decisions about which 2026 race is real.

For each (state, name), KEEP_SLUG names the record whose office reflects the
actual/announced 2026 race. The other record is dropped, but its scores (if
richer), sources, photo, and website are merged into the keeper first.

Decisions (verified against 2026 cycle as of 2026-05-20):
  REAL higher-office runs (keep campaign record):
    Bennet→CO Gov, Weiser→CO Gov, Ford→NV Gov, Stefanik→NY Gov,
    Blackburn→TN Gov, Drazan→OR Gov, Paxton→TX Senate (vs Cornyn),
    Lindsay James→IA Senate, Mills→ME Senate (vs Collins),
    Tipping→ME Senate, Joe Tate→MI Senate, Jared Sullivan→NH Senate
  Base record is accurate (drop speculative addition):
    Lamb→AZ-05 House, Moskowitz→FL House, Simpson→FL Ag Comm,
    Beshear→KY Gov (sitting), Royce White→MN Senate (2024 nominee),
    Lawler→NY House (staying), Ogles→TN House, Hagerty→TN Senate (staying),
    Gloria Johnson→TN state rep, Allred→TX-33 House, Wesley Hunt→TX House,
    Chuck Gray→WY SoS, Hageman→WY House (staying)
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

# (state, name) -> slug to KEEP
KEEP = {
    ('AZ', 'Mark Lamb'):          'mark-lamb',                 # AZ-05 House (Biggs seat open)
    ('CO', 'Michael Bennet'):     'michael-bennet-gov',        # announced CO Gov
    ('CO', 'Phil Weiser'):        'phil-weiser-gov',           # announced CO Gov
    ('FL', 'Jared Moskowitz'):    'jared-moskowitz',           # US House reelection
    ('FL', 'Wilton Simpson'):     'wilton-simpson',            # Ag Commissioner
    ('IA', 'Lindsay James'):      'lindsay-james-ia-senate',   # IA US Senate
    ('KY', 'Andy Beshear'):       'andy-beshear',              # sitting KY Gov (not Senate)
    ('ME', 'Janet Mills'):        'janet-mills-senate-2026',   # challenging Collins
    ('ME', 'Mike Tipping'):       'mike-tipping-senate',       # ME US Senate
    ('MI', 'Joe Tate'):           'joe-tate-mi-senate',        # MI US Senate
    ('MN', 'Royce White'):        'royce-white',               # MN US Senate (2024 nominee)
    ('NH', 'Jared Sullivan'):     'jared-sullivan-nh-senate',  # NH US Senate
    ('NV', 'Aaron Ford'):         'aaron-ford-gov',            # announced NV Gov
    ('NY', 'Elise Stefanik'):     'elise-stefanik-gov',        # announced NY Gov
    ('NY', 'Mike Lawler'):        'mike-lawler',               # US House reelection (staying)
    ('OR', 'Christine Drazan'):   'christine-drazan-gov-2026', # OR Gov (2022 nominee)
    ('TN', 'Andy Ogles'):         'andy-ogles',                # US House reelection
    ('TN', 'Bill Hagerty'):       'bill-hagerty',              # US Senate (staying)
    ('TN', 'Gloria Johnson'):     'gloria-johnson',            # TN state rep
    ('TN', 'Marsha Blackburn'):   'marsha-blackburn-gov',      # announced TN Gov
    ('TX', 'Colin Allred'):       'colin-allred',              # TX-33 House (runoff)
    ('TX', 'Ken Paxton'):         'ken-paxton-senate',         # TX US Senate (vs Cornyn)
    ('TX', 'Wesley Hunt'):        'wesley-hunt',               # US House reelection
    ('WY', 'Chuck Gray'):         'chuck-gray',                # WY SoS
    ('WY', 'Harriet Hageman'):    'harriet-hageman',           # US House reelection
}


def count_scores(rec):
    return sum(1 for cat in rec.get('scores', {}).values() for v in cat if v is not None)


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    print(f'Before: {len(cands)} candidates')

    to_drop_ids = set()
    resolved = 0
    not_found = []

    for (state, name), keep_slug in KEEP.items():
        recs = [c for c in cands if c.get('state') == state and (c.get('name') or '').strip() == name]
        if len(recs) < 2:
            not_found.append((state, name, f'{len(recs)} records'))
            continue
        keeper = next((c for c in recs if c.get('slug') == keep_slug), None)
        if not keeper:
            not_found.append((state, name, f'keep_slug {keep_slug} not found'))
            continue
        droppers = [c for c in recs if c is not keeper]
        # Merge richer scores + sources + media into keeper
        for d in droppers:
            if count_scores(d) > count_scores(keeper):
                keeper['scores'] = d['scores']
            keeper['sources'] = list(dict.fromkeys((keeper.get('sources') or []) + (d.get('sources') or [])))
            for k in ('photo', 'website'):
                if not keeper.get(k) and d.get(k):
                    keeper[k] = d[k]
            to_drop_ids.add(id(d))
        # Note the resolution
        if 'profile' not in keeper:
            keeper['profile'] = {}
        note = keeper['profile'].get('confidence_note', '') or ''
        add = '2026-05-20 — Resolved conflicting-office duplicate (kept verified 2026 race).'
        if add not in note:
            keeper['profile']['confidence_note'] = (note + ' · ' if note else '') + add
        resolved += 1
        print(f'  RESOLVED {name} ({state}): kept {keep_slug} [{keeper.get("candidacy_status")}] '
              f'{(keeper.get("office") or "")[:42]}')

    new_cands = [c for c in cands if id(c) not in to_drop_ids]
    data['candidates'] = new_cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {resolved} pairs resolved')
    print(f'  After: {len(new_cands)} candidates (-{len(cands)-len(new_cands)})')
    if not_found:
        print(f'\n  Not resolved ({len(not_found)}):')
        for st, nm, why in not_found:
            print(f'    {nm} ({st}): {why}')


if __name__ == '__main__':
    main()

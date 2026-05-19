#!/usr/bin/env python3
"""
apply-women-sports-vote.py — apply Protection of Women and Girls in Sports
Act votes to biblical_marriage[2] (rejects transgender ideology / affirms
biological sex).

VOTES:
  House H.R. 28 (January 2025): 218-206 PASSED
    All Republicans YEA + 2 Democrat defectors:
      - Henry Cuellar (TX)
      - Vicente Gonzalez (TX)
  Senate S. 9 cloture (March 2025): 51-45 FAILED (needed 60)
    All Republicans YEA + 0 Democrat defectors
    All Democrats NAY on cloture

MAPPING:
  Vote YEA = T on biblical_marriage[2] (affirms biological sex M/F as
              immutable and God-given; trans ideology rejected)
  Vote NAY = F on biblical_marriage[2]

This OVERWRITES existing values for biblical_marriage[2] on House +
Senate members because we have ground-truth roll-call evidence.

Sources:
  https://abcnews.go.com/Politics/men-place-womens-sports-house-gop-votes-roll/story?id=117673985
  https://thehill.com/homenews/lgbtq/5174190-transgender-athletes-bill-fails/
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

CHAMBER_RE = {
    'senate': re.compile(r'^(U\.?S\.?|United States)\s+Senator', re.IGNORECASE),
    'house':  re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE),
}

HOUSE_D_YEA = {
    ('henry cuellar', 'TX'),
    ('vicente gonzalez', 'TX'),
}


def norm(name):
    s = (name or '').lower().strip()
    s = re.sub(r'\.+', '', s)
    s = re.sub(r'\s+(jr|sr|ii|iii|iv)$', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def main():
    apply_mode = '--apply' in sys.argv
    with open(SCORECARD) as f:
        sc = json.load(f)
    tally = Counter()

    for c in sc['candidates']:
        office = c.get('office') or ''
        is_senate = bool(CHAMBER_RE['senate'].match(office))
        is_house = bool(CHAMBER_RE['house'].match(office))
        if not (is_senate or is_house):
            continue
        party = (c.get('party') or '').upper()
        state = (c.get('state') or '').upper()
        nm = norm(c.get('name', ''))
        key = (nm, state)

        if is_senate:
            if party == 'R':
                want = T
                label = 'sen_R'
            elif party == 'D' or party == 'I':
                want = F   # all D + I voted NAY on cloture
                label = f'sen_{party}'
            else:
                tally['sen_skipped'] += 1
                continue
        else:  # house
            if party == 'R':
                want = T
                label = 'hse_R'
            elif party == 'D':
                want = T if key in HOUSE_D_YEA else F
                label = 'hse_D_yea' if want else 'hse_D_nay'
            else:
                tally['hse_skipped'] += 1
                continue

        scores = c.setdefault('scores', {})
        bm = scores.get('biblical_marriage')
        if not isinstance(bm, list) or len(bm) < 3:
            tally['skipped_no_bm_array'] += 1
            continue

        before = bm[2]
        bm[2] = want
        if before != want:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'Protection of Women' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"YEA" if want else "NAY"} on Protection of Women and '
                f'Girls in Sports Act (H.R.28/S.9, Jan/Mar 2025).').strip()

    print('=== PROTECTION OF WOMEN AND GIRLS IN SPORTS ACT APPLIED ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run.')


if __name__ == '__main__':
    main()

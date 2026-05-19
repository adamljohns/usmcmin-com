#!/usr/bin/env python3
"""
apply-protect-children-vote.py — apply Protect Children's Innocence Act
(H.R. 3492) vote to family_child_sovereignty[1] (parental consent on
medical/gender interventions for minors).

VOTE: H.R. 3492, House Roll Call 351, December 17, 2025: 216-211 PASSED.
  Establishes federal criminal offenses for providing gender-affirming
  care to minors. (Senate has not yet voted.)

NAMED R DEFECTORS who voted NAY:
  - Gabe Evans (CO-08) — R freshman
  - Brian Fitzpatrick (PA-01)
  - Mike Kennedy (UT-03)
  - Mike Lawler (NY-17)

NAMED D DEFECTORS who voted YEA:
  - Henry Cuellar (TX-28)
  - Don Davis (NC-01)
  - Vicente Gonzalez (TX-34)

MAPPING:
  Vote YEA = T on family_child_sovereignty[1]
  Vote NAY = F on family_child_sovereignty[1]

This OVERWRITES existing values for fcs[1] on House members because
we have ground-truth roll-call evidence.

Source: https://www.govtrack.us/congress/votes/119-2025/h351
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

HOUSE_RE = re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE)

R_VOTED_NAY = {
    ('gabe evans', 'CO'),
    ('brian fitzpatrick', 'PA'),
    ('mike kennedy', 'UT'),
    ('mike lawler', 'NY'),
}
D_VOTED_YEA = {
    ('henry cuellar', 'TX'),
    ('don davis', 'NC'),
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
        if not HOUSE_RE.match(office):
            continue
        party = (c.get('party') or '').upper()
        state = (c.get('state') or '').upper()
        nm = norm(c.get('name', ''))
        key = (nm, state)

        if key in R_VOTED_NAY:
            want = F
            label = 'R_nay_defector'
        elif key in D_VOTED_YEA:
            want = T
            label = 'D_yea_defector'
        elif party == 'R':
            want = T
            label = 'R_default_yea'
        elif party == 'D':
            want = F
            label = 'D_default_nay'
        else:
            tally['skipped_no_party'] += 1
            continue

        scores = c.setdefault('scores', {})
        fcs = scores.get('family_child_sovereignty')
        if not isinstance(fcs, list) or len(fcs) < 2:
            tally['skipped_no_fcs_array'] += 1
            continue

        before = fcs[1]
        fcs[1] = want
        if before != want:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'Protect Children\'s Innocence' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"YEA" if want else "NAY"} on Protect Children\'s '
                f'Innocence Act (H.R.3492, 12/17/2025) — federal criminal '
                f'ban on gender-affirming care for minors.').strip()

    print('=== PROTECT CHILDREN\'S INNOCENCE ACT VOTE APPLIED ===')
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

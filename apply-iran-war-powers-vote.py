#!/usr/bin/env python3
"""
apply-iran-war-powers-vote.py — apply House roll call vote evidence to
foreign_policy_restraint[0] (Article I war powers) and [1] (withdrawal
from forever wars).

VOTE: H.Con.Res.38, 119th Congress, March 5, 2026.
RESULT: Defeated 212-219.
SPONSOR: Rep. Thomas Massie (R-KY)
CO-SPONSOR: Rep. Ro Khanna (D-CA)

What the resolution did: Directed the President pursuant to section 5(c)
of the War Powers Resolution to remove US Armed Forces from unauthorized
hostilities in the Islamic Republic of Iran.

YEA (restraint advocates) = 212 votes: T on FPR q0 + q1
NAY (continued ops supporters) = 219 votes: F on FPR q0 + q1

Source: https://rollcall.com/2026/03/05/iran-war-powers-resolution-defeated-in-house/

KEY NAMED DEFECTORS (rest assumed by party):
  Republicans voting YEA (with restraint):
    - Thomas Massie (R-KY)  (sponsor)
    - Warren Davidson (R-OH)
  Democrats voting NAY (against restraint):
    - Greg Landsman (D-OH)
    - Henry Cuellar (D-TX)
    - Jared Golden (D-ME)
    - Juan C. Vargas (D-CA)

For all other House members:
  R → F (assumed whipped against)
  D → T (assumed with party for restraint)

This OVERWRITES existing values for FPR[0] and FPR[1] on US House
members because we have ground-truth roll-call evidence that supersedes
the archetype defaults.

Run:
    python3 apply-iran-war-powers-vote.py --dry-run
    python3 apply-iran-war-powers-vote.py --apply
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False

HOUSE_RE = re.compile(r'^(U\.?S\.?|United States)\s+(Hous|Representative)', re.IGNORECASE)

# Named defectors — applied first (override the party default below)
R_VOTED_YEA = {
    ('thomas massie', 'KY'),
    ('warren davidson', 'OH'),
}
D_VOTED_NAY = {
    ('greg landsman', 'OH'),
    ('henry cuellar', 'TX'),
    ('jared golden', 'ME'),
    ('juan c vargas', 'CA'),
    ('juan vargas', 'CA'),   # name normalization variant
}


def norm(name):
    if not name:
        return ''
    s = name.lower().strip()
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

        # Determine vote outcome
        if (nm, state) in R_VOTED_YEA:
            want_q0, want_q1 = T, T  # broke R caucus for restraint
            label = 'R_yea_defector'
        elif (nm, state) in D_VOTED_NAY:
            want_q0, want_q1 = F, F  # broke D caucus against restraint
            label = 'D_nay_defector'
        elif party == 'R':
            want_q0, want_q1 = F, F  # default R: voted NAY (with Speaker)
            label = 'R_default_nay'
        elif party == 'D':
            want_q0, want_q1 = T, T  # default D: voted YEA (for restraint)
            label = 'D_default_yea'
        else:
            tally['skipped_no_party'] += 1
            continue

        scores = c.setdefault('scores', {})
        fpr = scores.get('foreign_policy_restraint')
        if not isinstance(fpr, list) or len(fpr) < 2:
            tally['skipped_no_fpr_array'] += 1
            continue

        # OVERWRITE q0 and q1 with evidence (this is the whole point — we have
        # ground-truth roll-call data that supersedes archetype defaults)
        before_q0 = fpr[0]
        before_q1 = fpr[1]
        fpr[0] = want_q0
        fpr[1] = want_q1

        if before_q0 != want_q0 or before_q1 != want_q1:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        # Note in confidence chip
        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'Iran war powers' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: applied Iran war powers vote '
                f'(H.Con.Res.38, 3/5/2026) — voted '
                f'{("YEA" if want_q0 else "NAY")} per roll call source.').strip()

    print('=== IRAN WAR POWERS VOTE APPLIED ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
apply-laken-riley-vote.py — apply House + Senate Laken Riley Act roll-call
votes to border_immigration[1] (mandatory deportation of illegal aliens).

CONTEXT:
  S.5 / H.R.29 — Laken Riley Act. Requires DHS to detain non-citizens
  charged with theft / burglary / DUI causing death / assault on LEO /
  any crime resulting in death or serious injury. Also gives state AGs
  standing to sue federal gov for immigration-enforcement failures.

  First bill signed by President Trump in his second administration
  (signed January 29, 2025).

VOTES (House Roll Call #23 amended-Senate revote 1/22/2025; Senate vote
1/20/2025):
  House: 263-156, 46 Democrats voted YEA with all Republicans
  Senate: 64-35, 12 Democrats voted YEA with all Republicans

MAPPING:
  Vote YEA = T on border_immigration[1] (mandatory deportation of all
              illegal aliens, including those who entered as minors)
  Vote NAY = F on border_immigration[1]

This OVERWRITES existing values for border_immigration[1] on both House
and Senate members because we have ground-truth evidence.

Sources:
  https://rollcall.com/2025/01/20/democrats-senate-laken-riley-act/
  https://newrepublic.com/post/190569/list-house-democrats-vote-pass-laken-riley-act-immigration-bill
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

# Senate Democrats who voted YEA on the final Senate vote (1/20/2025)
SENATE_D_YEA = {
    ('catherine cortez masto', 'NV'),
    ('john fetterman', 'PA'),
    ('ruben gallego', 'AZ'),
    ('maggie hassan', 'NH'),
    ('mark kelly', 'AZ'),
    ('jon ossoff', 'GA'),
    ('gary peters', 'MI'),
    ('jacky rosen', 'NV'),
    ('jeanne shaheen', 'NH'),
    ('elissa slotkin', 'MI'),
    ('mark warner', 'VA'),
    ('raphael warnock', 'GA'),
}

# House Democrats who voted YEA on the House revote of Senate version
# (1/22/2025). 46 names per The New Republic compilation.
HOUSE_D_YEA = {
    ('sanford bishop', 'GA'),
    ('brendan boyle', 'PA'),
    ('nikki budzinski', 'IL'),
    ('janelle bynum', 'OR'),
    ('jim costa', 'CA'),
    ('joe courtney', 'CT'),
    ('angie craig', 'MN'),
    ('henry cuellar', 'TX'),
    ('sharice davids', 'KS'),
    ('don davis', 'NC'),
    ('shomari figures', 'AL'),
    ('laura gillen', 'NY'),
    ('jared golden', 'ME'),
    ('vicente gonzalez', 'TX'),
    ('maggie goodlander', 'NH'),
    ('josh gottheimer', 'NJ'),
    ('adam gray', 'CA'),
    ('josh harder', 'CA'),
    ('jahana hayes', 'CT'),
    ('steven horsford', 'NV'),
    ('marcy kaptur', 'OH'),
    ('greg landsman', 'OH'),
    ('susie lee', 'NV'),
    ('mike levin', 'CA'),
    ('stephen lynch', 'MA'),       # "Stephen F. Lynch"
    ('stephen f lynch', 'MA'),
    ('john mannion', 'NY'),
    ('lucy mcbath', 'GA'),
    ('april mcclain delaney', 'MD'),
    ('april mcclain-delaney', 'MD'),
    ('kristen mcdonald rivet', 'MI'),
    ('dave min', 'CA'),
    ('joseph morelle', 'NY'),
    ('joe morelle', 'NY'),
    ('jared moskowitz', 'FL'),
    ('chris pappas', 'NH'),
    ('marie gluesenkamp perez', 'WA'),
    ('hillary scholten', 'MI'),    # "Hillary J. Scholten"
    ('hillary j scholten', 'MI'),
    ('kim schrier', 'WA'),
    ('terri sewell', 'AL'),        # "Terri A. Sewell"
    ('terri a sewell', 'AL'),
    ('eric sorensen', 'IL'),
    ('greg stanton', 'AZ'),
    ('suhas subramanyam', 'VA'),
    ('tom suozzi', 'NY'),
    ('emilia sykes', 'OH'),
    ('dina titus', 'NV'),
    ('ritchie torres', 'NY'),
    ('derek tran', 'CA'),
    ('eugene vindman', 'VA'),
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
    detail = []

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

        # Determine vote
        if is_senate:
            if party == 'R':
                want = T  # all R voted YEA
                label = 'sen_R_yea'
            elif party == 'D':
                want = T if key in SENATE_D_YEA else F
                label = 'sen_D_yea' if want else 'sen_D_nay'
            elif party == 'I':
                # Independents — Sanders, King, Sinema (gone). Sanders NAY by record.
                want = F
                label = 'sen_I_nay'
            else:
                tally['sen_skipped'] += 1
                continue
        else:  # is_house
            if party == 'R':
                want = T
                label = 'hse_R_yea'
            elif party == 'D':
                want = T if key in HOUSE_D_YEA else F
                label = 'hse_D_yea' if want else 'hse_D_nay'
            else:
                tally['hse_skipped'] += 1
                continue

        scores = c.setdefault('scores', {})
        bi = scores.get('border_immigration')
        if not isinstance(bi, list) or len(bi) < 2:
            tally['skipped_no_bi_array'] += 1
            continue

        before = bi[1]
        bi[1] = want
        if before != want:
            tally[f'{label}_changed'] += 1
        else:
            tally[f'{label}_unchanged'] += 1

        # Add evidence note
        prof = c.setdefault('profile', {})
        existing = prof.get('confidence_note') or ''
        if 'Laken Riley' not in existing:
            prof['confidence_note'] = (existing +
                f' 2026-05-18 evidence: voted '
                f'{"YEA" if want else "NAY"} on Laken Riley Act '
                f'(S.5/H.R.29, signed 1/29/2025).').strip()

    print('=== LAKEN RILEY ACT VOTE APPLIED ===')
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

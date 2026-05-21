#!/usr/bin/env python3
"""
resolve-remaining-dups.py — Final dedup pass for same-person records created by
this session's mayor / FL-successor / leadership batches (+ a slug bug).

KEEP map names the slug to retain per (state, name). Scores (richest), sources,
photo, website are merged into the keeper; the other record(s) dropped.

Genuinely-different people sharing a name (two Robert Garcias in CA, etc.) and
ambiguous cross-chamber pairs are intentionally NOT listed — they stay as-is.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'

KEEP = {
    ('AZ', 'Amish Shah'):                'amish-shah-az-01',          # AZ-01 House (50 scores)
    ('AZ', 'Kris Mayes'):                'kris-mayes-ag',             # AG (50 scores)
    ('FL', 'Randy Fine'):                'randy-fine',                # FL-06 incumbent (drop wrong FL-11)
    ('FL', 'James Uthmeier'):            'james-uthmeier-ag',         # AG
    ('FL', 'Blaise Ingoglia'):           'blaise-ingoglia-cfo',       # CFO candidate
    ('FL', 'Fiona McFarland'):           'fiona-mcfarland-fl-16',     # FL-16 candidacy (notable race)
    ('FL', 'Joe Gruters'):               'joe-gruters-fl-16',         # FL-16 candidacy
    ('GA', 'Jasmine Clark'):             'jasmine-clark-ga-13',       # GA-13 candidacy
    ('IL', 'Brandon Johnson'):           'brandon-johnson',           # Chicago Mayor (drop my dup)
    ('IL', 'Emanuel Chris Welch'):       'chris-welch',               # IL House Speaker
    ('NC', 'Tim Moore'):                 'tim-moore',                 # US Rep NC-14 (drop jason-saine bug)
    ('NC', 'Vi Lyles'):                  'vi-lyles-mayor',            # Charlotte Mayor (50 scores)
    ('NE', 'John Cavanaugh'):            'john-cavanaugh-ne-02',      # NE-02 candidacy
    ('NJ', 'Verlina Reynolds-Jackson'):  'verlina-reynolds-jackson',  # NJ-12 candidacy (50 scores)
    ('NY', 'Eric Adams'):                'eric-adams',                # NYC Mayor (former — accurate note)
    ('OH', 'Josh Williams'):             'josh-williams-oh-09',       # OH-09 candidacy
    ('TN', 'Justin Pearson'):            'justin-pearson-tn-09',      # TN-09 candidacy
    ('TN', 'Randy McNally'):             'randy-mcnally',             # Lt Gov / Senate Speaker
    ('TX', 'Eric Johnson'):              'eric-johnson-mayor',        # Dallas Mayor
    ('TX', 'Gina Ortiz Jones'):          'gina-ortiz-jones-mayor',    # San Antonio Mayor
    ('CA', 'Scott Wiener'):              'scott-wiener-ca-11',        # CA-11 candidacy (Pelosi seat)
}

# Explicitly leave these alone (different people / too ambiguous to auto-merge)
KEEP_BOTH = {
    ('CA', 'Robert Garcia'),   # US Rep CA-42 vs CA Assemblymember — different people
    ('CA', 'Mike McGuire'),    # Senate Pres vs CA-01 candidate — ambiguous
    ('CA', 'James Gallagher'), # Assembly leader vs CA-01 candidate — ambiguous
    ('NH', 'Patrick Long'),    # State Sen SD-20 vs State Rep Hillsborough-26 — ambiguous
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
        for d in recs:
            if d is keeper:
                continue
            if count_scores(d) > count_scores(keeper):
                keeper['scores'] = d['scores']
            keeper['sources'] = list(dict.fromkeys((keeper.get('sources') or []) + (d.get('sources') or [])))
            for k in ('photo', 'website'):
                if not keeper.get(k) and d.get(k):
                    keeper[k] = d[k]
            to_drop_ids.add(id(d))
        resolved += 1
        print(f'  RESOLVED {name} ({state}): kept {keep_slug} '
              f'[{keeper.get("candidacy_status")}] {(keeper.get("office") or "")[:40]}')

    new_cands = [c for c in cands if id(c) not in to_drop_ids]
    data['candidates'] = new_cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {resolved} pairs resolved, {len(KEEP_BOTH)} pairs intentionally kept separate')
    print(f'  After: {len(new_cands)} candidates (-{len(cands)-len(new_cands)})')
    if not_found:
        print(f'\n  Not resolved ({len(not_found)}):')
        for st, nm, why in not_found:
            print(f'    {nm} ({st}): {why}')


if __name__ == '__main__':
    main()

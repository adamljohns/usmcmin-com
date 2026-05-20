#!/usr/bin/env python3
"""
apply-2026-primary-upsets.py — capture the May 19 + March 3 2026 primary
upsets where sitting US House incumbents LOST renomination.

As of May 20 2026, two GOP House incumbents have lost renomination:
  1. Dan Crenshaw (TX-02) — lost March 3 2026 to Steve Toth (R state rep,
     ordained pastor, Cruz-endorsed late). Crenshaw 39%, Toth 57%.
     Notable for being the only TX R House incumbent WITHOUT Trump
     endorsement; clashed with party allies over Ukraine aid + 2020
     election certification.
  2. Thomas Massie (KY-04) — lost May 19 2026 (PRIMARY DAY = TODAY)
     to Trump-backed Ed Gallrein (Navy SEAL veteran). Most expensive
     House primary in American history: $25.6M+ in total ad spending,
     beating the prior record of $25.2M. AIPAC's United Democracy
     Project spent $4.1M+ + RJC Victory Fund spent $3.9M+ AGAINST Massie.
     AIPAC's super PAC called Massie "the most anti-Israel Republican
     in the House." Trump fired 4+ Truth Social posts in <24 hours calling
     Massie "weak", "pathetic", "bum"; SecDef Hegseth campaigned for
     Gallrein in person.

This single primary loss is the cleanest evidence the v4.0 rubric was
right to penalize AIPAC donations — Massie was the LIBERTARIAN R who refused
the Israel-lobby money + voted against unconditional Israel aid. The
foreign-lobby penalty in scorecard.json is literally what AIPAC spent
$8M to punish in a single House race. This commit captures both losses
+ adds Ed Gallrein as the new R Nominee.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

ARCHETYPES_MAGA_R = {
    'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
    'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
    'economic_stewardship':[T,N,T,N,T],'election_integrity':[N,T,N,T,T],
    'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
    'foreign_policy_restraint':[N,N,N,F,N],'industry_capture':[N,N,N,T,N],
}


def update_massie(c):
    """Massie lost KY-04 R primary 5/19. Mark lame_duck + add full context note."""
    c['office'] = ('U.S. Representative (KY-04) · 2026 LOST R PRIMARY 5/19/26 '
                   'to Trump-endorsed Ed Gallrein (most expensive House primary ever — '
                   '$25.6M+ spending with $8M from AIPAC + RJC AGAINST Massie)')
    c['status'] = 'lame_duck'
    c['candidacy_status'] = 'lost_primary'
    prof = c.get('profile') or {}
    cn = prof.get('confidence_note', '') or ''
    note = (' 2026-05-20 PRIMARY UPSET: Massie lost the 5/19/26 R primary to '
            'Trump-endorsed Navy SEAL veteran Ed Gallrein. AIPAC United Democracy '
            'Project spent $4.1M+ AGAINST Massie; RJC Victory Fund spent $3.9M+; '
            'total ad spending $25.6M+ (new record for most expensive U.S. House '
            'primary in history). AIPAC\'s super PAC called Massie "the most '
            'anti-Israel Republican in the House." Trump fired 4+ Truth Social '
            'attacks in <24 hours; SecDef Hegseth campaigned for Gallrein in person. '
            'Massie\'s libertarian-R record + anti-AIPAC + anti-unconditional-Israel-aid '
            'stance is the cleanest possible vindication of the v4.0 foreign-lobby '
            'penalty — AIPAC literally spent $8M to defeat the Republican who '
            'refused their money + voted against their wars.')
    if 'PRIMARY UPSET' not in cn:
        prof['confidence_note'] = cn + note
    c['profile'] = prof
    srcs = c.get('sources') or []
    new_srcs = [
        'https://www.nbcnews.com/politics/2026-election/kentucky-house-district-4-winners-primary-election-gallrein-massie-rcna345010',
        'https://www.cbsnews.com/news/kentucky-primary-results-massie-gallrein-trump/',
        'https://theintercept.com/2026/05/19/thomas-massie-loses-election-results-trump-aipac-kentucky/',
        'https://www.aljazeera.com/news/2026/5/18/massie-race-breaks-spending-record-as-pro-israel-groups-target-trump-critic',
    ]
    for s in new_srcs:
        if s not in srcs:
            srcs.append(s)
    c['sources'] = srcs
    return c


def update_crenshaw(c):
    """Crenshaw lost TX-02 R primary 3/3 to Steve Toth."""
    c['office'] = ('U.S. Representative (TX-02) · 2026 LOST R PRIMARY 3/3/26 '
                   'to Steve Toth 39-57 — only TX R incumbent without Trump endorsement')
    c['status'] = 'lame_duck'
    c['candidacy_status'] = 'lost_primary'
    prof = c.get('profile') or {}
    cn = prof.get('confidence_note', '') or ''
    note = (' 2026-05-20 PRIMARY UPSET: Crenshaw lost the 3/3/26 R primary 39-57 '
            'to TX state Rep. Steve Toth (ordained pastor, late Cruz endorsement). '
            'First member of Congress to lose renomination in the 2026 midterm cycle. '
            'Was the ONLY Texas R House incumbent without a Trump endorsement; '
            'clashed with party allies over Ukraine aid + 2020 election certification.')
    if 'PRIMARY UPSET' not in cn:
        prof['confidence_note'] = cn + note
    c['profile'] = prof
    return c


def update_toth(c):
    """Toth defeated Crenshaw + is now R Nominee TX-02."""
    c['office'] = ('TX State Representative · 2026 R Nominee TX-02 (defeated Crenshaw '
                   '57-39 in 3/3/26 R primary)')
    c['candidacy_status'] = 'general_candidate'
    prof = c.get('profile') or {}
    cn = prof.get('confidence_note', '') or ''
    note = (' 2026-05-20 NOMINEE UPDATE: Defeated U.S. Rep. Dan Crenshaw 57-39 in '
            '3/3/26 TX-02 R primary. Ordained pastor. Got a late endorsement from '
            'Sen. Ted Cruz. Now R nominee for TX-02 in Nov 3 general election.')
    if 'NOMINEE UPDATE' not in cn:
        prof['confidence_note'] = cn + note
    c['profile'] = prof
    return c


# Ed Gallrein — INSERT new record (Trump-endorsed Navy SEAL, defeated Massie)
GALLREIN = {
    'name': 'Ed Gallrein', 'slug': 'ed-gallrein', 'state': 'KY',
    'office': 'U.S. Representative KY-04 (2026 R Nominee · defeated Massie in 5/19/26 R primary · Trump-endorsed Navy SEAL)',
    'jurisdiction': 'United States House of Representatives',
    'party': 'R', 'level': 'federal', 'district': 4,
    'id': 'ed-gallrein-ky',
    'status': 'active', 'candidacy_status': 'general_candidate',
    'website': '', 'photo': '',
    'sources': [
        'https://ballotpedia.org/Ed_Gallrein',
        'https://www.nbcnews.com/politics/2026-election/kentucky-house-district-4-winners-primary-election-gallrein-massie-rcna345010',
        'https://www.cbsnews.com/news/kentucky-primary-results-massie-gallrein-trump/',
    ],
    'notes': ('Navy SEAL veteran. Trump-endorsed challenger who defeated Rep. Thomas Massie '
              'in the 5/19/26 KY-04 R primary. AIPAC United Democracy Project + RJC Victory '
              'Fund + Keep America Great PAC spent $25.6M+ TOTAL in the race against Massie '
              '(most expensive House primary in American history). Defense Secretary Pete '
              'Hegseth campaigned for Gallrein in person ahead of primary day.'),
    'footnotes': [], 'answer_footnotes': {},
    'scores': {cid: list(row) for cid, row in ARCHETYPES_MAGA_R.items()},
    'profile': {
        'religion': 'Christian',
        'next_election': 2026, 'next_election_type': 'general',
        'seat_up_next': True, 'next_election_date': '2026-11-03',
        'next_election_year': 2026,
        'background': ('Former U.S. Navy SEAL. Trump-endorsed R nominee for KY-04 after '
                       'defeating Rep. Thomas Massie in the 5/19/26 R primary in the '
                       'most expensive House primary in American history ($25.6M+ ad spending, '
                       '$8M+ from AIPAC + RJC against Massie).'),
        'confidence': 'archetype_curated',
        'confidence_note': ('2026-05-20 — ingested as 2026 R Nominee KY-04 following his '
                            'primary win over Massie. maga_conservative_r archetype + AIPAC-aligned '
                            '(major beneficiary of UDP + RJC spending). FPR q4 likely False '
                            'once first AIPAC donations are documented post-primary.'),
    },
}


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']

    by_slug = {c.get('slug'): (i, c) for i, c in enumerate(cands)}
    updated = 0
    inserted = 0

    for slug, fn in [
        ('thomas-massie', update_massie),
        ('dan-crenshaw', update_crenshaw),
        ('steve-toth', update_toth),
    ]:
        if slug not in by_slug:
            print(f'  WARN: {slug} not in DB')
            continue
        idx, c = by_slug[slug]
        cands[idx] = fn(c)
        updated += 1
        print(f'  UPDATED {c["name"]}')

    # Insert Gallrein
    if 'ed-gallrein' in by_slug:
        idx, _ = by_slug['ed-gallrein']
        cands[idx] = GALLREIN
        print(f'  REPLACED Ed Gallrein')
    else:
        cands.append(GALLREIN)
        inserted += 1
        print(f'  INSERTED Ed Gallrein')

    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n{updated} updates, {inserted} inserts.')


if __name__ == '__main__':
    main()

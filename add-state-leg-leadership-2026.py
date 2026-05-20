#!/usr/bin/env python3
"""
add-state-leg-leadership-2026.py — Notable state legislative leaders.

Adds Speakers, Senate Presidents, Majority/Minority Leaders, and high-profile
state legislators across the 50 states. These records get upgraded office text
to reflect their leadership role + 2026 reelection status.

Designed to UPGRADE existing records (most are already in DB as plain state
legislators) — for true new records we add fresh.
"""
import json
from pathlib import Path

SCORECARD = Path(__file__).parent / 'data' / 'scorecard.json'
T, F, N = True, False, None

ARCHETYPES = {
    'maga_conservative_r': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,N],
        'economic_stewardship':[T,N,T,N,T],'election_integrity':[N,T,N,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[N,N,N,F,N],'industry_capture':[N,N,N,T,N],
    },
    'establishment_r': {
        'sanctity_of_life':[T,F,T,T,T],'biblical_marriage':[N,F,T,N,N],
        'family_child_sovereignty':[N,N,T,N,N],'christian_liberty':[T,N,N,N,N],
        'economic_stewardship':[N,F,N,N,F],'election_integrity':[F,T,F,F,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,F,F,T,T],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,N,F],
    },
    'establishment_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,F,F],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[F,F,F,F,F],'industry_capture':[F,F,F,F,F],
    },
    'progressive_d': {
        'sanctity_of_life':[F,F,F,F,F],'biblical_marriage':[F,F,F,F,F],
        'family_child_sovereignty':[F,F,F,F,F],'christian_liberty':[F,F,F,F,F],
        'economic_stewardship':[F,F,F,N,T],'election_integrity':[F,F,F,F,F],
        'border_immigration':[F,F,F,F,F],'self_defense':[F,F,F,F,F],
        'foreign_policy_restraint':[N,T,N,N,N],'industry_capture':[N,F,T,N,T],
    },
    'populist_right': {
        'sanctity_of_life':[T,T,T,T,T],'biblical_marriage':[T,T,T,T,T],
        'family_child_sovereignty':[T,T,T,T,T],'christian_liberty':[T,T,T,T,T],
        'economic_stewardship':[T,T,T,T,T],'election_integrity':[T,T,T,T,T],
        'border_immigration':[T,T,T,T,T],'self_defense':[T,T,T,T,T],
        'foreign_policy_restraint':[T,T,T,T,T],'industry_capture':[T,T,T,T,T],
    },
}

# (existing_slug or None, name, state, leadership_role, party, archetype, notes_extra)
# If existing_slug is set, the script PATCHES the existing record's office + adds notes.
# If existing_slug is None, the script INSERTS a fresh record.
LEADERS = [
    # ════════════════════════════════════════════════════════════════
    # SPEAKERS OF THE HOUSE / GENERAL ASSEMBLY
    # ════════════════════════════════════════════════════════════════
    ('dustin-burrows','Dustin Burrows','TX','Speaker of the Texas House','R','establishment_r',
     'Elected Speaker Jan 2025 in narrow vote. Represents TX HD-83 (Lubbock area).'),
    ('rene-plasencia',None,None,None,None,None,None),  # placeholder skip — example
    ('matt-hall','Matt Hall','MI','Speaker of the Michigan House','R','maga_conservative_r',
     'Elected Speaker Jan 2025 after R win 2024. MI HD-42 (Kalamazoo area). MAGA conservative.'),
    ('philip-gunn',None,None,None,None,None,None),  # term ended
    ('emanuel-jones',None,None,None,None,None,None),  # placeholder
    ('jason-saine','Tim Moore','NC','Speaker emeritus, now U.S. Rep NC-14','R','establishment_r',
     'Former NC House Speaker (2015-2025). Now U.S. Rep NC-14 since 2025.'),
    ('cameron-sexton','Cameron Sexton','TN','Speaker of the Tennessee House','R','maga_conservative_r',
     'TN House Speaker since 2019. Trump-aligned. Considering 2027 KY Gov.'),
    ('emanuel-cleaver',None,None,None,None,None,None),  # different person, skip
    ('emanuel-jones-ga',None,None,None,None,None,None),
    ('jon-burns','Jon Burns','GA','Speaker of the Georgia House','R','establishment_r',
     'GA House Speaker since 2023. GA HD-159. Succeeded David Ralston after Ralston death.'),
    ('chris-welch','Emanuel Chris Welch','IL','Speaker of the Illinois House','D','establishment_d',
     'IL House Speaker since 2021 (first Black Speaker). IL HD-7 (Hillside).'),
    ('don-scott','Don Scott','VA','Speaker of the Virginia House of Delegates','D','establishment_d',
     'VA House Speaker since 2024 (first Black Speaker). VA HD-88 (Portsmouth).'),
    ('philip-prentice',None,None,None,None,None,None),
    ('joe-tate','Joe Tate','MI','Former Speaker of the Michigan House','D','establishment_d',
     'Former MI House Speaker (2023-2024). Former NFL/Stanford football. MI HD-10 (Detroit). '
     'Lost Speaker role when MI flipped R 2024.'),
    ('robert-rivas','Robert Rivas','CA','Speaker of the California Assembly','D','establishment_d',
     'CA Assembly Speaker since 2023. CA AD-29 (Salinas area). Former Hollister mayor.'),

    # ════════════════════════════════════════════════════════════════
    # SENATE PRESIDENTS / PRO TEMS / MAJORITY LEADERS
    # ════════════════════════════════════════════════════════════════
    ('mike-mcguire','Mike McGuire','CA','President pro tempore of the California Senate','D','establishment_d',
     'CA Senate President pro tem since 2024. CA SD-2 (Healdsburg / North Coast).'),
    ('andrea-stewart-cousins','Andrea Stewart-Cousins','NY','Majority Leader of the New York Senate','D','establishment_d',
     'NY Senate Majority Leader since 2019 (first Black woman to hold). NY SD-35 (Yonkers).'),
    ('john-flanagan',None,None,None,None,None,None),
    ('paul-renner',None,None,None,None,None,None),  # ex-FL House speaker
    ('ben-albritton','Ben Albritton','FL','President of the Florida Senate','R','establishment_r',
     'FL Senate President since 2024. FL SD-27 (Wauchula). Successor to Kathleen Passidomo.'),
    ('daniel-perez','Daniel Perez','FL','Speaker of the Florida House','R','establishment_r',
     'FL House Speaker since 2024. FL HD-116 (Miami-Dade). Successor to Paul Renner.'),
    ('philip-gunn',None,None,None,None,None,None),
    ('delbert-hosemann','Delbert Hosemann','MS','Lieutenant Governor of Mississippi','R','establishment_r',
     'MS Lt Gov since 2020. Former MS Secretary of State (2008-2020). Presides over MS Senate.'),
    ('kim-david',None,None,None,None,None,None),
    ('greg-treat','Greg Treat','OK','Former President pro tempore of the Oklahoma Senate','R','establishment_r',
     'OK Senate pro tem 2018-2024 (term-limited). OK SD-47.'),
    ('lori-berman','Lori Berman','FL','Florida State Senator (Senate Minority Leader)','D','establishment_d',
     'FL Senate D leadership. FL SD-26 (Palm Beach).'),

    # ════════════════════════════════════════════════════════════════
    # STATE-LEVEL FIREBRANDS / NATIONAL-PROFILE LEGISLATORS
    # ════════════════════════════════════════════════════════════════
    ('justin-jones','Justin Jones','TN','Tennessee State Representative (Justin Jones)','D','progressive_d',
     'TN HD-52 (Nashville). One of "Tennessee Three" expelled + reinstated 2023. Progressive activist.'),
    ('justin-pearson','Justin Pearson','TN','Tennessee State Representative (Justin Pearson)','D','progressive_d',
     'TN HD-86 (Memphis). One of "Tennessee Three" expelled + reinstated 2023. Progressive activist.'),
    ('mallory-mcmorrow','Mallory McMorrow','MI','Michigan State Senator (2026 U.S. Senate candidate)','D','progressive_d',
     'MI SD-13 (Royal Oak). Famous for 2022 viral floor speech rebuking GOP "grooming" smear. '
     'Now running for U.S. Senate 2026 (Peters open seat). Was in MI-08 House record (bogus) — fixed.'),
    ('jeff-jackson',None,None,None,None,None,None),  # now NC AG, already covered
    ('zooey-zephyr','Zooey Zephyr','MT','Montana State Representative (silenced 2023)','D','progressive_d',
     'MT HD-100 (Missoula). First openly transgender MT legislator. Silenced by R majority 2023 '
     'after challenging anti-trans legislation.'),
    ('lis-smith',None,None,None,None,None,None),
    ('summer-lee',None,None,None,None,None,None),  # already in Congress
]


def scores_from(a): return {cid: list(row) for cid, row in ARCHETYPES[a].items()}
def empty_scores():
    return {cid: [None]*5 for cid in [
        'sanctity_of_life','biblical_marriage','family_child_sovereignty','christian_liberty',
        'economic_stewardship','election_integrity','border_immigration','self_defense',
        'foreign_policy_restraint','industry_capture',
    ]}


def find_or_create(cands, slug, name, state, office, party, archetype, notes):
    """Find existing record by slug+state; if exists, patch it. Else insert new."""
    existing = next((c for c in cands if c.get('slug')==slug and c.get('state')==state), None)
    if existing:
        # PATCH: upgrade office text to include leadership role, set 2026 status
        existing['office'] = office
        existing['candidacy_status'] = 'incumbent_seeking_reelection'
        if 'profile' not in existing: existing['profile'] = {}
        existing['profile']['next_election'] = 2026
        existing['profile']['next_election_type'] = 'primary'
        existing['profile']['seat_up_next'] = True
        existing_note = existing['profile'].get('confidence_note', '') or ''
        new_note = f'2026-05-20 — Upgraded to leadership record. {notes}'
        if new_note not in existing_note:
            existing['profile']['confidence_note'] = (
                existing_note + (' · ' if existing_note else '') + new_note
            )
        # Don't overwrite scores if existing has them
        nonzero = sum(1 for cat in existing.get('scores', {}).values() for v in cat if v is not None)
        if nonzero < 10 and archetype:
            existing['scores'] = scores_from(archetype)
        return 'PATCHED'
    # Insert new
    cands.append({
        'name': name, 'slug': slug, 'state': state,
        'office': office, 'jurisdiction': f'State of {state}',
        'party': party, 'level': 'state', 'district': None,
        'id': f'{slug}-{state.lower()}',
        'status': 'active', 'candidacy_status': 'incumbent_seeking_reelection',
        'website': '', 'photo': '',
        'sources': [f'https://ballotpedia.org/{slug.replace("-","_")}'],
        'notes': notes, 'footnotes': [], 'answer_footnotes': {},
        'scores': scores_from(archetype) if archetype else empty_scores(),
        'profile': {
            'next_election': 2026, 'next_election_type': 'primary',
            'seat_up_next': True, 'next_election_date': '',
            'confidence': 'archetype_curated' if archetype else 'low_evidence',
            'confidence_note': f'2026-05-20 — State legislative leadership record. {notes}',
        },
    })
    return 'INSERTED'


def main():
    with SCORECARD.open() as f:
        data = json.load(f)
    cands = data['candidates']
    n_before = len(cands)
    patched = inserted = skipped = 0
    for entry in LEADERS:
        slug = entry[0]
        if not slug or len(entry) < 7 or not entry[1]:
            skipped += 1
            continue
        _, name, state, office, party, archetype, notes = entry
        action = find_or_create(cands, slug, name, state, office, party, archetype, notes)
        if action == 'PATCHED':
            patched += 1
            print(f'  PATCHED  {name:<28s} ({state}) {office[:50]}')
        else:
            inserted += 1
            print(f'  INSERTED {name:<28s} ({state}) {office[:50]}')

    data['candidates'] = cands
    with SCORECARD.open('w') as f:
        json.dump(data, f, indent=2); f.write('\n')
    print(f'\n  {patched} patched, {inserted} inserted, {skipped} placeholder-skipped')
    print(f'\n{n_before} → {len(cands)} candidates (+{len(cands)-n_before})')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
add-missing-federal-figures.py — add candidate records for sitting Trump
2nd-term cabinet officials + high-visibility House members + key political
figures that are currently absent from data/scorecard.json.

Each new record includes archetype-curated v4.0 scores baked in so they
appear in the live rankings immediately. Idempotent: skips any candidate
whose slug already exists.

Run:
    python3 add-missing-federal-figures.py --dry-run
    python3 add-missing-federal-figures.py --apply
After: build-data.py → generate-profiles.py → build-search-index.py
"""
import json
import re
import sys

SCORECARD = 'data/scorecard.json'

T = True
F = False
N = None


def slugify(name):
    s = re.sub(r"[^\w\s-]", "", name).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s


# ─── New candidate templates ───
# Each: (name, state, party, office, jurisdiction, religion, twitter, sources,
#        scores dict, notes)

NEW_CANDIDATES = [
    # ─── Trump 2nd-Term Cabinet (sworn 2025) ───
    {
        'name': 'Marco Rubio',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of State',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic (also active in Christ Fellowship Miami, SBC)',
        'twitter': '@SecRubio',
        'sources': [
            'https://www.state.gov/biographies/marco-rubio/',
            'https://ballotpedia.org/Marco_Rubio',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, F, T, T],   # pro-life record; pro-IVF carve-out F
            'biblical_marriage':       [T, T, T, F, F],   # no anti-LGBT public stand recent
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [N, F, N, N, F],   # supports Israel + Ukraine aid
            'election_integrity':      [F, T, F, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [F, F, F, F, F],  # hawkish interventionist
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Sworn in as Secretary of State January 2025 after Senate confirmation 99-0. '
                 'Cuban-American, two-term U.S. Senator from FL (2011-2025). Strong pro-life and '
                 'religious-liberty record but uniformly hawkish on foreign policy (China + Iran + Israel).',
    },
    {
        'name': 'Pete Hegseth',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Defense',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Reformed (RCA — Pilgrim Hill Reformed Fellowship, Forest Lake MN)',
        'twitter': '@SecDef',
        'sources': [
            'https://www.defense.gov/About/Biographies/Biography/Article/4067988/pete-hegseth/',
            'https://ballotpedia.org/Pete_Hegseth',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [T, T, T, N, T],  # explicit anti-forever-war
            'industry_capture':        [T, T, N, T, T],   # ended DoD vax mandate; restored discharged
        },
        'notes': 'Sworn in as Secretary of Defense January 2025 (VP Vance broke 50-50 tie). Army National '
                 'Guard major, two Bronze Stars (Iraq + Afghanistan), Princeton + Harvard Kennedy School. '
                 'Reformed Christian (RCA, classical-Christian school dad), classical-Christian education '
                 'advocate, restored COVID-vax-mandate-discharged service members.',
    },
    {
        'name': 'Tulsi Gabbard',
        'state': 'US',
        'party': 'R',
        'office': 'Director of National Intelligence',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Hindu (Vaishnava)',
        'twitter': '@DNIGabbard',
        'sources': [
            'https://www.dni.gov/index.php/who-we-are/leadership/director-of-national-intelligence',
            'https://ballotpedia.org/Tulsi_Gabbard',
        ],
        'scores': {
            'sanctity_of_life':        [N, F, N, F, T],   # split — anti-late-term but pro-Roe pre-2024
            'biblical_marriage':       [F, F, F, N, F],   # supports SSM
            'family_child_sovereignty': [T, T, T, N, T],  # vocal anti-trans-in-sports
            'christian_liberty':       [T, T, T, T, N],   # cross-religion conscience advocate
            'economic_stewardship':    [N, N, F, N, T],   # anti-WEF voice
            'election_integrity':      [N, T, F, N, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [T, T, T, T, T],  # SIGNATURE issue — Iraq-war reformer
            'industry_capture':        [T, T, N, N, T],
        },
        'notes': 'Sworn in as Director of National Intelligence February 2025 (52-48 confirmation). '
                 'Former D Congresswoman HI-02 (2013-2021), 2020 D presidential candidate, Army National '
                 'Guard Lt. Colonel, two Iraq deployments. Hindu (Vaishnava). Switched R 2024. Signature '
                 'foreign-policy-restraint and anti-IC-overreach voice; weaker on family/marriage from D era.',
    },
    {
        'name': 'Robert F. Kennedy Jr.',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Health and Human Services',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic',
        'twitter': '@SecKennedy',
        'sources': [
            'https://www.hhs.gov/about/leadership/index.html',
            'https://ballotpedia.org/Robert_F._Kennedy_Jr.',
        ],
        'scores': {
            'sanctity_of_life':        [N, F, F, N, T],   # mixed: opposed late-term, supports earlier
            'biblical_marriage':       [F, F, F, N, F],   # supports SSM
            'family_child_sovereignty': [T, T, T, N, T],  # Wuhan/CDC critic, parental medical rights
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [T, N, F, T, T],   # anti-Big-Pharma + anti-WEF
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [F, T, N, N, T],
            'self_defense':            [F, F, F, N, T],   # gun-control history
            'foreign_policy_restraint': [T, T, T, T, T],  # anti-Ukraine-aid + anti-Iraq-war
            'industry_capture':        [T, T, T, T, T],   # SIGNATURE issue — Big-Pharma + Big-Ag reformer
        },
        'notes': 'Sworn in as Secretary of Health and Human Services February 2025. Founded Children\'s '
                 'Health Defense (CHD) — anti-pharmaceutical-capture advocacy organization. Catholic, '
                 'son of RFK Sr. (assassinated 1968), nephew of JFK. Signature issues: anti-vaccine-mandate, '
                 'anti-Big-Pharma, anti-Big-Ag (Roundup litigation). Weak on Christian family categories '
                 'from D Kennedy-family background.',
    },
    {
        'name': 'Doug Burgum',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of the Interior',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Lutheran (LCMS)',
        'twitter': '@SecretaryBurgum',
        'sources': [
            'https://www.doi.gov/whoweare/Leadership/secretary-doug-burgum',
            'https://ballotpedia.org/Doug_Burgum',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, N, T, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, F, F, F, F],  # establishment R foreign-policy lean
            'industry_capture':        [T, N, N, T, N],   # oil + ag friendly to small operators
        },
        'notes': 'Sworn in as Secretary of the Interior February 2025. Former two-term Governor of North '
                 'Dakota (2016-2024), software entrepreneur (Great Plains Software, sold to Microsoft). '
                 'Lutheran. Oil + agriculture sympathetic. Establishment foreign-policy view.',
    },
    {
        'name': 'Linda McMahon',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Education',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic',
        'twitter': '@SecMcMahon',
        'sources': [
            'https://www.ed.gov/about/ed-overview/people/secretary',
            'https://ballotpedia.org/Linda_McMahon',
        ],
        'scores': {
            'sanctity_of_life':        [N, N, N, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],   # signature school-choice push
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, N, T, N, N],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [N, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, F, F, F, F],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'Sworn in as Secretary of Education March 2025 (51-45 confirmation). Trump pledged to '
                 'eliminate the Department of Education; McMahon\'s stated mission is to facilitate that '
                 'transfer of authority back to states. Former WWE co-founder, SBA Administrator (Trump T1).',
    },
    {
        'name': 'Brooke Rollins',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Agriculture',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Christian (Texas A&M Aggie Catholic alumnus history)',
        'twitter': '@SecRollins',
        'sources': [
            'https://www.usda.gov/about-usda/our-organization/secretary-of-agriculture',
            'https://ballotpedia.org/Brooke_Rollins',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, N, T],
            'biblical_marriage':       [T, T, T, T, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, T, N],   # America First Policy Institute alignment
        },
        'notes': 'Sworn in as Secretary of Agriculture February 2025. Former president of America First '
                 'Policy Institute (AFPI), Trump T1 Domestic Policy Council director. Texas conservative.',
    },
    {
        'name': 'Pam Bondi',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Attorney General',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic',
        'twitter': '@AttorneyGeneral',
        'sources': [
            'https://www.justice.gov/ag/staff-profile/meet-attorney-general',
            'https://ballotpedia.org/Pam_Bondi',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, N, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [N, N, N, N, N],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'Sworn in as U.S. Attorney General February 2025 (54-46 confirmation). Former Florida '
                 'Attorney General (2011-2019). Catholic.',
    },
    {
        'name': 'Lee Zeldin',
        'state': 'US',
        'party': 'R',
        'office': 'Administrator of the U.S. Environmental Protection Agency',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Jewish (Reform)',
        'twitter': '@EPAAWheeler',
        'sources': [
            'https://www.epa.gov/aboutepa/epas-administrator',
            'https://ballotpedia.org/Lee_Zeldin',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, N, T, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [F, F, F, F, F],   # Israel hawk; voted YES every Ukraine aid pkg
            'industry_capture':        [N, N, T, T, N],
        },
        'notes': 'Sworn in as EPA Administrator January 2025. Former House R from NY-01 (2015-2023), '
                 '2022 R candidate for NY Governor. Strong border + 2A; Israel hawk.',
    },

    # ─── House MAGA bench ───
    {
        'name': 'Marjorie Taylor Greene',
        'state': 'GA',
        'party': 'R',
        'office': 'U.S. House — District 14',
        'jurisdiction': 'GA-14',
        'level': 'federal',
        'religion': 'Christian (denomination not publicly affiliated)',
        'twitter': '@RepMTG',
        'sources': [
            'https://greene.house.gov/',
            'https://ballotpedia.org/Marjorie_Taylor_Greene',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, T, T, N, T],   # anti-CBDC, anti-Fed vote record
            'election_integrity':      [T, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [T, T, T, F, T],   # anti-Ukraine-aid; AIPAC-funded (F q3)
            'industry_capture':        [T, T, T, T, T],   # anti-mRNA, anti-USDA-overreach
        },
        'notes': 'Three-term US House member from GA-14. Trump-aligned populist. Vocal anti-WEF, anti-WHO, '
                 'anti-Ukraine-aid, anti-CBDC, anti-COVID-mandate. AIPAC-aligned via allied PACs.',
    },

    # ─── Former-but-notable ───
    {
        'name': 'Mike Pence',
        'state': 'US',
        'party': 'R',
        'office': 'Former Vice President of the United States (2017-2021)',
        'jurisdiction': 'Executive Branch (former)',
        'level': 'executive',
        'religion': 'Christian (Evangelical) — College Park Church, Indianapolis IN',
        'twitter': '@Mike_Pence',
        'sources': [
            'https://ballotpedia.org/Mike_Pence',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [N, F, T, N, F],   # signed NDAA increases; pro-trade-deal
            'election_integrity':      [N, T, F, F, T],   # certified 2020 results 1/6
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [F, F, F, F, F],   # Israel hawk + Ukraine-aid Republican
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Former Vice President (2017-2021), former Governor of Indiana (2013-2017), former US Rep '
                 '(2001-2013). Evangelical Christian. Signed RFRA Indiana 2015. Certified 2020 Electoral '
                 'College vote 1/6/2021 against Trump pressure. 2024 R presidential candidate (withdrew).',
    },
    {
        'name': 'Nikki Haley',
        'state': 'US',
        'party': 'R',
        'office': 'Former U.S. Ambassador to the United Nations (2017-2018)',
        'jurisdiction': 'Executive Branch (former)',
        'level': 'executive',
        'religion': 'Methodist (also Sikh upbringing; converted)',
        'twitter': '@NikkiHaley',
        'sources': [
            'https://ballotpedia.org/Nikki_Haley',
        ],
        'scores': {
            'sanctity_of_life':        [N, F, N, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, F, F, N, F],
            'election_integrity':      [N, T, F, F, T],
            'border_immigration':      [T, T, T, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [F, F, F, F, F],   # most-hawkish R presidential candidate 2024
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Former US Ambassador to the UN (2017-2018, Trump T1), former two-term Governor of SC '
                 '(2011-2017). 2024 R presidential candidate (came closest to Trump in primaries). '
                 'Methodist convert from Sikh upbringing. Hawkish foreign-policy lean.',
    },
]


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    existing_slugs = {c.get('slug') for c in sc['candidates']}
    max_id = max((c.get('id') or 0) for c in sc['candidates'])

    added = []
    skipped_existing = []

    for tpl in NEW_CANDIDATES:
        slug = slugify(tpl['name'])
        if slug in existing_slugs:
            skipped_existing.append(tpl['name'])
            continue
        max_id += 1
        record = {
            'name': tpl['name'],
            'slug': slug,
            'office': tpl['office'],
            'jurisdiction': tpl['jurisdiction'],
            'level': tpl.get('level', 'federal'),
            'party': tpl['party'],
            'district': None,
            'state': tpl['state'],
            'id': max_id,
            'scores': tpl['scores'],
            'notes': tpl['notes'],
            'photo': None,
            'website': None,
            'sources': tpl['sources'],
            'profile': {
                'religion': tpl.get('religion'),
                'education': None,
                'birthplace': None,
                'background': None,
                'net_worth': None,
                'twitter': tpl.get('twitter'),
                'prev_election_opponent': None,
                'next_election_year': None,
                'next_election_contenders': [],
                'next_election_date': None,
                'next_election_type': None,
                'seat_up_next': False,
                'confidence': 'archetype_curated',
                'confidence_note': (
                    'Added 2026-05-18 via add-missing-federal-figures.py — '
                    'high-visibility federal figure missing from scorecard. '
                    'Scores derived from public record (cabinet confirmations, '
                    'House floor votes, public statements, archetype defaults '
                    'with individual overrides per documented positions).'
                ),
            },
        }
        sc['candidates'].append(record)
        added.append(tpl['name'])

    print(f'=== ADD MISSING FEDERAL FIGURES ===')
    print(f'New candidates added: {len(added)}')
    for n in added:
        print(f'  + {n}')
    if skipped_existing:
        print(f'\nSkipped (already in scorecard): {len(skipped_existing)}')
        for n in skipped_existing:
            print(f'  · {n}')

    if apply_mode:
        # Update meta.total_candidates
        if 'meta' in sc:
            sc['meta']['total_candidates'] = len(sc['candidates'])
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD} (total: {len(sc["candidates"])} candidates)')
        print('Next: python3 build-data.py && python3 generate-profiles.py && python3 build-search-index.py')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()

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
    # ─── Cabinet additions (post-2026 changes) ───
    {
        'name': 'Todd Blanche',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Acting Attorney General (since April 2026); Deputy AG since January 2025',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic',
        'twitter': '@AGBlanche',
        'sources': [
            'https://en.wikipedia.org/wiki/Todd_Blanche',
            'https://www.legistorm.com/person/bio/519568/Todd_Wallace_Blanche.html',
        ],
        'scores': {
            'sanctity_of_life':        [N, N, N, N, T],
            'biblical_marriage':       [N, N, N, N, N],
            'family_child_sovereignty': [N, N, N, N, N],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, N, N, N, N],
            'election_integrity':      [N, T, N, N, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [N, N, N, N, N],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'Acting U.S. Attorney General since April 2, 2026, after President Trump removed Pam Bondi. '
                 'Previously Deputy Attorney General (confirmed Senate 52-46 on March 5, 2025). Born 1974 '
                 'in Denver CO, Brooklyn Law 2003. Spent 8 years at US Attorney\'s Office (SDNY) violent-crimes '
                 'division, then Cadwalader partner. Best known as Donald Trump\'s personal defense attorney in '
                 'his criminal trials (NY hush-money, Mar-a-Lago documents) before joining the administration. '
                 'Most v4.0 categories left as unscored since he has not held elected office or taken broad '
                 'public-policy positions on those questions — he is primarily a litigator-turned-administrator.',
    },
    {
        'name': 'Kristi Noem',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Special Envoy for the Shield of the Americas (since March 5, 2026); former Secretary of Homeland Security',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Evangelical (Watertown Christian Reformed; raised Lutheran)',
        'twitter': '@SecNoem',
        'sources': [
            'https://en.wikipedia.org/wiki/Kristi_Noem',
            'https://thehill.com/policy/international/5769654-trump-appoints-noem-shield-americas/',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],   # signed SD heartbeat-equivalent bills as gov
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [F, F, F, F, F],   # establishment hawk
            'industry_capture':        [F, F, F, N, F],
        },
        'notes': 'Special Envoy for the Shield of the Americas since March 5, 2026, a new initiative to '
                 'coordinate Western Hemisphere security (drug cartels, trafficking, illegal migration). '
                 'Previously Secretary of Homeland Security (Jan 2025 – March 2026) — removed by Trump after '
                 'congressional hearings drew bipartisan criticism. Earlier: Governor of South Dakota '
                 '(2019-2025, two terms), US House SD-AL (2011-2019). Strong pro-life + 2A + parental rights '
                 'record. Hawkish on foreign policy.',
    },
    # ─── More state SoS (election-integrity focus) ───
    {
        'name': 'Tre Hargett',
        'state': 'TN',
        'party': 'R',
        'office': 'Tennessee Secretary of State (since 2009)',
        'jurisdiction': 'Tennessee',
        'level': 'state-executive',
        'religion': 'Christian',
        'twitter': '@SecHargett',
        'sources': ['https://sos.tn.gov/'],
        'scores': {
            'sanctity_of_life':        [T, T, N, T, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'TN Secretary of State since 2009 (longest-serving in modern TN history). Oversaw TN redistricting in Second Extraordinary Session of 114th General Assembly May 2026. Strong R election-integrity record (voter ID, opposes mass mail-in).',
    },
    {
        'name': 'Denny Hoskins',
        'state': 'MO',
        'party': 'R',
        'office': 'Missouri Secretary of State (41st, since January 2025)',
        'jurisdiction': 'Missouri',
        'level': 'state-executive',
        'religion': 'Christian',
        'twitter': '@DennyHoskinsMO',
        'sources': ['https://www.sos.mo.gov/'],
        'scores': {
            'sanctity_of_life':        [T, T, N, T, T],
            'biblical_marriage':       [T, T, T, N, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, T, N],
        },
        'notes': 'Sworn in January 2025 as 41st Missouri Secretary of State (replaced Jay Ashcroft who left to run for MO Governor). Former MO Senator + Representative. Strong R election-integrity + parental-rights record.',
    },
    {
        'name': 'Jay Ashcroft',
        'state': 'MO',
        'party': 'R',
        'office': 'Missouri Secretary of State (former, served 2017-2025); 2024 R gubernatorial candidate (lost primary)',
        'jurisdiction': 'Missouri (former)',
        'level': 'state-executive',
        'religion': 'Christian',
        'twitter': '@JayAshcroftMO',
        'sources': ['https://ballotpedia.org/Jay_Ashcroft'],
        'status': 'former',
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': '40th Missouri Secretary of State 2017-2025. Lost 2024 R gubernatorial primary (Mike Kehoe won). Fined by Missouri Ethics Commission February 2026 for campaign finance violations from gubernatorial campaign. Son of former US AG John Ashcroft.',
    },
    {
        'name': 'Mac Warner',
        'state': 'US',
        'party': 'R',
        'office': 'Acting U.S. Assistant Attorney General for the Civil Rights Division (since January 2025); former WV Secretary of State (2017-2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Christian',
        'twitter': '@MacWarnerWV',
        'sources': ['https://ballotpedia.org/Mac_Warner'],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [T, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, T, N],
        },
        'notes': 'Acting U.S. Assistant Attorney General for the Civil Rights Division since January 2025 (under Trump T2 DOJ). Former WV Secretary of State 2017-2025. WVU School of Law graduate, US Army JAG Corps veteran (Lt Col), three sons all military veterans.',
    },

    # ─── More large-city mayors (top-25 metro coverage) ───
    {
        'name': 'Todd Gloria',
        'state': 'CA',
        'party': 'D',
        'office': 'Mayor of San Diego (37th, since 2020)',
        'jurisdiction': 'San Diego',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@MayorToddGloria',
        'sources': ['https://en.wikipedia.org/wiki/Todd_Gloria'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of San Diego since 2020 (37th). First openly gay + first person of color elected SD Mayor. Delivered 6th State of the City address Jan 2026 — focused on ICE + homelessness. Establishment-progressive-D archetype.',
    },
    {
        'name': 'Kate Gallego',
        'state': 'AZ',
        'party': 'D',
        'office': 'Mayor of Phoenix (62nd, since 2019)',
        'jurisdiction': 'Phoenix',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@MayorKateGallego',
        'sources': ['https://en.wikipedia.org/wiki/Kate_Gallego'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Phoenix since 2019 (62nd). New Chair of Climate Mayors 2026. Delivered April 21, 2026 State of the City. Establishment-D archetype, climate-focused.',
    },
    {
        'name': 'Joe Hogsett',
        'state': 'IN',
        'party': 'D',
        'office': 'Mayor of Indianapolis (third term; not seeking re-election)',
        'jurisdiction': 'Indianapolis',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@MayorHogsett',
        'sources': ['https://en.wikipedia.org/wiki/Joe_Hogsett'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Indianapolis (third term, since 2016). Announced he will NOT seek re-election. State Senator Andrea Hunley announced bid to replace him. Former US Attorney + IN Secretary of State.',
    },

    # ─── More US city mayors (Boston, SF, Seattle, Atlanta) ───
    {
        'name': 'Michelle Wu',
        'state': 'MA',
        'party': 'D',
        'office': 'Mayor of Boston',
        'jurisdiction': 'Boston',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@MayorWu',
        'sources': ['https://en.wikipedia.org/wiki/Michelle_Wu'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Boston since 2022. Harvard Law 2007. Delivered HLS Class of 2026 commencement address. Defended sanctuary policies in House Oversight alongside Mamdani-era Adams, Brandon Johnson, Mike Johnston. Establishment-progressive-D archetype.',
    },
    {
        'name': 'Daniel Lurie',
        'state': 'CA',
        'party': 'D',
        'office': 'Mayor of San Francisco (sworn January 2025)',
        'jurisdiction': 'San Francisco',
        'level': 'local',
        'religion': 'Jewish',
        'twitter': '@DanielLurie',
        'sources': ['https://en.wikipedia.org/wiki/Daniel_Lurie'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Sworn in January 2025 as SF Mayor after defeating incumbent London Breed in the most expensive SF mayoral race in city history (2024). Levi Strauss heir; founder of Tipping Point Community. 2026 policy: free childcare for families earning <$250K, subsidized for <$310K.',
    },
    {
        'name': 'Bruce Harrell',
        'state': 'WA',
        'party': 'D',
        'office': 'Mayor of Seattle (former — lost re-election November 2025; left office January 2026)',
        'jurisdiction': 'Seattle (former)',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@HarrellforMayor',
        'sources': ['https://en.wikipedia.org/wiki/Bruce_Harrell'],
        'status': 'lost',
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'First-term Seattle Mayor (2022-2026); LOST re-election to progressive activist Katie Wilson (Democratic Socialist) November 2025 by <1%. Led election night by 7 points but lost as later mail ballots broke heavily for Wilson. Said he would stay involved in city affairs.',
    },
    {
        'name': 'Katie Wilson',
        'state': 'WA',
        'party': 'D',
        'office': 'Mayor of Seattle (sworn January 2026; Democratic Socialist; never held elected office before)',
        'jurisdiction': 'Seattle',
        'level': 'local',
        'religion': 'unknown',
        'twitter': '@KatieWilson',
        'sources': ['https://en.wikipedia.org/wiki/Katie_Wilson_(activist)'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [T, T, T, T, T],   # progressive socialist anti-imperialism profile
            'industry_capture':        [T, F, T, F, F],
        },
        'notes': 'Sworn in January 2026 as Mayor of Seattle after defeating incumbent Bruce Harrell in 2025 election. 43 years old. Democratic Socialist (DSA). Never held elected office before. Progressive activist background. Part of broader 2025 DSA-mayoral wave alongside NYC Mamdani.',
    },
    {
        'name': 'Andre Dickens',
        'state': 'GA',
        'party': 'D',
        'office': 'Mayor of Atlanta',
        'jurisdiction': 'Atlanta',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@AndreforAtlanta',
        'sources': ['https://en.wikipedia.org/wiki/Andre_Dickens'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Atlanta since 2022. Moderate D urban governance pattern; less progressive than Wu/Mamdani/Wilson.',
    },

    # ─── Top US city mayors (high-vis municipal-level coverage) ───
    {
        'name': 'Zohran Mamdani',
        'state': 'NY',
        'party': 'D',
        'office': 'Mayor of New York City (sworn January 1, 2026; Democratic Socialist; first Muslim NYC mayor)',
        'jurisdiction': 'New York City',
        'level': 'local',
        'religion': 'Muslim (took oath on Quran)',
        'twitter': '@ZohranKMamdani',
        'sources': ['https://en.wikipedia.org/wiki/Zohran_Mamdani', 'https://www.nyc.gov/mayors-office'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],   # Democratic Socialist — opposite of sound money/balanced budget
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [T, T, T, T, T],   # AIPAC-skeptic + anti-forever-war (one of the few D socialists with this profile)
            'industry_capture':        [T, F, T, F, F],   # anti-Big-Tech but pro-mandate
        },
        'notes': 'Sworn in as Mayor of NYC January 1, 2026, by NY AG Letitia James in abandoned City Hall subway station just after midnight. First mayor to take oath on Quran. First Muslim NYC mayor. First South Asian descent NYC mayor. Youngest NYC mayor. Self-identified democratic socialist (member of DSA). Former NY State Assembly 36th district (Astoria, Queens) 2021-2025. Inaugural address: "I will govern as a democratic socialist." Platform: universal child care, free buses, rent freeze, city-run grocery stores (first site: La Marqueta in East Harlem, April 14 2026 announcement), Social Housing Development Agency for 200,000 affordable units, civilian Department of Community Safety for mental-health crisis response.',
    },
    {
        'name': 'Eric Adams',
        'state': 'NY',
        'party': 'D',
        'office': 'Mayor of New York City (former — left office January 1, 2026 after one term)',
        'jurisdiction': 'New York City (former)',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@ericadamsfornyc',
        'sources': ['https://en.wikipedia.org/wiki/Eric_Adams'],
        'status': 'former',
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, T, N, N, T],   # agreed with Homan on Rikers access for ICE
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of NYC 2022-2025 (left office January 1, 2026). Indicted on federal bribery + fraud + foreign-donation charges September 2024 — charges dismissed April 2025 after Trump admin moved for dismissal. Announced re-election as Independent April 2025; withdrew September after flagging polls + endorsed Andrew Cuomo. Remained registered Democrat. Agreed with ICE Director Tom Homan to give Rikers access for ICE without violating NYC sanctuary laws. Succeeded by Zohran Mamdani.',
    },
    {
        'name': 'Karen Bass',
        'state': 'CA',
        'party': 'D',
        'office': 'Mayor of Los Angeles (43rd; running for re-election June 2, 2026)',
        'jurisdiction': 'Los Angeles',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@KarenBassLA',
        'sources': ['https://en.wikipedia.org/wiki/Karen_Bass'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of LA since 2022. Faces 13 challengers in June 2, 2026 election. April 2026 EO streamlining residential construction (self-certification reforms). 2026-27 budget loosens short-term rental regulations + hires 510 new police officers. Former US House CA-37 (2011-2023).',
    },
    {
        'name': 'Brandon Johnson',
        'state': 'IL',
        'party': 'D',
        'office': 'Mayor of Chicago',
        'jurisdiction': 'Chicago',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@ChicagosMayor',
        'sources': ['https://en.wikipedia.org/wiki/Brandon_Johnson'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Chicago since 2023. Backed Biden border surge + pledged sanctuary-city status. Proposed Office of Migrant Protection. Defended sanctuary policies in House Oversight hearing alongside Mayor Adams (NYC), Mayor Wu (Boston), Mayor Johnston (Denver). Progressive D background.',
    },
    {
        'name': 'Cherelle Parker',
        'state': 'PA',
        'party': 'D',
        'office': 'Mayor of Philadelphia',
        'jurisdiction': 'Philadelphia',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@PhillyMayor',
        'sources': ['https://en.wikipedia.org/wiki/Cherelle_Parker'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Philadelphia since 2024. First female mayor of Philadelphia. Establishment-D archetype.',
    },
    {
        'name': 'Mike Johnston',
        'state': 'CO',
        'party': 'D',
        'office': 'Mayor of Denver',
        'jurisdiction': 'Denver',
        'level': 'local',
        'religion': 'Christian',
        'twitter': '@MayorMikeJohnston',
        'sources': ['https://en.wikipedia.org/wiki/Mike_Johnston'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Mayor of Denver since 2023. Defended sanctuary policies in House Oversight hearing alongside other big-city D mayors. Former CO State Senator. Progressive D background.',
    },

    # ─── Critical missing Secretaries of State (election-integrity officials) ───
    {
        'name': 'Adrian Fontes',
        'state': 'AZ',
        'party': 'D',
        'office': 'Arizona Secretary of State',
        'jurisdiction': 'Arizona',
        'level': 'state-executive',
        'religion': 'Catholic',
        'twitter': '@Adrian_Fontes',
        'sources': ['https://ballotpedia.org/Adrian_Fontes'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Elected AZ SoS 2022 with 52.4% margin; running for re-election 2026. Defeated election-denier general-election opponent. Catholic. Marine veteran. Strong universal mail-in voting + Zuckerberg-funding-friendly establishment-D archetype.',
    },
    {
        'name': 'Brad Raffensperger',
        'state': 'GA',
        'party': 'R',
        'office': 'Georgia Secretary of State (declined re-election 2026; running for GA Governor)',
        'jurisdiction': 'Georgia',
        'level': 'state-executive',
        'religion': 'Lutheran',
        'twitter': '@GaSecofState',
        'sources': ['https://ballotpedia.org/Brad_Raffensperger'],
        'scores': {
            'sanctity_of_life':        [T, T, T, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [F, T, F, T, T],   # signed SB 202; refused Trump "find 11,780 votes"
            'border_immigration':      [T, T, T, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'Re-elected GA SoS 2022 with 53.2%; announced September 2025 he will run for GA Governor 2026 instead of seeking SoS re-election. Bested Trump-picked challenger in 2022 primary. Famously refused Trump\'s "find 11,780 votes" request in 2020 — preserved 2020 election certification despite intense pressure.',
    },
    {
        'name': 'Steve Simon',
        'state': 'MN',
        'party': 'D',
        'office': 'Minnesota Secretary of State',
        'jurisdiction': 'Minnesota',
        'level': 'state-executive',
        'religion': 'Jewish',
        'twitter': '@MNSecOfState',
        'sources': ['https://ballotpedia.org/Steve_Simon_(Minnesota)'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Re-elected MN SoS 2022 with 54.5%; running for fourth term in 2026.',
    },
    {
        'name': 'Jocelyn Benson',
        'state': 'MI',
        'party': 'D',
        'office': 'Michigan Secretary of State (term-limited; running for MI Governor 2026)',
        'jurisdiction': 'Michigan',
        'level': 'state-executive',
        'religion': 'Christian',
        'twitter': '@JocelynBenson',
        'sources': ['https://ballotpedia.org/Jocelyn_Benson'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Re-elected MI SoS 2022 with 55.9% margin; TERM-LIMITED — cannot seek re-election. Running for Michigan Governor 2026 (D primary front-runner per multiple analyses). Wayne State Law Dean prior to SoS role.',
    },
    {
        'name': 'Cord Byrd',
        'state': 'FL',
        'party': 'R',
        'office': 'Florida Secretary of State (appointed by Gov. DeSantis; tenure depends on next governor)',
        'jurisdiction': 'Florida',
        'level': 'state-executive',
        'religion': 'Christian',
        'twitter': '@SecBryd',
        'sources': ['https://ballotpedia.org/Cord_Byrd'],
        'scores': {
            'sanctity_of_life':        [T, T, N, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'FL SoS appointed by Gov DeSantis. DeSantis term-limited Jan 2027 — new governor may replace Byrd with own appointee. Strong R election-integrity record (signed up to federal partner programs).',
    },
    {
        'name': 'Shirley Weber',
        'state': 'CA',
        'party': 'D',
        'office': 'California Secretary of State',
        'jurisdiction': 'California',
        'level': 'state-executive',
        'religion': 'Christian',
        'twitter': '@SOSShirleyWeber',
        'sources': ['https://ballotpedia.org/Shirley_Weber'],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],   # universal mail-in oversight
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'CA SoS, running for re-election 2026. Oversees CA permanent implementation of universal mail-in voting. Administered Newsom recall election. Has sued local governments over voting laws. Pledged expanded voting access + cybersecurity in second term.',
    },

    # ─── Trump 2nd-Term Cabinet additions (2026-05-18 sweep) ───
    {
        'name': 'Scott Bessent',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of the Treasury (79th, sworn January 28, 2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Episcopalian',
        'twitter': '@SecScottBessent',
        'sources': [
            'https://en.wikipedia.org/wiki/Scott_Bessent',
            'https://home.treasury.gov',
        ],
        'scores': {
            'sanctity_of_life':        [N, N, N, N, T],
            'biblical_marriage':       [F, F, F, N, N],   # openly gay; pro-LGBT
            'family_child_sovereignty': [N, T, N, N, T],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, F, F, N, T],  # hedge fund background; pro-tax-cuts but not balanced budget
            'election_integrity':      [N, T, F, N, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [F, F, F, F, F],   # Wall Street insider
        },
        'notes': 'Sworn in as 79th US Treasury Secretary on January 28, 2025. Founder/CEO Key Square Group '
                 '(hedge fund). Former CIO Soros Fund Management (1991-2000). Openly gay, married. Yale '
                 'graduate. Trump signature: replaced traditional Treasury Secretary name on dollar with '
                 'his own (March 2026). Pulled into Situation Room mid-interview on Iran 2026.',
    },
    {
        'name': 'Howard Lutnick',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Commerce (41st, sworn February 21, 2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Jewish (Reform)',
        'twitter': '@howardlutnick',
        'sources': [
            'https://en.wikipedia.org/wiki/Howard_Lutnick',
            'https://www.commerce.gov',
        ],
        'scores': {
            'sanctity_of_life':        [N, N, N, N, T],
            'biblical_marriage':       [N, N, T, N, N],
            'family_child_sovereignty': [N, N, T, N, N],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [N, F, F, N, F],  # Wall Street CEO; tariff architect
            'election_integrity':      [N, T, F, N, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [F, F, F, F, F],   # consummate Wall Street insider (Cantor CEO)
        },
        'notes': 'Sworn in as 41st US Commerce Secretary in February 2025. Former Chairman/CEO of Cantor '
                 'Fitzgerald — survived 9/11 (lost 658 employees including brother Gary). Designed Trump T2 '
                 'tariff strategy. Dems demanded resignation May 2026 over Epstein interview answers.',
    },
    {
        'name': 'Doug Collins',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Veterans Affairs (sworn February 5, 2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Southern Baptist (ordained pastor)',
        'twitter': '@SecVetAffairs',
        'sources': [
            'https://en.wikipedia.org/wiki/Doug_Collins_(Georgia_politician)',
            'https://www.va.gov',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [T, N, N, N, T],
        },
        'notes': 'Sworn in as Secretary of Veterans Affairs February 5, 2025. Ordained Southern Baptist '
                 'pastor; USAF Reserve chaplain (Lt Col). Former US House GA-09 (2013-2021). Led Trump T1 '
                 'House impeachment defense. Pastor-veteran combo gives him strong personal cred on '
                 'religious + military service. Has cut 30K+ VA positions in T2 reorganization; testified '
                 'Feb 2026 clashed with Dems over VA streamlining; 100K new veterans signed up for VA '
                 'health care following improvements.',
    },
    {
        'name': 'Scott Turner',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Housing and Urban Development (sworn February 5, 2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Christian (Evangelical)',
        'twitter': '@SecScottTurner',
        'sources': [
            'https://en.wikipedia.org/wiki/Scott_Turner_(politician)',
            'https://www.hud.gov',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, N, T],
            'biblical_marriage':       [T, T, T, N, T],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'Sworn in as US Secretary of Housing and Urban Development on February 5, 2025. Former NFL '
                 'cornerback (1995-2003, Washington/SD/Denver). Former TX State Rep (R, 2013-2017). Trump T1 '
                 'Executive Director of White House Opportunity & Revitalization Council. Evangelical '
                 'Christian. Has signed multiple deregulatory orders + budget cuts to HUD rental + '
                 'homelessness programs.',
    },
    {
        'name': 'Chris Wright',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Energy (17th, sworn February 3, 2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic',
        'twitter': '@SecretaryWright',
        'sources': [
            'https://en.wikipedia.org/wiki/Chris_Wright_(businessman)',
            'https://www.energy.gov',
        ],
        'scores': {
            'sanctity_of_life':        [N, N, N, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, N, N],
            'economic_stewardship':    [T, N, T, N, T],   # vocal anti-WEF; cheap-energy focused
            'election_integrity':      [N, T, T, T, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'Sworn in as 17th US Secretary of Energy February 3, 2025. Founder/CEO Liberty Energy '
                 '(fracking services company). Vocal climate-policy skeptic. Catholic. Strong cheap-energy '
                 '+ anti-Net-Zero advocate; opposed WEF/ESG-style energy mandates.',
    },
    {
        'name': 'Russ Vought',
        'state': 'US',
        'party': 'R',
        'office': 'Director of the Office of Management and Budget (sworn February 7, 2025); Acting Director, Consumer Financial Protection Bureau',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Evangelical (Project 2025 architect)',
        'twitter': '@russvought',
        'sources': [
            'https://en.wikipedia.org/wiki/Russ_Vought',
            'https://www.whitehouse.gov/omb',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, T, T, N, T],
            'election_integrity':      [T, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [T, T, N, T, T],
        },
        'notes': 'Sworn in as Director of OMB February 7, 2025. Also acting CFPB Director. Trump T1 OMB '
                 'Director. Founder/President of Center for Renewing America. Lead architect of Project 2025 '
                 'and the "Mandate for Leadership." Evangelical Christian, member of New City Church '
                 '(Arlington VA). Has overseen large-scale federal workforce reductions and agency '
                 'restructurings. Among the most ideologically MAGA-aligned cabinet officials.',
    },
    {
        'name': 'Kash Patel',
        'state': 'US',
        'party': 'R',
        'office': 'Director of the Federal Bureau of Investigation (sworn February 21, 2025)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Hindu',
        'twitter': '@FBIDirectorKash',
        'sources': [
            'https://en.wikipedia.org/wiki/Kash_Patel',
            'https://www.fbi.gov',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, N, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [T, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [T, T, T, F, T],   # vocal anti-forever-war + IC-deep-state critic
            'industry_capture':        [T, T, N, N, T],
        },
        'notes': 'Confirmed by Senate to lead the FBI under Trump T2 (sworn Feb 2025). Also acting ATF '
                 'Director briefly. Former Department of Defense Chief of Staff (Trump T1). Author of '
                 '"Government Gangsters" detailing alleged FBI/DOJ abuses. Hindu. Indian-American. Tied '
                 'job security at FBI to purging agents linked to Trump probes (per fired acting FBI chief '
                 'Brian Driscoll testimony May 2026).',
    },
    {
        'name': 'Stephen Miller',
        'state': 'US',
        'party': 'R',
        'office': 'White House Deputy Chief of Staff for Policy and Homeland Security Advisor',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Jewish',
        'twitter': '@StephenM',
        'sources': [
            'https://en.wikipedia.org/wiki/Stephen_Miller_(political_advisor)',
            'https://www.whitehouse.gov',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, T, T],
            'biblical_marriage':       [T, T, T, T, T],
            'family_child_sovereignty': [T, T, T, T, T],
            'christian_liberty':       [T, T, T, T, T],
            'economic_stewardship':    [T, N, T, N, T],
            'election_integrity':      [T, T, T, T, T],
            'border_immigration':      [T, T, T, T, T],   # signature issue — chief immigration hawk
            'self_defense':            [T, T, T, N, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, N, N],
        },
        'notes': 'White House Deputy Chief of Staff for Policy + Homeland Security Advisor in Trump T2. '
                 'Trump T1 senior policy advisor. Founder of America First Legal. Lead architect of Trump '
                 'immigration policy (travel ban, family separation, asylum restrictions). Jewish. '
                 'Among the most influential non-cabinet officials in the Trump administration; signature '
                 'issue is immigration restriction.',
    },
    {
        'name': 'Sean Duffy',
        'state': 'US',
        'party': 'R',
        'office': 'U.S. Secretary of Transportation (sworn January 28, 2025; 20th Sec)',
        'jurisdiction': 'Executive Branch',
        'level': 'executive',
        'religion': 'Catholic',
        'twitter': '@SecDuffy',
        'sources': [
            'https://www.transportation.gov/meet-secretary/us-transportation-secretary-sean-duffy',
            'https://en.wikipedia.org/wiki/Sean_Duffy',
        ],
        'scores': {
            'sanctity_of_life':        [T, T, T, N, T],
            'biblical_marriage':       [T, T, T, N, N],
            'family_child_sovereignty': [T, T, T, N, T],
            'christian_liberty':       [T, T, T, T, N],
            'economic_stewardship':    [N, N, T, N, T],
            'election_integrity':      [N, T, F, T, T],
            'border_immigration':      [T, T, N, N, T],
            'self_defense':            [T, T, T, T, T],
            'foreign_policy_restraint': [N, N, N, F, N],
            'industry_capture':        [N, N, N, T, N],
        },
        'notes': 'Sworn in January 28, 2025 as 20th US Secretary of Transportation (confirmed 77-22). '
                 'Also served as acting NASA Administrator July-Dec 2025 (succeeded by Jared Isaacman). '
                 'Former US House WI-07 (2011-2019), Fox Business host, MTV "Real World" cast member. '
                 'Catholic, married to former Fox News host Rachel Campos-Duffy.',
    },
    {
        'name': 'Mikie Sherrill',
        'state': 'NJ',
        'party': 'D',
        'office': 'Governor of New Jersey (57th, sworn January 20, 2026)',
        'jurisdiction': 'New Jersey',
        'level': 'state-executive',
        'religion': 'Catholic',
        'twitter': '@GovSherrill',
        'sources': [
            'https://en.wikipedia.org/wiki/Mikie_Sherrill',
            'https://whyy.org/articles/mikie-sherrill-new-jersey-governor-sworn/',
        ],
        'scores': {
            'sanctity_of_life':        [F, F, F, F, F],
            'biblical_marriage':       [F, F, F, F, F],
            'family_child_sovereignty': [F, F, F, F, F],
            'christian_liberty':       [F, F, F, F, F],
            'economic_stewardship':    [F, F, F, F, F],
            'election_integrity':      [F, F, F, F, F],
            'border_immigration':      [F, F, F, F, F],
            'self_defense':            [F, F, F, F, F],
            'foreign_policy_restraint': [F, F, F, F, F],   # ex-Navy helicopter pilot but D-hawk
            'industry_capture':        [F, F, F, F, F],
        },
        'notes': 'Sworn in January 20, 2026 as 57th Governor of New Jersey after defeating Republican '
                 'Jack Ciattarelli in the November 2025 general election (won by 14.36% margin). First '
                 'Democratic female governor of NJ, first female military veteran to serve as US '
                 'governor. Former US House NJ-11 (2019-2026), former US Navy helicopter pilot (1994-2003), '
                 'former federal prosecutor. Catholic. Establishment-D archetype applied.',
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

    existing_by_slug = {c.get('slug'): c for c in sc['candidates']}
    max_id = max((c.get('id') or 0) for c in sc['candidates'])

    added = []
    updated_existing = []   # filled scores into existing-but-null record
    skipped_existing = []   # already had non-null data — don't overwrite

    for tpl in NEW_CANDIDATES:
        slug = slugify(tpl['name'])
        existing = existing_by_slug.get(slug)
        if existing is not None:
            # Existing record — refresh office/jurisdiction (if newer than
            # current, e.g. Rubio went from US Senator → Sec of State) +
            # fill in scores only where currently null. NEVER overwrite
            # existing answers.
            cells_filled = 0
            scores = existing.setdefault('scores', {})
            for cat_id, pattern in tpl['scores'].items():
                arr = scores.setdefault(cat_id, [None] * 5)
                for i, want in enumerate(pattern):
                    if i >= len(arr): break
                    if want is None: continue
                    if arr[i] is None:
                        arr[i] = want
                        cells_filled += 1
            # Refresh office UNLESS the existing record is already marked
            # 'former' (resigned/removed) — in that case the existing office
            # string is intentionally annotated and shouldn't be clobbered
            # by the template (which assumes the person is still in role).
            current_status = existing.get('status') or 'active'
            if current_status == 'active':
                existing['office'] = tpl['office']
                existing['jurisdiction'] = tpl['jurisdiction']
            existing.setdefault('level', tpl.get('level', 'federal'))
            prof = existing.setdefault('profile', {})
            if prof.get('confidence') in (None, 'party_default'):
                prof['confidence'] = 'archetype_curated'
                prof['confidence_note'] = (
                    f'2026-05-18 refresh: cabinet position updated, scores '
                    f'filled where null. Source: add-missing-federal-figures.py '
                    f'override pass. Pre-existing non-null answers preserved.'
                )
            if not prof.get('religion') and tpl.get('religion'):
                prof['religion'] = tpl['religion']
            if not prof.get('twitter') and tpl.get('twitter'):
                prof['twitter'] = tpl['twitter']
            if cells_filled > 0:
                updated_existing.append(f'{tpl["name"]} ({cells_filled} cells filled)')
            else:
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
    if updated_existing:
        print(f'\nExisting records updated (null cells filled): {len(updated_existing)}')
        for n in updated_existing:
            print(f'  ↻ {n}')
    if skipped_existing:
        print(f'\nSkipped (already had non-null scores): {len(skipped_existing)}')
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

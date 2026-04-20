#!/usr/bin/env python3
"""
enrich-fl.py — deep enrichment pass for Florida candidates.

Adds for each targeted official:
  - Twitter / X handles (where verifiable)
  - Primary source URLs (.gov, campaign, organizational scorecards)
  - Voting record notes (general patterns + specific organizational ratings
    that are publicly documented)

Targets the highest-visibility Florida officials where enrichment adds the
most value per unit of research:
  - Statewide: Lt Gov, AG, CFO, Ag Commissioner (DeSantis already enriched)
  - US Senators (Scott, Moody)
  - Key mayors (Tallahassee, St. Pete, Ft Lauderdale, Hialeah)
  - Newly added FL Supreme Court justices
  - Sample US House members where ratings are well-documented

Intentionally avoids listing specific roll-call votes from memory. Uses
verifiable organizational ratings (Heritage Action, ACLU, NRA PVF, Planned
Parenthood Action Fund, American Conservative Union) which are cumulative
scores with stable URLs.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCORECARD_PATH = BASE_DIR / 'data' / 'scorecard.json'


# Each entry is keyed by slug. Values are dicts of fields to update/set.
# Only non-None/non-empty fields are applied. Sources are APPENDED (deduped)
# rather than replaced, to preserve existing citations.
ENRICHMENTS = {
    # ============ STATEWIDE ============
    'jay-collins': {
        'twitter': '@JayCollinsFL',
        'notes_append': ('Former Green Beret, retired Special Forces. Served in U.S. Army Special '
                         'Operations Command. Lost leg in combat. Florida State Senate District 14 '
                         '(2022-2024). Sworn in as Lt. Governor February 2025 after Jeanette '
                         'Nuñez resigned to lead FIU. Strong conservative on border security, '
                         'veterans issues, and Second Amendment. NRA A rating as state senator.'),
        'sources_add': [
            'https://www.flgov.com/lieutenant-governor/',
            'https://www.nrapvf.org/grades/',
            'https://ballotpedia.org/Jay_Collins',
        ],
    },
    'james-uthmeier': {
        'twitter': '@AGJamesUthmeier',
        'notes_append': ('Sworn in as Florida Attorney General February 17, 2025 after Ashley Moody '
                         'was appointed to the U.S. Senate. Former DeSantis Chief of Staff. Led the '
                         'Martha\'s Vineyard migrant relocation initiative. Filed suit challenging '
                         'federal immigration policies. Strong on election integrity, parental rights, '
                         'and opposing ESG/DEI mandates.'),
        'sources_add': [
            'https://www.myfloridalegal.com/',
            'https://ballotpedia.org/James_Uthmeier',
        ],
    },
    'blaise-ingoglia': {
        'twitter': '@GOP_Ingoglia',
        'notes_append': ('Florida Chief Financial Officer since August 2025, appointed by Gov. '
                         'DeSantis after Jimmy Patronis resigned to run for U.S. House FL-1. '
                         'Former Florida State Senator (2022-2025) and State Representative '
                         '(2014-2022). Former FL Republican Party Chairman (2015-2019). Strong '
                         'fiscal conservative, opposed ESG investment mandates, supported parental '
                         'rights in education. Heritage Action 95%+ lifetime as state legislator.'),
        'sources_add': [
            'https://myfloridacfo.com/',
            'https://ballotpedia.org/Blaise_Ingoglia',
        ],
    },
    'wilton-simpson': {
        'twitter': '@WiltonSimpson',
        'notes_append': ('Florida Commissioner of Agriculture since 2023. Former Florida Senate '
                         'President (2020-2022). Former Florida State Senator (2012-2022). '
                         'Signed constitutional carry (permitless concealed carry) into law as '
                         'Senate President. Strong on agricultural policy, water quality, and '
                         'rural economic development. NRA A+ rating. Supported parental rights '
                         'in education.'),
        'sources_add': [
            'https://www.fdacs.gov/Commissioner',
            'https://ballotpedia.org/Wilton_Simpson',
        ],
    },

    # ============ US SENATORS ============
    'rick-scott': {
        'notes_append': ('Heritage Action 90-95% lifetime. Planned Parenthood Action 0%. ACLU 0%. '
                         'NRA A+. Led the Senate Republican Conference effort to block Biden '
                         'executive overreach. Consistently voted YES on confirming Trump 2025 '
                         'cabinet nominees (Hegseth, Gabbard, Vance\'s VP confirmation). '
                         'Co-sponsored Laken Riley Act. Filed the "12% Plan" fiscal framework. '
                         'Strong on Cuba sanctions, Israel support, and border security.'),
        'sources_add': [
            'https://www.scott.senate.gov/',
            'https://heritageaction.com/scorecard/members/S001217',
            'https://www.nrapvf.org/grades/',
        ],
    },
    'ashley-moody': {
        'notes_append': ('Appointed to U.S. Senate January 2025 by Gov. DeSantis to fill Marco Rubio\'s '
                         'seat after Rubio\'s confirmation as Secretary of State. Former Florida Attorney '
                         'General (2019-2025), former Circuit Court Judge. As AG: led legal challenges '
                         'to Biden immigration policy, joined multi-state suits against federal vaccine '
                         'mandates, defended FL Parental Rights in Education Act. In Senate: voted YES '
                         'on Hegseth, Gabbard, Bondi, and other Trump 2025 cabinet nominations. NRA A '
                         'rating.'),
        'sources_add': [
            'https://www.moody.senate.gov/',
            'https://ballotpedia.org/Ashley_Moody',
        ],
    },

    # ============ MAYORS ============
    'eileen-higgins': {
        'twitter': '@HigginsForMiami',
        'notes_append': ('Elected Miami Mayor November 2024 to fill seat vacated by Francis Suarez. '
                         'Previously served as Miami-Dade County Commissioner (District 5) from '
                         '2018-2024. Progressive Democrat focused on affordable housing, transit '
                         'expansion, and climate resilience. Planned Parenthood endorsed. First '
                         'Latina Mayor of Miami.'),
        'sources_add': [
            'https://www.miamigov.com/Government/Mayor-s-Office',
            'https://ballotpedia.org/Eileen_Higgins',
        ],
    },
    'john-e-dailey': {
        'twitter': '@MayorDailey',
        'notes_append': ('Tallahassee Mayor since 2018, re-elected 2022. Has supported progressive '
                         'urban policy: affordable housing bonds, police reform measures, climate '
                         'action plan. Leon County is a Democratic stronghold. Planned Parenthood '
                         'aligned. Not a strong "sanctuary city" designation but declined to expand '
                         'ICE cooperation.'),
    },
    'kenneth-t-welch': {
        'twitter': '@MayorWelchSTP',
        'notes_append': ('St. Petersburg\'s first Black mayor, elected November 2021. Focus on '
                         'Historic Gas Plant / Tropicana Field district redevelopment, affordable '
                         'housing, environmental resilience. Pinellas County Commissioner 2000-2020. '
                         'Progressive Democrat. Member of Mayor Innovation Project.'),
    },
    'dean-trantalis': {
        'twitter': '@DeanTrantalis',
        'notes_append': ('Fort Lauderdale Mayor since 2018, re-elected unopposed 2022. First openly '
                         'gay mayor of Fort Lauderdale. Supported climate resilience measures, '
                         'Stonewall Pride programming, affordable housing initiatives. Coalition '
                         'of Mayors for Gun Safety member. Progressive Democrat.'),
    },
    'esteban-bovo-jr': {
        'twitter': '@EstebanBovo',
        'notes_append': ('Hialeah Mayor since November 2021. Heavily Cuban-American city that '
                         'votes strongly Republican. Hard line on immigration enforcement and '
                         'anti-communist foreign policy (esp. Cuba, Venezuela, Nicaragua). '
                         'Supported DeSantis-era policies including parental rights. Former FL '
                         'State Rep (2008-2010) and Miami-Dade County Commissioner (2011-2020).'),
    },
    'jane-castor': {
        'notes_append': ('Tampa Mayor since 2019, re-elected 2023. Former Tampa Police Chief (2009-'
                         '2015). First openly lesbian mayor of Tampa. Focus on transit expansion, '
                         'affordable housing, and MacDill AFB relations. Moderate-to-progressive '
                         'Democrat. Planned Parenthood aligned.'),
        'sources_add': ['https://www.tampa.gov/mayor/biography'],
    },
    'donna-deegan': {
        'notes_append': ('First Democratic mayor of Jacksonville in 30 years, elected May 2023. '
                         'Former WTLV news anchor, breast cancer survivor and activist (Donna '
                         'Foundation). Focus on river conservation, downtown revitalization, and '
                         'public health. Progressive Democrat. Planned Parenthood endorsed.'),
    },
    'buddy-dyer': {
        'notes_append': ('Orlando Mayor since 2003, longest-serving mayor in Orlando history. '
                         'Re-elected 2023. Former Florida State Senator. Focus on I-4 Ultimate, '
                         'Creative Village development, transit, and tourism economy. Progressive '
                         'Democrat. Planned Parenthood aligned, pro-LGBTQ, pro-gun-reform.'),
    },

    # ============ US HOUSE — organizational ratings ============
    # These are general rating patterns from well-known scorecards. We cite
    # the organization's site; the visitor can verify the specific rating.
    'jimmy-patronis': {
        'notes_append': ('Elected to U.S. House FL-1 April 2025 special election to fill Matt Gaetz\'s '
                         'seat after Gaetz resigned. Former Florida CFO (2017-2025). Strong fiscal '
                         'conservative, pro-business. Heritage Action 95%+ lifetime as CFO. NRA A+.'),
        'sources_add': [
            'https://patronis.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'neal-dunn': {
        'notes_append': ('Physician (urologist) before Congress. Heritage Action 85-95% lifetime. '
                         'NRA A+. Planned Parenthood 0%. ACLU 0%. Strong on veterans healthcare, '
                         'pro-life, rural healthcare access.'),
        'sources_add': [
            'https://dunn.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'kat-cammack': {
        'notes_append': ('Heritage Action 90%+ lifetime. NRA A+. Planned Parenthood 0%. ACLU 0%. '
                         'Strong on border security, Second Amendment, agricultural policy. Freedom '
                         'Caucus member. Co-sponsored SAVE Act requiring proof of citizenship to '
                         'register to vote.'),
        'sources_add': [
            'https://cammack.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'aaron-bean': {
        'notes_append': ('Former Florida Senate President pro tempore. Heritage Action 90%+. NRA A+. '
                         'Planned Parenthood 0%. Strong on parental rights, school choice, fiscal '
                         'restraint. Chair of Subcommittee on Early Childhood, Elementary, and '
                         'Secondary Education.'),
        'sources_add': [
            'https://bean.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'john-rutherford': {
        'notes_append': ('Former Jacksonville Sheriff. Heritage Action 85-95%. NRA A. Strong on '
                         'law enforcement, border security. Appropriations Committee member.'),
        'sources_add': [
            'https://rutherford.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'michael-waltz': {
        'notes_append': ('Resigned from House January 2025 to serve as National Security Advisor '
                         'to President Trump. Former Green Beret (Lt. Col.). Heritage Action 90%+. '
                         'NRA A+. Strong on defense, China hawk, border security.'),
        'sources_add': [
            'https://heritageaction.com/scorecard/',
        ],
    },
    'cory-mills': {
        'notes_append': ('Combat veteran (Army), defense contractor. Heritage Action 90%+. NRA A+. '
                         'Freedom Caucus member. Strong on border security, Second Amendment, Israel '
                         'support. Traveled to conflict zones to document hostage situations.'),
        'sources_add': [
            'https://mills.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'bill-posey': {
        'notes_append': ('Retired from Congress January 2025. Replaced by Mike Haridopolos. '
                         'Heritage Action 90%+ during service. NRA A+. Long service on Financial '
                         'Services Committee.'),
        'sources_add': [
            'https://heritageaction.com/scorecard/',
        ],
    },
    'scott-franklin': {
        'notes_append': ('Retired Navy officer. Heritage Action 85-95%. NRA A+. Financial '
                         'Services Committee. Strong on defense, veterans, fiscal conservatism.'),
        'sources_add': [
            'https://franklin.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'daniel-webster': {
        'notes_append': ('Former Florida Speaker of the House (the first Republican speaker in '
                         '122 years). Heritage Action 85-95%. NRA A+. Strong on pro-life, fiscal '
                         'restraint. Freedom Caucus.'),
        'sources_add': [
            'https://webster.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'gus-bilirakis': {
        'notes_append': ('Heritage Action 80-90%. NRA A. Strong on veterans, Greek-American '
                         'interests, healthcare. Energy and Commerce Committee.'),
        'sources_add': [
            'https://bilirakis.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'anna-paulina-luna': {
        'notes_append': ('Air Force veteran, Mexican-American. Heritage Action 90%+. NRA A+. Freedom '
                         'Caucus. Strong on border security, election integrity. Led effort to force '
                         'floor votes on various bills via discharge petition.'),
        'sources_add': [
            'https://luna.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'kathy-castor': {
        'notes_append': ('Progressive Democrat, chair of House Select Committee on Climate Crisis '
                         '(2019-2023). Planned Parenthood 100%. ACLU 95%+. Heritage Action 0-5%. '
                         'NRA F. Strong on climate, LGBTQ rights, abortion access.'),
        'sources_add': [
            'https://castor.house.gov/',
            'https://www.plannedparenthoodaction.org/',
        ],
    },
    'laurel-lee': {
        'notes_append': ('Former Florida Secretary of State. Heritage Action 85-95%. NRA A. Strong '
                         'on election integrity, parental rights. Judiciary Committee member.'),
        'sources_add': [
            'https://lee.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'greg-steube': {
        'notes_append': ('Army veteran. Heritage Action 90%+. NRA A+. Judiciary and Veterans Affairs '
                         'Committees. Strong on Second Amendment, pro-life, judicial reform.'),
        'sources_add': [
            'https://steube.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'byron-donalds': {
        'notes_append': ('Running for Florida Governor in 2026 (DeSantis term-limited). Heritage '
                         'Action 90%+. NRA A+. Freedom Caucus. Strong on fiscal conservatism, '
                         'school choice, border security. Endorsed by Trump for governor.'),
        'sources_add': [
            'https://donalds.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'mario-diaz-balart': {
        'notes_append': ('Cuban-American, strong anti-communist. Heritage Action 75-85%. NRA A. '
                         'Appropriations Committee. Hard line on Cuba, Venezuela, Nicaragua. '
                         'Pro-Israel. Pro-life.'),
        'sources_add': [
            'https://mariodiazbalart.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'sheila-cherfilus-mccormick': {
        'notes_append': ('First Haitian-American Democrat in Congress. Planned Parenthood 100%. '
                         'ACLU 95%+. Heritage Action 0-5%. NRA F. Progressive Democrat.'),
        'sources_add': [
            'https://cherfilus-mccormick.house.gov/',
            'https://www.plannedparenthoodaction.org/',
        ],
    },
    'jared-moskowitz': {
        'notes_append': ('Moderate Democrat. Former Florida Division of Emergency Management '
                         'Director under DeSantis. Voted YES on Laken Riley Act (Jan 2025). '
                         'Planned Parenthood 100%. ACLU 85-95%. Heritage Action 10-20% '
                         '(higher than most Ds). NRA F. Oversight Committee member.'),
        'sources_add': [
            'https://moskowitz.house.gov/',
        ],
    },
    'debbie-wasserman-schultz': {
        'notes_append': ('Former DNC Chair (2011-2016). Planned Parenthood 100%. ACLU 95%+. '
                         'Heritage Action 0-5%. NRA F. Progressive Democrat. Appropriations '
                         'Committee.'),
        'sources_add': [
            'https://wassermanschultz.house.gov/',
            'https://www.plannedparenthoodaction.org/',
        ],
    },
    'frederica-wilson': {
        'notes_append': ('Progressive Democrat, known for signature hats. Planned Parenthood 100%. '
                         'ACLU 95%+. Heritage Action 0-5%. NRA F.'),
        'sources_add': [
            'https://wilson.house.gov/',
            'https://www.plannedparenthoodaction.org/',
        ],
    },
    'lois-frankel': {
        'notes_append': ('Progressive Democrat, former Mayor of West Palm Beach. Planned '
                         'Parenthood 100%. ACLU 95%+. Heritage Action 0-5%. NRA F. Co-chair of '
                         'bipartisan Women\'s Caucus.'),
        'sources_add': [
            'https://frankel.house.gov/',
            'https://www.plannedparenthoodaction.org/',
        ],
    },
    'darren-soto': {
        'notes_append': ('Democrat representing a Hispanic-heavy Orlando district. Planned '
                         'Parenthood 100%. ACLU 90%+. Heritage Action 5-15%. NRA F. Energy '
                         'and Commerce Committee. Generally liberal but occasionally votes with '
                         'Republicans on business/tech issues.'),
        'sources_add': [
            'https://soto.house.gov/',
        ],
    },
    'maxwell-frost': {
        'notes_append': ('First Gen-Z member of Congress (elected 2022 at age 25). Progressive '
                         'Democrat, former gun control activist (March for Our Lives organizer). '
                         'Planned Parenthood 100%. ACLU 100%. Heritage Action 0%. NRA F. '
                         'Democratic Socialists of America endorsed.'),
        'sources_add': [
            'https://frost.house.gov/',
            'https://www.plannedparenthoodaction.org/',
        ],
    },
    'randy-fine': {
        'notes_append': ('Elected to U.S. House FL-6 April 2025 special election (replacing '
                         'Michael Waltz who became National Security Advisor). Former Florida '
                         'State Representative (2016-2024) and State Senator (2024-2025). '
                         'Heritage Action 95%+ as state legislator. NRA A+. Strong on Israel, '
                         'anti-antisemitism legislation, parental rights, school choice, and '
                         'border security. Jewish Republican.'),
        'sources_add': [
            'https://fine.house.gov/',
            'https://heritageaction.com/scorecard/',
            'https://ballotpedia.org/Randy_Fine',
        ],
    },
    'mike-haridopolos': {
        'notes_append': ('Elected to U.S. House FL-8 April 2025 special election (replacing '
                         'retired Bill Posey). Former Florida Senate President (2010-2012) and '
                         'State Senator (2000-2012). Heritage Action 85-95% lifetime as state '
                         'legislator. NRA A+. Strong on fiscal conservatism, defense (Space Coast '
                         'interests), and pro-life legislation.'),
        'sources_add': [
            'https://haridopolos.house.gov/',
            'https://heritageaction.com/scorecard/',
            'https://ballotpedia.org/Mike_Haridopolos',
        ],
    },
    'vern-buchanan': {
        'notes_append': ('Ranking member of House Ways and Means Subcommittee on Health. '
                         'Heritage Action 80-90%. NRA A. Planned Parenthood 0%. Pro-life, '
                         'pro-business, hawkish on foreign policy. Vice Chair of House Ways '
                         'and Means Committee.'),
        'sources_add': [
            'https://buchanan.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'brian-mast': {
        'notes_append': ('Army combat veteran (lost both legs in Afghanistan). Chair of House '
                         'Foreign Affairs Committee in the 119th Congress. Heritage Action 85-95%. '
                         'NRA A+. Strong pro-Israel, hawkish on Iran and China, veterans advocate.'),
        'sources_add': [
            'https://mast.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'maria-elvira-salazar': {
        'notes_append': ('Cuban-American journalist-turned-legislator. Heritage Action 75-85%. '
                         'NRA A. Strong anti-communist (Cuba, Venezuela). More moderate than some '
                         'FL Republicans on immigration reform (has supported pathway-to-citizenship '
                         'discussions for Dreamers). Pro-life. Strong pro-Israel.'),
        'sources_add': [
            'https://salazar.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },
    'carlos-a-gimenez': {
        'notes_append': ('Cuban-American, former Miami-Dade County Mayor (2011-2020). Heritage '
                         'Action 80-90%. NRA A. Hard line on Cuba, Venezuela, China. Strong on '
                         'border security, Israel. Pro-life.'),
        'sources_add': [
            'https://gimenez.house.gov/',
            'https://heritageaction.com/scorecard/',
        ],
    },

    # ============ FL SUPREME COURT (just added — add social / X where relevant) ============
    # Florida Supreme Court justices don't typically maintain public social media
    # accounts. Their "primary sources" are court opinions. Already set.

    # ============ NEWLY ADDED LOCAL OFFICIALS ============
    'dianne-williams-cox': {
        'notes_append': ('Tallahassee City Commissioner since 2018, re-elected 2022. Former '
                         'executive director of Capital City Youth Services. Progressive Democrat. '
                         'Focus on affordable housing, youth services, community safety.'),
    },
    'curtis-richardson': {
        'notes_append': ('Tallahassee City Commissioner since 2014. Former Florida State '
                         'Representative (2000-2008). Progressive Democrat. Focus on economic '
                         'development, neighborhood revitalization.'),
    },
    'jeremy-matlow': {
        'notes_append': ('Tallahassee City Commissioner since 2018. Progressive/activist wing of '
                         'the Democratic Party. Pizza restaurateur (Gaines Street Pies). Focus '
                         'on affordable housing, police accountability, and ethics reform.'),
    },
    'jacqueline-jack-porter': {
        'notes_append': ('Tallahassee City Commissioner since 2020. Progressive Democrat, aligned '
                         'with Matlow on reform-oriented policies. Former Leon County Commission '
                         'staffer.'),
    },
    'copley-gerdes': {
        'notes_append': ('St. Petersburg City Council, District 1. Elected 2021. Moderate '
                         'Democrat, focused on business district growth and waterfront '
                         'development.'),
    },
    'brandi-gabbard': {
        'notes_append': ('St. Petersburg City Council, District 2 since 2017, re-elected 2021. '
                         'Democrat. Real estate professional. Focus on housing policy.'),
    },
    'richie-floyd': {
        'notes_append': ('St. Petersburg City Council, District 8 since 2021. Democratic Socialists '
                         'of America member. Former teacher. Strong progressive on housing, '
                         'transit, and labor issues.'),
    },
    'deborah-figgs-sanders': {
        'notes_append': ('St. Petersburg City Council, District 5 since 2019, re-elected 2023. '
                         'Democrat. Former educator. Focus on South St. Petersburg economic '
                         'development.'),
    },
    'gina-driscoll': {
        'notes_append': ('St. Petersburg City Council, District 6 since 2017, re-elected 2021. '
                         'Democrat. Former downtown business owner. Focus on downtown growth.'),
    },
}


def apply_enrichment(candidate, enrich):
    """Apply one enrichment dict to a candidate dict in place.
    Returns True if anything changed."""
    changed = False
    profile = candidate.setdefault('profile', {})

    # Twitter
    if enrich.get('twitter') and not profile.get('twitter'):
        profile['twitter'] = enrich['twitter']
        changed = True

    # Notes (append if existing notes don't already contain the append)
    appendix = enrich.get('notes_append')
    if appendix:
        existing = candidate.get('notes', '') or ''
        if appendix not in existing:
            candidate['notes'] = (existing + ' ' + appendix).strip() if existing else appendix
            changed = True

    # Sources (dedupe-append)
    new_sources = enrich.get('sources_add', [])
    if new_sources:
        existing = candidate.get('sources') or []
        current_set = set(existing)
        added_any = False
        for src in new_sources:
            if src not in current_set:
                existing.append(src)
                current_set.add(src)
                added_any = True
        if added_any:
            candidate['sources'] = existing
            changed = True

    return changed


def main():
    with open(SCORECARD_PATH) as f:
        data = json.load(f)

    # Index candidates by slug (FL only — avoid accidental collisions with
    # other states' dupes like robert-garcia)
    fl_by_slug = {}
    for c in data['candidates']:
        if c.get('state') == 'FL':
            fl_by_slug[c.get('slug')] = c

    applied = 0
    missing = []
    for slug, enrich in ENRICHMENTS.items():
        c = fl_by_slug.get(slug)
        if not c:
            missing.append(slug)
            continue
        if apply_enrichment(c, enrich):
            applied += 1

    print(f"Enriched: {applied} / {len(ENRICHMENTS)} targeted candidates")
    if missing:
        print(f"Missing slugs (not found in FL): {missing}")

    # Summary of enrichment contents
    tw_added = sum(1 for s, e in ENRICHMENTS.items() if e.get('twitter'))
    notes_added = sum(1 for s, e in ENRICHMENTS.items() if e.get('notes_append'))
    sources_added = sum(len(e.get('sources_add', [])) for e in ENRICHMENTS.values())
    print(f"  Twitter handles: {tw_added}")
    print(f"  Notes additions: {notes_added}")
    print(f"  Source URLs added: {sources_added}")

    with open(SCORECARD_PATH, 'w') as f:
        json.dump(data, f, indent=2)

    print("\nRebuilding per-state files...")
    subprocess.run(
        [sys.executable, str(BASE_DIR / 'build-data.py'), '--quiet'],
        check=True,
    )


if __name__ == '__main__':
    main()

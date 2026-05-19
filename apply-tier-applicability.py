#!/usr/bin/env python3
"""
apply-tier-applicability.py — annotate each of the 50 v4.0 questions with
`applicable_at` = list of office tiers ('federal', 'state', 'local')
where the question is scoreable based on real authority.

Per Adam's 2026-05-18 directive (Option C hybrid): the 100-pt rubric was
calibrated for federal officials, but many questions don't apply to
state/local officials who have no authority on those issues (e.g.,
Article I war powers for a mayor, Pentagon audits for a state senator).

Ship Option B (N/A masking) now via this script + dynamic-max retrofit;
Option A (tier-specific question banks) can layer on top later.

This script:
  1. Reads data/scorecard.json
  2. Adds `applicable_at` field to each category's questions metadata
  3. Optionally retrofits candidate score arrays: replaces True/False
     with the string 'N/A' on out-of-tier questions (via --retrofit)

The applicable_at matrix below is the AUTHORITATIVE source for tier
applicability. Update here if a question should apply at more/fewer tiers.

OFFICE-TO-TIER classifier rules:
  federal  = US Pres/VP, US Sen, US House, US Cabinet, federal agency
             heads, SCOTUS, US Ambassadors, federal-judicial
  state    = Governor, Lt Gov, State Sen, State Rep, State AG, State SoS,
             State Treasurer, State Auditor, state-judicial
  local    = Mayor, City Council, County Board, School Board, DA,
             Sheriff, City Clerk, local-judicial

Officials at a higher tier ALSO have authority on issues lower tiers
care about (a US Senator can hold positions on local issues), but for
scoring we apply the question only at the LOWEST tier where the official
has real authority to act. Federal officials get ALL 50 questions because
they have direct authority on federal questions AND can vote on issues
that affect state/local (e.g., a senator's vote on No Sanctuary Cities Act).
"""
import json
import re
import sys

SCORECARD = 'data/scorecard.json'

# Tier matrix: (category_id, q_index_0_based) -> list of tiers
# Tiers: 'federal', 'state', 'local'
# A question applicable_at ['federal'] is ONLY scoreable for federal officials.
# A question applicable_at ['federal', 'state', 'local'] is scoreable everywhere.
QUESTION_TIERS = {
    # ─── sanctity_of_life ───
    # q0: Affirms life begins at conception / personhood
    #   → universal (any official can make a public statement / cast a vote)
    ('sanctity_of_life', 0): ['federal', 'state', 'local'],
    # q1: Voted for / advocates abortion abolition
    #   → federal + state (DAs at local can decline-to-enforce abortion laws too)
    ('sanctity_of_life', 1): ['federal', 'state', 'local'],
    # q2: Opposes embryonic stem-cell research / IVF embryo discard
    #   → federal + state (state can regulate IVF; locals can't)
    ('sanctity_of_life', 2): ['federal', 'state'],
    # q3: Opposes euthanasia / PAS / quality-of-life rationing
    #   → federal + state (state-leg passes PAS laws)
    ('sanctity_of_life', 3): ['federal', 'state'],
    # q4: Never accepted PP / NARAL / EMILY's List funding
    #   → federal + state (federal/state candidates raise from these PACs;
    #     local candidates rarely on their radar)
    ('sanctity_of_life', 4): ['federal', 'state'],

    # ─── biblical_marriage ───
    # q0: Affirms marriage as one-man-one-woman (universal — any official)
    ('biblical_marriage', 0): ['federal', 'state', 'local'],
    # q1: Opposes SSM / civil unions / domestic partnerships in law
    #   → federal + state (states can refuse to recognize; locals can't redefine)
    ('biblical_marriage', 1): ['federal', 'state'],
    # q2: Rejects transgender ideology / affirms biological sex
    #   → universal (school boards directly relevant for K-12)
    ('biblical_marriage', 2): ['federal', 'state', 'local'],
    # q3: Supports no-fault divorce reform / strengthens marriage covenant
    #   → state primarily (divorce is state law)
    ('biblical_marriage', 3): ['federal', 'state'],
    # q4: Opposes LGBT promotion in public policy/schools/military/corporate
    #   → universal (mayors sign proclamations; school boards on curriculum)
    ('biblical_marriage', 4): ['federal', 'state', 'local'],

    # ─── family_child_sovereignty ───
    # q0: Universal school choice / homeschool freedom / no compulsory PS
    #   → federal + state (state runs ed; locals influence via boards)
    ('family_child_sovereignty', 0): ['federal', 'state', 'local'],
    # q1: Parental notification + consent on medical/gender interventions
    #   → universal (school boards, county DAs, state legs, federal Congress)
    ('family_child_sovereignty', 1): ['federal', 'state', 'local'],
    # q2: Opposes CRT/SOGI/gender-ideology curricula in K-12
    #   → state + local primarily (school boards are PRIMARY actors)
    ('family_child_sovereignty', 2): ['federal', 'state', 'local'],
    # q3: Age-verify porn + criminal penalties for sexualization of minors
    #   → federal + state primarily (state-leg passes age-verification laws)
    ('family_child_sovereignty', 3): ['federal', 'state'],
    # q4: Faith-based adoption/foster (no SS-couple placement)
    #   → federal + state (state runs foster systems)
    ('family_child_sovereignty', 4): ['federal', 'state'],

    # ─── christian_liberty ───
    # q0: Right to publicly profess Christ in all spheres
    #   → universal (any public official can affirm or oppose)
    ('christian_liberty', 0): ['federal', 'state', 'local'],
    # q1: Conscience exemptions for Christian professionals
    #   → federal + state (state-leg passes most RFRA-style protections)
    ('christian_liberty', 1): ['federal', 'state'],
    # q2: Opposes compelled speech against Christian conviction
    #   → universal (universities, school boards, employer mandates all relevant)
    ('christian_liberty', 2): ['federal', 'state', 'local'],
    # q3: Public-square Christian symbols / prayer in public bodies
    #   → universal (city council invocations, school prayer, federal seals)
    ('christian_liberty', 3): ['federal', 'state', 'local'],
    # q4: Opposes state-funded non-Christian religious displays/curricula
    #   → universal
    ('christian_liberty', 4): ['federal', 'state', 'local'],

    # ─── economic_stewardship ───
    # q0: Opposes CBDC / supports cash + decentralized crypto
    #   → federal primarily; state SoS + state Treasurer have limited say
    ('economic_stewardship', 0): ['federal', 'state'],
    # q1: Sound money / gold-silver / audit-Fed
    #   → FEDERAL ONLY (states can't issue money; states can opt out of
    #     ESG funds but that's q4)
    ('economic_stewardship', 1): ['federal'],
    # q2: Opposes deficit spending / balanced-budget amendment
    #   → universal (federal national debt + state budgets + city budgets all relevant)
    ('economic_stewardship', 2): ['federal', 'state', 'local'],
    # q3: Usury limits / anti-debt-slavery / tithe-friendly tax
    #   → federal + state
    ('economic_stewardship', 3): ['federal', 'state'],
    # q4: Opposes WEF/ESG/Davos capture / anti-trust on financial cartels
    #   → federal + state (state treasurers can pull pension funds from BlackRock etc.)
    ('economic_stewardship', 4): ['federal', 'state'],

    # ─── election_integrity ───
    # q0: Hand-counted paper ballots / opposes electronic machines
    #   → state + local (states + counties run elections; federal sets some standards)
    ('election_integrity', 0): ['federal', 'state', 'local'],
    # q1: Photo voter ID + citizenship verification
    #   → universal (state SoS sets rules; federal can preempt; locals enforce)
    ('election_integrity', 1): ['federal', 'state', 'local'],
    # q2: Single-day in-person voting / minimal absentee
    #   → state + federal (state laws set early-vote windows)
    ('election_integrity', 2): ['federal', 'state'],
    # q3: Opposes mass mail-in / drop boxes / ballot harvesting
    #   → state + federal
    ('election_integrity', 3): ['federal', 'state'],
    # q4: Opposes "Zuckerbucks" + foreign election interference
    #   → universal (city clerks accept or reject private grants)
    ('election_integrity', 4): ['federal', 'state', 'local'],

    # ─── border_immigration ───
    # q0: Physical border barrier + military presence
    #   → FEDERAL ONLY (states can't fund border wall; TX exception via state-funded)
    ('border_immigration', 0): ['federal', 'state'],
    # q1: Mandatory deportation of illegals
    #   → federal + state (states can decline to cooperate; DAs can decline prosecution)
    ('border_immigration', 1): ['federal', 'state', 'local'],
    # q2: Opposes sanctuary policies + federal preemption
    #   → universal (cities + counties + states + federal all touch this)
    ('border_immigration', 2): ['federal', 'state', 'local'],
    # q3: Mandatory E-Verify for employment / benefits
    #   → federal + state (state can mandate beyond federal)
    ('border_immigration', 3): ['federal', 'state'],
    # q4: Opposes birthright citizenship for illegals / tourist births / foreign farmland ownership
    #   → federal + state (states can restrict foreign farmland ownership)
    ('border_immigration', 4): ['federal', 'state'],

    # ─── self_defense ───
    # q0: Affirms 2A as individual right; opposes registries
    #   → universal (any official can take public position)
    ('self_defense', 0): ['federal', 'state', 'local'],
    # q1: Opposes red-flag laws / mag limits / AWB / registries
    #   → federal + state (states pass these; locals can opt in/out)
    ('self_defense', 1): ['federal', 'state', 'local'],
    # q2: Constitutional carry (no permit required)
    #   → federal + state (state law sets carry permits)
    ('self_defense', 2): ['federal', 'state'],
    # q3: Opposes private-sale background checks / opposes UBC
    #   → federal + state
    ('self_defense', 3): ['federal', 'state'],
    # q4: Castle Doctrine + stand-your-ground
    #   → state primarily (state law)
    ('self_defense', 4): ['federal', 'state'],

    # ─── foreign_policy_restraint ───
    # q0: Article I war powers required before military action
    #   → FEDERAL ONLY
    ('foreign_policy_restraint', 0): ['federal'],
    # q1: Immediate withdrawal from forever wars / repeal AUMFs
    #   → FEDERAL ONLY
    ('foreign_policy_restraint', 1): ['federal'],
    # q2: Opposes foreign aid to hostile nations
    #   → FEDERAL ONLY
    ('foreign_policy_restraint', 2): ['federal'],
    # q3: Never accepted AIPAC / foreign-linked PAC donations
    #   → federal + state (federal/state campaigns receive PAC money;
    #     local typically doesn't)
    ('foreign_policy_restraint', 3): ['federal', 'state'],
    # q4: Opposes WHO/UN/NATO governance overreach
    #   → FEDERAL ONLY
    ('foreign_policy_restraint', 4): ['federal'],

    # ─── industry_capture ───
    # q0: Opposes pharma mandates / informed consent
    #   → federal + state (states set vaccine mandates for schools)
    ('industry_capture', 0): ['federal', 'state', 'local'],
    # q1: Repeal pharma liability shields (NCVIA / PREP Act)
    #   → FEDERAL ONLY (federal liability shields can only be repealed federally)
    ('industry_capture', 1): ['federal'],
    # q2: Opposes Big Ag consolidation / anti-trust on Bayer/Monsanto/Cargill
    #   → federal + state (state AGs can sue)
    ('industry_capture', 2): ['federal', 'state'],
    # q3: Raw-milk freedom / small-farm protections / anti-USDA-EPA overreach
    #   → federal + state + local (county boards regulate small farms)
    ('industry_capture', 3): ['federal', 'state', 'local'],
    # q4: Defense-contractor accountability / Pentagon audit / no revolving door
    #   → FEDERAL ONLY
    ('industry_capture', 4): ['federal'],
}


def classify_office_tier(c):
    """Return 'federal' | 'state' | 'local' | None based on candidate.office.

    Rules:
      federal = US Pres/VP, US Senator, US House Rep, US Cabinet
                (Secretary/Director/Acting AG/Ambassador/Administrator),
                SCOTUS Justice, federal agency head
      state   = Governor, Lt Governor, State Senator/Rep/Delegate/Assembly,
                State Attorney General, State Secretary of State,
                State Treasurer/Auditor/Comptroller, state Supreme Court
      local   = Mayor, City Council, County Commissioner/Supervisor,
                School Board, District Attorney, Sheriff, City Clerk,
                local-judicial
    """
    office = c.get('office') or ''
    if not office:
        # Empty office field — fall back to jurisdiction
        jur = (c.get('jurisdiction') or '').lower()
        if 'executive branch' in jur or 'judicial branch' in jur:
            return 'federal'
        return None

    o = office.lower()

    # Federal
    if re.search(r'\b(president|vice president|u\.?s\.?\s+sen|u\.?s\.?\s+hous|u\.?s\.?\s+rep|'
                 r'united states sen|united states hous|united states rep|secretary of|'
                 r'acting attorney general|attorney general of the united states|'
                 r'director of|administrator of|ambassador|chief of staff|deputy chief of staff|'
                 r'homeland security advisor|chief justice|associate justice.+supreme court|'
                 r'special envoy)', o):
        # But carve out STATE attorneys general which match "attorney general"
        if re.search(r'^attorney general$|state attorney general', o) and 'united states' not in o:
            return 'state'
        return 'federal'

    # State-level — governors, lt govs, state legislators, state AGs, state SoS, state treasurer
    if re.search(r'\bgovernor\b|^lt\.?\s+governor|lieutenant governor|'
                 r'state senator|state senate|state representative|state hous|'
                 r'state assembl|^delegate$|delegate \(', o):
        return 'state'
    if re.search(r'^attorney general$|secretary of state$|state treasurer|state auditor|'
                 r'state comptroller', o):
        return 'state'
    # State Supreme Court
    if 'state supreme court' in o or re.search(r'(chief justice|justice).+state', o):
        return 'state'

    # Local
    if re.search(r'\bmayor\b|city council|town council|borough council|'
                 r'county (commissioner|supervisor|judge|board)|'
                 r'school board|board of education|'
                 r'district attorney|sheriff|city clerk|city attorney|'
                 r'commonwealth\'?s attorney', o):
        return 'local'

    # Default — try jurisdiction
    jur = (c.get('jurisdiction') or '').lower()
    if jur in ('executive branch', 'judicial branch', 'federal'):
        return 'federal'

    # Final fallback — assume state (most state legislators have office strings
    # like "Texas State Representative" that should match above, but stragglers
    # like raw "Representative" are common in less-curated records).
    return 'state'


def main():
    apply_mode = '--apply' in sys.argv
    retrofit = '--retrofit' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    # 1. Add applicable_at to each question (category-level metadata)
    cats_updated = 0
    for cat in sc.get('categories', []):
        cat_id = cat['id']
        # Add applicable_at as a parallel list to questions
        applicable_at = []
        for q_idx in range(len(cat.get('questions', []))):
            tiers = QUESTION_TIERS.get((cat_id, q_idx))
            if tiers is None:
                print(f"⚠️  no tier mapping for {cat_id}[{q_idx}] — defaulting to ['federal']")
                tiers = ['federal']
            applicable_at.append(tiers)
        cat['applicable_at'] = applicable_at
        cats_updated += 1
    print(f'Added applicable_at metadata to {cats_updated} categories.')

    # 2. If --retrofit, walk all candidates and replace out-of-tier bool/null
    #    with 'N/A' string in scores arrays
    retrofit_stats = {'na_set': 0, 'preserved_bool': 0, 'tier_unknown': 0}
    if retrofit:
        for c in sc.get('candidates', []):
            tier = classify_office_tier(c)
            if tier is None:
                retrofit_stats['tier_unknown'] += 1
                continue
            scores = c.get('scores') or {}
            for cat_id, vals in scores.items():
                if not isinstance(vals, list): continue
                for i in range(len(vals)):
                    applicable = QUESTION_TIERS.get((cat_id, i), ['federal'])
                    if tier not in applicable:
                        # Out-of-tier question for this candidate
                        if vals[i] in (True, False):
                            vals[i] = 'N/A'
                            retrofit_stats['na_set'] += 1
                        elif vals[i] is None:
                            vals[i] = 'N/A'
                            retrofit_stats['na_set'] += 1
                    # If in-tier, preserve whatever's there
        print(f'\nRetrofit applied:')
        for k, v in retrofit_stats.items():
            print(f'  {k}: {v}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run. Re-run with --apply (and optionally --retrofit) to write.')


if __name__ == '__main__':
    main()

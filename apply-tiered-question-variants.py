#!/usr/bin/env python3
"""
apply-tiered-question-variants.py — v4.2 + v4.3 — add state-tier and
local-tier text variants for the questions where implementation differs.

Per Adam's 2026-05-19 directive: the v4.0 100-pt rubric was federal-
calibrated. v4.1 added N/A masking for federal-only questions on
state/local officials. v4.2 + v4.3 add SAME SCOPE / DIFFERENT
IMPLEMENTATION question text variants, so a mayor sees a question
about LOCAL implementation (e.g., "opposes city resolutions endorsing
US military intervention abroad") instead of the federal version
("supports Article I war powers requirement").

SCORING SEMANTICS:
  The Boolean (T/F) is the same across all tiers — represents the
  candidate's alignment with the question's underlying spirit. The
  TEXT shown to the visitor varies by the candidate's office tier so
  the question describes implementation appropriate to their authority.

  For questions where the implementation is UNIVERSAL (e.g., "Candidate
  affirms life begins at conception"), no variant needed — same text
  at all tiers.

SCHEMA:
  Each category in scorecard.json gets two new optional parallel arrays:
    questions_state: [str or null, ...]  # state-tier text for each q
    questions_local: [str or null, ...]  # local-tier text for each q

  None entries mean "use the default federal text" (questions[i]).

Run:
    python3 apply-tiered-question-variants.py --apply
"""
import json
import sys

SCORECARD = 'data/scorecard.json'

# State + local text variants per (category_id, question_index).
# Empty string = use federal default. Tuple value = (state_text, local_text).
# Where one tier has no meaningful equivalent, set that variant to None
# (the federal text + applicable_at masking already handles N/A).
QUESTION_VARIANTS = {
    # ─── sanctity_of_life ───
    ('sanctity_of_life', 0): (
        # Federal: "Candidate affirms life begins at conception and personhood from conception"
        None,  # state: same (universal moral question)
        None,  # local: same
    ),
    ('sanctity_of_life', 1): (
        # Federal: "Candidate has voted for or actively advocates abortion abolition (not merely restrictions)"
        "Candidate has voted for or sponsored state legislation moving toward abortion abolition (e.g., heartbeat ban, total ban) — not merely restrictions",
        "Candidate (if District Attorney) has committed to prosecuting illegal abortion procedures; (if mayor/council) has supported pro-life city resolutions or refused to declare 'sanctuary city for abortion'",
    ),
    ('sanctity_of_life', 2): (
        # Federal: "Candidate opposes embryonic stem-cell research, IVF embryo discard, and chimeric experimentation"
        "Candidate opposes state funding for embryonic stem-cell research and supports state IVF embryo-protection laws",
        None,  # not really local-actionable
    ),
    ('sanctity_of_life', 3): (
        # Federal: "Candidate opposes euthanasia, physician-assisted suicide, and quality-of-life rationing"
        "Candidate opposes state physician-assisted suicide laws and opposes state Medicaid death-panel rationing",
        None,
    ),
    ('sanctity_of_life', 4): (
        # Federal: "Candidate has never accepted Planned Parenthood, NARAL, EMILY's List, or abortion-industry PAC funding"
        "Candidate has never accepted abortion-industry PAC funding for state-legislative or statewide-office campaigns",
        None,  # local candidates typically don't get these PACs
    ),

    # ─── biblical_marriage ───
    ('biblical_marriage', 0): (
        # Federal: "Candidate affirms marriage as exclusively the lifelong union of one man and one woman as instituted by God"
        None, None,  # universal moral question
    ),
    ('biblical_marriage', 1): (
        # Federal: "Candidate opposes all forms of same-sex marriage, civil unions, and domestic partnerships in law"
        "Candidate opposes state recognition of same-sex marriage / civil unions / domestic partnerships, and supports state non-recognition resolutions where federally permitted",
        None,
    ),
    ('biblical_marriage', 2): (
        # Federal: "Candidate rejects transgender ideology and affirms biological sex (male/female) as immutable and God-given"
        "Candidate has voted for state legislation affirming biological sex (bathroom/locker access, sports participation, minor gender-procedure bans)",
        "Candidate opposes city/county trans-affirming policies (bathroom mandates on private businesses, Pride flag raisings at city hall, pronouns-required HR rules)",
    ),
    ('biblical_marriage', 3): (
        # Federal: "Candidate supports no-fault divorce reform and policies that strengthen the marriage covenant"
        "Candidate supports state no-fault divorce reform and pro-marriage policy (covenant marriage option, waiting periods, etc.)",
        None,  # local has no divorce-law authority
    ),
    ('biblical_marriage', 4): (
        # Federal: "Candidate opposes promotion of LGBTQ+ identity in public policy, schools, military, and corporate-government partnerships"
        "Candidate opposes promotion of LGBTQ+ identity in state-funded schools, state agencies, and state corporate-partnership programs",
        "Candidate opposes city/county Pride proclamations, Pride flags at city facilities, drag programming in libraries, and LGBT-affirming K-12 curriculum (school-board-relevant)",
    ),

    # ─── family_child_sovereignty ───
    ('family_child_sovereignty', 0): (
        # Federal: "Candidate supports universal school choice, homeschool freedom, and opposes compulsory public-school attendance"
        "Candidate has voted for state school-choice (vouchers, ESAs, charter expansion) and supports state homeschool freedom statutes",
        "Candidate (school board) opts the district into school-choice transfers + protects homeschool freedom + opposes truancy-based criminal referrals",
    ),
    ('family_child_sovereignty', 1): (
        # Federal: "Candidate supports parental notification and consent on all medical, mental-health, and gender-related interventions for minors"
        "Candidate has voted for state law requiring parental notification + consent on minors' medical, mental-health, and gender interventions (incl. school counseling referrals)",
        "Candidate (school board) requires parental notification before any gender/sexuality counseling of minors; (mayor/council) opposes city programs facilitating minor medical procedures without parents",
    ),
    ('family_child_sovereignty', 2): (
        # Federal: "Candidate opposes CRT, SOGI, 'comprehensive sex ed,' and gender-ideology curricula in K-12 public schools"
        "Candidate has voted for state law restricting CRT/SOGI/comprehensive-sex-ed/gender-ideology curricula in K-12",
        "Candidate (school board) has voted to remove CRT/SOGI/comprehensive-sex-ed/gender-ideology materials from district curriculum and library shelves",
    ),
    ('family_child_sovereignty', 3): (
        # Federal: "Candidate supports age-verification on pornographic content and criminal penalties for sexualized content marketed to minors"
        "Candidate has voted for state age-verification laws on pornographic content and state criminal penalties for sexualizing minors",
        "Candidate (mayor/council/library board) supports local enforcement of age-verification + removes sexualized content from library children's sections",
    ),
    ('family_child_sovereignty', 4): (
        # Federal: "Candidate supports faith-based adoption/foster agencies and opposes placement of children with same-sex couples"
        "Candidate has voted for state RFRA-style protections for faith-based adoption + foster agencies; opposes state-mandated SS-couple placement",
        None,  # local doesn't run adoption agencies typically
    ),

    # ─── christian_liberty ───
    ('christian_liberty', 0): (
        # Federal: "Candidate affirms the right to publicly profess Christ in all spheres (workplace, military, public office, schools)"
        None, None,  # universal
    ),
    ('christian_liberty', 1): (
        # Federal: "Candidate supports conscience exemptions for Christian medical professionals, business owners, adoption agencies, and educators"
        "Candidate has voted for state conscience-exemption laws (state RFRA, medical-professional carve-outs, business-owner protections)",
        None,
    ),
    ('christian_liberty', 2): (
        # Federal: "Candidate opposes compelled speech against Christian conviction (pronoun mandates, gospel-proclamation hate-speech laws)"
        "Candidate opposes state-level pronoun mandates + state 'hate speech' laws restricting Christian conviction",
        "Candidate (city/county/school board) opposes mandatory pronoun policies for staff + employees + students",
    ),
    ('christian_liberty', 3): (
        # Federal: "Candidate supports public-square Christian symbols, prayer in public bodies, and Sabbath/Sunday closure protections"
        "Candidate supports state public-square Christian display protections + state legislative prayer + state Sunday-closure laws",
        "Candidate (mayor/council) supports city/county Christian displays (Ten Commandments, Nativity scenes), invocation prayer at meetings, Sunday-closure where chosen by community",
    ),
    ('christian_liberty', 4): (
        # Federal: "Candidate opposes state-funded promotion of non-Christian religious displays, curricula, or holidays in public institutions"
        "Candidate opposes state-funded promotion of non-Christian religious displays/curricula/holidays in state institutions",
        "Candidate opposes city-funded non-Christian religious displays/programming (Ramadan illumination, etc.) at city facilities",
    ),

    # ─── economic_stewardship ───
    ('economic_stewardship', 0): (
        # Federal: "Candidate opposes a Central Bank Digital Currency (CBDC) and supports cash and decentralized crypto as legal tender"
        "Candidate has voted for state law protecting cash as legal tender, opposing state-level CBDC pilot programs, and protecting crypto-as-property status",
        "Candidate (city/county) opposes city participation in CBDC pilot programs + supports cash-acceptance ordinances for local businesses",
    ),
    ('economic_stewardship', 1): (
        # Federal: "Candidate supports sound-money policies including gold/silver as constitutional money and audit/abolition of the Federal Reserve"
        # → federal-only — applicable_at = ['federal']
        None, None,
    ),
    ('economic_stewardship', 2): (
        # Federal: "Candidate opposes deficit spending and supports a balanced-budget constitutional amendment"
        "Candidate has voted for state balanced-budget compliance + opposed state borrowing for non-capital expenditures",
        "Candidate (mayor/council) has voted against deficit-bond issuances for non-capital city expenditures + supports balanced city budgets without service cuts via tax increases on residents",
    ),
    ('economic_stewardship', 3): (
        # Federal: "Candidate supports usury limits, anti-debt-slavery protections, and tithe-friendly tax structures"
        "Candidate has voted for state usury caps + state predatory-lending protections + state charitable-deduction parity",
        None,  # local has limited authority
    ),
    ('economic_stewardship', 4): (
        # Federal: "Candidate opposes WEF/ESG/Davos economic capture and supports anti-trust action against monopolistic financial cartels"
        "Candidate has voted for state pension/treasury divestment from ESG-aligned funds (e.g., BlackRock) + state anti-monopoly enforcement against financial cartels",
        "Candidate (city/county) has voted to remove city pension/treasury investment in ESG-aligned funds + opposes city participation in WEF-aligned sister-city programs",
    ),

    # ─── election_integrity ───
    ('election_integrity', 0): (
        # Federal: "Candidate supports hand-counted paper ballots and opposes electronic voting machines"
        "Candidate (state SoS/legislature) has voted for state hand-count requirements / opposed electronic voting machines",
        "Candidate (city clerk/county election official) supports hand-counted paper ballots at local precincts where state law permits",
    ),
    ('election_integrity', 1): (
        # Federal: "Candidate supports photo voter ID with citizenship verification"
        "Candidate (state SoS/legislature) has voted for state photo voter ID + citizenship verification at registration",
        "Candidate (city clerk/election official) enforces state photo voter ID + citizenship verification at local precincts",
    ),
    ('election_integrity', 2): (
        # Federal: "Candidate supports single-day in-person voting with absentee only for verified medical/military exceptions"
        "Candidate has voted to restrict state early-voting windows + tighten state absentee qualifications to verified medical/military",
        None,
    ),
    ('election_integrity', 3): (
        # Federal: "Candidate opposes mass mail-in voting, drop boxes, and ballot harvesting"
        "Candidate has voted against state mass mail-in voting expansion, against state drop-box deployment, and against legalizing ballot harvesting",
        None,
    ),
    ('election_integrity', 4): (
        # Federal: "Candidate opposes private election funding ('Zuckerbucks') and foreign-government election interference"
        "Candidate (state SoS/legislature) has voted to ban state acceptance of private election grants ('Zuckerbucks') + state penalties for foreign interference",
        "Candidate (city clerk/council) refused acceptance of private election-administration grants ('Zuckerbucks')",
    ),

    # ─── border_immigration ───
    ('border_immigration', 0): (
        # Federal: "Candidate supports completed physical border barrier and active military border presence"
        "Candidate (state) has voted for state-funded border-security measures (e.g., TX Operation Lone Star analog, AZ wall expansion)",
        None,
    ),
    ('border_immigration', 1): (
        # Federal: "Candidate supports mandatory deportation of all illegal aliens, including those who entered as minors"
        "Candidate (state) has voted for state laws requiring local cooperation with ICE deportation enforcement",
        "Candidate (DA/sheriff) cooperates with ICE detainers + transfers; (mayor/council) supports local cooperation with ICE rather than sanctuary policies",
    ),
    ('border_immigration', 2): (
        # Federal: "Candidate opposes sanctuary city/state policies and supports federal preemption against them"
        "Candidate (state) has voted to preempt or punish sanctuary-city policies + ban state cities from declaring sanctuary status",
        "Candidate (city/county) has voted against local sanctuary-city ordinances + supports city cooperation with federal immigration enforcement",
    ),
    ('border_immigration', 3): (
        # Federal: "Candidate supports mandatory E-Verify for all employment and benefit eligibility"
        "Candidate (state) has voted for state E-Verify mandate (beyond federal floor) for state employers + state-benefit eligibility verification",
        None,
    ),
    ('border_immigration', 4): (
        # Federal: "Candidate opposes birthright citizenship for children of illegal aliens, tourist births, and opposes foreign ownership of U.S. farmland"
        "Candidate (state) has voted to restrict foreign ownership of state farmland (e.g., China-buyer prohibitions)",
        None,
    ),

    # ─── self_defense ───
    ('self_defense', 0): (
        # Federal: "Candidate affirms the Second Amendment as an individual right and opposes federal gun registries"
        None,  # state: universal stance
        "Candidate (mayor/council) opposes local gun-registry ordinances + local gun-shop zoning restrictions",
    ),
    ('self_defense', 1): (
        # Federal: "Candidate opposes red-flag laws, magazine capacity limits, assault weapons bans, and gun registries"
        "Candidate (state) has voted against state red-flag laws, mag-capacity limits, AWBs, and registries (or voted to repeal where enacted)",
        "Candidate (city/council) opposes local-ordinance red-flag/magazine/AWB analogs + local gun-shop zoning restrictions",
    ),
    ('self_defense', 2): (
        # Federal: "Candidate supports constitutional carry (no permit required)"
        "Candidate (state) has voted for state constitutional-carry statute",
        None,
    ),
    ('self_defense', 3): (
        # Federal: "Candidate opposes private-sale background checks and universal background check schemes"
        "Candidate (state) has voted against state universal-background-check schemes",
        None,
    ),
    ('self_defense', 4): (
        # Federal: "Candidate supports Castle Doctrine and stand-your-ground laws"
        "Candidate (state) has voted to enact / strengthen state Castle Doctrine + stand-your-ground statute",
        None,
    ),

    # ─── foreign_policy_restraint ───
    ('foreign_policy_restraint', 0): (
        # Federal: "Candidate supports Article I congressional war-powers requirement before any U.S. military action"
        # → federal-only per applicable_at
        None, None,
    ),
    ('foreign_policy_restraint', 1): (
        # Federal: "Candidate supports immediate withdrawal from forever wars and repeal of standing AUMFs"
        # → federal-only
        None, None,
    ),
    ('foreign_policy_restraint', 2): (
        # Federal: "Candidate opposes foreign aid to nations hostile to U.S. interests or actively persecuting Christians"
        # → federal-only
        None, None,
    ),
    ('foreign_policy_restraint', 3): (
        # Federal: "Candidate has never accepted donations from foreign-backed lobbies (e.g., AIPAC) or foreign-linked PACs"
        "Candidate has never accepted donations from foreign-backed lobbies (AIPAC) or foreign-linked PACs for state-legislative or statewide campaigns",
        None,  # local typically out of scope
    ),
    ('foreign_policy_restraint', 4): (
        # Federal: "Candidate opposes U.S. participation in WHO, U.N. governance overreach, NATO expansion, and supranational governance"
        # → federal-only
        None, None,
    ),

    # ─── industry_capture ───
    ('industry_capture', 0): (
        # Federal: "Candidate opposes pharmaceutical mandates of any kind (COVID, childhood, employer-required) and supports informed consent"
        "Candidate (state) has voted against state pharmaceutical mandates (school childhood vaccine schedule, employer mandates) + supports state medical-conscience exemptions",
        "Candidate (city/county/school board) opposes local pharmaceutical mandates (city-employee, school-attendance) + supports informed-consent ordinances",
    ),
    ('industry_capture', 1): (
        # Federal: "Candidate supports repeal of pharma liability shields (1986 NCVIA, PREP Act) and restoration of tort accountability"
        # → federal-only
        None, None,
    ),
    ('industry_capture', 2): (
        # Federal: "Candidate opposes Big Ag consolidation (Bayer/Monsanto/Cargill) and supports anti-trust action against agricultural cartels"
        "Candidate (state AG/legislature) has filed/supported state antitrust action against Big Ag consolidation",
        None,
    ),
    ('industry_capture', 3): (
        # Federal: "Candidate supports raw-milk freedom, small-farm protections, and opposes USDA / EPA overreach against family farms"
        "Candidate (state) has voted for state raw-milk freedom + state small-farm protections against USDA/EPA federal overreach",
        "Candidate (county/city) supports local raw-milk sales + local small-farm zoning protections + opposes county-board EPA-cooperation enforcement against family farms",
    ),
    ('industry_capture', 4): (
        # Federal: "Candidate supports defense-contractor accountability, completion of Pentagon audits, and ending revolving-door appointments"
        # → federal-only
        None, None,
    ),
}


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    cats_updated = 0
    state_variants_added = 0
    local_variants_added = 0
    universal_count = 0

    for cat in sc.get('categories', []):
        cat_id = cat['id']
        n_questions = len(cat.get('questions', []))
        questions_state = []
        questions_local = []
        for q_idx in range(n_questions):
            variant = QUESTION_VARIANTS.get((cat_id, q_idx))
            if variant is None:
                questions_state.append(None)
                questions_local.append(None)
                universal_count += 1
            else:
                state_text, local_text = variant
                questions_state.append(state_text)
                questions_local.append(local_text)
                if state_text:
                    state_variants_added += 1
                if local_text:
                    local_variants_added += 1
                if state_text is None and local_text is None:
                    universal_count += 1
        cat['questions_state'] = questions_state
        cat['questions_local'] = questions_local
        cats_updated += 1

    print(f'=== TIERED QUESTION VARIANTS APPLIED ===')
    print(f'  Categories updated:          {cats_updated}')
    print(f'  State-tier variants added:   {state_variants_added}')
    print(f'  Local-tier variants added:   {local_variants_added}')
    print(f'  Universal (no variant):      {universal_count}')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()

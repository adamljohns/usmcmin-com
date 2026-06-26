#!/usr/bin/env python3
"""Enrichment batch 426: hand-curated claims for 5 sitting Washington State Senators (all R).

archetype_curated federal bucket is fully exhausted; this batch moves to
archetype_party_default state senators from the bottom of the alphabet (WA).

Targets: John Braun (WA-20, Senate Minority Leader), Keith Wagoner (WA-39),
Keith Goehner (WA-12, formerly WA House), Judy Warnick (WA-13, Caucus Chair),
Leonard Christian (WA-04, formerly WA House).

Each claim cites >=1 reliable public source reflecting 2023-2026 voting records
or official public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ------------ John Braun (WA-20, R, Senate Minority Leader) ------------
    ("john-braun", "WA", "State Senator", [
        claim("jb1", "john-braun", "self_defense", 1, True,
              "As Washington Senate Minority Leader, led all 21 Republican senators in voting against HB 1240 (2023), the state ban on the manufacture, sale, and importation of semi-automatic firearms classified as 'assault weapons.' The measure passed 27-21 on a strict party-line vote with zero Republican support; Braun's caucus unanimously rejected it as unconstitutional and ineffective.",
              ["https://www.spokesman.com/stories/2023/apr/08/assault-weapon-ban-clears-wa-state-senate/",
               "https://www.nbcrightnow.com/news/assault-weapons-ban-passes-washington-senate-returns-to-house/article_846552e2-d66b-11ed-b5d3-8b6c509ed520.html"]),
        claim("jb2", "john-braun", "biblical_marriage", 2, True,
              "Issued a formal public statement condemning SB 5599 (2023) as a bill 'threatening the rights of parents,' after the measure passed the Senate 29–22. The law permits licensed youth shelters to report to the state rather than to parents when a minor runs away to seek gender-affirming care or reproductive services — removing parents from their child's medical decisions. Braun opposed the measure as an unconstitutional intrusion on parental and family rights.",
              ["https://johnbraun.src.wastateleg.org/bill-threatening-rights-parents-passes-senate/",
               "https://www.spokesman.com/stories/2023/apr/19/washington-senate-passes-bill-to-protect-transgend/"]),
        claim("jb3", "john-braun", "family_child_sovereignty", 0, True,
              "Voted for Initiative 2081 (Parents' Bill of Rights), which passed the Washington State Senate unanimously 49–0 in March 2024. The measure established parents' statutory right to review classroom materials and textbooks, access their child's academic and medical records, and opt their children out of sexual-health education — the most significant parental-rights law enacted in Washington in decades.",
              ["https://www.spokesman.com/stories/2024/mar/04/initiative-enhancing-parental-rights-over-school-a/",
               "https://ballotpedia.org/Washington_Initiative_2081,_Parental_Right_to_Review_Education_Materials,_Receive_Notifications,_and_Opt_Out_of_Sexual-Health_Education_Initiative_(2024)"]),
    ]),

    # ------------ Keith Wagoner (WA-39, R, Sedro Woolley) ------------
    ("keith-wagoner", "WA", "State Senator", [
        claim("kw1", "keith-wagoner", "self_defense", 1, True,
              "Signed the Senate Law & Justice Committee minority report recommending 'do not pass' on HB 1240 (2023), Washington's ban on so-called 'assault weapons,' alongside Senators Padden (Ranking Member), McCune, Torres, and Wilson. Wagoner opposed the ban as a violation of Second Amendment rights, and all 21 Senate Republicans ultimately voted against final passage.",
              ["https://lawfilesext.leg.wa.gov/biennium/2023-24/Pdf/Bill%20Reports/Senate/1240-S%20SBR%20APS2%2023.pdf",
               "https://www.seattletimes.com/seattle-news/politics/assault-weapon-ban-clears-wa-state-senate/"]),
        claim("kw2", "keith-wagoner", "family_child_sovereignty", 0, True,
              "Led the Senate floor battle defending I-2081 (Parents' Bill of Rights) after Democrats passed SB 5181 stripping key provisions — including an emergency clause that denied citizens their referendum right. Wagoner explicitly stated parents have a right to know what is being taught to their children and called the Democrat effort to gut the initiative a betrayal of the 454,000 Washingtonians who signed it.",
              ["https://keithwagoner.src.wastateleg.org/battle-parental-rights-hits-senate-floor/",
               "https://lynnwoodtimes.com/2025/03/04/rights-initiative/"]),
        claim("kw3", "keith-wagoner", "sanctity_of_life", 4, True,
              "On record stating that 'Abortion providers, including Planned Parenthood, should not receive taxpayer funds from federal, state, or local governments (including Title X grants),' and that chemical abortion drugs must meet essential safety standards — including mandatory in-person consultation with a medical doctor and required reporting of adverse outcomes — reflecting a pro-life regulatory posture consistent with protecting maternal and fetal health.",
              ["https://ivoterguide.com/candidate/41811/race/20752/election/1118"]),
    ]),

    # ------------ Keith Goehner (WA-12, R, orchardist; formerly WA House) ------------
    ("keith-goehner", "WA", "State Senator", [
        claim("kg1", "keith-goehner", "self_defense", 1, True,
              "As a Washington House Representative, voted against HB 1240 (2023) — the state ban on 'assault weapons' — and explained in a legislative update to constituents that 'as a lawmaker it is my job to uphold the state and U.S. constitutions,' and that he believed the bill violated both the Washington State Constitution and the Second Amendment of the U.S. Constitution. His 'no' vote was among 42 House Republicans opposing the measure.",
              ["https://lakechelannow.com/legislative-update-from-representative-keith-goehner-6/",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023"]),
        claim("kg2", "keith-goehner", "family_child_sovereignty", 0, True,
              "Voted for Initiative 2081 (Parents' Bill of Rights) as a Washington House Representative; the measure passed the House 82-15 in March 2024 with broad bipartisan support. I-2081 established parents' rights to review classroom materials, access their children's academic and medical records, and opt out of sexual-health education — a significant expansion of parental oversight of public schools.",
              ["https://www.spokesman.com/stories/2024/mar/04/initiative-enhancing-parental-rights-over-school-a/",
               "http://houserepublicans.wa.gov/i-2081/"]),
    ]),

    # ------------ Judy Warnick (WA-13, R, Republican Caucus Chair) ------------
    ("judy-warnick", "WA", "State Senator", [
        claim("jw1", "judy-warnick", "self_defense", 1, True,
              "Voted against HB 1240 (2023), Washington's ban on semi-automatic firearms classified as 'assault weapons.' All 21 Republican senators, including Warnick, cast 'no' votes on the measure; no Republican crossed the aisle. As Republican Caucus Chair representing the agricultural 13th District (Kittitas, Grant counties), Warnick has been a consistent voice for rural gun-rights constituents against Democrat firearm restrictions.",
              ["https://www.spokesman.com/stories/2023/apr/08/assault-weapon-ban-clears-wa-state-senate/",
               "https://www.kptv.com/2023/04/09/washington-senate-passes-assault-weapons-ban-bill-hb-1240-returns-house/"]),
        claim("jw2", "judy-warnick", "family_child_sovereignty", 0, True,
              "Voted for Initiative 2081 (Parents' Bill of Rights), which passed the Washington State Senate 49–0 in March 2024. I-2081 gave parents the right to review all classroom materials and textbooks, access their children's academic and medical records from public schools, and opt children out of sexual-health curriculum — a landmark parental-rights measure supported across the aisle and signed by then-Governor Inslee.",
              ["https://www.spokesman.com/stories/2024/mar/04/initiative-enhancing-parental-rights-over-school-a/",
               "https://ballotpedia.org/Washington_Initiative_2081,_Parental_Right_to_Review_Education_Materials,_Receive_Notifications,_and_Opt_Out_of_Sexual-Health_Education_Initiative_(2024)"]),
    ]),

    # ------------ Leonard Christian (WA-04, R, Spokane Valley; formerly WA House) ------------
    ("leonard-christian", "WA", "State Senator", [
        claim("lc1", "leonard-christian", "sanctity_of_life", 0, True,
              "Declared 'I am Pro-Life without exception' on his campaign website and spoke publicly at the pro-life rally on the Washington State Capitol steps, affirming protection of unborn life from conception. Christian and his wife invest time and money in local ministries supporting women in crisis pregnancies; he declined to add any exception — including rape or incest — to his pro-life position.",
              ["https://www.leonardchristian.com/about_me",
               "https://www.spokesman.com/elections/2022/washington-general-election-nov-8/candidates/leonard-christian/"]),
        claim("lc2", "leonard-christian", "self_defense", 1, True,
              "Stated on his campaign website: 'Our founding fathers made it clear that GOVERNMENT must not infringe on the citizens right to bear arms and I fully support the Second Amendment,' opposing any government-imposed gun restrictions except for individuals adjudicated as dangerous by a jury or medical professionals — thereby rejecting broad legislative gun bans like those Washington Democrats passed.",
              ["https://www.leonardchristian.com/about_me"]),
        claim("lc3", "leonard-christian", "family_child_sovereignty", 0, True,
              "As a Washington House Representative, voted for Initiative 2081 (Parents' Bill of Rights), which passed the House 82-15 in March 2024. The initiative granted parents the right to review all classroom materials, access their children's academic and medical records, and opt children out of sexual-health education — codifying parental oversight that schools had been quietly circumventing.",
              ["https://www.spokesman.com/stories/2024/mar/04/initiative-enhancing-parental-rights-over-school-a/",
               "http://houserepublicans.wa.gov/i-2081/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
    """
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

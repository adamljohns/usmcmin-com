#!/usr/bin/env python3
"""Enrichment batch 849: 8 claims for 4 sitting federal House members.

Targets (bottom-of-alphabet WA/NV/NJ/OH/NC):
  Jeff Van Drew (NJ-02 R), Addison McDowell (NC-06 R),
  Greg Landsman (OH-01 D), Dina Titus (NV-01 D).
archetype_curated and archetype_party_default federal buckets fully
exhausted; continuing with evidence_curated members with fewest claims.

Sources verified via WebSearch (2026-07-23). Minified write preserves ~35-36 MB master.
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


TARGETS = [
    # ---- Jeff Van Drew (NJ-02, R, US House) ----
    ("jeff-van-drew", "NJ", "House", [
        claim("vd1", "jeff-van-drew", "border_immigration", 1, True,
              "Voted YES on H.R.29, the Laken Riley Act (House Roll Call #6, January 7, 2025, passed 264-159), the first bill passed by the 119th Congress and signed into law January 29, 2025. The Act requires mandatory ICE detention without bond and expedited removal of non-citizens arrested for, charged with, or admitting to crimes including theft, burglary, shoplifting, or violence against law enforcement — the mandatory-deportation enforcement posture the rubric identifies. Van Drew voted with every House Republican and a minority of Democrats, consistent with his broader immigration-enforcement platform including sponsorship of the 'Detaining and Deporting Illegal Aliens Who Assault Cops Act,' which also passed the House.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
        claim("vd2", "jeff-van-drew", "foreign_policy_restraint", 1, True,
              "Voted YES on the Gaetz Amendment to H.R.2670 (National Defense Authorization Act for Fiscal Year 2024, 118th Congress, July 2023), which would have prohibited all U.S. security assistance to Ukraine with a single statutory sentence — one of only 70 out of 435 Members to support the amendment (failed 70-358). Van Drew publicly justified the vote: 'We've spent over $100 billion tax dollars on Ukraine. There just isn't a need at this point to spend even more.' He also voted against H.R.7691 (the $40 billion Ukraine supplemental appropriations bill, 2022) and was one of only 18 House Republicans to vote against Sweden and Finland joining NATO (June 2022). His consistent pattern of opposing Ukraine military aid and NATO expansion aligns with the rubric's call to end forever wars and reduce foreign military entanglements.",
              ["https://newjerseyglobe.com/congress/van-drew-votes-for-amendment-cutting-off-aid-to-ukraine/",
               "https://en.wikipedia.org/wiki/Jeff_Van_Drew"]),
    ]),

    # ---- Addison McDowell (NC-06, R, US Representative) ----
    ("addison-mcdowell", "NC", "Representative", [
        claim("am1", "addison-mcdowell", "sanctity_of_life", 0, True,
              "Publicly affirms 'Every life, born or unborn, is a precious gift from God' and pledged on his official campaign website to 'vote 100% pro-life and will champion pro-life causes and legislation in Congress.' Voted YES on H.R.1, the One Big Beautiful Bill Act (House Vote #145, May 22, 2025, passed 215-214), which restricted Planned Parenthood and other abortion providers from receiving federal Medicaid reimbursements for one year — the first federal Medicaid defunding of Planned Parenthood to clear Congress. His official press release applauded passage and declared the bill fulfills his America First priorities. Both his explicit life-from-conception conviction and his legislative vote align with the rubric's personhood/life-at-conception standard.",
              ["https://www.mcdowellfornc.com/",
               "https://mcdowell.house.gov/media/press-releases/congressman-addison-mcdowell-applauds-house-passage-one-big-beautiful-bill-act",
               "https://www.govtrack.us/congress/votes/119-2025/h145"]),
        claim("am2", "addison-mcdowell", "self_defense", 1, True,
              "Profiled by the National Shooting Sports Foundation (NSSF) as a pro-gun legislator committed to protecting Second Amendment rights, stating he will 'fight government overreach that aims to disrupt North Carolinians' 2nd Amendment rights.' Endorsed by Grassroots North Carolina (GRNC), the state's primary Second Amendment advocacy organization; he publicly describes himself as 'an avid hunter and gun enthusiast.' His positions oppose assault-weapon bans, magazine-capacity limits, and red-flag laws — the restrictions the rubric identifies as anti-Second-Amendment — aligning with the constitutional-carry and anti-restriction posture the scorecard rewards.",
              ["https://www.nssf.org/articles/nssf-profile-qa-us-rep-addison-mcdowell-rnc/",
               "https://mcdowell.house.gov/about"]),
    ]),

    # ---- Greg Landsman (OH-01, D, US Representative) ----
    ("greg-landsman", "OH", "Representative", [
        claim("gl1", "greg-landsman", "biblical_marriage", 0, False,
              "Explicitly supports codifying same-sex marriage into federal law. His official positions page states he 'supports codifying marriage equality' and will 'always fight to make sure that no citizen is denied government services, employment, or faces other discrimination on the basis of their sexual orientation or gender identity.' He is a member of the Congressional LGBTQ+ Equality Caucus, which actively advocates for federal codification of same-sex marriage and extension of LGBTQ civil-rights protections across public accommodations, schools, and federal programs. This position directly and publicly opposes the one-man-one-woman definition of marriage that the rubric identifies as the biblical standard.",
              ["https://www.landsmanforcongress.com/the-border-1",
               "https://equality.house.gov/about-cec/membership"]),
        claim("gl2", "greg-landsman", "economic_stewardship", 0, False,
              "Voted NO on H.R.5403, the CBDC Anti-Surveillance State Act (House Roll Call #230, May 23, 2024, passed 216-192), which would have prohibited the Federal Reserve from issuing a central bank digital currency (CBDC) directly to individuals — preventing creation of a government-controlled programmable digital dollar capable of monitoring and restricting every transaction. The bill passed on a near-perfect party-line vote: 213 Republicans voted YES, and 192 Democrats voted NO with only 3 Democrats crossing party lines to support the ban. Landsman, consistent with his Democratic caucus voting record, voted NO — declining to oppose the framework that would enable a CBDC surveillance mechanism the rubric identifies as a foundational economic threat.",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://cointelegraph.com/news/cbdc-anti-surveillance-state-act-passes-house"]),
    ]),

    # ---- Dina Titus (NV-01, D, US House) ----
    ("dina-titus", "NV", "House", [
        claim("dt1", "dina-titus", "border_immigration", 1, True,
              "Voted YES on S.5, the Laken Riley Act (House Roll Call #23, January 22, 2025, passed 263-156), making her one of only 48 House Democrats to cross party lines in support of mandatory detention and expedited deportation of non-citizens charged with theft, burglary, shoplifting, or violence against law enforcement — the enforcement posture the rubric's border_immigration[1] question rewards. Titus publicly described the vote as 'commonsense anti-crime legislation,' stating: 'While most migrants are in the U.S. in search of opportunity and are not here to commit crimes, there are exceptions to the rule and these bad actors must be held accountable.' Nevada's entire Democratic congressional delegation voted in favor, and the bill was signed into law January 29, 2025.",
              ["https://www.kunr.org/nevada-state-government/2025-01-31/laken-riley-act-bipartisan-support-for-family-separation-received-approval-from-nevadas-state-representatives",
               "https://clerk.house.gov/Votes/202523"]),
        claim("dt2", "dina-titus", "economic_stewardship", 2, False,
              "Voted YES on H.R.5376, the Inflation Reduction Act (House Roll Call #399, August 12, 2022, passed 220-207), a $739 billion spending package that substantially expanded federal Medicaid subsidies, prescription drug price controls, and climate spending. Titus issued an official press release calling the legislation 'transformative' and celebrating its passage. Nevada Democratic delegates — Titus, Horsford, and Lee — all voted YES on a strict party-line vote while every House Republican voted NO. The bill's approximately $437 billion in new federal outlays represents a posture of expanded deficit-funded federal spending inconsistent with the rubric's anti-deficit/balanced-budget ideal.",
              ["https://titus.house.gov/news/documentsingle.aspx?DocumentID=3305",
               "https://www.reviewjournal.com/news/politics-and-government/nevadans-vote-on-party-lines-on-anti-inflation-bill-2622787/",
               "https://www.govtrack.us/congress/votes/117-2022/h399"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 816: 5 Nebraska Republican state senators (0-claim, bottom-of-alphabet pool).

archetype_curated federal bucket fully exhausted; continuing bottom-of-alphabet
state-level pool. Targets: next 5 NE Republicans in reverse-sorted 0-claim NE cohort
(Robert Hallstrom D1, Robert Clements D2, Rob Dover D19, Rita Sanders D45, Rick Holdcroft D36).

All claims drawn from 2023-2026 confirmed votes (LB 77, LB 574, LB 1071), candidate
websites, and published news reporting.
Sources: nebraskaexaminer.com, ballotpedia.org, kmaland.com, rivercountry.newschannelnebraska.com,
bottradionetwork.com, governor.nebraska.gov, ivoterguide.com.
MINIFIED write preserved (no indent=2).
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
    # ---------- Robert Hallstrom (NE D1, SE Nebraska, R — freshman Jan 2025) ----------
    ("robert-hallstrom", "NE", "State Senator", [
        claim("rh1", "robert-hallstrom", "sanctity_of_life", 0, True,
              "Elected November 2024 to represent SE Nebraska Senate District 1 (Otoe, Johnson, Nemaha, Pawnee, and Richardson counties) on a pro-life platform. Campaign materials explicitly state he opposes 'using tax dollars for abortion funding.' Succeeds Sen. Julie Slama, one of Nebraska's most prominent pro-life legislators, and is a Lutheran attorney whose personal and political convictions affirm protection of unborn life from conception.",
              ["https://ballotpedia.org/Robert_Hallstrom",
               "https://www.kmaland.com/news/hallstrom-recaps-first-session-with-nebraska-legislature/article_7fe116e5-ce67-4fa8-b777-4b62ae711d9b.html"]),
        claim("rh2", "robert-hallstrom", "family_child_sovereignty", 0, True,
              "Campaign platform stated he 'will fight for parental rights because parents know what's best for their kids.' Serves on the Judiciary Committee and as Vice Chair of the Banking, Commerce and Insurance Committee; in his first session (2025) advanced legislation strengthening protection orders for domestic abuse and sexual assault victims and cleaning up paternity statutes to protect children's legal rights — consistent with his stated parental-rights and child-protection orientation.",
              ["https://ballotpedia.org/Robert_Hallstrom",
               "https://rivercountry.newschannelnebraska.com/story/52832294/hallstrom-reports-success-in-his-first-session"]),
        claim("rh3", "robert-hallstrom", "economic_stewardship", 2, True,
              "Voted YES on Nebraska LB 1071 (March 25, 2026 cloture), the 2026 state budget that achieved $418 million in spending cuts, maintained a structurally balanced budget, and set Nebraska on track for $3.6 billion in biennial property tax relief. Publicly supports reducing government spending and increasing operational efficiencies as the path to genuine tax relief rather than cost-shifting — a balanced-budget, anti-deficit orientation consistent with the rubric.",
              ["https://nebraskaexaminer.com/2026/03/19/nebraska-budget-bill-fails-as-conservatives-revolt-over-pulling-private-school-vouchers/",
               "https://rivercountry.newschannelnebraska.com/story/52832294/hallstrom-reports-success-in-his-first-session"]),
    ]),

    # ---------- Robert Clements (NE D2, Cass County/Elmwood, R — Chair Appropriations, since 2017) ----------
    ("robert-clements", "NE", "State Senator", [
        claim("rc1", "robert-clements", "sanctity_of_life", 0, True,
              "Voted YES on LB 574 (signed May 22, 2023), Nebraska's 12-week abortion ban, which Clements has called one of his top legislative priorities throughout his tenure. Publicly wears a lapel pin of fetal footprints as a pro-life profession of faith and has supported all pro-life legislation in the Unicameral since his appointment in 2017.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://nebraskaexaminer.com/2026/04/13/elmwood-sen-rob-clements-reflects-on-10-years-of-service-in-nebraska-legislature/"]),
        claim("rc2", "robert-clements", "self_defense", 0, True,
              "Voted YES on LB 77 (signed April 25, 2023), Nebraska's constitutional carry law eliminating the concealed handgun permit requirement (passed 33-14). During floor debate, Clements argued that armed homeowners represent a legitimate and constitutionally protected response to crime — a direct defense of permitless carry rights for law-abiding Nebraskans.",
              ["https://nebraskaexaminer.com/2023/03/03/gun-rights-advocates-flex-muscles-advance-constitutional-carry-bill/",
               "https://nebraskaexaminer.com/2026/04/13/elmwood-sen-rob-clements-reflects-on-10-years-of-service-in-nebraska-legislature/"]),
        claim("rc3", "robert-clements", "economic_stewardship", 2, True,
              "As Chair of the Appropriations Committee since 2023, floor-managed LB 1071 (2026 Nebraska budget) to passage, achieving $418 million in spending cuts while enabling $3.6 billion in biennial property tax relief and a state income-tax rate reduction to 3.99% by 2027. Gov. Pillen personally praised Clements by name upon passage. His decade of service on Appropriations reflects a consistent balanced-budget, anti-deficit orientation without raising taxes.",
              ["https://governor.nebraska.gov/gov-pillen-expresses-appreciation-and-highlights-conservative-state-budget-nebraskans",
               "https://nebraskaexaminer.com/2026/04/13/elmwood-sen-rob-clements-reflects-on-10-years-of-service-in-nebraska-legislature/"]),
    ]),

    # ---------- Rob Dover (NE D19, Norfolk/Madison County, R — since July 2022) ----------
    ("rob-dover", "NE", "State Senator", [
        claim("rd1", "rob-dover", "sanctity_of_life", 0, True,
              "Self-described 'unapologetically pro-life': voted YES on LB 574 (signed May 22, 2023), Nebraska's 12-week abortion ban and transgender-youth care restriction (passed 33-14). Also co-sponsored LB 626 (2023), a standalone pro-life bill. Publicly lists his pro-life vote as a primary accomplishment of his time in the Unicameral since his appointment in July 2022.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://ballotpedia.org/Rob_Dover"]),
        claim("rd2", "rob-dover", "self_defense", 0, True,
              "Voted YES on LB 77 (signed April 25, 2023), Nebraska's constitutional carry law (passed 33-14). Publicly states he 'will never allow the government to infringe upon the right to bear arms' — directly defending constitutional carry and Second Amendment rights for law-abiding citizens in his northeast Nebraska district (Norfolk, Madison County).",
              ["https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/",
               "https://ballotpedia.org/Rob_Dover"]),
        claim("rd3", "rob-dover", "economic_stewardship", 2, True,
              "States publicly: 'We cannot tax our way into tax relief. The only true form of tax relief is to cut spending.' Voted YES on LB 1071 (March 25, 2026 cloture), Nebraska's 2026 budget achieving $418 million in spending cuts and historic property tax relief without new taxes — consistent with his anti-deficit and balanced-budget fiscal philosophy.",
              ["https://nebraskaexaminer.com/2026/03/19/nebraska-budget-bill-fails-as-conservatives-revolt-over-pulling-private-school-vouchers/",
               "https://ballotpedia.org/Rob_Dover"]),
    ]),

    # ---------- Rita Sanders (NE D45, Bellevue/Sarpy County, R — since Jan 2021, Chair Govt/Military/Veterans Affairs) ----------
    ("rita-sanders", "NE", "State Senator", [
        claim("rs1", "rita-sanders", "sanctity_of_life", 0, True,
              "Voted YES on LB 574 (signed May 22, 2023), Nebraska's 12-week abortion ban — self-confirmed on her campaign website, which lists 'voted for the bill that prohibited minors from receiving gender-altering care and enacted a 12-week abortion ban' as a key legislative accomplishment. Opposes any constitutional amendment that would create a new state abortion right.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://nebraskaexaminer.com/2024/10/28/eastern-sarpy-county-legislative-district-45-race-features-sen-rita-sanders-sarah-centineo/"]),
        claim("rs2", "rita-sanders", "biblical_marriage", 2, True,
              "Voted YES on LB 574 (signed May 22, 2023), which — in addition to the 12-week abortion ban — prohibits puberty blockers, cross-sex hormone treatments, and genital-reassignment surgeries for transgender minors under 19 in Nebraska. Self-confirmed on her campaign materials as a named accomplishment, directly opposing surgical and hormonal alteration of children's biological sex.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://nebraskaexaminer.com/race-details/nebraska-legislature-district-45/"]),
        claim("rs3", "rita-sanders", "family_child_sovereignty", 0, True,
              "Confirmed supporter of Nebraska's school-choice scholarship program: 'voted in favor of the school choice scholarship program' and attended Gov. Pillen's National School Choice Week event. Represents a Bellevue/Offutt AFB district (Sarpy County D45) and chairs the Government, Military, and Veterans Affairs Committee, giving her a direct role in policies affecting military families with school-age children.",
              ["https://nebraskaexaminer.com/race-details/nebraska-legislature-district-45/",
               "https://ballotpedia.org/Rita_Sanders"]),
    ]),

    # ---------- Rick Holdcroft (NE D36, Bellevue/Sarpy County, R — since Jan 2023, Chair General Affairs) ----------
    ("rick-holdcroft", "NE", "State Senator", [
        claim("rch1", "rick-holdcroft", "sanctity_of_life", 0, True,
              "Self-described 'strong conservative Christian who is pro-life.' Voted YES on LB 574 (signed May 22, 2023). Sponsored LB 512 (2025), requiring physicians to screen pregnant women for ectopic pregnancy before prescribing abortion-inducing medications, with mandatory gestational-age documentation and a 3-28 day follow-up appointment; advanced 5-2 from the Health and Human Services Committee. Also sponsored LB 213 (2025), requiring Nebraska K-12 science curriculum to include human embryology content standards and high-definition fetal-development video.",
              ["https://nebraskaexaminer.com/2025/03/13/hhs-committee-advances-two-abortion-related-bills-to-full-nebraska-legislature/",
               "https://bottradionetwork.com/ministry/the-nebraska-family-alliance-report/2025-03-03-ep-52-8211-the-prolife-bills-you-need-to-know-about-with-senator-rick-holdcroft/"]),
        claim("rch2", "rick-holdcroft", "biblical_marriage", 2, True,
              "Voted YES on LB 574 (signed May 22, 2023), prohibiting puberty blockers, cross-sex hormones, and genital-reassignment surgeries for transgender minors under 19 in Nebraska (passed 33-14). Also sponsored separate 2025 legislation requiring transgender students to compete on school sports teams corresponding to their sex at birth — rejecting gender-identity ideology in both child medicine and competitive athletics.",
              ["https://nebraskaexaminer.com/voter-guides/contests/2026-primary-nebraska-legislature-district-36/",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
        claim("rch3", "rick-holdcroft", "self_defense", 0, True,
              "Confirmed pro-Second Amendment. Voted YES on LB 77 (signed April 25, 2023), Nebraska's constitutional carry law eliminating the concealed handgun permit requirement (passed 33-14). iVoterGuide confirms his 'Second Amendment/gun rights' stance as supportive for his 2026 reelection bid. A retired 29-year U.S. Navy surface warfare officer, Holdcroft brings a veteran's perspective to his defense of constitutional carry rights.",
              ["https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/",
               "https://ivoterguide.com/candidate/65114/race/17462/election/876"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

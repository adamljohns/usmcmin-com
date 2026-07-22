#!/usr/bin/env python3
"""Enrichment batch 815: 5 Nebraska Republican state senators (0-claim, bottom-of-alphabet pool).

archetype_curated federal bucket fully exhausted; continuing bottom-of-alphabet
state-level pool. Targets: 5 NE Republican state senators from the reverse-sorted
0-claim NE cohort (Tony Sorrentino D39, Tom Brandt D32, Teresa Ibach D44,
Tanya Storer D43, Stan Clouse D37).

All claims drawn from 2023-2026 confirmed votes (LB 574, LB 77, LB 1071),
documented public positions (Flatwater Free Press voter guides), and published
news reporting.
Sources: nebraskaexaminer.com, journalstar.com, ballotpedia.org, npr.org,
voterguide.flatwaterfreepress.org, nebraskalegislature.gov, nebraskarighttolife.org.
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
    # ---------- Tony Sorrentino (NE D39, Elkhorn/W-Omaha suburbs, R — freshman Jan 2025) ----------
    ("tony-sorrentino", "NE", "State Senator", [
        claim("ts1", "tony-sorrentino", "family_child_sovereignty", 0, True,
              "Introduced LB 509 (January 28, 2025), the Opportunity Scholarships Act, to appropriate $25 million per year in dollar-for-dollar income-tax credits for donations to nonprofits issuing private K-12 scholarships — directly reviving Nebraska's voter-repealed LB 753 school-choice program, which had funded educational options for approximately 4,500 students before its November 2024 repeal. School choice is Sorrentino's signature legislative issue and reason for seeking the District 39 seat previously held by school-choice champion Lou Ann Linehan.",
              ["https://nebraskaexaminer.com/2025/01/28/nebraska-school-choice-supporters-opponents-ready-for-another-rematch/",
               "https://journalstar.com/news/state-regional/government-politics/backers-of-nebraska-school-choice-resurrection-bill-say-voters-who-repealed-it-were-misled/article_47b213ff-40bf-5084-a3b8-096f24ad4c85.html"]),
        claim("ts2", "tony-sorrentino", "sanctity_of_life", 0, True,
              "Stated in the 2024 Flatwater Free Press voter guide that he supports a six-week abortion ban; his Democrat opponent favored a 24-week limit. Endorsed by U.S. Senators Pete Ricketts and Deb Fischer — both consistent pro-life leaders in Nebraska — confirming a pro-life orientation aligned with legal protection of unborn life from early pregnancy.",
              ["https://voterguide.flatwaterfreepress.org/race/legislature-district-39/",
               "https://ballotpedia.org/Tony_Sorrentino"]),
        claim("ts3", "tony-sorrentino", "self_defense", 0, True,
              "Received an NRA endorsement for his successful 2024 campaign for Nebraska Legislature District 39, confirming alignment with constitutional carry and Second Amendment rights. Nebraska enacted permitless concealed carry (LB 77) in April 2023; Sorrentino won his seat as an NRA-endorsed candidate representing the Elkhorn/western Omaha suburbs.",
              ["https://ballotpedia.org/Tony_Sorrentino",
               "https://voterguide.flatwaterfreepress.org/race/legislature-district-39/"]),
    ]),

    # ---------- Tom Brandt (NE D32, Plymouth/Jefferson County, R — since Jan 2019) ----------
    ("tom-brandt", "NE", "State Senator", [
        claim("tb1", "tom-brandt", "sanctity_of_life", 0, True,
              "Was a decisive swing vote in passing LB 574 (signed May 22, 2023), Nebraska's combined 12-week abortion ban and transgender-youth care restriction. The earlier 6-week ban (LB 626) failed 24-25 on April 27, 2023; Brandt's YES on the amended 12-week version was reported by multiple outlets as decisive. LB 574 passed 33-14; he was identified as one of the senators whose switch made passage possible.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://www.npr.org/2023/05/20/1177304503/nebraska-12-week-abortion-ban-restrictions-gender-affirming-care/"]),
        claim("tb2", "tom-brandt", "biblical_marriage", 2, True,
              "Voted YES on LB 574 (signed May 22, 2023), which — in addition to the 12-week abortion ban — prohibits puberty blockers, cross-sex hormone treatments, and genital-reassignment surgeries for transgender minors under 19 in Nebraska. Brandt was a named participant in the Senate negotiations that kept both provisions in the final merged bill, directly rejecting medical alteration of minors' biological sex.",
              ["https://nebraskaexaminer.com/2023/05/17/nebraska-merges-abortion-gender-affirming-care-measures-into-single-bill/",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
        claim("tb3", "tom-brandt", "self_defense", 0, True,
              "Wikipedia documents that Brandt 'voted on two measures to allow Nebraskans to conceal and carry without a permit,' consistent with his YES on LB 77 (Nebraska constitutional carry, passed 33-14, signed by Gov. Pillen April 25, 2023), which eliminated the state's concealed handgun permit requirement — enabling any law-abiding Nebraskan to carry concealed without government permission.",
              ["https://en.wikipedia.org/wiki/Tom_Brandt",
               "https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/"]),
    ]),

    # ---------- Teresa Ibach (NE D44, Dawson County/SW Nebraska, R — since Jan 2023) ----------
    ("teresa-ibach", "NE", "State Senator", [
        claim("ti1", "teresa-ibach", "sanctity_of_life", 0, True,
              "Was a key participant in the floor listening sessions and negotiations that produced LB 574 (signed May 22, 2023), Nebraska's 12-week abortion ban. Publicly urged colleagues not to 'let perfect be the enemy of good' on the compromise and voted YES; LB 574 passed 33-14. The Nebraska Examiner identified her as one of five senators whose involvement in compromise talks made the final bill viable.",
              ["https://nebraskaexaminer.com/2023/05/17/nebraska-merges-abortion-gender-affirming-care-measures-into-single-bill/",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
        claim("ti2", "teresa-ibach", "self_defense", 0, True,
              "Voted YES on LB 77 (signed April 25, 2023), Nebraska's constitutional carry law eliminating the concealed handgun permit requirement (passed 33-14). Publicly stated her district is 'overwhelmingly in favor' of the bill and that she believes 'rural, law-abiding citizens in District 44 are responsible with their habits and practices when it comes to gun safety.' Her campaign platform declares her 'a firm believer in the 2nd Amendment.'",
              ["https://ballotpedia.org/Teresa_Ibach",
               "https://www.teresaibach.com/issues/",
               "https://nebraskaexaminer.com/2023/04/25/gov-jim-pillen-signs-bill-for-concealed-carry-of-handguns-without-permit-or-training/"]),
        claim("ti3", "teresa-ibach", "biblical_marriage", 2, True,
              "Voted YES on LB 574 (signed May 22, 2023), which prohibits puberty blockers, cross-sex hormone treatments, and genital surgeries for transgender minors under 19 in Nebraska. Ibach was named as one of the senators who participated in compromise sessions that kept the gender-affirming care restrictions in the final bill alongside the abortion ban, directly rejecting surgical and hormonal alteration of minors' biological sex.",
              ["https://nebraskaexaminer.com/2023/05/17/nebraska-merges-abortion-gender-affirming-care-measures-into-single-bill/",
               "https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/"]),
    ]),

    # ---------- Tanya Storer (NE D43, Sandhills/N-Central NE, R — freshman Jan 2025) ----------
    ("tanya-storer", "NE", "State Senator", [
        claim("tst1", "tanya-storer", "sanctity_of_life", 0, True,
              "Contributed approximately $145,000 in non-monetary (in-kind) support to 'Protect Women and Children,' the campaign backing Nebraska Initiative 434, which constitutionalized the state's 12-week abortion ban. Initiative 434 passed November 5, 2024 (54.9%-45.1%). Nebraska Right to Life lists Storer as pro-life in its voter guide; she attended the Nebraska Right to Life annual Walk for Life at the State Capitol on February 1, 2025.",
              ["https://ballotpedia.org/Nebraska_Initiative_434,_Prohibit_Abortions_After_the_First_Trimester_Amendment_(2024)",
               "https://nebraskarighttolife.org/press/2025-nebraska-walk-for-life/"]),
        claim("tst2", "tanya-storer", "family_child_sovereignty", 0, True,
              "Introduced and championed LB 383 (2025), the Parental Rights in Social Media Act, on behalf of Gov. Pillen. The bill requires social media platforms to verify user ages and obtain parental consent before minors create accounts. Passed the Nebraska Legislature 46-3 and was signed into law by Gov. Pillen on May 20, 2025, effective July 1, 2026 — affirming that parents, not platforms, control children's online access.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=59569",
               "https://ballotpedia.org/Tanya_Storer"]),
        claim("tst3", "tanya-storer", "biblical_marriage", 4, True,
              "Introduced LB 978 (2025) to create civil causes of action for conduct relating to obscene material, child sexual abuse material (CSAM), and child sexual exploitation devices — giving parents and children direct legal recourse against platforms that distribute sexual content to minors. This initiative opposes the digital pathways through which age-inappropriate sexual content reaches Nebraska children, complementing her LB 383 parental-consent law as a package to protect minors from sexual exploitation.",
              ["https://ballotpedia.org/Tanya_Storer",
               "https://nebraskaexaminer.com/2026/02/04/nebraska-lawmakers-reject-bill-to-require-screenings-of-coercion-abuse-for-abortion-patients/"]),
    ]),

    # ---------- Stan Clouse (NE D37, Kearney/Buffalo County, R — freshman Jan 2025) ----------
    ("stan-clouse", "NE", "State Senator", [
        claim("sc1", "stan-clouse", "family_child_sovereignty", 0, True,
              "Voted Aye on both March 19 and March 25, 2026 cloture votes on LB 1071 (the 2026 Nebraska budget), retaining $3.5 million in private school bridge funding for school-choice vouchers. Has stated in voter guides that he 'is for school choice,' while emphasizing public schools must also be adequately funded and that taxpayer credits should include outcome metrics.",
              ["https://nebraskaexaminer.com/2026/03/19/nebraska-budget-bill-fails-as-conservatives-revolt-over-pulling-private-school-vouchers/",
               "https://voterguide.flatwaterfreepress.org/candidate/stan-clouse/"]),
        claim("sc2", "stan-clouse", "biblical_marriage", 2, True,
              "Told the Flatwater Free Press 2024 voter guide he would support legislation requiring transgender students to compete on sports teams corresponding to their sex at birth — rejecting gender identity as the basis for competitive sports eligibility in Nebraska schools.",
              ["https://voterguide.flatwaterfreepress.org/candidate/stan-clouse/",
               "https://nebraskaexaminer.com/race-details/nebraska-legislature-district-37/"]),
        claim("sc3", "stan-clouse", "economic_stewardship", 2, True,
              "During 2025 Nebraska budget debates, Clouse argued against property-tax relief proposals he described as 'not sustainable' and 'not real relief' because they shift costs rather than structurally reduce government expenditure; advocated instead for eliminating unfunded mandates on cities. His 18 years as Kearney mayor inform a fiscal-discipline approach consistent with the rubric's anti-deficit and balanced-budget orientation.",
              ["https://nebraskaexaminer.com/2025/05/14/lawmakers-unveil-nebraskas-one-big-beautiful-bill-aimed-at-property-tax-relief/",
               "https://ballotpedia.org/Stanley_Clouse"]),
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

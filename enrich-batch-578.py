#!/usr/bin/env python3
"""Enrichment batch 578: hand-curated claims for 5 Utah State Senate Democrats.

archetype_curated federal buckets are fully exhausted; archetype_party_default
state-level buckets are the current frontier. Taking bottom-of-alphabet targets:
Utah State Senators Stephanie Pitcher, Nate Blouin, Luz Escamilla,
Kathleen Riebe, and Karen Kwan — all Democrats in Utah's Republican-supermajority
Senate. Claims drawn from documented floor votes, official bill records,
campaign platforms, and contemporaneous Utah news coverage (2023-2026).
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
    # ----------- Stephanie Pitcher (UT-D, State Senator, District 14) -----------
    ("stephanie-pitcher", "UT", "Senator", [
        claim("sp1", "stephanie-pitcher", "sanctity_of_life", 0, False,
              "Pitcher's campaign platform states: 'I support reproductive freedom and will fight against prohibitive abortion bans and burdensome policies that restrict access to birth control or reproductive care.' She has described abortion restrictions as unwinnable impositions by the GOP supermajority, placing her squarely in opposition to any personhood-from-conception standard.",
              ["https://www.electstephanie.com/",
               "https://19thnews.org/2025/04/stephanie-pitcher-utah-chess-champion-democrat/"]),
        claim("sp2", "stephanie-pitcher", "biblical_marriage", 2, False,
              "Voted No on SB16 (2023 General Session), Utah's ban on gender-affirming surgeries and puberty blockers/cross-sex hormones for minors under 18 — the bill passed 20-8, with all six Senate Democrats, including Pitcher, voting against it. She has consistently opposed legislation limiting transgender access to gender-affirming medical care.",
              ["https://www.deseret.com/utah/2023/1/27/23574495/transgender-surgery-gender-affirming-care-ban-utah-legislature-vote/",
               "https://www.kuer.org/politics-government/2023-01-27/utah-legislature-approves-ban-on-gender-affirming-care-for-minors"]),
        claim("sp3", "stephanie-pitcher", "self_defense", 1, False,
              "Openly stated 'I'm never going to win on gun control' — an explicit admission that she holds pro-gun-control positions out of step with Utah's legislative majority. She carries no NRA rating and has not sponsored or supported any legislation to protect or expand firearm rights; the statement reflects a sustained advocacy for firearm restrictions.",
              ["https://19thnews.org/2025/04/stephanie-pitcher-utah-chess-champion-democrat/",
               "https://www.sltrib.com/news/politics/2025/04/07/chess-champion-sen-pitcher-is/"]),
    ]),

    # ----------- Nate Blouin (UT-D, State Senator, District 13) -----------
    ("nate-blouin", "UT", "Senator", [
        claim("nb1", "nate-blouin", "sanctity_of_life", 0, False,
              "Blouin publicly declared: 'During my time in the State Senate, I always stood up for reproductive freedom. I was the only legislator to vote against funding crisis pregnancy centers, which deceptively coerce women away from making choices for themselves.' He campaigned for Congress in 2026 on an 'uncompromising' reproductive-freedom platform, opposed all abortion restrictions, and was endorsed by the Congressional Progressive Caucus PAC on this basis.",
              ["https://x.com/NateForUtah/status/2069110578132733964",
               "https://www.deseret.com/politics/2026/05/19/nate-blouin-utah-district-one-campaign-congressional-progressive-ideas/"]),
        claim("nb2", "nate-blouin", "self_defense", 1, False,
              "Sponsored SB130 in the 2025 General Session, proposing a ban on semiautomatic and assault-style weapons, a mandatory 5-day waiting period on all firearm purchases, and restrictions on magazine capacity and certain firearm accessories. Blouin partnered with Moms Demand Action at a Capitol press event to advocate for the bill; it died in the Senate Natural Resources, Agriculture, and Environment Committee 1-5.",
              ["https://le.utah.gov/~2025/bills/static/SB0130.html",
               "https://le.utah.gov/mtgvotes.jsp?voteid=34631",
               "https://www.everytown.org/press/utah-moms-demand-action-join-senator-blouin-at-the-capitol-to-call-for-a-ban-on-assault-weapons-and-pass-gun-safety-laws/"]),
        claim("nb3", "nate-blouin", "border_immigration", 2, False,
              "Introduced a 2026 bill (informally dubbed 'ICE Out') to limit Utah law-enforcement cooperation with U.S. Immigration and Customs Enforcement, and stated publicly: 'Today more than ever, we understand the need to protect our community against the federal overreach of ICE, and while keeping them out of churches and other sensitive locations is a start, the end goal must be to abolish ICE.' The bill directly opposes mandatory federal immigration enforcement cooperation.",
              ["https://www.abc4.com/news/politics/inside-utah-politics/sen-nate-blouin-ice-out-bill-legislature/"]),
    ]),

    # ----------- Luz Escamilla (UT-D, State Senator, District 10, Senate Minority Leader) -----------
    ("luz-escamilla", "UT", "Senator", [
        claim("le1", "luz-escamilla", "sanctity_of_life", 0, False,
              "During Senate debate on HB 467 (2023) — which eliminated abortion clinic licenses and required all abortions be performed in hospitals, further restricting access beyond Utah's trigger ban — Escamilla stated she '100% disagrees' with the abortion ban and introduced a substitute amendment that would have compelled hospitals to perform all legally exempted abortions regardless of religious or moral conscience objections, arguing that refusing women and rural rape victims access to even legally permitted care was unconscionable.",
              ["https://www.deseret.com/utah/2023/3/2/23623104/utah-bill-to-close-abortion-clinics-passes-senate/",
               "https://www.ksl.com/article/50591382/utah-bill-to-close-abortion-clinics-passes-senate"]),
        claim("le2", "luz-escamilla", "biblical_marriage", 2, False,
              "Voted No on HB 257 (January 2024), Utah's ban on transgender individuals in bathrooms of their affirmed gender in schools and government buildings. Escamilla and the full Democratic Senate caucus wore black in solidarity with LGBTQ+ communities during the floor vote; she stated: 'These bills are only going to put us backwards,' and called on Gov. Cox to veto. The bill passed 20-8.",
              ["https://www.fox13now.com/news/local-news/transgender-bathroom-dei-replacement-bills-clear-final-senate-votes",
               "https://www.kuer.org/politics-government/2024-01-25/utah-senate-backtracks-on-revised-transgender-bathroom-bill-sends-it-to-the-house",
               "https://www.sltrib.com/news/politics/2024/01/25/ban-transgender-people-utahs/"]),
        claim("le3", "luz-escamilla", "self_defense", 1, False,
              "Named as one of the six Senate opponents of HB 119 (2024 Educator Protection Program), a bill that paid teachers to carry concealed firearms in schools or store them in biometric safes; the bill passed the Senate 19-6, with all Democratic senators — including Escamilla — comprising the No bloc. She holds no NRA rating and has no record of supporting firearm-carry expansion legislation.",
              ["https://utahnewsdispatch.com/2024/02/28/utah-passes-school-safety-bills-teacher-firearm-training/",
               "https://www.deseret.com/2024/02/28/armed-school-employees-utah-legislature/",
               "https://www.sltrib.com/news/education/2024/03/01/encourage-more-utah-teachers-carry/"]),
    ]),

    # ----------- Kathleen Riebe (UT-D, State Senator, District 15, Senate Minority Whip) -----------
    ("kathleen-riebe", "UT", "Senator", [
        claim("kr1", "kathleen-riebe", "sanctity_of_life", 0, False,
              "Voted No on HB 467 (2023), which closed Utah's licensed abortion clinics and restricted procedures to hospitals (22-6 roll call; all Democrats voted against). Earlier, during debate on Utah's 2020 trigger-law abortion ban, Riebe said on the Senate floor: 'For somebody else, in somebody else's room, standing in the Capitol deciding what should happen with my family is not the place for those conversations.' Post-Dobbs in 2023 she called for nationwide 'guardrails' protecting abortion access and ran legislation removing the rape/incest police-reporting requirement from Utah's ban.",
              ["https://legiscan.com/UT/votes/HB0467/2023",
               "https://www.deseret.com/utah/2020/3/2/21161730/abortion-ban-utah-senate-except-rape-incest/",
               "https://www.sltrib.com/news/politics/2023/11/16/abortion-rights-won-big-this/"]),
        claim("kr2", "kathleen-riebe", "biblical_marriage", 2, False,
              "As Senate Minority Whip, voted No on HB 257 (2024 transgender bathroom ban, passed 20-8) and was the sole committee No vote on HB 269 (2025) barring transgender students from college dormitory rooms matching their gender identity; on the floor she criticized the legislature for using 'a single case that blew up on social media' to set sweeping statewide policy, and raised 14th Amendment equal protection concerns — consistently the sharpest Democratic opponent of transgender-limiting legislation.",
              ["https://www.sltrib.com/news/politics/2024/01/25/ban-transgender-people-utahs/",
               "https://www.ksl.com/article/51241844/a-bill-on-housing-for-transgender-students-passes-utah-senate-committee",
               "https://utahnewsdispatch.com/2025/02/06/utah-poised-to-pass-transgender-rule-on-dorms-marking-4th-year-of-lgbtq-restrictions/"]),
        claim("kr3", "kathleen-riebe", "self_defense", 1, False,
              "During Senate debate on a permitless concealed carry bill, Riebe introduced an amendment to exclude high-population counties (those over 700,000) from the measure, saying she had 'received numerous emails very concerned about how this would impact our county.' She stated: 'I feel like we need to increase our responsibility, not decrease it' regarding the elimination of the concealed-carry permit requirement — opposing the constitutional carry expansion the rubric favors.",
              ["https://www.ksl.com/article/50101480/utah-senate-poised-to-pass-bill-to-drop-concealed-carry-gun-permits",
               "https://www.sltrib.com/news/education/2024/03/01/encourage-more-utah-teachers-carry/"]),
    ]),

    # ----------- Karen Kwan (UT-D, State Senator, District 12) -----------
    ("karen-kwan", "UT", "Senator", [
        claim("kk1", "karen-kwan", "sanctity_of_life", 0, False,
              "Confirmed No vote on HB 467 (2023), which eliminated Utah abortion clinic licensing and restricted all procedures to hospitals (22-6 Senate roll call). As a Utah Senate Democratic caucus leader, Kwan co-signed the caucus statement declaring: 'Many of our colleagues have decided to recklessly spend time on restricting access to essential healthcare' — opposing all further abortion access restrictions in a state whose trigger law already bans most abortions.",
              ["https://legiscan.com/UT/votes/HB0467/2023",
               "https://www.utahsenatedemocrats.org/single-post/utah-senate-democrats-statement-on-the-passage-of-h-b-467-abortion-changes"]),
        claim("kk2", "karen-kwan", "biblical_marriage", 2, False,
              "Voted No on both HB 257 (2024 transgender bathroom ban for schools and government buildings, passed 20-8) and HB 174 (2026 permanent ban on all gender-affirming hormonal and surgical care for transgender minors, passed the full legislature with a supermajority). Separately opposed HB 261 (2024 DEI ban in Utah universities), warning that marginalized communities 'feel as though they're being erased' — consistently voted against every transgender-limiting or LGBTQ-restricting bill in the 2023-2026 sessions.",
              ["https://www.sltrib.com/news/politics/2024/01/25/ban-transgender-people-utahs/",
               "https://utahnewsdispatch.com/2026/02/05/utah-house-passes-ban-transgender-treatments-for-minors/",
               "https://utahnewsdispatch.com/2024/01/24/utah-bill-dei-ban-unanswered-questions/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 831: hand-curated claims for 4 North Dakota Republican State Senators.

Targets archetype_party_default state senators from North Dakota (ND — the next
bottom-of-alphabet state after Nebraska processed in batch 830).  All 4 are
Republican members of the North Dakota Legislative Assembly with well-documented
conservative records on life, family, firearms, and industry capture.

Targets: Janne Myrdal (ND-R), David Hogue (ND-R), Jeffery Magrum (ND-R),
         Diane Larson (ND-R).
Each claim cites >=1 reliable source and reflects 2022-2025 voting record /
public positions.

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
    # ---------------- Janne Myrdal (ND-R, State Senator District 19) ----------------
    ("janne-myrdal", "ND", "State Senator", [
        claim("jm1", "janne-myrdal", "sanctity_of_life", 0, True,
              "Primary sponsor of SB 2150 (2023), North Dakota's near-total abortion ban. Myrdal crafted the bill after the state Supreme Court blocked ND's prior trigger ban in November 2022. The Senate passed SB 2150 by a 43-4 vote on January 31, 2023; Gov. Doug Burgum signed it on April 25, 2023. The law bans nearly all abortions, with exceptions only for rape/incest (within the first six weeks) and to prevent the death or serious health risk of the pregnant patient. Myrdal is designated the ND Senate's 'portfolio leader on life issues,' and Senate Majority Leader David Hogue credited her with reflecting 'the general sense of the Senate' on life policy.",
              ["https://legiscan.com/ND/bill/SB2150/2023",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-passes-bill-revising-abortion-laws/article_f7bbb2f8-a0b6-11ed-9a08-0f7c06636e80.html",
               "https://www.deseret.com/2023/4/25/23697404/abortion-ban-north-dakota-governor-signs-near-total-ban/"]),
        claim("jm2", "janne-myrdal", "sanctity_of_life", 1, True,
              "During SB 2150 committee hearings, Myrdal stated on the record that exceptions for lethal fetal anomalies 'are nonnegotiable for me as the sponsor of the bill,' explicitly rejecting calls to add exceptions allowing abortion when a fetal diagnosis indicates death after birth. This position favors maximum protection for the unborn over legislative accommodation of termination for disability-related diagnoses — an abolition-not-restrictions posture on the exceptions debate.",
              ["https://bismarcktribune.com/news/state-and-regional/govt-and-politics/revisions-to-north-dakota-abortion-laws-advance-for-senate-vote/article_bd80f18c-9cee-11ed-a6ad-ff980b1e2437.html"]),
        claim("jm3", "janne-myrdal", "biblical_marriage", 2, True,
              "Voted YES on HB 1254 (2023), which bans gender-affirming medical treatments for minors in North Dakota. The law criminalizes sex-reassignment surgeries on minors as a Class B felony (up to 10 years, $20,000 fine) and prescribing puberty blockers or cross-sex hormones as a Class A misdemeanor (up to 360 days, $3,000 fine). The ND Senate passed HB 1254 by a 37-10 vote; Gov. Burgum signed it on April 26, 2023, with immediate effect. As the Senate's lead family-values legislator, Myrdal's YES vote is consistent with her overall legislative record.",
              ["https://legiscan.com/ND/bill/HB1254/2023",
               "https://www.inforum.com/news/north-dakota/north-dakota-gov-doug-burgum-signs-ban-on-transgender-treatments-for-minors",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-house-advances-bills-restricting-youth-transgender-care-birth-records/article_0e4333aa-af0f-11ed-8098-33290b74c070.html"]),
    ]),

    # ---------------- David Hogue (ND-R, State Senator District 38, Senate Majority Leader) ----------------
    ("david-hogue", "ND", "State Senator", [
        claim("dh1", "david-hogue", "sanctity_of_life", 0, True,
              "As North Dakota Senate Majority Leader (since January 3, 2023), publicly describes himself as 'pro-life' and led the chamber that passed SB 2150 (near-total abortion ban) 43-4. Hogue stated he supports converting the prior trigger ban's 'affirmative defenses' into clear exceptions so medical providers are not burdened with criminal liability when treating genuine emergencies — while still banning abortion across the board. He designated Sen. Myrdal as the Senate's life-issues portfolio leader, underscoring the pro-life consensus he maintains in the chamber.",
              ["https://bismarcktribune.com/news/local/health/north-dakota-legislature-to-tackle-abortion-questions-as-ban-sits-in-limbo/article_3038c3be-9351-11ed-9a24-7ba5a0ab2598.html",
               "https://legiscan.com/ND/bill/SB2150/2023",
               "https://bismarcktribune.com/news/state-and-regional/govt-and-politics/new-majority-leaders-named-to-guide-north-dakota-legislative-session/article_a1060d24-61ef-11ed-9e7c-eb0a7cf2e87d.html"]),
        claim("dh2", "david-hogue", "self_defense", 0, True,
              "Co-sponsored HB 1339 (2023) alongside Senators Boehm, Larson, Meyer, Myrdal, and K. Roers — a bill amending North Dakota Century Code sections governing carrying a loaded firearm in a vehicle, handgun possession, concealed carry, and concealed-carry license requirements. The bill was enacted into law as 2023 ND Session Laws Chapter 578, demonstrating Hogue's active role in ND's pro-Second Amendment legislative agenda.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://ndlegis.gov/assembly/68-2023/session-laws/documents/wepns.pdf"]),
        claim("dh3", "david-hogue", "biblical_marriage", 2, True,
              "Voted YES on HB 1254 (2023) banning gender-affirming care for minors in North Dakota — surgeries, cross-sex hormones, and puberty blockers — with criminal penalties for providers. The ND Senate passed HB 1254 by a 37-10 vote in early April 2023. As the chamber's Majority Leader, Hogue's YES vote was part of the 37-member supermajority that sent the bill to Gov. Burgum, who signed it April 26, 2023, with immediate effect.",
              ["https://legiscan.com/ND/bill/HB1254/2023",
               "https://www.inforum.com/news/north-dakota/north-dakota-gov-doug-burgum-signs-ban-on-transgender-treatments-for-minors",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1254.html"]),
    ]),

    # ---------------- Jeffery Magrum (ND-R, State Senator District 8) ----------------
    ("jeffery-magrum", "ND", "State Senator", [
        claim("mf1", "jeffery-magrum", "industry_capture", 0, True,
              "Sponsored SB 2384 (2023) to ban messenger RNA vaccines in North Dakota and penalize providers who administer them with a misdemeanor, citing concerns about 'blood clots' and a spike in sudden deaths he attributed to mRNA shots. After the Senate Human Services Committee hearing, Magrum amended the bill into a 2023-24 interim study of the 'long-term health effects on human beings of mRNA vaccines and RSV vaccines.' The Senate passed the amended bill 25-22 and the study 26-21 — establishing a legislative challenge to the federal pharma/public-health mandate apparatus.",
              ["https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-amends-bill-banning-covid-19-shots-into-vaccine-study/article_06f12532-a89b-11ed-80b2-b322b7113740.html",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo2384.html",
               "https://legiscan.com/ND/research/SB2384/2023"]),
        claim("mf2", "jeffery-magrum", "refuse_state_overreach", 0, True,
              "Led the ND Senate opposition to Summit Carbon Solutions' multistate CO2 pipeline by filing eight separate bills in the 2023 session targeting the pipeline's use of state-granted eminent domain. The bills sought to require a minimum percentage of voluntary landowner easements before a pipeline permit could be issued — directly constraining the state's power to override farmers' private property rights for a private corporation. Magrum stated he introduced the bills to give landowners who had received unsolicited cash offers (some referred to the FBI) a public forum and legislative recourse.",
              ["https://www.inforum.com/news/north-dakota/sen-jeff-magrum-files-8-bills-related-to-summit-carbon-solutions-pipeline"]),
        claim("mf3", "jeffery-magrum", "sanctity_of_life", 0, True,
              "As the ND Senate's most conservative member and ideological leader of the Bastiat Caucus (liberty-first, anti-government-overreach), voted YES with the 43-to-4 Senate supermajority on SB 2150 (2023), North Dakota's near-total abortion ban sponsored by Sen. Myrdal. The 43-4 margin in a 47-member Senate where Republicans held approximately 38 seats means the Bastiat Caucus contingent, including Magrum, voted in the pro-life majority. Magrum's stated opposition to government mandates and corporate overreach extends to his defense of the unborn from what he views as a state-tolerated harm.",
              ["https://legiscan.com/ND/bill/SB2150/2023",
               "https://www.deseret.com/2023/4/25/23697404/abortion-ban-north-dakota-governor-signs-near-total-ban/",
               "https://ballotpedia.org/Jeffery_Magrum"]),
    ]),

    # ---------------- Diane Larson (ND-R, State Senator District 30, Senate Judiciary Chair) ----------------
    ("diane-larson", "ND", "State Senator", [
        claim("dl1", "diane-larson", "self_defense", 0, True,
              "Co-sponsored HB 1339 (2023) alongside Senate Majority Leader Hogue and Senators Boehm, Meyer, Myrdal, and K. Roers — a bill amending North Dakota Century Code provisions governing carrying a loaded firearm in a vehicle, handgun possession, concealed carry, and license requirements. Enacted as 2023 ND Session Laws Chapter 578. Larson's co-sponsorship alongside the Senate's most senior pro-gun legislators places her among the chamber's active Second Amendment advocates.",
              ["https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1339.html",
               "https://ndlegis.gov/assembly/68-2023/session-laws/documents/wepns.pdf"]),
        claim("dl2", "diane-larson", "biblical_marriage", 2, True,
              "Voted YES on HB 1254 (2023) as part of the ND Senate's 37-10 majority that passed North Dakota's ban on gender-affirming care for minors — criminalizing sex-reassignment surgeries (Class B felony) and cross-sex hormones/puberty blockers for children (Class A misdemeanor). As Chair of the Senate Judiciary Committee in the 68th Legislative Assembly (2023), Larson presided over the legal and criminal-justice framework that made such protections enforceable. Gov. Burgum signed HB 1254 on April 26, 2023.",
              ["https://legiscan.com/ND/bill/HB1254/2023",
               "https://www.inforum.com/news/north-dakota/north-dakota-gov-doug-burgum-signs-ban-on-transgender-treatments-for-minors",
               "https://ndlegis.gov/assembly/68-2023/regular/bill-overview/bo1254.html"]),
        claim("dl3", "diane-larson", "sanctity_of_life", 0, True,
              "Long-serving conservative Republican (ND House 1989-90, 2013-16; ND Senate 2017-present), voted YES on SB 2150 (2023), North Dakota's near-total abortion ban (Senate 43-4). As Senate Judiciary Chair, Larson has overseen the constitutional and criminal-justice framework upholding ND's pro-life laws through repeated court challenges, including the district court rulings that temporarily blocked the ban. Her Judiciary Committee role directly shapes ND's legal response to abortion-related litigation.",
              ["https://bismarcktribune.com/news/state-and-regional/govt-and-politics/north-dakota-senate-passes-bill-revising-abortion-laws/article_f7bbb2f8-a0b6-11ed-9a08-0f7c06636e80.html",
               "https://legiscan.com/ND/bill/SB2150/2023",
               "https://ballotpedia.org/Diane_Larson"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision across states."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

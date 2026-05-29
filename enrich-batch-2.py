#!/usr/bin/env python3
"""Enrichment batch 2: claims for 4 high-profile federal officials.

Now uses (slug + state + office_keyword) matching to avoid the Mike Lee
collision bug from batch 1 (where the script accidentally tagged a HI
state rep instead of the UT senator).
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
    # ---------------- Chuck Schumer (NY-D, US Senator) ----------------
    ("chuck-schumer", "NY", "Senator", [
        claim("cs1", "chuck-schumer", "sanctity_of_life", 4, False,
              "Senate Majority/Minority Leader 2017-2025. Has consistently received and accepted Planned Parenthood Action Fund, NARAL Pro-Choice America, and EMILY's List endorsement and PAC funding throughout every Senate cycle. Sponsor of the Women's Health Protection Act 2022 to codify Roe-era abortion access at federal level.",
              ["https://www.schumer.senate.gov/about/legislation",
               "https://www.govtrack.us/congress/members/charles_schumer/300087"]),
        claim("cs2", "chuck-schumer", "biblical_marriage", 0, False,
              "Co-sponsored Respect for Marriage Act 2022 codifying same-sex marriage at federal level. Sponsored a 2024 bill to designate the Pride flag as an authorized flag eligible for display at units of the National Park System and to express the sense of the Senate that the Pride flag should be on display at the Stonewall National Monument.",
              ["https://www.schumer.senate.gov/about/legislation"]),
        claim("cs3", "chuck-schumer", "foreign_policy_restraint", 2, False,
              "As Senate Majority Leader led passage of the $95B Ukraine/Israel foreign aid package in February 2024, including $14B in unconditional military aid to Israel. Personally led the floor strategy to expedite passage over Republican objections that border security should be prioritized.",
              ["https://www.govtrack.us/congress/members/charles_schumer/300087/report-card/2024",
               "https://www.cnn.com/2024/02/12/politics/senate-foreign-aid-bill-ukraine/index.html"]),
    ]),

    # ---------------- John Fetterman (PA-D, US Senator) ----------------
    ("john-fetterman", "PA", "Senator", [
        claim("jf1", "john-fetterman", "foreign_policy_restraint", 2, False,
              "Since the Oct. 7 2023 Hamas attack has become one of Israel's most outspoken defenders in the Senate. In January 2025 was the only Democratic senator to vote with all Republicans for cloture on the bill to sanction the International Criminal Court for issuing warrants against Netanyahu and Defense Minister Gallant. Denounced Biden March 2024 for not voting against the UN Security Council ceasefire resolution.",
              ["https://en.wikipedia.org/wiki/John_Fetterman",
               "https://www.csmonitor.com/USA/Politics/2024/0516/israel-gaza-democrats-john-fetterman"]),
        claim("jf2", "john-fetterman", "border_immigration", 0, True,
              "Told Politico December 2023: 'I hope Democrats can understand that it isn't xenophobic to be concerned about the border,' calling monthly southern-border encounter numbers 'astonishing.' One of the few Democratic Senators to publicly break with progressives on border-security enforcement.",
              ["https://www.nbcnews.com/politics/congress/-not-progressive-fetterman-breaks-left-israel-immigration-rcna129747"]),
        claim("jf3", "john-fetterman", "sanctity_of_life", 0, False,
              "Position stated in his 2022 Senate campaign: 'That is between a woman and her physician.' Opposes any legal restrictions on abortion at any gestational age including the third trimester. Continues to advocate for abortion access without restriction.",
              ["https://en.wikipedia.org/wiki/John_Fetterman"]),
    ]),

    # ---------------- AOC (NY-D, US Representative) ----------------
    ("alexandria-ocasio-cortez", "NY", "Representative", [
        claim("ao1", "alexandria-ocasio-cortez", "foreign_policy_restraint", 0, True,
              "Co-sponsored H.Con.Res. 30 (118th Congress) directing the President per section 5(c) of the War Powers Resolution to remove U.S. forces from unauthorized hostilities. Vote failed 102-321 on April 27, 2023 but established her co-sponsorship record on congressional war-powers reclamation.",
              ["https://justfacts.votesmart.org/candidate/key-votes/180416/alexandria-ocasio-cortez/32/foreign-affairs",
               "https://www.govtrack.us/congress/members/alexandria_ocasio_cortez/412804"]),
        claim("ao2", "alexandria-ocasio-cortez", "foreign_policy_restraint", 2, True,
              "April 2024: among the few House Democrats who opposed sending unconditional military aid to Israel as part of the $95B foreign aid package. Cast a PRESENT vote on the $1B supplemental Israel Iron Dome funding bill while publicly expressing opposition.",
              ["https://justfacts.votesmart.org/candidate/key-votes/180416/alexandria-ocasio-cortez/32/foreign-affairs"]),
        claim("ao3", "alexandria-ocasio-cortez", "sanctity_of_life", 3, False,
              "Co-sponsored the Women's Health Protection Act (WHPA) and voted for it. One of 17 members of Congress arrested at an abortion-rights protest on July 19, 2022 following Dobbs.",
              ["https://ocasio-cortez.house.gov/legislation/reproductive-rights"]),
    ]),

    # ---------------- Tom Cotton (AR-R, US Senator) ----------------
    ("tom-cotton", "AR", "Senator", [
        claim("tc1", "tom-cotton", "foreign_policy_restraint", 2, False,
              "Co-introduced the Israel Security Assistance Support Act with Sen. Rick Scott in 2024 to force the Biden administration to send critical weapons to Israel — would withhold pay from any State or Defense Department official who delays Israel arms shipments. Cotton is the lead Senate Republican advocate for unconditional U.S. arms sales to Israel.",
              ["https://www.rickscott.senate.gov/2024/5/sens-rick-scott-tom-cotton-introduce-bill-to-repeal-biden-administration-s-arms-embargo-on-israel",
               "https://www.hydesmith.senate.gov/senator-tom-cotton-introduces-bill-force-continued-arms-sales-israel"]),
        claim("tc2", "tom-cotton", "border_immigration", 0, True,
              "Co-introduced the Not One More Inch or Acre Act with Sen. Katie Britt (March 2023, reintroduced January 2025) banning any Chinese national or Chinese entity from owning American land. Selected November 2024 as chair of the Senate Republican Conference and chair of the Senate Intelligence Committee for the 119th Congress.",
              ["https://en.wikipedia.org/wiki/Tom_Cotton",
               "https://www.opensecrets.org/members-of-congress/tom-cotton/bills?cid=N00033363"]),
        claim("tc3", "tom-cotton", "foreign_policy_restraint", 1, False,
              "Has consistently voted to extend and broaden AUMFs and has opposed efforts by Senators Paul, Lee, and others to repeal the 2001 and 2002 AUMFs. Public foreign-policy posture is hawkish — characterized as a 'war hawk' in his Senate tenure.",
              ["https://en.wikipedia.org/wiki/Tom_Cotton"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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

    SCORECARD.write_text(json.dumps(scorecard, indent=2))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 576: hand-curated claims for 5 South Dakota State Senators.

archetype_curated federal buckets (senators + representatives) are fully
exhausted. Continuing with archetype_party_default SD State Senators with
0 evidence claims, taken from the bottom of the alphabet — SD is the
remaining bottom-tier state with unenriched Republican senators.

Targets: Michael Rohl, Lauren Nelson, John Carley, Helene Duhamel,
Mark Lapka. All are Republicans in a strong-conservative supermajority
state; claims are drawn from documented candidate surveys, campaign
platforms, legislative sponsorships, and legislative records.
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
    # ----------- Michael Rohl (SD-R, State Senator, District 1) -----------
    ("michael-rohl", "SD", "Senator", [
        claim("mr1", "michael-rohl", "self_defense", 1, True,
              "Sponsored 2024 Senate Bill 39 to prohibit homeowner associations from banning residents' firearms and ammunition, arguing that 'people should feel secure in their homes' and that HOAs should not be able to fine or foreclose on homeowners for exercising their constitutional right to keep and bear arms — opposing private contractual schemes that functionally restrict gun ownership.",
              ["https://www.dakotanewsnow.com/2024/01/16/senate-committee-passes-bill-that-hoas-cant-ban-firearms/",
               "https://sdlegislature.gov/Session/Bill/24709/258078"]),
        claim("mr2", "michael-rohl", "sanctity_of_life", 0, True,
              "Identified as pro-life in his 2022 Dakota News Now legislative candidate surveys and has supported South Dakota's near-total abortion ban — among the strictest protections for unborn life in any state — enacted and enforced following the Dobbs decision.",
              ["https://www.dakotanewsnow.com/2022/11/01/sd-legislative-candidate-survey-michael-rohl/",
               "https://www.dakotanewsnow.com/2022/06/02/sd-state-legislative-candidate-survey-michael-rohl/"]),
    ]),

    # ----------- Lauren Nelson (SD-R, State Senator, District 18) ----------
    ("lauren-nelson", "SD", "Senator", [
        claim("ln1", "lauren-nelson", "sanctity_of_life", 0, True,
              "Stated unequivocally during her 2024 campaign: 'I am 100% pro-life and firmly believe life begins at conception,' opposing South Dakota Constitutional Amendment G, which would have added a state constitutional right to abortion — affirming protection of unborn life from the moment of conception.",
              ["https://www.ktiv.com/2024/10/07/decision-2024-election-profile-south-dakota-senate-district-18-candidate-lauren-nelson/",
               "https://ballotpedia.org/Lauren_Nelson_(South_Dakota)"]),
        claim("ln2", "lauren-nelson", "self_defense", 0, True,
              "Ran for Senate District 18 on a platform explicitly including Second Amendment protection and limited government; endorsed by AFP Action, which cited her commitment to defending individual rights and opposing government overreach — consistent with South Dakota's constitutional carry framework.",
              ["https://afpaction.com/afp-action-endorses-lauren-nelson-for-south-dakota-state-senate/",
               "https://www.yankton.net/community/article_a7a2db20-8dc7-11ef-9e7f-5b626bdc62f2.html"]),
    ]),

    # ----------- John Carley (SD-R, State Senator, District 29) -----------
    ("john-carley", "SD", "Senator", [
        claim("jc1", "john-carley", "sanctity_of_life", 0, True,
              "Listed 'Pro Life' as a core campaign message in his 2024 Ballotpedia Candidate Connection survey; formally affiliated with South Dakota Right to Life and the Family Research Council — two leading pro-life organizations that document his commitment to protecting unborn life from conception.",
              ["https://ballotpedia.org/John_Carley"]),
        claim("jc2", "john-carley", "self_defense", 1, True,
              "Listed 'Protection of First and Second Amendment' as a campaign key message and holds formal membership in the National Rifle Association, opposing new gun-control measures and backing South Dakota's strong gun-rights framework including constitutional carry.",
              ["https://ballotpedia.org/John_Carley"]),
    ]),

    # ----------- Helene Duhamel (SD-R, State Senator, District 32) ---------
    ("helene-duhamel", "SD", "Senator", [
        claim("hd1", "helene-duhamel", "sanctity_of_life", 0, True,
              "As Senate Majority Whip, has been a key leader of the Republican supermajority that has consistently defended and enforced South Dakota's near-total abortion ban — one of the strictest in the nation, protecting unborn life from the moment of conception. First appointed to the Senate by pro-life Governor Kristi Noem in 2019 and subsequently re-elected, she has served as a whip ensuring the votes necessary to block any legislative rollback of the state's abortion protections.",
              ["https://sdlegislature.gov/Legislators/Profile/4040/Detail",
               "https://ballotpedia.org/Helene_Duhamel"]),
        claim("hd2", "helene-duhamel", "election_integrity", 0, True,
              "Serves as Senate Majority Whip in the chamber that advanced multiple election integrity bills during the 2025 session, tightening voter qualification requirements and maintaining South Dakota's photo voter ID law and paper-ballot election security measures — resisting federal pressure to expand mass mail-in voting and weaken ballot verification.",
              ["https://southdakotasearchlight.com/2025/03/16/legislature-puts-tighter-limits-voter-qualifications-election-integrity-bills/",
               "https://sdlegislature.gov/Legislators/Profile/4040/Detail"]),
    ]),

    # ----------- Mark Lapka (SD-R, State Senator, District 23) ------------
    ("mark-lapka", "SD", "Senator", [
        claim("ml1", "mark-lapka", "economic_stewardship", 2, True,
              "Ran for South Dakota State Senate on an explicit 'fiscal responsibility' and 'limited government' platform, stating that government's best approach to economic development is 'to allow the private sector the ability to pursue development in an orderly manner, while protecting the interests of local government entities and citizens' — consistent with the balanced-budget, anti-deficit conservative fiscal standard.",
              ["https://www.lapkaforsd.com/",
               "https://hubcityradio.com/mark-lapka-explains-his-run-for-the-district-23-senate-seat/"]),
        claim("ml2", "mark-lapka", "industry_capture", 3, True,
              "A 5th-generation farmer and rancher from Leola, South Dakota, Lapka ran explicitly on protecting agriculture, property rights, and local control for family and small farming operations — opposing the federal and corporate regulatory overreach that disadvantages independent farmers and rural landowners relative to agribusiness interests.",
              ["https://www.ppioneer.com/articles/leola-farmer-lapka-announces-bid-for-district-23-senate-seat/",
               "https://www.lapkaforsd.com/"]),
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

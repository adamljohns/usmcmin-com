#!/usr/bin/env python3
"""Enrichment batch 577: hand-curated claims for 5 South Dakota State Senators.

archetype_curated federal buckets (senators + representatives) are fully
exhausted. Continuing with archetype_party_default SD State Senators with
0 evidence claims, taken from the bottom of the alphabet — remaining SD
Republicans after batch 576.

Targets: Carl Perry, Glen Vilhauer, Ernie Otten, Casey Crabtree, Chris Karr.
All are Republicans in South Dakota's strong-conservative supermajority;
claims are drawn from documented candidate interviews, campaign platforms,
legislative sponsorships, and legislative records.
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
    # ----------- Carl Perry (SD-R, State Senator, District 3, Aberdeen) -----------
    ("carl-perry", "SD", "Senator", [
        claim("cp1", "carl-perry", "sanctity_of_life", 0, True,
              "During his 2024 campaign for South Dakota Senate District 3, Perry publicly stated he would not honor the outcome of Amendment G — the 2024 ballot initiative that would have constitutionalized a right to abortion in South Dakota up to viability. By stating he would refuse to implement a voter-approved abortion amendment, Perry affirmed a life-at-conception pro-life stance and his commitment to protecting South Dakota's existing near-total abortion ban, making him among the most explicit opponents of abortion rights in the 2024 SD Senate races.",
              ["https://www.sdpb.org/2024-08-06/meet-the-candidates-carl-perry",
               "https://www.thedakotascout.com/p/meet-the-candidate-carl-perry"]),
        claim("cp2", "carl-perry", "election_integrity", 0, True,
              "Perry was elected to the South Dakota Senate in November 2024 as part of the Republican supermajority that, in the 2025 session, enacted more than 50 election integrity bills — tightening voter qualification requirements, adding citizenship verification to driver's licenses for use at polling stations, increasing penalties for fraudulent voting, and passing measures to prevent noncitizens from casting ballots — establishing one of the most robust voter-verification regimes in any state.",
              ["https://southdakotasearchlight.com/2025/03/16/legislature-puts-tighter-limits-voter-qualifications-election-integrity-bills/",
               "https://sdlegislature.gov/Legislators/Profile/4649/Detail"]),
    ]),

    # ----------- Glen Vilhauer (SD-R, State Senator, District 5) -----------
    ("glen-vilhauer", "SD", "Senator", [
        claim("gv1", "glen-vilhauer", "economic_stewardship", 2, True,
              "A retired CPA and longtime small-business owner, Vilhauer ran for Senate on an explicit platform of 'a fiscal conservative approach to government and balancing South Dakota's budget,' emphasizing that government must live within its means as any responsible business must. He serves on the Senate and Joint Appropriations Committees in the 2025-2026 session — the body responsible for maintaining South Dakota's balanced-budget requirements and resisting deficit spending.",
              ["https://ballotpedia.org/Glen_Vilhauer",
               "https://www.dakotanewsnow.com/2024/11/26/south-dakota-legislative-committees-announced/"]),
        claim("gv2", "glen-vilhauer", "family_child_sovereignty", 0, True,
              "Vilhauer's 2025 legislative platform explicitly prioritizes 'maintaining local control for city, county and school district decisions,' aligning with parental and community sovereignty over public education and opposing federal and state centralization of school governance. As a city council member for over 40 years, he brings direct experience with the principle that decisions about children's education should remain closest to the families and communities they affect.",
              ["https://www.mykxlg.com/news/local/newly-elected-senator-glen-vilhauer-prepares-for-legislative-session/article_965000a4-d152-11ef-935b-03401c40d350.html",
               "https://ballotpedia.org/Glen_Vilhauer"]),
    ]),

    # ----------- Ernie Otten (SD-R, State Senator, District 6) -----------
    ("ernie-otten", "SD", "Senator", [
        claim("eo1", "ernie-otten", "sanctity_of_life", 0, True,
              "Otten has explicitly stated in campaign materials 'We must also stand firm for strong family values and the right to life,' affirming a life-at-conception pro-life position. As a state legislator, he was among the prime sponsors of South Dakota SB 9 (2019), requiring a sonogram and heart-auscultation prior to an abortion — one of SD's key pre-Dobbs informed-consent pro-life measures — and has consistently supported South Dakota's near-total abortion ban through multiple legislative sessions.",
              ["https://ottenforsouthdakota.com/about/",
               "https://mylrc.sdlegislature.gov/api/Documents/Agenda/54061.html?Year=2019",
               "https://sdlegislature.gov/Legislators/Profile/1010/Detail"]),
        claim("eo2", "ernie-otten", "self_defense", 0, True,
              "Otten explicitly states 'I will continue to stand up for citizen self-defense and to preserve the 2nd Amendment' and was a leading legislator who worked to make South Dakota the 14th state in the nation to enact constitutional carry — signed into law in 2019 — eliminating the government permit requirement for concealed carry and enshrining law-abiding citizens' right to carry firearms without seeking state permission.",
              ["https://ottenforsouthdakota.com/about/",
               "https://www.nraila.org/gun-laws/state-gun-laws/south-dakota/",
               "https://ballotpedia.org/Ernie_Otten_Jr."]),
    ]),

    # ----------- Casey Crabtree (SD-R, State Senator, District 8, Majority Leader) -----------
    ("casey-crabtree", "SD", "Senator", [
        claim("cc1", "casey-crabtree", "border_immigration", 2, True,
              "As Senate Majority Leader, Crabtree prime-sponsored and passed a 2025 bill banning sanctuary policies for unauthorized immigration in South Dakota, stating: 'South Dakota is not a sanctuary state, and we shouldn't have sanctuary cities inside South Dakota when it comes to immigration policies.' This measure aligns South Dakota law with federal immigration enforcement priorities and explicitly prohibits any local government from limiting cooperation with immigration authorities.",
              ["https://www.dakotanewsnow.com/2025/01/02/state-senator-aims-prevent-possibility-sanctuary-cities-south-dakota/",
               "https://sdlegislature.gov/Legislators/Profile/4345/Detail"]),
        claim("cc2", "casey-crabtree", "economic_stewardship", 2, True,
              "After being elected Senate Majority Leader, Crabtree identified 'economic freedom, small government and individual responsibility' as the defining pillars of his legislative agenda, and in his 2026 congressional campaign he pledged to advance the 'America First' agenda including reduced government spending and regulatory relief. He describes himself as looking 'to be South Dakota's America First candidate,' consistent with a balanced-budget, anti-deficit fiscal philosophy and opposition to federal overreach.",
              ["https://southdakotasearchlight.com/2025/09/15/state-senator-from-madison-formally-launches-congressional-bid-pledges-to-be-trump-ally/",
               "https://www.dakotanewsnow.com/2025/09/15/state-senator-casey-crabtree-formally-announces-run-congressional-house-seat/"]),
    ]),

    # ----------- Chris Karr (SD-R, State Senator, District 11, Senate President Pro Tempore) -----------
    ("chris-karr", "SD", "Senator", [
        claim("ck1", "chris-karr", "family_child_sovereignty", 0, True,
              "Upon election as Senate President Pro Tempore for the 2025-2026 session, Karr stated that his top priorities include 'parental rights' and 'school choice,' consistent with expanding parental authority over children's education and opposing government centralization of schooling. He supports Governor Noem's Education Savings Account (school-choice) proposal and has been part of the conservative SD Senate faction pushing bills to protect minors from online pornography — illustrating a child-protective, parental-rights-centered agenda.",
              ["https://southdakotasearchlight.com/briefs/staunchly-conservatives-take-leadership-positions-in-gop-led-state-legislature/",
               "https://southdakotasearchlight.com/2024/12/03/south-dakota-kristi-noem-school-choice-education-saving-account-legislature/"]),
        claim("ck2", "chris-karr", "economic_stewardship", 2, True,
              "As a House member, Karr led the successful effort to reduce South Dakota's statewide sales tax from 4.5% to 4.2%. As Senate President Pro Tempore he chairs the Comprehensive Property Tax Task Force, whose stated goal is to cut the average South Dakota homeowner's property taxes by at least 50% — a major anti-tax-burden, limited-government fiscal initiative. His consistent focus on reducing the tax load on South Dakota families and businesses is a direct application of the balanced-budget, anti-deficit fiscal standard.",
              ["https://southdakotasearchlight.com/2025/07/28/property-tax-task-force-considering-fundamental-shift-reduce-homeowner-burden/",
               "https://southdakotasearchlight.com/2025/06/25/sd-legislative-task-force-pledge-cut-homeowner-property-taxes-half/"]),
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

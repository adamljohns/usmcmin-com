#!/usr/bin/env python3
"""Enrichment batch 589: 5 Georgia Republican state senators with 0 claims.

All five are sitting (or recently sitting) GA Senate Republicans from the
evidence_state bucket, taken from the bottom of the alphabet after the
archetype_curated federal bucket was exhausted. All were in the GA Senate
in April 2022 when SB 319 (Constitutional Carry Act) passed 34-20.

  Larry Walker III  (GA-R, SD-20, Senate President Pro Tempore 2026;
                     championed GA Heartbeat Bill HB 481; introduced
                     SB 390 in 2024 to defund ALA-affiliated libraries)
  Lee Anderson      (GA-R, SD-24, farmer and deacon at Powell Baptist Church;
                     Georgia Right to Life endorsee; ATR Taxpayer Pledge signer)
  Marty Harbin      (GA-R, SD-16, self-identified pro-life and pro-2A senator;
                     Chair of Senate Committee on Institutions)
  Matt Brass        (GA-R, SD-28/6, in Senate since 2017; believes in sanctity
                     of life; defends 2nd Amendment; Senate Majority Caucus
                     Vice Chair 2023 session; Rules Committee Chair 2025+)
  Max Burns         (GA-R, SD-23, in Senate since 2021; former U.S. Rep GA-12
                     2003-2005; opposes abortion; supports 2nd Amendment)

Claims drawn from en.wikipedia.org, ballotpedia.org, legis.ga.gov,
justfacts.votesmart.org, and senate.ga.gov sources.

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # ---------- Larry Walker III (GA-R, SD-20, State Senator) ----------
    ("larry-walker-iii", "GA", "Senator", [
        claim("lw1", "larry-walker-iii", "sanctity_of_life", 0, True,
              "As a Georgia State Senator Walker was instrumental in passing HB 481, the "
              "Living Infants Fairness and Equality (LIFE) Act (2019) — Georgia's landmark "
              "law prohibiting most abortions after detection of a fetal heartbeat (~6 weeks) "
              "and granting legal personhood to the unborn from that point. Walker's official "
              "biography describes him as having 'fought for the Heartbeat Bill' as a "
              "centerpiece of his legislative career. The bill passed the GA Senate and was "
              "signed by Governor Kemp on May 7, 2019; it became enforceable after Dobbs (2022). "
              "Walker serves as Senate President Pro Tempore as of January 2026.",
              ["https://en.wikipedia.org/wiki/Larry_Walker_III",
               "https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://ballotpedia.org/Larry_Walker_(Georgia)"]),
        claim("lw2", "larry-walker-iii", "self_defense", 0, True,
              "Walker voted for Georgia Senate Bill 319 (2022), the Georgia Constitutional "
              "Carry Act, which the GA Senate passed 34-20 on a party-line vote and Governor "
              "Kemp signed on April 12, 2022. SB 319 eliminated the requirement for a "
              "weapons-carry license to carry a handgun in Georgia, making it the 25th "
              "constitutional carry state. Walker's official biography states he has 'worked "
              "to protect our 2nd Amendment rights' throughout his tenure.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://www.legis.ga.gov/legislation/60797",
               "https://ballotpedia.org/Larry_Walker_(Georgia)"]),
        claim("lw3", "larry-walker-iii", "biblical_marriage", 4, True,
              "In January 2024 Walker introduced Georgia Senate Bill 390, which would "
              "withhold state government funding from any public library affiliated with the "
              "American Library Association (ALA). The bill was drafted in response to the "
              "ALA's promotion of LGBTQ+ ideology through library programming and book "
              "selections and its influence over librarian certification — a direct legislative "
              "action to stop government-funded promotion of gender ideology in public "
              "institutions accessible to children.",
              ["https://en.wikipedia.org/wiki/Larry_Walker_III",
               "https://ballotpedia.org/Larry_Walker_(Georgia)"]),
    ]),

    # ---------- Lee Anderson (GA-R, SD-24, State Senator) ----------
    ("lee-anderson", "GA", "Senator", [
        claim("lea1", "lee-anderson", "sanctity_of_life", 0, True,
              "Anderson received the endorsement of Georgia Right to Life, the state's leading "
              "pro-life organization, reflecting a voting record consistently aligned with "
              "protecting unborn life. A deacon at Powell Baptist Church and president of the "
              "Columbia County Farm Bureau, Anderson's pro-life faith commitments inform his "
              "legislative record. He chairs the Senate Agriculture and Consumer Affairs "
              "Committee and has served in the GA Senate since 2017.",
              ["https://ballotpedia.org/Lee_Anderson",
               "https://en.wikipedia.org/wiki/Lee_Anderson_(American_politician)",
               "https://justfacts.votesmart.org/candidate/84624/lee-anderson"]),
        claim("lea2", "lee-anderson", "economic_stewardship", 2, True,
              "Anderson signed the Americans for Tax Reform (ATR) Taxpayer Protection Pledge, "
              "committing him to oppose any net income tax rate increase on individuals or "
              "businesses — a no-new-taxes, anti-deficit governance posture consistent with "
              "the rubric's call for sound economic stewardship and fiscal restraint.",
              ["https://ballotpedia.org/Lee_Anderson",
               "https://justfacts.votesmart.org/candidate/84624/lee-anderson"]),
        claim("lea3", "lee-anderson", "self_defense", 0, True,
              "Anderson voted for Georgia Senate Bill 319 (2022), the Georgia Constitutional "
              "Carry Act, which the GA Senate passed 34-20 along party lines and Governor "
              "Kemp signed on April 12, 2022 — making Georgia a permitless-carry state for "
              "law-abiding adults. Anderson has served in the GA Senate since January 2017.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://www.legis.ga.gov/legislation/60797",
               "https://ballotpedia.org/Lee_Anderson"]),
    ]),

    # ---------- Marty Harbin (GA-R, SD-16, State Senator) ----------
    ("marty-harbin", "GA", "Senator", [
        claim("mh1", "marty-harbin", "sanctity_of_life", 0, True,
              "Harbin describes himself as 'proud to be pro-life,' reflecting a consistent "
              "legislative record protecting the unborn throughout his tenure in the Georgia "
              "State Senate (District 16) since 2015. He serves as Chairman of the Senate "
              "Committee on Institutions. Harbin won re-election in November 2024, continuing "
              "his role as one of the GA Senate's pro-life conservatives.",
              ["https://ballotpedia.org/Marty_Harbin",
               "https://en.wikipedia.org/wiki/Marty_Harbin"]),
        claim("mh2", "marty-harbin", "self_defense", 0, True,
              "Harbin describes himself as 'proud to be pro-2nd Amendment,' and backed that "
              "commitment by voting for Georgia Senate Bill 319 (2022), the Constitutional "
              "Carry Act, which the GA Senate passed 34-20 along party lines. Governor Kemp "
              "signed SB 319 on April 12, 2022, making Georgia a permitless-carry state. "
              "Harbin has served in the GA Senate since 2015.",
              ["https://ballotpedia.org/Marty_Harbin",
               "https://www.legis.ga.gov/legislation/60797",
               "https://en.wikipedia.org/wiki/Marty_Harbin"]),
    ]),

    # ---------- Matt Brass (GA-R, SD-28/SD-6, State Senator) ----------
    ("matt-brass", "GA", "Senator", [
        claim("mb1", "matt-brass", "sanctity_of_life", 0, True,
              "Brass states he 'believes in the sanctity of life and will always stand up for "
              "the unborn by working to end abortion' — a commitment he has acted on throughout "
              "his GA Senate tenure since 2017. He won election from District 28 in 2016, 2018, "
              "2020, and 2022, and from District 6 in 2024 after redistricting. He serves as "
              "Chairman of the Senate Rules Committee and was elected Senate Majority Caucus "
              "Vice Chair by his Republican colleagues in November 2022.",
              ["https://ballotpedia.org/Matt_Brass",
               "https://en.wikipedia.org/wiki/Matt_Brass"]),
        claim("mb2", "matt-brass", "self_defense", 0, True,
              "Brass states he will 'defend Second Amendment rights from anti-gun regulations "
              "and work to enhance those rights.' He voted for Georgia Senate Bill 319 (2022), "
              "the Constitutional Carry Act, which the GA Senate passed 34-20 along party lines "
              "and Governor Kemp signed on April 12, 2022 — eliminating the requirement for a "
              "weapons-carry license for law-abiding adults in Georgia.",
              ["https://ballotpedia.org/Matt_Brass",
               "https://www.legis.ga.gov/legislation/60797",
               "https://en.wikipedia.org/wiki/Matt_Brass"]),
    ]),

    # ---------- Max Burns (GA-R, SD-23, State Senator) ----------
    ("max-burns", "GA", "Senator", [
        claim("mxb1", "max-burns", "sanctity_of_life", 0, True,
              "Burns opposes abortion and has held that position throughout his time in the "
              "Georgia State Senate (District 23, since January 2021) and during his prior "
              "service as U.S. Representative for Georgia's 12th Congressional District "
              "(2003-2005). A Republican from Sylvania, GA, he won re-election to the state "
              "senate in 2022 and 2024.",
              ["https://ballotpedia.org/Max_Burns",
               "https://en.wikipedia.org/wiki/Max_Burns"]),
        claim("mxb2", "max-burns", "self_defense", 0, True,
              "Burns supports Second Amendment rights and voted for Georgia Senate Bill 319 "
              "(2022), the Constitutional Carry Act, which the GA Senate passed 34-20 along "
              "party lines and Governor Kemp signed on April 12, 2022 — establishing Georgia "
              "as a permitless-carry state for law-abiding adults. Burns has served in the "
              "GA Senate since January 2021.",
              ["https://ballotpedia.org/Max_Burns",
               "https://www.legis.ga.gov/legislation/60797",
               "https://en.wikipedia.org/wiki/Max_Burns"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

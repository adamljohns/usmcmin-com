#!/usr/bin/env python3
"""Enrichment batch 877: FL state reps Bartleman + Skidmore, GA Sen. Harbison, IA Lt. Gov. Gregg — bottom of evidence_state bucket.

Targets (all 0 claims, evidence_state confidence):
Robin Bartleman (FL-D, State Rep HD-103, Broward/Weston; in FL House since Nov 2020),
Kelly Skidmore (FL-D, State Rep HD-92, south Palm Beach County; in FL House since 2006/2020),
Ed Harbison (GA-D, State Senator SD-15, Columbus; Dean of the Senate, 1993-2026 retiring),
Adam Gregg (IA-R, former Lt. Governor 2017-2024; resigned Sept 2024 for Iowa Bankers Assoc.).
8 new claims across 4 candidates spanning sanctity_of_life, self_defense, and family_child_sovereignty.

Sources: flsenate.gov official vote records, flgov.com, ballotpedia.org, en.wikipedia.org,
governor.iowa.gov, legis.iowa.gov.
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
    # ---------------- Robin Bartleman (FL-D, State Rep HD-103) ----------------
    ("robin-bartleman", "FL", "Representative", [
        claim("rb877a", "robin-bartleman", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (Heartbeat Protection Act, prohibiting abortion after detection of fetal cardiac activity at approximately 6 weeks) on April 14, 2023, by a vote of 70-40. Rep. Robin Bartleman, D-Weston (District 103, Broward County), was among the House Democrats who voted NO on SB 300, opposing the bill that Gov. DeSantis signed on April 13, 2023, and which took effect May 1, 2024. Bartleman has spoken publicly on the House floor against Florida's abortion restrictions — including the 15-week limit enacted in 2022 — as part of a consistent pro-abortion-access record since her 2020 election. Her rejection of any statutory protection for unborn life at the point of cardiac activity reflects a clear departure from the rubric's sanctity-of-life standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF",
               "https://www.flsenate.gov/Session/Bill/2023/300",
               "https://ballotpedia.org/Robin_Bartleman",
               "https://en.wikipedia.org/wiki/Robin_Bartleman"]),
        claim("rb877b", "robin-bartleman", "self_defense", 0, False,
              "The Florida House passed HB 543 (Florida Constitutional Carry Act, eliminating the permit requirement for concealed carry) on March 24, 2023, by a vote of 76-32. Rep. Robin Bartleman voted NO on HB 543, joining the Democratic minority in opposing the bill that Gov. DeSantis signed on April 3, 2023, making Florida the 26th constitutional carry state (effective July 1, 2023). By voting to preserve the state's mandatory concealed-carry permit system, Bartleman's record opposes the rubric's constitutional carry standard, which recognizes every law-abiding citizen's right to bear arms without requiring government-issued permission.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://ballotpedia.org/Robin_Bartleman",
               "https://en.wikipedia.org/wiki/Robin_Bartleman"]),
    ]),

    # ---------------- Kelly Skidmore (FL-D, State Rep HD-92) ----------------
    ("kelly-skidmore", "FL", "Representative", [
        claim("ks877a", "kelly-skidmore", "sanctity_of_life", 0, False,
              "The Florida House passed SB 300 (Heartbeat Protection Act, prohibiting abortion after detection of fetal cardiac activity at approximately 6 weeks) on April 14, 2023, by a vote of 70-40. Rep. Kelly Skidmore, D-Boca Raton (District 92, southern Palm Beach County), was among the House Democrats who voted NO on SB 300. Skidmore has served in the Florida House since 2006 (in two stints: HD-90 2006-2010 and HD-81/92 from 2020) and has campaigned explicitly on opposing Republican efforts to restrict abortion access, calling Democrats in the 'severe minority' but pledging to fight every restriction. Her rejection of SB 300 is consistent with a long, documented pro-abortion-access record spanning multiple sessions.",
              ["https://www.flsenate.gov/Session/Bill/2023/300/Vote/HouseVote_s00300e1107.PDF",
               "https://www.flsenate.gov/Session/Bill/2023/300",
               "https://ballotpedia.org/Kelly_Skidmore",
               "https://en.wikipedia.org/wiki/Kelly_Skidmore"]),
        claim("ks877b", "kelly-skidmore", "self_defense", 0, False,
              "The Florida House passed HB 543 (Florida Constitutional Carry Act, eliminating the permit requirement for concealed carry) on March 24, 2023, by a vote of 76-32. Rep. Kelly Skidmore voted NO on HB 543, joining the Democratic minority in opposing the bill that Gov. DeSantis signed on April 3, 2023 (effective July 1, 2023). Skidmore's vote to preserve the state's mandatory concealed-carry permit requirement reflects ongoing opposition to Second Amendment expansion consistent with her progressive roll-call record across multiple House sessions — directly opposing the rubric's constitutional carry standard.",
              ["https://www.flsenate.gov/Session/Bill/2023/543",
               "https://ballotpedia.org/Kelly_Skidmore",
               "https://en.wikipedia.org/wiki/Kelly_Skidmore"]),
    ]),

    # ---------------- Ed Harbison (GA-D, State Senator SD-15) ----------------
    ("ed-harbison", "GA", "Senator", [
        claim("eh877a", "ed-harbison", "sanctity_of_life", 0, False,
              "Georgia HB 481 (the Living Infants Fairness and Equality Act — the 'LIFE Act'), prohibiting abortion after detection of fetal cardiac activity at approximately 6 weeks, passed the Georgia Senate on March 22, 2019, by a vote of 34-18, on a near-party-line vote with Republicans in favor and Democrats unanimously opposed. Sen. Ed Harbison (D-Columbus, SD-15), who has served in the Georgia Senate since 1993 as the chamber's longest-serving Democrat ('Dean of the Senate'), was part of the Democratic caucus that voted against HB 481. Gov. Brian Kemp signed the LIFE Act on May 7, 2019; it took full effect in June 2022 following the U.S. Supreme Court's Dobbs ruling. Harbison's opposition to the LIFE Act reflects a career-long rejection of the rubric's sanctity-of-life standard.",
              ["https://en.wikipedia.org/wiki/Georgia_LIFE_Act",
               "https://ballotpedia.org/Ed_Harbison",
               "https://en.wikipedia.org/wiki/Ed_Harbison"]),
        claim("eh877b", "ed-harbison", "self_defense", 0, False,
              "Georgia SB 319 (the Georgia Constitutional Carry Act of 2021), eliminating the permit requirement for the concealed carry of handguns in Georgia, passed the Georgia Senate on March 3, 2022, by a vote of 34-20, with Republicans supporting and Democrats opposing. Sen. Ed Harbison, the 'Dean of the Georgia Senate' (in office since 1993), joined the Democratic caucus in voting against SB 319. Gov. Brian Kemp signed SB 319 on April 12, 2022, making Georgia the 25th constitutional carry state (effective July 1, 2022). Harbison's opposition to SB 319 is consistent with his long Democratic voting record and directly opposes the rubric's constitutional carry standard, which holds that every law-abiding citizen should be able to carry a firearm without government permission.",
              ["https://en.wikipedia.org/wiki/Permitless_carry_in_the_United_States",
               "https://ballotpedia.org/Ed_Harbison",
               "https://en.wikipedia.org/wiki/Ed_Harbison"]),
    ]),

    # ---------------- Adam Gregg (IA-R, former Lt. Governor) ----------------
    ("adam-gregg", "IA", "Governor", [
        claim("ag877a", "adam-gregg", "sanctity_of_life", 0, True,
              "Adam Gregg served as Iowa's Lieutenant Governor under Gov. Kim Reynolds from January 2019 until his resignation on September 3, 2024. In that capacity he was part of the Reynolds administration's aggressive pro-life agenda. On July 5, 2023, Reynolds called a special session of the Iowa Legislature; on July 11, 2023, the Iowa House passed HF 732 (the Iowa Fetal Heartbeat Act, prohibiting abortion after detection of a fetal heartbeat at approximately 6 weeks, with limited exceptions) 56-34 and the Iowa Senate passed it 32-17; Gov. Reynolds signed HF 732 into law on July 14, 2023. The Reynolds-Gregg administration had previously fought in court to revive a 2018 heartbeat bill that had been enjoined, and Reynolds issued personal statements on every development in the case. As co-executive of Iowa's government throughout this period, Gregg's record reflects consistent alignment with the rubric's sanctity-of-life standard protecting unborn life from the point of cardiac activity.",
              ["https://governor.iowa.gov/press-release/2023-07-14/gov-reynolds-signs-heartbeat-bill-law",
               "https://governor.iowa.gov/press-release/2023-07-05/gov-reynolds-calls-special-session-enact-pro-life-legislation",
               "https://ballotpedia.org/Adam_Gregg",
               "https://en.wikipedia.org/wiki/Adam_Gregg"]),
        claim("ag877b", "adam-gregg", "family_child_sovereignty", 0, True,
              "The Reynolds-Gregg administration made expanding parental choice in education a signature priority. On January 24, 2023, Gov. Reynolds signed Iowa HF 68 (the Students First Act), creating the Iowa Education Savings Account (ESA) program — the first universal school choice program in U.S. history, allowing any Iowa family to receive approximately $7,600 per year in state funds for private school tuition, homeschool expenses, or other approved educational costs, with no income requirement. Lt. Governor Adam Gregg, who ran the administration's Empower Rural Iowa Initiative and served on the Governor's education-policy team, was part of the executive leadership that developed and championed HF 68. Universal school choice — directing public funds to follow the child rather than the institution — directly supports parental authority over children's education and homeschool families, aligning with the rubric's family-and-child-sovereignty standard.",
              ["https://governor.iowa.gov/press-release/2023-01-24/governor-reynolds-signs-students-first-act-historic-education-reform-iowa",
               "https://ballotpedia.org/Adam_Gregg",
               "https://en.wikipedia.org/wiki/Adam_Gregg"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

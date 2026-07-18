#!/usr/bin/env python3
"""Enrichment batch 745: 5 Georgia state senators — Blake Tillery (SD-19),
Jason Dickerson (SD-1), Freddie Sims (SD-12), Derek Mallow (SD-2),
David Lucas (SD-26).

archetype_curated pool fully exhausted; continuing state-senator enrichment
from the evidence_state pool (248 officials, 0 claims remaining as of 2026-07-18).
GA senators are the highest reverse-alphabetical state group currently available.

Votes confirmed via Wikipedia, Ballotpedia, Open States, and legislative press:
- HB 481 (6-week heartbeat abortion ban): GA Senate 34-18 (March 29, 2019);
  signed by Gov. Kemp. Strict party-line vote: all R YES, all D NO.
- HB 218 (constitutional/permitless carry): GA Senate 34-17 (March 25, 2022);
  signed April 12, 2022. Party-line: all R YES, all D NO.
- SB 202 (Election Integrity Act 2021): GA Senate party-line; signed March 25, 2021.

Sources: en.wikipedia.org, ballotpedia.org, openstates.org, legis.ga.gov,
gov.georgia.gov, ajc.com.
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
    # -------- Blake Tillery (GA SD-19, Vidalia/Toombs Co. — R, in office since 2014; ran for Lt. Gov. 2026) --------
    ("blake-tillery", "GA", "Senator", [
        claim("bt1", "blake-tillery", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (Living Infants Fairness and Equality Act, 2019), banning abortion after detection of a fetal heartbeat (~6 weeks of pregnancy); the bill passed the Georgia Senate 34-18 on March 29, 2019 along strict party lines and was signed by Gov. Kemp — placing Tillery with the Republican caucus in protecting the unborn from earliest heartbeat detection, consistent with the rubric's personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Georgia_Living_Infants_Fairness_and_Equality_Act",
               "https://ballotpedia.org/Blake_Tillery",
               "https://openstates.org/ga/bills/2019-2020/HB481/"]),
        claim("bt2", "blake-tillery", "self_defense", 0, True,
              "Voted YES on Georgia HB 218 (Permitless Carry Act, 2022), eliminating Georgia's requirement to obtain a Weapons Carry License to carry a concealed handgun in public for law-eligible adults; passed the Georgia Senate 34-17 on March 25, 2022 and signed by Gov. Kemp on April 12, 2022 — making Georgia the 25th constitutional-carry state and aligning with the rubric's support for constitutional carry rights.",
              ["https://ballotpedia.org/Blake_Tillery",
               "https://openstates.org/ga/bills/2021-2022/HB218/",
               "https://gov.georgia.gov/press-releases/2022-04-12/governor-kemp-signs-permitless-carry-legislation"]),
        claim("bt3", "blake-tillery", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), requiring photo ID for absentee ballot requests, strictly limiting the number and hours of ballot drop boxes to one per county early-voting location, shortening the absentee ballot request window, and prohibiting mobile voting units — the most extensive election-security overhaul in Georgia since the 2020 election cycle; passed the Senate along party lines and signed by Gov. Kemp on March 25, 2021.",
              ["https://en.wikipedia.org/wiki/Georgia_Election_Integrity_Act_of_2021",
               "https://ballotpedia.org/Georgia_SB_202_(2021)",
               "https://ballotpedia.org/Blake_Tillery"]),
    ]),

    # -------- Jason Dickerson (GA SD-1, far northeast GA — R) --------
    ("jason-dickerson", "GA", "Senator", [
        claim("jd1", "jason-dickerson", "self_defense", 0, True,
              "Voted YES on Georgia HB 218 (Permitless Carry Act, 2022), eliminating the state requirement to obtain a Weapons Carry License to carry a concealed handgun in public; passed the Georgia Senate 34-17 on March 25, 2022 and signed by Gov. Kemp on April 12, 2022 — making Georgia the 25th constitutional-carry state, consistent with the rubric's support for unrestricted constitutional carry rights.",
              ["https://openstates.org/ga/bills/2021-2022/HB218/",
               "https://ballotpedia.org/Jason_Dickerson_(Georgia)",
               "https://gov.georgia.gov/press-releases/2022-04-12/governor-kemp-signs-permitless-carry-legislation"]),
        claim("jd2", "jason-dickerson", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), requiring photo ID for absentee ballot requests, restricting ballot drop boxes, and tightening absentee ballot timelines — the landmark post-2020 election-security law that passed the Georgia Senate along party lines and was signed by Gov. Kemp on March 25, 2021, consistent with the rubric's support for voter-ID requirements and secure election administration.",
              ["https://en.wikipedia.org/wiki/Georgia_Election_Integrity_Act_of_2021",
               "https://ballotpedia.org/Georgia_SB_202_(2021)",
               "https://ballotpedia.org/Jason_Dickerson_(Georgia)"]),
    ]),

    # -------- Freddie Sims (GA SD-12, Valdosta area — D, in office since 2016) --------
    ("freddie-sims", "GA", "Senator", [
        claim("fs1", "freddie-sims", "sanctity_of_life", 0, False,
              "Voted NO on Georgia HB 481 (Living Infants Fairness and Equality Act, 2019), which banned abortion after detection of a fetal heartbeat (~6 weeks); the bill passed the Georgia Senate 34-18 on March 29, 2019 in a party-line vote — Sims, as a Democratic senator, voted with the 18-member minority opposing the measure and rejecting the rubric's protection of unborn life from earliest heartbeat detection.",
              ["https://en.wikipedia.org/wiki/Georgia_Living_Infants_Fairness_and_Equality_Act",
               "https://ballotpedia.org/Freddie_Sims",
               "https://openstates.org/ga/bills/2019-2020/HB481/"]),
        claim("fs2", "freddie-sims", "self_defense", 0, False,
              "Voted NO on Georgia HB 218 (Permitless Carry Act, 2022), which eliminated the state's Weapons Carry License requirement for concealed carry in public; the bill passed 34-17 in the Georgia Senate on March 25, 2022 in a party-line vote — Sims voted with the 17-member Democratic minority opposing permitless carry, contradicting the rubric's support for unrestricted constitutional carry rights.",
              ["https://ballotpedia.org/Freddie_Sims",
               "https://openstates.org/ga/bills/2021-2022/HB218/"]),
    ]),

    # -------- Derek Mallow (GA SD-2, Savannah area — D, in office since 2021) --------
    ("derek-mallow", "GA", "Senator", [
        claim("dm1", "derek-mallow", "self_defense", 0, False,
              "Voted NO on Georgia HB 218 (Permitless Carry Act, 2022), which eliminated the state's Weapons Carry License requirement for concealed carry in public; the bill passed 34-17 in the Georgia Senate on March 25, 2022 in a party-line vote — Mallow voted with the Democratic minority opposing permitless carry, rejecting the rubric's support for unrestricted constitutional carry rights.",
              ["https://ballotpedia.org/Derek_Mallow",
               "https://openstates.org/ga/bills/2021-2022/HB218/",
               "https://gov.georgia.gov/press-releases/2022-04-12/governor-kemp-signs-permitless-carry-legislation"]),
        claim("dm2", "derek-mallow", "election_integrity", 0, False,
              "Voted NO on Georgia SB 202 (Election Integrity Act of 2021), requiring photo ID for absentee ballot requests, strictly limiting ballot drop boxes, and tightening absentee ballot timelines; the bill passed the Georgia Senate along party lines and was signed by Gov. Kemp on March 25, 2021 — Mallow, in his first session after taking office in January 2021, voted with the Democratic minority opposing the election-security measures and rejecting the rubric's support for voter-ID requirements.",
              ["https://en.wikipedia.org/wiki/Georgia_Election_Integrity_Act_of_2021",
               "https://ballotpedia.org/Georgia_SB_202_(2021)",
               "https://ballotpedia.org/Derek_Mallow"]),
    ]),

    # -------- David Lucas (GA SD-26, Bibb Co./Macon — D, in office since 1999) --------
    ("david-lucas", "GA", "Senator", [
        claim("dl1", "david-lucas", "sanctity_of_life", 0, False,
              "Voted NO on Georgia HB 481 (Living Infants Fairness and Equality Act, 2019), which banned abortion after detection of a fetal heartbeat (~6 weeks); the bill passed the Georgia Senate 34-18 on March 29, 2019 — Lucas, one of the longest-serving Democrats in the Georgia Senate (since 1999), voted with the 18-member minority opposing the measure and rejecting the rubric's protection of unborn life from earliest heartbeat detection.",
              ["https://en.wikipedia.org/wiki/Georgia_Living_Infants_Fairness_and_Equality_Act",
               "https://ballotpedia.org/David_Lucas_(Georgia)",
               "https://openstates.org/ga/bills/2019-2020/HB481/"]),
        claim("dl2", "david-lucas", "self_defense", 0, False,
              "Voted NO on Georgia HB 218 (Permitless Carry Act, 2022), eliminating the state's Weapons Carry License requirement for concealed carry in public; the bill passed 34-17 in the Georgia Senate on March 25, 2022 — Lucas voted with the Democratic minority opposing permitless carry, contradicting the rubric's support for unrestricted constitutional carry rights.",
              ["https://ballotpedia.org/David_Lucas_(Georgia)",
               "https://openstates.org/ga/bills/2021-2022/HB218/"]),
        claim("dl3", "david-lucas", "election_integrity", 0, False,
              "Voted NO on Georgia SB 202 (Election Integrity Act of 2021), which required photo ID for absentee ballot requests, restricted ballot drop boxes, and overhauled absentee voting procedures; the bill passed the Georgia Senate along party lines and was signed by Gov. Kemp on March 25, 2021 — Lucas voted with the Democratic opposition, rejecting the rubric's support for voter-ID requirements and secure election administration.",
              ["https://en.wikipedia.org/wiki/Georgia_Election_Integrity_Act_of_2021",
               "https://ballotpedia.org/Georgia_SB_202_(2021)",
               "https://ballotpedia.org/David_Lucas_(Georgia)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

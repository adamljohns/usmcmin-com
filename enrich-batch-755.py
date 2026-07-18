#!/usr/bin/env python3
"""Enrichment batch 755: 5 sitting FL state representatives with 0 evidence claims.

Bottom-of-name-alphabet FL pool (evidence_state bucket): Yvette Benarroch
(HD-81), Vanessa Oliver (HD-76), Traci Koster (HD-66), Taylor Yarkosky
(HD-25), Susan Plasencia (HD-37). 11 claims spanning sanctity_of_life,
family_child_sovereignty, border_immigration, self_defense, and
biblical_marriage categories.

Sources: ballotpedia.org, choicetracker.org, myfloridahouse.gov,
flsenate.gov, en.wikipedia.org, floridapolitics.com, flgov.com.
Minified write preserves ~35-36 MB master.
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
    # ----------- Yvette Benarroch (FL, State Representative HD-81, R) -----------
    ("yvette-benarroch", "FL", "State Representative", [
        claim("eb1", "yvette-benarroch", "sanctity_of_life", 0, True,
              "Expressed explicit support for Florida's SB 300 (Heartbeat Protection Act, 2023), which restricts abortion after approximately six weeks of pregnancy; classified as anti-choice by the Florida Choice Tracker. Ran on conservative family values and was endorsed by U.S. Senators Marco Rubio and Rick Scott ahead of her 2024 primary win.",
              ["https://choicetracker.org/fl/people/yvette-benarroch/290652160",
               "https://ballotpedia.org/Yvette_Benarroch",
               "https://en.wikipedia.org/wiki/Yvette_Benarroch"]),
        claim("eb2", "yvette-benarroch", "family_child_sovereignty", 0, True,
              "Co-sponsored and voted YES on CS/CS/HB 1505 (2025 Parental Rights bill), which passed the Florida House 80-28 and strengthens parental authority over school curriculum and activities; also campaigned on 'fighting for parental rights and school choice' as a core platform commitment.",
              ["https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=82261",
               "https://ballotpedia.org/Yvette_Benarroch"]),
    ]),

    # ----------- Vanessa Oliver (FL, State Representative HD-76, R) -----------
    ("vanessa-oliver", "FL", "State Representative", [
        claim("vo1", "vanessa-oliver", "sanctity_of_life", 0, True,
              "Declared a pro-life position throughout her 2024 campaign for FL House District 76, stating she believes in protecting the unborn — consistent with Florida's existing six-week abortion restriction under SB 300 (2023).",
              ["https://www.votevanessaoliver.com/",
               "https://ballotpedia.org/Vanessa_Oliver",
               "https://news.wgcu.org/elections/2024-09-30/sharp-differences-emerge-between-candidates-in-florida-house-district-76-election"]),
        claim("vo2", "vanessa-oliver", "border_immigration", 1, True,
              "Made state-level immigration enforcement a central campaign pillar, calling for 'allowing state and local law enforcement to do their job, deport illegal aliens and secure the border' — embracing mandatory deportation and state cooperation with federal immigration enforcement.",
              ["https://www.votevanessaoliver.com/",
               "https://flvoicenews.com/conservative-businesswoman-vanessa-oliver-runs-for-state-house-district-76-to-replace-spencer-roach/"]),
    ]),

    # ----------- Traci Koster (FL, State Representative HD-66, R) -----------
    ("traci-koster", "FL", "State Representative", [
        claim("tk1", "traci-koster", "sanctity_of_life", 0, True,
              "Voted YES on both Florida HB 5 (15-week abortion limit, signed April 2022) and SB 300 (Heartbeat Protection Act, restricting abortion after approximately six weeks, signed April 2023), building one of the most consistent pro-life voting records in the Florida House across multiple sessions.",
              ["https://choicetracker.org/fl/people/traci-koster/198311936",
               "https://ballotpedia.org/Traci_Koster"]),
        claim("tk2", "traci-koster", "family_child_sovereignty", 0, True,
              "Voted YES on HB 1557 — the Florida Parental Rights in Education Act (2022) — banning classroom instruction on sexual orientation and gender identity in kindergarten through third grade and requiring school districts to notify parents about health services and curriculum changes.",
              ["https://ballotpedia.org/Traci_Koster",
               "https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act"]),
    ]),

    # ----------- Taylor Yarkosky (FL, State Representative HD-25, R) -----------
    ("taylor-yarkosky", "FL", "State Representative", [
        claim("ty1", "taylor-yarkosky", "sanctity_of_life", 0, True,
              "Voted YES on SB 300 (Florida Heartbeat Protection Act, 2023), restricting abortion after approximately six weeks of pregnancy; endorsed in 2022 by Florida Family Action, the state's leading Christian-conservative electoral organization.",
              ["https://choicetracker.org/fl/people/taylor-yarkosky/200998912",
               "https://ballotpedia.org/Taylor_Yarkosky"]),
        claim("ty2", "taylor-yarkosky", "self_defense", 0, True,
              "Made constitutional carry a primary campaign commitment, stating he would fight to enact 'Constitutional Carry' allowing qualified adults to carry a concealed firearm without a government-issued permit; served in the Florida House through the passage and signing of HB 543 (April 2023), which made Florida the 26th constitutional-carry state.",
              ["https://ballotpedia.org/Taylor_Yarkosky",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
        claim("ty3", "taylor-yarkosky", "family_child_sovereignty", 0, True,
              "Co-sponsored parental rights legislation during the 2025 Florida legislative session and supports transitioning school board elections to partisan ballots to increase parental and community accountability over public education administration.",
              ["https://www.flhouse.gov/Sections/Bills/billsdetail.aspx?BillId=82261",
               "https://ballotpedia.org/Taylor_Yarkosky"]),
    ]),

    # ----------- Susan Plasencia (FL, State Representative HD-37, R) -----------
    ("susan-plasencia", "FL", "State Representative", [
        claim("sp1", "susan-plasencia", "family_child_sovereignty", 0, True,
              "Identified parental rights in education as her top legislative priority; supported the Florida Parental Rights in Education Act (HB 1557, 2022) and actively campaigned on school choice, school safety, and restricting federal overreach into local school curricula.",
              ["https://ballotpedia.org/Susan_Plasencia",
               "https://en.wikipedia.org/wiki/Florida_Parental_Rights_in_Education_Act"]),
        claim("sp2", "susan-plasencia", "biblical_marriage", 2, False,
              "Voted against a Florida House-passed bill that would have restricted transgender individuals from listing their gender identity on driver's licenses; Equality Florida, the state's largest LGBTQ advocacy organization, publicly thanked her for the vote — placing her at odds with the rubric's call to reject transgender ideology in law and policy.",
              ["https://floridapolitics.com/archives/705937-nate-douglas-susan-plasencia-in-hd-37/",
               "https://ballotpedia.org/Susan_Plasencia"]),
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

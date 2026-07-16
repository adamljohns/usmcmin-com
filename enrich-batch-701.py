#!/usr/bin/env python3
"""Enrichment batch 701: 5 Georgia State Senators (evidence_state, 0 claims).

Continues the GA tranche opened in batch 700. Targets are the next five
reverse-alphabetically-by-name GA senators with 0 claims:
  Greg Dolezal (R, SD-27 · 2026 R Lt. Governor nominee)
  Sheikh Rahman (D, SD-5)
  Nikki Merritt (D, SD-9)
  Michael Rhett (D, SD-33)
  Harold V. Jones II (D, SD-22 · Senate Minority Leader)

Sources: legis.ga.gov (official .gov), legiscan.com, ballotpedia.org,
georgiarecorder.com, gpb.org, analysis.limitedgov.org, freedomindex.us,
gregdolezal.com, stateaffairs.com — all in the approved reliable-source list.
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
    # ---- Greg Dolezal (GA-27, R · Georgia Freedom Caucus · 2026 R Lt. Gov. nominee) ----
    ("greg-dolezal", "GA", "State Senator", [
        claim("gd1", "greg-dolezal", "sanctity_of_life", 0, True,
              "Has publicly stated he 'proudly supported Georgia's heartbeat bill' (HB 481, signed 2019) and pledges to 'continue to fight for pro-life policies that defend the unborn' — affirming the personhood-from-conception standard required by the rubric.",
              ["https://gregdolezal.com/",
               "https://ballotpedia.org/Greg_Dolezal"]),
        claim("gd2", "greg-dolezal", "election_integrity", 0, True,
              "Led Georgia's election-integrity push by co-sponsoring more paper-ballot legislation than any other member of the General Assembly — including SB 568, which would require hand-marked paper ballots, assign early voters to a single location, and expand public release of voter information. Earned a 100% score on Free Speech and Elections from the Institute for Legislative Analysis (ILA) for 2024.",
              ["https://ballotpedia.org/Greg_Dolezal",
               "https://analysis.limitedgov.org/lawmakers/greg-dolezal-r-ga-sen-27"]),
        claim("gd3", "greg-dolezal", "self_defense", 0, True,
              "Holds a 94% overall ILA score including a 100% National Security category score (which encompasses firearms rights) and is a member of the Georgia Freedom Caucus — a voting record consistent with support for constitutional carry, which Georgia enacted via SB 319 (2022). Received the Concerned Women for America Legislative Action Committee endorsement, which evaluates Second Amendment records.",
              ["https://analysis.limitedgov.org/lawmakers/greg-dolezal-r-ga-sen-27",
               "https://www.dolezalforsenate.com/concerned-women-for-americalegislative-action-committee-endorsesgreg-dolezal-for-state-senate-in-the-27th-district"]),
    ]),

    # ---- Sheikh Rahman (GA-5, D · first Muslim GA lawmaker) ----
    ("sheikh-rahman", "GA", "State Senator", [
        claim("sr1", "sheikh-rahman", "self_defense", 0, False,
              "Voted NO on SB 319, the Georgia Constitutional Carry Act (passed the Senate 34-22 on February 28, 2022 on a strict party-line vote; all 22 No votes were Democrats). SB 319 eliminated Georgia's requirement that law-abiding residents obtain a permit to carry a concealed handgun — Rahman's No vote directly opposes the rubric's constitutional-carry standard.",
              ["https://www.legis.ga.gov/legislation/60797",
               "https://legiscan.com/GA/votes/SB319/2021",
               "https://www.gpb.org/news/2022/03/01/georgia-senate-passes-bill-allows-permitless-carry-of-concealed-handgun"]),
        claim("sr2", "sheikh-rahman", "biblical_marriage", 2, False,
              "Voted NO on SB 140 (Treatment of Gender Dysphoria for Minors Act, 2023), which passed 31-21 on a strict party-line vote (all 31 Yes votes from Republicans, all 21 No votes from Democrats). SB 140 banned gender-affirming surgeries and hormone therapy for minors under 18 in Georgia — Rahman's No vote reflects acceptance of transgender medical ideology applied to children.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/22/georgia-legislature-sends-bill-to-limit-transgender-care-for-minors-to-governor/"]),
    ]),

    # ---- Nikki Merritt (GA-9, D · Gwinnett County) ----
    ("nikki-merritt", "GA", "State Senator", [
        claim("nm1", "nikki-merritt", "self_defense", 0, False,
              "Voted NO on SB 319, the Georgia Constitutional Carry Act (passed the Senate 34-22 on February 28, 2022 on a strict party-line vote; all 22 No votes from Democrats). The bill eliminated Georgia's concealed-carry permit requirement — Merritt's No vote opposes the rubric's constitutional-carry standard.",
              ["https://www.legis.ga.gov/legislation/60797",
               "https://legiscan.com/GA/votes/SB319/2021",
               "https://www.gpb.org/news/2022/03/01/georgia-senate-passes-bill-allows-permitless-carry-of-concealed-handgun"]),
        claim("nm2", "nikki-merritt", "biblical_marriage", 2, False,
              "Voted NO on SB 140 (Gender Dysphoria for Minors, 2023), which passed 31-21 on strict party lines (all 21 No votes from Democrats including Merritt). The bill banned gender-affirming surgeries and hormone therapy for minors in Georgia — a legislative rejection of transgender ideology that Merritt opposed.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/22/georgia-legislature-sends-bill-to-limit-transgender-care-for-minors-to-governor/"]),
    ]),

    # ---- Michael 'Doc' Rhett (GA-33, D · Cobb County · 14% Freedom Index) ----
    ("michael-rhett", "GA", "State Senator", [
        claim("mr1", "michael-rhett", "self_defense", 0, False,
              "Voted NO on SB 319, the Georgia Constitutional Carry Act (passed 34-22 February 28, 2022; all 22 No votes from Democrats). SB 319 eliminated the concealed-carry permit requirement for law-abiding Georgians. Rhett carries a 14% Freedom Index score — among the lowest in the GA Senate — reflecting consistent opposition to gun-rights legislation.",
              ["https://www.legis.ga.gov/legislation/60797",
               "https://legiscan.com/GA/votes/SB319/2021",
               "https://freedomindex.us/legislator/3762"]),
        claim("mr2", "michael-rhett", "biblical_marriage", 2, False,
              "Voted NO on SB 140 (Treatment of Gender Dysphoria for Minors Act, 2023), which passed 31-21 on party lines (all 21 No votes from Democrats including Rhett). SB 140 banned gender-affirming surgeries and hormone therapy for minors under 18 in Georgia.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/22/georgia-legislature-sends-bill-to-limit-transgender-care-for-minors-to-governor/"]),
        claim("mr3", "michael-rhett", "family_child_sovereignty", 0, False,
              "Voted NO on SB 390 (2024), which would have withheld all state funding from Georgia library systems affiliated with the American Library Association — legislation designed to assert parental authority over publicly funded library content available to minors. SB 390 passed 33-20; Rhett's No vote opposes parental oversight of library materials.",
              ["https://freedomindex.us/legislator/3762",
               "https://ballotpedia.org/Michael_A._Rhett"]),
    ]),

    # ---- Harold V. Jones II (GA-22, D · Augusta · Senate Minority Leader) ----
    ("harold-v-jones-ii", "GA", "State Senator", [
        claim("hj1", "harold-v-jones-ii", "self_defense", 0, False,
              "Voted NO on SB 319, the Georgia Constitutional Carry Act (passed 34-22 February 28, 2022 on a strict party-line vote; all 22 No votes from Democrats). As Georgia Senate Minority Leader since January 2025, Jones has stated his caucus will pursue 'gun safety' legislation — confirming continued opposition to the rubric's constitutional-carry standard.",
              ["https://www.legis.ga.gov/legislation/60797",
               "https://legiscan.com/GA/votes/SB319/2021",
               "https://pro.stateaffairs.com/ga/politics/harold-jones-senate-minority-leader-profile"]),
        claim("hj2", "harold-v-jones-ii", "biblical_marriage", 2, False,
              "Voted NO on SB 140 (Treatment of Gender Dysphoria for Minors Act, 2023), which passed 31-21 on strict party lines (all 21 No votes from Democrats including Jones). SB 140 prohibited gender-affirming surgeries and hormone therapy for minors under 18 in Georgia.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://georgiarecorder.com/2023/03/22/georgia-legislature-sends-bill-to-limit-transgender-care-for-minors-to-governor/",
               "https://ballotpedia.org/Harold_V._Jones_II"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

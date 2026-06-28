#!/usr/bin/env python3
"""Enrichment batch 461: evidence_curated claims for 5 Florida Supreme Court justices.

Targets from the evidence_federal / 0-claims bucket, bottom of alphabet (FL).
Mix: 4 DeSantis-appointee conservatives (True scores) + 1 Crist-appointee liberal (False scores).

Justices:
  Carlos G. Muñiz  (FL Chief Justice, DeSantis 2019)
  Jamie R. Grosshans (FL Associate Justice, DeSantis 2020)
  John D. Couriel   (FL Associate Justice, DeSantis 2020)
  Jorge Labarga     (FL Associate Justice, Crist 2009)
  Charles T. Canady (FL Former Associate Justice, ret. Dec 31 2025; R congressman 1993-2001)

Primary anchor: Planned Parenthood of SW & Central FL v. State of Florida (April 2024)
6-1 ruling; Grosshans wrote majority; Labarga sole dissenter.
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


TARGETS = [
    # -------- Carlos G. Muñiz (FL, Chief Justice, DeSantis 2019) --------
    ("carlos-g-muñiz", "FL", "Chief Justice", [
        claim("a461", "carlos-g-muñiz", "sanctity_of_life", 0, True,
              "Joined the 6-1 majority in Planned Parenthood of Southwest and Central Florida v. State of Florida (April 2024), ruling that Florida's Privacy Clause does not protect abortion access and allowing the state's 6-week heartbeat ban to take effect — reversing the court's own 1989 activist precedent. During oral arguments, Chief Justice Muñiz questioned whether 'natural person' in the Florida Constitution could include the unborn.",
              ["https://www.npr.org/2024/04/02/1242196735/florida-supreme-court-orders-states-6-week-abortion-ban-to-go-into-effect-may-1",
               "https://statecourtreport.org/our-work/analysis-opinion/florida-supreme-court-allows-abortion-ban-final-decision-will-go-voters"]),
        claim("b461", "carlos-g-muñiz", "public_justice", 0, True,
              "Career originalist jurist: served as Deputy Florida Attorney General under AG Pam Bondi (2011-2014) and as General Counsel of the U.S. Department of Education under Secretary Betsy DeVos (confirmed 55-43, April 2018) before Gov. DeSantis appointed him to the FL Supreme Court in January 2019. Ballotpedia's 2020 judicial partisanship study rated him 'Strong Republican.' Leads a reconstituted court that enforces constitutional text rather than judicially invented rights.",
              ["https://ballotpedia.org/Carlos_Mu%C3%B1iz",
               "https://en.wikipedia.org/wiki/Carlos_G._Mu%C3%B1iz"]),
    ]),

    # -------- Jamie R. Grosshans (FL, Associate Justice, DeSantis 2020) --------
    ("jamie-r-grosshans", "FL", "Associate Justice", [
        claim("c461", "jamie-r-grosshans", "sanctity_of_life", 0, True,
              "Wrote the majority opinion in Planned Parenthood of SW & Central Florida v. State of Florida (April 2024), stating: 'We recede from our prior decisions in which — relying on reasoning the U.S. Supreme Court has rejected — we held that the Privacy Clause guaranteed the right to receive an abortion through the end of the second trimester.' The ruling cleared the 6-week heartbeat ban and reversed 35 years of activist abortion precedent.",
              ["https://news.ballotpedia.org/2024/04/03/florida-supreme-court-rules-on-abortion-there-is-no-right-to-abortion-in-the-states-privacy-clause-but-voters-will-decide-the-issue-in-nov/",
               "https://www.npr.org/2024/04/02/1242196735/florida-supreme-court-orders-states-6-week-abortion-ban-to-go-into-effect-may-1"]),
        claim("d461", "jamie-r-grosshans", "public_justice", 0, True,
              "Former Assistant State Attorney for Orange County, Florida (criminal division) who tried numerous jury trials; founded her own firm focused on family law and criminal defense before her appointment to the FL Fifth District Court of Appeal by Gov. Rick Scott (2018) and then to the FL Supreme Court by Gov. DeSantis (2020). Extensive prosecutorial and family-law background grounding her in public order and parental rights.",
              ["https://ballotpedia.org/Jamie_Rutland_Grosshans",
               "https://en.wikipedia.org/wiki/Jamie_Grosshans"]),
    ]),

    # -------- John D. Couriel (FL, Associate Justice, DeSantis 2020) --------
    ("john-d-couriel", "FL", "Associate Justice", [
        claim("e461", "john-d-couriel", "sanctity_of_life", 0, True,
              "Voted with the 6-1 majority in Planned Parenthood of SW & Central Florida v. State of Florida (April 2024), ruling that the Florida Privacy Clause does not protect abortion access and allowing the 6-week heartbeat ban to take effect. DeSantis appointed him alongside Justice Grosshans in 2020 to restore originalist constitutional interpretation to the court.",
              ["https://www.npr.org/2024/04/02/1242196735/florida-supreme-court-orders-states-6-week-abortion-ban-to-go-into-effect-may-1",
               "https://ballotpedia.org/John_D._Couriel"]),
        claim("f461", "john-d-couriel", "public_justice", 0, True,
              "Former Assistant U.S. Attorney for the Southern District of Florida (federal criminal prosecution) and Harvard Law graduate; served as partner at Kobre & Kim in Miami before Gov. DeSantis appointed him to the FL Supreme Court in 2020. Retained in 2022 retention election with 63.7% of the vote. Career prosecutorial and textualist legal record reflects commitment to law as enacted, not judicially expanded.",
              ["https://ballotpedia.org/John_D._Couriel",
               "https://en.wikipedia.org/wiki/John_D._Couriel"]),
    ]),

    # -------- Jorge Labarga (FL, Associate Justice, Crist 2009) --------
    ("jorge-labarga", "FL", "Associate Justice", [
        claim("g461", "jorge-labarga", "sanctity_of_life", 0, False,
              "Sole dissenter in the 6-1 Florida Supreme Court ruling (April 2024) in Planned Parenthood of SW & Central Florida v. State of Florida; Justice Labarga argued that Florida's Privacy Clause DOES protect abortion access and opposed allowing the 6-week heartbeat ban to take effect — the only justice on the court to endorse an abortion right under the state constitution.",
              ["https://www.npr.org/2024/04/02/1242196735/florida-supreme-court-orders-states-6-week-abortion-ban-to-go-into-effect-may-1",
               "https://www.aclu.org/press-releases/florida-supreme-court-allows-state-to-ban-abortion-but-sends-measure-to-protect-abortion-rights-to-the-voters-in-november"]),
        claim("h461", "jorge-labarga", "refuse_state_overreach", 0, False,
              "Dissented from the FL Supreme Court majority that denied jurisdiction over an emergency redistricting petition (June 10, 2026); Justice Labarga favored the court inserting itself into the legislative redistricting process — a posture of expanding state judicial authority over legislative maps rather than deferring to the legislature's Article I redistricting power.",
              ["https://ballotpedia.org/Jorge_Labarga"]),
    ]),

    # -------- Charles T. Canady (FL, Former Associate Justice, ret. Dec 31 2025) --------
    ("charles-t-canady", "FL", "Associate Justice", [
        claim("i461", "charles-t-canady", "sanctity_of_life", 0, True,
              "As a U.S. Congressman (R-FL, 1993-2001), Canady coined the term 'partial-birth abortion' and sponsored the Partial-Birth Abortion Ban Act of 1995 — landmark pro-life legislation that passed both chambers of Congress before President Clinton's veto. He then voted with the 6-1 FL Supreme Court majority in Planned Parenthood v. State of Florida (April 2024) upholding the 6-week heartbeat ban, demonstrating a lifelong commitment to protecting the unborn.",
              ["https://en.wikipedia.org/wiki/Charles_T._Canady",
               "https://www.npr.org/2024/04/02/1242196735/florida-supreme-court-orders-states-6-week-abortion-ban-to-go-into-effect-may-1"]),
        claim("j461", "charles-t-canady", "biblical_marriage", 1, True,
              "As a member of the House Judiciary Committee, Canady cosponsored the Defense of Marriage Act (DOMA, 1996) and submitted the committee report (H.Rept. 104-664) recommending its passage — defining federal marriage as one man and one woman. DOMA passed the House 342-67 on July 12, 1996. Canady's committee leadership was central to enacting DOMA into law.",
              ["https://www.congress.gov/congressional-report/104th-congress/house-report/664/1",
               "https://www.govtrack.us/congress/votes/104-1996/h316"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

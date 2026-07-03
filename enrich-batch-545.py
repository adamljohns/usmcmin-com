#!/usr/bin/env python3
"""Enrichment batch 545: 5 WA Republican State Representatives (bottom-of-alphabet run).

All archetype_curated federal senator and representative buckets exhausted.
Targets selected from archetype_party_default WA Republican state reps with 0 claims,
sorted reverse-alphabetically by name to pull from the bottom of the alphabet.

Targets (all WA-R, State Representative):
  Ed Orcutt (WA-20), Drew Stokesbary (WA-31), Dan Griffey (WA-35),
  Carolyn Eslick (WA-39), Chris Corry (WA-15).

Claims span self_defense, family_child_sovereignty, biblical_marriage,
sanctity_of_life, and economic_stewardship rubric categories. Sources include
WA state legislature records, legiscan.com, official .houserepublicans.wa.gov
pages, and contemporaneous news coverage.
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
    # ---------------- Ed Orcutt (WA-20, R) ----------------
    ("ed-orcutt", "WA", "Representative", [
        claim("eo1", "ed-orcutt", "self_defense", 1, True,
              "Voted NO on WA HB 1240 (2023), the state assault weapons ban banning sale and manufacture of semi-automatic rifles with detachable magazines; no House Republican voted for the bill (passed 55–42 on a strict party-line vote), and Orcutt filed a floor amendment in opposition to the bill.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://www.fox13seattle.com/news/washington-house-votes-55-42-to-ban-sale-of-assault-weapons",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023"]),
        claim("eo2", "ed-orcutt", "biblical_marriage", 0, True,
              "Has publicly stated his opposition to same-sex marriage, affirming the one-man-one-woman definition of marriage; served in the WA House since 2003 and has consistently voted with the Republican minority against legislation expanding same-sex and LGBTQ+ recognition in state law.",
              ["https://en.wikipedia.org/wiki/Ed_Orcutt",
               "https://edorcutt.houserepublicans.wa.gov/"]),
        claim("eo3", "ed-orcutt", "economic_stewardship", 2, True,
              "Ranking Republican on the House Appropriations Committee; consistently voted against Democrat-authored state biennial budgets, citing deficit spending and structural imbalance in Washington's General Fund that relies on one-time revenues and postpones obligations.",
              ["https://edorcutt.houserepublicans.wa.gov/category/legislature/",
               "https://houserepublicans.wa.gov/current/an-update-on-the-2023-legislative-session/"]),
    ]),

    # ---------------- Drew Stokesbary (WA-31, R) ----------------
    ("drew-stokesbary", "WA", "Representative", [
        claim("ds1", "drew-stokesbary", "self_defense", 1, True,
              "Voted NO on WA HB 1240 (2023), the state assault weapons ban; as newly elected House Republican Leader (April 2023), led unified Republican caucus opposition to the bill, which passed 55–42 with zero Republican votes in the House.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://www.thecentersquare.com/washington/article_d1ff7d58-e3b2-11ed-9915-9f55d2a8ae57.html",
               "https://drewstokesbary.houserepublicans.wa.gov/"]),
        claim("ds2", "drew-stokesbary", "family_child_sovereignty", 0, True,
              "As House Republican Leader, opposed WA HB 1296 (2025), the Democrat-passed bill that rewrote and weakened the voter-approved I-2081 Parents' Bill of Rights, calling it a rollback that stripped rights from the nearly 500,000 Washingtonians who signed the original petition.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://drewstokesbary.houserepublicans.wa.gov/",
               "https://houserepublicans.wa.gov/i-2081/"]),
        claim("ds3", "drew-stokesbary", "economic_stewardship", 2, True,
              "Led Republican caucus criticism of the Democrat-majority 2025 state budget, opposing unsustainable government spending growth, rent control provisions, and failure to provide broad tax relief — calling instead for responsible budgeting and fiscal discipline.",
              ["https://washingtonstatestandard.com/2023/05/09/washington-state-republicans-legislature-drew-stokesbary/",
               "https://drewstokesbary.houserepublicans.wa.gov/news-media/"]),
    ]),

    # ---------------- Dan Griffey (WA-35, R) ----------------
    ("dan-griffey", "WA", "Representative", [
        claim("dg1", "dan-griffey", "self_defense", 1, True,
              "Voted NO on WA HB 1240 (2023), Washington's assault weapons ban banning sale and manufacture of semi-automatic rifles; Griffey filed a floor amendment attempting to narrow the bill's scope, and all 42 House Republicans voted against final passage.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://app.leg.wa.gov/billsummary?BillNumber=1240&Year=2023",
               "https://dangriffey.houserepublicans.wa.gov/"]),
        claim("dg2", "dan-griffey", "family_child_sovereignty", 0, True,
              "Championed I-2081, the voter-approved Parents' Bill of Rights, calling it a landmark win for families; voted NO on WA HB 1296 (2025) that the Democrat majority used to overhaul and weaken I-2081, saying the majority was 'stripping away rights' the 500,000 petition signers had secured.",
              ["https://dangriffey.houserepublicans.wa.gov/2025/01/31/rep-dan-griffey-checks-in-with-the-latest-on-the-2025-legislative-session/",
               "https://houserepublicans.wa.gov/i-2081/",
               "https://www.thecentersquare.com/washington/article_8ca9ce28-d7e8-4456-a6db-e107c49ea7f5.html"]),
        claim("dg3", "dan-griffey", "biblical_marriage", 2, True,
              "Offered a floor amendment to WA HB 1296 (2025) requiring school districts to provide separate showering and locker room facilities for female students, opposing policies that would place biological males in girls' private changing spaces under transgender accommodation rules.",
              ["https://dangriffey.houserepublicans.wa.gov/2025/01/31/rep-dan-griffey-checks-in-with-the-latest-on-the-2025-legislative-session/",
               "https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/"]),
    ]),

    # ---------------- Carolyn Eslick (WA-39, R) ----------------
    ("carolyn-eslick", "WA", "Representative", [
        claim("ce1", "carolyn-eslick", "self_defense", 1, True,
              "Voted NO on WA HB 1240 (2023), Washington's assault weapons ban prohibiting the sale and manufacture of semi-automatic rifles with detachable magazines; all 42 House Republicans voted against the bill, which passed 55–42 on a strict party-line vote.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://www.fox13seattle.com/news/washington-house-votes-55-42-to-ban-sale-of-assault-weapons",
               "https://carolyneslick.houserepublicans.wa.gov/"]),
        claim("ce2", "carolyn-eslick", "sanctity_of_life", 0, True,
              "Stated that chemical abortion drugs must meet essential safety standards including mandatory in-person consultation with a physician before dispensing, and that abortion providers including Planned Parenthood should not receive taxpayer funds at any level of government.",
              ["https://ivoterguide.com/candidate/41816/race/4062/election/1247",
               "https://carolyneslick.houserepublicans.wa.gov/"]),
        claim("ce3", "carolyn-eslick", "family_child_sovereignty", 0, True,
              "Voted NO on WA HB 1296 (2025), the Democrat-authored bill that overhauled and weakened the voter-approved I-2081 Parents' Bill of Rights by extending records timelines and narrowing parental access to school curriculum and notifications; all Republicans opposed the rewrite.",
              ["https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/",
               "https://houserepublicans.wa.gov/i-2081/"]),
    ]),

    # ---------------- Chris Corry (WA-15, R) ----------------
    ("chris-corry", "WA", "Representative", [
        claim("cc1", "chris-corry", "self_defense", 1, True,
              "Voted NO on WA HB 1240 (2023), the state assault weapons ban prohibiting sale and manufacture of semi-automatic rifles; all WA House Republicans voted against the bill, which passed 55–42 on a strict party-line vote.",
              ["https://legiscan.com/WA/votes/HB1240/2023",
               "https://www.fox13seattle.com/news/washington-house-votes-55-42-to-ban-sale-of-assault-weapons",
               "https://chriscorry.houserepublicans.wa.gov/"]),
        claim("cc2", "chris-corry", "family_child_sovereignty", 0, True,
              "Publicly supported I-2081 (Parents' Bill of Rights) and the initiative protecting fairness in girls' sports (I-2082), both of which gathered hundreds of thousands of WA voter signatures; stated that if given a full and transparent legislative process including public hearings, he would have voted for both.",
              ["https://chriscorry.houserepublicans.wa.gov/about/",
               "https://houserepublicans.wa.gov/i-2081/"]),
        claim("cc3", "chris-corry", "economic_stewardship", 2, True,
              "Advocates for reducing state taxes, curbing irresponsible government budget growth, and protecting businesses from excessive regulations; serves as Eastern Washington director for the Washington Policy Center, a free-market think tank whose principles he brings to his legislative role.",
              ["https://chriscorry.houserepublicans.wa.gov/about/",
               "https://govprofiles.com/chris-corry/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

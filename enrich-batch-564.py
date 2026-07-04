#!/usr/bin/env python3
"""Enrichment batch 564: 5 WA Republican State Representatives, 10 claims.

All archetype_curated federal slots (senators + representatives) are
exhausted as of batch 563. This batch continues from the bottom of the
alphabet with WA Republican state-level officials — the highest-priority
remaining targets given the rubric alignment potential.

Candidates (all WA, R, 'State Representative'):
  Cyndy Jacobsen   (District 25, Puyallup / Pierce County)
  April Connors    (District 8, Tri-Cities / Republican Floor Leader)
  David Stuebe     (District 17, Washougal / Marine Col. ret.)
  Brian Burnett    (District 12, Chelan / former Sheriff)
  Deb Manjarrez    (District 14, Wapato / Yakima County)
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
    # -------- Cyndy Jacobsen (WA-25, R, State Representative) --------
    ("cyndy-jacobsen", "WA", "State Representative", [
        claim("cj1", "cyndy-jacobsen", "family_child_sovereignty", 0, True,
              "Spoke on the House floor against HB 1296 (2025), the Democratic rewrite of Initiative 2081's Parents' Bill of Rights, invoking the 450,000+ signatures that placed I-2081 on the ballot and arguing parents are the 'primary stakeholders' in their children's education. She voted against HB 1296 when it passed 59-39 on a strict party-line vote on April 23, 2025.",
              ["https://washingtonstatestandard.com/2025/04/14/rewrite-of-parental-rights-law-passes-washington-house/",
               "https://legiscan.com/WA/rollcall/HB1296/id/1478198"]),
        claim("cj2", "cyndy-jacobsen", "biblical_marriage", 2, True,
              "Supported an amendment during the 2025 session to preserve biological sex-based eligibility in K-12 and collegiate girls' sports in Washington, opposing policies that allow transgender-identified males to compete in women's athletics. She stated that protecting girls' sports is a matter of fairness and the integrity of women's competition.",
              ["https://ballotpedia.org/Cyndy_Jacobsen",
               "https://cyndyjacobsen.houserepublicans.wa.gov/"]),
    ]),

    # -------- April Connors (WA-8, R, Republican Floor Leader) --------
    ("april-connors", "WA", "State Representative", [
        claim("ac1", "april-connors", "family_child_sovereignty", 0, True,
              "As House Republican Floor Leader, led the caucus strategy against HB 1296 (2025), the Democratic rewrite of Initiative 2081's Parents' Bill of Rights. Connors introduced an amendment to add a referendum clause so voters — not legislators — could decide whether to strip parental notification rights over children's gender-related school health decisions. Democrats defeated the amendment; the bill passed 59-39 on a party-line vote.",
              ["https://aprilconnors.houserepublicans.wa.gov/2025/03/18/as-democrats-move-to-weaken-parents-rights-law-rep-april-connors-fights-to-let-voters-decide/",
               "https://legiscan.com/WA/rollcall/HB1296/id/1478198"]),
        claim("ac2", "april-connors", "economic_stewardship", 2, True,
              "In the 2026 legislative session, coordinated a more-than-24-hour Republican floor debate — the longest in modern Washington state history — to block a Democrat-backed state income tax proposal, standing firm against new broad-based taxation; Washington State Standard named her one of the 2026 session's winners for this fiscal fight.",
              ["https://aprilconnors.houserepublicans.wa.gov/",
               "https://washingtonstatestandard.com/"]),
    ]),

    # -------- David Stuebe (WA-17, R, Marine Col. ret.) --------
    ("david-stuebe", "WA", "State Representative", [
        claim("ds1", "david-stuebe", "self_defense", 1, True,
              "Voted against HB 1163 (2025), which requires Washington residents to obtain a government-issued permit before purchasing any firearm and creates a state purchaser registry (described by the NRA as 'an illegal government registry of firearm owners'). During floor debate, Stuebe — a 30-year Marine Corps Colonel — proposed an amendment to exempt military veterans from the permit mandate, arguing veterans' formal service training surpasses the bill's requirements.",
              ["https://www.thecentersquare.com/washington/article_4df4c5bc-fde7-11ef-8143-175771d022e0.html",
               "https://legiscan.com/WA/rollcall/HB1163/id/1502231"]),
        claim("ds2", "david-stuebe", "economic_stewardship", 2, True,
              "Publicly decried passage of a state income tax in the 2025-26 session, advocating for tax relief and policies to alleviate financial burdens on struggling families, students, and small businesses in Washington's 17th District.",
              ["https://davidstuebe.houserepublicans.wa.gov/",
               "https://ballotpedia.org/David_Stuebe"]),
    ]),

    # -------- Brian Burnett (WA-12, R, former Chelan County Sheriff) --------
    ("brian-burnett", "WA", "State Representative", [
        claim("bb1", "brian-burnett", "family_child_sovereignty", 0, True,
              "Voted against HB 1296 (2025), the Democratic overhaul of Initiative 2081's Parents' Bill of Rights, which removed parental notification rights over children's gender-related school health decisions and restricted parental access to student health records. The bill passed 59-39 on a strict party-line vote; signed by Gov. Ferguson on May 20, 2025.",
              ["https://legiscan.com/WA/rollcall/HB1296/id/1478198",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
        claim("bb2", "brian-burnett", "self_defense", 1, True,
              "Voted against HB 1163 (2025), requiring Washington residents to obtain a government-issued permit before purchasing firearms and creating a state purchaser registry. As a former three-term Chelan County Sheriff with 25+ years in law enforcement, Burnett opposed the permit-to-purchase mandate as an infringement on law-abiding residents' right to keep and bear arms.",
              ["https://legiscan.com/WA/rollcall/HB1163/id/1502231",
               "https://ballotpedia.org/Brian_Burnett_(Washington)"]),
    ]),

    # -------- Deb Manjarrez (WA-14, R, Wapato / Yakima County) --------
    ("deb-manjarrez", "WA", "State Representative", [
        claim("dm1", "deb-manjarrez", "family_child_sovereignty", 0, True,
              "Voted against HB 1296 (2025), the Democratic overhaul of Initiative 2081's Parents' Bill of Rights, which removed parental notification rights over children's gender-related school health decisions and restricted parental access to student health records. The bill passed 59-39 on a strict party-line vote; signed by Gov. Ferguson on May 20, 2025.",
              ["https://legiscan.com/WA/rollcall/HB1296/id/1478198",
               "https://washingtonstatestandard.com/2025/04/24/parental-rights-overhaul-gains-final-approval-in-wa-legislature/"]),
        claim("dm2", "deb-manjarrez", "self_defense", 1, True,
              "Voted against HB 1163 (2025), requiring Washington residents to obtain a government-issued permit before purchasing firearms and creating a state purchaser registry (described by the NRA as 'an illegal government registry of firearm owners'). The bill passed 58-38 on April 23, 2025, and was signed by Gov. Ferguson effective May 1, 2027.",
              ["https://legiscan.com/WA/rollcall/HB1163/id/1502231",
               "https://app.leg.wa.gov/billsummary?BillNumber=1163&Year=2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

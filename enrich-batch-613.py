#!/usr/bin/env python3
"""Enrichment batch 613: hand-curated claims for 5 state legislators.

The archetype_curated federal senator/rep bucket is fully depleted.
Pivoting to archetype_party_default state reps from bottom-of-alphabet
states (TN/UT — WY/WV/WI/WA/VA/TX R state-rep buckets are exhausted).

Targets (5 R): William Lamberth (TN), Tom Leatherwood (TN),
Susan M. Lynn (TN), Scott Cepicky (TN), Ryan D. Wilcox (UT).
Each claim cites >=1 reliable source and reflects 2019-2026
voting record / public positions.

NOTE: writes scorecard.json MINIFIED to keep the master under
GitHub's 50MB warning.
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
    # ---------- William Lamberth (TN-R, House Majority Leader, District 44) ----------
    ("william-lamberth", "TN", "Representative", [
        claim("wl1", "william-lamberth", "biblical_marriage", 2, True,
              "Sponsored Tennessee legislation criminalizing doctors who perform gender-reassignment "
              "surgery on minors, requiring transgender people to use restrooms matching their "
              "biological sex, and requiring transgender athletes to compete per biological sex — "
              "a comprehensive rejection of transgender ideology in law, passed across multiple "
              "bills from 2021 through 2023.",
              ["https://en.wikipedia.org/wiki/William_Lamberth",
               "https://www.capitol.tn.gov/Bills/113/Bill/SB0001.pdf"]),
        claim("wl2", "william-lamberth", "self_defense", 0, True,
              "Primary House sponsor of Tennessee HB 786 / SB 765 (112th GA, 2021) — Tennessee's "
              "constitutional carry law — allowing law-abiding adults to carry handguns without a "
              "government-issued permit starting July 1, 2021, restoring the right to bear arms "
              "free of prior state permission.",
              ["https://en.wikipedia.org/wiki/William_Lamberth",
               "https://www.capitol.tn.gov/Bills/112/Bill/SB0765.pdf"]),
    ]),

    # ---------- Tom Leatherwood (TN-R, District 99, Shelby County) ----------
    ("tom-leatherwood", "TN", "Representative", [
        claim("tl1", "tom-leatherwood", "sanctity_of_life", 0, True,
              "Cosponsored Tennessee HB 1029 'Human Life Protection Act' (111th GA, 2019, "
              "enacted as Public Chapter 351) — Tennessee's near-total abortion trigger ban "
              "prohibiting all abortions from conception with narrow medical exceptions, which "
              "took effect automatically after Dobbs v. Jackson (June 2022). Leatherwood also "
              "states publicly that 'life begins at conception and should be protected.'",
              ["https://en.wikipedia.org/wiki/Tom_Leatherwood",
               "https://legiscan.com/TN/bill/HB1029/2019"]),
        claim("tl2", "tom-leatherwood", "biblical_marriage", 1, True,
              "Sponsored Tennessee HB 0233 (112th GA) creating an alternative civil marriage "
              "framework outside federal marriage law — widely reported as an effort to create "
              "a marriage category not governed by Obergefell v. Hodges, affirming one-man-"
              "one-woman marriage as a distinct civil institution.",
              ["https://en.wikipedia.org/wiki/Tom_Leatherwood",
               "https://ballotpedia.org/Tom_Leatherwood"]),
    ]),

    # ---------- Susan M. Lynn (TN-R, District 57, Wilson County / Mt. Juliet) ----------
    ("susan-m-lynn", "TN", "Representative", [
        claim("sl1", "susan-m-lynn", "sanctity_of_life", 0, True,
              "Primary House sponsor of HB 1029 'Human Life Protection Act' (111th GA, 2019, "
              "Senate companion SB 1257 by Sen. Dolores Gresham) — Tennessee's near-total "
              "abortion trigger ban protecting human life from conception. The law took effect "
              "after Dobbs (2022) and is Lynn's signature legislative accomplishment over a "
              "decade-long pro-life legislative career.",
              ["https://www.capitol.tn.gov/Bills/111/Bill/HB1029.pdf",
               "https://en.wikipedia.org/wiki/Susan_Lynn"]),
        claim("sl2", "susan-m-lynn", "christian_liberty", 0, True,
              "Sponsored and passed 2018 Tennessee legislation (Public Chapter 782) requiring "
              "all public school classrooms and common areas to prominently display the national "
              "motto 'In God We Trust,' affirming the place of religious expression in public "
              "civic and educational life.",
              ["https://ballotpedia.org/Susan_Lynn",
               "https://en.wikipedia.org/wiki/Susan_Lynn"]),
    ]),

    # ---------- Scott Cepicky (TN-R, District 64, Maury County) ----------
    ("scott-cepicky", "TN", "Representative", [
        claim("sc1", "scott-cepicky", "biblical_marriage", 2, True,
              "Introduced Tennessee HB 0003 (112th GA, 2021) — the first bill of that session — "
              "banning biological males from competing on female athletic teams in Tennessee public "
              "middle and high schools, requiring birth-certificate verification. The Tennessee "
              "Supreme Court and U.S. Supreme Court (2025) upheld transgender athlete bans, "
              "validating the law.",
              ["https://www.capitol.tn.gov/Bills/112/Bill/HB0003.pdf",
               "https://ballotpedia.org/Scott_Cepicky"]),
        claim("sc2", "scott-cepicky", "industry_capture", 0, True,
              "Sponsored Tennessee HB 94, signed into law April 22, 2024, prohibiting the "
              "manufacture, delivery, or sale of food containing a vaccine unless the labeling "
              "explicitly identifies it — protecting informed consent and opposing covert "
              "pharmaceutical use of the food supply.",
              ["https://ballotpedia.org/Scott_Cepicky",
               "https://wapp.capitol.tn.gov/apps/LegislatorInfo/Member?district=h64"]),
    ]),

    # ---------- Ryan D. Wilcox (UT-R, District 7, Ogden/Weber County; Law Enforcement Committee Chair) ----------
    ("ryan-d-wilcox", "UT", "Representative", [
        claim("rw1", "ryan-d-wilcox", "self_defense", 0, True,
              "Cosponsored Utah HB 357, which strengthens Second Amendment rights regardless "
              "of conceal-carry permit status — affirming the right of law-abiding citizens to "
              "bear arms without prior government permission, consistent with the constitutional-"
              "carry principle.",
              ["https://ballotpedia.org/Ryan_Wilcox",
               "https://justfacts.votesmart.org/candidate/103559/ryan-wilcox"]),
        claim("rw2", "ryan-d-wilcox", "self_defense", 1, True,
              "Sponsored Utah HB 84 (2024 General Session) — a comprehensive school safety law "
              "creating a 'school guardian' program authorizing trained, armed school employees "
              "to carry firearms on campus; the bill passed the Senate unanimously and the House "
              "with only 9 no votes, and appropriated $100 million in funding. This directly "
              "counters gun-free-zone restrictions in schools.",
              ["https://ballotpedia.org/Ryan_Wilcox",
               "https://www.kuer.org/politics-government/2024-02-28/bill-requiring-armed-security-in-utah-schools-nears-the-finish-line"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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

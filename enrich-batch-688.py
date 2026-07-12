#!/usr/bin/env python3
"""Enrichment batch 688: hand-curated claims for 5 sitting U.S. Representatives (OR + PA).

Targets sitting Democratic U.S. Representatives from Oregon and Pennsylvania with only
3 existing claims, taken from the bottom of the alphabet (OR, PA) per the
collision-avoidance protocol. Adds 2 new claims each spanning distinct rubric
categories (biblical_marriage, economic_stewardship, election_integrity).

All votes are party-line House roll calls sourced from clerk.house.gov and govtrack.us.

Candidates: Brendan Boyle (PA), Chrissy Houlahan (PA), Madeleine Dean (PA),
            Andrea Salinas (OR), Maxine Dexter (OR).

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ------------ Brendan Boyle (PA, US Representative) ------------
    ("brendan-boyle", "PA", "Representative", [
        claim("bb4", "brendan-boyle", "biblical_marriage", 0, False,
              "Voted YEA on the Respect for Marriage Act (H.R. 8404 / S. 4556; House Roll Call #588, December 8, 2022, passed 258-169), codifying federal recognition of same-sex and interracial marriages in statute and requiring states to recognize marriages performed lawfully in other states — directly rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://clerk.house.gov/Votes/2022588",
               "https://www.govtrack.us/congress/votes/117-2022/h588",
               "https://www.congress.gov/bill/117th-congress/senate-bill/4556"]),
        claim("bb5", "brendan-boyle", "economic_stewardship", 0, False,
              "Voted NAY on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which would have prohibited the Federal Reserve from issuing a retail central bank digital currency directly to individuals. Boyle joined the unanimous Democratic caucus in opposing the bill, effectively blocking a statutory bar on a government-controlled digital dollar.",
              ["https://clerk.house.gov/Votes/2025201",
               "https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
    ]),

    # ------------ Chrissy Houlahan (PA, US Representative) ------------
    ("chrissy-houlahan", "PA", "Representative", [
        claim("ch4", "chrissy-houlahan", "election_integrity", 0, False,
              "Voted NAY on H.R. 22, the SAVE Act (Safeguard American Voter Eligibility Act; House Roll Call #102, April 10, 2025, passed 220-208), which would have required documentary proof of U.S. citizenship when registering to vote in federal elections. Houlahan joined the unanimous Democratic caucus in opposing the bill.",
              ["https://clerk.house.gov/Votes/2025102",
               "https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("ch5", "chrissy-houlahan", "economic_stewardship", 0, False,
              "Voted NAY on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which would have prohibited the Federal Reserve from issuing a retail central bank digital currency directly to individuals. Houlahan voted with the unanimous Democratic caucus against the statutory block on a government-controlled digital dollar.",
              ["https://clerk.house.gov/Votes/2025201",
               "https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
    ]),

    # ------------ Madeleine Dean (PA, US Representative) ------------
    ("madeleine-dean", "PA", "Representative", [
        claim("md4", "madeleine-dean", "election_integrity", 0, False,
              "Voted NAY on H.R. 22, the SAVE Act (Safeguard American Voter Eligibility Act; House Roll Call #102, April 10, 2025, passed 220-208), which would have required documentary proof of U.S. citizenship when registering to vote in federal elections. Dean joined the unanimous Democratic caucus in opposing the bill.",
              ["https://clerk.house.gov/Votes/2025102",
               "https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("md5", "madeleine-dean", "economic_stewardship", 0, False,
              "Voted NAY on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which would have prohibited the Federal Reserve from issuing a retail central bank digital currency directly to individuals. Dean voted with the unanimous Democratic caucus against the statutory bar on a government-controlled digital dollar.",
              ["https://clerk.house.gov/Votes/2025201",
               "https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
    ]),

    # ------------ Andrea Salinas (OR, US Representative) ------------
    ("andrea-salinas", "OR", "Representative", [
        claim("as4", "andrea-salinas", "biblical_marriage", 2, False,
              "Voted NAY on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206), which amends Title IX to define sex as 'based solely on a person's reproductive biology and genetics at birth' and prohibits biological males from competing in women's and girls' athletic programs at federally funded schools. Salinas joined the unanimous Democratic caucus in opposing the bill.",
              ["https://clerk.house.gov/Votes/202512",
               "https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
        claim("as5", "andrea-salinas", "economic_stewardship", 0, False,
              "Voted NAY on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which would have prohibited the Federal Reserve from issuing a retail central bank digital currency directly to individuals. Salinas voted with the unanimous Democratic caucus against the statutory block on a government-controlled digital dollar.",
              ["https://clerk.house.gov/Votes/2025201",
               "https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
    ]),

    # ------------ Maxine Dexter (OR, US Representative) ------------
    ("maxine-dexter", "OR", "Representative", [
        claim("md4", "maxine-dexter", "biblical_marriage", 2, False,
              "Voted NAY on H.R. 28, the Protection of Women and Girls in Sports Act (House Roll Call #12, January 14, 2025, passed 218-206), which amends Title IX to define sex as 'based solely on a person's reproductive biology and genetics at birth' and prohibits biological males from competing in women's and girls' athletic programs at federally funded schools. Dexter joined the unanimous Democratic caucus in opposing the bill.",
              ["https://clerk.house.gov/Votes/202512",
               "https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
        claim("md5", "maxine-dexter", "economic_stewardship", 0, False,
              "Voted NAY on H.R. 1919, the Anti-CBDC Surveillance State Act (House Roll Call #201, July 17, 2025, passed 219-210), which would have prohibited the Federal Reserve from issuing a retail central bank digital currency directly to individuals. Dexter voted with the unanimous Democratic caucus against the statutory bar on a government-controlled digital dollar.",
              ["https://clerk.house.gov/Votes/2025201",
               "https://www.govtrack.us/congress/votes/119-2025/h201",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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

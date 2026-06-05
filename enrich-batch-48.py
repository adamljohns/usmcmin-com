#!/usr/bin/env python3
"""Enrichment batch 48: hand-curated claims for 5 U.S. House candidates.

Targets archetype_curated federal representatives with 0 evidence claims,
taken from the bottom of the alphabet (KY, GA, FL, IL, CA) — the
bottom-of-bucket side assigned to the descending loop.

Mix (4 R / 1 R-with-exceptions): Thomas Massie (KY-R), Marjorie Taylor Greene
(GA-R), Anthony Sabatini (FL-R), Joe McGraw (IL-R), Mike Garcia (CA-R).

Each claim cites >=1 reliable source and reflects the 2023-2026 voting record
/ public positions documented in congress.gov, govtrack, GOA, and news coverage.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ---------------- Thomas Massie (KY-R, U.S. Rep KY-04) ----------------
    ("thomas-massie", "KY", "Representative", [
        claim("tm1", "thomas-massie", "sanctity_of_life", 0, True,
              "Co-sponsored H.R.431, the Life at Conception Act (118th Congress, 2023), which would grant full federal personhood from the moment of fertilization with no exceptions. Has maintained a 100% pro-life voting record and publicly stated he believes life begins at conception.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/431/cosponsors",
               "https://massie.house.gov/issues/issue/?IssueID=112043"]),
        claim("tm2", "thomas-massie", "economic_stewardship", 1, True,
              "Introduced H.R.24, the Federal Reserve Transparency Act of 2025 (119th Congress), requiring the Comptroller General to conduct a comprehensive audit of the Federal Reserve Board of Governors and all Federal Reserve banks — a sound-money bill Massie has championed in every Congress since 2012.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/24/text",
               "https://massie.house.gov/news/documentsingle.aspx?DocumentID=395681"]),
        claim("tm3", "thomas-massie", "foreign_policy_restraint", 3, True,
              "AIPAC's super PAC spent over $4 million to defeat Massie in the 2026 KY-04 Republican primary — the most expensive House primary in U.S. history ($32M total) — because Massie never accepted AIPAC or pro-Israel PAC money. AIPAC labeled him 'the most anti-Israel Republican in the House.'",
              ["https://www.axios.com/2026/05/11/thomas-massie-ed-gallrein-kentucky-aipac-trump",
               "https://theintercept.com/2026/05/19/thomas-massie-loses-election-results-trump-aipac-kentucky/"]),
    ]),

    # ------------ Marjorie Taylor Greene (GA-R, U.S. House GA-14) ------------
    ("marjorie-taylor-greene", "GA", "House", [
        claim("mtg1", "marjorie-taylor-greene", "sanctity_of_life", 0, True,
              "Co-sponsored H.R.431, the Life at Conception Act (118th Congress, cosponsored 01/20/2023), which would establish full federal personhood protections from the moment of fertilization under federal law.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/431/cosponsors"]),
        claim("mtg2", "marjorie-taylor-greene", "biblical_marriage", 2, True,
              "Authored H.R.3492, the Protect Children's Innocence Act, which the U.S. House passed in December 2025 — making it a crime to provide puberty blockers, cross-sex hormones, or gender surgeries to minors, directly rejecting transgender ideology in federal law.",
              ["https://www.washingtonpost.com/nation/2025/12/17/marjorie-taylor-greene-trans-care-ban/",
               "https://equality.house.gov/cec-condemns-hr-3492"]),
        claim("mtg3", "marjorie-taylor-greene", "border_immigration", 0, True,
              "Voted YES on H.R.2, the Secure the Border Act of 2023 (passed House 219-213, May 2023), mandating resumed border-wall construction, reinstating the Remain in Mexico policy, and tightening asylum adjudications. Has repeatedly demanded military deployment at the southern border.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://www.timesfreepress.com/news/2023/jan/25/marjorie-taylor-greene-tfp/"]),
    ]),

    # ------------ Anthony Sabatini (FL-R, U.S. Rep FL-11 candidate) ----------
    ("anthony-sabatini-fl-11", "FL", "Representative", [
        claim("as1", "anthony-sabatini-fl-11", "self_defense", 0, True,
              "Introduced constitutional carry (permitless carry) legislation in the Florida House three consecutive sessions (2020, 2021, 2022), each time endorsed by Gun Owners of America; called permit requirements 'paying government to exercise a God-given right.'",
              ["https://www.gunowners.org/fl09022021/",
               "https://mynews13.com/fl/orlando/news/2021/10/08/state-rep--sabatini-pushes-bill-for-no-concealed-weapon-permits"]),
        claim("as2", "anthony-sabatini-fl-11", "border_immigration", 1, True,
              "Has publicly called for a blanket moratorium on immigration to the United States — going beyond enforcement to advocate for stopping all legal immigration — placing him among the most restrictionist voices in the America-First movement.",
              ["https://en.wikipedia.org/wiki/Anthony_Sabatini"]),
    ]),

    # ------------ Joe McGraw (IL-R, U.S. Rep IL-17 candidate) ----------------
    ("joe-mcgraw", "IL", "Representative", [
        claim("jm1", "joe-mcgraw", "border_immigration", 1, True,
              "Campaigned on tightening immigration enforcement, arguing that illegal migrants have become 'a drain on social services, health care, and schools,' and calling for strict border enforcement measures.",
              ["https://qctimes.com/news/local/government-politics/scott-crowl-joe-mcgraw-illinois-17th-congressional-republican-primary/article_b62f7c82-3f2d-5e2c-9972-dbd09b3129e6.html",
               "https://pantagraph.com/news/state-regional/government-politics/retired-judge-joe-mcgraw-to-run-for-congress/article_056fe646-67f7-11ee-8b75-eba34d749635.html"]),
        claim("jm2", "joe-mcgraw", "sanctity_of_life", 0, False,
              "Supports the Dobbs v. Jackson decision returning abortion regulation to states but frames abortion as a 'states' rights' question — not asserting federal life-at-conception personhood — stopping short of the rubric's personhood standard.",
              ["https://pantagraph.com/news/state-regional/government-politics/retired-judge-joe-mcgraw-to-run-for-congress/article_056fe646-67f7-11ee-8b75-eba34d749635.html"]),
    ]),

    # ------------ Mike Garcia (CA-R, U.S. Rep CA-27 candidate) ---------------
    ("mike-garcia", "CA", "Representative", [
        claim("mg1", "mike-garcia", "sanctity_of_life", 0, False,
              "Identifies as 'pro-life with exceptions' for rape, incest, and to save the life of the mother — not a life-at-conception/personhood position; issued a statement reaffirming those exceptions in response to the Dobbs ruling.",
              ["https://mikegarcia.house.gov/news/documentsingle.aspx?DocumentID=1695",
               "https://ivoterguide.com/candidate/48939/race/1256/election/962"]),
        claim("mg2", "mike-garcia", "border_immigration", 3, True,
              "Supports requiring all employers to use the federal E-Verify system to confirm that every employee is legally authorized to work in the United States.",
              ["https://ivoterguide.com/candidate/48939/race/1256/election/962",
               "https://justfacts.votesmart.org/candidate/188664/mike-garcia"]),
        claim("mg3", "mike-garcia", "self_defense", 1, True,
              "States he 'does not support any new restrictions on gun ownership' and believes law-abiding Americans should have the ability to defend themselves and their families — opposing assault-weapons bans, magazine limits, and registry proposals.",
              ["https://justfacts.votesmart.org/candidate/188664/mike-garcia?categoryId=37&type=V,S,R,E,F,P",
               "https://ivoterguide.com/candidate/48939/race/1256/election/962"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

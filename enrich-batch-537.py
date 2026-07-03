#!/usr/bin/env python3
"""Enrichment batch 537: 10 new claims across 5 sitting Wisconsin Republican U.S. House members.

Targets: Bryan Steil (WI-01), Derrick Van Orden (WI-03), Scott Fitzgerald (WI-05),
Glenn Grothman (WI-06), Tom Tiffany (WI-07) — bottom-of-alphabet state (WI) with
evidence_curated confidence and 5 existing claims. Adds 2 distinct new-category
claims per target: economic_stewardship[0] (H.R. 1919 Anti-CBDC Surveillance State
Act, July 17 2025) and biblical_marriage[2] (H.R. 3492 Protect Children's Innocence
Act, December 17 2025). Both votes were party-line Republican yeas.

Sources: congress.gov, govtrack.us, en.wikipedia.org, ballotpedia.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ---------------- Bryan Steil (WI-01, R) ----------------
    ("bryan-steil", "WI", "House", [
        claim("bs537a", "bryan-steil", "economic_stewardship", 0, True,
              "Steil voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual financial accounts — blocking a government-issued digital dollar that would enable real-time surveillance of every citizen's financial transactions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/votes/119-2025/h201"]),
        claim("bs537b", "bryan-steil", "biblical_marriage", 2, True,
              "Steil voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties — up to 10 years imprisonment — for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors. The vote directly rejects the premise that a child's biological sex can or should be chemically or surgically altered.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
    ]),

    # ---------------- Derrick Van Orden (WI-03, R) ----------------
    ("derrick-van-orden", "WI", "House", [
        claim("dvo537a", "derrick-van-orden", "economic_stewardship", 0, True,
              "Van Orden voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual financial accounts — opposing a programmable government digital dollar and defending decentralized money outside direct federal control.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/votes/119-2025/h201"]),
        claim("dvo537b", "derrick-van-orden", "biblical_marriage", 2, True,
              "Van Orden voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — affirming biological sex as immutable in federal law and rejecting gender-ideology medical interventions on children.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
    ]),

    # ---------------- Scott Fitzgerald (WI-05, R) ----------------
    ("scott-fitzgerald", "WI", "House", [
        claim("sf537a", "scott-fitzgerald", "economic_stewardship", 0, True,
              "Fitzgerald voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual accounts — blocking a government-issued digital dollar and preserving financial privacy against federal surveillance infrastructure.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/votes/119-2025/h201"]),
        claim("sf537b", "scott-fitzgerald", "biblical_marriage", 2, True,
              "Fitzgerald voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — protecting children's biological identities and rejecting gender ideology in federal law.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
    ]),

    # ---------------- Glenn Grothman (WI-06, R) ----------------
    ("glenn-grothman", "WI", "House", [
        claim("gg537a", "glenn-grothman", "economic_stewardship", 0, True,
              "Grothman voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual financial accounts — blocking the creation of a government-controlled digital dollar that could enable granular surveillance of citizens' financial activity.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/votes/119-2025/h201"]),
        claim("gg537b", "glenn-grothman", "biblical_marriage", 2, True,
              "Grothman voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — affirming that biological sex is fixed and rejecting the premise that transgender medical interventions on children are permissible.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
    ]),

    # ---------------- Tom Tiffany (WI-07, R) ----------------
    ("tom-tiffany", "WI", "House", [
        claim("tt537a", "tom-tiffany", "economic_stewardship", 0, True,
              "Tiffany voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual accounts — opposing a programmable government digital dollar and defending the monetary privacy of citizens from federal financial surveillance.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/votes/119-2025/h201"]),
        claim("tt537b", "tom-tiffany", "biblical_marriage", 2, True,
              "Tiffany voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — rejecting gender ideology and affirming biological sex as immutable in federal criminal law.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

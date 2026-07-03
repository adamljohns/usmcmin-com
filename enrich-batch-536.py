#!/usr/bin/env python3
"""Enrichment batch 536: 10 new claims across 5 sitting U.S. House members.

Targets: Carol Miller (WV-01, R), Riley Moore (WV-02, R), Rob Wittman (VA-01, R),
Morgan Griffith (VA-09, R), Ben Cline (VA-06, R) — bottom-of-alphabet states
(WV, VA) with evidence_curated confidence and 5–6 existing claims. Adds 2
distinct new-category claims per target: biblical_marriage q2 (H.R. 3492
Protect Children's Innocence Act, Dec 17 2025) and economic_stewardship q0
(H.R. 1919 Anti-CBDC Surveillance State Act, July 17 2025), except Riley Moore
who gets border_immigration q1 instead (CECOT deportation support, April 2025).

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
    # ---------------- Carol Miller (WV-01, R) ----------------
    ("carol-miller", "WV", "Representative", [
        claim("cm536a", "carol-miller", "biblical_marriage", 2, True,
              "Miller voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties — up to 10 years imprisonment — for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors. The vote was party-line, directly rejecting the premise that a child's biological sex can or should be chemically or surgically altered.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
        claim("cm536b", "carol-miller", "economic_stewardship", 0, True,
              "Miller voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual financial accounts — blocking a government-issued digital dollar that would enable real-time surveillance of every citizen's financial transactions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919"]),
    ]),

    # ---------------- Riley Moore (WV-02, R) ----------------
    ("riley-moore", "WV", "Representative", [
        claim("rm536a", "riley-moore", "biblical_marriage", 2, True,
              "Moore cosponsored H.R. 3492, the Protect Children's Innocence Act of 2025, and voted for its passage on December 17, 2025 (House Vote #351, 216–211). The bill establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — rejecting gender ideology as applied to children and affirming that biological sex is immutable.",
              ["https://www.govtrack.us/congress/bills/119/hr3492/cosponsors",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
        claim("rm536b", "riley-moore", "border_immigration", 1, True,
              "In April 2025, Moore traveled to El Salvador to tour the CECOT (Terrorism Confinement Center) detention facility and publicly praised the Trump administration's mass deportation operations, declaring: 'Several inmates were extremely violent criminals recently deported from the U.S. I leave now even more determined to support President Trump's efforts to secure our homeland.' This represents active endorsement of mandatory deportation and removal of unauthorized migrants — the core rubric standard for border_immigration Q1.",
              ["https://en.wikipedia.org/wiki/Riley_Moore",
               "https://ballotpedia.org/Riley_Moore"]),
    ]),

    # ---------------- Rob Wittman (VA-01, R) ----------------
    ("rob-wittman", "VA", "House", [
        claim("rw536a", "rob-wittman", "biblical_marriage", 2, True,
              "Wittman voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — rejecting gender ideology in federal law and protecting children's biological identities.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
        claim("rw536b", "rob-wittman", "economic_stewardship", 0, True,
              "Wittman voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual accounts — blocking a government-issued digital dollar and preserving financial privacy against federal surveillance infrastructure.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919"]),
    ]),

    # ---------------- Morgan Griffith (VA-09, R) ----------------
    ("morgan-griffith", "VA", "House", [
        claim("mg536a", "morgan-griffith", "biblical_marriage", 2, True,
              "Griffith voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — affirming biological sex as fixed in federal law and rejecting gender-ideology medical interventions on children.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
        claim("mg536b", "morgan-griffith", "economic_stewardship", 0, True,
              "Griffith voted for H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress, passed the House 219–210 on July 17, 2025), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual financial accounts — opposing a programmable government digital dollar and defending decentralized money outside direct federal control.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919"]),
    ]),

    # ---------------- Ben Cline (VA-06, R) ----------------
    ("ben-cline", "VA", "House", [
        claim("bc536a", "ben-cline", "economic_stewardship", 0, True,
              "Cline cosponsored H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual financial accounts. The bill passed the House 219–210 on July 17, 2025, with Cline's co-sponsorship on record — blocking a government-issued digital dollar that would enable unprecedented real-time financial surveillance of American citizens.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919"]),
        claim("bc536b", "ben-cline", "biblical_marriage", 2, True,
              "Cline voted for H.R. 3492, the Protect Children's Innocence Act of 2025 (House Vote #351, December 17, 2025, 216–211), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones or puberty-blocking drugs to minors — rejecting gender ideology and affirming biological sex as immutable in federal law.",
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

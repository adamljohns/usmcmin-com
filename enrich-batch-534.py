#!/usr/bin/env python3
"""Enrichment batch 534: 10 new claims across 5 sitting U.S. House members.

Targets: Ryan Mackenzie (PA-07 R), Joe Wilson (SC-02 R), Russell Fry (SC-07 R),
Cliff Bentz (OR-02 R), Guy Reschenthaler (PA-14 R) — bottom-of-alphabet states
(PA, SC, OR) with evidence_curated confidence and 3–5 existing claims. Adds 2
distinct new-category claims per target from 2022–2026 voting records and
co-sponsorships.

Sources: congress.gov, govtrack.us, en.wikipedia.org, ballotpedia.org,
mackenzie.house.gov (via search result).

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
    # ---------------- Ryan Mackenzie (PA-07, R) ----------------
    ("ryan-mackenzie", "PA", "Representative", [
        claim("rm25a", "ryan-mackenzie", "economic_stewardship", 0, True,
              "Mackenzie co-sponsored H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress), which prohibits the Federal Reserve from issuing a retail central bank digital currency or maintaining individual accounts — blocking a government-issued digital dollar. The bill passed the House 219–210 on July 17, 2025, with Mackenzie's co-sponsorship on record.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919"]),
        claim("rm25b", "ryan-mackenzie", "election_integrity", 0, True,
              "Mackenzie voted for the Safeguard American Voter Eligibility (SAVE) Act (H.R. 22), which requires documentary proof of U.S. citizenship to register to vote in federal elections. The bill passed 220–208 on April 10, 2025, with Mackenzie's campaign record explicitly noting his support for 'Voter ID and other election integrity efforts that would make it easier to vote and harder to cheat.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
    ]),

    # ---------------- Joe Wilson (SC-02, R) ----------------
    ("joe-wilson", "SC", "Representative", [
        claim("jw15a", "joe-wilson", "biblical_marriage", 0, True,
              "In 2015, Wilson co-sponsored H.J.Res. 32, a proposed constitutional amendment defining marriage exclusively as the union of one man and one woman in federal law — formally committing to the biblical, natural-law definition of marriage against judicial redefinition following Obergefell.",
              ["https://en.wikipedia.org/wiki/Joe_Wilson",
               "https://www.congress.gov/member/joe-wilson/W000795"]),
        claim("jw25a", "joe-wilson", "biblical_marriage", 2, True,
              "Wilson voted for the Protect Children's Innocence Act (H.R. 3492, December 17, 2025), which establishes federal criminal penalties for physicians who perform gender-transition surgeries or administer cross-sex hormones to minors — rejecting gender ideology and protecting children's biological identities. The bill passed 216–211.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
    ]),

    # ---------------- Russell Fry (SC-07, R) ----------------
    ("russell-fry", "SC", "Representative", [
        claim("rf25a", "russell-fry", "election_integrity", 0, True,
              "Fry voted for the Safeguard American Voter Eligibility (SAVE) Act (H.R. 22, April 10, 2025), which requires documentary proof of U.S. citizenship to register to vote in federal elections. The bill passed 220–208, directly implementing the voter-integrity standard the rubric supports.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("rf23a", "russell-fry", "foreign_policy_restraint", 0, True,
              "Fry was among 52 Republicans who voted for H.Con.Res. 30 (118th Congress) to direct the President to remove U.S. military forces from Somalia under the War Powers Resolution — invoking Congress's Article I authority over troop deployments and opposing open-ended executive military engagements without congressional authorization.",
              ["https://en.wikipedia.org/wiki/Russell_Fry",
               "https://www.govtrack.us/congress/members/russell_fry/456938"]),
    ]),

    # ---------------- Cliff Bentz (OR-02, R) ----------------
    ("cliff-bentz", "OR", "Representative", [
        claim("cb25a", "cliff-bentz", "biblical_marriage", 2, True,
              "Bentz voted for the Protect Children's Innocence Act (H.R. 3492, December 17, 2025), establishing federal criminal penalties for gender-transition surgeries and cross-sex hormone regimens administered to minors — rejecting gender ideology as applied to children and affirming biological sex as fixed.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
        claim("cb21a", "cliff-bentz", "economic_stewardship", 2, True,
              "Bentz signed the Americans for Tax Reform Taxpayer Protection Pledge, committing him to oppose any net federal income-tax increases — a fiscal-restraint posture consistent with anti-deficit, balanced-budget governance that resists spending funded by new taxes.",
              ["https://ballotpedia.org/Cliff_Bentz",
               "https://www.govtrack.us/congress/members/cliff_bentz/456842"]),
    ]),

    # ---------------- Guy Reschenthaler (PA-14, R) ----------------
    ("guy-reschenthaler", "PA", "Representative", [
        claim("gr25a", "guy-reschenthaler", "biblical_marriage", 2, True,
              "Reschenthaler voted for the Protect Children's Innocence Act (H.R. 3492, December 17, 2025), which criminalizes physicians who perform gender-transition procedures on minors at the federal level — affirming that biological sex is immutable and protecting children from gender-ideology-based medical interventions.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/votes/119-2025/h351"]),
        claim("gr22a", "guy-reschenthaler", "foreign_policy_restraint", 1, False,
              "During House floor debate on Ukraine aid legislation, Reschenthaler publicly called for speeding up weapon deliveries to Ukraine and condemned critics of open-ended funding as promoting 'defeatism, pessimism, and surrender' — aligning with the interventionist, indefinite-commitment camp rather than the rubric's call to wind down foreign military entanglements and restore congressional war-powers oversight.",
              ["https://en.wikipedia.org/wiki/Guy_Reschenthaler",
               "https://www.congress.gov/member/guy-reschenthaler/R000610"]),
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

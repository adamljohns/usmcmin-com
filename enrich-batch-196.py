#!/usr/bin/env python3
"""Enrichment batch 196: 1 new claim each for 5 TX U.S. Representatives.

archetype_curated/evidence_curated federal House members from bottom of
alphabet (TX), each already having 2 claims in sanctity_of_life and
border_immigration. Adds a third claim in a DISTINCT category per target.

Targets (all TX-R, U.S. Representative):
  Pete Sessions (TX-17)  — self_defense
  John Carter  (TX-31)  — election_integrity
  Jake Ellzey  (TX-6)   — economic_stewardship
  Brian Babin  (TX-36)  — self_defense
  Brandon Gill (TX-26)  — election_integrity

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
    # ---- Pete Sessions (TX-17, R) — self_defense ----
    ("pete-sessions", "TX", "Representative", [
        claim("ps1", "pete-sessions", "self_defense", 1, True,
              "Cosponsored H.R.1271 (118th Congress, 2023), the 'No Retaining Every Gun In a System That Restricts Your Rights Act,' which would end the requirement for out-of-business federal firearms licensees to transfer their transaction records to the ATF — directly opposing federal gun-registry infrastructure.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/1271/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/1271/all-info"]),
    ]),

    # ---- John Carter (TX-31, R) — election_integrity ----
    ("john-carter", "TX", "Representative", [
        claim("jc1", "john-carter", "election_integrity", 0, True,
              "Voted Yea on the SAVE Act (H.R.22, House Vote #102, April 10, 2025), which passed 220-208 and requires documentary proof of U.S. citizenship to register to vote in federal elections — a hard voter-ID measure to close noncitizen-registration loopholes.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---- Jake Ellzey (TX-6, R) — economic_stewardship ----
    ("jake-ellzey", "TX", "Representative", [
        claim("je1", "jake-ellzey", "economic_stewardship", 2, True,
              "Voted against raising the U.S. debt ceiling and publicly called for a balanced federal budget, stating 'DON'T SPEND MORE THAN YOU HAVE' and committing to work with fellow Republicans to restore fiscal accountability and stop passing bloated, deficit-spending budgets.",
              ["https://ellzey.house.gov/issues",
               "https://ballotpedia.org/Jake_Ellzey"]),
    ]),

    # ---- Brian Babin (TX-36, R) — self_defense ----
    ("brian-babin", "TX", "Representative", [
        claim("bb1", "brian-babin", "self_defense", 1, True,
              "Cosponsor of H.Res.339 (119th Congress, 2025), which supports the Second Amendment and commends President Trump's efforts to eliminate Biden-era firearm restrictions; earns top grades from the NRA and Gun Owners of America and serves on the Congressional Second Amendment Caucus.",
              ["https://www.congress.gov/bill/119th-congress/house-resolution/339/text",
               "https://babin.house.gov/issues/issue/?IssueID=14889"]),
    ]),

    # ---- Brandon Gill (TX-26, R) — election_integrity ----
    ("brandon-gill", "TX", "Representative", [
        claim("bg1", "brandon-gill", "election_integrity", 0, True,
              "Voted for the SAVE Act (H.R.22, April 10, 2025) requiring proof of U.S. citizenship to register in federal elections, then led an RSC letter campaign urging Senate Rules Committee Chairman McConnell to schedule an immediate markup after the bill stalled nearly 300 days without Senate action.",
              ["https://gill.house.gov/media/press-releases/rep-gill-leads-rsc-members-urging-senate-mark-save-act",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

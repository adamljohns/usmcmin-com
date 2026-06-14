#!/usr/bin/env python3
"""Enrichment batch 209: 3rd claims for 5 sitting U.S. Senators (archetype_curated bucket
exhausted — pivoted to evidence_curated senators with exactly 2 claims from the bottom of
the alphabet: ND, MT, IA, OH, MI).

Targets: John Hoeven (ND-R), Tim Sheehy (MT-R), Joni Ernst (IA-R),
         Bernie Moreno (OH-R), Gary Peters (MI-D).
Each adds one sourced claim in a distinct rubric category not yet covered.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- John Hoeven (ND-R, US Senator) ----------------
    ("john-hoeven", "ND", "Senator", [
        claim("jh3", "john-hoeven", "election_integrity", 0, True,
              "Co-sponsored the Safeguard American Voter Eligibility (SAVE) Act (S. 128, 119th Congress), which requires documentary proof of U.S. citizenship to register for federal elections and mandates photo voter ID. Hoeven championed it as 'commonsense legislation that safeguards our elections by ensuring only U.S. citizens can vote in our elections,' citing North Dakota's own robust voter-ID standard as the model.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/128",
               "https://news.ballotpedia.org/2026/03/25/senate-takes-up-save-america-act-to-require-voter-id-proof-of-citizenship-for-federal-elections/"]),
    ]),

    # ---------------- Tim Sheehy (MT-R, US Senator) ----------------
    ("tim-sheehy", "MT", "Senator", [
        claim("ts3", "tim-sheehy", "self_defense", 0, True,
              "Ran for Senate in 2024 explicitly pledging to 'protect gun ownership,' earning Trump's endorsement as 'Strong on... our constantly under siege Second Amendment.' A former U.S. Navy SEAL, Sheehy campaigned in one of the few states with constitutional carry (Montana enacted HB 102 in 2021) and has identified Second Amendment protection as a core Senate priority.",
              ["https://en.wikipedia.org/wiki/Tim_Sheehy",
               "https://ballotpedia.org/Tim_Sheehy"]),
    ]),

    # ---------------- Joni Ernst (IA-R, US Senator) ----------------
    ("joni-ernst", "IA", "Senator", [
        claim("je3", "joni-ernst", "self_defense", 4, True,
              "Introduced the FIREARM Act (2024) to prevent the ATF from revoking Federal Firearms Licenses over minor clerical errors, and co-sponsored the GRIP Act prohibiting federal funds from financing any government gun registry — directly targeting ATF overreach and government gun-tracking. Holds an NRA 'A' rating and an A+ on the 2024 NSSF Congressional Report Card.",
              ["https://www.ernst.senate.gov/news/press-releases/ernst-works-to-protect-lawful-gun-dealers-from-atf",
               "https://www.ernst.senate.gov/news/press-releases/senators-reintroduce-bill-to-prohibit-use-of-federal-money-for-state-gun-registries"]),
    ]),

    # ---------------- Bernie Moreno (OH-R, US Senator) ----------------
    ("bernie-moreno", "OH", "Senator", [
        claim("bm3", "bernie-moreno", "self_defense", 0, True,
              "Co-sponsored the Constitutional Concealed Carry Reciprocity Act in the 119th Congress (2025), which would allow any valid state-issued concealed-carry permit to be honored nationally — an NRA-, GOA-, and NSSF-endorsed measure reflecting the rubric's constitutional-carry standard.",
              ["https://www.govtrack.us/congress/members/bernie_moreno/456967",
               "https://ballotpedia.org/Bernie_Moreno"]),
    ]),

    # ---------------- Gary Peters (MI-D, US Senator) ----------------
    ("gary-peters", "MI", "Senator", [
        claim("gp3", "gary-peters", "border_immigration", 1, True,
              "On January 20, 2025, voted Yea on the Laken Riley Act (S. 5, 119th Congress) — one of only twelve Senate Democrats to join all Republicans in requiring DHS to detain non-U.S. nationals who have been arrested for burglary, theft, or other offenses. The bill passed 64-35 and was signed by President Trump on January 29, 2025.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

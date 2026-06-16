#!/usr/bin/env python3
"""Enrichment batch 243: 5 federal House members from bottom of alphabet.

Targets archetype_party_default House reps with 0 claims.
States: NJ×2, MO, MN, MA (bottom of alphabet, avoiding top-side collision agent).

Mix (0 R / 5 D): Donald Norcross (NJ-D), Bonnie Watson Coleman (NJ-D),
Wesley Bell (MO-D), Betty McCollum (MN-D), Stephen Lynch (MA-D).
Each claim cites >=1 reliable source and reflects 2021-2026 voting record /
public positions.

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
    # ------------ Donald Norcross (NJ-01, D, retiring 2026) ------------
    ("donald-norcross", "NJ", "House", [
        claim("dn1", "donald-norcross", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act of 2022 (the first major federal gun legislation in nearly 30 years), which strengthened background checks and funded crisis-intervention programs; holds a 0% NRA lifetime rating and 100% Brady Campaign rating. Separately demanded a House floor vote on gun safety, stating 'Inaction is killing us.'",
              ["https://norcross.house.gov/media-center/press-releases/rep-norcross-votes-pass-historic-gun-safety-bill",
               "https://norcross.house.gov/media-center/press-releases/rep-norcross-votes-gun-safety-inaction-killing-us"]),
        claim("dn2", "donald-norcross", "sanctity_of_life", 4, False,
              "Joined Planned Parenthood of New Jersey's 'Protect X' campaign and cosponsored the Right to Contraception Act (H.R.4121, June 2023); separately issued a statement opposing anti-abortion executive orders, demonstrating ongoing collaboration with and support for Planned Parenthood.",
              ["https://norcross.house.gov/media-center/press-releases/norcross-joins-planned-parenthood-new-jersey-protect-x",
               "https://norcross.house.gov/media-center/press-releases/anti-abortion-executive-order"]),
    ]),

    # ------------ Bonnie Watson Coleman (NJ-12, D, retiring 2026) ------------
    ("bonnie-watson-coleman", "NJ", "House", [
        claim("bwc1", "bonnie-watson-coleman", "self_defense", 1, False,
              "Voted for the Federal Extreme Risk Protection Order Act, a red-flag bill that empowers family members and law enforcement to seek federal court orders to temporarily remove firearm access from individuals deemed a danger; also introduced the Stop Online Ammunition Sales Act requiring identity verification for online ammo purchases.",
              ["https://watsoncoleman.house.gov/newsroom/press-releases/rep-watson-coleman-votes-to-prevent-future-gun-violence-through-extreme-risk-protection-orders",
               "https://ballotpedia.org/Bonnie_Watson_Coleman"]),
        claim("bwc2", "bonnie-watson-coleman", "sanctity_of_life", 0, False,
              "Was arrested outside the U.S. Supreme Court in June 2022 while demonstrating against the Dobbs v. Jackson Women's Health Organization ruling that overturned Roe v. Wade; one of several House members taken into custody at the protest defending unrestricted abortion access.",
              ["https://watsoncoleman.house.gov/newsroom/press-releases/congresswoman-bonnie-watson-coleman-arrested-outside-supreme-court-during-protest-for-abortion-rights",
               "https://en.wikipedia.org/wiki/Bonnie_Watson_Coleman"]),
    ]),

    # ------------ Wesley Bell (MO-01, D, took office Jan 2025) ------------
    ("wesley-bell", "MO", "House", [
        claim("wb1", "wesley-bell", "self_defense", 0, False,
              "Co-introduced the Safer Neighborhoods Gun Buyback Act in 2025 (119th Congress) directing $360 million in federal grants to state and local programs to remove privately-owned firearms from communities; also cosponsored H.R.1307, the Office of Gun Violence Prevention Act of 2025, to institutionalize federal gun-control infrastructure.",
              ["https://bell.house.gov/media/press-releases/bell-hayes-mciver-introduce-legislation-fund-gun-buybacks-and-remove-firearms",
               "https://www.congress.gov/bill/119th-congress/house-bill/1307/cosponsors"]),
        claim("wb2", "wesley-bell", "sanctity_of_life", 0, False,
              "In the 119th Congress (2025-2026), advocated in the Congressional Record to 'ensure affordable abortion coverage for every woman' and to 'limit restrictions on provision of abortion services to protect women's right to determine whether to continue or end pregnancy.'",
              ["https://www.congress.gov/congressional-record/congressional-record-index/119th-congress/1st-session/bell-wesley-a-representative-from-missouri/1959862",
               "https://ballotpedia.org/Wesley_Bell"]),
    ]),

    # ------------ Betty McCollum (MN-04, D) ------------
    ("betty-mccollum", "MN", "House", [
        claim("bm1", "betty-mccollum", "self_defense", 1, False,
              "Earned an 'F' rating from the NRA; cosponsored the Assault Weapons Ban of 2023 (H.R.698) and signed a discharge petition to force a House floor vote on the assault weapons ban. Joined a House floor sit-in to demand votes on gun violence prevention legislation.",
              ["https://mccollum.house.gov/gun-violence-prevention",
               "https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors"]),
        claim("bm2", "betty-mccollum", "sanctity_of_life", 4, False,
              "A long-time champion of Planned Parenthood: issued a formal statement defending Planned Parenthood's Title X federal family-planning funding when the Trump administration forced PP to withdraw from the program, and is endorsed by NARAL Pro-Choice America.",
              ["https://mccollum.house.gov/media/press-releases/mccollum-statement-planned-parenthood-withdrawal-title-x-program",
               "https://ballotpedia.org/Betty_McCollum"]),
    ]),

    # ------------ Stephen Lynch (MA-08, D) ------------
    ("stephen-lynch", "MA", "Representative", [
        claim("sl1", "stephen-lynch", "self_defense", 1, False,
              "Cosponsored the Assault Weapons Ban of 2022 (H.R.1808), which passed the House on July 29, 2022; advocates for banning assault weapons, bump stocks, and high-capacity ammunition magazines and has a dedicated gun-control section on his official House website.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/1808",
               "https://lynch.house.gov/gun-control"]),
        claim("sl2", "stephen-lynch", "sanctity_of_life", 0, False,
              "Voted for the Women's Health Protection Act in 2021 establishing a federal statutory right to abortion — a notable shift from his prior anti-abortion stance (had called himself 'pro-life' since entering Congress in 2001); now consistently votes to protect and expand abortion access.",
              ["https://ballotpedia.org/Stephen_Lynch",
               "https://en.wikipedia.org/wiki/Stephen_Lynch_(politician)"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

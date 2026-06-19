#!/usr/bin/env python3
"""Enrichment batch 304: 3rd claims for 5 federal representatives (bottom-of-alphabet states).

Archetype_curated federal bucket fully exhausted (see batch 303 note).
Batch targets evidence_curated federal representatives with exactly 2 claims —
taken from the bottom of the alphabet (IN, IL ×3, HI) spanning
distinct rubric categories not yet covered in each candidate's profile.

Targets:
  Frank Mrvan      (IN-1,  D) — voted YES Inflation Reduction Act → economic_stewardship
  Jonathan Jackson (IL-1,  D) — voted NO Secure the Border Act  → border_immigration
  Eric Sorensen    (IL-17, D) — cosponsor Assault Weapons Ban 2023 → self_defense
  Delia Ramirez    (IL-3,  D) — voted NO Secure the Border Act  → border_immigration
  Jill Tokuda      (HI-2,  D) — voted NO Secure the Border Act  → border_immigration

Each claim cites >=1 reliable source and reflects 2023-2025 public record.

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
    # ---- Frank Mrvan (IN-1, D — US Representative) ----
    ("frank-mrvan", "IN", "US Representative", [
        claim("fm3", "frank-mrvan", "economic_stewardship", 2, False,
              "Voted YES on the Inflation Reduction Act (H.R. 5376, 117th Congress, House Vote #420, August 12, 2022), which passed 220-207 with every House Democrat — including Mrvan — voting in favor. The IRA authorized approximately $369 billion in new federal spending on climate programs and ACA subsidy extensions, financed in part by new corporate minimum taxes; fiscal conservatives and balanced-budget advocates widely criticized it as a net expansion of federal outlays and government reach, placing Mrvan outside the anti-deficit stewardship posture the rubric calls for.",
              ["https://www.govtrack.us/congress/votes/117-2022/h420",
               "https://ballotpedia.org/Inflation_Reduction_Act_of_2022"]),
    ]),

    # ---- Jonathan Jackson (IL-1, D — US Representative) ----
    ("jonathan-jackson", "IL", "US Representative", [
        claim("jj3", "jonathan-jackson", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R. 2, 118th Congress, House Vote #209, May 11, 2023), which passed 219-213; H.R. 2 would have resumed funding for border-wall construction at roughly $4.1 billion, limited asylum eligibility to applicants presenting at official ports of entry, ended the 'catch and release' practice, and mandated E-Verify for employers — comprehensive wall-and-enforcement measures that Jackson, representing Illinois's 1st congressional district (Chicago's South Side), opposed along with virtually every other House Democrat.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://www.govtrack.us/congress/votes/118-2023/h209"]),
    ]),

    # ---- Eric Sorensen (IL-17, D — US Representative) ----
    ("eric-sorensen", "IL", "US Representative", [
        claim("es3", "eric-sorensen", "self_defense", 1, False,
              "Co-sponsored the Assault Weapons Ban of 2023 (H.R. 698, 118th Congress), as confirmed by Congress.gov co-sponsor records dated March 27, 2023; the bill would have banned the manufacture, sale, transfer, importation, and possession of semi-automatic assault weapons as well as large-capacity ammunition-feeding devices holding more than ten rounds — directly opposing the rubric's rejection of assault-weapon bans and magazine-capacity restrictions as unconstitutional infringements on Second Amendment rights.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://www.govtrack.us/congress/bills/118/hr698/cosponsors"]),
    ]),

    # ---- Delia Ramirez (IL-3, D — US Representative) ----
    ("delia-ramirez", "IL", "US Representative", [
        claim("dr3", "delia-ramirez", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R. 2, 118th Congress, House Vote #209, May 11, 2023), which passed 219-213; the bill would have mandated border-wall construction, limited asylum to official ports of entry, eliminated humanitarian parole for economic migrants, and required E-Verify — enforcement-first and wall-building measures that Ramirez, the daughter of undocumented Guatemalan immigrants and a member of the House Homeland Security Subcommittee on Border Security and Enforcement, openly opposed as harmful to immigrant communities.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Delia_Ramirez"]),
    ]),

    # ---- Jill Tokuda (HI-2, D — US Representative) ----
    ("jill-tokuda", "HI", "US Representative", [
        claim("jt3", "jill-tokuda", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R. 2, 118th Congress, House Vote #209, May 11, 2023), which passed 219-213; H.R. 2 would have renewed border-wall construction funding, restricted asylum to ports of entry only, ended catch-and-release, and instituted E-Verify mandates — the comprehensive wall-and-enforcement posture the rubric identifies as aligned with border security. Tokuda, a member of the Congressional Progressive Caucus representing Hawaii's 2nd district, voted against the measure in keeping with her progressive immigration stance.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Jill_Tokuda"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; prevents wrong-state same-slug collisions."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

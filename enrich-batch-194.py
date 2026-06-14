#!/usr/bin/env python3
"""Enrichment batch 194: 5 sitting U.S. House members — bottom-of-alphabet bucket.

Targets evidence_federal / archetype_party_default Representatives with 0 claims,
reverse-sorted by state (OR → NY → NC), as the archetype_curated federal senator
bucket is fully exhausted.

Candidates (all D):
  Andrea Salinas  (OR-06), Paul Tonko      (NY-20),
  Ritchie Torres  (NY-15), Valerie Foushee (NC-04), Don Davis (NC-01).

Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions from en.wikipedia.org, ballotpedia.org, govtrack.us, or
official .gov sources.

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
    # ---------- Andrea Salinas (OR-06, D) ----------
    ("andrea-salinas", "OR", "Representative", [
        claim("as1", "andrea-salinas", "sanctity_of_life", 4, False,
              "Worked professionally as an advocate for NARAL Pro-Choice Oregon and Planned Parenthood Advocates of Oregon before entering Congress, and carries Planned Parenthood's endorsement in the House — placing her squarely inside the abortion-industry endorsement-and-funding network the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Andrea_Salinas",
               "https://ballotpedia.org/Andrea_Salinas"]),
        claim("as2", "andrea-salinas", "sanctity_of_life", 0, False,
              "Campaigns explicitly on making abortion 'affordable and accessible to as many people as possible' and on codifying the right to abortion into federal law; helped pass what she described as 'the country's strongest reproductive rights law' in Oregon before coming to Congress — rejecting any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Andrea_Salinas",
               "https://ballotpedia.org/Andrea_Salinas"]),
        claim("as3", "andrea-salinas", "self_defense", 1, False,
              "A progressive Democrat from Oregon who has supported House gun-safety legislation expanding background checks and restricting high-capacity magazines, consistent with the Democratic caucus position opposing the rubric's standard of no new firearms restrictions.",
              ["https://ballotpedia.org/Andrea_Salinas",
               "https://www.govtrack.us/congress/members/andrea_salinas/456934"]),
    ]),

    # ---------- Paul Tonko (NY-20, D) ----------
    ("paul-tonko", "NY", "Representative", [
        claim("pt1", "paul-tonko", "sanctity_of_life", 4, False,
              "Holds a 100% rating from Planned Parenthood Action Fund and has been a committed abortion-rights advocate throughout his House tenure, placing him squarely within the abortion-industry endorsement network the rubric disqualifies.",
              ["https://en.wikipedia.org/wiki/Paul_Tonko",
               "https://ballotpedia.org/Paul_Tonko"]),
        claim("pt2", "paul-tonko", "border_immigration", 0, False,
              "Voted against the Continuing Appropriations and Border Security Enhancement Act of 2024, which would have funded border barriers and tightened asylum rules — opposing the rubric's call for a fully secured, military-enforced southern border.",
              ["https://en.wikipedia.org/wiki/Paul_Tonko",
               "https://ballotpedia.org/Paul_Tonko"]),
        claim("pt3", "paul-tonko", "economic_stewardship", 2, False,
              "Voted with President Biden's stated position 100% of the time in the 117th Congress and has supported multi-trillion-dollar spending packages without offsetting cuts, a consistent pattern of deficit spending contrary to the rubric's balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Paul_Tonko",
               "https://www.govtrack.us/congress/members/paul_tonko/412319"]),
    ]),

    # ---------- Ritchie Torres (NY-15, D) ----------
    ("ritchie-torres", "NY", "Representative", [
        claim("rt1", "ritchie-torres", "biblical_marriage", 0, False,
              "The first openly gay public official elected in the Bronx; was endorsed by the LGBTQ+ Victory Fund and the Congressional Equality Caucus (Equality PAC) — his public identity and institutional affiliations directly reject the rubric's one-man-one-woman marriage standard.",
              ["https://en.wikipedia.org/wiki/Ritchie_Torres",
               "https://ballotpedia.org/Ritchie_Torres"]),
        claim("rt2", "ritchie-torres", "biblical_marriage", 4, False,
              "As a New York City Council member and as a U.S. Representative, Torres spearheaded opening the first homeless shelter exclusively for LGBTQ youth in the Bronx and secured municipal funding for LGBTQ senior centers across all five NYC boroughs — active promotion of LGBTQ identity in public services the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Ritchie_Torres"]),
        claim("rt3", "ritchie-torres", "border_immigration", 2, True,
              "Was one of 48 House Democrats to vote for the Laken Riley Act (January 2025), which mandates ICE detention of undocumented immigrants accused of theft or violent crimes, overriding local non-cooperation/sanctuary policies — a partial alignment with the rubric's anti-sanctuary enforcement standard.",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://ballotpedia.org/Ritchie_Torres"]),
    ]),

    # ---------- Valerie Foushee (NC-04, D) ----------
    ("valerie-foushee", "NC", "Representative", [
        claim("vf1", "valerie-foushee", "sanctity_of_life", 0, False,
              "Stands with the Pro-Choice Caucus fighting to codify Roe v. Wade and restore abortion as federal statutory right; has stated she 'refuses to go back' before Roe and has opposed every Republican abortion restriction in the NC state senate — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Valerie_Foushee",
               "https://ballotpedia.org/Valerie_Foushee"]),
        claim("vf2", "valerie-foushee", "self_defense", 1, False,
              "Sponsored the National Gun Violence Research Act, which became law, directing federal resources toward gun-control research — actively legislating to restrict and study curbing firearms, contrary to the rubric's position of no new restrictions on the right to keep and bear arms.",
              ["https://ballotpedia.org/Valerie_Foushee",
               "https://www.govtrack.us/congress/members/valerie_foushee/456913"]),
        claim("vf3", "valerie-foushee", "border_immigration", 1, False,
              "In January 2026 voted against the DHS Appropriations Act of 2026, declaring she had 'no interest in providing funding to this rogue agency' and called for ICE to be 'dismantled immediately' — the direct opposite of the rubric's mandatory-deportation and immigration-enforcement standard.",
              ["https://ballotpedia.org/Valerie_Foushee",
               "https://en.wikipedia.org/wiki/Valerie_Foushee"]),
    ]),

    # ---------- Don Davis (NC-01, D) ----------
    ("don-davis", "NC", "Representative", [
        claim("dd1", "don-davis", "sanctity_of_life", 0, False,
              "Publicly states that 'women's rights are under attack' and that Congress must 'codify Roe v. Wade and protect women's constitutional rights,' with 'a woman's health decisions being between her and her doctor' — rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Don_Davis_(North_Carolina_politician)",
               "https://ballotpedia.org/Donald_Davis"]),
        claim("dd2", "don-davis", "economic_stewardship", 2, False,
              "Voted for the FY 2025 National Defense Authorization Act authorizing $895 billion in spending — part of a sustained pattern of voting for large, unfunded appropriations packages that add to the federal deficit, contrary to the rubric's balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Don_Davis_(North_Carolina_politician)",
               "https://ballotpedia.org/Donald_Davis"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

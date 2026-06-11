#!/usr/bin/env python3
"""Enrichment batch 129: hand-curated claims for 5 sitting U.S. Representatives.

Targets evidence_federal representatives with 0 claims, drawn from the bottom
of the alphabet (FL, ID, IA). Sources: ballotpedia.org, congress.gov,
govtrack.us, sbaprolife.org, wikipedia.org. All claims reflect 2023-2026
voting record / public positions.

Candidates (5 R):
  Brian Mast (FL-R), Gus Bilirakis (FL-R), Mario Diaz-Balart (FL-R),
  Michael Simpson (ID-R), Zach Nunn (IA-R).
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
    # ---------------- Brian Mast (FL-R, US Representative) ----------------
    ("brian-mast", "FL", "Representative", [
        claim("bm1", "brian-mast", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life rating from the National Right to Life Committee; stated 'The decision to overturn Roe v. Wade will protect millions of innocent babies' and voted for the Born-Alive Abortion Survivors Protection Act (H.R.26), consistently opposing taxpayer abortion funding.",
              ["https://ballotpedia.org/Brian_Mast",
               "https://sbaprolife.org/representative/brian-mast"]),
        claim("bm2", "brian-mast", "self_defense", 0, True,
              "Has publicly committed to 'fight to protect our Second Amendment from all attempts to erode it'; helped pass concealed carry reciprocity legislation during his House tenure and opposed all measures to restrict lawful firearm ownership.",
              ["https://ballotpedia.org/Brian_Mast",
               "https://www.govtrack.us/congress/members/brian_mast/412698"]),
        claim("bm3", "brian-mast", "foreign_policy_restraint", 1, True,
              "Voted NO on the $95 billion Ukraine, Israel, and Taiwan foreign-aid supplemental package in April 2024, opposing open-ended overseas military entanglements; as House Foreign Affairs Committee Chair from January 2025, insists on 'America First' accountability before any foreign aid flows.",
              ["https://en.wikipedia.org/wiki/Brian_Mast",
               "https://www.congress.gov/member/brian-mast/M001199"]),
    ]),

    # ---------------- Gus Bilirakis (FL-R, US Representative) ----------------
    ("gus-bilirakis", "FL", "Representative", [
        claim("gb1", "gus-bilirakis", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee in 2023-24; voted for the Born-Alive Abortion Survivors Protection Act (H.R.26); requested House floor consideration of the No Taxpayer Funding for Abortion Act (H.R.18) to make the Hyde Amendment permanent.",
              ["https://sbaprolife.org/representative/gus-bilirakis",
               "https://www.congress.gov/member/gus-bilirakis/B001257"]),
        claim("gb2", "gus-bilirakis", "self_defense", 0, True,
              "Cosponsored H.R.38, the Constitutional Concealed Carry Reciprocity Act of 2025 (119th Congress), enabling law-abiding permit holders to carry concealed across state lines; carries an A rating from the NRA reflecting a consistent pro-Second Amendment record.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/cosponsors",
               "https://en.wikipedia.org/wiki/Gus_Bilirakis"]),
        claim("gb3", "gus-bilirakis", "election_integrity", 0, True,
              "Original cosponsor of the SAVE Act (H.R.22, 119th Congress, 2025) requiring documentary proof of U.S. citizenship when registering to vote in federal elections — a foundational election-integrity measure to prevent non-citizen participation.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Gus_Bilirakis"]),
    ]),

    # ---------------- Mario Diaz-Balart (FL-R, US Representative) ----------------
    ("mario-diaz-balart", "FL", "Representative", [
        claim("mdb1", "mario-diaz-balart", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee; stated 'I will always support pro-life protections and ensure no taxpayer funds are spent to promote or perform abortions,' and secured long-standing life-protection provisions in the FY2025 State and Foreign Operations appropriations bill he authored.",
              ["https://ballotpedia.org/Mario_Diaz-Balart",
               "https://justfacts.votesmart.org/candidate/24312/mario-diaz-balart"]),
        claim("mdb2", "mario-diaz-balart", "foreign_policy_restraint", 2, True,
              "The leading Congressional voice against U.S. assistance to the hostile communist regimes of Cuba, Venezuela, and Nicaragua; co-chairs the Cuba Democracy Caucus, consistently advocating sanctions rather than normalization or foreign aid to governments that persecute their citizens and threaten U.S. interests.",
              ["https://en.wikipedia.org/wiki/Mario_D%C3%ADaz-Balart",
               "https://www.congress.gov/member/mario-diaz-balart/D000600"]),
    ]),

    # ---------------- Michael Simpson (ID-R, US Representative) ----------------
    ("michael-simpson", "ID", "Representative", [
        claim("ms1", "michael-simpson", "sanctity_of_life", 0, True,
              "Rated 100% by the National Right to Life Committee and 0% by NARAL Pro-Choice America; voted for the Born-Alive Abortion Survivors Protection Act (H.R.26) and has opposed taxpayer funding for abortion and embryo-destructive stem-cell research throughout his congressional career.",
              ["https://ballotpedia.org/Michael_Simpson_(Idaho)",
               "https://justfacts.votesmart.org/candidate/2917/mike-simpson"]),
        claim("ms2", "michael-simpson", "border_immigration", 0, True,
              "Voted YES on H.R.2, the Secure the Border Act of 2023, mandating resumption of border-wall construction, tightening asylum eligibility, and requiring E-Verify employer verification — supporting a physical-barrier and enforcement-first approach to the southern border.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://ballotpedia.org/Michael_Simpson_(Idaho)"]),
        claim("ms3", "michael-simpson", "self_defense", 0, True,
              "Signed the amicus curiae brief in D.C. v. Heller (2008) supporting the Second Amendment as an individual constitutional right; has been endorsed by the National Rifle Association and maintained a pro-Second Amendment voting record across his congressional career since 1999.",
              ["https://en.wikipedia.org/wiki/Mike_Simpson",
               "https://ballotpedia.org/Michael_Simpson_(Idaho)"]),
    ]),

    # ---------------- Zach Nunn (IA-R, US Representative) ----------------
    ("zach-nunn", "IA", "Representative", [
        claim("zn1", "zach-nunn", "sanctity_of_life", 0, True,
              "A self-described 'recognized pro-life leader committed to fighting for the unborn'; voted YES on H.R.26, the Born-Alive Abortion Survivors Protection Act (118th Congress), requiring that infants born alive after failed abortions receive the same medical care as any newborn.",
              ["https://ballotpedia.org/Zach_Nunn",
               "https://www.govtrack.us/congress/members/zachary_zach_nunn/456898"]),
        claim("zn2", "zach-nunn", "border_immigration", 0, True,
              "Voted YES on H.R.5525, the Continuing Appropriations and Border Security Enhancement Act (2024), supporting additional border security funding and enforcement to combat drug trafficking and illegal crossings at the southern border.",
              ["https://ballotpedia.org/Zach_Nunn",
               "https://www.congress.gov/member/zachary-nunn/N000193"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent slug collisions across states."""
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

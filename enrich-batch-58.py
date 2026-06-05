#!/usr/bin/env python3
"""Enrichment batch 58: hand-curated claims for 4 federal House candidates.

Targets archetype_curated U.S. Representatives / House candidates with 0 claims,
taken from the bottom of the alphabet (NY, FL). Mix: 3 R / 1 D.

Candidates:
  Byron Donalds (FL-19, R) — current US Rep, Freedom Caucus, running for FL Gov 2026
  Anna Paulina Luna (FL-13, R) — current US Rep, self-described "pro-life extremist"
  Carlos A. Gimenez (FL-28, R) — current US Rep, former Miami-Dade Mayor
  Antonio Reynoso (NY-07, D) — Brooklyn Borough President, 2026 D congressional candidate

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
    # ---------------- Byron Donalds (FL-19, R) ----------------
    ("byron-donalds", "FL", "Representative", [
        claim("bd1", "byron-donalds", "sanctity_of_life", 0, True,
              "Self-described as 'pro-life' since his 2020 campaign and carries an SBA Pro-Life America scorecard rating; voted consistently throughout his House tenure to protect the lives of the unborn and stop taxpayer-funded abortion.",
              ["https://sbaprolife.org/representative/byron-donalds",
               "https://en.wikipedia.org/wiki/Byron_Donalds"]),
        claim("bd2", "byron-donalds", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29), signed into law January 29, 2025, requiring DHS to mandatorily detain illegal aliens arrested for theft-related crimes — a step toward mandatory deportation of criminal illegal aliens that passed the House with all Republicans voting in favor.",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
        claim("bd3", "byron-donalds", "self_defense", 1, True,
              "Freedom Caucus and Republican Study Committee member who has consistently opposed gun control legislation; self-identifies as 'gun owning' and has never supported red-flag laws, assault-weapons bans, or magazine-capacity restrictions.",
              ["https://en.wikipedia.org/wiki/Byron_Donalds",
               "https://ballotpedia.org/Byron_Donalds"]),
    ]),

    # ---------------- Anna Paulina Luna (FL-13, R) ----------------
    ("anna-paulina-luna", "FL", "Representative", [
        claim("apl1", "anna-paulina-luna", "sanctity_of_life", 0, True,
              "Labels herself a 'pro-life extremist' and has been endorsed by SBA Pro-Life America; voted consistently to protect the lives of the unborn and to block taxpayer funding of abortion throughout her House service.",
              ["https://sbaprolife.org/representative/anna-paulina-luna",
               "https://en.wikipedia.org/wiki/Anna_Paulina_Luna"]),
        claim("apl2", "anna-paulina-luna", "foreign_policy_restraint", 1, True,
              "Voted against the $60 billion Ukraine military aid package in April 2024 and cosponsored the Ukraine Fatigue Resolution (H.Res.113), which calls for suspending all U.S. foreign aid to Ukraine and requiring immediate peace negotiations — aligning with the rubric's call to end foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/Anna_Paulina_Luna"]),
        claim("apl3", "anna-paulina-luna", "foreign_policy_restraint", 4, True,
              "Expressed opposition to U.S. membership in NATO in March 2025, favoring an America-First foreign policy that avoids entangling alliances and resists NATO expansion commitments.",
              ["https://en.wikipedia.org/wiki/Anna_Paulina_Luna"]),
    ]),

    # ---------------- Carlos A. Gimenez (FL-28, R) ----------------
    ("carlos-a-gimenez", "FL", "Representative", [
        claim("cg1", "carlos-a-gimenez", "sanctity_of_life", 0, True,
              "Holds a pro-life voting record tracked by SBA Pro-Life America's National Pro-Life Scorecard; voted to defend the lives of the unborn and infants and actively opposed Florida's 2024 abortion expansion amendment (Amendment 4).",
              ["https://sbaprolife.org/representative/carlos-gimenez",
               "https://en.wikipedia.org/wiki/Carlos_A._Gim%C3%A9nez"]),
        claim("cg2", "carlos-a-gimenez", "border_immigration", 1, False,
              "In April 2026, was one of only six House Republicans to vote with all Democrats to preserve Temporary Protected Status for approximately 350,000 Haitian immigrants despite the Trump administration's efforts to terminate TPS — siding with a stay-of-deportation rather than mandatory removal.",
              ["https://en.wikipedia.org/wiki/Carlos_A._Gim%C3%A9nez"]),
        claim("cg3", "carlos-a-gimenez", "border_immigration", 2, True,
              "As Miami-Dade County Mayor, ordered his corrections department to honor all ICE detainer requests; the Miami-Dade County Board of Commissioners formally codified this anti-sanctuary policy by a 9-to-3 vote, directly rejecting the sanctuary-city model.",
              ["https://en.wikipedia.org/wiki/Carlos_A._Gim%C3%A9nez"]),
    ]),

    # ---------------- Antonio Reynoso (NY-07, D) ----------------
    ("antonio-reynoso", "NY", "Representative", [
        claim("ar1", "antonio-reynoso", "border_immigration", 2, False,
              "As Brooklyn Borough President and 2026 NY-07 congressional candidate, publicly declared 'ICE is not welcome in Brooklyn' following 2026 federal immigration enforcement operations and used his platform to protect illegal immigrants from deportation — the opposite of the anti-sanctuary posture the rubric requires.",
              ["https://en.wikipedia.org/wiki/Antonio_Reynoso",
               "https://en.wikipedia.org/wiki/ICE_and_New_York_City_during_the_second_Trump_presidency"]),
        claim("ar2", "antonio-reynoso", "border_immigration", 1, False,
              "Endorsed the 'Abolish ICE' pledge, explicitly calling for the elimination of the federal agency responsible for enforcing immigration laws and executing deportations of illegal aliens.",
              ["https://ballotpedia.org/Antonio_Reynoso"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

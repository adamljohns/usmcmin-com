#!/usr/bin/env python3
"""Enrichment batch 226: third-claim enrichment for 5 OR/OH U.S. Representatives.

Targets evidence_curated federal representatives at the bottom of the alphabet
with exactly 2 claims, adding one distinct-category claim each.

Mix (2 R / 3 D): Maxine Dexter (OR-03-D), Shontel Brown (OH-11-D),
Michael Turner (OH-10-R), Marcy Kaptur (OH-09-D), David Joyce (OH-14-R).

Sources: govtrack.us, congress.gov, ballotpedia.org, en.wikipedia.org.

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
    # ---------------- Maxine Dexter (OR-03-D, U.S. Representative) ----------------
    ("maxine-dexter", "OR", "Representative", [
        claim("md3", "maxine-dexter", "border_immigration", 1, False,
              "In April 2025 Dexter traveled to El Salvador to personally advocate for the release of Kilmar Abrego Garcia, a Salvadoran national deported under the Trump administration's mandatory-enforcement immigration policy — publicly opposing deportation enforcement and the rubric's call for mandatory removal of unlawfully present individuals.",
              ["https://en.wikipedia.org/wiki/Maxine_Dexter",
               "https://ballotpedia.org/Maxine_Dexter"]),
    ]),

    # ---------------- Shontel Brown (OH-11-D, U.S. Representative) ----------------
    ("shontel-brown", "OH", "Representative", [
        claim("sb3", "shontel-brown", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (H.R. 8404, House Vote #479, December 8, 2022; 258–169), which repeals the Defense of Marriage Act and requires federal and all state governments to recognize same-sex marriages — directly opposing the rubric's standard that marriage is between one man and one woman.",
              ["https://www.govtrack.us/congress/votes/117-2022/h479",
               "https://ballotpedia.org/Shontel_Brown"]),
    ]),

    # ---------------- Michael Turner (OH-10-R, U.S. Representative) ----------------
    ("michael-turner", "OH", "Representative", [
        claim("mt3", "michael-turner", "foreign_policy_restraint", 2, False,
              "As House Intelligence Committee Chairman (118th Congress, 2023–2025), Turner championed and voted for the Emergency National Security Supplemental Appropriations Act, 2024 (H.R. 815 / Public Law 118-50, April 24, 2024), which provided $61 billion for Ukraine and $26 billion for Israel in open-ended foreign military aid — a hawkish posture opposing the rubric's foreign-policy-restraint standard against perpetual overseas commitments.",
              ["https://en.wikipedia.org/wiki/Mike_Turner",
               "https://www.congress.gov/bill/118th-congress/house-bill/815",
               "https://ballotpedia.org/Michael_Turner_(Ohio)"]),
    ]),

    # ---------------- Marcy Kaptur (OH-09-D, U.S. Representative) ----------------
    ("marcy-kaptur", "OH", "Representative", [
        claim("mk3", "marcy-kaptur", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022; passed 234–193 with all 220 House Democrats in favor), which expanded background checks for under-21 firearm buyers, funded state red-flag laws, and narrowed private-sale exemptions — supporting gun-control measures the rubric opposes as infringements on Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Marcy_Kaptur",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
    ]),

    # ---------------- David Joyce (OH-14-R, U.S. Representative) ----------------
    ("david-joyce", "OH", "Representative", [
        claim("dj3", "david-joyce", "biblical_marriage", 0, False,
              "One of 47 Republicans to vote YES on the Respect for Marriage Act (H.R. 8404, July 19, 2022 and again December 8, 2022), which codifies federal recognition of same-sex marriages and repeals the Defense of Marriage Act — placing him among the small Republican minority that rejected the one-man-one-woman marriage standard the rubric upholds.",
              ["https://en.wikipedia.org/wiki/David_Joyce_(politician)",
               "https://ballotpedia.org/David_Joyce",
               "https://www.govtrack.us/congress/votes/117-2022/h479"]),
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

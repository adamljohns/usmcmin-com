#!/usr/bin/env python3
"""Enrichment batch 247: 4 sitting Illinois U.S. Representatives.

Targets archetype_party_default House members with 0 claims — the last
four sitting US Reps in that bucket, all IL Democrats.

Mix (0 R / 4 D): Lauren Underwood (IL-14), Eric Sorensen (IL-17),
Brad Schneider (IL-10), Bill Foster (IL-11).
Each claim cites >=1 reliable source and reflects 2022-2024 voting
record / public positions.

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
    # ---------------- Lauren Underwood (IL-14, D) ----------------
    ("lauren-underwood", "IL", "Representative", [
        claim("lu1", "lauren-underwood", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act of 2022 (H.R. 8296, House Vote #360, July 15, 2022), which would have federally protected abortion access through viability and in many cases beyond, explicitly pre-empting state personhood and heartbeat laws — directly opposing life-from-conception standards.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Lauren_Underwood"]),
        claim("lu2", "lauren-underwood", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022), which expanded background-check waiting periods for under-21 firearm buyers, closed the 'boyfriend loophole,' and funded state red-flag law programs — opposing the rubric's standard of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Lauren_Underwood"]),
        claim("lu3", "lauren-underwood", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R. 2, House Vote #209, May 11, 2023), which would have resumed border-wall construction, tightened asylum eligibility, and mandated deportation enforcement — opposing enforcement-first, secure-border immigration policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Lauren_Underwood"]),
    ]),

    # ---------------- Eric Sorensen (IL-17, D) ----------------
    ("eric-sorensen", "IL", "Representative", [
        claim("es1", "eric-sorensen", "sanctity_of_life", 0, False,
              "Voted NO on the Born Alive Abortion Survivors Protection Act (H.R. 26, House Vote #38, January 11, 2023), which would have required physicians to provide immediate medical care to infants born alive after a failed abortion attempt — opposing legal protection for life at birth.",
              ["https://www.govtrack.us/congress/votes/118-2023/h38",
               "https://ballotpedia.org/Eric_Sorensen"]),
        claim("es2", "eric-sorensen", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R. 2, House Vote #209, May 11, 2023), which would have resumed physical border-wall construction, tightened asylum standards, and strengthened deportation enforcement — opposing enforcement-first immigration policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Eric_Sorensen"]),
    ]),

    # ---------------- Brad Schneider (IL-10, D) ----------------
    ("brad-schneider", "IL", "Representative", [
        claim("bs1", "brad-schneider", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act of 2022 (H.R. 8296, House Vote #360, July 15, 2022), which would have established a federal statutory right to abortion through viability and pre-empted state personhood and heartbeat protections — rejecting life-from-conception standards.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Brad_Schneider"]),
        claim("bs2", "brad-schneider", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022), which expanded background checks for under-21 buyers, closed the 'boyfriend loophole,' and provided federal funding for state red-flag law programs — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Brad_Schneider"]),
        claim("bs3", "brad-schneider", "border_immigration", 0, False,
              "Voted NO on the Secure the Border Act of 2023 (H.R. 2, House Vote #209, May 11, 2023), which would have resumed border-wall construction, imposed tighter asylum caps, and required mandatory deportation enforcement — opposing enforcement-first immigration policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://ballotpedia.org/Brad_Schneider"]),
    ]),

    # ---------------- Bill Foster (IL-11, D) ----------------
    ("bill-foster", "IL", "Representative", [
        claim("bf1", "bill-foster", "sanctity_of_life", 0, False,
              "Voted YES on the Women's Health Protection Act of 2022 (H.R. 8296, House Vote #360, July 15, 2022), which would have created a federal right to abortion through viability and beyond in many cases, explicitly pre-empting state personhood laws — rejecting life-from-conception protections.",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://ballotpedia.org/Bill_Foster_(Illinois)"]),
        claim("bf2", "bill-foster", "economic_stewardship", 0, False,
              "A leading congressional CBDC proponent who introduced the Central Bank Digital Currency Study Act (H.R. 2211, 117th Congress) to accelerate development of a U.S. government-issued digital dollar, stating 'we need to make development of secure and effective digital currency a priority' — directly opposing the rubric's anti-CBDC position.",
              ["https://foster.house.gov/media/press-releases/foster-hill-introduce-bipartisan-legislation-to-spur-development-of-us-digital",
               "https://www.congress.gov/bill/117th-congress/house-bill/2211"]),
        claim("bf3", "bill-foster", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (S. 2938, House Vote #299, June 24, 2022), which expanded background-check waiting periods for young firearm buyers, closed the 'boyfriend loophole,' and funded state red-flag law programs — opposing the rubric's standard of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h299",
               "https://ballotpedia.org/Bill_Foster_(Illinois)"]),
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

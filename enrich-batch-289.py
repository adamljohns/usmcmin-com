#!/usr/bin/env python3
"""Enrichment batch 289: 3rd claims for 5 sitting US Representatives.

archetype_curated bucket is exhausted; this batch adds a 3rd evidential claim
to sitting members with exactly 2 existing claims, taken from the bottom of the
remaining alphabet (IN, IA, FL).

Targets (4 R / 1 R-moderate):
  Mark Messmer          (IN-08, R) — border: Laken Riley Act YES vote
  Jim Baird             (IN-04, R) — border: HR 2 Secure Border Act YES vote
  Jefferson Shreve      (IN-06, R) — border: Build the Wall Act sponsor
  Zach Nunn             (IA-03, R) — self-defense: Iowa strict-scrutiny amendment
  Scott Franklin        (FL-18, R) — border: HR 2 Secure Border Act YES vote

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB
warning.
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
    # ---------- Mark Messmer (IN-08, R — freshman 2025) ----------
    ("mark-messmer", "IN", "Representative", [
        claim("mm-b1", "mark-messmer", "border_immigration", 1, True,
              "Voted YES on H.R.29/S.5, the Laken Riley Act (H.R.29 passed the House 264–159 on Jan. 7, 2025; signed into law Jan. 29, 2025), which requires U.S. Immigration and Customs Enforcement to detain any undocumented immigrant arrested for burglary, theft, or a violent offense and prohibits their release pending removal proceedings — the first bill signed in the 119th Congress and a landmark expansion of mandatory-deportation grounds aligned with the rubric's enforcement standard. Messmer was sworn in Jan. 3, 2025, and voted with the unanimous Indiana Republican delegation.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://ballotpedia.org/Mark_Messmer"]),
    ]),

    # ---------- Jim Baird (IN-04, R) ----------
    ("jim-baird", "IN", "Representative", [
        claim("jb-b2", "jim-baird", "border_immigration", 0, True,
              "Voted YES on H.R.2, the Secure the Border Act of 2023 (passed 219–213 on May 11, 2023), which would resume construction of the southern border wall, reinstate the Migrant Protection Protocols ('Remain in Mexico'), tighten asylum eligibility, and expand expedited-removal authority — directly aligning with the rubric's wall-plus-military enforcement standard. Baird has publicly pledged to work with President Trump to 'secure our border, and put America First.'",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://baird.house.gov/"]),
    ]),

    # ---------- Jefferson Shreve (IN-06, R — freshman 2025) ----------
    ("jefferson-shreve", "IN", "Representative", [
        claim("js-b1", "jefferson-shreve", "border_immigration", 0, True,
              "Introduced H.R.816, the Build the Wall Act of 2025 (Jan. 28, 2025) as his first bill in Congress, redirecting unobligated COVID-19 State and Local Fiscal Recovery Funds to a new Southern Border Wall Construction Fund to finish building the southern border wall. The provision was subsequently included in the House-passed 'One Big Beautiful Bill' reconciliation package — advancing the rubric's wall-plus-military enforcement standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/816",
               "https://shreve.house.gov/media/press-releases/shreve-introduces-first-bill-congress-finish-building-southern-border-wall"]),
    ]),

    # ---------- Zach Nunn (IA-03, R) ----------
    ("zach-nunn", "IA", "Representative", [
        claim("zn-s1", "zach-nunn", "self_defense", 1, True,
              "As an Iowa State Senator (2018–2022), Nunn voted in support of the joint resolution that placed Iowa Amendment 1 on the November 2022 ballot, enshrining a strict-scrutiny fundamental right to keep and bear arms in the Iowa Constitution — which Iowa voters ratified 65–35 percent. As a U.S. Representative he has pledged to 'put a stop to any DC politicians who try to tell us how to act or how to defend our families,' opposing new federal gun-control mandates consistent with the rubric's anti-red-flag and anti-AWB standard.",
              ["https://ballotpedia.org/Iowa_Right_to_Firearms_Amendment_(2022)",
               "https://nunn.house.gov/"]),
    ]),

    # ---------- Scott Franklin (FL-18, R) ----------
    ("scott-franklin", "FL", "Representative", [
        claim("sf-b1", "scott-franklin", "border_immigration", 0, True,
              "Voted YES on H.R.2, the Secure the Border Act of 2023 (passed 219–213 on May 11, 2023), praising the bill as the 'Border Security Package' that would resume wall construction, reinstate 'Remain in Mexico,' and expand expedited-removal authority. Franklin publicly condemned the 'Biden Border Crisis' for allowing over 9 million illegal crossings and called on the administration to 'restore border security' — aligning with the rubric's wall-plus-military enforcement standard.",
              ["https://franklin.house.gov/news/documentsingle.aspx?DocumentID=379",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

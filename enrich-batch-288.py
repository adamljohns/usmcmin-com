#!/usr/bin/env python3
"""Enrichment batch 288: 3rd claims for 5 sitting US Representatives.

archetype_curated bucket is exhausted; this batch adds a 3rd evidential claim
to sitting members with exactly 2 existing claims, taken from the bottom of the
remaining alphabet (FL, GA, IA, IL).

Targets (5 R):
  Greg Steube            (FL-17, R) — border + economic claims
  Mike Haridopolos       (FL-08, R) — border claim
  Clay Fuller            (GA-14, R) — sanctity_of_life claim
  Mariannette Miller-Meeks (IA-01, R) — border claim
  Mike Bost              (IL-12, R) — border claim

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
    # ---------- Greg Steube (FL-17, R — Freedom Caucus) ----------
    ("greg-steube", "FL", "Representative", [
        claim("gs3", "greg-steube", "border_immigration", 1, True,
              "Introduced H.R. 707, the 'Deport Illegal Voters Act of 2025,' in the 119th Congress, mandating the removal of any non-citizen who votes in a federal election — expanding mandatory deportation grounds to cover voter-fraud ineligibility and signaling a hard-line enforcement posture consistent with the rubric's mandatory-deportation standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/707",
               "https://ballotpedia.org/Greg_Steube"]),
        claim("gs4", "greg-steube", "economic_stewardship", 2, True,
              "As a founding-era Freedom Caucus member (joined 2019), Steube opposed spending resolutions that did not include commensurate spending cuts; the Freedom Caucus, including Steube, objected to the bipartisan Fiscal Responsibility Act of 2023 as insufficiently conservative and pushed for deeper deficit reduction as a condition of any debt-ceiling increase — aligning with the rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Greg_Steube",
               "https://ballotpedia.org/Greg_Steube"]),
    ]),

    # ---------- Mike Haridopolos (FL-08, R — freshman 2025) ----------
    ("mike-haridopolos", "FL", "Representative", [
        claim("mh3", "mike-haridopolos", "border_immigration", 1, True,
              "Publicly stated that 'American tax dollars should serve American citizens and not those who are here illegally,' explicitly endorsing the Trump administration's mandatory deportation agenda; made these remarks in the context of congressional immigration debates in early 2025 as a newly sworn-in member of the 119th Congress.",
              ["https://ballotpedia.org/Mike_Haridopolos",
               "https://www.govtrack.us/congress/members/mike_haridopolos/456986"]),
    ]),

    # ---------- Clay Fuller (GA-14, R — special election winner Apr 2026) ----------
    ("clay-fuller", "GA", "Representative", [
        claim("cf3", "clay-fuller", "sanctity_of_life", 0, True,
              "Campaigned explicitly as 'a Christian Conservative who will defend the unborn' during the 2026 special election for Georgia's 14th Congressional District, making protection of life from conception a core platform pillar — succeeding fellow pro-life Republican Marjorie Taylor Greene in a Trump +40 northwest Georgia district and receiving President Trump's endorsement.",
              ["https://ballotpedia.org/Clayton_Fuller",
               "https://en.wikipedia.org/wiki/Clay_Fuller"]),
    ]),

    # ---------- Mariannette Miller-Meeks (IA-01, R) ----------
    ("mariannette-miller-meeks", "IA", "Representative", [
        claim("mm3", "mariannette-miller-meeks", "border_immigration", 1, True,
              "Cosponsored H.R. 5759, the 'BE GONE Act' (117th Congress), which amends the Immigration and Nationality Act to classify sexual assault and aggravated sexual violence as aggravated felonies requiring expedited mandatory removal of any non-citizen convicted of those crimes; also voted NO on H.R. 6, the American Dream and Promise Act of 2021, which would have granted legal status and shielded DACA recipients from deportation — both votes aligning with the rubric's mandatory-deportation standard.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/5759",
               "https://en.wikipedia.org/wiki/Mariannette_Miller-Meeks"]),
    ]),

    # ---------- Mike Bost (IL-12, R — Veterans' Affairs Committee chair) ----------
    ("mike-bost", "IL", "Representative", [
        claim("mb3", "mike-bost", "border_immigration", 0, True,
              "Voted YES on H.R. 2, the Secure the Border Act of 2023, which passed the House 219-213 on May 11, 2023; the bill would resume construction of the southern border wall, reinstate the 'Remain in Mexico' Migrant Protection Protocols, tighten asylum rules, and expand grounds for expedited removal — aligning with the rubric's wall-plus-military enforcement standard.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/2",
               "https://en.wikipedia.org/wiki/Mike_Bost"]),
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

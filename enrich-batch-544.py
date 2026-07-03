#!/usr/bin/env python3
"""Enrichment batch 544: 5 claims across 5 active 2026 federal candidates.

Targets evidence_curated U.S. Congress candidates with exactly 2 claims,
taken from the bottom of the remaining alphabet (MI, IA, MD, GA) after the
archetype_curated and higher-alphabet buckets were exhausted.

Targets (reverse alpha by state):
  Christina Hines     (MI-10, D primary candidate — former Washtenaw Co SVU prosecutor)
  Sarah Trone Garriott (IA-03, D nominee — IA state senator / Giffords-endorsed)
  Sarah Corkery       (IA-02, D candidate — 2024 nominee / advocate)
  Adrian Boafo        (MD-05, D nominee — former MD Delegate / won June 23 primary)
  Jasmine Clark       (GA-13, D nominee — GA state rep / won May 19 primary)

One distinct rubric-category claim per target (adding to their existing 2 claims).
Sources: christinahinesforcongress.com, macombdefenders.com, giffords.org,
iowapublicradio.org, pbs.org/video (Iowa Press), wikipedia.org,
ballotpedia.org, 19thnews.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ------------ Christina Hines (MI-10, D primary candidate) ------------
    ("christina-hines", "MI", "MI-10", [
        claim("chbi1a", "christina-hines", "border_immigration", 1, False,
              "Her official campaign platform lists 'Rein in ICE/DHS' and 'Overhaul ICE / DHS' as explicit policy positions, alongside a call to 'push back against Department of Homeland Security policies that destabilize families or target communities unfairly' — directly opposing the rubric's mandatory-deportation standard.",
              ["https://www.christinahinesforcongress.com/",
               "https://macombdefenders.com/voters-guide/"]),
    ]),

    # ------------ Sarah Trone Garriott (IA-03, D nominee) ------------
    ("sarah-trone-garriott", "IA", "IA-03", [
        claim("stgsd1a", "sarah-trone-garriott", "self_defense", 1, False,
              "Endorsed by the Giffords gun-control organization for her 2026 congressional bid and volunteers with Moms Demand Action for Gun Sense in America; supports universal background checks, mandatory safe-storage requirements, and mental-health-based firearm restrictions — policies the rubric opposes as infringements on constitutional carry and the right to keep arms without registration-style controls.",
              ["https://giffords.org/candidates/sarah-trone-garriott/",
               "https://iowasenatedemocrats.com/senator-sarah-trone-garriott/"]),
    ]),

    # ------------ Sarah Corkery (IA-02, D candidate) ------------
    ("sarah-corkery", "IA", "IA-02", [
        claim("scbi1a", "sarah-corkery", "border_immigration", 1, False,
              "Explicitly opposes mass deportation, arguing it would cause severe economic harm (predicting milk prices rising from $2 to $10 due to agricultural labor shortages) and supports a bipartisan immigration deal that includes a pathway to legal status for long-term residents — directly contradicting the rubric's mandatory-deportation ideal.",
              ["https://www.pbs.org/video/iowa-press-debates-2nd-congressional-district-yufl77/",
               "https://www.iowapublicradio.org/political-news/2024-10-23/what-iowa-candidates-for-congress-say-about-immigration-border"]),
    ]),

    # ------------ Adrian Boafo (MD-05, D nominee) ------------
    ("adrian-boafo", "MD", "MD-05", [
        claim("abbi2a", "adrian-boafo", "border_immigration", 2, False,
              "As a Maryland Delegate, introduced legislation to bar ICE officers hired during the second Trump administration from ever becoming Maryland state or local law enforcement officers — explicitly building a firewall between state police power and federal immigration enforcement in direct opposition to the rubric's anti-sanctuary standard.",
              ["https://en.wikipedia.org/wiki/Adrian_Boafo",
               "https://wtop.com/maryland-election/2026/02/long-list-of-candidates-running-for-congress-in-marylands-5th-district-gets-longer/"]),
    ]),

    # ------------ Jasmine Clark (GA-13, D nominee) ------------
    ("jasmine-clark-ga-13", "GA", "GA-13", [
        claim("jcsd1a", "jasmine-clark-ga-13", "self_defense", 1, False,
              "Pledged to push for a 'real assault weapon and bump stock ban,' comprehensive background checks, mandatory safe-storage laws, and federal legislation to hold gun manufacturers and the NRA accountable for gun violence — directly opposing the rubric's defense of semi-automatic firearms and resistance to registration-adjacent controls.",
              ["https://ballotpedia.org/Jasmine_Clark",
               "https://19thnews.org/2026/05/georgia-primary-election-jasmine-clark-congress/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

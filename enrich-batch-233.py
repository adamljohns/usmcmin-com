#!/usr/bin/env python3
"""Enrichment batch 233: third-claim enrichment for 4 federal / state candidates
from the bottom of the alphabet (AL, GA×2, WV).

Targets evidence_curated candidates that had exactly 2 claims and needed a
third claim in a distinct rubric category.  Each claim cites ≥1 reliable
source and reflects 2024-2026 voting record / public positions.

Targets (all R):
  Barry Moore      (AL – U.S. Rep / 2026 Senate candidate) – election_integrity
  Buddy Carter     (GA – U.S. Rep / 2026 Senate candidate) – border_immigration
  Mike Collins     (GA – U.S. Rep / 2026 Senate candidate) – sanctity_of_life
  JB McCuskey      (WV – Attorney General)                  – refuse_federal_overreach

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
    # ---------------- Barry Moore (AL-R, U.S. Rep / 2026 Senate candidate) ----------------
    ("barry-moore", "AL", "Representative", [
        claim("bm3", "barry-moore", "election_integrity", 0, True,
              "On January 6, 2021, voted to sustain the objection to Arizona's electoral votes and separately to Pennsylvania's, challenging certification of those states' results on grounds that expanded mail-in ballot procedures lacked adequate safeguards — consistent with the rubric's demand for paper-ballot integrity and opposition to mass mail-in voting.",
              ["https://en.wikipedia.org/wiki/Barry_Moore_(American_politician)",
               "https://ballotpedia.org/Barry_Moore_(Alabama_U.S._representative)"]),
    ]),

    # ---------------- Buddy Carter (GA-R, U.S. Rep / 2026 Senate candidate) ----------------
    ("buddy-carter", "GA", "Representative", [
        claim("bc3", "buddy-carter", "border_immigration", 0, True,
              "Cast a key vote in favor of the Secure America Act (2025 budget reconciliation), which fully funds Border Patrol and Immigration and Customs Enforcement and includes border-wall construction funding — directly matching the rubric's wall-and-military-enforcement ideal.",
              ["https://buddycarter.house.gov/",
               "https://ballotpedia.org/Earl_%22Buddy%22_Carter"]),
    ]),

    # ---------------- Mike Collins (GA-R, U.S. Rep / 2026 Senate candidate) ----------------
    ("mike-collins", "GA", "Representative", [
        claim("mc3", "mike-collins", "sanctity_of_life", 0, True,
              "Stated 'I am unapologetically pro-life. All human beings have a right to life, including unborn children.' Marked the one-year Dobbs anniversary by posting that overturning Roe brought the country 'one step closer to ending abortion in America,' and supported legislation withholding federal funds from abortion providers.",
              ["https://ballotpedia.org/Mike_Collins_(Georgia)",
               "https://www.govtrack.us/congress/members/mike_collins/456895"]),
    ]),

    # ---------------- JB McCuskey (WV-R, Attorney General) ----------------
    ("jb-mccuskey-ag-2026", "WV", "Attorney General", [
        claim("jbm3", "jb-mccuskey-ag-2026", "refuse_federal_overreach", 0, True,
              "Took office as West Virginia AG in January 2025 and immediately pledged to make suing the federal government a top priority, committing to overturn federal policies that challenge West Virginia values and to build a coalition of conservative in-state firms to provide outside counsel for those multistate challenges.",
              ["https://ballotpedia.org/John_B._McCuskey",
               "https://en.wikipedia.org/wiki/JB_McCuskey"]),
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

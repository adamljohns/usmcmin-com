#!/usr/bin/env python3
"""Enrichment batch 551: add 4th claims for 4 Senate candidates in bottom-alphabet states.

Primary buckets (archetype_curated / archetype_party_default federal with 0 claims) are
fully exhausted.  This batch adds a fourth claim to evidence_curated candidates who had
only 3 claims, working the WY→MN portion of the bottom-of-alphabet assignment.

Targets (1 MT-R, 1 MN-R, 2 MI-D):
  - Charles Walking Child  (MT-R, 2026 R Candidate · Daines seat)
  - Adam Schwarze          (MN-R, 2026 R Candidate · Smith seat)
  - Joe Tate               (MI-D, 2026 D Candidate · Peters seat)
  - Abdul El-Sayed         (MI-D, 2026 D Candidate · Peters seat)

Each new claim covers a category not yet represented in the candidate's existing 3 claims.
Scorecard written MINIFIED (separators=(",",":")) to stay under GitHub's 50 MB limit.
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
    # --- Charles Walking Child (MT-R, 2026 Senate candidate) ---
    ("charles-walking-child", "MT", "Senator", [
        claim("cwc1", "charles-walking-child", "border_immigration", 2, True,
              "Walking Child explicitly opposes sanctuary jurisdictions, stating that cities and counties "
              "that 'deliberately shield undocumented immigrants who have broken our laws' undermine "
              "federal immigration enforcement and 'endanger American citizens by protecting criminals "
              "from deportation'; he supports full local compliance with ICE detainers and operations.",
              ["https://ivoterguide.com/candidate/60272/race/27491/election/1419",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/charles-walking-child/"]),
    ]),

    # --- Adam Schwarze (MN-R, 2026 Senate candidate) ---
    ("adam-schwarze", "MN", "Senator", [
        claim("as1", "adam-schwarze", "biblical_marriage", 2, True,
              "On his campaign issues page, Schwarze pledges to 'keep men out of women's sports' and "
              "explicitly endorses the Protection of Women and Girls in Sports Act, noting that 'over "
              "80% of Americans support protecting girls' sports' while 'nearly every Democrat opposed' "
              "the bill; he has also publicly criticized Minnesota Democrats for 'inviting men into "
              "women's locker rooms,' reflecting a consistent rejection of transgender ideology.",
              ["https://www.schwarzeforsenate.com/issues/",
               "https://ballotpedia.org/Adam_Schwarze"]),
    ]),

    # --- Joe Tate (MI-D, 2026 Senate candidate) ---
    ("joe-tate-mi-senate", "MI", "Senator", [
        claim("jt1", "joe-tate-mi-senate", "border_immigration", 2, False,
              "As Michigan House Speaker, Tate co-introduced House Bills 4194–96 in March 2025 to grant "
              "driver's licenses and state IDs to undocumented immigrants regardless of legal status, "
              "while also barring the Michigan Secretary of State from sharing licensee data with federal "
              "authorities for immigration enforcement — a sanctuary-style data-sharing shield that "
              "directly conflicts with the rubric's anti-sanctuary standard.",
              ["https://www.detroitnews.com/story/news/politics/2025/03/20/michigan-undocumented-immigrants-drivers-licenses-bill-fails-illegal-immigration/82578119007/",
               "https://housedems.com/tate-carter-and-fitzgerald-introduce-bill-package-to-expand-access-to-drivers-licenses-and-id-cards-for-all-michiganders-2/"]),
    ]),

    # --- Abdul El-Sayed (MI-D, 2026 Senate candidate) ---
    ("abdul-el-sayed", "MI", "Senator", [
        claim("aes1", "abdul-el-sayed", "economic_stewardship", 2, False,
              "El-Sayed campaigns on Medicare for All as his signature economic platform plank — a "
              "federal single-payer system projected to add trillions to federal expenditures — paired "
              "with a 'billionaire tax' to fund it; this large-government expansion directly contradicts "
              "the rubric's standard of fiscal discipline, deficit restraint, and limited federal "
              "spending.",
              ["https://abdulforsenate.com/",
               "https://ballotpedia.org/Abdul_El-Sayed"]),
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

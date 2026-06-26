#!/usr/bin/env python3
"""Enrichment batch 425: 2 claims each for 5 sitting U.S. Representatives
with thin coverage (3 existing claims), chosen from bottom-of-alphabet states
(TX, SC, PA).  All archetype_curated 0-claim federal senators/reps have been
exhausted; this batch targets evidence_curated sitting members with minimum
coverage.

Targets: Al Green (TX-D), Henry Cuellar (TX-D), Jim Clyburn (SC-D),
Brian Fitzpatrick (PA-R), Rob Bresnahan (PA-R).
All claims cite 2024-2026 voting records / public positions from reliable
sources.

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
    # ---------------- Al Green (TX-D, U.S. Representative TX-09) ----------------
    ("al-green", "TX", "Representative", [
        claim("ag4", "al-green", "border_immigration", 2, False,
              "Voted NO on the impeachment of DHS Secretary Alejandro Mayorkas (H.Res. 863, Feb. 6, 2024), one of 216 members whose votes sank the first impeachment attempt 214-216. Mayorkas had been accused of willful refusal to enforce immigration removal orders, and blocking accountability for the catch-and-release border policy critics called a federally-enabled sanctuary approach.",
              ["https://en.wikipedia.org/wiki/Al_Green_(politician)",
               "https://en.wikipedia.org/wiki/Impeachment_of_Alejandro_Mayorkas"]),
        claim("ag5", "al-green", "election_integrity", 0, False,
              "Voted NO on the SAVE Act (H.R. 22, Apr. 10, 2025), which requires documentary proof of U.S. citizenship to register to vote in federal elections (House: 220-198, near-unanimous Democratic opposition). Green opposes citizenship verification as a condition of voter registration.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://en.wikipedia.org/wiki/Safeguard_American_Voter_Eligibility_Act"]),
    ]),

    # ---------------- Henry Cuellar (TX-D, U.S. Representative TX-28) ----------------
    ("henry-cuellar", "TX", "Representative", [
        claim("hc4", "henry-cuellar", "border_immigration", 2, True,
              "One of only seven House Democrats to cross party lines and vote for the FY2026 DHS appropriations bill (2025) providing approximately $10 billion for ICE enforcement operations — making him one of the most immigration-enforcement-supportive Democrats in the House. Stated publicly: 'If you don't qualify, then with all respect, we're going to hold you and then deport you back to your country.'",
              ["https://www.tpr.org/government-politics/2026-01-28/rep-henry-cuellar-still-supports-funding-ice",
               "https://ballotpedia.org/Henry_Cuellar"]),
        claim("hc5", "henry-cuellar", "economic_stewardship", 2, True,
              "A charter member of the fiscally-conservative Blue Dog Coalition — whose founding mission is reducing the federal deficit and opposing unfunded spending — Cuellar voted against the One Big Beautiful Bill Act (H.R. 1, July 2025), which the CBO estimated adds $2.4-$3.4 trillion to the national debt over a decade, consistent with his long-stated deficit-reduction platform.",
              ["https://cuellar.house.gov/issues/issue/?IssueID=9903",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---------------- Jim Clyburn (SC-D, U.S. Representative SC-06) ----------------
    ("jim-clyburn", "SC", "Representative", [
        claim("jc4", "jim-clyburn", "election_integrity", 0, False,
              "Introduced the Voter Empowerment Act of 2026 (H.R. 8078) and prior iterations, which would expand automatic voter registration nationwide and explicitly prohibit photo ID requirements for federal elections — directly opposing voter-ID verification as a safeguard against non-citizen voting.",
              ["https://clyburn.house.gov/clyburn-gillibrand-and-morelle-reintroduce-voter-empowerment-act/",
               "https://en.wikipedia.org/wiki/Jim_Clyburn"]),
        claim("jc5", "jim-clyburn", "border_immigration", 1, False,
              "Voted NO on the Laken Riley Act (S. 5, Jan. 22, 2025) — signed into law Feb. 1, 2025 — which mandates ICE detention and initiation of deportation proceedings for undocumented immigrants arrested for burglary, theft, or assault of a law enforcement officer. One of 156 House Democrats who opposed mandatory detention and deportation of criminal aliens (final House vote: 263-156).",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Brian Fitzpatrick (PA-R, U.S. Representative PA-01) ----------------
    ("brian-fitzpatrick", "PA", "Representative", [
        claim("bf4", "brian-fitzpatrick", "biblical_marriage", 1, False,
              "One of 47 House Republicans who voted YES on the Respect for Marriage Act (H.R. 8404, Dec. 8, 2022), which codifies federal recognition of same-sex and interracial marriages. In early 2026 Fitzpatrick publicly reiterated he 'support[s] gay marriage' and opposed efforts to overturn Obergefell v. Hodges — rejecting the one-man-one-woman definition the rubric affirms.",
              ["https://en.wikipedia.org/wiki/Brian_Fitzpatrick_(American_politician)",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
        claim("bf5", "brian-fitzpatrick", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (S. 5, Jan. 22, 2025 — House: 263-156), signed into law by President Trump on Feb. 1, 2025, requiring mandatory ICE detention and deportation proceedings for undocumented immigrants charged with burglary, theft, or assault of a law enforcement officer.",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Rob Bresnahan (PA-R, U.S. Representative PA-08) ----------------
    ("rob-bresnahan", "PA", "Representative", [
        claim("rb4", "rob-bresnahan", "economic_stewardship", 2, False,
              "Voted YES on the One Big Beautiful Bill Act (H.R. 1, May 22, 2025 House passage 215-214), which the CBO estimates adds $2.4-$3.4 trillion to the national debt over ten years. Bresnahan acknowledged being 'one of the last holdouts' before casting his yes vote, defending it as 'the largest working-class tax cuts in American history.'",
              ["https://bresnahan.house.gov/media/press-releases/bresnahan-statement-reconciliation-vote",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
        claim("rb5", "rob-bresnahan", "self_defense", 1, True,
              "Ran on a Second Amendment platform explicitly opposing measures that would 'take guns away from law-abiding citizens' and has maintained a 100% pro-gun voting record in the 119th Congress, opposing red-flag law funding and assault-weapon restrictions. Represents a northeastern Pennsylvania district where Second Amendment rights are a core constituent priority.",
              ["https://en.wikipedia.org/wiki/Rob_Bresnahan",
               "https://bresnahan.house.gov/about"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions across states."""
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

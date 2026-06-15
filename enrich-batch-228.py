#!/usr/bin/env python3
"""Enrichment batch 228: third-claim enrichment for 5 U.S. Representatives (LA, NM, NC).

Targets evidence_curated federal representatives at the bottom of the alphabet
with exactly 2 claims, adding one distinct-category claim each.

Mix (3 R / 2 D):
  Clay Higgins (LA-03-R), Yvette Herrell (NM-02-R),
  Richard Hudson (NC-09-R), Don Davis (NC-01-D), Alma Adams (NC-12-D).

Sources: congress.gov, govtrack.us, en.wikipedia.org, ballotpedia.org,
         wnct.com, clerk.house.gov.

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
    # ---------------- Clay Higgins (LA-03-R, U.S. Representative) ----------------
    ("clay-higgins", "LA", "Representative", [
        claim("ch3", "clay-higgins", "economic_stewardship", 2, True,
              "Higgins was one of 71 House Republicans who voted NO on final passage of the Fiscal Responsibility Act of 2023 (H.R.3746, House Vote #243, May 31, 2023, 314–117). The bill suspended the statutory debt ceiling through January 1, 2025 and imposed only modest discretionary spending caps. Higgins rejected it as insufficiently conservative — consistent with the rubric's anti-deficit, balanced-budget standard.",
              ["https://www.govtrack.us/congress/votes/118-2023/h243",
               "https://www.congress.gov/bill/118th-congress/house-bill/3746",
               "https://ballotpedia.org/Clay_Higgins"]),
    ]),

    # ---------------- Yvette Herrell (NM-02-R, U.S. Representative) ----------------
    ("yvette-herrell", "NM", "Representative", [
        claim("yh3", "yvette-herrell", "election_integrity", 0, True,
              "On January 6, 2021, Herrell voted to object to the certification of Arizona's and Pennsylvania's 2020 presidential electoral votes, citing election-integrity concerns about those states' ballot processes. The House rejected both objections (Arizona 121–303; Pennsylvania 138–282). Her votes reflect support for the principle that election procedures must satisfy rigorous scrutiny before results are certified — aligning with the rubric's election-integrity standard.",
              ["https://en.wikipedia.org/wiki/Yvette_Herrell",
               "https://ballotpedia.org/Yvette_Herrell",
               "https://ballotpedia.org/Counting_of_electoral_votes_(January_6-7,_2021)"]),
    ]),

    # ---------------- Richard Hudson (NC-09-R, U.S. Representative) ----------------
    ("richard-hudson", "NC", "Representative", [
        claim("rh3", "richard-hudson", "border_immigration", 1, True,
              "Voted for S.5, the Laken Riley Act (119th Congress), which requires the Secretary of Homeland Security to mandatorily detain illegal immigrants who have been charged with or convicted of theft, burglary, or violent crimes. The bill passed the House 263–156 on January 22, 2025, and was signed into law on January 29, 2025 — the first bill enacted in the 119th Congress. This aligns with the rubric's mandatory-deportation/enforcement standard.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://www.govtrack.us/congress/bills/119/s5",
               "https://ballotpedia.org/Richard_Hudson"]),
    ]),

    # ---------------- Don Davis (NC-01-D, U.S. Representative) ----------------
    ("don-davis", "NC", "Representative", [
        claim("dd3", "don-davis", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (H.R. 29, House Roll Call 6, January 7, 2025, 264–159), one of only 46 House Democrats to cross party lines — and the only North Carolina Democrat to do so. Davis issued a press release praising the bill as 'a vital piece of legislation that addresses critical failures in our immigration enforcement system.' The Laken Riley Act mandates DHS detention of illegal immigrants charged with theft or violent crimes, aligning with the rubric's mandatory-enforcement standard.",
              ["https://www.wnct.com/local-news/congressman-don-davis-votes-in-favor-of-laken-riley-act/",
               "https://dondavis.house.gov/media/press-releases/congressman-don-davis-votes-again-laken-riley-act",
               "https://clerk.house.gov/Votes/20256"]),
    ]),

    # ---------------- Alma Adams (NC-12-D, U.S. Representative) ----------------
    ("alma-adams", "NC", "Representative", [
        claim("aa3", "alma-adams", "border_immigration", 1, False,
              "Voted NO on S.5, the Laken Riley Act (House Roll Call 23, January 22, 2025, 263–156), which requires mandatory DHS detention of illegal immigrants charged with theft, burglary, or violent crimes. Adams did not cross party lines; as local reporting confirmed, Rep. Don Davis was 'the only Democrat from North Carolina' to vote for the bill. Her NO vote opposes the rubric's mandatory-deportation/enforcement standard.",
              ["https://clerk.house.gov/Votes/202523",
               "https://www.wnct.com/local-news/congressman-don-davis-votes-in-favor-of-laken-riley-act/",
               "https://www.govtrack.us/congress/members/alma_adams/412607"]),
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

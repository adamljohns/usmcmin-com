#!/usr/bin/env python3
"""Enrichment batch 227: third-claim enrichment for 5 NY U.S. Representatives.

Targets evidence_curated federal representatives at the bottom of the alphabet
with exactly 2 claims, adding one distinct-category claim each.

Mix (2 R / 3 D — wait, actually 3 R / 2 D):
  Yvette Clarke (NY-09-D), Tim Kennedy (NY-26-D),
  Nicole Malliotakis (NY-11-R), Nick Langworthy (NY-23-R), Nick LaLota (NY-01-R).

Sources: congress.gov, govtrack.us, en.wikipedia.org, ballotpedia.org.

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
    # ---------------- Yvette Clarke (NY-09-D, U.S. Representative) ----------------
    ("yvette-clarke", "NY", "Representative", [
        claim("yc3", "yvette-clarke", "self_defense", 1, False,
              "Clarke was an original cosponsor of the Assault Weapons Ban of 2022 (H.R. 1808, cosponsor date March 11, 2021), which passed the House on July 29, 2022 (House Vote #410, 217–213). The bill would have banned the manufacture, sale, and transfer of semiautomatic assault-style rifles and high-capacity magazines — directly opposing the rubric's standard against assault-weapons bans and magazine restrictions.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/1808/cosponsors",
               "https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://ballotpedia.org/Yvette_Clarke"]),
    ]),

    # ---------------- Tim Kennedy (NY-26-D, U.S. Representative) ----------------
    ("tim-kennedy", "NY", "Representative", [
        claim("tk3", "tim-kennedy", "biblical_marriage", 2, False,
              "Kennedy cosponsored the Equality Act (H.R. 15, 119th Congress) on April 29, 2025, which would amend federal civil-rights law to prohibit discrimination based on sexual orientation and gender identity in employment, housing, education, and public accommodations — an explicit endorsement of transgender legal protections that opposes the rubric's rejection of transgender ideology.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/15/cosponsors",
               "https://www.govtrack.us/congress/members/timothy_kennedy/456957",
               "https://ballotpedia.org/Tim_Kennedy_(New_York)"]),
    ]),

    # ---------------- Nicole Malliotakis (NY-11-R, U.S. Representative) ----------------
    ("nicole-malliotakis", "NY", "Representative", [
        claim("nm3", "nicole-malliotakis", "biblical_marriage", 1, False,
              "Malliotakis was one of 47 Republicans to vote YES on the Respect for Marriage Act (H.R. 8404) on July 19, 2022, and again voted YES on the final bipartisan version on December 8, 2022 (House Vote #479, 258–169). The law repeals the Defense of Marriage Act and requires federal and state governments to recognize same-sex marriages — placing her among the minority of House Republicans who rejected the one-man-one-woman marriage standard the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Nicole_Malliotakis",
               "https://www.govtrack.us/congress/votes/117-2022/h479",
               "https://ballotpedia.org/Nicole_Malliotakis"]),
    ]),

    # ---------------- Nick Langworthy (NY-23-R, U.S. Representative) ----------------
    ("nick-langworthy", "NY", "Representative", [
        claim("nl3", "nick-langworthy", "election_integrity", 0, True,
              "Voted YES on the SAVE Act (H.R. 22, House Vote #102, April 10, 2025; passed 220–208 with every Republican voting in favor), which requires documentary proof of U.S. citizenship to register to vote in any federal election — a strong voter-eligibility safeguard aligned with the rubric's election-integrity standard for verified-identity voter registration.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Nick_Langworthy"]),
    ]),

    # ---------------- Nick LaLota (NY-01-R, U.S. Representative) ----------------
    ("nick-lalota", "NY", "Representative", [
        claim("nll3", "nick-lalota", "biblical_marriage", 0, False,
              "In 2026 LaLota publicly expressed opposition to banning same-sex marriage, repealing the Respect for Marriage Act, or otherwise undermining the Obergefell v. Hodges decision — a stated commitment to preserving federally recognized same-sex marriage that places him outside the rubric's one-man-one-woman marriage standard.",
              ["https://en.wikipedia.org/wiki/Nick_LaLota",
               "https://ballotpedia.org/Nicholas_J._LaLota"]),
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

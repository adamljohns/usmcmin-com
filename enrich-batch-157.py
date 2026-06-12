#!/usr/bin/env python3
"""Enrichment batch 157: 3rd claim for 5 sitting U.S. Representatives.

Targets evidence_curated House members with only 2 claims (archetype_curated
pool is fully exhausted). Bottom-of-alphabet selection: Kiggans (VA), Maloy
(UT), Moore (UT), Williams (TX), Moran (TX). Each gets a claim in a distinct
rubric category from the two already recorded.

Sources: official House pages, congress.gov, ballotpedia.org, sbaprolife.org,
govtrack.us, moran.house.gov.

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
    # ---------------- Jen Kiggans (VA-02, R) ----------------
    ("jen-kiggans", "VA", "House", [
        claim("jk1", "jen-kiggans", "election_integrity", 0, True,
              "Voted for the Safeguard American Voter Eligibility (SAVE) Act (H.R.22, 119th Congress), which requires documentary proof of U.S. citizenship to register to vote in federal elections and mandates states to remove non-citizens from voter rolls — directly supporting voter-ID and citizenship-verification goals. Kiggans stated she supports policies that 'make it easy to vote, but hard to cheat,' including maintaining photo ID requirements, preventing ballot harvesting, and ensuring state election officials can secure the federal election process.",
              ["https://kiggans.house.gov/posts/kiggans-votes-to-preserve-the-integrity-of-americas-federal-elections",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------------- Celeste Maloy (UT-02, R) ----------------
    ("celeste-maloy", "UT", "Representative", [
        claim("cm1", "celeste-maloy", "self_defense", 1, True,
              "Publicly pledges to oppose all efforts to weaken or infringe the Second Amendment, stating 'the 2nd Amendment is clear — the right of the people to keep and bear Arms, shall not be infringed,' and vowing to 'fight the gun grabbers in Washington DC.' This blanket opposition to new restrictions aligns with the rubric's rejection of red-flag laws, assault-weapons bans, magazine limits, and universal-background-check expansion.",
              ["https://maloy.house.gov/issues/issue/?IssueID=15140",
               "https://ballotpedia.org/Celeste_Maloy"]),
    ]),

    # ---------------- Blake Moore (UT-01, R) ----------------
    ("blake-moore", "UT", "Representative", [
        claim("bm1", "blake-moore", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and a consistent pro-life voting record: has voted to stop taxpayer funding for abortion domestically and internationally, to protect health-care providers who refuse to perform abortions, and celebrated the Dobbs ruling as restoring to states 'the right to protect the lives of millions of children.' Moore also supported the H.R.1 reconciliation package that included a one-year Medicaid defunding of Planned Parenthood.",
              ["https://sbaprolife.org/representative/blake-moore",
               "https://blakemoore.house.gov/issue/family-pro-life-issues"]),
    ]),

    # ---------------- Roger Williams (TX-25, R) ----------------
    ("roger-williams", "TX", "Representative", [
        claim("rw1", "roger-williams", "border_immigration", 0, True,
              "A consistent border-security vote: cosponsored the Border Safety and Security Act (H.R.29, 118th Congress) and supported the Secure the Border Act (H.R.2, 118th Congress), which mandates resumption of border-wall construction, requires all employers to use E-Verify to reduce illegal-immigration incentives, and reinstates Remain-in-Mexico — aligning with the rubric's wall-plus-enforcement ideal.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/29/cosponsors",
               "https://ballotpedia.org/Roger_Williams_(Texas)"]),
    ]),

    # ---------------- Nathaniel Moran (TX-01, R) ----------------
    ("nathaniel-moran", "TX", "Representative", [
        claim("nm1", "nathaniel-moran", "border_immigration", 0, True,
              "A leading House voice for border enforcement: led and passed a House resolution (225-187) condemning Biden's open-border policies; sponsored the Visa Overstays Penalties Act to reclassify visa overstays as illegal entry with heightened criminal penalties; supported H.R.2 (Secure the Border Act, including wall construction and E-Verify mandate); and applauded passage of the Laken Riley Act strengthening mandatory deportation enforcement.",
              ["https://moran.house.gov/news/documentsingle.aspx?DocumentID=299",
               "https://moran.house.gov/news/documentsingle.aspx?DocumentID=111",
               "https://moran.house.gov/news/documentsingle.aspx?DocumentID=729"]),
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

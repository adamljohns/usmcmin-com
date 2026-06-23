#!/usr/bin/env python3
"""Enrichment batch 384: additional claims for 5 sitting Texas U.S. Representatives.

All five are evidence_curated candidates (already 3 claims each) from TX,
taken from the bottom of the alphabet bucket. Adds 2 new claims each in
rubric categories not yet scored.

Targets (all TX-R):
  Pete Sessions (TX-17), Pat Fallon (TX-4), Nathaniel Moran (TX-1),
  Michael Cloud (TX-27), Monica De La Cruz (TX-15).

Sources: official .house.gov press releases, congress.gov, ballotpedia.org.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace).
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
    # -------- Pete Sessions (TX-17, U.S. Representative) --------
    ("pete-sessions", "TX", "Representative", [
        claim("ps1", "pete-sessions", "election_integrity", 0, True,
              "Congressman Sessions proudly cosponsored H.R. 8281, the Safeguard American Voter Eligibility (SAVE) Act in the 118th Congress (July 2024), requiring documentary proof of U.S. citizenship for voter registration in federal elections. His press release called on the Senate to 'quickly take up this important piece of legislation.'",
              ["https://sessions.house.gov/2024/7/congressman-sessions-cosponsors-save-act-to-protect-election-integrity",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281"]),
        claim("ps2", "pete-sessions", "biblical_marriage", 1, False,
              "Sessions was one of 39 Republicans who voted for the Respect for Marriage Act (H.R. 8404) on final passage December 8, 2022 (258–169), codifying federal recognition of same-sex marriages and repealing the Defense of Marriage Act definition of marriage as the union of a man and a woman — directly opposing the rubric's one-man-one-woman standard.",
              ["https://www.washingtonpost.com/politics/interactive/2022/republican-marriage-equality-vote-count/",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
    ]),

    # -------- Pat Fallon (TX-4, U.S. Representative) --------
    ("pat-fallon", "TX", "Representative", [
        claim("pf1", "pat-fallon", "economic_stewardship", 0, True,
              "Fallon was an original cosponsor of H.R. 5403, the CBDC Anti-Surveillance State Act (118th Congress), which passed the House 216–192 on May 23, 2024. The bill prohibits Federal Reserve banks from issuing a central bank digital currency directly to individuals, blocking a government surveillance-capable digital dollar — aligning with the rubric's anti-CBDC standard.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5403",
               "https://www.govtrack.us/congress/votes/118-2024/h230"]),
        claim("pf2", "pat-fallon", "election_integrity", 0, True,
              "Fallon cosponsored H.R. 8281, the Safeguard American Voter Eligibility (SAVE) Act (118th Congress), which passed the House 221–198 on July 10, 2024, requiring states to obtain proof of U.S. citizenship before registering individuals to vote in federal elections and creating programs to remove non-citizens from voter rolls.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/8281",
               "https://fallon.house.gov/voterecord/"]),
    ]),

    # -------- Nathaniel Moran (TX-1, U.S. Representative) --------
    ("nathaniel-moran", "TX", "Representative", [
        claim("nm1", "nathaniel-moran", "self_defense", 0, True,
              "Rep. Moran joined over 120 colleagues in cosponsoring the Constitutional Concealed Carry Reciprocity Act, which provides nationwide reciprocity for concealed carry license holders and residents of constitutional-carry states. Moran stated: 'The Second Amendment rights of law-abiding citizens should not end at the state line.'",
              ["https://moran.house.gov/news/documentsingle.aspx?DocumentID=925",
               "https://www.congress.gov/member/nathaniel-moran/M001224"]),
        claim("nm2", "nathaniel-moran", "election_integrity", 0, True,
              "Congressman Moran voted to protect American election integrity on the House floor in July 2024, supporting H.R. 8281, the Safeguard American Voter Eligibility (SAVE) Act requiring documentary proof of U.S. citizenship for voter registration in federal elections — aligning with the rubric's voter-ID and proof-of-citizenship standard.",
              ["https://moran.house.gov/news/documentsingle.aspx?DocumentID=580",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281"]),
    ]),

    # -------- Michael Cloud (TX-27, U.S. Representative) --------
    ("michael-cloud", "TX", "Representative", [
        claim("mc1", "michael-cloud", "election_integrity", 0, True,
              "Rep. Cloud publicly expressed disappointment when the government-funding bill containing the SAVE Act — which would have required proof of citizenship to register to vote in federal elections — failed to pass, calling it a critical safeguard for election security. He is a consistent advocate for proof-of-citizenship voter registration requirements.",
              ["https://cloud.house.gov/posts/release-rep-cloud-expresses-disappointment-after-funding-bill-that-would-secure-american-elections-fails-to-pass",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("mc2", "michael-cloud", "economic_stewardship", 1, True,
              "Rep. Cloud cosponsored H.R. 24, the Federal Reserve Transparency Act of 2025 (119th Congress), introduced by Rep. Massie, requiring a full audit of the Board of Governors of the Federal Reserve System and all Federal Reserve banks by the Comptroller General — fulfilling the rubric's sound-money/audit-the-Fed standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/24/text",
               "https://cloud.house.gov/"]),
    ]),

    # -------- Monica De La Cruz (TX-15, U.S. Representative) --------
    ("monica-de-la-cruz", "TX", "Representative", [
        claim("mdlc1", "monica-de-la-cruz", "election_integrity", 0, True,
              "Rep. De La Cruz voted FOR H.R. 8281, the Safeguard American Voter Eligibility (SAVE) Act on July 10, 2024, which prohibits states from registering individuals to vote in federal elections without documentary proof of U.S. citizenship. Her office issued a press release explicitly supporting proof-of-citizenship voter registration.",
              ["https://delacruz.house.gov/news/documentsingle.aspx?DocumentID=1928",
               "https://www.congress.gov/bill/118th-congress/house-bill/8281"]),
        claim("mdlc2", "monica-de-la-cruz", "economic_stewardship", 0, True,
              "Rep. De La Cruz cosponsored H.R. 5403, the CBDC Anti-Surveillance State Act (118th Congress, 2023), which prohibits Federal Reserve banks from issuing a central bank digital currency directly to individuals, blocking a government-controlled surveillance digital dollar. She later cosponsored the successor Anti-CBDC Surveillance State Act (H.R. 1919) in the 119th Congress.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5403",
               "https://www.congress.gov/bill/119th-congress/house-bill/1919/all-info"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

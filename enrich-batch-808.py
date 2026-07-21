#!/usr/bin/env python3
"""Enrichment batch 808: 10 verified claims across 4 active 2026 R candidates.

Targets (bottom-of-alphabet states, 3 existing claims each):
  Rob Mercuri    (PA-17 · 2026 R Candidate · former state rep / West Point)
  Brinker Harding (NE-02 · 2026 R Nominee · Trump-endorsed · Omaha Council VP)
  Brad Knott     (NC-13 · US Rep · freshman 119th Congress / former DA)
  Adrian Smith   (NE-03 · US Rep · sitting since 2007 / Ways & Means)

Each candidate gains claims in DISTINCT rubric categories not yet covered.
Sources: congress.gov, govtrack.us, clerk.house.gov, ivoterguide, campaign sites.

MINIFIED write preserves master under GitHub 50 MB limit.
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
    # -------- Rob Mercuri (PA-17 · 2026 R Candidate) --------
    ("rob-mercuri", "PA", "PA-17", [
        claim("rm1", "rob-mercuri", "election_integrity", 0, True,
              "Co-sponsored Pennsylvania's 2021 Voting Rights Protection Act (HB 1300), which required photo ID at every poll, restricted mail-ballot drop boxes to one per county plus one per 100,000 residents, moved the mail-ballot request deadline back to 15 days before Election Day, and created a Bureau of Election Audits — later publishing a press release titled 'Voting Security, Integrity Non-Negotiable.' Gov. Wolf vetoed the bill on June 30, 2021.",
              ["https://legiscan.com/PA/bill/HB1300/2021",
               "https://www.reprobmercuri.com/News-Print/19996/Latest-News/Mercuri-%E2%80%98Voting-Security,-Integrity-Non-Negotiable%E2%80%99-"]),
        claim("rm2", "rob-mercuri", "christian_liberty", 0, True,
              "Stated 'Religious liberty is at risk in the United States and deserves the highest level of protection in the law,' identifying as 'a life-long Christian, saved by grace through faith,' and pledging 'to protect the freedom of Christians to share the Gospel and to practice Biblical principles' while supporting 'complete freedom of religious expression without restriction or restraint by the state.'",
              ["https://ivoterguide.com/candidate/52703/race/1792/election/778"]),
        claim("rm3", "rob-mercuri", "family_child_sovereignty", 0, True,
              "Pledged to pass 'a parental bill of rights for education' and supports school choice including 'voucher programs, tax credits, charter schools, private schools, and home schools'; also supports eliminating the U.S. Department of Education and returning educational control to 'states and communities.'",
              ["https://ivoterguide.com/candidate/52703/race/1792/election/778"]),
    ]),

    # -------- Brinker Harding (NE-02 · 2026 R Nominee) --------
    ("brinker-harding", "NE", "NE-02", [
        claim("bh1", "brinker-harding", "economic_stewardship", 2, True,
              "Campaign platform pledges to 'fight to grow our economy and eliminate wasteful spending to increase revenues and reduce our deficit' and to 'stop reckless spending that fuels inflation and threatens Social Security & Medicare,' while cutting taxes for working families and small businesses.",
              ["https://www.brinkerharding.com/vision",
               "https://nebraskaexaminer.com/2025/07/01/omaha-city-council-vp-brinker-harding-jumps-into-nebraska-2nd-district-u-s-house-race/"]),
    ]),

    # -------- Brad Knott (NC-13 · US Rep · 119th Congress) --------
    ("brad-knott", "NC", "Representative", [
        claim("bk1", "brad-knott", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (H.R. 29, Roll Call 6, January 7, 2025), which passed 263-156 requiring federal detention of illegal immigrants who commit theft or violent crimes; stated: 'As a federal prosecutor, I saw firsthand how criminal illegal immigrants disregard our laws with intent on causing harm to Americans... I'm proud to vote for the Laken Riley Act to ensure illegal immigrants like Laken's killer will be detained.'",
              ["https://clerk.house.gov/Votes/20256",
               "https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.carolinajournal.com/nc-lawmakers-vote-to-pass-laken-riley-act/"]),
        claim("bk2", "brad-knott", "self_defense", 0, True,
              "Co-sponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025 (119th Congress, 188 Republican co-sponsors), which would require all states to honor valid concealed carry permits from any other state — affirming that Second Amendment rights have no geographic limits within U.S. borders.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/all-info",
               "https://www.govtrack.us/congress/bills/119/hr38/cosponsors"]),
        claim("bk3", "brad-knott", "economic_stewardship", 2, True,
              "Signed the Americans for Tax Reform Taxpayer Protection Pledge and voted YES on the One Big Beautiful Bill Act (H.R. 1, Roll Call 190, July 3, 2025), which permanently extended 2017 TCJA tax rates and made major spending reductions; earns a 96% Heritage Action scorecard rating for fiscal conservatism in the 119th Congress.",
              ["https://atr.org/bradd-knott-signs-taxpayer-protection-pledge/",
               "https://knott.house.gov/media/press-releases/knott-votes-pass-president-trumps-one-big-beautiful-bill",
               "https://heritageaction.com/scorecard/members/K000405"]),
    ]),

    # -------- Adrian Smith (NE-03 · US Rep · since 2007) --------
    ("adrian-smith", "NE", "House", [
        claim("as1", "adrian-smith", "election_integrity", 0, True,
              "Voted YES on the SAVE America Act (H.R. 7296, February 11, 2026), which passed 218-213 and requires photo ID to vote in federal elections and proof of U.S. citizenship to register; issued a named press release: 'Today's passage of the SAVE America Act marks an important first step toward strengthening safeguards, improving accountability, and reinforcing public trust in our democratic process.'",
              ["https://adriansmith.house.gov/media/press-releases/smith-celebrates-house-passage-save-america-act-strengthen-election-integrity"]),
        claim("as2", "adrian-smith", "family_child_sovereignty", 0, True,
              "Lead House author and Ways and Means champion of the Educational Choice for Children Act (ECCA) provisions included in the One Big Beautiful Bill (H.R. 1, signed July 4, 2025), creating the first-ever federal school-choice program — a $5 billion annual tax credit for donations to nonprofit scholarship organizations serving K-12 students; Nebraska was the first state to opt in.",
              ["https://adriansmith.house.gov/media/press-releases/smith-bill-expand-school-choice-passed-ways-and-means-committee",
               "https://www.congress.gov/bill/119th-congress/house-bill/1/history"]),
        claim("as3", "adrian-smith", "economic_stewardship", 0, True,
              "Voted YES on the CBDC Anti-Surveillance State Act (H.R. 5403, Roll Call 230, May 23, 2024), which passed 216-192 on a near-party-line vote (zero Republican no-votes) and prohibits the Federal Reserve from issuing a central bank digital currency directly to individuals or using a CBDC to implement monetary policy.",
              ["https://clerk.house.gov/Votes/2024230",
               "https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://www.congress.gov/bill/118th-congress/house-bill/5403"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing wrong-state same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

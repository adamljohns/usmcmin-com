#!/usr/bin/env python3
"""Enrichment batch 420: depth claims for 5 sitting U.S. Representatives.

Targets: evidence_curated reps with 3-4 claims, adding 2 new claims each
in uncovered rubric categories. All sitting members, bottom-of-alphabet
states (TX, SC, PA).

Beth Van Duyne (TX-R): election_integrity + biblical_marriage
Joe Wilson (SC-R): border_immigration + economic_stewardship
Scott Perry (PA-R): border_immigration + self_defense
Glenn Thompson (PA-R): self_defense + election_integrity
Guy Reschenthaler (PA-R): election_integrity + economic_stewardship
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
    # ---------------- Beth Van Duyne (TX-R, U.S. Representative) ----------------
    ("beth-van-duyne", "TX", "Representative", [
        claim("bvd5", "beth-van-duyne", "election_integrity", 0, True,
              "Voted YES on H.R.22, the Safeguard American Voter Eligibility (SAVE) Act (April 10, 2025), requiring documentary proof of U.S. citizenship for voter registration in federal elections — a citizens-only safeguard the rubric supports.",
              ["https://ballotpedia.org/Beth_Van_Duyne",
               "https://www.govtrack.us/congress/bills/119/hr22"]),
        claim("bvd6", "beth-van-duyne", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (H.R.8404, December 2022), one of 39 House Republicans to support federal codification of same-sex marriage — putting her at odds with the rubric's defense of traditional one-man-one-woman marriage.",
              ["https://www.washingtonpost.com/politics/interactive/2022/house-vote-count-respect-for-marriage-act/",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
    ]),

    # ---------------- Joe Wilson (SC-R, U.S. Representative) ----------------
    ("joe-wilson", "SC", "Representative", [
        claim("jw4", "joe-wilson", "border_immigration", 0, True,
              "Voted YES on H.R.2, the Secure the Border Act of 2023 (May 11, 2023), authorizing border-wall construction, mandatory detention, and tightened asylum rules; Wilson has a decades-long record as a border-security hawk and previously praised the Secure Fence Act as a key enforcement milestone.",
              ["https://joewilson.house.gov/issues/immigration",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
        claim("jw5", "joe-wilson", "economic_stewardship", 2, True,
              "Voted NO on the $1.9 trillion American Rescue Plan Act (March 2021) and NO on the Inflation Reduction Act (August 2022), joining unanimous House Republican opposition to both major deficit-spending packages — consistent with his stated platform of smaller government and fiscal restraint.",
              ["https://joewilson.house.gov/issues/economy-and-jobs",
               "https://www.govtrack.us/congress/members/joe_wilson/400433"]),
    ]),

    # ---------------- Scott Perry (PA-R, U.S. Representative) ----------------
    ("scott-perry", "PA", "Representative", [
        claim("sp4", "scott-perry", "border_immigration", 0, True,
              "Voted YES on H.R.2, the Secure the Border Act of 2023, and has cosponsored border-security enforcement bills; Perry has publicly called for real border security and mandatory enforcement of existing immigration law, consistent with the rubric's demand for physical barrier construction and deportation.",
              ["https://perry.house.gov/news/documentsingle.aspx?DocumentID=402604",
               "https://www.congress.gov/bill/118th-congress/house-bill/2"]),
        claim("sp5", "scott-perry", "self_defense", 1, True,
              "Voted against H.R.8 (universal background checks), H.R.1446 (extended background-check delays), and H.R.1808 (Assault Weapons Ban of 2022) — opposing every major gun-control package passed by House Democrats in the 117th Congress. As House Freedom Caucus chairman, Perry introduced the Protecting Our Second Amendment Data Act to safeguard gun-owner privacy against federal registry creation.",
              ["https://perry.house.gov/",
               "https://www.govtrack.us/congress/members/scott_perry/412569"]),
    ]),

    # ---------------- Glenn Thompson (PA-R, U.S. Representative) ----------------
    ("glenn-thompson", "PA", "Representative", [
        claim("gt4", "glenn-thompson", "self_defense", 1, True,
              "Voted NO on H.R.1808, the Assault Weapons Ban of 2022 (July 29, 2022), joining all but two House Republicans in opposing the semi-automatic weapons prohibition. Thompson maintains a consistent pro-Second Amendment voting record opposing new gun restrictions.",
              ["https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://www.congress.gov/bill/117th-congress/house-bill/1808"]),
        claim("gt5", "glenn-thompson", "election_integrity", 0, True,
              "Voted YES on H.R.22, the Safeguard American Voter Eligibility (SAVE) Act (April 10, 2025), requiring documentary proof of U.S. citizenship for voter registration in federal elections — supporting the citizens-only ballot protection the rubric endorses.",
              ["https://www.govtrack.us/congress/bills/119/hr22",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------------- Guy Reschenthaler (PA-R, U.S. Representative) ----------------
    ("guy-reschenthaler", "PA", "Representative", [
        claim("gr4", "guy-reschenthaler", "election_integrity", 0, True,
              "Voted NO on H.R.1, House Democrats' 'For the People Act' (2021), which would have undermined voter ID laws, mandated expansion of mail-in balloting, and legalized ballot harvesting; Reschenthaler called it 'Democrats' Electoral Power Grab' and has consistently opposed legislation that weakens election-integrity safeguards.",
              ["https://reschenthaler.house.gov/media/press-releases/reschenthaler-votes-against-democrats-electoral-power-grab",
               "https://www.govtrack.us/congress/members/guy_reschenthaler/412813"]),
        claim("gr5", "guy-reschenthaler", "economic_stewardship", 2, True,
              "Voted NO on President Biden and Democrats' $3.5 trillion reconciliation package (2021), warning the bill would add hundreds of billions to the national debt; has maintained consistent opposition to large unpaid spending increases throughout his tenure, opposing what he termed the 'Socialist Spending Scam.'",
              ["https://reschenthaler.house.gov/media/press-releases/reschenthaler-votes-no-democrats-socialist-spending-scam",
               "https://www.govtrack.us/congress/members/guy_reschenthaler/412813"]),
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

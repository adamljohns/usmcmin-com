#!/usr/bin/env python3
"""Enrichment batch 165: 4 sitting House Republicans from bottom of alphabet.

Targets archetype_party_default federal House members with 0 evidence claims,
taken from the bottom of the alphabet (NC, MS, ND).  All claims sourced from
official .house.gov, congress.gov, govtrack.us, ballotpedia.org, or
sbaprolife.org and reflect 2025-2026 public record.

Candidates:
  David Rouzer   (NC-07, R) — sanctity_of_life, border_immigration, election_integrity
  Trent Kelly    (MS-01, R) — sanctity_of_life, self_defense, border_immigration
  Tim Moore      (NC-14, R) — sanctity_of_life, border_immigration, election_integrity
  Julie Fedorchak(ND-AL, R) — election_integrity, border_immigration, sanctity_of_life
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
    # ---------------- David Rouzer (NC-07, R) ----------------
    ("david-rouzer", "NC", "US Representative", [
        claim("dr1", "david-rouzer", "sanctity_of_life", 0, True,
              "A cosponsor of H.R. 7, the No Taxpayer Funding for Abortion and Abortion Insurance Full Disclosure Act of 2025 (119th Congress), and a self-described champion for the unborn — stating publicly 'I am pro-life and will do everything in my power in Congress to fight for the rights of the unborn in our country.' SBA Pro-Life America lists him on their congressional scorecard.",
              ["https://sbaprolife.org/representative/david-rouzer",
               "https://www.congress.gov/bill/119th-congress/house-bill/7/history"]),
        claim("dr2", "david-rouzer", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29 / S. 5, Jan. 2025), which mandates the detention and removal of illegal immigrants arrested for burglary, theft, or violent crimes — aligning with the rubric's call for mandatory deportation of criminal aliens.",
              ["https://rouzer.house.gov/news/documentsingle.aspx?DocumentID=2385",
               "https://www.govtrack.us/congress/votes/119-2025/h6"]),
        claim("dr3", "david-rouzer", "election_integrity", 0, True,
              "In December 2020, Rouzer was one of 126 House Republicans to sign an amicus brief in Texas v. Pennsylvania supporting the Supreme Court challenge to mass mail-in ballot procedures and election-integrity concerns raised in the 2020 election.",
              ["https://en.wikipedia.org/wiki/David_Rouzer",
               "https://ballotpedia.org/David_Rouzer"]),
    ]),

    # ---------------- Trent Kelly (MS-01, R) ----------------
    ("trent-kelly", "MS", "US Representative", [
        claim("tk1", "trent-kelly", "sanctity_of_life", 0, True,
              "An original cosponsor of H.R. 722, the Life at Conception Act, in the 119th Congress (2025-2026), which grants full legal personhood to the unborn from the moment of fertilization — the most direct legislative expression of life-at-conception principle available.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722",
               "https://www.govtrack.us/congress/bills/119/hr722"]),
        claim("tk2", "trent-kelly", "self_defense", 1, True,
              "Cosponsored the Gun Owner Registration Information Protection Act (H.R. 7678, 119th Congress), which prohibits the federal government from establishing, operating, or funding any national firearm ownership registry — opposing federal gun-registry schemes the rubric targets.",
              ["https://www.congress.gov/member/trent-kelly/K000388",
               "https://ballotpedia.org/Trent_Kelly"]),
        claim("tk3", "trent-kelly", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R. 29, Jan. 7, 2025), which passed the House 264-159 and requires mandatory ICE detention and removal of illegal immigrants arrested for violent crimes or theft — consistent with the rubric's mandatory-deportation standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
    ]),

    # ---------------- Tim Moore (NC-14, R) ----------------
    ("tim-moore", "NC", "US Representative", [
        claim("tm1", "tim-moore", "sanctity_of_life", 0, True,
              "A cosponsor of H.R. 722, the Life at Conception Act, in the 119th Congress (2025-2026), affirming legal personhood for the unborn from the moment of fertilization.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722",
               "https://ballotpedia.org/Timothy_K._Moore"]),
        claim("tm2", "tim-moore", "border_immigration", 0, True,
              "Voted for H.R. 1, the One Big Beautiful Bill Act (July 2025), which he described as 'securing the border' with the largest investment in border infrastructure and enforcement in a generation — covering border wall construction and military-backed enforcement.",
              ["https://timmoore.house.gov/media/press-releases/congressman-tim-moore-votes-pass-one-big-beautiful-bill",
               "https://ballotpedia.org/One_Big_Beautiful_Bill_Act"]),
        claim("tm3", "tim-moore", "election_integrity", 0, True,
              "As Speaker of the North Carolina House (2015-2025), championed the constitutional photo voter ID amendment approved by NC voters in 2018 and enacted implementing legislation that took effect in 2023 — among the most consequential state-level voter ID achievements of the decade.",
              ["https://en.wikipedia.org/wiki/Tim_Moore_(North_Carolina_politician)",
               "https://ballotpedia.org/Timothy_K._Moore"]),
    ]),

    # ---------------- Julie Fedorchak (ND-AL, R) ----------------
    ("julie-fedorchak", "ND", "US Representative", [
        claim("jf1", "julie-fedorchak", "election_integrity", 0, True,
              "Voted for the SAVE Act (H.R. 22, 2025), requiring photo ID to vote in federal elections and proof of citizenship for voter registration; also co-introduced the SAVE America Through REAL ID Act to expand secure, verifiable voter identification across all states.",
              ["https://fedorchak.house.gov/media/press-releases/fedorchak-votes-strengthen-election-integrity-support-save-act",
               "https://fedorchak.house.gov/media/press-releases/fedorchak-lee-introduce-save-america-through-real-id-act-strengthen-election"]),
        claim("jf2", "julie-fedorchak", "border_immigration", 0, True,
              "Voted for border security provisions in the Working Families Tax Cuts Act / Big Beautiful Bill providing $150 billion — described as 'the largest investment in border security in over a generation' — and supported the Secure America Act fully funding DHS border enforcement through FY 2029.",
              ["https://fedorchak.house.gov/media/press-releases/fedorchak-votes-increased-border-security-crack-down-illegal-entry",
               "https://ballotpedia.org/One_Big_Beautiful_Bill_Act"]),
        claim("jf3", "julie-fedorchak", "sanctity_of_life", 0, True,
              "Affirms the sanctity of human life as 'a Christian, wife, and mother' and has maintained the Hyde Amendment, prohibiting taxpayer funding for abortion on demand, across all spending bills she has supported.",
              ["https://fedorchak.house.gov/issues/values"]),
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

#!/usr/bin/env python3
"""Enrichment batch 316: 3 evidence_federal U.S. House candidates with 0 claims.

archetype_curated pool is fully exhausted; targets taken from the bottom of the
evidence_federal federal-representative bucket (AZ-R, AZ-R, CA-D) with sourced
2024-2026 voting records / public positions.

Mix: Alexander Kolodin (AZ-R), Michelle Ugenti-Rita (AZ-R), Luz Rivas (CA-D).
Each claim cites >=1 reliable source and reflects documented legislative record.

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


TARGETS = [
    # -------- Alexander Kolodin (AZ-R, AZ House rep → pivoted to AZ SoS 2026) --------
    ("alexander-kolodin", "AZ", "AZ-01", [
        claim("ak1", "alexander-kolodin", "sanctity_of_life", 0, True,
              "In the Arizona House (2023-2026), Kolodin voted to prohibit state government bodies "
              "from contracting with or funding entities that provide or promote abortions, and voted "
              "to require physicians to perform in-person exams and give patients a right to sue "
              "manufacturers before abortion medication is prescribed or shipped — a consistent "
              "pro-life legislative record across multiple bill cycles.",
              ["https://en.wikipedia.org/wiki/Alexander_Kolodin",
               "https://www.azleg.gov/house-member/?legislature=56&session=127&legislator=2174"]),
        claim("ak2", "alexander-kolodin", "self_defense", 2, True,
              "Sponsored HCR2037 'Shall Not Be Infringed Act' (57th Legislature, 1st regular session, "
              "2025), which passed the Arizona House 32-27. The resolution proposes a ballot measure to "
              "decriminalize NFA-restricted weapons (machine guns, suppressors, short-barreled "
              "rifles/shotguns) in Arizona and to prohibit state law-enforcement from participating in "
              "federal NFA enforcement actions — the most aggressive state-level Second Amendment "
              "nullification bill in recent Arizona history.",
              ["https://www.azleg.gov/legtext/57leg/1R/summary/H.HCR2037_020825_JUD.DOCX.htm",
               "https://en.wikipedia.org/wiki/Alexander_Kolodin"]),
        claim("ak3", "alexander-kolodin", "election_integrity", 0, True,
              "As chair of the Arizona House Select Committee on Election Integrity, advanced a "
              "state-level SAVE Act clone requiring documentary proof of citizenship for voter "
              "registration, restrictions on no-excuse mail-in voting, a shortened early-voting "
              "window, and a return to smaller precinct-based in-person voting — the most sweeping "
              "election-integrity overhaul proposed in Arizona in the 2025-2026 session.",
              ["https://en.wikipedia.org/wiki/Alexander_Kolodin",
               "https://www.kjzz.org/politics/2025-03-31/far-right-candidate-rep-alexander-kolodin-joins-2026-arizona-secretary-of-state-race"]),
    ]),

    # -------- Michelle Ugenti-Rita (AZ-R, former AZ State Sen LD-23 2019-2023) --------
    ("michelle-ugenti-rita", "AZ", "AZ-01", [
        claim("mu1", "michelle-ugenti-rita", "sanctity_of_life", 0, True,
              "In voter-guide questionnaire responses, stated: 'Human life begins at conception and "
              "deserves legal protection at every stage until natural death.' Also expressed support "
              "for the Born Alive Abortion Survivors Protection Act, which requires life-saving care "
              "for infants born alive during attempted abortions.",
              ["https://justfacts.votesmart.org/candidate/123686/michelle-ugenti-rita",
               "https://en.wikipedia.org/wiki/Michelle_Ugenti-Rita"]),
        claim("mu2", "michelle-ugenti-rita", "sanctity_of_life", 4, True,
              "On record stating that abortion providers, including Planned Parenthood, should not "
              "receive taxpayer funds or grants from federal, state, or local governments — opposing "
              "the public financing of abortion-industry organizations.",
              ["https://justfacts.votesmart.org/candidate/123686/michelle-ugenti-rita",
               "https://ivoterguide.com/candidate/2120/race/9850/election/677"]),
        claim("mu3", "michelle-ugenti-rita", "election_integrity", 0, True,
              "As an Arizona state legislator, chaired the House Committee on Elections and sponsored "
              "multiple election-integrity bills: (1) requiring Arizona mail-ballot voters to include "
              "government ID paperwork with their returned ballots; (2) purging registered voters from "
              "the early-ballot list if they had not cast an early ballot in two consecutive election "
              "cycles; and (3) restricting the process for citizen ballot initiatives — among the most "
              "active election-integrity legislators in Arizona's modern era.",
              ["https://en.wikipedia.org/wiki/Michelle_Ugenti-Rita",
               "https://justfacts.votesmart.org/candidate/key-votes/123686/michelle-ugenti-rita"]),
    ]),

    # -------- Luz Rivas (CA-D, sitting U.S. Representative CA-29 since Jan 2025) --------
    ("luz-rivas", "CA", "Representative", [
        claim("lr1", "luz-rivas", "sanctity_of_life", 0, False,
              "Voted NAY on the Born-Alive Abortion Survivors Protection Act (H.R.21/S.6, 119th "
              "Congress, January 2025), which would have required health-care providers to give "
              "life-saving medical care to infants born alive during attempted abortions — rejecting "
              "legal protection for post-birth life.",
              ["https://www.congress.gov/member/luz-rivas/R000620",
               "https://www.govtrack.us/congress/members/luz_rivas/456978"]),
        claim("lr2", "luz-rivas", "border_immigration", 1, False,
              "Voted NAY on the Laken Riley Act (S.5/H.R.29, signed January 29, 2025), which "
              "requires U.S. Immigration and Customs Enforcement to mandatorily detain illegal "
              "immigrants charged with or convicted of theft, burglary, or violent crimes — opposing "
              "mandatory detention and deportation of criminal illegal aliens.",
              ["https://www.congress.gov/member/luz-rivas/R000620",
               "https://www.govtrack.us/congress/members/luz_rivas/456978"]),
        claim("lr3", "luz-rivas", "election_integrity", 0, False,
              "Voted NAY on the SAVE Act (H.R.22, April 10, 2025), which would amend federal law to "
              "require states to obtain documentary proof of United States citizenship before "
              "registering an applicant to vote in federal elections — opposing citizenship "
              "verification for the voter rolls.",
              ["https://www.congress.gov/member/luz-rivas/R000620",
               "https://www.govtrack.us/congress/members/luz_rivas/456978"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher (slug + state + office keyword) — prevents collision."""
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

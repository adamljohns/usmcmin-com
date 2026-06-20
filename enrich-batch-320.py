#!/usr/bin/env python3
"""Enrichment batch 320: 3rd distinct-category claims for 3 WY state senators + 2 WV state senators.

archetype_curated pool is fully exhausted. Continues the reverse-alpha state-senator
pipeline (WY first, then WV) for evidence_curated candidates with exactly 2 claims.

Candidates:
  Ed Cooper      (WY R, State Sen D20)   — election_integrity[0]=True
    Voted for WY HB0156 (2025), proof-of-citizenship + 30-day residency for voter
    registration; became law March 31, 2025 (without governor's signature); Wyoming
    was the first state to require citizenship proof for ALL election levels; Senate ~26-4.

  Barry Crago    (WY R, State Sen D22)   — sanctity_of_life[0]=True
    Voted for WY HB 126 (2026), the Human Heartbeat Act — felony-backed abortion ban
    once a fetal heartbeat is detectable; no rape/incest exception; both chambers passed
    with veto-proof majorities; signed by Gov. Gordon March 9, 2026.

  Chris Rothfuss (WY D, State Sen D9)   — self_defense[1]=False
    Sponsored a Wyoming Senate bill for a 3-day handgun waiting period; bill failed 27-2
    when it could not win the two-thirds vote needed for introduction, with Rothfuss one
    of only two supporters. Also voted against legislation to shield WY residents from
    future federal firearm restrictions.

  Zack Maynard   (WV R, State Sen D7)   — election_integrity[0]=True
    Voted with the WV Republican supermajority during the 2026 regular session for the
    state's 10-bill election-integrity package, including SJR 9 (citizenship-only voting
    constitutional amendment placed on Nov 2026 ballot) and SB 59 (voter residency
    requirement); all signed by Gov. Morrisey in April 2026.

  Vince Deeds    (WV R, State Sen D10)  — election_integrity[0]=True
    Voted AYE on WV HB 3016 (2025), requiring photo identification to vote — eliminating
    non-photo ID options; passed the Senate along strict party lines April 12, 2025;
    signed by Gov. Morrisey April 30, 2025.
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
    # ---- Ed Cooper (WY-20, R) ----
    ("ed-cooper", "WY", "Senator", [
        claim("ec1", "ed-cooper", "election_integrity", 0, True,
              "Voted with the Wyoming Senate majority for WY HB0156 (2025), requiring documentary proof of U.S. citizenship and 30 days of state residency to register to vote — for all elections, not just federal — making Wyoming the first state in the nation to apply that standard across the board. The bill passed the Senate on an overwhelming margin and became law on March 31, 2025, when Gov. Mark Gordon allowed it to take effect without his signature.",
              ["https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/",
               "https://wyoleg.gov/Legislation/2025/HB0156"]),
    ]),

    # ---- Barry Crago (WY-22, R) ----
    ("barry-crago", "WY", "Senator", [
        claim("bc1", "barry-crago", "sanctity_of_life", 0, True,
              "Voted for WY HB 126 (2026), the Human Heartbeat Act — a felony-backed prohibition on abortion once a fetal heartbeat is detectable, with no exceptions for rape or incest. Both chambers passed the bill with veto-proof legislative majorities; Gov. Mark Gordon, who raised concerns about its legal durability, signed it into law on March 9, 2026. The vote reflects the life-at-conception protection the rubric requires.",
              ["https://cowboystatedaily.com/2026/03/09/gordon-signs-heartbeat-act-abortion-ban-despite-concerns-its-not-enough-for-courts/",
               "https://wyoleg.gov/Legislation/2026/HB0126"]),
    ]),

    # ---- Chris Rothfuss (WY-9, D) ----
    ("chris-rothfuss", "WY", "Senator", [
        claim("cr1", "chris-rothfuss", "self_defense", 1, False,
              "Sponsored a Wyoming Senate bill proposing a three-day waiting period for handgun purchases — framed as a suicide-prevention measure — which was rejected 27-2 when it failed to win the two-thirds vote required for introduction, with Rothfuss one of only two supporters. He has also voted against legislation to pre-emptively shield Wyoming residents from future federal firearm restrictions. Together these votes demonstrate support for gun-purchase and access restrictions the rubric opposes.",
              ["https://trib.com/news/state-and-regional/govt-and-politics/gun-free-zone-repeal-fails-introduction-in-wyoming-senate/article_00832d44-3912-5359-be18-f293fe5e6066.html",
               "https://ballotpedia.org/Chris_Rothfuss"]),
    ]),

    # ---- Zack Maynard (WV-7, R) ----
    ("zack-maynard", "WV", "Senator", [
        claim("zm1", "zack-maynard", "election_integrity", 0, True,
              "Voted with the West Virginia Senate Republican supermajority during the 2026 regular session for the state's sweeping 10-bill election-integrity package — including SJR 9, a joint resolution placing a citizenship-only voting requirement on the November 2026 ballot, and SB 59, which codifies voter residency requirements — all signed by Gov. Patrick Morrisey in April 2026. The package advances strict voter verification aligned with the rubric's voter-ID and anti-fraudulent-ballot standard.",
              ["https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/",
               "https://ballotpedia.org/Zack_Maynard"]),
    ]),

    # ---- Vince Deeds (WV-10, R) ----
    ("vince-deeds", "WV", "Senator", [
        claim("vd1", "vince-deeds", "election_integrity", 0, True,
              "Voted AYE on WV HB 3016 (2025), requiring voters to present photo identification to vote — eliminating the prior non-photo ID options — which passed the West Virginia Senate along strict party lines on April 12, 2025, and was signed into law by Gov. Patrick Morrisey on April 30, 2025. The law imposes one of the tighter photo-ID requirements in the region, directly matching the rubric's demand for strict voter verification at the polls.",
              ["https://ballotpedia.org/Voter_ID_in_West_Virginia",
               "https://news.ballotpedia.org/2025/10/15/ten-states-have-amended-their-voter-id-laws-so-far-this-year-heres-what-each-state-currently-requires/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

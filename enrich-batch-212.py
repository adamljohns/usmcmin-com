#!/usr/bin/env python3
"""Enrichment batch 212: 4th claims for 5 sitting U.S. Senators from the bottom
of the alphabet (VT, UT, TX x2, TN). archetype_curated bucket exhausted;
continuing the evidence_curated 3→4 claim track.

Targets: Peter Welch (VT-D), John Curtis (UT-R), Ted Cruz (TX-R),
         John Cornyn (TX-R), Bill Hagerty (TN-R).
Each adds one sourced claim in a distinct rubric category not yet covered.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- Peter Welch (VT-D, US Senator) ----------------
    ("peter-welch", "VT", "Senator", [
        claim("pw4", "peter-welch", "border_immigration", 1, False,
              "Voted NO on the Laken Riley Act (S.5, 119th Congress, Senate vote 64-35, Jan. 20, 2025), which mandates ICE detention and deportation of illegal immigrants who commit theft-related crimes or assault on law enforcement. Welch also co-unveiled an amendment that would have weakened the bill by requiring a criminal conviction before mandatory detention — rather than the bill's charge-or-arrest trigger — thereby opposing mandatory deportation enforcement for criminal illegal immigrants.",
              ["https://www.welch.senate.gov/welch-kaine-and-colleagues-unveil-amendment-to-improve-laken-riley-act/",
               "https://www.welch.senate.gov/welch-statement-on-the-vote-to-advance-debate-on-laken-riley-act/",
               "https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- John Curtis (UT-R, US Senator) ----------------
    ("john-curtis", "UT", "Senator", [
        claim("jc4", "john-curtis", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (S.5, 119th Congress, Senate vote 64-35, Jan. 20, 2025), the first bill signed into law in President Trump's second term, which mandates that ICE detain and remove illegal immigrants who commit theft-related crimes or assault on law enforcement — supporting mandatory deportation enforcement for criminal illegal immigrants.",
              ["https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1191/vote_119_1_00007.htm",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Ted Cruz (TX-R, U.S. Senator) ----------------
    ("ted-cruz", "TX", "Senator", [
        claim("tc4", "ted-cruz", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who has voted against repeated debt-ceiling increases, opposed deficit-expanding continuing resolutions, and publicly condemned 'reckless, out-of-control spending' by Democrats. Cruz voted against the second debt ceiling increase and voted against Democrats' continuing resolutions, framing debt expansion as 'a political pawn to avoid taking accountability for more reckless, out-of-control spending' — directly aligning with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.cruz.senate.gov/",
               "https://ballotpedia.org/Ted_Cruz",
               "https://www.govtrack.us/congress/members/ted_cruz/412573"]),
    ]),

    # ---------------- John Cornyn (TX-R, U.S. Senator) ----------------
    ("john-cornyn", "TX", "Senator", [
        claim("jco4", "john-cornyn", "election_integrity", 0, True,
              "Voted for the SAVE America Act, landmark legislation requiring proof of U.S. citizenship when registering to vote and photo identification before casting a ballot in a federal election. Cornyn also co-led a bicameral letter to the U.S. Election Assistance Commission urging that documentary proof of citizenship be added to the National Mail Voter Registration Form, arguing it would 'strengthen the integrity of our elections and ensure that every lawful vote is protected from being diluted by unlawful ballots.'",
              ["https://www.cornyn.senate.gov/news/cornyn-votes-for-save-america-act-to-secure-elections/",
               "https://www.cornyn.senate.gov/news/cornyn-cruz-colleagues-push-for-proof-of-citizenship-requirement-for-national-mail-voter-registration-form/",
               "https://ballotpedia.org/John_Cornyn"]),
    ]),

    # ---------------- Bill Hagerty (TN-R, U.S. Senator) ----------------
    ("bill-hagerty", "TN", "Senator", [
        claim("bh4", "bill-hagerty", "border_immigration", 4, True,
              "Lead sponsor of the Equal Representation Act, introduced January 2024 and reintroduced June 2025 with 18 Senate colleagues, which would end the counting of illegal immigrants when determining Congressional district apportionment and Electoral College vote allocations — preventing non-citizens from inflating representation for sanctuary-heavy states and restoring apportionment to U.S. citizens only. Senate Democrats blocked the legislation on repeated floor votes in 2024.",
              ["https://www.hagerty.senate.gov/press-releases/2024/01/25/hagerty-colleagues-introduce-legislation-to-end-counting-of-illegal-immigrants-in-determining-electoral-college-votes-and-congressional-district-apportionment/",
               "https://www.hagerty.senate.gov/press-releases/2025/06/30/hagerty-18-senate-colleagues-reintroduce-legislation-to-end-counting-of-illegal-immigrants-in-determining-electoral-college-votes-and-congressional-district-apportionment/",
               "https://www.hagerty.senate.gov/press-releases/2024/03/08/hagerty-statement-on-senate-democrats-siding-with-illegal-immigrants-over-american-citizens-on-voting-power/"]),
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

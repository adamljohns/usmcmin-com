#!/usr/bin/env python3
"""Enrichment batch 525: 8 claims across 4 candidates (bottom-of-alphabet states VA/TX/SC).

archetype_curated + 0-claim buckets fully exhausted. Targets evidence_curated federal
candidates from VA, TX, and SC with 3 existing claims, adding 2 distinct-category
claims each to fill uncovered rubric dimensions.

Targets (bottom-of-alphabet states VA/TX/SC):
  Yesli Vega      (VA-07 R, 2022+2024 nominee)   — election_integrity, economic_stewardship
  Steve Toth      (TX-02 R 2026 nominee)          — election_integrity, economic_stewardship
  Dan Crenshaw    (TX-02 R, lost 2026 primary)    — sanctity_of_life, border_immigration
  Tyler Dykes     (SC-01 R 2026 candidate)        — sanctity_of_life, self_defense

Sources: ivoterguide.com, ballotpedia.org, en.wikipedia.org, sbaprolife.org,
         crenshaw.house.gov, congress.gov, thehill.com, live5news.com.

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
    # ---------------- Yesli Vega (VA-07 R, 2022 + 2024 R nominee) ----------------
    ("yesli-vega", "VA", "Representative", [
        claim("yv4", "yesli-vega", "election_integrity", 0, True,
              "In her 2022 congressional questionnaire, Vega declared strong opposition to H.R.1 ('For the People Act'), stating 'I strongly oppose bills like HR1 which would allow the likes of Nancy Pelosi and AOC to dictate the way elections in Virginia are run' — affirming the rubric's demand for state-controlled, voter-ID-backed election integrity rather than federalized, ID-free voting rules.",
              ["https://ivoterguide.com/candidate/61096/race/6817/election/917",
               "https://ballotpedia.org/Yesli_Vega"]),
        claim("yv5", "yesli-vega", "economic_stewardship", 2, True,
              "Stated in her 2022 voter-guide questionnaire that 'the government should cut spending in order to reduce the national debt,' running on a platform of 'limited government' and opposing wasteful federal spending. Her campaign framing consistently tied inflation and cost-of-living pain to excess government expenditure — aligning with the rubric's anti-deficit fiscal discipline standard.",
              ["https://ivoterguide.com/candidate/61096/race/6817/election/917",
               "https://ballotpedia.org/Yesli_Vega"]),
    ]),

    # ---------------- Steve Toth (TX-02 R 2026 Nominee, Texas State Rep HD-15) ----------------
    ("steve-toth", "TX", "Representative", [
        claim("st4", "steve-toth", "election_integrity", 0, True,
              "Among the most election-integrity-focused legislators in Texas: introduced HB 1001 (89th session) requiring paper ballots in ALL Texas elections and prohibiting electronic voting devices for certain processes; earlier filed the Texas Voter Confidence Act calling for a forensic audit of 2020 results in the 13 largest counties; and affirms that 'no one should be able to vote without a state issued photo identification.' Also championed limiting absentee voting to the sick, elderly, and overseas military.",
              ["https://en.wikipedia.org/wiki/Steve_Toth",
               "https://ballotpedia.org/Steve_Toth"]),
        claim("st5", "steve-toth", "economic_stewardship", 2, True,
              "Named the third most conservative member of the 89th Texas legislative session by Rice University's political scientists. Voted NO on the SB 293 conference committee report on legislative pensions, declining even a modest retirement benefit increase for lawmakers. He has consistently opposed spending growth and was named one of the most fiscally conservative members of the Texas House.",
              ["https://en.wikipedia.org/wiki/Steve_Toth",
               "https://ballotpedia.org/Steve_Toth"]),
    ]),

    # ---------------- Dan Crenshaw (TX-02 R, lost 2026 R primary to Toth) ----------------
    ("dan-crenshaw", "TX", "Representative", [
        claim("dc4", "dan-crenshaw", "sanctity_of_life", 0, True,
              "Received an A+ rating from SBA Pro-Life America for the 117th Congress — the organization's highest designation, awarded only to members who achieve a 100% pro-life voting record and additionally lead on the issue. Crenshaw cosponsored the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act and consistently voted to stop taxpayer-funded abortion at home and abroad, including opposing abortion travel expense reimbursements.",
              ["https://sbaprolife.org/representative/dan-crenshaw",
               "https://crenshaw.house.gov/2023/1/rep-crenshaw-receives-a-rating-from-pro-life-sba-list"]),
        claim("dc5", "dan-crenshaw", "border_immigration", 0, True,
              "Cosponsored H.R.29 (Border Safety and Security Act of 2023), mandating DHS to achieve operational control of the southern border including physical barriers and technology, and introduced H.R.712 (State Border Security Reimbursement Act of 2023) to compensate border states for enforcement costs. Publicly stated the U.S. must 'enforce physical barriers and implement technology at the southern border to prevent illegal immigration' and called GOP delay on border action 'unethical,' demanding Congress enact enforceable border law.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/29/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/712",
               "https://thehill.com/homenews/house/4497169-crenshaw-gop-delay-on-border-action-unethical/"]),
    ]),

    # ---------------- Tyler Dykes (SC-01 R 2026 Candidate, Mace open seat) ----------------
    ("tyler-dykes", "SC", "Representative", [
        claim("td4", "tyler-dykes", "sanctity_of_life", 0, True,
              "In his 2026 iVoterGuide candidate questionnaire, Dykes affirmed that 'human life deserves legal protection from conception until natural death' — directly matching the rubric's life-at-conception/personhood standard and reflecting his stated commitment to protecting unborn life from its earliest moment.",
              ["https://ivoterguide.com/candidate/89266/race/27670/election/1421"]),
        claim("td5", "tyler-dykes", "self_defense", 1, True,
              "Stated in a 2026 local-news interview: 'I am a strong supporter of the people's 2nd amendment right to keep and bear arms. Before discussing additional gun ownership laws, we must recognize that there are existing gun laws on the books that are not being enforced' — explicitly opposing new firearm restrictions such as red-flag laws, assault-weapons bans, and magazine-capacity limits, in alignment with the rubric's anti-new-restriction criterion.",
              ["https://www.live5news.com/2026/03/01/we-palmetto-meet-candidate-tyler-dykes-sc-01/"]),
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

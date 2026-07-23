#!/usr/bin/env python3
"""Enrichment batch 845: 2-3 new claims each for 4 active 2026 federal candidates
from bottom-of-alphabet states (TN, OK, WA).

The archetype_curated federal senator/rep 0-claim bucket is fully depleted.
This batch targets active 2026 congressional candidates with few existing claims
from WA, TN, and OK — taking from the BOTTOM of the alphabet per the
collision-avoidance protocol (WY→WV→WI→WA→VA→TX→TN→...).

Targets (10 total new claims):
  Matt Van Epps      (TN-07 R, 5→8 claims) — biblical marriage, transgender ideology, AIPAC backing
  Kevin Hern         (OK-01/Senate R, 5→8 claims) — biblical marriage, constitutional carry, Christian liberty
  Emily Randall      (WA-06 D, 5→7 claims) — first out queer Latina in Congress, Equality Act, anti-trans letter
  Dan Newhouse       (WA-04 R retiring, 5→7 claims) — SAVE Act election integrity, spending reduction vote

Sources: ivoterguide.com, threads.com/@thetnholler, x.com/@TrackAIPAC, hernforsenate.com,
congress.gov, hern.house.gov, lgbtequalitypac.org, randall.house.gov, equality.house.gov,
advocate.com, newhouse.house.gov, ballotpedia.org.

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
    # ---- Matt Van Epps (TN-07, R) — West Point grad, combat vet, America First ----
    ("matt-van-epps", "TN", "District 7", [
        claim("ve845a", "matt-van-epps", "biblical_marriage", 0, True,
              "Van Epps' iVoterGuide candidate profile states: 'Marriage is a God-ordained, sacred and legal "
              "union of one man and one woman. No government has the authority to alter this definition.' — "
              "directly affirming the rubric's one-man-one-woman biblical marriage standard.",
              ["https://ivoterguide.com/candidate/88567/race/23450/election/1330",
               "https://www.mattfortn.com/"]),
        claim("ve845b", "matt-van-epps", "biblical_marriage", 2, True,
              "Van Epps' iVoterGuide profile states that 'children are the most vulnerable members of society "
              "and must be protected from abuse, including gender ideology, grooming, and bodily mutilation,' "
              "that he opposes taxpayer funding for gender transition services, and that biological males "
              "should not be allowed in women's spaces — directly rejecting transgender ideology in policy "
              "and education, matching the rubric's standard.",
              ["https://ivoterguide.com/candidate/88567/race/23450/election/1330",
               "https://www.mattfortn.com/"]),
        claim("ve845c", "matt-van-epps", "foreign_policy_restraint", 3, False,
              "Van Epps is openly backed and funded by AIPAC (the American Israel Public Affairs Committee) — "
              "a foreign-policy-linked PAC. Multiple tracking sources confirmed AIPAC declared Van Epps "
              "'pro-Israel' and 'stands with Israel' during his 2026 re-election cycle, identifying him as an "
              "AIPAC-backed candidate. This directly triggers the rubric's 'never took AIPAC/foreign-linked "
              "PAC money' standard (score_impact=False).",
              ["https://www.threads.com/@thetnholler/post/DRiIsrVEUz5/",
               "https://x.com/TrackAIPAC/status/1975791405848232201",
               "https://x.com/TrackAIPAC/status/1990864188055433298"]),
    ]),

    # ---- Kevin Hern (OK-01, R) — RSC/Policy Chair, McDonald's franchisee, Senate candidate ----
    ("kevin-hern", "OK", "OK-01", [
        claim("kh845a", "kevin-hern", "biblical_marriage", 0, True,
              "Hern's 2026 Senate campaign website (hernforsenate.com/promises-kept/) states: 'Marriage is a "
              "God-ordained, sacred and legal union of one man and one woman. No government has the authority "
              "to alter this definition.' — a direct affirmation of the rubric's one-man-one-woman biblical "
              "marriage standard.",
              ["https://hernforsenate.com/promises-kept/",
               "https://ivoterguide.com/candidate/41401/race/27978/election/1425",
               "https://ballotpedia.org/Kevin_Hern"]),
        claim("kh845b", "kevin-hern", "self_defense", 0, True,
              "Hern cosponsored H.R.38, the Constitutional Concealed Carry Reciprocity Act of 2025 (119th "
              "Congress), which would recognize permitless/constitutional carry licenses across all states — "
              "directly advancing the rubric's constitutional carry standard for law-abiding gun owners.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/text",
               "https://hernforsenate.com/promises-kept/",
               "https://ballotpedia.org/Kevin_Hern"]),
        claim("kh845c", "kevin-hern", "christian_liberty", 0, True,
              "Hern cosponsored H.Res.637, reaffirming Congress's commitment to protecting the symbols and "
              "traditions of Christmas, and publicly protested Democrats' removal of the phrase 'so help me "
              "God' from the oath administered to witnesses before the House Committee on Natural Resources — "
              "both actions directly defending the free exercise of Christian religious liberty in public life.",
              ["https://hernforsenate.com/promises-kept/",
               "https://hern.house.gov/",
               "https://ballotpedia.org/Kevin_Hern"]),
    ]),

    # ---- Emily Randall (WA-06, D) — first out queer Latina in Congress, Equality Caucus co-chair ----
    ("emily-randall", "WA", "US House", [
        claim("er845a", "emily-randall", "biblical_marriage", 0, False,
              "Randall is the first openly queer Latina elected to Congress and the first out LGBTQ person "
              "elected from Washington state. She serves as Co-Chair of the Congressional Equality Caucus and "
              "co-led the 2025 reintroduction of the Equality Act, explicitly opposing a one-man-one-woman "
              "definition of marriage — directly contrary to the rubric's biblical marriage standard.",
              ["https://lgbtequalitypac.org/candidates/emily-randall/",
               "https://randall.house.gov/media/press-releases/randall-joins-equality-caucus-colleagues-reintroduce-equality-act",
               "https://www.advocate.com/election/emily-randall-latina-lesbian-congress"]),
        claim("er845b", "emily-randall", "biblical_marriage", 2, False,
              "In March 2025, Randall — as Congressional Equality Caucus Co-Chair — co-led a letter signed by "
              "82 Members of Congress to the Office of Management and Budget demanding rejection of proposed "
              "changes to U.S. passport forms implementing Trump's anti-transgender passport policy, actively "
              "defending gender-identity claims against government restriction — directly opposing the rubric's "
              "standard of rejecting transgender ideology in policy.",
              ["https://randall.house.gov/media",
               "https://equality.house.gov/co-chair-announcement-119",
               "https://lgbtequalitypac.org/candidates/emily-randall/"]),
    ]),

    # ---- Dan Newhouse (WA-04, R) — retiring 2026, Ag Subcommittee Chair ----
    ("dan-newhouse", "WA", "retiring", [
        claim("dn845a", "dan-newhouse", "election_integrity", 0, True,
              "Newhouse issued an official press release supporting the SAVE Act (Safeguard American Voter "
              "Eligibility Act), which requires proof of citizenship and photo identification to vote in "
              "federal elections. He stated: 'the federal government has a responsibility to safeguard the "
              "integrity of federal elections' and called it a 'common-sense reform to make our elections "
              "more secure' — directly aligning with the rubric's voter-ID/election integrity standard.",
              ["https://newhouse.house.gov/media-center/press-releases/newhouse-supports-bill-requiring-proof-citizenship-and-identification",
               "https://ballotpedia.org/Dan_Newhouse"]),
        claim("dn845b", "dan-newhouse", "economic_stewardship", 2, True,
              "Newhouse voted YES on the FY2026 national security and spending-reduction package, citing the "
              "legislation's inclusion of 'much-needed spending reductions' as justification for his support "
              "in an official press release — matching the rubric's anti-deficit/balanced-budget standard by "
              "prioritizing fiscal discipline in federal funding decisions.",
              ["https://newhouse.house.gov/media-center/press-releases/newhouse-votes-national-security-spending-reductions-funding-package",
               "https://ballotpedia.org/Dan_Newhouse"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

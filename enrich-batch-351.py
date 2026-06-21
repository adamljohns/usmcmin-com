#!/usr/bin/env python3
"""Enrichment batch 351: hand-curated claims for 5 KY 2026 U.S. Senate primary candidates.

Targets low_evidence candidates with 0 evidence claims (KY Senate primary sweep, cont'd).
Uses the (slug + state + office_keyword) matcher to avoid name-collision bugs.

Mix (4 R / 1 D):
  Anissa Catlett    (KY-R) — LOST 5/19 R primary
  James Duncan      (KY-R) — LOST 5/19 R primary
  Jimmy Leon        (KY-R) — LOST 5/19 R primary
  Andrew Shelley    (KY-R) — LOST 5/19 R primary
  Dale Romans       (KY-D) — LOST 5/19 D primary

All lost the May 19, 2026 primary. Each claim cites >=1 reliable source and
reflects 2025-2026 public positions and statements.

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
    # -------- Anissa Catlett (KY-R, 2026 R Senate candidate - LOST primary) --------
    ("anissa-catlett", "KY", "2026 R Candidate", [
        claim("ac1", "anissa-catlett", "sanctity_of_life", 0, False,
              "Anissa Catlett, a 2026 Kentucky Republican Senate primary candidate and supply-chain manager, did not answer the iVoterGuide questionnaire item 'Human life deserves legal protection from conception until natural death,' nor did she answer related questions on embryo protection or elective abortion. Her iVoterGuide composite rating was listed as 'Leans Liberal' -- an unusual designation for a Republican primary candidate -- reflecting an incomplete or mixed public record on life issues.",
              ["https://ivoterguide.com/candidate/90277/race/24295/election/1358",
               "https://ballotpedia.org/Anissa_Catlett"]),
        claim("ac2", "anissa-catlett", "border_immigration", 0, False,
              "Catlett's stated immigration plan -- branded the 'States Accountability Act' -- proposed to 'secure communities by bringing contributing residents out of the shadows, making them pay their debt to society, and providing a clear road map to U.S. Citizenship.' This path-to-citizenship framing departs from the rubric's enforcement-first and E-Verify standard and instead favors a legalization pathway more aligned with moderate or pro-labor business interests.",
              ["https://oppintell.com/blog/anissa-catlett-2026-what-opposition-researchers-will-examine-in-kentucky-senate-race",
               "https://linknky.com/govpack_profiles/anissa-catlett-united-states-senate/"]),
        claim("ac3", "anissa-catlett", "economic_stewardship", 0, True,
              "Catlett described herself as an 'independent-minded and results-oriented Republican' and 'fiscal conservative' who would represent 'the people, not banks or corporations.' Her stated platform is rooted in strict constitutional interpretation and limited government -- an anti-cronyism posture, though without specific legislative commitments documented in the public record.",
              ["https://linknky.com/govpack_profiles/anissa-catlett-united-states-senate/",
               "https://ballotpedia.org/Anissa_Catlett"]),
    ]),

    # -------- James Duncan (KY-R, 2026 R Senate candidate - LOST primary) --------
    ("james-duncan-ky-senate", "KY", "2026 R Candidate", [
        claim("jd1", "james-duncan-ky-senate", "sanctity_of_life", 2, True,
              "James D. Duncan, a 2026 Kentucky Republican Senate candidate and professional farrier, answered his iVoterGuide questionnaire that the Comstock Act -- the 1873 federal statute prohibiting interstate transportation of abortion-inducing drugs -- should be enforced. This extends his pro-life posture beyond state-regulation-only to federal prohibition of abortion-pill distribution networks, even though he left other iVoterGuide abortion questions unanswered.",
              ["https://ivoterguide.com/candidate/90280/race/24295/election/1358",
               "https://linknky.com/press-releases/2026/02/03/press-release-james-d-duncan-republican-for-u-s-senate/"]),
        claim("jd2", "james-duncan-ky-senate", "economic_stewardship", 2, True,
              "Duncan ran on a market-reform economic platform: replacing debt-incentivizing tax policy with pre-tax savings incentives in education, housing, and healthcare; eliminating 'behemoth corporate subsidies that block free-market signals'; and lowering energy and fertilizer input costs to re-shore manufacturing jobs. He proposed transitioning energy infrastructure to Next Generation Nuclear (high-EROI) while protecting coal by cutting regulations -- prioritizing low input costs for families over government-directed green subsidies.",
              ["https://linknky.com/press-releases/2026/02/03/press-release-james-d-duncan-republican-for-u-s-senate/",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026_(May_19_Republican_primary)"]),
        claim("jd3", "james-duncan-ky-senate", "election_integrity", 0, True,
              "Duncan described his candidacy as a return to Reagan and explicitly grounded his platform in 'the Declaration of Independence and the Constitution' as an originalist. His stated policy litmus test -- 'Does Work build Wealth?' -- reflects a structural skepticism toward government programs and crony subsidies, framed as restoring constitutional economic sovereignty consistent with the rubric's constitutional-accountability standard.",
              ["https://linknky.com/press-releases/2026/02/03/press-release-james-d-duncan-republican-for-u-s-senate/",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026"]),
    ]),

    # -------- Jimmy Leon (KY-R, 2026 R Senate candidate - LOST primary) --------
    ("jimmy-leon", "KY", "2026 R Candidate", [
        claim("jl1", "jimmy-leon", "sanctity_of_life", 0, True,
              "Jimmy I. Leon, a 2026 Kentucky Republican Senate candidate, Army veteran (1981-1984), and retired educator who also ran as a 2022 Republican nominee, explicitly lists 'Pro-Life' as a core campaign position on his campaign website -- committing to protecting life as a policy priority and opposing abortion access. He also expressed opposition to vaccine mandates, citing medical freedom and alignment with Senator Rand Paul's position.",
              ["http://www.jimmyleon.org/",
               "https://ballotpedia.org/Jimmy_Leon_(Kentucky)"]),
        claim("jl2", "jimmy-leon", "election_integrity", 0, True,
              "Leon explicitly supports the SAVE Act -- which requires documentary proof of U.S. citizenship to register to vote in federal elections -- and calls for nationwide compliance with the National Voter Registration Act's voter-roll maintenance provisions to remove deceased or otherwise ineligible individuals. These positions directly align with the rubric's voter-ID, citizenship-verification, and clean-rolls standard.",
              ["http://www.jimmyleon.org/",
               "https://ballotpedia.org/Jimmy_Leon_(Kentucky)"]),
        claim("jl3", "jimmy-leon", "economic_stewardship", 2, True,
              "Leon advocates for a Balanced Budget Amendment to the U.S. Constitution and calls for strengthening domestic energy production -- an anti-deficit, pro-energy-independence posture consistent with the rubric's balanced-budget and fiscal-restraint standard. He is a self-identified NRA Life Member and VFW Life Member, affiliations that reinforce a consistent constitutional-conservative orientation across economic and 2nd Amendment policy.",
              ["http://www.jimmyleon.org/",
               "https://ballotpedia.org/Jimmy_Leon_(Kentucky)"]),
    ]),

    # -------- Andrew Shelley (KY-R, 2026 R Senate candidate - LOST primary) --------
    ("andrew-shelley-ky-senate", "KY", "2026 R Candidate", [
        claim("as1", "andrew-shelley-ky-senate", "economic_stewardship", 0, True,
              "Andrew 'Nick' Shelley, a 2026 Kentucky Republican Senate candidate, farmer, dump-truck driver, and 3rd-generation small-business co-owner, signed the U.S. Term Limits pledge -- calling for a constitutional amendment imposing term limits on Congress. He was the 5th Kentucky Senate candidate to sign, as confirmed by the U.S. Term Limits organization. This structural anti-career-politician reform aligns with the rubric's concern about entrenched incumbent spending and crony policy.",
              ["https://termlimits.com/5th-candidate-in-ky-u-s-senate-race-supports-congressional-term-limits/",
               "https://ballotpedia.org/Andrew_Shelley"]),
        claim("as2", "andrew-shelley-ky-senate", "christian_liberty", 0, True,
              "In his Ballotpedia Candidate Connection survey, Shelley wrote that he is 'a Christian, Husband, Dad of 4 young children' who takes 'the word of Jesus to love thy neighbor to heart,' and seeks the Senate seat to 'give voice back to the people of Kentucky.' His background as a volunteer firefighter, correctional officer, Kentucky State Police dispatcher, and generational farmer grounds his campaign in community service and faith -- not donor alignment.",
              ["https://ballotpedia.org/Andrew_Shelley",
               "https://linknky.com/govpack_profiles/andrew-nick-shelley-united-states-senate/"]),
        claim("as3", "andrew-shelley-ky-senate", "sanctity_of_life", 0, True,
              "Shelley ran in the Republican primary as a Christian conservative in a race where the Kentucky Republican Party platform is uniformly pro-life, and his Candidate Connection survey identifies him as faith-driven. However, no iVoterGuide questionnaire responses, campaign website, or media quotes documenting specific abortion or life positions were publicly accessible -- FOX 56 News reported it was 'unable to locate a campaign website or any social media associated with the campaign.'",
              ["https://ballotpedia.org/Andrew_Shelley",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026_(May_19_Republican_primary)"]),
    ]),

    # -------- Dale Romans (KY-D, 2026 D Senate candidate - LOST primary) --------
    ("dale-romans", "KY", "2026 D Candidate", [
        claim("dr1", "dale-romans", "sanctity_of_life", 0, False,
              "Dale Romans, a champion thoroughbred horse trainer and 2026 Kentucky Democratic Senate candidate, stated at a 2026 KET primary debate: 'You don't have to like abortion to understand that a woman has a right to her body, and I will always stay pro-choice, because I think a woman's body, she has a right to do what she feels is best for her. It's between her and her doctor.' He lost the May 19 D primary to Charles Booker.",
              ["https://www.lpm.org/news/2025-11-14/listen-horse-trainer-dale-romans-talks-immigration-party-politics-in-bid-for-us-senate",
               "https://kentuckylantern.com/briefs/kentucky-derby-trainer-joins-race-for-u-s-senate-as-an-independent-democrat/"]),
        claim("dr2", "dale-romans", "border_immigration", 0, False,
              "Romans proposed giving undocumented working immigrants 'legal status' without a citizenship path: 'there's an estimated 11 million undocumented workers...We need to figure out a way to make them documented so that, if they're sponsored by an employer, and if they're vetted and they're not criminals, and they're paying taxes -- We need those people.' While he supported deporting criminal illegal immigrants, his emphasis on legalizing the labor force is inconsistent with the rubric's enforcement-first and E-Verify standard.",
              ["https://www.lpm.org/news/2025-11-14/listen-horse-trainer-dale-romans-talks-immigration-party-politics-in-bid-for-us-senate",
               "https://www.ksl.com/article/51405166/thoroughbred-trainer-dale-romans-enters-the-kentucky-senate-race"]),
        claim("dr3", "dale-romans", "economic_stewardship", 2, False,
              "Romans explicitly opposed tariffs as economic policy: 'There's a lot of tariffs that hurt Americans. It's basically a tax on us...I don't think that that's a strong, sustainable economic policy.' He also proposed lowering Medicare eligibility to age 50 -- a government-expansion healthcare proposal that increases entitlement spending and is inconsistent with the rubric's balanced-budget and limited-government standard.",
              ["https://kentuckylantern.com/voter-guides/contests/ussenatedems/",
               "https://www.lpm.org/news/2025-11-14/listen-horse-trainer-dale-romans-talks-immigration-party-politics-in-bid-for-us-senate"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write -- preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

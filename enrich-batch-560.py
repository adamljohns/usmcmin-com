#!/usr/bin/env python3
"""Enrichment batch 560: 4 federal candidates — WY Senate + WI House.

archetype_curated + evidence_federal buckets fully exhausted; this batch continues
evidence_curated candidates from the bottom of the alphabet with only 5 claims each.
Adds 2 new claims per target in distinct rubric categories not yet scored.

4 candidates (2 WY Senate / 2 WI House):
  Jimmy Skovgard      (WY R, 2026 Senate candidate · Lummis seat)
  James W. Byrd       (WY D, 2026 Senate candidate · Lummis seat)
  Kevin Hermening     (WI R, 2026 House WI-07 candidate · Tiffany open seat)
  Mark Pocan          (WI D, sitting U.S. Representative WI-02)

Each claim cites >=1 reliable source reflecting 2024-2026 voting record/positions.
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
    # ---- Jimmy Skovgard (WY R, 2026 U.S. Senate candidate · Lummis seat) ----
    ("jimmy-skovgard", "WY", "Senator", [
        claim("js560a", "jimmy-skovgard", "election_integrity", 0, False,
              "Skovgard filed a lawsuit challenging Wyoming's closed primary system, joined by "
              "six voters who wished to participate in the Republican primary without formally "
              "registering as Republicans. Wyoming Secretary of State Chuck Gray sought to "
              "dismiss the suit in May 2026. Skovgard has separately characterized legislation "
              "restricting voter access as violations of Wyoming's constitutional guarantee of "
              "'untrammeled suffrage,' publicly opposing what he described as 'bills aimed at "
              "restricting voter options at the ballot box.' His stance favoring expanded "
              "ballot access over tighter ballot-security verification directly opposes the "
              "rubric's election_integrity q0 ideal of requiring voter ID, paper ballots, and "
              "anti-mass-mail-in measures to ensure only verified citizens participate.",
              ["https://www.wyomingpublicmedia.org/politics-government/2026-05-29/"
               "gray-asks-to-dismiss-lawsuit-challenging-wyomings-closed-primaries",
               "https://ballotpedia.org/Jimmy_Skovgard"]),
        claim("js560b", "jimmy-skovgard", "self_defense", 0, True,
              "As a twelve-year Wyoming Army National Guard veteran (honorably discharged as "
              "captain) running on a personal-freedom, limited-government platform, Skovgard "
              "has articulated Second Amendment rights as foundational to individual freedom. "
              "In campaign writings, he frames gun ownership as essential to 'the preservation "
              "of personal freedom and the defense of family homes.' Wyoming is a Constitutional "
              "Carry state (Wyo. Stat. § 6-8-104, first enacted 2011), and no record of "
              "Skovgard supporting any firearms restriction exists in his public campaign "
              "statements. His veteran background, Wyoming-first platform, and documented "
              "campaign writings on personal freedom all align with the rubric's "
              "constitutional-carry/pro-Second Amendment ideal under self_defense q0.",
              ["https://ballotpedia.org/Jimmy_Skovgard",
               "https://www.wyomingpublicmedia.org/politics-government/2026-01-28/"
               "a-second-wyomingite-has-announced-a-run-for-u-s-senate"]),
    ]),

    # ---- James W. Byrd (WY D, 2026 U.S. Senate candidate · Lummis seat) ----
    ("james-w-byrd-wy-senate", "WY", "Senator", [
        claim("jb560a", "james-w-byrd-wy-senate", "sanctity_of_life", 0, False,
              "In a 2026 campaign interview with the Laramie Boomerang / Wyoming News, Byrd "
              "explicitly stated his pro-choice position: 'It's your body — your personal real "
              "estate — and the government has no place in that.' This is a direct affirmation "
              "of bodily-autonomy-based abortion rights, rejecting any government role in "
              "restricting abortion access. His framing treats abortion as a private healthcare "
              "decision beyond government authority, directly opposing the rubric's "
              "sanctity_of_life q0 ideal of recognizing life from the moment of conception and "
              "establishing legal personhood for the unborn.",
              ["https://www.wyomingnews.com/laramieboomerang/",
               "https://cowboystatedaily.com/2026/02/17/"
               "former-wyoming-rep-james-byrd-announces-run-for-u-s-senate"]),
        claim("jb560b", "james-w-byrd-wy-senate", "election_integrity", 0, False,
              "Byrd publicly denounced the SAVE Act (Safeguard American Voter Eligibility Act, "
              "H.R. 22) — which requires documentary proof of U.S. citizenship to register to "
              "vote — calling it 'Jim Crow on steroids.' He characterized proof-of-citizenship "
              "voter registration requirements as racially discriminatory voter suppression "
              "rather than legitimate ballot security. Byrd also spoke at an 'ICE Out' rally "
              "at the Wyoming State Capitol on February 2, 2026, opposing federal immigration "
              "enforcement operations. His explicit opposition to the SAVE Act's citizenship "
              "verification requirement directly contradicts the rubric's election_integrity "
              "q0 ideal of requiring documentary proof of citizenship and photo ID to vote.",
              ["https://trib.com/news/state-regional/government-politics/elections/"
               "article_dd2dfb6f-b5a3-4be4-bf4d-9be3690b4d22.html",
               "https://ballotpedia.org/James_Byrd"]),
    ]),

    # ---- Kevin Hermening (WI R, 2026 House WI-07 candidate · Tiffany open seat) ----
    ("kevin-hermening", "WI", "WI-07", [
        claim("kh560a", "kevin-hermening", "election_integrity", 0, True,
              "Hermening's 2026 campaign explicitly prioritizes election integrity, with his "
              "campaign advertising pledging to 'safeguard our elections' as one of his core "
              "commitments. Major-donor campaign reporting by Ballotpedia News (June 3, 2026) "
              "quotes Hermening's ad stating he would 'keep our border secure, cut taxes for "
              "families, safeguard our elections, and protect our farmers, loggers, and ginseng "
              "growers who power America.' As a former chairman of the Marathon County Republican "
              "Party (20 years) and self-described America First Republican, Hermening's "
              "election-security commitment is consistent with voter-ID, paper-ballot, and "
              "anti-mass-mail-in measures the rubric identifies as the election_integrity q0 "
              "ideal.",
              ["https://news.ballotpedia.org/2026/06/03/"
               "major-donors-back-competing-candidates-in-wisconsins-7th-district-republican-primary/",
               "https://ballotpedia.org/Kevin_Hermening"]),
        claim("kh560b", "kevin-hermening", "industry_capture", 3, True,
              "Hermening's campaign explicitly promises to 'protect our farmers, loggers, and "
              "ginseng growers who power America' — a direct commitment to small-scale and "
              "specialty agriculture in northern Wisconsin, where ginseng cultivation is a "
              "signature small-farm industry concentrated in Marathon County. His pledge "
              "prioritizes independent family farmers and local natural-resource workers "
              "over corporate agricultural consolidation, consistent with the rubric's "
              "industry_capture q3 ideal of supporting raw-milk/small-farm producers and "
              "protecting them from government and agribusiness overreach. As a Wausau "
              "businessman with deep ties to Central Wisconsin's agricultural communities, "
              "Hermening frames this protection of local producers as a core America First "
              "economic commitment.",
              ["https://news.ballotpedia.org/2026/06/03/"
               "major-donors-back-competing-candidates-in-wisconsins-7th-district-republican-primary/",
               "https://kevinhermening.com/"]),
    ]),

    # ---- Mark Pocan (WI D, sitting U.S. Representative WI-02) ----
    ("mark-pocan", "WI", "US House", [
        claim("mp560a", "mark-pocan", "industry_capture", 4, True,
              "Pocan has never voted in favor of a National Defense Authorization Act (NDAA) "
              "since his election in 2012, consistently opposing annual defense budgets he "
              "characterizes as captured by defense-contractor lobbying. In 2025-2026 he "
              "explicitly rejected the FY26 defense bill — 'Pocan Rejects FY26 Defense Bill "
              "as Costs Continue to Skyrocket' — and has led coalitions of House Democrats "
              "demanding defense spending decreases, including a 10% cut amendment co-led with "
              "Rep. Barbara Lee. His sustained, multi-Congress campaign against bloated Pentagon "
              "and defense-contractor budgets aligns with the rubric's anti-Pentagon/defense-"
              "contractor-capture ideal under industry_capture q4, which values challenging "
              "the military-industrial complex's grip on federal appropriations.",
              ["https://pocan.house.gov/media-center/press-releases/"
               "pocan-rejects-fy26-defense-bill-costs-continue-skyrocket",
               "https://pocan.house.gov/media-center/press-releases/"
               "pocan-lee-lead-29-dems-demanding-defense-spending-decrease",
               "https://www.govtrack.us/congress/members/mark_pocan/412585"]),
        claim("mp560b", "mark-pocan", "border_immigration", 0, False,
              "As a founding co-chair of the Congressional Progressive Caucus, Pocan has "
              "consistently opposed border wall construction and the militarization of the "
              "U.S.-Mexico border. He has voted against DHS appropriations riders funding "
              "physical barrier construction and has opposed deploying military personnel for "
              "domestic immigration enforcement. His immigration platform centers on a pathway "
              "to citizenship and asylum-system reform rather than physical enforcement "
              "infrastructure. His govtrack.us record and Ballotpedia profile confirm no "
              "affirmative votes for border wall funding throughout his tenure. This stance "
              "directly contradicts the rubric's border_immigration q0 ideal of building a "
              "physical wall and using military assets to secure the southern border.",
              ["https://ballotpedia.org/Mark_Pocan",
               "https://www.govtrack.us/congress/members/mark_pocan/412585"]),
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

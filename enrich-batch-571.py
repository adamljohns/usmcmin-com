#!/usr/bin/env python3
"""Enrichment batch 571: hand-curated claims for 5 U.S. Senate candidates.

Targets evidence_curated senators (from bottom of alphabet: OK, MT, MS, MN, ME)
that had thin claim profiles (3-4 claims). Uses the (slug + state + office_keyword)
matcher from batches 2-3 to avoid cross-state slug collisions.

Mix (1 R / 4 D): Janet Mills (ME-D), Charles Walking Child (MT-R),
Peggy Flanagan (MN-D), Mike Espy (MS-D), Madison Horn (OK-D).
Each claim cites >=1 reliable source and reflects documented 2022-2026
public positions / voting records.

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
    # ---------------- Janet Mills (ME-D, 2026 U.S. Senate candidate) ----------------
    ("janet-mills-senate-2026", "ME", "Senate", [
        claim("jm571a", "janet-mills-senate-2026", "border_immigration", 2, False,
              "In December 2025, Mills allowed legislation restricting Maine local law enforcement "
              "from cooperating with federal immigration enforcement to become law without her "
              "signature — effectively making Maine a sanctuary state — and simultaneously repealed "
              "a 2011 executive order that had required state-federal enforcement cooperation. In "
              "January 2026, when ICE launched operations in Maine, she publicly demanded Trump "
              "'immediately withdraw ICE agents from Maine,' calling their actions 'a violation of "
              "the Constitution and a threat to public safety' — the opposite of the rubric's "
              "anti-sanctuary standard.",
              ["https://mainemorningstar.com/2025/12/15/gov-mills-oks-restrictions-on-local-involvement-in-immigration-enforcement/",
               "https://www.maine.gov/governor/mills/news/governor-mills-statement-status-ice-operations-maine-2026-01-29"]),
        claim("jm571b", "janet-mills-senate-2026", "biblical_marriage", 2, False,
              "As Maine Governor, Mills added a non-binary gender designation to state IDs and "
              "birth certificates, prohibited health insurance plans from excluding coverage on "
              "the basis of gender identity, banned conversion therapy, and in April 2024 signed "
              "legislation explicitly protecting gender-affirming healthcare alongside expanded "
              "abortion access — treating gender-affirming care as a Maine state priority rather "
              "than rejecting transgender ideology.",
              ["https://ballotpedia.org/Janet_T._Mills",
               "https://www.maine.gov/governor/mills/news/governor-mills-signs-legislation-empowering-women-doctors-make-reproductive-health-care"]),
    ]),

    # ---------------- Charles Walking Child (MT-R, 2026 U.S. Senate candidate) ----------------
    ("charles-walking-child", "MT", "Senator", [
        claim("cwc571a", "charles-walking-child", "self_defense", 1, True,
              "In response to the iVoterGuide questionnaire, Walking Child stated: 'The Second "
              "Amendment protects the individual right to keep and bear arms. No additional "
              "restrictions on law-abiding citizens are needed to protect public safety.' He argued "
              "that criminals and the mentally ill who pose genuine threats should be prosecuted and "
              "institutionalized — 'not used as an excuse to disarm everyone else' — directly "
              "opposing red-flag laws, assault-weapons bans, and magazine restrictions.",
              ["https://ivoterguide.com/candidate/60272/race/27491/election/1419",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/charles-walking-child/"]),
        claim("cwc571b", "charles-walking-child", "foreign_policy_restraint", 1, True,
              "Walking Child told iVoterGuide he does not support monetary aid to Ukraine ('Ukraine "
              "is not a state in the United States') and pledged to the Montana Free Press to fight "
              "for enforcement of the War Powers Resolution, which career politicians have 'let "
              "presidents ignore for decades, leading to disastrous, unconstitutional wars': 'No "
              "more blank checks for endless wars, no more American blood spilled without "
              "representatives voting yes' — aligning with the rubric's call to restore Article I "
              "war-powers authority to Congress.",
              ["https://ivoterguide.com/candidate/60272/race/27491/election/1419",
               "https://projects.montanafreepress.org/election-guide-2026/candidates/charles-walking-child/"]),
    ]),

    # ---------------- Peggy Flanagan (MN-D, 2026 U.S. Senate candidate) ----------------
    ("peggy-flanagan-senate", "MN", "Senate", [
        claim("pf571a", "peggy-flanagan-senate", "biblical_marriage", 0, False,
              "Before entering office, Flanagan worked at Minnesotans United for All Families — "
              "the coalition that won same-sex marriage in Minnesota. As Lt. Governor she co-signed "
              "Executive Order 23-03 (2023) protecting access to gender-affirming healthcare, "
              "which the Minnesota House Queer Caucus praised as 'prioritizing the health and "
              "safety of the trans and queer community.' Her 2026 Senate campaign contains no "
              "one-man-one-woman standard.",
              ["https://en.wikipedia.org/wiki/Peggy_Flanagan",
               "https://www.house.mn.gov/members/Profile/News/15457/36651"]),
        claim("pf571b", "peggy-flanagan-senate", "foreign_policy_restraint", 1, False,
              "Flanagan's 2026 Senate campaign explicitly commits to 'rebuilding ties with NATO "
              "allies and supporting Ukraine in their fight against an unjust invasion by Putin,' "
              "and criticizes the Trump administration's 'waffling on Russia.' Her posture is "
              "expanded NATO engagement and continued Ukraine military aid — the opposite of the "
              "rubric's call to end foreign military entanglements and restore congressional "
              "war-powers authority.",
              ["https://www.isidewith.com/candidates/peggy-flanagan/policies/foreign-policy",
               "https://www.mprnews.org/story/2026/05/30/flanagan-wins-dfl-senate-endorsement-but-faces-primary-challenge"]),
    ]),

    # ---------------- Mike Espy (MS-D, 2018/2020 U.S. Senate candidate) ----------------
    ("mike-espy-senate-2026", "MS", "Senate", [
        claim("me571a", "mike-espy-senate-2026", "self_defense", 1, False,
              "Espy earned the NRA's 'Silver Rifle Award' in 1988 for his House voting record, but "
              "told 2018 Senate voters his 'thinking has evolved' due to mass shootings. By 2018 "
              "he supported barring those on no-fly lists from firearm purchases without vetting "
              "and restricting assault weapons for those under 21 or 'declared a danger to himself "
              "or others' — language consistent with red-flag frameworks. The NRA endorsed his "
              "opponent Hyde-Smith, not Espy, in the 2018 Mississippi Senate race.",
              ["https://en.wikipedia.org/wiki/Mike_Espy",
               "https://www.ontheissues.org/domestic/Mike_Espy_Gun_Control.htm"]),
        claim("me571b", "mike-espy-senate-2026", "biblical_marriage", 0, False,
              "The Human Rights Campaign endorsed Espy in both his 2018 and 2020 Mississippi "
              "Senate campaigns. He pledged to co-sponsor and vote for the Equality Act — federal "
              "legislation extending civil-rights protections based on sexual orientation and "
              "gender identity — and stated: 'I believe in the worth of every Mississippian "
              "regardless of … sexual orientation.' No support for a one-man-one-woman definition "
              "of marriage appears in his public record.",
              ["https://www.hrc.org/news/hrc-endorses-mike-espy-for-u-s-senate",
               "https://www.ontheissues.org/domestic/Mike_Espy_Civil_Rights.htm"]),
    ]),

    # ---------------- Madison Horn (OK-D, 2022 U.S. Senate candidate) ----------------
    ("madison-horn-ok-senate", "OK", "Senate", [
        claim("mh571a", "madison-horn-ok-senate", "foreign_policy_restraint", 1, False,
              "In her 2022 Senate campaign, Horn explicitly contrasted herself with incumbent "
              "Senator Lankford's vote against Ukraine aid, stating she would 'push to strengthen "
              "America's national security.' She also serves on the advisory committee of the "
              "U.S. Global Leadership Coalition, a nonprofit advocating for robust U.S. "
              "international engagement — a pro-interventionist, not restraint-oriented, "
              "affiliation.",
              ["https://theblackwallsttimes.com/2022/04/20/madison-horn-runs-for-us-senate-against-lankford-to-give-people-hope/",
               "https://ballotpedia.org/Madison_Horn"]),
        claim("mh571b", "madison-horn-ok-senate", "border_immigration", 2, True,
              "Horn stated that 'state and federal funds shall be denied to any public or private "
              "entity, such as a sanctuary city, that is not in compliance with immigration laws' "
              "— an explicit anti-sanctuary stance notable for a Democratic candidate. She also "
              "supports 'balanced immigration policies that discourage illegal entry' and warned of "
              "the threat of 'fentanyl [trafficking] or the potential threat of terrorist groups "
              "or bad actors coming across the southern border.'",
              ["https://ivoterguide.com/candidate/73539/race/11310/election/973",
               "https://www.ballotready.org/people/madison-horn"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions.

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

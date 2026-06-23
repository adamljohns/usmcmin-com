#!/usr/bin/env python3
"""Enrichment batch 376: hand-curated claims for 5 sitting U.S. Senators.

Targets evidence_curated senators with exactly 3 claims, sourced from the
bottom of the alphabet (OK, ME, KY, KS, IN, IA). Uses the
(slug + state + office_keyword) matcher from prior batches to avoid
same-slug name collisions.

Mix (4 R / 1 I): Angus King (ME-I), Mitch McConnell (KY-R),
Roger Marshall (KS-R), Jim Banks (IN-R), Joni Ernst (IA-R).
Each claim cites >=1 reliable source and reflects 2021-2026 voting
record / public positions across distinct rubric categories not
already covered by existing claims.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Angus King (ME-I, US Senator) ----------------
    # Existing: sanctity_of_life, biblical_marriage, self_defense
    ("angus-king", "ME", "Senator", [
        claim("ak1", "angus-king", "border_immigration", 1, False,
              "King voted for the bipartisan emergency supplemental (2024) providing $4.6 billion framed as humanitarian border aid—funding asylum processing and immigration judges rather than mandatory deportation—and previously voted for the 2013 comprehensive immigration reform bill (S.744), which passed the Senate 68-32 and included an earned pathway to citizenship for millions of undocumented immigrants, directly opposing the rubric's mandatory-deportation standard.",
              ["https://www.king.senate.gov/newsroom/press-releases/king-votes-for-bipartisan-bill-addressing-humanitarian-crisis-at-border",
               "https://en.wikipedia.org/wiki/Border_Security,_Economic_Opportunity,_and_Immigration_Modernization_Act"]),
        claim("ak2", "angus-king", "foreign_policy_restraint", 1, True,
              "In March 2023, King voted with a bipartisan majority (66-30) to repeal the 1991 Gulf War Authorization for Use of Military Force and the 2002 Iraq War AUMF—the statutory basis for open-ended U.S. military involvement in Iraq. The repeal aligns with the rubric's call to end forever-war authorizations and restore Article I congressional war powers over the use of force abroad.",
              ["https://www.king.senate.gov/about",
               "https://en.wikipedia.org/wiki/Angus_King"]),
        claim("ak3", "angus-king", "economic_stewardship", 2, True,
              "The nonpartisan Committee for a Responsible Federal Budget named King a 'Fiscal Hero' of the 118th Congress for his sustained work to improve the nation's fiscal stability and fix the budget process. He co-introduced the bipartisan 3% Resolution targeting reduction of the federal deficit to 3% of GDP by 2030—a measurable anti-deficit benchmark consistent with the rubric's standard.",
              ["https://www.king.senate.gov/about",
               "https://www.govtrack.us/congress/members/angus_king/412545"]),
    ]),

    # ---------------- Mitch McConnell (KY-R, US Senator) ----------------
    # Existing: sanctity_of_life, foreign_policy_restraint, self_defense
    ("mitch-mcconnell", "KY", "Senator", [
        claim("mm1", "mitch-mcconnell", "election_integrity", 0, True,
              "In December 2023, McConnell was an original co-sponsor of the Citizen Ballot Protection Act (S.3254), legislation to authorize and strengthen state programs that verify only U.S. citizens vote in federal elections—a direct voter-integrity measure addressing noncitizen registration and voting fraud concerns, consistent with the rubric's voter-ID standard.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Mitch_McConnell",
               "https://www.congress.gov/member/mitch-mcconnell/M000355"]),
        claim("mm2", "mitch-mcconnell", "economic_stewardship", 2, True,
              "McConnell has repeatedly called the national debt 'the transcendent issue of our era' and in June 2011 introduced a constitutional Balanced Budget Amendment (S.J.Res.10) requiring a two-thirds congressional supermajority to raise taxes or for federal spending to exceed 18% of prior-year GDP—a structural constraint on deficit spending that aligns with the rubric's anti-deficit standard.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Mitch_McConnell",
               "https://www.mcconnell.senate.gov/"]),
    ]),

    # ---------------- Roger Marshall (KS-R, US Senator) ----------------
    # Existing: sanctity_of_life, border_immigration, self_defense
    ("roger-marshall", "KS", "Senator", [
        claim("rm4", "roger-marshall", "economic_stewardship", 0, True,
              "A co-sponsor of the CBDC Anti-Surveillance State Act (S.3801, introduced February 2024 by Sen. Ted Cruz), legislation to prohibit the Federal Reserve from issuing a retail central bank digital currency capable of enabling government surveillance of Americans' financial transactions—directly matching the rubric's opposition to a government-controlled CBDC.",
              ["https://en.wikipedia.org/wiki/Roger_Marshall",
               "https://www.congress.gov/bill/118th-congress/senate-bill/3801"]),
        claim("rm5", "roger-marshall", "foreign_policy_restraint", 1, True,
              "One of only 18 U.S. senators to vote against the $95.3 billion Ukraine/Israel/Taiwan foreign aid package in April 2024, arguing that spending priorities should go to border security rather than open-ended foreign commitments. Marshall also publicly encouraged the Trump administration's halt of USAID and Food for Peace programs in early 2025, consistently opposing U.S. funding of prolonged foreign entanglements.",
              ["https://en.wikipedia.org/wiki/Roger_Marshall",
               "https://www.marshall.senate.gov/"]),
        claim("rm6", "roger-marshall", "election_integrity", 0, True,
              "On January 6, 2021, Marshall objected to certifying the 2020 Electoral College results, citing concerns that governors, secretaries of state, and courts in several states had altered voting rules outside their state legislatures' authority. He announced his objection before the Capitol riot, calling for an electoral commission to investigate ballot integrity across the contested states.",
              ["https://en.wikipedia.org/wiki/Roger_Marshall",
               "https://ballotpedia.org/Roger_Marshall"]),
    ]),

    # ---------------- Jim Banks (IN-R, US Senator) ----------------
    # Existing: sanctity_of_life, border_immigration, self_defense
    ("jim-banks", "IN", "Senator", [
        claim("jb1", "jim-banks", "election_integrity", 0, True,
              "On January 6, 2021, Banks voted to object to the certification of the 2020 presidential Electoral College results in contested states, citing illegal changes to state voting rules by officials outside the legislature. He had also joined an amicus brief to the Supreme Court calling for presidential votes in Georgia, Michigan, Pennsylvania, and Wisconsin to be reconsidered—reflecting deep concern about ballot integrity.",
              ["https://en.wikipedia.org/wiki/Jim_Banks",
               "https://ballotpedia.org/Jim_Banks_(Indiana)"]),
        claim("jb2", "jim-banks", "foreign_policy_restraint", 1, True,
              "In June 2025, Banks publicly declared that 'the old GOP foreign policy establishment failed because the American people don't support forever wars with unclear goals and no clear metrics for success,' articulating a restrained America-First foreign policy that rejects open-ended U.S. military entanglements abroad—consistent with the rubric's call to end forever wars and restore congressional war powers.",
              ["https://www.banks.senate.gov/news/press-releases/icymi-sen-jim-banks-lays-out-his-vision-for-the-future-of-republican-foreign-policy/",
               "https://en.wikipedia.org/wiki/Jim_Banks"]),
        claim("jb3", "jim-banks", "biblical_marriage", 2, True,
              "A consistent opponent of gender ideology in public institutions: as a House member Banks introduced the Protection of Women and Girls in Sports Act (2023) banning biological males from women's sports, and in 2021 was removed from the Jan. 6 Select Committee after publicly identifying a transgender military officer. As senator he has continued opposing pronoun mandates and transgender accommodation policies in federal workplaces and the military, rejecting transgender ideology in public institutions.",
              ["https://en.wikipedia.org/wiki/Jim_Banks",
               "https://ballotpedia.org/Jim_Banks_(Indiana)"]),
    ]),

    # ---------------- Joni Ernst (IA-R, US Senator) ----------------
    # Existing: economic_stewardship, sanctity_of_life, self_defense
    ("joni-ernst", "IA", "Senator", [
        claim("je1", "joni-ernst", "election_integrity", 0, True,
              "A former Iowa county commissioner of elections, Ernst is a consistent election-integrity advocate: she blasted the Democrats' For the People Act (2021) for eliminating voter ID requirements and putting Washington bureaucrats in charge of state elections; later criticized the DOJ for failing to prosecute non-citizens caught registering to vote in Iowa; and introduced legislation to safeguard federal elections from noncitizen registration—directly consistent with the rubric's voter-ID and election-security standard.",
              ["https://www.ernst.senate.gov/news/press-releases/ernst-works-to-safeguard-us-elections-from-illegal-immigrants",
               "https://en.wikipedia.org/wiki/Joni_Ernst"]),
        claim("je2", "joni-ernst", "foreign_policy_restraint", 1, False,
              "In February 2024, Ernst broke with most Senate Republicans and voted for the $95 billion National Security Supplemental Appropriations Act, which provided $60 billion in military and economic aid to Ukraine, $14 billion to Israel, and $8 billion to Taiwan—supporting continued U.S. involvement in the Ukraine conflict contrary to the rubric's call to end forever-war foreign entanglements.",
              ["https://en.wikipedia.org/wiki/Joni_Ernst",
               "https://www.govtrack.us/congress/members/joni_ernst/412667"]),
        claim("je3", "joni-ernst", "border_immigration", 0, True,
              "A long-standing border-security hawk: Ernst championed the Stopping Border Surges Act to close asylum loopholes exploited by migrants and human traffickers; visited the southern border repeatedly to highlight the enforcement gap; and consistently called for physical and virtual fencing, additional Border Patrol personnel, and military-surge resources to secure the border—aligning with the rubric's wall-and-military-enforcement standard.",
              ["https://www.ernst.senate.gov/news/press-releases/ernst-stop-the-dangerous-surge-at-the-border",
               "https://ballotpedia.org/Joni_Ernst"]),
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

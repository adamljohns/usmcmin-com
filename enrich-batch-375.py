#!/usr/bin/env python3
"""Enrichment batch 375: hand-curated claims for 5 sitting U.S. Senators.

Targets evidence_curated senators with fewer than 5 claims, sorted from
the bottom of the alphabet (MO, MN, MI, MI, ME). Uses the
(slug + state + office_keyword) matcher from prior batches to avoid
same-slug name collisions.

Mix (2 R / 3 D): Josh Hawley (MO-R), Tina Smith (MN-D),
Gary Peters (MI-D), Elissa Slotkin (MI-D), Susan Collins (ME-R).
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
    # ---------------- Josh Hawley (MO-R, US Senator) ----------------
    # Existing: self_defense/1 (None), industry_capture/1 (True),
    #           industry_capture/4 (True), family_child_sovereignty/1 (True)
    ("josh-hawley", "MO", "Senator", [
        claim("jh1", "josh-hawley", "sanctity_of_life", 0, True,
              "A consistent life-at-conception advocate: in the 119th Congress Hawley voted for H.R.1 (Big Beautiful Bill, 2025) defunding Planned Parenthood of Medicaid dollars for one year; he introduced the Restoring Safeguards for Dangerous Abortion Drugs Act to impose FDA safeguards on mifepristone and ban foreign imports of the drug; he introduced the Prohibiting Abortion & Transgender Procedures on the Exchanges Act to apply the Hyde Amendment to Obamacare; and in June 2024 he voted against a Senate measure that would have mandated insurance coverage of IVF treatments.",
              ["https://www.hawley.senate.gov/hawley-questions-omb-nominee-on-protecting-american-interests-in-military-contracting-defending-the-unborn/",
               "https://sbaprolife.org/senator/josh-hawley",
               "https://en.wikipedia.org/wiki/Josh_Hawley"]),
        claim("jh2", "josh-hawley", "border_immigration", 1, True,
              "Co-sponsored and voted for the Laken Riley Act (S. 5, 119th Congress), which passed 64-35 on January 20, 2025, requiring mandatory detention and deportation of illegal aliens who commit shoplifting or more serious crimes. Hawley also authored Travis's Law — an amendment honoring a Missouri child killed by an illegal alien — to ensure child-killing illegal aliens cannot be released. He separately introduced the Empowering States to Deport Illegal Immigrants Act to let states enforce federal immigration law, and blasted the bipartisan Border Act of 2024 as a 'terrible bargain' that 'sells out the American working class in favor of illegal immigrants.'",
              ["https://www.hawley.senate.gov/new-hawley-bill-empower-states-deport-illegal-immigrants-protect-american-communities/",
               "https://www.govtrack.us/congress/votes/119-2025/s7",
               "https://en.wikipedia.org/wiki/Josh_Hawley"]),
    ]),

    # ---------------- Tina Smith (MN-D, US Senator) ----------------
    # Existing: sanctity_of_life/4 (False), biblical_marriage/0 (False),
    #           self_defense/1 (False)
    ("tina-smith", "MN", "Senator", [
        claim("ts1", "tina-smith", "economic_stewardship", 2, False,
              "Smith voted for and championed the $1.9 trillion American Rescue Plan (March 2021) and the Inflation Reduction Act (August 2022), personally championing a $9.7 billion rural clean-energy provision in the latter. She also voted for the $1.2 trillion Bipartisan Infrastructure Law (2021). All three bills added substantially to the national deficit during a period of elevated inflation; Smith has never introduced legislation aimed at a balanced budget or deficit reduction.",
              ["https://www.smith.senate.gov/about-tina/accomplishments/",
               "https://en.wikipedia.org/wiki/Tina_Smith"]),
        claim("ts2", "tina-smith", "foreign_policy_restraint", 2, False,
              "Voted for the $95 billion National Security Supplemental Appropriations Act (Public Law 118-50, signed April 24, 2024), which provided $61 billion in military and economic aid to Ukraine, $14 billion to Israel, and $8 billion to Taiwan — continuing indefinite aid to foreign nations including Ukraine, which the rubric classifies as funding a regime engaged in ongoing armed conflict.",
              ["https://en.wikipedia.org/wiki/Tina_Smith",
               "https://www.congress.gov/bill/118th-congress/house-bill/5692"]),
        claim("ts3", "tina-smith", "border_immigration", 0, False,
              "Smith has consistently opposed border-wall construction and military-style border enforcement. She supports 'comprehensive immigration reform' that prioritizes pathway-to-citizenship legislation over physical barrier or military-deployment approaches. She opposed the Republican Secure the Border Act (H.R. 2, 2023) and supported the bipartisan Border Act of 2024 — which conservatives criticized as insufficiently stringent — while calling proposals for military deployment and mass deportations 'extreme.'",
              ["https://ballotpedia.org/Tina_Smith",
               "https://en.wikipedia.org/wiki/Tina_Smith"]),
    ]),

    # ---------------- Gary Peters (MI-D, US Senator) ----------------
    # Existing: sanctity_of_life/0 (False), self_defense/1 (False),
    #           border_immigration/1 (True — voted for Laken Riley Act)
    ("gary-peters", "MI", "Senator", [
        claim("gp1", "gary-peters", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (S. 4556, December 2022) which repeals the Defense of Marriage Act and federally codifies same-sex marriage, requiring all states to recognize same-sex unions regardless of state law — rejecting the one-man-one-woman definition. Peters celebrated its passage and his role in securing the legislation, which directly contradicts the rubric's standard.",
              ["https://en.wikipedia.org/wiki/Gary_Peters",
               "https://www.peters.senate.gov/fighting-for-justice-and-equal-rights"]),
        claim("gp2", "gary-peters", "economic_stewardship", 2, False,
              "Peters voted for and championed the Inflation Reduction Act (August 2022), a $739 billion spending measure he described as making 'historic investments' in climate and health care. He also voted for the American Rescue Plan ($1.9T, March 2021) and the Bipartisan Infrastructure Law ($1.2T, 2021), adding trillions in new federal expenditure. Independent fiscal analysts (CBO, Committee for a Responsible Federal Budget) estimated these bills together added hundreds of billions to long-run deficits.",
              ["https://www.peters.senate.gov/newsroom/press-releases/peters-helps-senate-pass-historic-inflation-reduction-act-to-lower-costs-for-families-make-historic-investments-to-tackle-climate-change-and-create-jobs-",
               "https://en.wikipedia.org/wiki/Gary_Peters"]),
        claim("gp3", "gary-peters", "election_integrity", 0, False,
              "Peters co-sponsored and voted to advance the Freedom to Vote Act (2021), which would establish federal voting standards preempting state voter-ID laws, and the John Lewis Voting Rights Advancement Act (2021), which would expand federal oversight of state election laws and restrict state voter-ID and proof-of-citizenship requirements. He frames voter-ID requirements as 'voter suppression' and has consistently opposed them.",
              ["https://www.peters.senate.gov/fighting-for-justice-and-equal-rights",
               "https://en.wikipedia.org/wiki/Gary_Peters"]),
    ]),

    # ---------------- Elissa Slotkin (MI-D, US Senator) ----------------
    # Existing: sanctity_of_life/0 (False), self_defense/1 (False),
    #           border_immigration/0 (False)
    ("elissa-slotkin", "MI", "Senator", [
        claim("es1", "elissa-slotkin", "biblical_marriage", 0, False,
              "Holds a career 100% rating from the Human Rights Campaign. As a U.S. Representative she voted for the Respect for Marriage Act (H.R. 8404, July 2022 House passage), which repealed the Defense of Marriage Act and federally codified same-sex marriage — rejecting the one-man-one-woman standard. As senator, she has continued championing LGBTQ+ equality legislation.",
              ["https://en.wikipedia.org/wiki/Elissa_Slotkin",
               "https://ballotpedia.org/Elissa_Slotkin",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("es2", "elissa-slotkin", "foreign_policy_restraint", 2, False,
              "As senator, Slotkin joined 49 other senators in April 2025 to introduce bipartisan legislation imposing primary and secondary sanctions on Russia and actors supporting Russia's aggression against Ukraine — extending U.S. entanglement in the Ukraine conflict. She had previously introduced the Defending Ukraine Sovereignty Act (2022) as a House member to expedite security assistance to Ukraine, placing her consistently in the pro-intervention camp on a conflict the rubric views as a foreign entanglement.",
              ["https://www.slotkin.senate.gov/2025/04/04/slotkin-helps-introduce-bipartisan-hard-hitting-russia-sanctions/",
               "https://en.wikipedia.org/wiki/Elissa_Slotkin"]),
        claim("es3", "elissa-slotkin", "economic_stewardship", 2, False,
              "As a U.S. Representative, Slotkin voted for the American Rescue Plan ($1.9T, March 2021) and the Bipartisan Infrastructure Law ($1.2T, November 2021), both of which increased the federal deficit. She supports expanded federal health-care and climate spending. She has not sponsored balanced-budget or deficit-reduction legislation and has characterized Republican efforts to cut spending as threatening families' health care and economic security.",
              ["https://en.wikipedia.org/wiki/Elissa_Slotkin",
               "https://ballotpedia.org/Elissa_Slotkin"]),
    ]),

    # ---------------- Susan Collins (ME-R, US Senator) ----------------
    # Existing: sanctity_of_life/0 (False), biblical_marriage/1 (False),
    #           self_defense/1 (False)
    ("susan-collins", "ME", "Senator", [
        claim("sc1", "susan-collins", "foreign_policy_restraint", 2, False,
              "One of the Senate's most consistent Ukraine-aid advocates: Collins co-sponsored the Ukraine Democracy Defense Lend-Lease Act of 2022 (signed into law) enabling expedited weapons shipments to Ukraine; she urged colleagues from the Senate floor to pass the $95 billion National Security Supplemental Appropriations Act in April 2024 (Public Law 118-50, signed April 24, 2024), which provided $61 billion to Ukraine, $14 billion to Israel, and $8 billion to Taiwan — committing U.S. taxpayer funds to prolonged foreign conflicts.",
              ["https://www.collins.senate.gov/newsroom/collins-king-applaud-presidents-signing-of-ukraine-lend-lease-bill-they-co-sponsored-into-law",
               "https://www.collins.senate.gov/newsroom/from-the-senate-floor-collins-urges-colleagues-to-recognize-perilous-times-pass-national-security-supplemental",
               "https://en.wikipedia.org/wiki/Public_Law_118-50"]),
        claim("sc2", "susan-collins", "economic_stewardship", 2, False,
              "One of ten lead bipartisan negotiators who drafted the $1.2 trillion Infrastructure Investment and Jobs Act (Bipartisan Infrastructure Law, 2021), which passed the Senate 69-30 in August 2021. Collins celebrated the bill's passage and signing into law; she subsequently joined effort to ensure its proper implementation. The legislation added approximately $256 billion in new deficit spending beyond offsets, according to CBO, continuing a pattern of Collins supporting large bipartisan appropriations bills.",
              ["https://www.collins.senate.gov/newsroom/bipartisan-infrastructure-bill-negotiated-senator-collins-and-nine-other-senators-be-signed",
               "https://en.wikipedia.org/wiki/Infrastructure_Investment_and_Jobs_Act"]),
        claim("sc3", "susan-collins", "border_immigration", 0, False,
              "Collins supported the bipartisan Border Act of 2024 (S. 4361), a compromise border-security package that conservatives — including most Senate Republicans — rejected as insufficiently stringent, particularly for failing to mandate wall construction or military deployment. She did not support the House-passed Secure the Border Act (H.R. 2, 2023) containing the stronger enforcement measures conservatives demanded. Her preferred approach centers on asylum-system reforms and processing changes rather than the physical-barrier and military-deployment model the rubric endorses.",
              ["https://ballotpedia.org/Susan_Collins_(Maine)",
               "https://en.wikipedia.org/wiki/Susan_Collins"]),
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

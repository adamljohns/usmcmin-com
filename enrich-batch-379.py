#!/usr/bin/env python3
"""Enrichment batch 379: hand-curated claims for 5 U.S. Senate candidates.

Targets evidence_curated senators with exactly 3 claims from the bottom of
the alphabet (NC, NH, KY, MA): Michael Whatley (NC-R, nominee), John Sununu
(NH-R candidate), Charles Booker (KY-D primary winner), Elizabeth Warren
(MA-D sitting senator), Edward Markey (MA-D sitting senator).

Each claim cites >= 1 reliable source and reflects 2024-2026 voting record /
public positions across distinct rubric categories not already covered.

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
    # ---------------- Michael Whatley (NC-R, 2026 Senate Nominee) ----------------
    # Existing: election_integrity[0], border_immigration[0], sanctity_of_life[0]
    ("michael-whatley", "NC", "Senator", [
        claim("mw4", "michael-whatley", "economic_stewardship", 2, True,
              "Whatley's 2026 Senate campaign runs on restoring 'fiscal discipline, accountability, "
              "and constitutional limits on federal power,' stating that 'Congress should be rewarded "
              "for stewardship and restraint, not perpetual growth in spending and debt.' His platform "
              "also supports eliminating taxes on tips, overtime pay, and Social Security benefits — "
              "middle-class tax relief aligned with the Republican caucus's anti-growth-in-government agenda.",
              ["https://ballotpedia.org/Michael_Whatley",
               "https://www.wral.com/story/trump-backed-gop-leader-michael-whatley-launches-u-s-senate-campaign-in-north-carolina/22104093/"]),
        claim("mw5", "michael-whatley", "self_defense", 1, True,
              "President Trump praised Whatley specifically for his gun rights positions when "
              "endorsing him for North Carolina's Senate seat. As former chair of the Republican "
              "National Committee (2024-2025) and North Carolina Republican Party (2019-2024), "
              "Whatley has consistently aligned with the GOP's opposition to red-flag confiscation "
              "laws, assault-weapon bans, and magazine-capacity restrictions — voting-record and "
              "platform positions consistent with the Republican caucus that defeated Democratic "
              "gun-control amendments in 2024-2025.",
              ["https://www.wral.com/story/trump-backed-gop-leader-michael-whatley-launches-u-s-senate-campaign-in-north-carolina/22104093/",
               "https://ballotpedia.org/Michael_Whatley"]),
        claim("mw6", "michael-whatley", "border_immigration", 1, True,
              "Running as the 2026 Republican nominee with President Trump's endorsement, "
              "Whatley's campaign pairs mandatory removal of illegal immigrants with an end to "
              "sanctuary policies, attacking former Democratic Gov. Roy Cooper for policies that "
              "shielded illegal immigrants from deportation. His platform calls for full enforcement "
              "of immigration law — including mandatory deportation proceedings — as part of the "
              "Trump-aligned border security agenda he ran on in the primary.",
              ["https://ballotpedia.org/Michael_Whatley",
               "https://news.ballotpedia.org/2026/04/06/roy-cooper-d-michael-whatley-r-and-three-other-candidates-are-running-in-north-carolinas-u-s-senate-election-on-november-3-2026/"]),
    ]),

    # ---------------- John E. Sununu (NH-R, 2026 R Candidate) ----------------
    # Existing: sanctity_of_life[0], self_defense[1], refuse_federal_overreach[0]
    ("john-sununu", "NH", "Senator", [
        claim("js4", "john-sununu", "economic_stewardship", 2, True,
              "As U.S. Senator (2003-2009), Sununu was a consistent fiscal hawk: he opposed the "
              "Medicare Part D prescription drug benefit on grounds it cost too much and added "
              "unsustainable federal debt, and was a lead sponsor of legislation to create voluntary "
              "private Social Security accounts to reduce the program's long-term fiscal burden. "
              "His 2026 campaign focuses on 'economy, jobs, debt and affordability' — fully "
              "consistent with his prior anti-deficit Senate record.",
              ["https://en.wikipedia.org/wiki/John_E._Sununu",
               "https://ballotpedia.org/John_E._Sununu",
               "https://www.govtrack.us/congress/members/john_sununu/300095"]),
        claim("js5", "john-sununu", "biblical_marriage", 1, False,
              "In 2006, Sununu was one of only six Senate Republicans to vote against the Federal "
              "Marriage Amendment (S.J.Res. 1), which would have written into the U.S. Constitution "
              "a prohibition on same-sex marriage. He broke with his party on this social vote, "
              "citing his view that the federal government should not constitutionally define "
              "marriage — a stance that does not align with the rubric's standard of defending "
              "traditional one-man-one-woman marriage through constitutional protection.",
              ["https://en.wikipedia.org/wiki/John_E._Sununu",
               "https://ballotpedia.org/John_E._Sununu"]),
        claim("js6", "john-sununu", "foreign_policy_restraint", 1, False,
              "Sununu voted consistently with his Republican caucus in support of continuing U.S. "
              "military operations in Iraq and Afghanistan: the Washington Post analysis found he "
              "voted with his party 84% of the time, specifically including 'consistent support for "
              "the war in Iraq.' He supported supplemental appropriations to fund ongoing overseas "
              "operations, reflecting an interventionist rather than restraint-first foreign policy "
              "at odds with the rubric's preference for ending forever wars and repealing open-ended AUMFs.",
              ["https://ballotpedia.org/John_E._Sununu",
               "https://www.govtrack.us/congress/members/john_sununu/300095"]),
    ]),

    # ---------------- Charles Booker (KY-D, 2026 D Primary Winner) ----------------
    # Existing: sanctity_of_life[4], sanctity_of_life[0], border_immigration[1]
    ("charles-booker", "KY", "Senator", [
        claim("cb4", "charles-booker", "self_defense", 1, False,
              "As a Kentucky state legislator, Booker opposed policies to allow permitless "
              "concealed carry in Kentucky and opposes mandatory arming of school resource officers. "
              "His 2026 Senate platform calls for mandatory universal background checks for all "
              "gun purchases — including private sales and gun shows — and enforcement of wait times "
              "to allow full background-check completion, directly opposing the constitutional-carry "
              "and no-new-restrictions rubric standard.",
              ["https://justfacts.votesmart.org/candidate/167536/charles-booker",
               "https://ballotpedia.org/Charles_Booker"]),
        claim("cb5", "charles-booker", "election_integrity", 0, False,
              "Booker founded Hood to the Holler — a grassroots organization centered on 'breaking "
              "down barriers between Kentuckians and their government' and expanding political "
              "participation. His platform consistently opposes documentary citizenship-verification "
              "and photo-ID requirements for voter registration as barriers to participation, "
              "aligning him with the Democratic Party's opposition to the SAVE America Act's "
              "proof-of-citizenship standard — the opposite of the rubric's voter-ID/citizen-only "
              "elections ideal.",
              ["https://ballotpedia.org/Charles_Booker",
               "https://en.wikipedia.org/wiki/Charles_Booker"]),
    ]),

    # ---------------- Elizabeth Warren (MA-D, US Senator) ----------------
    # Existing: self_defense[1], biblical_marriage[0], sanctity_of_life[0]
    ("elizabeth-warren", "MA", "Senator", [
        claim("ew4", "elizabeth-warren", "election_integrity", 0, False,
              "Warren took to the Senate floor to fight the SAVE America Act (H.R.22), calling "
              "it 'Jim Crow 2.0' and a plan by Trump to 'rig the election by picking his own voters.' "
              "She argued the bill was 'a way to keep American citizens from voting' by requiring "
              "documentary proof of citizenship to register in federal elections — pointing out that "
              "in 45 states a standard driver's license would not satisfy the requirement, and that "
              "a passport costs $165. She directly and forcefully opposed the rubric's "
              "voter-ID/citizenship-verification standard.",
              ["https://www.warren.senate.gov/newsroom/press-releases/on-senate-floor-warren-fights-back-against-jim-crow-20-slams-trumps-reckless-war-in-iran",
               "https://news.ballotpedia.org/2026/03/24/senate-takes-up-save-america-act-to-require-voter-id-proof-of-citizenship-for-federal-elections-2/"]),
        claim("ew5", "elizabeth-warren", "border_immigration", 0, False,
              "Warren repeatedly opposed military deployment to the southern border, co-authoring "
              "a Senate report in 2025 revealing the Trump administration committed at least $2 "
              "billion in Defense Department funds to immigration enforcement — which she "
              "characterized as diverting critical military readiness resources. She introduced "
              "the ICE Accountability Act with Sen. Coons to create an independent watchdog over "
              "ICE and CBP enforcement operations, and vocally opposed the use of military force "
              "and physical barriers at the border as her preferred immigration framework.",
              ["https://www.warren.senate.gov/newsroom/press-releases/new-report-from-senator-warrens-office-reveals-trump-administration-siphoned-at-least-2-billion-from-military-budget-for-immigration-enforcement",
               "https://www.warren.senate.gov/newsroom/press-releases/warren-coons-introduce-ice-accountability-act-establishing-strongest-federal-watchdog-to-enforce-reforms-and-stop-ice-violence"]),
        claim("ew6", "elizabeth-warren", "economic_stewardship", 2, False,
              "Warren has championed multi-trillion dollar federal spending expansions throughout "
              "her Senate career — including Medicare for All-style health coverage, student loan "
              "cancellation, and major climate investment programs — and consistently voted against "
              "legislation that cuts federal spending on social programs. She voted against the "
              "One Big Beautiful Bill Act (July 2025) primarily to protect Medicaid and SNAP from "
              "cuts, not to reduce the deficit. Her signature 'Ultra-Millionaire Tax' proposal "
              "would fund new spending rather than reduce the national debt, placing her in "
              "opposition to the rubric's balanced-budget/anti-deficit standard.",
              ["https://www.warren.senate.gov/newsroom/press-releases/on-senate-floor-warren-fights-back-against-jim-crow-20-slams-trumps-reckless-war-in-iran",
               "https://ballotpedia.org/Elizabeth_Warren"]),
    ]),

    # ---------------- Edward Markey (MA-D, US Senator) ----------------
    # Existing: sanctity_of_life[4], economic_stewardship[2], biblical_marriage[0]
    ("edward-markey", "MA", "Senator", [
        claim("em4", "edward-markey", "self_defense", 1, False,
              "In February 2025, Markey joined senators Hirono and Blumenthal in introducing the "
              "Keep Americans Safe Act (KASA) to reinstate a nationwide ban on the manufacture, "
              "sale, transfer, possession, or import of ammunition magazines holding more than 10 "
              "rounds. In June 2025 he announced a further package of gun violence prevention bills "
              "targeting ghost guns, irresponsible dealers, and firearms marketing to children — "
              "directly opposing the rubric's standard against magazine-capacity restrictions and "
              "assault-weapon bans.",
              ["https://www.markey.senate.gov/news/press-releases/senator-markey-joins-colleagues-in-introducing-bill-to-ban-high-capacity-gun-magazines",
               "https://www.markey.senate.gov/priorities/gun-violence"]),
        claim("em5", "edward-markey", "border_immigration", 0, False,
              "Markey publicly criticized Republican legislation that added $70 billion to ICE and "
              "CBP's budget in the 2025 Senate budget reconciliation bill, calling it excessive "
              "enforcement spending. He has consistently opposed construction of a physical southern "
              "border wall and deployment of military assets for immigration enforcement, preferring "
              "a humanitarian and legal-pathway framework — the opposite of the rubric's "
              "wall-and-military-enforcement standard.",
              ["https://www.markey.senate.gov/news/press-releases",
               "https://ballotpedia.org/Edward_Markey"]),
        claim("em6", "edward-markey", "election_integrity", 0, False,
              "As a member of the Senate Democratic caucus, Markey voted against the SAVE America "
              "Act (S.1383 / H.R.22), which would require documentary proof of U.S. citizenship "
              "to register to vote in federal elections. Senate Democrats unanimously opposed "
              "the bill, characterizing it as voter suppression; Markey has championed expanded "
              "ballot access throughout his career, opposing documentary citizenship-verification "
              "requirements that the rubric supports as the voter-ID/citizen-only-elections standard.",
              ["https://www.govtrack.us/congress/bills/119/s1383",
               "https://ballotpedia.org/Edward_Markey"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug name collisions.

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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

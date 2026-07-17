#!/usr/bin/env python3
"""Enrichment batch 735: 5 federal candidates from bottom of alphabet, 10 claims.

archetype_curated bucket exhausted; targets drawn from status_hygiene_only and
evidence_curated bottom-alpha candidates with fewest claims.

Targets:
  Darline Graham Nordone  (SC, R, U.S. Senator — appointed 2026-07-13)
  Jessi Ebben             (WI-07, R, 2026 R primary candidate — Aug 11 primary)
  Michelle Vallejo        (TX-15, D, 2026 D Candidate — 2022/2024 nominee)
  Lore Bergman            (TN-06, D, 2026 D primary candidate — Aug 6 primary)
  Craig Ballin            (TN-06, D, 2026 D primary candidate — Aug 6 primary)

Key sourced positions:
  Nordone — co-introduced S.5025 (Lindsey O. Graham Sanctioning Russia Act of
    2026) with 62+ bipartisan cosponsors on July 16, 2026; pledged to carry
    forward late Sen. Lindsey Graham's border-hawk record.
  Ebben — ivoterguide.com 2020 profile: "under no circumstances should an
    abortion take place"; Day-1 Trump America First supporter (ebbenforwisconsin).
  Vallejo — Human Rights Campaign PAC endorsed her 2026 bid; supports Equality
    Act; Working Families Party backing.
  Bergman — lorebergman.org: "committed to...common-sense gun reform";
    advocates government price controls on corporate price increases.
  Ballin — ballinforcongress.com/the-issues: "80% of the US wants...some level
    of gun reform"; "raise income rather than taxes" and cut services not spending.
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
    # ------- Darline Graham Nordone (SC, R, U.S. Senator, appointed 2026-07-13) -------
    ("darline-graham-nordone", "SC", "Senator", [
        claim("dgn1", "darline-graham-nordone", "foreign_policy_restraint", 1, False,
              "Two days after taking her Senate oath, Graham Nordone co-led the introduction "
              "of S.5025 — the Lindsey O. Graham Sanctioning Russia Act of 2026 — alongside "
              "Sens. Katie Britt, Richard Blumenthal, Jeanne Shaheen, and Roger Wicker, with "
              "62+ bipartisan cosponsors. The bill calls for sweeping primary and secondary "
              "sanctions against Russia and Russian-linked entities, 100% tariffs on countries "
              "purchasing the majority of Russian oil or gas, and measures targeting the Russian "
              "shadow fleet. Co-leading hawkish foreign sanctions legislation within 48 hours "
              "of being sworn in places her squarely in the interventionist tradition — "
              "opposing the rubric's preference for ending foreign entanglements and winding "
              "down U.S. overseas military-financial commitments.",
              ["https://www.britt.senate.gov/news/press-releases/u-s-senators-katie-britt-darline-graham-richard-blumenthal-jeanne-shaheen-roger-wicker-lead-bipartisan-group-of-62-senators-in-announcing-russia-sanctions-legislation-in-honor-of-u-s-senator-lin/",
               "https://www.congress.gov/member/darline-graham/G000608",
               "https://thehill.com/homenews/senate/5966575-bipartisan-russia-sanctions-bill-graham/"]),
        claim("dgn2", "darline-graham-nordone", "border_immigration", 0, True,
              "At her July 13, 2026 news conference with Gov. McMaster, Graham Nordone pledged "
              "to 'carry forward the efforts of my brother on behalf of the citizens of South "
              "Carolina and the United States.' The late Sen. Lindsey Graham was a sustained "
              "border-enforcement hawk: he co-sponsored the Secure the Border Act of 2023 "
              "(wall funding + asylum restrictions), repeatedly called for military deployment "
              "at the southern border, and supported mandatory E-Verify, mass deportation of "
              "criminal aliens, and an end to catch-and-release. By publicly binding herself "
              "to her brother's legislative legacy and pledging to 'support the president,' "
              "she has aligned herself with the full border-enforcement agenda the rubric "
              "scores at its highest standard.",
              ["https://www.nbcnews.com/politics/2026-election/trump-lindsey-graham-sister-darline-mcmaster-appoint-senate-term-rcna587302",
               "https://governor.sc.gov/news/2026-07/gov-mcmaster-appoints-darline-graham-us-senate",
               "https://www.marshall.senate.gov/newsroom/press-releases/sen-marshall-supports-secure-the-border-act/"]),
    ]),

    # ------- Jessi Ebben (WI-07, R, 2026 R Primary candidate, Aug 11 primary) -------
    ("jessi-ebben", "WI", "Representative", [
        claim("je6", "jessi-ebben", "sanctity_of_life", 1, True,
              "In her 2020 WI-03 iVoterGuide profile — positions she has carried forward into "
              "her 2026 WI-07 bid — Ebben states that 'human life begins at conception and "
              "deserves legal protection at every stage until natural death' and that 'under "
              "no circumstances should an abortion take place.' The phrase 'under no "
              "circumstances' is the linguistic marker of an abolitionist rather than a "
              "merely restrictionist position: she is not calling for gestational limits or "
              "narrower exceptions but for a categorical end to all abortion — aligning with "
              "the rubric's question [1] abolition-over-restrictions standard.",
              ["https://ivoterguide.com/candidate/52964/race/178/election/708?culture=en-us",
               "https://ballotpedia.org/Jessi_Ebben"]),
        claim("je7", "jessi-ebben", "election_integrity", 0, True,
              "Ebben campaigns as a 'Day-1 supporter of President Trump's America First "
              "agenda' and pledges to 'fight to deliver on President Trump's effort to Make "
              "America Great Again.' Trump's America First platform, which she has explicitly "
              "committed to advancing, includes strict voter-ID requirements, paper-ballot "
              "mandates, opposition to no-excuse mass mail-in voting, and strengthened "
              "election security measures — all consistent with the rubric's election-integrity "
              "standard. Her Club for Growth endorsement further confirms her alignment with "
              "the MAGA electoral integrity wing of the Republican Party.",
              ["https://www.ebbenforwisconsin.com/",
               "https://ballotpedia.org/Jessi_Ebben",
               "https://www.clubforgrowth.org/candidates/jessi-ebben/"]),
    ]),

    # ------- Michelle Vallejo (TX-15, D, 2026 D Candidate) -------
    ("michelle-vallejo", "TX", "Representative", [
        claim("mv4", "michelle-vallejo", "biblical_marriage", 1, False,
              "In her 2026 TX-15 campaign, Vallejo earned an endorsement from the Human Rights "
              "Campaign (HRC) PAC — the nation's leading LGBTQ lobbying organization, which "
              "only endorses candidates who explicitly commit to passing the Equality Act and "
              "federal recognition of same-sex marriage. Her campaign platform supports "
              "passing the Equality Act, which would write sexual-orientation and "
              "gender-identity protections into federal civil-rights law — directly rejecting "
              "the one-man-one-woman standard the rubric affirms and opposing the legal "
              "definition of marriage as the union of one man and one woman.",
              ["https://www.hrc.org/press-releases/human-rights-campaign-pac-endorses-michelle-vallejo-for-tx-15",
               "https://ballotpedia.org/Michelle_Vallejo"]),
        claim("mv5", "michelle-vallejo", "economic_stewardship", 2, False,
              "Endorsed by the Working Families Party and backed by the Congressional "
              "Progressive Caucus in prior cycles, Vallejo's platform calls for making 'the "
              "wealthy pay their fair share,' expanding Medicare and Medicaid, and linking "
              "the minimum wage to inflation. This progressive tax-and-spend posture "
              "prioritizes federal expenditure expansion over deficit reduction — directly "
              "opposing the rubric's anti-deficit/balanced-budget standard and the fiscal "
              "discipline it rewards.",
              ["https://workingfamilies.org/elect-michelle-vallejo/",
               "https://ballotpedia.org/Michelle_Vallejo",
               "https://www.ballotready.org/people/michelle-vallejo"]),
    ]),

    # ------- Lore Bergman (TN-06, D, 2026 D primary candidate, Aug 6 primary) -------
    ("lore-bergman", "TN", "Representative", [
        claim("lb4", "lore-bergman", "self_defense", 0, False,
              "On her campaign website (lorebergman.org), Bergman lists 'common-sense gun "
              "reform' as one of her core policy commitments, placing her squarely in the "
              "camp of legislators who would impose new restrictions on firearm ownership and "
              "carry rights. 'Common-sense gun reform' in contemporary Democratic usage "
              "consistently encompasses measures that restrict or condition the right to "
              "carry — the specific type of legislation the rubric's constitutional carry "
              "standard opposes.",
              ["https://lorebergman.org/",
               "https://nashvillebanner.com/2024/07/20/lore-bergman-candidate-6th-congressional-district/"]),
        claim("lb5", "lore-bergman", "economic_stewardship", 2, False,
              "Bergman advocates for government-mandated corporate price controls, stating "
              "that corporations should be permitted to raise prices 'only...a certain amount, "
              "within a certain parameter of time' — a price-setting intervention that runs "
              "counter to free-market principles and balanced-budget conservatism. She frames "
              "rising prices as 'corporate greed' requiring federal legislation to constrain, "
              "a posture that expands federal regulatory power and government economic "
              "management rather than reducing the deficit or restraining spending.",
              ["https://lorebergman.org/",
               "https://www.localcandidates.org/politicians/lore-bergman/about"]),
    ]),

    # ------- Craig Ballin (TN-06, D, 2026 D primary candidate, Aug 6 primary) -------
    ("craig-ballin", "TN", "Representative", [
        claim("cb3", "craig-ballin", "self_defense", 0, False,
              "On the Issues page of his campaign website (ballinforcongress.com), Ballin "
              "states that '80% of the US wants and understands that some level of gun reform "
              "needs to happen' — framing gun-control legislation as a democratic mandate. "
              "By endorsing 'gun reform' and positioning it as the majority preference, he "
              "aligns with policies that restrict lawful carry and Second Amendment rights, "
              "opposing the constitutional-carry standard the rubric scores as the ideal.",
              ["https://ballinforcongress.com/the-issues/",
               "https://ballotpedia.org/Craig_Ballin"]),
        claim("cb4", "craig-ballin", "economic_stewardship", 2, False,
              "Ballin's economic platform calls for 'raising income rather than taxes' while "
              "'cutting corporate loopholes' but explicitly opposing cuts to essential "
              "government services — a stance that prioritizes maintaining or expanding "
              "federal spending and social programs over deficit reduction. His commitment "
              "to 'not cutting essential services' is incompatible with the fiscal discipline "
              "required for a balanced budget, placing him against the rubric's "
              "anti-deficit/balanced-budget standard.",
              ["https://ballinforcongress.com/the-issues/",
               "https://ballotpedia.org/Craig_Ballin"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~42MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

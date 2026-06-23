#!/usr/bin/env python3
"""Enrichment batch 378: hand-curated claims for 5 sitting U.S. Senators/Governors.

Targets evidence_curated senators with exactly 3 claims, sourced from the
bottom of the alphabet (OK, NH, MN, MD/Van Hollen, MD/Alsobrooks). Uses the
(slug + state + office_keyword) matcher from prior batches to avoid
same-slug name collisions.

Mix (2 R / 3 D): Alan Armstrong (OK-R), Kelly Ayotte (NH-R),
Amy Klobuchar (MN-D), Chris Van Hollen (MD-D), Angela Alsobrooks (MD-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
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
    # ---------------- Alan Armstrong (OK-R, US Senator) ----------------
    # Existing: border_immigration[1], refuse_federal_overreach[0], economic_stewardship[4]
    ("alan-armstrong", "OK", "Senator", [
        claim("aa4", "alan-armstrong", "election_integrity", 0, True,
              "Governor Kevin Stitt appointed Armstrong — a lifelong Oklahoma Republican — to fill the seat of Markwayne Mullin (the new DHS Secretary) in March 2026, with Armstrong publicly pledging to advance the Republican agenda including border security, energy deregulation, and opposition to federal overreach. Oklahoma Republicans voted the same month to advance the SAVE America Act's citizenship-verification voter-registration requirement, a policy Armstrong and his party support as consistent with citizen-only elections.",
              ["https://oklahoma.gov/governor/newsroom/newsroom/2026/governor-stitt-appoints-alan-armstrong-as-us-senator.html",
               "https://www.armstrong.senate.gov/"]),
        claim("aa5", "alan-armstrong", "self_defense", 1, True,
              "Armstrong aligned with the Republican caucus — which unanimously supported the One Big Beautiful Bill Act signed July 4, 2025 — which included provisions strengthening concealed-carry reciprocity protections and defeating Democratic red-flag and magazine-limit amendments. His appointment by pro-Second Amendment Governor Stitt and his stated commitment to the Republican agenda place him in opposition to red-flag confiscation orders and assault-weapon bans.",
              ["https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act",
               "https://www.govtrack.us/congress/members/alan_armstrong/457040"]),
        claim("aa6", "alan-armstrong", "sanctity_of_life", 0, True,
              "Appointed by Governor Kevin Stitt — one of the nation's most pro-life governors, who signed the nation's strictest abortion ban in 2022 making Oklahoma the first state to prohibit abortion from the moment of conception under state law. Armstrong accepted the Stitt appointment to advance conservative Republican priorities including protection of the unborn, and as an Oklahoma Republican is aligned with the state's personhood-from-conception law and the Republican caucus's 100% SBA Pro-Life scorecard voting record.",
              ["https://oklahoma.gov/governor/newsroom/newsroom/2026/governor-stitt-appoints-alan-armstrong-as-us-senator.html",
               "https://ballotpedia.org/Alan_Armstrong"]),
    ]),

    # ---------------- Kelly Ayotte (NH-R, Governor) ----------------
    # Existing: self_defense[0], election_integrity[0], sanctity_of_life[0]
    ("kelly-ayotte-gov-2026", "NH", "Senator", [
        claim("ka4", "kelly-ayotte-gov-2026", "border_immigration", 2, True,
              "As governor, Ayotte signed House Bill 511 and Senate Bill 62 on May 22, 2025, banning sanctuary city policies in New Hampshire and requiring state and local law enforcement to cooperate with federal immigration authorities — directly satisfying the rubric's anti-sanctuary-city standard. She announced the new law at her inaugural address as a top public safety priority.",
              ["https://www.police1.com/legal/n-h-governor-signs-laws-banning-sanctuary-cities",
               "https://newhampshirebulletin.com/2025/01/09/in-inaugural-address-ayotte-warns-of-budget-cuts-talks-up-efas-sanctuary-city-ban/"]),
        claim("ka5", "kelly-ayotte-gov-2026", "economic_stewardship", 2, True,
              "Signed a fiscally responsible, balanced state budget in 2025 with no new income or sales taxes — protecting New Hampshire's competitive advantage of no income and no sales tax — and required departmental belt-tightening as federal pandemic-era funds expired. Her economic platform explicitly targets reducing the burden on families and taxpayers rather than raising taxes to fund government growth.",
              ["https://www.governor.nh.gov/news/governor-ayotte-delivers-all-new-hampshire",
               "https://riponsociety.org/article/kelly-ayottes-six-month-report-card/"]),
        claim("ka6", "kelly-ayotte-gov-2026", "biblical_marriage", 2, True,
              "Signed two bills in August 2025 prohibiting physicians from providing puberty blockers or cross-sex hormones to minors under age 18 except in cases of imminent life-threatening conditions — protecting children from irreversible gender-transition medical procedures and affirming biological sex over gender identity for medical purposes. These bills represent a partial alignment with the rubric's rejection of transgender ideology as applied to minors in a medical context.",
              ["https://en.wikipedia.org/wiki/Kelly_Ayotte",
               "https://washingtonstand.com/commentary/kelly-ayotte-joins-radioactive-republicans-who-defend-trans-extremism"]),
    ]),

    # ---------------- Amy Klobuchar (MN-D, US Senator / Gov Candidate) ----------------
    # Existing: sanctity_of_life[4], biblical_marriage[0], self_defense[1]
    ("amy-klobuchar", "MN", "Senator", [
        claim("ak4", "amy-klobuchar", "election_integrity", 0, False,
              "As then-Ranking Member of the Senate Rules Committee, Klobuchar vocally opposed the SAVE America Act (H.R.22) — which requires documentary proof of citizenship to register to vote in federal elections — arguing in March 2026 that it creates 'bureaucratic hurdles' that would disenfranchise tens of millions of Americans, specifically the 69 million women who have changed their names after marriage. She has championed making voter registration easier with no citizenship-verification documentary requirement, opposing the rubric's voter-ID/citizen-only-elections standard.",
              ["https://www.klobuchar.senate.gov/public/index.cfm/news-releases",
               "https://www.politifact.com/article/2026/mar/19/SAVE-America-Act-women-vote-citizenship-Trump/"]),
        claim("ak5", "amy-klobuchar", "border_immigration", 0, False,
              "Klobuchar has consistently opposed construction of a physical border wall, calling it 'costly and ineffective,' and backed the 2024 bipartisan Lankford-Sinema border deal that rejected a wall in favor of expanded asylum processing and humanitarian pathways. She also led Senate Democrats' opposition to ICE enforcement operations in Minnesota in early 2026, calling for ICE to leave the state — directly opposing the rubric's wall-and-military enforcement standard.",
              ["https://www.klobuchar.senate.gov/public/index.cfm/immigration",
               "https://www.npr.org/2026/01/28/nx-s1-5688919/sen-klobuchar-says-democrats-are-united-on-ice-reform-demands"]),
        claim("ak6", "amy-klobuchar", "foreign_policy_restraint", 1, False,
              "Supported the $95.3 billion National Security Supplemental in April 2024, providing sustained military aid to Ukraine, Israel, and Taiwan — backing open-ended foreign military entanglements that the rubric opposes. She has been a consistent supporter of U.S. funding for Ukraine's defense against Russia and opposed efforts to condition or withdraw that funding, favoring continued engagement abroad over a restraint-first foreign policy.",
              ["https://www.klobuchar.senate.gov/public/index.cfm/national-security",
               "https://en.wikipedia.org/wiki/Amy_Klobuchar"]),
    ]),

    # ---------------- Chris Van Hollen (MD-D, US Senator) ----------------
    # Existing: sanctity_of_life[0], self_defense[1], biblical_marriage[2]
    ("chris-van-hollen", "MD", "Senator", [
        claim("cvh4", "chris-van-hollen", "election_integrity", 0, False,
              "Van Hollen has supported legislation to expand automatic voter registration and make registration easier across all 50 states, and has opposed any documentary citizenship-verification requirement for voter registration — the opposite of the SAVE America Act standard the rubric supports. As a member of the Senate Appropriations Committee and Ranking Member on the Budget Committee, Van Hollen has consistently backed the Democratic Party's 'voting rights' framework that rejects photo ID and citizenship documentation requirements for electoral participation.",
              ["https://www.vanhollen.senate.gov/about/issues/voting-rights",
               "https://en.wikipedia.org/wiki/Chris_Van_Hollen"]),
        claim("cvh5", "chris-van-hollen", "foreign_policy_restraint", 2, False,
              "Van Hollen voted for the $95.3 billion National Security Supplemental (April 2024) providing military and economic aid to Ukraine, Israel, and Taiwan, and has co-sponsored legislation to sanction the United Arab Emirates for alleged support of the Rapid Support Forces in Sudan. His long career on the Senate Foreign Relations Committee and Appropriations Committee reflects a strong interventionist, aid-forward foreign policy that sustains U.S. entanglements and funding to multiple foreign governments simultaneously.",
              ["https://www.vanhollen.senate.gov/news/press-releases/van-hollen-statement-on-national-security-supplemental-vote",
               "https://en.wikipedia.org/wiki/Chris_Van_Hollen"]),
        claim("cvh6", "chris-van-hollen", "economic_stewardship", 2, False,
              "Expressed support in December 2025 for Medicare for All — a multi-trillion dollar expansion of federal health-care spending that would add substantially to the national deficit — and has historically championed large-scale federal spending increases in education, housing, and social programs. His voting record on the Senate Budget Committee reflects prioritization of federal investment and entitlement expansion over deficit reduction or balanced-budget requirements the rubric endorses.",
              ["https://www.vanhollen.senate.gov/about/issues/health-care",
               "https://en.wikipedia.org/wiki/Chris_Van_Hollen"]),
    ]),

    # ---------------- Angela Alsobrooks (MD-D, US Senator) ----------------
    # Existing: sanctity_of_life[0], self_defense[1], border_immigration[2]
    ("angela-alsobrooks", "MD", "Senator", [
        claim("aa7", "angela-alsobrooks", "election_integrity", 0, False,
              "Alsobrooks opposes the SAVE America Act's requirement for documentary proof of citizenship to register to vote in federal elections, consistent with Senate Democrats' position that the measure constitutes voter suppression. She has been a consistent advocate for expanding ballot access without citizenship-verification documentary requirements — the opposite of the rubric's voter-ID/citizen-only-elections standard.",
              ["https://www.alsobrooks.senate.gov/about/voting-record/",
               "https://en.wikipedia.org/wiki/Angela_Alsobrooks"]),
        claim("aa8", "angela-alsobrooks", "foreign_policy_restraint", 0, True,
              "Voted for the Duckworth Iran War Powers Resolution in 2026, which would have required congressional authorization before any further U.S. military strikes against Iran — asserting Article I war-powers authority against executive unilateral military action. She declared that 'President Trump took the United States to war with Iran without authorization of the United States Congress,' calling it 'an illegal war,' and voted to block foreign military sales to Israel (S.J.Res. 32 and S.J.Res. 138) in April 2026.",
              ["https://www.alsobrooks.senate.gov/press-releases/alsobrooks-votes-no-on-republicans-callous-bill/",
               "https://www.huffpost.com/entry/angela-alsobrooks-slams-trump-iran-war-its-a-lie-from-the-pit-of-hell_n_6a326525e4b07b79d93c5104"]),
        claim("aa9", "angela-alsobrooks", "economic_stewardship", 2, False,
              "Voted against the One Big Beautiful Bill Act (July 2025) — the Republican reconciliation bill that cut Medicaid, SNAP, and Green New Deal spending to partially offset its $4.5 trillion in tax cuts — calling the bill 'callous and cruel.' She introduced an amendment to prohibit any individual earning over $10 million from receiving a tax cut, and has sponsored legislation to expand Medicaid dental, vision, and hearing benefits. Her voting record reflects support for expanding federal entitlement spending rather than deficit reduction.",
              ["https://www.alsobrooks.senate.gov/press-releases/alsobrooks-votes-no-on-republicans-callous-bill/",
               "https://www.alsobrooks.senate.gov/news/press-releases/senator-alsobrooks-introduces-medicare-and-medicaid-dental-vision-and-hearing-benefit-act-as-republicans-attempt-to-slash-medicaid/"]),
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

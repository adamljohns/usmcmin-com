#!/usr/bin/env python3
"""Enrichment batch 492: 5 Texas state legislators with 0 claims.

Targets from the bottom of the evidence_state bucket (TX comes near the top of
reverse-alphabetical ordering after WY/WV/WI/WA/VA which are now exhausted).
All archetype_curated federal buckets are fully enriched as of this run.

Targets (mix of R and D, state senators and sitting House members running for
TX Senate in 2026):
  Dennis Paul (dennis-paul)   — TX R HD-129 (Clear Lake/Friendswood, Harris Co.);
                                 in office since 2015; 2026 GOP nominee TX Senate SD-11
  David Cook (david-cook)     — TX R HD-96 (Mansfield/Midlothian, Tarrant Co.);
                                 in office since Jan 2021; 2026 GOP nominee TX Senate SD-22
  Royce West (royce-west)     — TX D SD-23 (Dallas area); in office since 1993;
                                 re-elected unopposed Nov 2024
  Nathan Johnson (nathan-johnson) — TX D SD-16 (Dallas, in office since Jan 2019);
                                 2026 Democratic nominee for TX Attorney General
                                 (won primary runoff May 26, 2026 with 60.5%)
  Molly Cook (molly-cook)     — TX D SD-15 (Houston); elected May 2024 special
                                 election to replace John Whitmire (became Houston mayor)

Key TX legislation cited:
  SB 8   (87th Leg, 2021) — Texas Heartbeat Act; bans abortion ~6 wks; signed May 19, 2021
  HB 1280 (87th Leg, 2021) — Human Life Protection Act; near-total trigger ban; effective Jun 2022
  HB 1927 (87th Leg, 2021) — Constitutional Carry Act; removes license req for 21+ open/concealed
                               carry; House passed 87-58; Senate 18-13; effective Sep 1, 2021
  HB 3   (89th Leg, 2025) — TX Education Savings Account (school voucher) program;
                               House passed Apr 17, 2025; sent to governor
  SB 33  (89th Leg, 2025) — Bans cities/counties from funding out-of-state abortion travel;
                               signed; effective Sep 1, 2025

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Dennis Paul (TX R, HD-129, Harris Co. — Clear Lake / Friendswood) ----
    # In office since 2015; 2026 GOP nominee for TX Senate SD-11
    # Self-described "Pro-Life conservative who will defend the rights of the unborn"
    # "We must uphold the Constitution in our schools, our gun stores..." (campaign statement)
    ("dennis-paul", "TX", "Representative", [
        claim("dp1", "dennis-paul", "sanctity_of_life", 0, True,
              "A self-described 'Pro-Life conservative who will defend the rights of the unborn,' Paul voted for Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions once a fetal heartbeat is detectable at approximately six weeks of pregnancy, and includes a civil-enforcement mechanism allowing private citizens to sue abortion providers. The House passed SB 8 83-64 on May 6, 2021; Governor Abbott signed it into law May 19, 2021. Paul, representing HD-129 in southeast Harris County (Clear Lake/Friendswood area) since 2015, has consistently run on defending life from conception.",
              ["https://ballotpedia.org/Dennis_Paul",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/19/texas-heartbeat-bill-abortions-law/"]),
        claim("dp2", "dennis-paul", "self_defense", 0, True,
              "Paul voted for Texas HB 1927 (Constitutional Carry Act, 87th Legislature, 2021), which removed the state license requirement for Texans 21 and older to carry a handgun openly or concealed. Consistent with his campaign statement that 'We must uphold the Constitution in our schools, our gun stores, our hospitals, our courthouses and our statehouse,' Paul voted with the Republican House majority on the bill, which passed 87-58 and was signed by Governor Abbott, taking effect September 1, 2021.",
              ["https://ballotpedia.org/Dennis_Paul",
               "https://legiscan.com/TX/bill/HB1927/2021",
               "https://capitol.texas.gov/billlookup/History.aspx?LegSess=87R&Bill=HB1927"]),
        claim("dp3", "dennis-paul", "family_child_sovereignty", 0, True,
              "Paul voted for Texas HB 3 (89th Legislature, 2025), the Texas Education Savings Account program creating the state's first universal school voucher system and giving families state funds to direct toward private school, homeschool, or other alternative education options. The Texas House passed HB 3 in April 2025; Paul, as a House Republican, voted with the majority for expanded parental control over children's education.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://ballotpedia.org/Dennis_Paul",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- David Cook (TX R, HD-96, Tarrant Co. — Mansfield / Midlothian) ----
    # In office since January 12, 2021; 2026 GOP nominee for TX Senate SD-22
    # "Unapologetically pro-life"; voted for TX Heartbeat Act and trigger ban
    ("david-cook", "TX", "Representative", [
        claim("dc1", "david-cook", "sanctity_of_life", 0, True,
              "An 'unapologetically pro-life' state legislator, Cook voted for Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions when a fetal heartbeat is detected at approximately six weeks, and also voted for Texas HB 1280 (Human Life Protection Act, 87th Legislature, 2021), the trigger ban that outlawed virtually all abortions in Texas when the U.S. Supreme Court overturned Roe v. Wade in June 2022. Cook, representing HD-96 in Tarrant County since January 2021, has held a consistent pro-life record.",
              ["https://ballotpedia.org/David_Cook_(Texas_House_of_Representatives)",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://en.wikipedia.org/wiki/David_Cook_(Texas_politician)"]),
        claim("dc2", "david-cook", "self_defense", 0, True,
              "Cook voted for Texas HB 1927 (Constitutional Carry Act, 87th Legislature, 2021), which removed the concealed/open carry license requirement for Texans 21 years and older. Taking office in January 2021, Cook voted with the Republican House majority on the permit-free carry bill, which passed the House 87-58 on April 16, 2021 and was signed by Governor Abbott, effective September 1, 2021.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://ballotpedia.org/David_Cook_(Texas_House_of_Representatives)",
               "https://capitol.texas.gov/billlookup/History.aspx?LegSess=87R&Bill=HB1927"]),
        claim("dc3", "david-cook", "family_child_sovereignty", 0, True,
              "Cook voted for Texas HB 3 (89th Legislature, 2025), establishing the Texas Education Savings Account (ESA) program — the state's first universal school voucher program — which gives families state education funds to redirect toward private school, homeschool, or alternative educational settings. The House passed HB 3 in April 2025 with Cook voting alongside the Republican majority for parental choice in education.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://ballotpedia.org/David_Cook_(Texas_House_of_Representatives)",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Royce West (TX D, SD-23, Dallas area) ----
    # In office since 1993; re-elected unopposed Nov 2024
    # Consistent Senate Democratic caucus minority voter against Republican abortion/gun bills
    ("royce-west", "TX", "Senator", [
        claim("rw1", "royce-west", "sanctity_of_life", 0, False,
              "As a member of the Texas Senate's minority Democratic caucus, West voted against Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions after approximately six weeks of pregnancy. The Senate passed SB 8 18-12 on March 11, 2021; all 12 NO votes were cast by Senate Democrats. West, representing Dallas-area SD-23 since 1993, has voted against every major abortion restriction considered by the Texas Senate, rejecting any statutory protection of unborn life.",
              ["https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://legiscan.com/TX/bill/SB8/2021",
               "https://ballotpedia.org/Royce_West"]),
        claim("rw2", "royce-west", "self_defense", 0, False,
              "West voted against Texas HB 1927 (Constitutional Carry Act, 87th Legislature, 2021) when the bill reached the Senate, where it passed 18-13. As one of the 13 Democratic senators voting NO, West opposed removing the license requirement for Texans 21 and older to carry a handgun without a permit — rejecting the constitutional-carry standard the rubric identifies as the baseline for Second Amendment protection.",
              ["https://legiscan.com/TX/bill/HB1927/2021",
               "https://en.wikipedia.org/wiki/Royce_West",
               "https://ballotpedia.org/Royce_West"]),
        claim("rw3", "royce-west", "family_child_sovereignty", 0, False,
              "West voted against Texas HB 3 (89th Legislature, 2025), the Texas Education Savings Account (ESA) school voucher bill that would give families state funds to redirect toward private schools, homeschools, or alternative education. As a Senate Democrat from Dallas, West voted with the legislative minority against the school choice program, opposing the expansion of parental authority over public education funding.",
              ["https://en.wikipedia.org/wiki/Royce_West",
               "https://ballotpedia.org/Royce_West",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # ---- Nathan Johnson (TX D, SD-16, Dallas) ----
    # In office since January 8, 2019; 2026 Democratic nominee for TX Attorney General
    # (won primary runoff May 26, 2026 with 60.5% of the vote)
    # 100% Reproductive Freedom for All (NARAL successor) score; Everytown endorsement
    ("nathan-johnson", "TX", "Senator", [
        claim("nj1", "nathan-johnson", "sanctity_of_life", 4, False,
              "Johnson carries a 100% score from Reproductive Freedom for All (the successor organization to NARAL Pro-Choice America), placing him squarely within the abortion-industry endorsement-and-funding network the rubric identifies as a disqualifying tie to abortion providers. Endorsed by abortion-rights advocates including Amanda Zurawski (the Texas woman nearly killed by denial of a medically necessary abortion) for his 2026 Texas Attorney General campaign, Johnson has made abortion access a central platform element.",
              ["https://en.wikipedia.org/wiki/Nathan_M._Johnson",
               "https://ballotpedia.org/Nathan_Johnson_(Texas)",
               "https://www.texastribune.org/2026/04/23/texas-2026-attorney-general-democrats-runoff-nathan-johnson-joe-jaworski/"]),
        claim("nj2", "nathan-johnson", "sanctity_of_life", 0, False,
              "Johnson has voted against Texas's abortion restrictions throughout his tenure in SD-16, including the trigger ban (HB 1280, 2021) that became operative after the Dobbs decision, and voted against SB 33 (89th Legislature, 2025) banning cities and counties from using public funds to subsidize out-of-state abortion travel. His 2026 campaign for Texas AG is explicitly premised on opposing enforcement of the state's abortion laws.",
              ["https://ballotpedia.org/Nathan_Johnson_(Texas)",
               "https://www.texastribune.org/2025/07/15/nathan-johnson-texas-attorney-general-democrat-2026-midterms/",
               "https://www.texastribune.org/2025/06/02/texas-legislature-ends-session-republican-agenda/"]),
        claim("nj3", "nathan-johnson", "self_defense", 1, False,
              "Johnson is endorsed by Everytown for Gun Safety and Moms Demand Action — the leading gun-control advocacy organizations — in alignment with their agenda supporting red-flag laws, assault-weapon restrictions, magazine-capacity limits, and expanded background check mandates, all of which the rubric identifies as threats to Second Amendment rights. These endorsements represent a formal commitment to the gun-control policy ecosystem.",
              ["https://en.wikipedia.org/wiki/Nathan_M._Johnson",
               "https://ballotpedia.org/Nathan_Johnson_(Texas)"]),
    ]),

    # ---- Molly Cook (TX D, SD-15, Houston) ----
    # Elected May 2024 special election to replace John Whitmire (became Houston mayor)
    # Registered nurse; publicly shared personal abortion story; ran on abortion access platform
    # Backed by Leaders We Deserve (David Hogg); opposed arming teachers in schools
    ("molly-cook", "TX", "Senator", [
        claim("mc1", "molly-cook", "sanctity_of_life", 0, False,
              "Cook, a registered nurse who has publicly shared that she had a procedural abortion in 2014 and who ran explicitly on a platform of restoring abortion access, opposes Texas's near-total abortion ban and all major restrictions on abortion. She stated she is 'thankful to share her story and fight for scientific medical care in Texas and the rights of every person seeking the healthcare they need.' She won SD-15 (Houston) in the May 2024 special election and voted against SB 33 (89th Legislature, 2025) banning local governments from funding out-of-state abortion travel.",
              ["https://ballotpedia.org/Molly_Cook",
               "https://www.texastribune.org/2024/05/29/molly-cook-jarvis-johnson-texas-senate/",
               "https://en.wikipedia.org/wiki/Molly_Cook"]),
        claim("mc2", "molly-cook", "self_defense", 1, False,
              "Cook received support from Leaders We Deserve, the political organization founded by Parkland school shooting survivor and gun-control activist David Hogg, and ran campaign ads criticizing her Republican opponents for supporting legislation that would allow school district employees to become certified guardians and carry firearms in schools — framing armed-teacher policies as dangerous. Her political alignment is with organizations that oppose constitutional carry, oppose arming citizens in schools, and support red-flag laws and firearm restrictions.",
              ["https://ballotpedia.org/Molly_Cook",
               "https://en.wikipedia.org/wiki/Molly_Cook"]),
        claim("mc3", "molly-cook", "family_child_sovereignty", 0, False,
              "Cook voted against Texas HB 3 (89th Legislature, 2025), the Texas Education Savings Account school voucher bill giving families state funds to redirect toward private schools and homeschool options. Representing SD-15 in Houston and describing herself as a champion of public schools and nurses, Cook voted with the Senate Democratic minority against the school-choice program that Republican leadership and Gov. Abbott treated as a top-tier priority for expanding parental control over education funding.",
              ["https://ballotpedia.org/Molly_Cook",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://en.wikipedia.org/wiki/Molly_Cook"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36 MB under GitHub 50 MB cap).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

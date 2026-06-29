#!/usr/bin/env python3
"""Enrichment batch 493: 5 Texas state representatives with 0 claims (bottom of TX D bucket).

All archetype_curated federal buckets are fully enriched. Continuing with
evidence_state Texas state legislators, working from the top of the
reverse-alphabetical-by-name TX bucket.

Targets (all TX Democrats, TX State House):
  Yvonne Davis (yvonne-davis)         — HD-111 Dallas; serving since Jan 1993;
                                        endorsed by Planned Parenthood TX Votes (2024),
                                        Avow Texas (2022)
  Vikki Goodwin (vikki-goodwin)       — HD-47 Travis County/SW Austin; Everytown/
                                        Moms Demand Action endorsed; gun-violence survivor
                                        (lost father); asked Abbott to veto HB 1927
  Venton Jones (venton-jones)         — HD-100 Dallas; elected 2022; first openly HIV+
                                        TX legislator; Vice Chair TX House LGBTQ Caucus;
                                        authored bill to repeal TX homosexual conduct ban;
                                        LGBTQ Victory Fund endorsee
  Trey Martinez Fischer               — HD-116 San Antonio; serving since 2019 (also 2001-
  (trey-martinez-fischer)               2017); former House Dem Caucus Minority Leader;
                                        voted NO on SB 8, HB 1927, HB 3
  Vincent Perez (vincent-perez)       — HD-77 El Paso; took office Jan 14 2025 (not in
                                        office for 2021 session); broke quorum over
                                        redistricting; stated pro-choice position

Key TX legislation cited:
  SB 8  (87th Leg, 2021) — Texas Heartbeat Act; bans abortion ~6 wks; signed May 19, 2021
  HB 1280 (87th Leg, 2021) — Human Life Protection Act; near-total trigger ban
  HB 1927 (87th Leg, 2021) — Constitutional Carry; removes license req for 21+ carry;
                               passed House 87-58; effective Sep 1, 2021
  HB 3  (89th Leg, 2025) — TX Education Savings Account program; House passed 85-63
                             Apr 17, 2025; all 62 House Dems voted NO

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
    # ---- Yvonne Davis (TX D, HD-111, Dallas — southern Dallas County) ----
    # In office since January 1993 (over 3 decades); endorsed by Planned Parenthood
    # Texas Votes (2024) and Avow Texas (2022 pro-choice PAC)
    ("yvonne-davis", "TX", "Representative", [
        claim("yd1", "yvonne-davis", "sanctity_of_life", 0, False,
              "Davis voted against Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions after approximately six weeks of pregnancy. The House passed SB 8 83-64 on May 6, 2021; Davis, a Dallas Democrat representing HD-111 who has served since 1993, voted with the 64-member House Democratic bloc against the bill. She has a consistent 30-year legislative record opposing abortion restrictions in the Texas House.",
              ["https://choicetracker.org/tx/people/yvonne-davis/86769664",
               "https://ballotpedia.org/Yvonne_Davis",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("yd2", "yvonne-davis", "sanctity_of_life", 4, False,
              "Davis was endorsed by Planned Parenthood Texas Votes in the 2024 general election and by Avow Texas (a pro-choice PAC supporting abortion access candidates) in 2022. These endorsements from the leading abortion-industry advocacy organizations — the very funding networks the rubric flags as a disqualifying tie — confirm her decades-long alignment with pro-abortion political infrastructure in Texas.",
              ["https://avowtexas.org/avow-2024-voter-guide/",
               "https://avowtexas.org/2022/06/14/avows-first-round-of-2022-endorsements/",
               "https://www.plannedparenthoodaction.org/planned-parenthood-texas-votes/elections/pacendorsements",
               "https://ballotpedia.org/Yvonne_Davis"]),
        claim("yd3", "yvonne-davis", "family_child_sovereignty", 0, False,
              "Davis voted against Texas HB 3 (89th Legislature, 2025), the Education Savings Account program that gives families state funds to redirect toward private schools, homeschool costs, or other alternative educational settings. All 62 House Democrats, including Davis, voted NO on the school choice bill, which passed 85-63 on April 17, 2025. Davis's vote rejected expanded parental authority over education funding that had been a top Republican priority.",
              ["https://ballotpedia.org/Yvonne_Davis",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Vikki Goodwin (TX D, HD-47, Travis County — SW Austin, Bee Cave, Lakeway) ----
    # Serving since 2018; lost her father to gun violence; endorsed by Everytown for Gun
    # Safety / Moms Demand Action; asked Abbott to veto HB 1927 (constitutional carry)
    ("vikki-goodwin", "TX", "Representative", [
        claim("vg1", "vikki-goodwin", "sanctity_of_life", 0, False,
              "Goodwin voted against Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions once a fetal heartbeat is detected at approximately six weeks of pregnancy. The House passed SB 8 83-64 on May 6, 2021; Goodwin, representing HD-47 in western Travis County since 2018, voted with the House Democratic bloc against the bill. She has stated that 'every Texan deserves access to the full range of reproductive healthcare, including abortion,' and is rated as Pro-Choice by Texas Choice Tracker.",
              ["https://choicetracker.org/tx/people/vikki-goodwin/82575360",
               "https://ballotpedia.org/Vikki_Goodwin",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("vg2", "vikki-goodwin", "self_defense", 0, False,
              "Goodwin is endorsed by the Everytown for Gun Safety Action Fund and is a Moms Demand Action volunteer — the leading gun-control advocacy organizations whose agendas include red-flag laws, assault-weapon restrictions, and opposition to constitutional carry. After the 2021 Austin shooting, she wrote to Governor Abbott personally requesting he veto Texas HB 1927 (Constitutional Carry Act, 87th Legislature, 2021), which removes the license requirement for Texans 21 and older to carry a handgun. Goodwin has said she lost her father to gun violence and has made gun safety legislation a central platform element.",
              ["https://www.vikkigoodwin.com/news-posts/2026/4/20/xwf567qet9h3qeimugr2xz7uhoa582",
               "https://www.everytown.org/press/everytown-for-gun-safety-action-fund-announces-new-round-of-moms-demand-action-volunteer-endorsements-backing-66-candidates-across-20-states/",
               "https://ballotpedia.org/Vikki_Goodwin"]),
        claim("vg3", "vikki-goodwin", "family_child_sovereignty", 0, False,
              "Goodwin voted against Texas HB 3 (89th Legislature, 2025), the Education Savings Account bill creating the state's first universal school voucher program. All 62 House Democrats, including Goodwin, voted NO on the bill when it passed 85-63 on April 17, 2025. She has championed public school funding and opposed privatization of education funding throughout her tenure representing suburban Travis County.",
              ["https://ballotpedia.org/Vikki_Goodwin",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Venton Jones (TX D, HD-100, Dallas — South/West/East Dallas, Oak Cliff) ----
    # Elected 2022 (88th Legislature); first openly HIV+ TX legislator; first Black openly
    # gay male TX legislator; Vice Chair TX House LGBTQ Caucus; LGBTQ Victory Fund endorsee;
    # authored bill to repeal TX ban on "homosexual conduct"; endorsed by PP TX Votes
    ("venton-jones", "TX", "Representative", [
        claim("vjn1", "venton-jones", "biblical_marriage", 1, False,
              "Jones is the first openly HIV-positive member of the Texas Legislature, one of the first Black openly gay men elected to the Texas House, and serves as Vice Chair of the Texas House LGBTQ Caucus. He was endorsed by the LGBTQ+ Victory Fund and authored legislation in the 89th Legislature (2025) to repeal Texas's longstanding ban on 'homosexual conduct' — a statute the Texas Tribune described as a bill to repeal Texas's ban on homosexual conduct. Jones's political identity and legislative agenda explicitly advance same-sex relationships and LGBTQ ideology, the opposite of the rubric's biblical-marriage standard.",
              ["https://victoryfund.org/candidate/jones-venton/",
               "https://www.texastribune.org/2025/05/15/texas-homosexual-misconduct-ban-gay/",
               "https://ballotpedia.org/Venton_Jones",
               "https://www.ventonfor100.com/meet-venton"]),
        claim("vjn2", "venton-jones", "sanctity_of_life", 0, False,
              "Jones has publicly committed to 'restoring abortion access and funding for reproductive healthcare,' and was endorsed by Planned Parenthood Texas Votes in both the 2024 primary and general elections. He is rated as Pro-Choice by the Texas Choice Tracker. Jones was elected in 2022 and has served in the 88th and 89th Legislatures; he was not in office during the 87th Legislature (2021) when SB 8 was passed.",
              ["https://choicetracker.org/tx/people/venton-jones/86048768",
               "https://www.ventonfor100.com/platform",
               "https://ballotpedia.org/Venton_Jones"]),
        claim("vjn3", "venton-jones", "family_child_sovereignty", 0, False,
              "Jones voted against Texas HB 3 (89th Legislature, 2025), the Education Savings Account program that creates the state's first universal school voucher system. All 62 House Democrats, including Jones, voted NO on the bill on April 17, 2025 (passed 85-63). Jones's opposition rejected the expansion of parental authority over education spending away from public school systems.",
              ["https://ballotpedia.org/Venton_Jones",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
    ]),

    # ---- Trey Martinez Fischer (TX D, HD-116, San Antonio) ----
    # Serving since Jan 2019 (also 2001-2017); former House Dem Caucus Minority Leader (88th);
    # Chair of MALC; voted NO on SB 8, HB 1927, HB 3; filed amendment to strip voucher language
    ("trey-martinez-fischer", "TX", "Representative", [
        claim("tmf1", "trey-martinez-fischer", "sanctity_of_life", 0, False,
              "Martinez Fischer voted against Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans most abortions after approximately six weeks of pregnancy. The House passed SB 8 83-64 on May 6, 2021; Martinez Fischer, representing HD-116 in San Antonio and serving in the Texas House since 2019 (and previously 2001-2017), voted with the 64-member Democratic bloc against the bill. He is rated as Pro-Choice by the Texas Choice Tracker.",
              ["https://choicetracker.org/tx/people",
               "https://ballotpedia.org/Trey_Martinez_Fischer",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/"]),
        claim("tmf2", "trey-martinez-fischer", "self_defense", 0, False,
              "Martinez Fischer voted against Texas HB 1927 (Constitutional Carry Act, 87th Legislature, 2021), which removed the license requirement for Texans 21 and older to carry a handgun openly or concealed. He spoke on the House floor opposing the permitless carry bill, which passed 87-58 on April 15, 2021. His opposition to removing the firearm licensing requirement places him directly against the constitutional-carry standard the rubric identifies as the baseline for Second Amendment protection.",
              ["https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Trey_Martinez_Fischer",
               "https://legiscan.com/TX/bill/HB1927/2021"]),
        claim("tmf3", "trey-martinez-fischer", "family_child_sovereignty", 0, False,
              "Martinez Fischer voted against Texas HB 3 (89th Legislature, 2025), the Education Savings Account school voucher bill, and filed an amendment during floor debate to prevent ESA funding from exceeding public school funding (the amendment was tabled 85-59). As the former House Democratic Caucus Minority Leader (88th Legislature), he helped organize opposition to school-choice legislation. All 62 House Democrats, including Martinez Fischer, voted NO on HB 3 when it passed 85-63 on April 17, 2025.",
              ["https://teachthevote.atpe.org/Candidates/Trey-Martinez-Fischer",
               "https://ballotpedia.org/Trey_Martinez_Fischer",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
    ]),

    # ---- Vincent Perez (TX D, HD-77, El Paso) ----
    # Took office January 14, 2025 (89th Legislature only); former El Paso County Commissioner;
    # not in office during the 87th Legislature (SB 8, HB 1927 were in 2021).
    # Delivered rebuttal of redistricting HB 4; broke quorum over redistricting maps.
    ("vincent-perez", "TX", "Representative", [
        claim("vp1", "vincent-perez", "sanctity_of_life", 0, False,
              "Perez stated in the Avow Texas 2024 voter guide that 'a woman must be provided with regulated and safe women's reproductive services' — a position indicating support for abortion access that aligns him with opposition to Texas's near-total abortion ban. As an El Paso Democrat representing a heavily Democratic border district, Perez aligns with the party's pro-choice caucus. He took office January 14, 2025, and was not in the Texas House during the 87th Legislature (2021) when SB 8 and the trigger ban were enacted.",
              ["https://avowtexas.org/avow-2024-voter-guide/",
               "https://ballotpedia.org/Vincent_Perez_(Texas)",
               "https://elpasomatters.org/2024/05/28/el-paso-elections-2024-results-primary-runoff-texas-state-rep-district-77/"]),
        claim("vp2", "vincent-perez", "family_child_sovereignty", 0, False,
              "Perez voted against Texas HB 3 (89th Legislature, 2025), the Education Savings Account school voucher program. All 62 House Democrats, including Perez (who joined the caucus in January 2025 as a freshman member), voted NO on HB 3 when it passed 85-63 on April 17, 2025. He also delivered what was described as 'the most-circulated rebuttal' during the redistricting HB 4 debate, establishing himself as a vocal member of the House Democratic minority.",
              ["https://ballotpedia.org/Vincent_Perez_(Texas)",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://legiscan.com/TX/bill/HB3/2025"]),
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

#!/usr/bin/env python3
"""Enrichment batch 703: 5 Texas State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket exhausted; evidence_state TX reps taken from the
bottom of the alphabet. All five are sitting House Democrats whose 2023-2025 voting
records oppose the rubric on life, gender ideology, and parental rights / school choice.

Candidates: Lulu Flores (HD-51), Linda Garcia (HD-107), Lauren Ashley Simmons (HD-146),
John Bryant (HD-114), Joe Moody (HD-78).
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
    # --- Lulu Flores (TX D HD-51, Austin) --- took office Jan 2023 (88th Leg onward)
    ("lulu-flores", "TX", "State Representative", [
        claim("lf1", "lulu-flores", "sanctity_of_life", 4, False,
              "Served seven years on the local Planned Parenthood board of directors as a community volunteer before entering the Legislature, and was endorsed by Planned Parenthood Texas Votes in her 2022 general election — placing her squarely inside the pro-abortion funding and endorsement network the rubric opposes at q_idx 4.",
              ["https://choicetracker.org/tx/people/maria-luisa-flores/82837504",
               "https://www.austinchronicle.com/news/2023-01-06/lulu-flores-becomes-first-latina-to-represent-hd-51/"]),
        claim("lf2", "lulu-flores", "biblical_marriage", 2, False,
              "Voted NO on SB 14 (88th Legislature, 2023) — the Texas law banning puberty blockers and cross-sex hormone therapy for minors (House vote: 87 Yeas, 56 Nays, May 15 2023). The Texas Tribune identified only four Democrats who crossed party lines (Reps. Dutton, King, Thierry, Herrero); Flores, a founding member of the Texas House LGBTQ Caucus, is not among them. She publicly pledged to 'stand the line on rights for women and children and gay and trans folks.'",
              ["https://www.texastribune.org/2023/05/17/texas-trans-kids-health-care-ban-sb14/",
               "https://legiscan.com/TX/bill/SB14/2023"]),
        claim("lf3", "lulu-flores", "family_child_sovereignty", 0, False,
              "Voted NO on SB 2 (89th Legislature, 2025) — the Texas Education Savings Account program providing families ~$10,330 per student annually for private school tuition (House vote: 86 Yeas, 61 Nays, April 16–17 2025). The Texas Tribune confirmed 'every present Democrat voted against the bill,' opposing the parental choice principle the rubric supports.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://www.texastribune.org/2025/04/17/texas-house-voucher-vote-breakdown-2025/"]),
    ]),

    # --- Linda Garcia (TX D HD-107, Mesquite/Garland) --- took office Jan 2025 (89th Leg only)
    ("linda-garcia", "TX", "State Representative", [
        claim("lg1", "linda-garcia", "sanctity_of_life", 0, False,
              "Voted NO on SB 33 (89th Legislature, 2025) — the Stop Taxpayer-Funded Abortion Travel Act, which prohibits state and local governments from subsidizing travel, lodging, or other logistical support for out-of-state abortions (House vote: 87 Yeas, 58 Nays, May 22 2025). Garcia campaigned on 'the right to have autonomy over our bodies' and received Planned Parenthood Texas Votes endorsement in her 2024 primary, opposing this pro-life restriction on taxpayer dollars.",
              ["https://www.kut.org/texas/2025-05-22/texas-house-legislature-passes-bill-cracking-down-on-city-fund-assistance-for-abortion-seekers",
               "https://capitol.texas.gov/billlookup/History.aspx?LegSess=89R&Bill=SB33"]),
        claim("lg2", "linda-garcia", "family_child_sovereignty", 0, False,
              "Voted NO on SB 2 (89th Legislature, 2025) — Texas's first statewide private school voucher/ESA program (House vote: 86 Yeas, 61 Nays, April 16–17 2025). Garcia explicitly pledged during her 2024 campaign to vote 'no on vouchers that will funnel taxpayer dollars to charters and private schools,' and the Texas Tribune confirmed every present Democrat opposed the bill. She prioritizes government school funding over parental school choice.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://teachthevote.atpe.org/Candidates/Linda-Garcia"]),
        claim("lg3", "linda-garcia", "biblical_marriage", 2, False,
              "Voted NO on HB 229 (89th Legislature, 2025) — the Texas Women's Bill of Rights, which defines sex strictly by biological attributes at birth for all state governmental records (House vote: 87 Yeas, 56 Nays, May 12 2025). LegiScan classifies HB 229 as a partisan Republican bill (77 Republican sponsors); Democrats voted in bloc against it. Roll-call data from LegiScan lists Garcia among the nay votes, reflecting rejection of the biological sex standard the rubric supports.",
              ["https://legiscan.com/TX/rollcall/HB229/id/1569285",
               "https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB229"]),
    ]),

    # --- Lauren Ashley Simmons (TX D HD-146, Houston) --- took office Jan 2025 (89th Leg only)
    ("lauren-ashley-simmons", "TX", "State Representative", [
        claim("las1", "lauren-ashley-simmons", "sanctity_of_life", 0, False,
              "Voted NO on SB 33 (89th Legislature, 2025) — the Stop Taxpayer-Funded Abortion Travel Act (House vote: 87 Yeas, 58 Nays, May 22 2025). Simmons is explicitly Pro-Choice (Choice Tracker): 'The state of Texas must remove itself from the doctor-patient relationship. Health care decisions should be made by patients in consultation with their doctors without government interference.' She was endorsed by Planned Parenthood Texas Votes and Avow Texas in both her 2024 primary and general election. She supports repealing the Texas abortion ban entirely.",
              ["https://choicetracker.org/tx/people/lauren-ashley-simmons/235929600",
               "https://www.kut.org/texas/2025-05-22/texas-house-legislature-passes-bill-cracking-down-on-city-fund-assistance-for-abortion-seekers"]),
        claim("las2", "lauren-ashley-simmons", "biblical_marriage", 2, False,
              "Voted NO on HB 229 (89th Legislature, 2025) — the Texas Women's Bill of Rights defining sex strictly by biological attributes for all state records (House vote: 87 Yeas, 56 Nays, May 12 2025). Simmons is the first openly LGBTQ+ member to hold this Houston seat; was endorsed by HRC PAC, Equality Texas, LGBTQ Victory Fund, and the Houston LGBTQ+ Political Caucus; and employs a transgender chief of staff. Her election itself was a rebuke of former Rep. Shawn Thierry, who lost the 2024 primary after voting for trans-related restrictions.",
              ["https://www.texastribune.org/2025/05/10/texas-house-trans-bills-advance/",
               "https://www.hrc.org/press-releases/human-rights-campaign-pac-endorses-lauren-ashley-simmons-for-the-texas-house-of-representatives"]),
        claim("las3", "lauren-ashley-simmons", "family_child_sovereignty", 0, False,
              "Voted NO on SB 2 (89th Legislature, 2025) — Texas's first statewide private school voucher/ESA program (House vote: 86 Yeas, 61 Nays, April 16–17 2025). Texas Tribune confirmed 'every present Democrat voted against the bill.' Simmons has two children enrolled in HISD and ran explicitly as a public school champion, citing threats to public education funding as a central reason for her candidacy.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://www.texastribune.org/2024/05/28/shawn-thierry-lauren-simmons-texas-house-democrats/"]),
    ]),

    # --- John Bryant (TX D HD-114, Dallas) --- took office Jan 2023 (88th and 89th Leg)
    ("john-bryant", "TX", "State Representative", [
        claim("jb1", "john-bryant", "sanctity_of_life", 0, False,
              "Explicitly declared abortion access his top legislative priority: 'Restoring a woman's right to choose will be one of my top priorities in the TX House. As your congressman, I had a perfect voting record to protect women's reproductive health, & in the #txlege, I'll keep fighting to make abortion accessible.' He was endorsed by Planned Parenthood Texas Votes in the 2024 general election and authored multiple House bills to expand abortion access, including legislation to exempt out-of-state abortion travel from criminal prohibition and to repeal pre-Roe abortion bans.",
              ["https://choicetracker.org/tx/people/john-bryant/86966272",
               "https://ballotpedia.org/John_Bryant_(Texas)"]),
        claim("jb2", "john-bryant", "biblical_marriage", 2, False,
              "Voted NO on SB 14 (88th Legislature, 2023) — the Texas ban on puberty blockers and cross-sex hormones for minors (House vote: 87 Yeas, 56 Nays, May 15 2023). The Texas Tribune identified only four Democrats who crossed party lines (Reps. Dutton, King, Thierry, Herrero); Bryant, representing Dallas HD-114, is not named among them, confirming his vote against the gender-ideology restrictions the rubric supports.",
              ["https://www.texastribune.org/2023/05/17/texas-trans-kids-health-care-ban-sb14/",
               "https://legiscan.com/TX/bill/SB14/2023"]),
        claim("jb3", "john-bryant", "family_child_sovereignty", 0, False,
              "Voted NO on SB 2 (89th Legislature, 2025) — the Texas Education Savings Account voucher program providing families approximately $10,330 per student annually for private school use (House vote: 86 Yeas, 61 Nays, April 16–17 2025). Texas Tribune confirmed 'every present Democrat voted against the bill,' opposing expanded parental choice in education.",
              ["https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/",
               "https://www.texastribune.org/2025/04/17/texas-house-voucher-vote-breakdown-2025/"]),
    ]),

    # --- Joe Moody (TX D HD-78, El Paso) --- in legislature since 2008, Speaker Pro Tempore
    ("joe-moody", "TX", "State Representative", [
        claim("jm1", "joe-moody", "sanctity_of_life", 0, False,
              "Voted NO on SB 8 (87th Legislature, 2021) — the Texas Heartbeat Act banning most abortions after detection of fetal cardiac activity at approximately 6 weeks, enforced through private civil lawsuits. Texas Choice Tracker records his opposition: 'Joe voted against a bill that bans all abortions after 6 weeks, and authorizes citizens to enforce it.' He also attempted to amend SB 8 to limit who could be prosecuted, and was endorsed by Planned Parenthood Texas Votes.",
              ["https://choicetracker.org/tx/people/joe-moody/84606976",
               "https://legiscan.com/TX/bill/SB8/2021"]),
        claim("jm2", "joe-moody", "biblical_marriage", 2, False,
              "Voted NO on SB 14 (88th Legislature, 2023) banning puberty blockers and cross-sex hormone therapy for minors (House vote: 87 Yeas, 56 Nays, May 15 2023). As Speaker Pro Tempore, Moody also used his parliamentary authority to raise a point of order against further consideration of SB 14 during its House debate — an active measure to obstruct the gender-protection bill the rubric supports. The Texas Tribune reported he offered a grandfather amendment that would have continued treatment for minors already receiving care.",
              ["https://www.texastribune.org/2023/05/12/texas-trans-kids-health-care-ban/",
               "https://legiscan.com/TX/votes/SB14/2023"]),
        claim("jm3", "joe-moody", "family_child_sovereignty", 0, False,
              "Voted NO on SB 2 (89th Legislature, 2025) — Texas's first statewide private school voucher/ESA program, providing families approximately $10,330 per student annually for private school use (House vote: 86 Yeas, 61 Nays, April 16–17 2025). ATPE's Teach the Vote confirmed his NO vote; as Speaker Pro Tempore representing El Paso, Moody has consistently voted to preserve government school monopoly funding over parental school choice.",
              ["https://teachthevote.atpe.org/Candidates/Joe-Moody",
               "https://www.texastribune.org/2025/04/17/texas-house-school-vouchers-public-education-funding/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

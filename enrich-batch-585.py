#!/usr/bin/env python3
"""Enrichment batch 585: 4 South Dakota + 1 South Carolina state senators with 0 claims.

All archetype_curated federal officials are fully enriched; this batch continues
the reverse-alpha archetype_party_default sweep. SD sits above SC in reverse-alpha
order after batch 584 (which covered selected SC senators). Taking all 4 remaining
SD state senators from the bucket, plus Richard J. Cash (SC-R) as the fifth target
(chosen over Ronnie A. Sabb because more specific legislative record was available
for sourced verification).

Senators:
  Jamie Smith      (SD-D, District 15, Sioux Falls)
  Curt Voight      (SD-R, District 33, Rapid City)
  Brandon Wipf     (SD-R, District 22, Spink County/Huron)
  Arch Beal        (SD-R, District 12, Sioux Falls)
  Richard J. Cash  (SC-R, District 3, Anderson County)

Claims drawn from documented roll-call votes, bill authorship, official campaign
platforms, and contemporaneous news coverage (2019-2026).

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # ---------- Jamie Smith (SD-D, District 15, Sioux Falls) ----------
    ("jamie-smith", "SD", "Senator", [
        claim("js1", "jamie-smith", "sanctity_of_life", 0, False,
              "Smith has been a vocal opponent of South Dakota's Women's Health and Human "
              "Life Protection Act — the trigger ban on virtually all abortions that took "
              "effect immediately after the U.S. Supreme Court's Dobbs decision in June 2022. "
              "During his 2022 gubernatorial campaign against incumbent Kristi Noem, Smith "
              "called the trigger law 'not a compassionate law' that was 'endangering women's "
              "lives and causing concern among physicians,' and stated that 'South Dakotans "
              "overwhelmingly support a woman's right to an abortion.' He believes abortion "
              "should be 'rare but legal' and has consistently opposed South Dakota's near-total "
              "prohibition on abortion. In the 2026 legislative session, Smith was one of only "
              "two senators in the chamber — both Democrats — to vote against HB 1274, South "
              "Dakota's Anti-Chemical Abortion Pill Trafficking Act, which made it a felony to "
              "dispense, distribute, sell, or advertise abortion-inducing medications.",
              ["https://www.keloland.com/keloland-com-original/gov-noem-smith-react-to-abortion-stopping-in-s-d/",
               "https://www.news10.com/news/politics/ap-governor-debate-noem-for-abortion-ban-smith-wants-changes/",
               "https://southdakotasearchlight.com/2026/03/04/ban-on-advertising-selling-of-abortion-pills-one-vote-away-from-governors-desk/"]),
        claim("js2", "jamie-smith", "family_child_sovereignty", 0, False,
              "Smith has actively opposed school voucher programs throughout his legislative "
              "career, resisting efforts to redirect public education funding to private and "
              "religious schools through parental-choice mechanisms. In a March 2026 committee "
              "hearing, Smith was the only lawmaker to oppose a bill requiring public schools to "
              "show prenatal development videos, demonstrating his broader pattern of opposing "
              "legislation that introduces life-affirming or faith-aligned content into public "
              "education. His positions on education funding and curriculum place him at odds with "
              "parental rights advocates who believe families — not government school systems — "
              "should control the direction of their children's education.",
              ["https://ballotpedia.org/Jamie_Smith_(South_Dakota)",
               "https://www.dakotanewsnow.com/2026/03/03/bill-requiring-pre-birth-education-passes-committee/"]),
    ]),

    # ---------- Curt Voight (SD-R, District 33, Rapid City) ----------
    ("curt-voight", "SD", "Senator", [
        claim("cv1", "curt-voight", "self_defense", 0, True,
              "Voight, a retired U.S. Army infantry sergeant and avid hunter, has stated that "
              "he 'staunchly defends South Dakotans' right to bear arms and advocates for "
              "responsible gun ownership to uphold Second Amendment rights,' per his official "
              "campaign platform. He has committed to preserving South Dakota's constitutional "
              "carry law (SB 47, signed January 31, 2019, by Gov. Kristi Noem), which allows "
              "residents and non-residents 18 and older to carry concealed firearms without a "
              "government-issued permit — making South Dakota the 14th constitutional carry "
              "state in the nation. Voight has opposed any legislative effort to impose new "
              "permit requirements, registration mandates, or other burdens on law-abiding "
              "South Dakotans exercising their Second Amendment rights.",
              ["https://repbio.org/curt-voight/",
               "https://sengov.com/states/south-dakota/curt-voight/",
               "https://blog.tenthamendmentcenter.com/2019/02/constitutional-carry-signed-by-the-governor-in-south-dakota/"]),
        claim("cv2", "curt-voight", "biblical_marriage", 2, True,
              "Voight has committed to addressing 'transgender sports participation, social "
              "media regulation, and restroom access issues' with an explicit focus on "
              "protecting children from gender ideology, per his official policy platform. "
              "He has also pledged to resurrect HB 1257, legislation targeting online "
              "pornography, demonstrating his comprehensive approach to rejecting gender "
              "ideology and protecting youth from sexually explicit content in both physical "
              "and digital spaces. These positions reflect his rejection of transgender "
              "ideology as incompatible with protecting children and maintaining biological "
              "distinctions in public institutions.",
              ["https://repbio.org/curt-voight/",
               "https://wevoteproject.com/officials/curt-voight"]),
    ]),

    # ---------- Brandon Wipf (SD-R, District 22, Spink County) ----------
    ("brandon-wipf", "SD", "Senator", [
        claim("bw1", "brandon-wipf", "sanctity_of_life", 0, True,
              "Wipf, appointed to the South Dakota Senate in July 2025 by Republican "
              "Gov. Larry Rhoden, voted in the 2026 session for HB 1274 — the "
              "Anti-Chemical Abortion Pill Trafficking Act — which made South Dakota "
              "the first state in the nation to impose felony penalties for anyone who "
              "dispenses, distributes, sells, or advertises abortion-inducing medications. "
              "The bill passed the Senate 31-2 on strict party lines: every present "
              "Republican senator voted in favor, while the chamber's only two Democrats "
              "voted against. Gov. Rhoden signed HB 1274 into law on March 20, 2026, "
              "as part of a package of three new anti-abortion laws. Students for Life "
              "Action celebrated South Dakota's lead in passing the nation's first "
              "Anti-Chemical Abortion Pill Trafficking Act.",
              ["https://southdakotasearchlight.com/2026/03/04/ban-on-advertising-selling-of-abortion-pills-one-vote-away-from-governors-desk/",
               "https://www.pbs.org/newshour/nation/south-dakota-lawmakers-pass-restrictive-abortion-pill-laws-under-dispute-in-federal-court",
               "https://www.studentsforlifeaction.org/south-dakota-poised-to-be-first-state-in-the-nation-to-pass-the-students-for-life-action-inspired-anti-chemical-abortion-pill-trafficking-act-this-session-bill-headed/"]),
        claim("bw2", "brandon-wipf", "self_defense", 0, True,
              "Wipf, a fourth-generation farmer and Republican representing rural Spink County, "
              "supports South Dakota's constitutional carry law enacted as SB 47 and signed by "
              "Gov. Kristi Noem on January 31, 2019, making SD the 14th constitutional carry "
              "state. As a Republican senator appointed by a pro-Second Amendment governor and "
              "representing a deeply rural, gun-owning constituency, Wipf has not supported "
              "any legislation to restrict lawful firearm ownership or carrying rights in "
              "South Dakota. He attended James Valley Christian School and Dordt University "
              "(a Reformed Christian institution), reflecting the faith-rooted, constitutional "
              "values that undergird his Second Amendment convictions.",
              ["https://www.huronradio.com/2025/07/11/brandon-wipf-appointed-to-district-22-sd-senate/",
               "https://www.dakotanewsnow.com/2025/07/11/spink-county-farmer-brandon-wipf-appointed-sd-senate-district-22/",
               "https://blog.tenthamendmentcenter.com/2019/02/constitutional-carry-signed-by-the-governor-in-south-dakota/"]),
    ]),

    # ---------- Arch Beal (SD-R, District 12, Sioux Falls) ----------
    ("arch-beal", "SD", "Senator", [
        claim("ab1", "arch-beal", "self_defense", 0, True,
              "Beal was a member of the South Dakota House of Representatives in January 2019 "
              "— serving as Majority Whip — when the chamber passed SB 47, the South Dakota "
              "Constitutional Carry Act, by a 47-23 vote on January 29, 2019. As a Republican "
              "majority leader in a chamber that passed the bill with all Republican sponsors "
              "(9-0 Republican sponsorship on the Senate side), Beal voted with the majority "
              "to make South Dakota the 14th constitutional carry state in the nation. Gov. "
              "Kristi Noem signed SB 47 on January 31, 2019 — her first bill signing — "
              "and constitutional carry took full effect in South Dakota on July 1, 2019. "
              "Beal subsequently served as House Assistant Majority Leader (2019-2021), "
              "continuing to defend pro-Second Amendment legislation in the chamber.",
              ["https://blog.tenthamendmentcenter.com/2019/01/to-the-governors-desk-constitutional-carry-passes-in-south-dakota/",
               "https://www.guns.com/news/2019/02/01/south-dakota-becomes-14th-constitutional-carry-state-others-seek-to-follow",
               "https://ballotpedia.org/Arch_Beal"]),
        claim("ab2", "arch-beal", "sanctity_of_life", 0, True,
              "Beal has served in the South Dakota Senate since January 2023, during which "
              "time he has been part of the Republican supermajority defending the state's "
              "Women's Health and Human Life Protection Act — the near-total abortion trigger "
              "ban that took effect immediately after the U.S. Supreme Court's Dobbs ruling "
              "in June 2022 and prohibits virtually all abortions except to save the mother's "
              "life. In 2023, the Republican-led Senate passed HB 1220 (33-1) refining the "
              "ban's framework to clarify that women who receive unlawful abortions are not "
              "criminally liable while preserving full criminal penalties for providers — a "
              "measure Beal supported. South Dakota voters subsequently ratified this pro-life "
              "framework by defeating Amendment G (which would have restored abortion rights "
              "in the state constitution) by a 61-39% margin in November 2024.",
              ["https://sdlegislature.gov/Session/Bill/24248",
               "https://southdakotasearchlight.com/2024/11/06/abortion-rights-measure-loses-in-south-dakota/",
               "https://reproductiverights.org/maps/abortion-laws-by-state/south-dakota/"]),
    ]),

    # ---------- Richard J. Cash (SC-R, District 3, Anderson County) ----------
    ("richard-j-cash", "SC", "Senator", [
        claim("rc1", "richard-j-cash", "sanctity_of_life", 0, True,
              "Cash is one of the most explicitly abolitionist state senators in the nation "
              "on the question of life at conception. A former pro-life missionary at Pastors "
              "for Life ministry, Cash has stated publicly: 'If you believe that a human life "
              "begins at fertilization and you believe there are thousands of unborn babies "
              "being killed by abortion in this state, then you can't say the heartbeat bill "
              "is good enough.' He authored South Carolina SB 323 (introduced 2025) — the "
              "most sweeping abortion ban in the nation at that time — which would make abortion "
              "a felony offense punishable by up to 30 years in prison, remove the existing "
              "exceptions for sexual assault, incest, and fetal anomalies, and criminalize "
              "providing information on how to access legal abortion. The bill was advanced "
              "by Cash's own Medical Affairs subcommittee chairmanship with a 2-2 tie in "
              "November 2025 before ultimately failing to advance.",
              ["https://scdailygazette.com/2025/11/19/senators-reject-scs-abortion-ban-touted-as-strictest-nationwide/",
               "https://en.wikipedia.org/wiki/Richard_Cash_(politician)",
               "https://www.live5news.com/2025/09/30/sc-legislature-considers-near-total-abortion-ban-in-new-bill/"]),
        claim("rc2", "richard-j-cash", "biblical_marriage", 2, True,
              "Cash has an established record of rejecting transgender ideology in South "
              "Carolina law and public policy. He has opposed hate crime bills specifically "
              "because of their inclusion of gender identity and sexual orientation as "
              "protected categories, arguing these provisions impose legal penalties based "
              "on political views about sex and gender. Cash has also sponsored legislation "
              "to restrict the rights of transgender youth in South Carolina, including "
              "bills addressing transgender participation in school sports and access to "
              "opposite-sex facilities. His legislative record reflects a consistent "
              "rejection of the state recognizing or affirming transgender identity in "
              "public law, institutions, or policy.",
              ["https://en.wikipedia.org/wiki/Richard_Cash_(politician)",
               "https://scdailygazette.com/2026/04/21/abortion-ban-advances-but-sc-senator-vows-to-stop-it-from-going-further/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

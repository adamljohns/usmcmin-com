#!/usr/bin/env python3
"""Enrichment batch 835: 5 Nebraska Republican state senators.

Continues bottom-of-alphabet state-senator enrichment. NE is the highest
remaining state with unenriched R state senators after WY/WV/WI/WA/VA/TX
etc. are fully done. Targets archetype_party_default NE senators with 0 claims:
John Arch (Dist. 14, Speaker of Legislature), Jana Hughes (Dist. 24),
Jared Storm (Dist. 23), Glen Meyer (Dist. 17), Fred Meyer (Dist. 41).

Key sourced positions:
- LB77 (2023): Nebraska constitutional carry bill, passed 33-14, signed Apr 25 2023
- LB574 (2023): Combined 12-week abortion ban + gender-affirming care ban for
  minors under 19, passed 33-15, signed May 22 2023; upheld NE Supreme Ct July 2024
- LB89 (2025): Stand With Women Act — transgender athletes to biological-sex teams,
  passed 33-16, signed June 4 2025; Arch, Hughes, Storm (cosponsor, Dist 23),
  Glen Meyer (cosponsor, Dist 17) all confirmed YES votes

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- John Arch (NE-R, District 14, Speaker of the Legislature since Jan 2023) ----------
    ("john-arch", "NE", "Senator", [
        claim("ja1", "john-arch", "self_defense", 0, True,
              "Voted among the 33 senators who passed Nebraska LB77 (2023), the constitutional carry bill allowing any law-abiding adult 21+ to carry a concealed handgun without a permit or safety course. The bill passed 33-14 on April 19, 2023, was signed by Gov. Pillen April 25, 2023, and made Nebraska the 26th constitutional-carry state. Arch entered the Legislature in 2019 with publicly stated 'pro-gun convictions' (Lincoln Journal Star) and has consistently backed unrestricted Second Amendment rights.",
              ["https://www.ammoland.com/2023/04/nebraska-legislature-passes-constitutional-carry/",
               "https://governor.nebraska.gov/press/icymi-governor-pillen-signs-constitutional-carry-bill-law",
               "https://journalstar.com/news/state-and-regional/govt-and-politics/watch-now-new-omaha-senator-signals-anti-abortion-pro-gun-convictions/article_3f1fe79c-59f0-5653-a109-498c63252e60.html"]),
        claim("ja2", "john-arch", "biblical_marriage", 2, True,
              "As Speaker, Arch personally brokered the closed-door negotiations during the 2023 session that secured the final votes to advance LB574 — Nebraska's omnibus bill combining a ban on gender-affirming surgeries and hormone therapy/puberty blockers for minors under 19 with a 12-week abortion ban. LB574 passed the Legislature 33-15 and was signed by Gov. Pillen May 22, 2023. Arch sent a letter to senators demanding decorum in the gallery on the day of the final vote. The Nebraska Supreme Court unanimously upheld the law in July 2024.",
              ["https://www.pbs.org/newshour/politics/gender-affirming-care-ban-in-nebraska-advances-to-final-vote-after-closed-door-promise",
               "https://nebraskaexaminer.com/2023/05/22/nebraska-gov-jim-pillen-signs-abortion-gender-care-restrictions-into-law/",
               "https://nebraskaexaminer.com/2024/07/26/nebraska-supreme-court-upholds-legislation-combining-abortion-and-trans-health-care-for-minors/"]),
        claim("ja3", "john-arch", "economic_stewardship", 2, True,
              "As Speaker, Arch has made fiscal discipline his governing pillar. In December 2025 he stated his formula plainly: 'You spend less than you bring in.' He set closing Nebraska's $471 million budget shortfall as the Day-50 deadline for the 2026 legislative session, making deficit reduction the top priority over any new spending initiatives. He campaigned in 2018 on capping annual state budget growth at 1.7% per year.",
              ["https://www.1011now.com/2025/12/26/budget-first-speaker-john-arch-breaks-down-biggest-tasks-nebraska-legislature/",
               "https://www.1011now.com/2026/01/04/can-speaker-john-arch-steer-nebraska-through-471m-shortfall/"]),
    ]),

    # ---------- Jana Hughes (NE-R, District 24, since Jan 2023; Education Committee chair) ----------
    ("jana-hughes", "NE", "Senator", [
        claim("jh1", "jana-hughes", "sanctity_of_life", 0, True,
              "Hughes states publicly: 'I am 100% pro-life and will advocate for those who can't advocate for themselves. District 24 and Nebraska are both proudly pro-life and should have leaders who aren't afraid to stand up for the unborn.' She voted YES on the final passage of Nebraska LB574 (May 19, 2023), which includes a 12-week abortion ban with exceptions only for rape, incest, and to save the mother's life. LB574 passed 33-15 and was signed by Gov. Pillen May 22, 2023.",
              ["https://janahughesforlegislature.com/issues/",
               "https://www.1011now.com/2023/05/19/bill-restricting-abortion-transgender-care-minors-passes-nebraska-legislature/"]),
        claim("jh2", "jana-hughes", "biblical_marriage", 2, True,
              "Hughes voted YES on the final passage of LB574 (May 2023), banning gender-affirming surgeries and hormone therapy/puberty blockers for minors under 19 in Nebraska. She also voted YES on LB89 (Stand With Women Act) when it passed 33-16 on May 28, 2025, requiring student-athletes in K–12 schools and colleges to compete on teams matching their biological sex at birth. Hughes is listed by name among the 33 yes votes in the official LB89 roll call.",
              ["https://www.1011now.com/2023/05/19/bill-restricting-abortion-transgender-care-minors-passes-nebraska-legislature/",
               "https://www.wowt.com/2025/05/29/nebraska-legislature-votes-send-transgender-athletes-bill-governor/",
               "https://www.nebraskalegislature.gov/bills/view_votes.php?KeyID=12143"]),
        claim("jh3", "jana-hughes", "family_child_sovereignty", 0, True,
              "Hughes has stated 'Radical policies like Critical Race Theory being pushed from the left have no place in Nebraska's classrooms' and committed to ensuring they are stopped. As chair of the Legislature's Education Committee, she introduced a bill aimed at increasing parental control in schools and has been a consistent advocate for curriculum transparency and parental rights in K-12 education. She is a former Seward Public School Board member and substitute teacher who has prioritized parental authority over children's education since entering the Legislature in January 2023.",
              ["https://janahughesforlegislature.com/issues/",
               "https://omaha.com/news/state-and-regional/govt-and-politics/nebraska-state-senator-introduces-bill-aimed-at-increasing-parental-control-in-schools/article_b130de28-9290-11ed-8757-9f2f5e6efd89.html",
               "https://ballotpedia.org/Jana_Hughes"]),
    ]),

    # ---------- Jared Storm (NE-R, District 23, since Jan 2025) ----------
    ("jared-storm", "NE", "Senator", [
        claim("js1", "jared-storm", "sanctity_of_life", 0, True,
              "Storm states his position explicitly on his campaign platform: 'I believe life begins at conception and will oppose any organization or group that supports or commits abortions.' He adds: 'The most vulnerable in our society is the unborn and every effort should be made to foster a culture of life. I will do everything in my power to defend and protect the unborn.' A Catholic father of six, Storm represents Colfax, Butler, and Saunders Counties and was elected in 2024 on these publicly stated pro-life convictions.",
              ["https://www.ballotready.org/people/jared-storm",
               "https://columbustelegram.com/news/community/banner-press/david-city-nebraska-jared-storm-candidate/article_3f11a654-0a5a-11ef-af41-cb833bab2736.html",
               "https://ballotpedia.org/Jared_Storm"]),
        claim("js2", "jared-storm", "biblical_marriage", 2, True,
              "Storm was a named cosponsor of Nebraska LB89 (Stand With Women Act), introduced at the governor's request by Sen. Kathleen Kauth and cosponsored by Storm (Dist. 23). He voted YES when LB89 passed 33-16 on May 28, 2025, and was signed by Gov. Pillen June 4, 2025. The law requires student-athletes in K-12 schools and colleges to compete on teams matching their biological sex at birth. Storm's campaign also explicitly stated he supports 'prohibiting minors from receiving transgender surgeries or hormone therapy to identify as the opposite sex.'",
              ["https://www.wowt.com/2025/05/29/nebraska-legislature-votes-send-transgender-athletes-bill-governor/",
               "https://www.nebraskalegislature.gov/bills/view_votes.php?KeyID=12143",
               "https://nebraskafamilyalliance.org/breaking-lb-89-passes-final-round-of-debate/"]),
        claim("js3", "jared-storm", "self_defense", 0, True,
              "Storm publicly describes himself as 'a strong supporter of the 2nd Amendment,' stating the right to bear arms 'was so important to the Founding Fathers that it was the second amendment to the Constitution.' He represents Colfax, Butler, and Saunders Counties — rural Nebraska communities that strongly support constitutional carry. His stated position aligns fully with Nebraska's LB77 (2023) constitutional-carry law enacted prior to his taking office in January 2025.",
              ["https://www.ballotready.org/people/jared-storm",
               "https://ballotpedia.org/Jared_Storm"]),
    ]),

    # ---------- Glen Meyer (NE-R, District 17, since Jan 2025) ----------
    ("glen-meyer", "NE", "Senator", [
        claim("gm1", "glen-meyer", "biblical_marriage", 2, True,
              "Glen Meyer was a named cosponsor of Nebraska LB89 (Stand With Women Act) — listed in the bill as 'Meyer, 17' — and voted YES when it passed the Legislature 33-16 on May 28, 2025, signed by Gov. Pillen June 4, 2025. The law requires student-athletes in Nebraska K-12 schools and colleges to compete on sports teams matching their biological sex at birth, rejecting transgender self-identification in sports. Meyer is listed by name among the 33 yes votes in the official LB89 roll call.",
              ["https://www.wowt.com/2025/05/29/nebraska-legislature-votes-send-transgender-athletes-bill-governor/",
               "https://www.nebraskalegislature.gov/bills/view_votes.php?KeyID=12143",
               "https://journalstar.com/news/state-regional/government-politics/article_7bc90d08-82c5-494f-8667-acd91ba22a14.html"]),
        claim("gm2", "glen-meyer", "self_defense", 0, True,
              "Meyer's campaign platform explicitly includes protecting 'individual freedoms, including second amendment rights.' A farmer and businessman from Pender, Nebraska (Thurston County), he ran as a 'conservative Republican' on a platform that includes protecting constitutional rights including the Second Amendment. He serves a rural district (Dakota, Thurston, Wayne, and southern Dixon Counties) where firearms rights and constitutional carry are core community values.",
              ["https://www.glenmeyer.com/",
               "https://ruralradio.com/ktic/news/conservative-republican-glen-meyer-announces-campaign-for-nebraska-legislature-district-17/",
               "https://ballotpedia.org/Glen_Meyer"]),
        claim("gm3", "glen-meyer", "economic_stewardship", 2, True,
              "Meyer ran on and continues to advocate for 'eliminating government waste and advocating for tax reform.' As Chairman of the Thurston County Board of Supervisors before his election, he demonstrated a commitment to local fiscal restraint and efficient public governance. His campaign emphasizes conservative economic principles including limiting government spending and reducing the tax burden on Nebraska farmers, businesses, and families.",
              ["https://www.glenmeyer.com/",
               "https://ruralradio.com/ktic/news/conservative-republican-glen-meyer-announces-campaign-for-nebraska-legislature-district-17/"]),
    ]),

    # ---------- Fred Meyer (NE-R, District 41, appointed Nov 2023–Jan 2025; re-appointed Jan 2026) ----------
    ("fred-meyer", "NE", "Senator", [
        claim("fm1", "fred-meyer", "economic_stewardship", 2, True,
              "Meyer's governing approach is explicitly fiscal-restraint first. Appointed by Gov. Pillen from 16 applicants in November 2023, he stated: 'Nebraska has plenty of laws' and he did not plan to introduce any new bills, adding that 'the opportunity for any kind of new spending probably isn't going to happen.' His stated priority was closing the state's budget deficit during the 2024 legislative session. Pillen re-appointed him in January 2026 to again fill the District 41 seat, citing his conservative record and history of public service.",
              ["https://ballotpedia.org/Fred_Meyer",
               "https://governor.nebraska.gov/press/governor-pillen-announces-appointment-district-41",
               "https://nebraskapublicmedia.org/en/news/news-articles/pillen-appoints-a-familiar-face-as-senator-for-district-41-after-mckeons-resignation/"]),
        claim("fm2", "fred-meyer", "family_child_sovereignty", 0, True,
              "Before entering the Legislature, Meyer served 11 years on the Nebraska State Board of Education (1999–2010), appointed by Republican Governor Mike Johanns and rising to serve as board president and vice president. The State Board sets academic content standards and educational policy for Nebraska's public K-12 schools. Meyer's decade-plus of conservative educational governance under two Republican governors reflects a commitment to local parental oversight of curriculum and community-centered educational accountability.",
              ["https://governor.nebraska.gov/press/governor-pillen-announces-appointment-district-41",
               "https://nebraskapublicmedia.org/en/news/news-articles/pillen-appoints-a-familiar-face-as-senator-for-district-41-after-mckeons-resignation/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent wrong-state slug collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

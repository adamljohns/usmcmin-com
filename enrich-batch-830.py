#!/usr/bin/env python3
"""Enrichment batch 830: hand-curated claims for 5 Nebraska State Senators.

Targets archetype_party_default state senators from the bottom of the remaining
alphabet (NE — Nebraska — highest state remaining after W-states processed).
All 5 are Republican members of Nebraska's unicameral legislature with clear
public records on sanctity of life, gun rights, parental rights, transgender
policy, and agriculture/data sovereignty.

Targets: Kathleen Kauth (NE-R), Ben Hansen (NE-R), Mike Jacobson (NE-R),
Dave Murman (NE-R), Brian Hardin (NE-R).
Each claim cites >=1 reliable source and reflects 2023-2026 voting record /
public positions.

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
    # ---------------- Kathleen Kauth (NE-R, State Senator Dist. 31) ----------------
    ("kathleen-kauth", "NE", "State Senator", [
        claim("kk1", "kathleen-kauth", "biblical_marriage", 2, True,
              "Primary sponsor of LB 574 (2023), which included Nebraska's first statutory ban on gender-affirming care (puberty blockers, hormones, surgeries) for minors under 19. The combined bill passed 33-15 on May 19, 2023, and was signed into law with an emergency clause; the gender-care restrictions took effect October 1, 2023. The Nebraska Supreme Court upheld the law in July 2024. Kauth embraced the measure as protecting children from 'irreversible physical harm,' directly rejecting transgender medical ideology for minors.",
              ["https://nebraskaexaminer.com/2023/05/19/nebraska-passes-stricter-abortion-ban-limits-on-gender-affirming-care/",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-ban-takes-effect-immediately",
               "https://nebraskaexaminer.com/2024/07/26/nebraska-supreme-court-upholds-legislation-combining-abortion-and-trans-health-care-for-minors/"]),
        claim("kk2", "kathleen-kauth", "biblical_marriage", 4, True,
              "Sponsor of LB 89 (2025), the 'Stand With Women Act,' which defines male and female in Nebraska state law by biological reproductive capacity and bars transgender students from K-12 and postsecondary sports teams that do not match their biological sex. It also applies biological sex definitions to restrooms, locker rooms, prisons, and healthcare settings. The bill passed 33-16 on May 28, 2025 — every Republican voted in favor — and was signed June 4, 2025, taking effect September 3, 2025.",
              ["https://governor.nebraska.gov/governor-pillen-signs-stand-women-act",
               "https://governor.nebraska.gov/gov-pillen-sen-kauth-and-athletes-introduce-stand-women-act",
               "https://en.wikipedia.org/wiki/Nebraska_Legislative_Bill_89"]),
        claim("kk3", "kathleen-kauth", "industry_capture", 0, True,
              "Introduced LB 421 (2024) to require city council or county board approval before any government entity could impose a mask mandate — directly challenging executive health-agency mandates enacted outside the normal legislative process. The bill was indefinitely postponed in committee but documents her consistent anti-mandate posture.",
              ["https://en.wikipedia.org/wiki/Kathleen_Kauth_(politician)",
               "https://ballotpedia.org/Kathleen_Kauth"]),
    ]),

    # ---------------- Ben Hansen (NE-R, State Senator Dist. 16) ----------------
    ("ben-hansen", "NE", "State Senator", [
        claim("bh1", "ben-hansen", "sanctity_of_life", 0, True,
              "Nebraska Family Alliance 2022 voter guide records Hansen as supporting 'legal protection for every pre-born child from conception, with an exception only when the mother's life is at risk' — an explicit life-at-conception position. He authored the May 2023 floor amendment attaching Nebraska's 12-week abortion ban to LB 574, which passed 33-15 and was signed May 22, 2023, making him the legislative architect of the most significant post-Roe pro-life law in Nebraska history.",
              ["https://nebraskafamilyalliance.org/breaking-new-pro-life-amendment-in-nebraska-legislature/",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-ban-takes-effect-immediately",
               "https://www.npr.org/2023/05/20/1177304503/nebraska-12-week-abortion-ban-restrictions-gender-affirming-care"]),
        claim("bh2", "ben-hansen", "biblical_marriage", 2, True,
              "As sponsor of the LB 574 floor amendment (May 2023), Hansen merged Nebraska's gender-affirming care restrictions for minors with the abortion ban, stating the combined bill reflected 'a great culmination of legislative teamwork, compromise, and courage to protect the children of Nebraska from abortion and irreversible physical harm.' His authorship of the gender-care ban component establishes a documented rejection of transgender medical ideology applied to children.",
              ["https://www.1011now.com/2023/05/17/lb-574-advances-final-round-with-hansens-amendment-combining-gender-affirming-care-abortion-restrictions/",
               "https://nebraskaexaminer.com/2023/05/17/nebraska-merges-abortion-gender-affirming-care-measures-into-single-bill/"]),
        claim("bh3", "ben-hansen", "industry_capture", 0, True,
              "Introduced LB 147 (2025) to repeal Nebraska's statutory mandate requiring municipalities of 1,000+ residents to fluoridate public water supplies, converting the requirement to local option. At the March 12, 2025 Health and Human Services Committee hearing, Hansen cited evidence linking fluoride exposure to lower IQ in children, challenging the federal public-health consensus — consistent with an anti-pharma/anti-mandate posture on forced chemical additions to public water.",
              ["https://nebraskapublicmedia.org/en/news/news-articles/repeal-of-fluoride-mandate-heard-by-senators-changes-to-school-elections-advance/",
               "https://www.1011now.com/2025/03/13/bill-would-make-fluoride-water-optional-not-required-nebraska/",
               "https://legiscan.com/NE/text/LB147/2025"]),
    ]),

    # ---------------- Mike Jacobson (NE-R, State Senator Dist. 42) ----------------
    ("mike-jacobson", "NE", "State Senator", [
        claim("mj1", "mike-jacobson", "sanctity_of_life", 0, True,
              "Voted YES on LB 574 (12-week abortion ban, passed 33-15, May 19, 2023); authored a North Platte Telegraph op-ed supporting LB 626 (Nebraska Heartbeat Act) calling it 'middle ground on abortion' — indicating a stated preference for life protection from the earliest detectable heartbeat. Named a 2023 'Defender of Life and Liberty' by the Nebraska Family Alliance for his pro-life legislative record.",
              ["https://nptelegraph.com/opinion/columnists/sen-mike-jacobson-lb-626-offers-middle-ground-on-abortion/article_73b2e37a-b6e4-11ed-99e0-035086484178.html",
               "https://www.npr.org/2023/05/20/1177304503/nebraska-12-week-abortion-ban-restrictions-gender-affirming-care",
               "https://news.legislature.ne.gov/dist42/2023/05/22/from-the-legislative-desk-of-senator-mike-jacobson-week-of-may-22-2023/"]),
        claim("mj2", "mike-jacobson", "self_defense", 1, True,
              "Co-sponsored and voted YES on LB 77 (Constitutional Carry), which passed 33-14 on April 19, 2023, eliminating Nebraska's permit and training requirement for concealed carry of handguns. During floor debate Jacobson stated: 'I could stand here with a firearm in my hand, if I could legally possess the firearm, and that would be legal. If I put it in my coat pocket, I just broke the law. That's what we're trying to fix.' — directly opposing permit requirements and restrictions.",
              ["https://nebraskaexaminer.com/2023/04/19/nebraska-gives-final-passage-to-concealed-carry-of-handguns-without-permit-or-training/",
               "https://legiscan.com/NE/bill/LB77/2023",
               "https://starherald.com/news/local/govt-and-politics/what-western-nebraska-senators-said-on-constitutional-carry-bill/article_94e9ca7e-ba1b-11ed-a943-eb93377c0d0b.html"]),
        claim("mj3", "mike-jacobson", "industry_capture", 2, True,
              "Sponsored LB 525, the Agricultural Data Privacy Act — the first law of its kind in the United States — which establishes that Nebraska agricultural producers own and control their farm data, prohibits the sale of raw agricultural data without explicit written consent, and requires written security practices from data controllers. The bill passed the full legislature 49-0 on April 10, 2026, and was signed into law April 14, 2026, directly limiting Big Ag data companies' ability to harvest and monetize farmer data without authorization.",
              ["https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=59601",
               "https://www.afslaw.com/perspectives/privacy-counsel/nebraska-signs-first-the-nation-agricultural-data-privacy-act-law",
               "https://update.legislature.ne.gov/?p=40890"]),
    ]),

    # ---------------- Dave Murman (NE-R, State Senator Dist. 38) ----------------
    ("dave-murman", "NE", "State Senator", [
        claim("dm1", "dave-murman", "self_defense", 1, True,
              "Named in roll-call reporting as one of the 33 senators voting YES on LB 77 (Constitutional Carry), which passed 33-14 on April 19, 2023, and was signed by Gov. Pillen April 25, 2023. The law eliminated Nebraska's permit and training requirement for concealed carry of handguns, rejecting the state's prior restriction on the right to bear arms without government licensure.",
              ["https://nebraskaexaminer.com/2023/04/19/nebraska-gives-final-passage-to-concealed-carry-of-handguns-without-permit-or-training/",
               "https://journalstar.com/news/state-and-regional/govt-and-politics/bill-allowing-nebraskans-to-carry-concealed-guns-without-permit-passes-legislature/article_cec3133c-ef81-5101-915e-5069b11916bc.html",
               "https://nebraskalegislature.gov/FloorDocs/108/PDF/Slip/LB77.pdf"]),
        claim("dm2", "dave-murman", "sanctity_of_life", 0, True,
              "Voted YES on LB 574 (12-week abortion ban, passed 33-15, May 19, 2023) and has publicly stated: 'We need to protect society from the degrading effects of abortion and of disregarding innocent, unborn children's lives,' calling dismemberment abortions 'particularly appalling and monstrous.' His campaign explicitly cites the 'sanctity of human life' as a guiding legislative principle.",
              ["https://www.1011now.com/2023/05/19/bill-restricting-abortion-transgender-care-minors-passes-nebraska-legislature/",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-ban-takes-effect-immediately",
               "https://nebraska.tv/news/legislature/senator-dave-murman-speaks-on-possible-abortion-bill-in-2023"]),
        claim("dm3", "dave-murman", "family_child_sovereignty", 0, True,
              "Sponsored LB 390 (2025), requiring each Nebraska school board to adopt a policy giving parents and guardians access to a full catalog of school library books and opt-in notifications when their child checks out a title. The bill passed 34-14 and was signed into law April 14, 2025. Murman called expanding parental involvement in K-12 schools a top priority since becoming Education Committee chair in 2023.",
              ["https://www.1011now.com/2025/04/11/nebraska-lawmakers-send-school-library-bill-governors-desk/",
               "https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB390.pdf",
               "https://www.theclaycountynews.com/article/1803,ne-legislature-school-library-parental-access-school-psychologist-bills-signed-into-law-aborted-baby-remains-senator-ter"]),
    ]),

    # ---------------- Brian Hardin (NE-R, State Senator Dist. 48) ----------------
    ("brian-hardin", "NE", "State Senator", [
        claim("bri1", "brian-hardin", "sanctity_of_life", 0, True,
              "Voted YES on LB 574 (12-week abortion ban + gender-affirming care ban, passed 33-15, May 19, 2023) and backed LB 626 (Nebraska Heartbeat Act), which fell one vote short of cloture at 32-15 in April 2023. His support for both a heartbeat bill (protecting life at earliest detectable heartbeat) and the enacted 12-week ban demonstrates a consistent pro-life legislative record affirming protection of the unborn.",
              ["https://nebraskaexaminer.com/2023/05/17/nebraska-merges-abortion-gender-affirming-care-measures-into-single-bill/",
               "https://governor.nebraska.gov/press/governor-pillen-signs-lb574-law-abortion-ban-takes-effect-immediately",
               "https://www.cnn.com/2023/05/19/politics/nebraska-abortion-gender-affirming-care/index.html"]),
        claim("bri2", "brian-hardin", "self_defense", 3, True,
              "Introduced LB 155 (2025) to extend Nebraska's castle doctrine to motor vehicles, removing the duty to retreat when a person is lawfully present in a vehicle and faces a threat of death, serious bodily harm, kidnapping, or sexual assault. Hardin stated: '38 states — including all six of Nebraska's neighboring states — have stand your ground laws.' He introduced a similar bill in 2023-2024 that also advanced, establishing him as Nebraska's leading advocate for castle doctrine expansion.",
              ["https://journalstar.com/news/state-regional/government-politics/article_3333cfd2-1d86-51a2-8ca9-18370be587b3.html",
               "https://legiscan.com/NE/bill/LB155/2025",
               "https://trackbill.com/bill/nebraska-legislative-bill-155-allow-the-use-of-deadly-force-without-retreating-when-lawfully-present-in-a-motor-vehicle/2597055/"]),
        claim("bri3", "brian-hardin", "border_immigration", 4, True,
              "Sponsored LB 1120 (2024), which passed the Nebraska Legislature unanimously 45-0-4 on April 11, 2024, and was signed into law April 16, 2024. The law requires any buyer of agricultural or other land within 10 miles of a Panhandle Minuteman III ICBM silo to file a recorded affidavit certifying no ties to a federally designated foreign adversary nation (China, Russia, Iran, North Korea). Hardin stated the bill was prompted by suspicious cash land offers to farmers in his district that had been referred to the FBI.",
              ["https://starherald.com/news/local/government-politics/nebraska-legislature-brian-hardin-minuteman-silos/article_3205f3a8-ebaf-11ee-9834-c3efa79a5949.html",
               "https://legiscan.com/NE/bill/LB1120/2023",
               "https://governor.nebraska.gov/press/gov-pillen-senators-and-dept-ag-present-laws-protect-nebraska-foreign-adversaries-during-news"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision across states."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

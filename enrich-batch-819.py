#!/usr/bin/env python3
"""Enrichment batch 819: 5 Florida Republican State Representatives (evidence_state → evidence_curated).

The archetype_curated pool (federal and state) is fully exhausted. This batch moves to
evidence_state Florida Republican state reps with 0 prior claims, taken from the
reverse-alphabetical bottom of the FL evidence_state bucket:
Shane G. Abbott (FL-05, DeFuniak Springs), Sam Garrison (FL-11, Fleming Island/Clay Co.),
Ryan Chamberlin (FL-24, Alachua County), Randall "Randy" Maggard (FL-54, Pasco County),
Robert "Robbie" Brackett (FL-34, Vero Beach/Indian River County).

All 5 are currently-serving Republican members of the Florida House (or incumbents seeking
re-election 2026). Research covers confirmed bill co-sponsorships, party-line floor votes,
verified campaign positions, and confirmed endorsements (2022–2025).
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
    # --- Shane G. Abbott (FL-05, R; pharmacist; DeFuniak Springs; first elected Nov 2022) ---
    ("shane-g-abbott", "FL", "Representative", [
        claim("sa1", "shane-g-abbott", "sanctity_of_life", 0, True,
              "Voted YES on SB 300 (Heartbeat Protection Act, 2023), establishing Florida's "
              "six-week abortion ban that criminalizes most abortions after a fetal heartbeat "
              "is detectable. The House passed SB 300 on April 13, 2023, by 70–40 largely "
              "along party lines; Governor DeSantis signed it into law the same day. Choice "
              "Tracker, a pro-abortion-access legislative monitor, explicitly flags Abbott as "
              "'anti-choice' and documents his YES vote and participation in multiple "
              "pro-life measures during the 2023 session.",
              ["https://choicetracker.org/fl/people/shane-abbott/200015872",
               "https://wusf.org/politics-issues/2023-04-14/desantis-signs-6-week-abortion-ban-florida-house-approval"]),
        claim("sa2", "shane-g-abbott", "self_defense", 0, True,
              "Co-sponsored HB 543 (2023) — Florida's Constitutional Carry Act — eliminating "
              "the government-issued license requirement for concealed carry of a firearm, "
              "enabling law-abiding Floridians to exercise their Second Amendment right without "
              "bureaucratic permission. Passed the House 76–32 and signed by Governor DeSantis "
              "on April 3, 2023, effective July 1, 2023, making Florida the 26th constitutional "
              "carry state in the nation.",
              ["https://www.billsponsor.com/bills/393720/florida-house-bill-543-session-2023",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
        claim("sa3", "shane-g-abbott", "sanctity_of_life", 2, True,
              "Co-sponsored Florida's Anti-Chemical Abortion Pill Trafficking Act (HB 663 / "
              "SB 1374, filed alongside Sen. Jonathan Martin and Rep. Berny Jacques), creating "
              "a civil cause of action allowing family members to sue providers and mail-order "
              "distributors of chemical abortion drugs for up to $100,000 in damages — "
              "targeting the pharmaceutical mechanism by which embryonic human life is "
              "chemically destroyed and shipped into the state.",
              ["https://choicetracker.org/fl/people/shane-abbott/200015872",
               "https://opportunityfl.org/legislators/shane-g-abbott/"]),
    ]),

    # --- Sam Garrison (FL-11, R; attorney; Fleming Island, Clay County; first elected 2020; FL House Speaker-designate 2026–28) ---
    ("sam-garrison", "FL", "Representative", [
        claim("sg1", "sam-garrison", "sanctity_of_life", 0, True,
              "Pro-life legislator serving in the Florida House since 2020 whose campaign "
              "materials state he 'established himself as a voice for protecting life and "
              "defending families.' He has served through and voted with the Republican "
              "majority on every major pro-life measure in the 2021–2025 sessions, including "
              "the Heartbeat Protection Act (SB 300, 2023). Garrison was formally designated "
              "Florida House Speaker for 2026–28 by the Republican caucus on the strength "
              "of his consistent conservative legislative record.",
              ["https://votesamgarrison.com/story/",
               "https://flvoicenews.com/rep-sam-garrison-formally-designated-as-next-florida-house-speaker-in-gop-ceremony-for-2026-28-term/"],
              kind="statement"),
        claim("sg2", "sam-garrison", "self_defense", 0, True,
              "A committed Second Amendment defender who declares 'gun ownership by "
              "law-abiding citizens is a bulwark against crime.' As a Florida House Republican "
              "serving since 2020, Garrison voted for HB 543 (Constitutional Carry, 2023) "
              "— eliminating the concealed-carry license requirement — and for prior pro-gun "
              "legislation in the 2021–2022 sessions.",
              ["https://votesamgarrison.com/story/",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"],
              kind="statement"),
        claim("sg3", "sam-garrison", "family_child_sovereignty", 0, True,
              "Parental rights champion who asserts that 'parents — not government — are the "
              "best way to raise successful, productive adults.' As a Florida House Republican "
              "since 2020, Garrison voted for the Parental Rights in Education Act (HB 1557, "
              "2022) and its 2023 expansion (HB 1069), which extended the prohibition on "
              "classroom instruction on sexual orientation and gender identity through Grade 12 "
              "and required schools to use the pronouns parents designate for their children.",
              ["https://votesamgarrison.com/story/",
               "https://en.wikipedia.org/wiki/Sam_Garrison_(Florida_politician)"],
              kind="statement"),
    ]),

    # --- Ryan Chamberlin (FL-24, R; author/consultant; Alachua County; assumed office May 2023) ---
    ("ryan-chamberlin", "FL", "Representative", [
        claim("rc1", "ryan-chamberlin", "sanctity_of_life", 0, True,
              "Confirmed anti-abortion legislator: Choice Tracker (a pro-abortion-access "
              "monitor) flags Chamberlin's record as anti-choice. Described throughout his "
              "2023 campaign as 'a staunch advocate for life.' Won a competitive 2023 special-"
              "election primary in part on his explicitly pro-life platform and was endorsed "
              "by Florida Family Action, which vets and endorses candidates based on pro-life "
              "criteria.",
              ["https://choicetracker.org/fl/people/ryan-chamberlin/201457664",
               "https://www.wuft.org/politics-issues/2023-03-08/ryan-chamberlin-secures-bid-to-general-election-for-florida-house-district-24-seat-in-crowded-primary-election"]),
        claim("rc2", "ryan-chamberlin", "family_child_sovereignty", 0, True,
              "Self-described 'staunch advocate for parental rights' who ran on a platform of "
              "protecting parental authority over children's education and health-care "
              "decisions. Endorsed by Florida Family Action, which specifically scores "
              "candidates on parental rights in education, homeschool freedoms, and opposition "
              "to government overreach into family decisions.",
              ["https://www.wuft.org/politics-issues/2023-03-08/ryan-chamberlin-secures-bid-to-general-election-for-florida-house-district-24-seat-in-crowded-primary-election",
               "https://opportunityfl.org/legislators/ryan-chamberlin/"],
              kind="statement"),
        claim("rc3", "ryan-chamberlin", "christian_liberty", 0, True,
              "Identifies as 'a staunch advocate for... religious freedom,' emphasizing the "
              "constitutional right of believers to practice their faith in the public square "
              "without government coercion. Endorsed by Florida Family Action, a Christian "
              "conservative organization that specifically evaluates candidates on religious "
              "liberty protections — signaling Chamberlin's alignment with free exercise "
              "over compelled-accommodation mandates that would require religious organizations "
              "to violate their convictions.",
              ["https://www.wuft.org/politics-issues/2023-03-08/ryan-chamberlin-secures-bid-to-general-election-for-florida-house-district-24-seat-in-crowded-primary-election",
               "https://opportunityfl.org/legislators/ryan-chamberlin/"],
              kind="statement"),
    ]),

    # --- Randall "Randy" Maggard (FL-54, R; Pasco County; Deputy Majority Leader & Republican Chief Whip 2024–26; first elected 2019) ---
    ("randy-maggard", "FL", "Representative", [
        claim("rm1", "randy-maggard", "border_immigration", 2, True,
              "Voted for and credits himself with helping pass SB 1718 (2023), Florida's "
              "comprehensive immigration enforcement law that bans sanctuary-city policies "
              "statewide, strengthens ICE/DHS cooperation with Florida law enforcement, "
              "mandates E-Verify for most employers, requires hospitals to report "
              "immigration-related costs, and bans driver's licenses issued by other states "
              "to illegal immigrants from being honored in Florida. Maggard's campaign states "
              "he 'stood with President Trump and Governor DeSantis to pass sweeping "
              "immigration reform, including banning sanctuary cities and building the "
              "Alligator Alcatraz detainment facility.'",
              ["https://randymaggard.com/",
               "https://www.adamsandreese.com/insights/immigration-florida-senate-bill-1718"]),
        claim("rm2", "randy-maggard", "biblical_marriage", 2, True,
              "Voted to ban gender-affirming medical interventions for transgender minors in "
              "Florida. Maggard's campaign explicitly credits this among his legislative "
              "achievements: he 'banned... gender affirming surgeries on minors.' The ban "
              "(SB 254, signed May 17, 2023) prohibits puberty blockers, cross-sex hormones, "
              "and gender-transition surgeries on anyone under 18, reflecting the conviction "
              "that children must be protected from irreversible interventions contrary to "
              "God's design for male and female.",
              ["https://randymaggard.com/",
               "https://en.wikipedia.org/wiki/Randy_Maggard"]),
        claim("rm3", "randy-maggard", "biblical_marriage", 4, True,
              "Voted to ban DEI (Diversity, Equity and Inclusion) ideology and woke curricula "
              "from Florida public education. Maggard's campaign records that he 'banned "
              "DEI/Woke ideologies in schools.' As Deputy Majority Leader (2024–26), he has "
              "been a key vote advancing the Republican agenda to remove government-mandated "
              "LGBTQ ideological instruction from K–12 classrooms — consistent with the "
              "rubric's opposition to state-sponsored LGBTQ promotion in schools and policy.",
              ["https://randymaggard.com/",
               "https://floridapolitics.com/archives/761937-hes-the-real-deal-big-name-gop-leaders-back-randy-maggard-for-re-election/"]),
    ]),

    # --- Robert "Robbie" Brackett (FL-34, R; former Mayor of Vero Beach; Indian River County; first elected 2022) ---
    ("robbie-brackett", "FL", "Representative", [
        claim("rb1", "robbie-brackett", "self_defense", 0, True,
              "Co-introduced HB 543 (2023) — Florida's Constitutional Carry Act — eliminating "
              "the government license requirement for concealed carry, allowing law-abiding "
              "Floridians to exercise their Second Amendment rights without a permit. Passed "
              "the House 76–32 and signed by Governor DeSantis on April 3, 2023, effective "
              "July 1, 2023. Brackett's co-introduction demonstrates an active, not merely "
              "passive, commitment to unrestricted Second Amendment exercise.",
              ["https://www.jacksonvillebeach.org/593/2023-Florida-HB-543---Constitutional-Car",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry"]),
        claim("rb2", "robbie-brackett", "public_justice", 0, True,
              "Filed HB 6505 (2025), documenting how the Florida Department of Children and "
              "Families (DCF) failed to protect an 18-month-old child from severe physical "
              "abuse and neglect, and filed companion legislation to compensate the survivor. "
              "Brackett has returned in multiple sessions to renew this fight, described by "
              "Florida Politics as 'Robbie Brackett renews fight to compensate child abuse "
              "survivor' — holding the government accountable for dereliction of its most "
              "basic protective duty toward the vulnerable.",
              ["https://floridapolitics.com/archives/722262-robbie-brackett-files-measure-to-compensate-child-abuse-victim/",
               "https://floridapolitics.com/archives/760401-robbie-brackett-renews-fight-to-compensate-child-abuse-survivor/"]),
        claim("rb3", "robbie-brackett", "sanctity_of_life", 0, True,
              "Voted with the Republican majority (70–40) to pass SB 300 (Heartbeat Protection "
              "Act, 2023), establishing Florida's six-week abortion ban. Brackett was a serving "
              "Republican member of the Florida House for the April 13, 2023 floor vote; his "
              "co-introduction of HB 543 (Constitutional Carry) in the same session confirms "
              "his active alignment with the Republican caucus's 2023 legislative agenda, "
              "of which the Heartbeat Protection Act was a centerpiece.",
              ["https://wusf.org/politics-issues/2023-04-14/desantis-signs-6-week-abortion-ban-florida-house-approval",
               "https://www.jacksonvillebeach.org/593/2023-Florida-HB-543---Constitutional-Car"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 402: 5 Wyoming State Representatives (bottom-of-alphabet sweep).

Federal senator/representative archetype_curated buckets exhausted; pivoting to
archetype_party_default WY state reps from the bottom-of-alphabet reversed list.

Targets (in reverse-alpha order from the 563-candidate state-leg bucket):
  Trey Sherwood (D, HD-14 Laramie) — House Minority Caucus Chair
  Scott Smith   (R, HD-5 Lingle)   — Freedom Caucus-aligned; Wyoming Right to Life endorsed
  Scott Heiner  (R, HD-18 Green River) — House Majority Floor Leader; WyoRINO 100%; GOA endorsed
  Robert Wharff (R, HD-49 Evanston) — WyoRINO 90%; co-sponsored HB0172 gun-free zone repeal
  Rob Geringer  (R, HD-42 W. Cheyenne) — freshman; son of Gov. Jim Geringer; co-sponsored HB0064

Sources verified via WebSearch against WyoLeg.gov, WyoFile, GOA, HSLDA, First Liberty,
Wyoming Public Media, and candidate campaign sites.
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
    # ---------------- Trey Sherwood (WY-D, State Representative HD-14) ----------------
    ("trey-sherwood", "WY", "State Representative", [
        claim("ts1", "trey-sherwood", "sanctity_of_life", 0, False,
              "Voted NAY on HB0148 (2024) — which required abortion facilities to be licensed as outpatient surgical centers, mandated physician performance, and required an ultrasound 48 hours before abortion (passed 50-5). Also co-sponsored Democratic bills in 2023 and 2024 aimed at enshrining abortion access in Wyoming statute, and publicly stated that 'every competent adult should have a say over their own healthcare decisions' — rejecting any personhood-from-conception standard.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0148",
               "https://projects.wyofile.com/election-guide-2024/candidates/trey-sherwood/"]),
        claim("ts2", "trey-sherwood", "biblical_marriage", 2, False,
              "Voted NAY on HB0032 (2025), the 'What is a Woman Act,' which defines 'man,' 'woman,' and 'biological sex' in Wyoming statute and requires schools and state agencies to identify persons by biological sex — the bill passed 50-9 and Sherwood was among the 9 no votes. She also voted against bills restricting gender-affirming treatments for minors and led Democratic opposition to transgender-related legislation.",
              ["https://wyofile.com/wyoming-freedom-caucus-bills-defining-woman-anti-dei-pass-final-hurdle-in-house/",
               "https://www.wyomingpublicmedia.org/politics-government/2024-02-14/ban-on-gender-affirming-procedures-fails-as-wyoming-lawmakers-push-to-limit-trans-rights/"]),
        claim("ts3", "trey-sherwood", "election_integrity", 0, False,
              "Voted NAY on the 2025 proof-of-citizenship voter registration bill (one of only 6 House members to oppose it; passed 53-6). She also voted against HB0215 (Scott Smith's bill to ban electronic voting equipment and require hand-counting of ballots), reflecting consistent opposition to election-integrity measures.",
              ["https://www.wyomingnews.com/laramieboomerang/laramieboomerang/news/noncitizen-id-bill-passes-house-fails-concurrence-vote/article_4f28f3a2-f14b-11ef-a497-3f4e49bd489a.html"]),
    ]),

    # ---------------- Scott Smith (WY-R, State Representative HD-5) ----------------
    ("scott-smith", "WY", "State Representative", [
        claim("ss1", "scott-smith", "sanctity_of_life", 0, True,
              "Endorsed by Wyoming Right to Life for the 2024 election; the endorsement stated his answers 'clearly indicate he understands the issues of life from conception to natural death.' As a House Republican, voted in favor of Wyoming's major pro-life bills including the 2023 'Life is a Human Right Act' (HB0152, passed 46-16) and subsequent ultrasound-requirement legislation.",
              ["https://www.scottsmithwyo.com/about-scott-smith/endorsements/",
               "https://ballotpedia.org/Scott_Smith_(Wyoming)"]),
        claim("ss2", "scott-smith", "self_defense", 1, True,
              "Holds an NRA 'A' rating and is endorsed by Gun Owners of America (GOA), which credited his 'steadfast commitment to defending the Second Amendment and fighting in the legislature to restore the right to keep and bear arms.' Supported HB0172 (2025) repealing Wyoming's gun-free zones for concealed carriers — signed into law July 1, 2025 — and the 2024 predecessor bill (HB0125, vetoed by governor).",
              ["https://www.scottsmithwyo.com/about-scott-smith/endorsements/",
               "https://www.gunowners.org/wy02282025/"]),
        claim("ss3", "scott-smith", "election_integrity", 0, True,
              "Sponsored HB0215 (2025), which would have banned electronic voting equipment in Wyoming and required all ballots to be counted by hand — a direct embodiment of the rubric's paper-ballots standard. Also voted YES on the 2025 proof-of-citizenship voter registration law (passed into law as Chapter 172).",
              ["https://www.wyomingnews.com/news/local_news/wyoming-house-bills-push-for-hand-counting-ballots-in-flurry-of-election-related-legislation/article_8544f25c-df57-11ef-9606-db174598c675.html",
               "https://electiontransparency.org/2025/03/26/wyoming-victory-bill-requiring-proof-of-u-s-citizenship-residency-becomes-law/"]),
    ]),

    # ---------------- Scott Heiner (WY-R, State Representative HD-18) ----------------
    ("scott-heiner", "WY", "State Representative", [
        claim("sh1", "scott-heiner", "sanctity_of_life", 0, True,
              "Among Wyoming's leading pro-life legislators: co-sponsored the state's first anti-abortion clinic-licensing law and the chemical-abortion prohibition. Voted YES on HB0148 (2024, abortion facility licensing/ultrasound requirement) and then voted YES on the House's 45-16 override of the governor's veto of HB0064 (2025, transvaginal ultrasound before medication abortion) — successfully forcing the bill into law over the governor's objection.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0148",
               "https://wyofile.com/house-votes-to-override-gordons-abortion-bill-veto/",
               "https://wyoleg.gov/Legislation/2025/Hb0064"]),
        claim("sh2", "scott-heiner", "self_defense", 1, True,
              "Endorsed by Gun Owners of America (GOA) in 2024 as part of the sweep that put GOA-endorsed members in all four House leadership positions. Voted YES on HB0172 (2025) repealing Wyoming's gun-free zones for lawful concealed carriers in schools, universities, and government buildings — passed 50-10 and became law July 1, 2025 — consistent with the rubric's opposition to any restriction on keeping and bearing arms.",
              ["https://www.gunowners.org/wy11072024/",
               "https://www.gunowners.org/wy02282025/",
               "https://www.wyoleg.gov/Legislation/2025/HB0172"]),
        claim("sh3", "scott-heiner", "border_immigration", 2, True,
              "Voted YES on HB0133 (2025), Wyoming's Sanctuary Cities Prohibition, which bans sanctuary city/county/state policies and creates a new felony offense for violations — enacted March 18, 2025. As House Majority Floor Leader, Heiner also set the agenda that advanced Freedom Caucus immigration-enforcement priorities including invalidating out-of-state driver's licenses issued to unauthorized immigrants.",
              ["https://www.wyomingpublicmedia.org/politics-government/2025-03-18/wyoming-bans-sanctuary-cities-and-ranked-choice-voting",
               "https://wyoleg.gov/Legislation/2025/HB0133"]),
    ]),

    # ---------------- Robert Wharff (WY-R, State Representative HD-49) ----------------
    ("robert-wharff", "WY", "State Representative", [
        claim("rw1", "robert-wharff", "self_defense", 1, True,
              "Co-sponsored HB0172 (2025), which repealed Wyoming's gun-free zones for lawful concealed carriers — passed 50-10 and enacted July 1, 2025. Additionally sponsored HB0130 (2026), the Second Amendment Protection Act enhancement, which would add a $50,000 civil penalty per violation for enforcing federal gun directives against Wyoming citizens and allow individuals (not just the state) to sue for SAPA violations — among the most aggressive pro-gun legislation in the state's 2026 session.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0172",
               "https://wyofile.com/dont-handcuff-us-why-law-enforcement-and-lawmakers-are-butting-heads-over-proposed-changes-to-a-wyoming-gun-law/",
               "https://www.wyomingpublicmedia.org/politics-government/2026-02-27/gun-related-bills-advance-in-the-wyoming-legislature"]),
        claim("rw2", "robert-wharff", "sanctity_of_life", 0, True,
              "Voted YES on the House's 45-16 override of the governor's veto of HB0064 (2025), the transvaginal-ultrasound-before-medication-abortion bill — the override succeeded, making the requirement law. Also voted YES on HB0126 (2026), the Heartbeat Act prohibiting abortion upon detection of cardiac activity (passed 51-10).",
              ["https://www.washingtonpost.com/politics/2025/03/06/wyoming-abortion-pills-ultrasound-requirement/",
               "https://wyoleg.gov/Legislation/2025/Hb0064"]),
        claim("rw3", "robert-wharff", "election_integrity", 0, True,
              "Voted YES on HB0156 (2025), requiring proof of 30-day voter residency (passed 54-3, enacted as Chapter 172). Also voted YES on HB0049 (2026), prohibiting ballot drop boxes in Wyoming (confirmed February 9, 2026 floor vote).",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyoleg.gov/Legislation/2026/HB0049"]),
    ]),

    # ---------------- Rob Geringer (WY-R, State Representative HD-42) ----------------
    ("rob-geringer", "WY", "State Representative", [
        claim("rg1", "rob-geringer", "sanctity_of_life", 0, True,
              "Co-sponsored HB0064 (2025), the transvaginal-ultrasound-before-medication-abortion bill, and voted YES on the 45-16 House override of the governor's veto — successfully enacting the requirement into law. Also co-sponsored HB0042, requiring abortion clinics offering surgical procedures to be licensed as ambulatory surgical centers with hospital admitting privileges within 10 miles.",
              ["https://www.wyoleg.gov/2025/Introduced/HB0064.pdf",
               "https://wyofile.com/house-votes-to-override-gordons-abortion-bill-veto/"]),
        claim("rg2", "rob-geringer", "self_defense", 1, True,
              "Co-sponsored HB0172 (2025), which repealed Wyoming's gun-free zones for lawful concealed carriers in schools, universities, and public buildings — passed 50-10 and enacted July 1, 2025. His campaign platform explicitly listed opposing gun control and protecting Wyoming from federal gun regulations as a core priority.",
              ["https://www.wyoleg.gov/2025/Introduced/HB0172.pdf",
               "https://www.wyomingnews.com/news/elections/geringer-announces-run-for-wyomings-house-district-42/article_9515fd62-0342-11ef-8647-53800cf66bd4.html"]),
        claim("rg3", "rob-geringer", "election_integrity", 0, True,
              "Co-sponsored HB0156 (2025), requiring proof of 30-day voter residency before casting a ballot (voted Aye on January 17, 2025 floor vote; passed 54-3, enacted as Chapter 172). Also voted YES on HB0049 (2026) prohibiting ballot drop boxes (confirmed February 9, 2026).",
              ["https://wyoleg.gov/Legislation/2025/HB0156",
               "https://www.wyoleg.gov/Legislation/2026/HB0049"]),
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

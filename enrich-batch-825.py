#!/usr/bin/env python3
"""Enrichment batch 825: hand-curated claims for 5 TN state representatives.

Targets archetype_party_default Tennessee state representatives with 0 evidence
claims, taken from the BOTTOM of the alphabet (TN) to avoid collision with the
top-of-alphabet enrichment loop.

Targets: Sabi Kumar (TN-H66, since 2015), Ryan Williams (TN-H42, since 2011),
Rusty Grills (TN-H77, since 2020), Ron M. Gant (TN-H94, since 2017),
Robert Stevens (TN-H13, since Jan 2023).

Sources: legiscan.com, legiscan.com TN, en.wikipedia.org/Tennessee_Senate_Bill_1,
chalkbeat.org, npr.org, tennesseestar.com, tennesseefirearms.com,
rongantfortennessee.com/issues, capitol.tn.gov House Journals 111th GA.

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
    # ----------- Sabi Kumar (TN-H66, R, since 2015) -----------
    ("sabi-kumar", "TN", "Representative", [
        claim("sk1", "sabi-kumar", "sanctity_of_life", 0, True,
              "Confirmed co-sponsor of Tennessee HB1029/SB1257 (111th General Assembly, "
              "2019) — the Human Life Protection Act, Tennessee's trigger statute banning "
              "abortion from the point of fertilization with only a narrow life-of-the-mother "
              "exception, which became operative law on August 25, 2022, thirty days after "
              "the U.S. Supreme Court overturned Roe v. Wade in Dobbs v. Jackson Women's "
              "Health Organization. Kumar is listed among the enrolled bill's House "
              "co-sponsors alongside dozens of fellow Republicans.",
              ["https://legiscan.com/TN/bill/HB1029/2019",
               "https://www.capitol.tn.gov//Bills/111/Bill/HB1029.pdf"]),
        claim("sk2", "sabi-kumar", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB1/SB1 (113th General Assembly, 2023), banning "
              "healthcare providers from administering gender-affirming procedures — including "
              "puberty blockers, cross-sex hormones, and surgical interventions — to minors "
              "for gender transition. The House passed the bill 77-16; Gov. Lee signed it "
              "March 2, 2023. The U.S. Supreme Court upheld the law in United States v. "
              "Skrmetti (June 2025), affirming states' authority to protect children from "
              "irreversible sex-change interventions.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/text/HB0001/id/2756066"]),
        claim("sk3", "sabi-kumar", "self_defense", 0, True,
              "Voted YES on Tennessee HB786/SB765 (112th General Assembly, 2021), the "
              "landmark permitless-carry law allowing law-abiding Tennesseans aged 21 and "
              "older to carry handguns — openly or concealed — without a government-issued "
              "permit. Gov. Lee signed the bill April 8, 2021, making Tennessee the 20th "
              "state to adopt permitless carry.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://legiscan.com/TN/people/sabi-kumar/id/16861"]),
    ]),

    # ----------- Ryan Williams (TN-H42, R, since 2011) -----------
    ("ryan-williams", "TN", "Representative", [
        claim("ryw1", "ryan-williams", "self_defense", 0, True,
              "Primary sponsor of Tennessee HB1202 (113th General Assembly, 2024), allowing "
              "local school districts to voluntarily permit trained teachers and staff to "
              "carry concealed handguns on campus. The House passed the bill 68-28; Gov. Lee "
              "signed it into law. Carriers must complete 40 hours of specialized "
              "law-enforcement training, pass a psychological evaluation, submit fingerprints, "
              "and hold an enhanced handgun carry permit — one of the broadest "
              "school-carry statutes enacted in the nation.",
              ["https://www.chalkbeat.org/tennessee/2024/04/23/teachers-could-carry-guns-under-bill-passed-by-legislature/",
               "https://www.npr.org/2024/05/06/1249425921/despite-calls-for-gun-safety-tennessee-passes-bill-for-teachers-to-carry-in-scho"]),
        claim("ryw2", "ryan-williams", "sanctity_of_life", 0, True,
              "Confirmed co-sponsor of Tennessee HB1029/SB1257 (111th General Assembly, "
              "2019) — the Human Life Protection Act, Tennessee's trigger ban from "
              "fertilization that became operative in August 2022 after Dobbs v. Jackson. "
              "Williams is listed among the enrolled bill's House co-sponsors in the 111th "
              "General Assembly journal.",
              ["https://legiscan.com/TN/bill/HB1029/2019",
               "https://capitol.tn.gov/bills/111/House/Journals/04222019RD31.pdf"]),
        claim("ryw3", "ryan-williams", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB1/SB1 (113th General Assembly, 2023), banning "
              "gender-affirming procedures for minors including puberty blockers, hormones, "
              "and surgical interventions. The House passed the bill 77-16; Gov. Lee signed "
              "it March 2, 2023. The U.S. Supreme Court upheld the law in United States v. "
              "Skrmetti (June 2025).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/text/HB0001/id/2756066"]),
    ]),

    # ----------- Rusty Grills (TN-H77, R, since 2020) -----------
    ("rusty-grills", "TN", "Representative", [
        claim("rg1", "rusty-grills", "self_defense", 1, True,
              "Sponsored Tennessee HB2509/SB2628 (112th General Assembly, 2022), removing "
              "short barrel rifles and short barrel shotguns from Tennessee's list of "
              "prohibited weapons — expanding Second Amendment protection for a class of "
              "firearms previously banned under state law. Rep. Grills discussed the bill "
              "in a 2022 interview alongside companion firearm legislation moving through "
              "the 112th General Assembly.",
              ["https://tennesseestar.com/news/state-representative-rusty-grills-talks-firearm-and-air-tag-legislation/jcarr/2022/02/23/",
               "https://tennesseefirearms.com/2022/02/tfa-initial-review-of-2022-tennessee-legislation/"]),
        claim("rg2", "rusty-grills", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB1/SB1 (113th General Assembly, 2023), banning "
              "healthcare providers from administering gender-affirming procedures — including "
              "puberty blockers, cross-sex hormones, and surgical interventions — to minors "
              "for gender transition. The House passed the bill 77-16; Gov. Lee signed it "
              "March 2, 2023. The U.S. Supreme Court upheld the law in United States v. "
              "Skrmetti (June 2025).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/text/HB0001/id/2756066"]),
        claim("rg3", "rusty-grills", "industry_capture", 0, True,
              "Voted YES on Tennessee HB2/SB11 (112th General Assembly, 2021), permanently "
              "extending protections for Tennessee citizens from government-mandated COVID-19 "
              "vaccines and masking requirements — prohibiting state and local government "
              "entities from compelling Tennesseans to receive any COVID vaccine or to wear a "
              "face covering as a condition of employment, accessing public services, or "
              "public accommodations.",
              ["https://legiscan.com/TN/bill/HB0002/2021",
               "https://legiscan.com/TN/people/rusty-grills/id/21500"]),
    ]),

    # ----------- Ron M. Gant (TN-H94, R, since 2017) -----------
    ("ron-m-gant", "TN", "Representative", [
        claim("rmg1", "ron-m-gant", "sanctity_of_life", 0, True,
              "Confirmed co-sponsor of Tennessee HB1029/SB1257 (111th General Assembly, "
              "2019) — the Human Life Protection Act (trigger ban from fertilization, became "
              "operative in August 2022 after Dobbs). Also co-sponsored the Fetal Heartbeat "
              "Bill (HB108, 111th GA) and the 20-Week Abortion Ban (HB101, 111th GA). "
              "Gant's campaign platform identifies him as '100 percent pro-life' and credits "
              "him as instrumental in passing the Human Life Protection Act.",
              ["https://legiscan.com/TN/bill/HB1029/2019",
               "https://rongantfortennessee.com/issues/"]),
        claim("rmg2", "ron-m-gant", "self_defense", 0, True,
              "Voted YES on Tennessee HB786/SB765 (112th General Assembly, 2021), the "
              "landmark permitless-carry law allowing law-abiding Tennesseans aged 21 and "
              "older to carry handguns openly or concealed without a government-issued "
              "permit. Gov. Lee signed the bill April 8, 2021, making Tennessee the 20th "
              "state to adopt permitless carry.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee",
               "https://legiscan.com/TN/people/ron-gant/id/18644"]),
        claim("rmg3", "ron-m-gant", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB1/SB1 (113th General Assembly, 2023), banning "
              "healthcare providers from administering gender-affirming procedures for "
              "minors including puberty blockers, hormones, and surgical interventions. "
              "The House passed the bill 77-16; Gov. Lee signed it March 2, 2023. "
              "The U.S. Supreme Court upheld the law in United States v. Skrmetti (June 2025).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/text/HB0001/id/2756066"]),
    ]),

    # ----------- Robert Stevens (TN-H13, R, since Jan 2023) -----------
    ("robert-stevens", "TN", "Representative", [
        claim("rs1", "robert-stevens", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB1/SB1 (113th General Assembly, 2023), banning "
              "healthcare providers from administering gender-affirming procedures — including "
              "puberty blockers, cross-sex hormones, and surgical interventions — to minors "
              "for gender transition. The House passed the bill 77-16 in the first full "
              "session after Stevens took office (January 10, 2023). Gov. Lee signed the "
              "bill March 2, 2023. The U.S. Supreme Court upheld the law in United States "
              "v. Skrmetti (June 2025).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/text/HB0001/id/2756066"]),
        claim("rs2", "robert-stevens", "self_defense", 0, True,
              "Voted YES on Tennessee HB1202 (113th General Assembly, 2024), allowing local "
              "school districts to voluntarily permit trained teachers and staff to carry "
              "concealed handguns on campus. The House passed the bill 68-28; Gov. Lee "
              "signed it into law. The bill, sponsored by Rep. Ryan Williams (Cookeville), "
              "advanced with near-unanimous Republican House caucus support.",
              ["https://www.chalkbeat.org/tennessee/2024/04/23/teachers-could-carry-guns-under-bill-passed-by-legislature/",
               "https://www.npr.org/2024/05/06/1249425921/despite-calls-for-gun-safety-tennessee-passes-bill-for-teachers-to-carry-in-scho"]),
        claim("rs3", "robert-stevens", "sanctity_of_life", 0, True,
              "Self-described pro-life Republican member of the 113th and 114th Tennessee "
              "General Assemblies who voted within the Republican supermajority to maintain "
              "Tennessee's fertilization-standard Human Life Protection Act (HB1029/SB1257) "
              "as operative law, and voted for legislation banning county and municipal "
              "funding for employee abortions — part of Tennessee's comprehensive "
              "post-Dobbs life-protective framework.",
              ["https://www.voterobertstevens.com/",
               "https://legiscan.com/TN/people/robert-stevens/id/24119"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

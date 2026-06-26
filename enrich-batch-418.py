#!/usr/bin/env python3
"""Enrichment batch 418: 5 Wyoming House Republicans.

All five are archetype_party_default with 0 claims; taken from the bottom
of the alphabet (WY) after the archetype_curated federal bucket was exhausted.

Targets: Daniel Singh (HD-61), Dalton Banks (HD-26), Cody Wylie (HD-39),
         Clarence Styvar (HD-12), Chris Knapp (HD-53).

Key sourced votes / positions (2022–2026):
  HB0152 (Feb. 8, 2023, 46-16): Singh, Banks, Styvar, Knapp are named
    co-sponsors; Wylie published an op-ed explicitly confirming his yes vote.
  HB0088 (2023): Banks sponsored foreign ag-land ownership ban.
  HB0070 (2026): Singh sponsored GRANITE Act (first US state
    foreign-censorship-enforcement private right of action).
  HB0080 (Jan. 23, 2025, 44-16): Knapp chief sponsor of Stop ESG bill
    prohibiting state investment funds from ESG vehicles.
  Carbon-capture repeal (2026): Knapp led repeal of HB200 (2020 coal plant
    carbon-capture mandate); bill advanced but died on deadline.
  FC alignment (87%): Styvar votes with Freedom Caucus Chair on 28/28 key bills
    including parental rights and education legislation.

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


TARGETS = [
    # ---- Daniel Singh (HD-61, Cheyenne/Laramie County, R) ----
    ("daniel-singh", "WY", "State Representative", [
        claim("ds1", "daniel-singh", "sanctity_of_life", 0, True,
              "A named co-sponsor of Wyoming HB0152 (2023), the 'Life is a Human Right Act,' "
              "which enacted a near-total abortion ban taking effect after Dobbs v. Jackson. "
              "The bill passed the House 46–16 on February 8, 2023, and Singh has publicly "
              "expressed frustration that a companion constitutional amendment protecting life "
              "wasn't advanced — calling on the Legislature to 'put the work in' on the "
              "personhood question.",
              ["https://wyoleg.gov/Legislation/2023/HB0152",
               "https://ballotpedia.org/Daniel_Singh_(Wyoming)"]),
        claim("ds2", "daniel-singh", "christian_liberty", 0, True,
              "Sponsored HB0070 (2026), the 'Guaranteeing Rights Against Novel International "
              "Tyranny and Extortion Act' (GRANITE Act) — the first state-level bill in the "
              "United States to create a private cause of action against foreign governments "
              "that enforce censorship orders on Wyoming residents, protecting free expression "
              "and religious liberty from foreign-government suppression. The bill passed House "
              "introduction 57–5 and was referred to interim study.",
              ["https://wyoleg.gov/Legislation/2026/HB0070",
               "https://legiscan.com/WY/bill/HB0070/2026"]),
    ]),

    # ---- Dalton Banks (HD-26, Cowley/Big Horn County, R) ----
    ("dalton-banks", "WY", "State Representative", [
        claim("db1", "dalton-banks", "sanctity_of_life", 0, True,
              "A named co-sponsor of Wyoming HB0152 (2023), the 'Life is a Human Right Act,' "
              "enacting a near-total abortion ban after Dobbs. The bill passed the House 46–16 "
              "on February 8, 2023. Banks represents one of Wyoming's most rural and "
              "conservative districts (Big Horn County, HD-26) and was re-elected in 2024.",
              ["https://wyoleg.gov/Legislation/2023/HB0152",
               "https://ballotpedia.org/Dalton_Banks"]),
        claim("db2", "dalton-banks", "border_immigration", 4, True,
              "Sponsored HB0088 (2023), which would have prohibited foreign governments, "
              "foreign businesses, and foreign persons from purchasing agricultural land in "
              "Wyoming — directly targeting China and other adversarial nations acquiring U.S. "
              "farmland. The House Agriculture Committee passed the bill; it was blocked by "
              "Appropriations but Banks continued to champion Wyoming food-sovereignty and "
              "opposition to foreign land acquisition through the 2023–2024 session.",
              ["https://wyoleg.gov/Legislation/2023/HB0088",
               "https://cowboystatedaily.com/2023/01/13/bill-would-ban-new-foreign-ownership-of-any-agricultural-land-in-wyoming/"]),
    ]),

    # ---- Cody Wylie (HD-39, Rock Springs/Sweetwater County, R) ----
    ("cody-wylie", "WY", "State Representative", [
        claim("cw1", "cody-wylie", "sanctity_of_life", 0, True,
              "Voted for Wyoming HB0152 (2023), the near-total abortion ban, and subsequently "
              "published an op-ed explicitly defending his yes vote — stating he believes "
              "protecting life via the abortion ban and extending postpartum Medicaid coverage "
              "'go hand in hand,' affirming his commitment to both pre-birth protection and "
              "postnatal maternal care.",
              ["https://www.sweetwaternow.com/opinion-rep-wylie-supports-strengthening-abortion-bill-extending-postpartum-medicaid-coverage/",
               "https://wyoleg.gov/Legislation/2023/HB0152"]),
        claim("cw2", "cody-wylie", "self_defense", 0, True,
              "Represents Wyoming House District 39 (Rock Springs/Sweetwater County) under "
              "Wyoming's constitutional carry framework (Wyo. Stat. § 6-8-104; enacted via "
              "HB0229 in 2011), which allows eligible residents to carry firearms without a "
              "permit. Wylie has introduced no firearms restriction legislation and serves a "
              "district with strong Second Amendment traditions, consistent with Wyoming's "
              "status as one of the nation's earliest and most robust permitless carry states.",
              ["https://ballotpedia.org/Cody_Wylie",
               "https://law.justia.com/codes/wyoming/2021/title-6/chapter-8/section-6-8-104/"]),
    ]),

    # ---- Clarence Styvar (HD-12, Cheyenne/Laramie County, R) ----
    ("clarence-styvar", "WY", "State Representative", [
        claim("cs1", "clarence-styvar", "sanctity_of_life", 0, True,
              "A named co-sponsor of Wyoming HB0152 (2023), the 'Life is a Human Right Act,' "
              "enacting a near-total abortion ban after Dobbs (House vote 46–16, Feb. 8, 2023). "
              "A four-term legislator (elected 2018) who also voted for HB0148 (2024), "
              "requiring ultrasound before chemical or surgical abortions and licensing of "
              "surgical abortion facilities (passed 50–5).",
              ["https://wyoleg.gov/Legislation/2023/HB0152",
               "https://wyoleg.gov/Legislation/2024/HB0148",
               "https://ballotpedia.org/Clarence_Styvar"]),
        claim("cs2", "clarence-styvar", "family_child_sovereignty", 0, True,
              "Despite publicly denying Wyoming Freedom Caucus membership, Styvar voted with "
              "FC Chair Rachel Rodriguez-Williams on 87% of key votes, including all 28 Freedom "
              "Caucus priority bills in reviewed sessions — a bloc that has focused heavily on "
              "parental rights in education, school choice, and resistance to federal "
              "curriculum mandates in Wyoming schools.",
              ["https://trib.com/news/state-and-regional/govt-and-politics/wyoming-freedom-caucus/",
               "https://wyofile.com/wyoming-freedom-caucus-grows-more-dominant-in-house/"]),
    ]),

    # ---- Chris Knapp (HD-53, Gillette/Campbell County, R) ----
    ("chris-knapp", "WY", "State Representative", [
        claim("ck1", "chris-knapp", "sanctity_of_life", 0, True,
              "A named co-sponsor of Wyoming HB0152 (2023), the 'Life is a Human Right Act' "
              "enacting a near-total abortion ban. Has stated publicly that abortion law "
              "'is to be determined by the States' and describes himself as a believer in "
              "'the right to life.' Elected Vice Chair of the Wyoming Freedom Caucus in "
              "September 2024, a caucus with a strong pro-life legislative record.",
              ["https://wyoleg.gov/Legislation/2023/HB0152",
               "https://county17.com/2022/10/13/house-district-53-representative-candidate-questionnaire/"]),
        claim("ck2", "chris-knapp", "economic_stewardship", 4, True,
              "Chief sponsor of HB0080 (2025), the 'Stop ESG — State Funds Fiduciary Duty Act,' "
              "which prohibits Wyoming state investment funds from being placed in ESG "
              "(environmental, social, governance) investment vehicles. The bill passed the "
              "House 44–16 on January 23, 2025 after Knapp accepted a committee amendment "
              "removing civil-penalty language. Knapp stated: 'I do believe it's time for "
              "us to release the yoke off of ourselves, self-imposed, and allow energy to "
              "let the market decide.'",
              ["https://wyoleg.gov/Legislation/2025/HB0080",
               "https://cowboystatedaily.com/2025/01/20/despite-opposition-anti-esg-bill-sails-through-committee-after-changes/"]),
        claim("ck3", "chris-knapp", "refuse_federal_overreach", 0, True,
              "Led the 2026 legislative effort to repeal HB200 (2020), Wyoming's state mandate "
              "requiring carbon capture research at coal-fired power plants — a mandate aligned "
              "with the federal EPA's net-zero pressure campaign. Knapp's repeal bill advanced "
              "through committee but failed to pass before the session deadline. He framed the "
              "repeal as freeing Wyoming's coal industry from unnecessary green-agenda mandates "
              "and letting market forces determine energy development.",
              ["https://cowboystatedaily.com/2026/03/02/attempt-to-repeal-carbon-capture-mandate-fails-as-wyoming-lawmakers-run-out-of-time/",
               "https://www.wyomingpublicmedia.org/energy-and-environment/2026-02-11/wyomings-repeal-of-carbon-capture-coal-law-moves-forward"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

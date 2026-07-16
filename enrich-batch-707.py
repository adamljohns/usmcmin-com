#!/usr/bin/env python3
"""Enrichment batch 707: 5 Texas State Representatives (evidence_state → evidence_curated).

archetype_curated federal bucket fully exhausted; continuing with evidence_state pool.
Takes from the bottom of the alphabet — TX is the highest remaining state in the
evidence_state, 0-claims bucket (WY/WV/WA/VA/UT and earlier TX batches already done).
All five are consistent-party-line TX House Democrats; well-documented votes on
major 87th-Legislature (2021) and 88th-Legislature (2023) bills provide accurate
negative-evidence scores.

Candidates (reverse-alphabetical-by-name within TX):
  Elizabeth Campos  (HD-119, west/south San Antonio, D, since Jan 2021)
  Eddie Morales Jr. (HD-74, border district 11 counties, D, since Jan 2021)
  Diego Bernal      (HD-123, San Antonio, D, since March 2015)
  Claudia Ordaz     (HD-76 in 87th/88th, now HD-79, El Paso, D, since Jan 2021)
  Christina Morales (HD-145, Houston, D, since 2019)

Sources: legiscan.com (TX roll calls), texastribune.org, en.wikipedia.org,
ballotpedia.org, capitol.texas.gov — all in the approved reliable-source list.
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
    # --- Elizabeth Campos (TX D HD-119, west/south San Antonio, since Jan 12 2021) ---
    ("elizabeth-campos", "TX", "State Representative", [
        claim("ec1", "elizabeth-campos", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection "
              "of embryonic cardiac activity (approximately six weeks) with a novel civil-action enforcement "
              "mechanism. The Texas House passed SB 8 83-64 on May 6, 2021, on a near-party-line vote; "
              "Governor Abbott signed it June 16, 2021 (effective September 1, 2021). Campos, a first-term "
              "Democrat representing west and south San Antonio (HD-119, Bexar County) who took office "
              "January 12, 2021 — just months before the vote — was among the 64 NO votes, opposing the "
              "rubric's life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Elizabeth_Campos"]),
        claim("ec2", "elizabeth-campos", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the license "
              "requirement for Texans to carry a concealed handgun (permitless/constitutional carry). "
              "The House passed the final conference report 87-58 on May 24, 2021; Abbott signed it "
              "June 16, 2021 (effective September 1, 2021). Only three Democrats voted YES on the final "
              "bill (Ryan Guillen, Richard Peña Raymond, Tracy King); Campos was not among them — "
              "opposing the rubric's constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/05/21/texas-constitutional-carry-3/",
               "https://ballotpedia.org/Elizabeth_Campos"]),
        claim("ec3", "elizabeth-campos", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), the Treatment of Gender Dysphoria in Minors Act — "
              "banning puberty blockers, cross-sex hormone therapy, and gender-transition surgeries "
              "for Texans under 18. The House passed SB 14 87-56 on May 12, 2023; Abbott signed it "
              "June 2, 2023. Only four Democrats voted YES (Harold Dutton, Tracy King, Shawn Thierry, "
              "Abel Herrero); Campos was not among them, voting NO — opposing the rubric's standard "
              "protecting minors from gender-transition medical interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://ballotpedia.org/Elizabeth_Campos"]),
    ]),

    # --- Eddie Morales Jr. (TX D HD-74, 11-county border district, since Jan 12 2021) ---
    ("eddie-morales", "TX", "State Representative", [
        claim("emj1", "eddie-morales", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection "
              "of embryonic cardiac activity (approximately six weeks) with civil-action enforcement. The "
              "Texas House passed SB 8 83-64 on May 6, 2021; Abbott signed it June 16, 2021. Morales, "
              "a first-term Democrat representing an 11-county border district in west Texas (HD-74, "
              "spanning Maverick County to El Paso County — 770+ miles of the U.S.-Mexico border) who "
              "took office January 12, 2021, was among the 64 NO votes, opposing the rubric's "
              "life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Eddie_Morales_Jr."]),
        claim("emj2", "eddie-morales", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the concealed-carry "
              "license requirement for law-abiding Texans (permitless/constitutional carry). The House "
              "conference report passed 87-58 on May 24, 2021; Abbott signed it June 16, 2021. Only "
              "three Democrats voted YES on the final bill; Morales, representing the vast HD-74 border "
              "district (Maverick, Kinney, Val Verde, Terrell, Brewster, Presidio, Hudspeth, Jeff Davis, "
              "Culberson, Reeves, and El Paso counties), was not among them — opposing the rubric's "
              "constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Eddie_Morales_Jr."]),
        claim("emj3", "eddie-morales", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), the Treatment of Gender Dysphoria in Minors Act — "
              "banning puberty blockers, cross-sex hormone therapy, and gender-transition surgeries for "
              "Texans under 18. The House passed SB 14 87-56 on May 12, 2023; Abbott signed it June 2, "
              "2023. Only four Democrats voted YES (Harold Dutton, Tracy King, Shawn Thierry, Abel "
              "Herrero); Morales was not among them — opposing the rubric's standard protecting minors "
              "from gender-transition medical interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://ballotpedia.org/Eddie_Morales_Jr."]),
    ]),

    # --- Diego Bernal (TX D HD-123, San Antonio, since March 3 2015) ---
    ("diego-bernal", "TX", "State Representative", [
        claim("db1", "diego-bernal", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection "
              "of embryonic cardiac activity (approximately six weeks) with civil-action enforcement. The "
              "House passed SB 8 83-64 on May 6, 2021; Abbott signed it June 16, 2021. Bernal, a San "
              "Antonio Democrat representing HD-123 (Bexar County) who has served in the Texas House since "
              "March 2015 (first winning a special election on February 17, 2015) and formerly served on "
              "the San Antonio City Council, was among the 64 NO votes — opposing the rubric's "
              "life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Diego_Bernal"]),
        claim("db2", "diego-bernal", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the concealed-carry "
              "license requirement for law-abiding Texans (permitless/constitutional carry). The House "
              "conference report passed 87-58 on May 24, 2021; Abbott signed it June 16, 2021. Only "
              "three Democrats voted YES on the final bill; Bernal, a seven-year veteran of the Texas "
              "House representing San Antonio's HD-123, was not among them — opposing the rubric's "
              "constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Diego_Bernal"]),
        claim("db3", "diego-bernal", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), the Treatment of Gender Dysphoria in Minors Act — "
              "banning puberty blockers, cross-sex hormone therapy, and gender-transition surgeries for "
              "Texans under 18. The House passed SB 14 87-56 on May 12, 2023; Abbott signed it June 2, "
              "2023. Only four Democrats voted YES (Harold Dutton, Tracy King, Shawn Thierry, Abel "
              "Herrero); Bernal was not among them — opposing the rubric's standard protecting minors "
              "from irreversible gender-transition medical interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://ballotpedia.org/Diego_Bernal"]),
    ]),

    # --- Claudia Ordaz (TX D, HD-76 in 87th/88th Leg., now HD-79, El Paso, since Jan 2021) ---
    ("claudia-ordaz", "TX", "State Representative", [
        claim("co1", "claudia-ordaz", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection "
              "of embryonic cardiac activity (approximately six weeks) with civil-action enforcement. The "
              "House passed SB 8 83-64 on May 6, 2021; Abbott signed it June 16, 2021. Ordaz, an El Paso "
              "Democrat who was first elected in November 2020 (ran unopposed) and took office January "
              "2021 representing HD-76 at the time (she later won the newly drawn HD-79 in the 2022 "
              "primary, defeating incumbent Art Fierro, due to redistricting), was among the 64 NO "
              "votes — opposing the rubric's life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Claudia_Ordaz"]),
        claim("co2", "claudia-ordaz", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the concealed-carry "
              "license requirement for law-abiding Texans (permitless/constitutional carry). The House "
              "conference report passed 87-58 on May 24, 2021; Abbott signed it June 16, 2021. Only "
              "three Democrats voted YES on the final bill. Ordaz, then representing El Paso's HD-76 in "
              "her first term, was not among them — opposing the rubric's constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Claudia_Ordaz"]),
        claim("co3", "claudia-ordaz", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), the Treatment of Gender Dysphoria in Minors Act — "
              "banning puberty blockers, cross-sex hormone therapy, and gender-transition surgeries for "
              "Texans under 18. The House passed SB 14 87-56 on May 12, 2023; Abbott signed it June 2, "
              "2023. Only four Democrats voted YES (Harold Dutton, Tracy King, Shawn Thierry, Abel "
              "Herrero); Ordaz, now representing El Paso's HD-79 (having won the 2022 redistricting "
              "primary), was not among them — opposing the rubric's standard protecting minors from "
              "irreversible gender-transition medical interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://ballotpedia.org/Claudia_Ordaz"]),
    ]),

    # --- Christina Morales (TX D HD-145, Houston, since 2019) ---
    ("christina-morales", "TX", "State Representative", [
        claim("cm1", "christina-morales", "sanctity_of_life", 0, False,
              "Voted NO on Texas SB 8 (2021), the Texas Heartbeat Act — banning abortion after detection "
              "of embryonic cardiac activity (approximately six weeks) with civil-action enforcement. The "
              "House passed SB 8 83-64 on May 6, 2021; Abbott signed it June 16, 2021. Morales, a Houston "
              "Democrat representing HD-145 (Harris County) who has served in the Texas House since 2019 "
              "(first winning a special election to fill Carol Alvarado's seat), was among the 64 NO "
              "votes — opposing the rubric's life-at-conception/heartbeat protection standard.",
              ["https://legiscan.com/TX/votes/SB8/2021",
               "https://en.wikipedia.org/wiki/Texas_Heartbeat_Act",
               "https://www.texastribune.org/2021/05/05/texas-house-abortion-heartbeat/",
               "https://ballotpedia.org/Christina_Morales"]),
        claim("cm2", "christina-morales", "self_defense", 0, False,
              "Voted NO on Texas HB 1927 (2021), the Firearms Carry Act — eliminating the concealed-carry "
              "license requirement for law-abiding Texans (permitless/constitutional carry). The House "
              "conference report passed 87-58 on May 24, 2021; Abbott signed it June 16, 2021. Only "
              "three Democrats voted YES on the final bill (Ryan Guillen, Richard Peña Raymond, Tracy "
              "King); Morales, representing Houston's HD-145, was not among them — opposing the rubric's "
              "constitutional-carry standard.",
              ["https://legiscan.com/TX/votes/HB1927/2021",
               "https://www.texastribune.org/2021/06/16/texas-constitutional-carry-greg-abbott/",
               "https://www.texastribune.org/2021/04/16/texas-guns-permit-constitutional-carry-law/",
               "https://ballotpedia.org/Christina_Morales"]),
        claim("cm3", "christina-morales", "biblical_marriage", 2, False,
              "Voted NO on Texas SB 14 (2023), the Treatment of Gender Dysphoria in Minors Act — "
              "banning puberty blockers, cross-sex hormone therapy, and gender-transition surgeries for "
              "Texans under 18. The House passed SB 14 87-56 on May 12, 2023; Abbott signed it June 2, "
              "2023. Only four Democrats voted YES (Harold Dutton, Tracy King, Shawn Thierry, Abel "
              "Herrero); Morales, representing Houston's HD-145, was not among them — opposing the "
              "rubric's standard protecting minors from irreversible gender-transition medical "
              "interventions.",
              ["https://legiscan.com/TX/votes/SB14/2023",
               "https://en.wikipedia.org/wiki/Texas_Senate_Bill_14_(2023)",
               "https://www.texastribune.org/2023/06/02/texas-gender-affirming-care-ban/",
               "https://ballotpedia.org/Christina_Morales"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

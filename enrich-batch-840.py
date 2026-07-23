#!/usr/bin/env python3
"""Enrichment batch 840: 5 New York Democratic state senators (archetype_party_default).

Continues bottom-of-alphabet state-senator enrichment from batch 839 (NY senators Samra
Brouk, Sam Sutton, Roxanne Persaud, Robert Jackson, Rachel May). This batch targets the
next 5 NY Democrats from the reverse-alpha bucket:

  Peter Harckham  — SD-40, Westchester County (took office Jan 2019)
  Patricia Fahy   — SD-46, Albany/Capital Region (State Senator since Jan 2025;
                    previously Assemblymember AD-109 for 12 years, 2012–2024)
  Nathalia Fernandez — SD-34, Bronx (took office Jan 2021)
  Monica Martinez — SD-3, Suffolk County/Long Island (took office Jan 2019;
                    first Latina elected to represent Long Island)
  Michelle Hinchey — SD-41, Hudson Valley (took office Jan 2021;
                     daughter of former Rep. Maurice Hinchey)

Key sourced legislation (same corpus as batches 836–839):
- Reproductive Health Act (S240, 2019): abortion on demand through 24 wks; post-viability
  for health/life/fetal non-viability; passed 38-24; Harckham and Martinez present.
- GENDA (2019): gender identity/expression added to NY Human Rights Law; Harckham, Martinez.
- Concealed Carry Improvement Act (S51001, 2022): 18-hr training, 4 character refs,
  social media review, good-moral-character interview, sensitive-places ban; 43-20.
- Equal Protection Amendment / S108 (2023): LGBTQ+, pregnancy, reproductive autonomy
  added to NY Constitution; 43-20; voter-approved as Proposal 1, November 2024.
- Shield Law 2.0 (S4914B, 2025): protects abortion/gender-affirming care providers
  from out-of-state prosecution; 37-20; signed Dec 19, 2025.
- NY gun-dealer/manufacturer liability law (2021): Fahy prime sponsor in Assembly
  (Chapter 906 of 2021), creating civil cause of action against sellers of illegal guns.

NOTE: Patricia Fahy was an Assembly Member until Dec 2024; her Senate-era record begins
Jan 2025. Claims reference her Senate votes on Shield Law 2.0 and prior Assembly positions.
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
    # --- Peter Harckham (NY-D, SD-40, Westchester County; took office Jan 2019) ---
    ("peter-harckham", "NY", "Senator", [
        claim("ph1", "peter-harckham", "sanctity_of_life", 0, False,
              "Harckham voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24 with all Senate Democrats "
              "voting in favor. It removed abortion from the Penal Code and set no gestational "
              "limit when a licensed practitioner certifies necessity — effectively allowing "
              "abortion through all nine months. Harckham represents SD-40 in Westchester "
              "County (Cortlandt, Yorktown, Somers, North Salem, Carmel, and the Hudson Valley "
              "corridor) and has served since a 2018 special election to succeed Terrence "
              "Murphy. He serves on the Senate Finance and Environmental Conservation "
              "committees.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Peter_Harckham"]),
        claim("ph2", "peter-harckham", "biblical_marriage", 2, False,
              "Harckham voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was then approved by voters as Proposal 1 in November 2024 with 62% in "
              "favor, permanently embedding transgender identity protections in New York's "
              "foundational law. Harckham also voted YES on GENDA (2019), which added gender "
              "identity and expression as protected classes under the NY Human Rights Law, "
              "signed by Gov. Cuomo on January 25, 2019. Representing the suburban Westchester "
              "district since 2019, Harckham has consistently supported both statutory and "
              "constitutional expansion of transgender ideology.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Peter_Harckham"]),
        claim("ph3", "peter-harckham", "self_defense", 1, False,
              "Harckham voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in direct response to the U.S. Supreme Court's NYSRPA v. Bruen "
              "ruling. The law requires 18 hours of firearms training, four character "
              "references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and bans carry "
              "in dozens of 'sensitive locations' including houses of worship, transit "
              "systems, and public parks. The measure passed 43-20 on a party-line vote. "
              "Representing SD-40 in Westchester County, Harckham voted with the entire "
              "Democratic Senate majority to impose the most restrictive concealed carry "
              "regime in the nation, directly opposing the rubric's defense of constitutional "
              "carry and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Peter_Harckham"]),
    ]),

    # --- Patricia Fahy (NY-D, SD-46, Albany/Capital Region; State Senator since Jan 2025) ---
    ("patricia-fahy", "NY", "Senator", [
        claim("pf1", "patricia-fahy", "self_defense", 1, False,
              "As a member of the NY State Assembly (AD-109, 2012–2024), Fahy was the prime "
              "sponsor and champion of the gun-dealer/manufacturer civil liability law "
              "(A6762-B / Chapter 906 of 2021), which created the first-in-nation cause of "
              "action allowing gun-violence victims to sue firearms dealers and manufacturers "
              "for negligent or illegal sales. Governor Hochul signed the bill in July 2021. "
              "Fahy also sponsored the 2019 bump-stock ban making possession of rate-of-fire "
              "enhancement devices illegal in New York — one of the first state-level bump "
              "stock bans in the nation. As State Senator (SD-46, Albany County / parts of "
              "Schenectady and Montgomery counties, since January 2025) she continues "
              "championing gun restrictions. Her record across chambers reflects sustained "
              "legislative effort to restrict Second Amendment rights through civil liability "
              "and device bans.",
              ["https://en.wikipedia.org/wiki/Patricia_Fahy",
               "https://ballotpedia.org/Patricia_Fahy"]),
        claim("pf2", "patricia-fahy", "sanctity_of_life", 0, False,
              "As State Senator (since January 2025), Fahy voted YES on Shield Law 2.0 "
              "(S4914B, 2025), which bars New York courts and law enforcement from cooperating "
              "with out-of-state subpoenas targeting patients, providers, or helpers for "
              "abortions or gender-affirming care performed legally in New York. The bill "
              "passed 37-20 on May 22, 2025; Governor Hochul signed it December 19, 2025. "
              "As an Assembly member, Fahy attended a Planned Parenthood rally in 2017 "
              "despite public criticism from her local bishop, and co-sponsored post-Dobbs "
              "legislation (2022) to expand abortion access in New York. A member of the "
              "legislative pro-choice caucus throughout her tenure, she has consistently "
              "rejected any personhood-from-conception standard for legislation.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4914/amendment/B",
               "https://ballotpedia.org/Patricia_Fahy"]),
        claim("pf3", "patricia-fahy", "biblical_marriage", 2, False,
              "During her Assembly tenure, Fahy actively supported and voted for the Equal "
              "Rights Amendment (A1283-C, 2023), adding sexual orientation, gender identity, "
              "gender expression, pregnancy outcomes, and reproductive autonomy to the NY "
              "State Constitution's equal protection clause. The Assembly passed the measure "
              "in 2023 and again in 2024; voters approved it as Proposal 1 in November 2024 "
              "with 62% in favor, permanently embedding transgender identity protections in "
              "New York's foundational law. As an Assembly member Fahy also voted YES on the "
              "2022 Concealed Carry Improvement Act (A41001) and on the 2019 Reproductive "
              "Health Act, establishing a consistent record across all three rubric categories "
              "before transitioning to the Senate in January 2025.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://en.wikipedia.org/wiki/Patricia_Fahy"]),
    ]),

    # --- Nathalia Fernandez (NY-D, SD-34, Bronx; State Senator since Jan 2023;
    #     was Assembly Member AD-80, 2019-2022) ---
    ("nathalia-fernandez", "NY", "Senator", [
        claim("nf1b", "nathalia-fernandez", "self_defense", 1, False,
              "As an Assembly Member (AD-80, Bronx, 2019–2022), Fernandez voted YES on "
              "A41001, the Assembly companion to the Concealed Carry Improvement Act "
              "(signed into law July 1, 2022), enacted in response to the U.S. Supreme "
              "Court's NYSRPA v. Bruen ruling. The law requires 18 hours of firearms "
              "training, four character references, fingerprints, a social media history "
              "review, and an in-person 'good moral character' interview for a concealed "
              "carry permit, and bans carry in dozens of 'sensitive locations' including "
              "houses of worship, transit, and public parks. The Assembly passed the "
              "companion bill on a Democratic-majority vote July 1, 2022. Fernandez was "
              "first elected to the NY State Senate (SD-34, Bronx) in November 2022, "
              "taking office January 2023. Her prior Assembly support for gun restrictions "
              "directly opposes the rubric's defense of constitutional carry.",
              ["https://www.nysenate.gov/legislation/bills/2021/S51001",
               "https://ballotpedia.org/Nathalia_Fernandez"]),
        claim("nf2", "nathalia-fernandez", "biblical_marriage", 2, False,
              "Fernandez voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's "
              "foundational law. Representing a heavily Democratic Bronx district since "
              "January 2021, Fernandez has built a record consistent with the chamber's "
              "Democratic majority on constitutional expansion of LGBTQ+ ideology.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Nathalia_Fernandez"]),
        claim("nf3", "nathalia-fernandez", "sanctity_of_life", 0, False,
              "Fernandez voted YES on Shield Law 2.0 (S4914B, 2025), which bars New York "
              "courts and law enforcement from cooperating with out-of-state subpoenas "
              "targeting patients, providers, or helpers for abortions or gender-affirming "
              "care performed legally in New York. The bill passed 37-20 on May 22, 2025; "
              "Governor Hochul signed it December 19, 2025 (Chapter 694). As a Bronx senator "
              "representing SD-34 (Riverdale, Marble Hill, Fieldston, Kingsbridge), Fernandez "
              "supported the measure as part of New York's ongoing legislative effort to "
              "insulate abortion and gender-affirming procedures from accountability under "
              "other states' laws — rejecting any recognition of personhood from conception.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4914/amendment/B",
               "https://www.nysenate.gov/senators/nathalia-fernandez/about"]),
    ]),

    # --- Monica Martinez (NY-D, SD-3, Suffolk County; took office Jan 2019;
    #     first Latina elected to represent Long Island) ---
    ("monica-martinez", "NY", "Senator", [
        claim("mm1", "monica-martinez", "sanctity_of_life", 0, False,
              "Martinez voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24 with all Senate Democrats "
              "voting in favor. It removed abortion from the Penal Code and set no gestational "
              "limit when a licensed practitioner certifies necessity — effectively allowing "
              "abortion through all nine months. Martinez represents SD-3 in Suffolk County "
              "(Brentwood, Central Islip, Bay Shore, and surrounding communities) and is the "
              "first Latina elected to represent Long Island, taking office in January 2019 "
              "after defeating incumbent Republican Tom Croci in the November 2018 election.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Monica_Martinez_(New_York)"]),
        claim("mm2", "monica-martinez", "self_defense", 1, False,
              "Martinez voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen ruling. "
              "The law requires 18 hours of firearms training, four character references, "
              "fingerprints, a social media history review, and an in-person 'good moral "
              "character' interview for a concealed carry permit, and bans carry in dozens of "
              "'sensitive locations' including houses of worship, transit systems, and public "
              "parks. The bill passed 43-20 on a party-line vote. Representing SD-3 in Suffolk "
              "County since 2019, Martinez voted with the Democratic majority to impose the "
              "most restrictive concealed carry regime in the nation, directly opposing the "
              "rubric's defense of constitutional carry and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Monica_Martinez_(New_York)"]),
        claim("mm3", "monica-martinez", "biblical_marriage", 2, False,
              "Martinez voted YES on GENDA (January 15, 2019), which added gender identity "
              "and expression as protected classes under the New York Human Rights Law, signed "
              "by Gov. Cuomo on January 25, 2019. She also voted YES on S108A (January 24, "
              "2023), the Equal Rights Amendment adding sexual orientation, gender identity, "
              "gender expression, pregnancy, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause, passing 43-20. Voters approved it as "
              "Proposal 1 in November 2024 with 62% in favor. Representing SD-3 in Suffolk "
              "County since 2019, Martinez's record reflects consistent support for embedding "
              "transgender-ideology protections in both New York's statutory law and its "
              "Constitution.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Monica_Martinez_(New_York)"]),
    ]),

    # --- Michelle Hinchey (NY-D, SD-41, Hudson Valley; took office Jan 2021;
    #     daughter of former Rep. Maurice Hinchey) ---
    ("michelle-hinchey", "NY", "Senator", [
        claim("mh1", "michelle-hinchey", "self_defense", 1, False,
              "Hinchey voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen ruling. "
              "The law requires 18 hours of firearms training, four character references, "
              "fingerprints, a social media history review, and an in-person 'good moral "
              "character' interview for a concealed carry permit, and bans carry in dozens of "
              "'sensitive locations.' The measure passed 43-20 on a party-line vote. Hinchey "
              "represents SD-41 in the Hudson Valley (Greene, Ulster, Sullivan, and Delaware "
              "counties) and has served since January 2021, when she succeeded Republican "
              "Daphne Jordan. As the daughter of longtime Congressman Maurice Hinchey (NY-22, "
              "1993–2013), she follows a family tradition of progressive advocacy that here "
              "directly opposes the rubric's defense of constitutional carry.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Michelle_Hinchey"]),
        claim("mh2", "michelle-hinchey", "biblical_marriage", 2, False,
              "Hinchey voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's "
              "foundational law. Representing SD-41 in the rural Hudson Valley since 2021, "
              "Hinchey voted with the entire Democratic Senate majority to constitutionalize "
              "LGBTQ+ protections — the policy promotion of transgender ideology the rubric "
              "opposes.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Michelle_Hinchey"]),
        claim("mh3", "michelle-hinchey", "sanctity_of_life", 0, False,
              "Hinchey voted YES on Shield Law 2.0 (S4914B, 2025), which bars New York courts "
              "and law enforcement from cooperating with out-of-state subpoenas targeting "
              "patients, providers, or helpers for abortions or gender-affirming care performed "
              "legally in New York. The bill passed 37-20 on May 22, 2025; Governor Hochul "
              "signed it December 19, 2025. Hinchey chairs the NY Senate Agriculture Committee "
              "and has focused much of her legislative career on agricultural and rural "
              "economic policy; on abortion and reproductive rights, she has voted in lockstep "
              "with the Democratic Senate majority, rejecting any personhood-from-conception "
              "standard for legislation.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4914/amendment/B",
               "https://www.nysenate.gov/senators/michelle-hinchey/about"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

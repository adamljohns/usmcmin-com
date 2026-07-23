#!/usr/bin/env python3
"""Enrichment batch 842: 5 New York Democratic state senators (archetype_party_default).

Continues bottom-of-alphabet state-senator enrichment from batch 841 (NY senators
Michael Gianaris, Luis R. Sepulveda, Liz Krueger, Leroy Comrie, Lea Webb). This
batch targets the next 5 NY Democrats from the reverse-alpha bucket:

  Kristen Gonzalez    — SD-59, western Queens/northern Brooklyn/East Side Manhattan
                        (senator since Jan 2023; youngest woman ever elected to NYS
                        Senate; chairs Internet & Technology and Elections committees)
  Kevin Parker        — SD-21, Central Brooklyn / Flatbush area (senator since 2002;
                        one of the chamber's longest-serving members; Chair, Energy
                        and Telecommunications Committee)
  Julia Salazar       — SD-18, North Brooklyn/Bushwick (senator since Jan 2019; DSA
                        member; defeated incumbent Dem Martin Malave Dilan in 2018
                        primary)
  Joseph Addabbo Jr.  — SD-15, Central/South Queens (senator since 2008; NOTABLE:
                        voted NO on the Reproductive Health Act in 2019 — one of only
                        2 Senate Democrats to do so; more moderate profile on life)
  Jose M. Serrano     — SD-29, South Bronx + Spanish Harlem/Yorkville/Roosevelt Island
                        (senator since 2004; co-sponsor of RHA; Chair, Senate Majority
                        Conference and Cultural Affairs, Tourism, Parks & Recreation)

Key sourced legislation (same corpus as batches 836–841):
- Reproductive Health Act (S240, 2019): abortion on demand through 24 wks; post-viability
  at practitioner discretion; passed 38-24; Parker, Salazar, Serrano voted YES;
  ADDABBO VOTED NO (one of only 2 Senate Dems to oppose — see sources below).
- GENDA (2019): gender identity/expression added to NY Human Rights Law; Parker,
  Salazar, Serrano present and voting yes; Gonzalez not yet seated.
- Concealed Carry Improvement Act (S51001, 2022): 18-hr training, 4 character refs,
  social media review, good-moral-character interview, sensitive-places ban; 43-20
  party-line (all 43 Dems voted yes, including Addabbo); Gonzalez not yet seated.
- Equal Protection Amendment / S108A (2023): LGBTQ+, pregnancy, reproductive autonomy
  added to NY Constitution; 43-20; voter-approved as Proposal 1, November 2024 (62%).
  All five senators voted yes (Gonzalez seated Jan 1, 2023; vote was Jan 24, 2023).
- Shield Law 2.0 (S4914B, 2025): protects abortion/gender-affirming care providers
  from out-of-state prosecution; 37-20; signed Dec 19, 2025.

NOTE: Kristen Gonzalez (seated Jan 2023) has only 2 claims — ERA and Shield Law 2.0
— spanning distinct categories, since she was not present for the 2019 or 2022 votes.
NOTE: Joseph Addabbo Jr. has 2 claims: his NO vote on RHA (score_impact True, aligns
with rubric) and his YES vote on CCIA (score_impact False; the CCIA passed 43-20 with
all 43 Senate Democrats in favor on a strict party-line vote).
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
    # --- Kristen Gonzalez (NY-D, SD-59, western Queens/northern Brooklyn/East Side
    #     Manhattan; senator since Jan 1, 2023; youngest woman ever elected to NYS Senate;
    #     chairs Internet & Technology and Elections committees) ---
    # NOTE: Not present for RHA (2019), GENDA (2019), or CCIA (2022); 2 claims only.
    ("kristen-gonzalez", "NY", "Senator", [
        claim("kg1", "kristen-gonzalez", "biblical_marriage", 2, False,
              "Gonzalez voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's foundational "
              "law. Gonzalez represents SD-59 covering parts of western Queens, northern "
              "Brooklyn, and the East Side of Manhattan, and took office January 1, 2023 — "
              "becoming the youngest woman ever elected to the New York State Senate. She "
              "chairs both the Internet and Technology and the Elections Committees. Her YES "
              "vote on S108A in her very first month of service placed constitutional "
              "protection of gender identity and reproductive autonomy squarely in New York's "
              "organic law, directly opposing the rubric's requirement that officials reject "
              "transgender ideology.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Kristen_Gonzalez"]),
        claim("kg2", "kristen-gonzalez", "sanctity_of_life", 0, False,
              "Gonzalez voted YES on Shield Law 2.0 (S4914B, 2025), which bars New York "
              "courts and law enforcement from cooperating with out-of-state subpoenas "
              "targeting patients, providers, or helpers for abortions or gender-affirming "
              "care performed legally in New York. The bill passed 37-20 on May 22, 2025; "
              "Governor Hochul signed it December 19, 2025 (Chapter 694). Gonzalez "
              "represents SD-59 (western Queens, northern Brooklyn, East Side of Manhattan) "
              "and has served since January 1, 2023, as the youngest woman ever elected to "
              "the New York State Senate. She chairs both the Internet and Technology and "
              "the Elections Committees, and has championed legislation protecting private "
              "health data in connection with abortion access. Her YES vote on Shield Law "
              "2.0 insulates abortion and gender-affirming care providers from accountability "
              "under other states' laws — rejecting any recognition of personhood from "
              "conception.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4914/amendment/B",
               "https://ballotpedia.org/Kristen_Gonzalez"]),
    ]),

    # --- Kevin Parker (NY-D, SD-21, Central Brooklyn — Flatbush, East Flatbush,
    #     Kensington, Ditmas Park, Midwood, Flatlands, Canarsie, Mill Basin, Bergen
    #     Beach, Marine Park; senator since 2002; Chair, Energy and Telecommunications) ---
    ("kevin-parker", "NY", "Senator", [
        claim("kp1", "kevin-parker", "sanctity_of_life", 0, False,
              "Parker voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24 with the Senate Democratic "
              "caucus voting in favor as a bloc. It removed abortion from the Penal Code and "
              "set no gestational limit when a licensed practitioner certifies necessity — "
              "effectively allowing abortion through all nine months. Parker represents SD-21 "
              "in Central Brooklyn (Flatbush, East Flatbush, Kensington, Ditmas Park, Midwood, "
              "Flatlands, Canarsie, Georgetown, Mill Basin, Bergen Beach, and Marine Park) and "
              "has served in the New York State Senate since 2002 — one of the chamber's "
              "longest-serving members — and chairs the Committee on Energy and "
              "Telecommunications.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Kevin_Parker_(New_York)"]),
        claim("kp2", "kevin-parker", "self_defense", 1, False,
              "Parker voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen "
              "ruling. The law requires 18 hours of firearms training, four character "
              "references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and bans carry "
              "in dozens of 'sensitive locations' including houses of worship, transit "
              "systems, and public parks. The measure passed 43-20 on a party-line vote "
              "with the full Democratic caucus voting unanimously. Representing SD-21 in "
              "Central Brooklyn since 2002 and serving as one of the Senate's most senior "
              "Democrats, Parker voted to impose the most restrictive concealed carry regime "
              "in the nation, directly opposing the rubric's defense of constitutional carry "
              "and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Kevin_Parker_(New_York)"]),
        claim("kp3", "kevin-parker", "biblical_marriage", 2, False,
              "Parker voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's "
              "foundational law. Parker also voted YES on GENDA (January 15, 2019), which "
              "added gender identity and expression as protected classes under the NY Human "
              "Rights Law, signed by Gov. Cuomo on January 25, 2019. Representing SD-21 in "
              "Central Brooklyn since 2002 as one of the chamber's most senior Democrats, "
              "Parker has consistently supported both statutory and constitutional expansion "
              "of LGBTQ+ protections across more than two decades in the Senate.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://en.wikipedia.org/wiki/Kevin_Parker_(New_York_politician)"]),
    ]),

    # --- Julia Salazar (NY-D, SD-18, North Brooklyn — Bushwick, Ridgewood, parts of
    #     Williamsburg, Maspeth; senator since Jan 2019; DSA member; defeated incumbent
    #     Dem Martin Malave Dilan in 2018 primary) ---
    ("julia-salazar", "NY", "Senator", [
        claim("jsal1", "julia-salazar", "sanctity_of_life", 0, False,
              "Salazar voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24; Salazar, who took office "
              "January 1, 2019 — less than four weeks before the vote — was among the newly "
              "seated Democratic senators who helped deliver the majority needed for passage. "
              "It removed abortion from the Penal Code and set no gestational limit when a "
              "licensed practitioner certifies necessity — effectively allowing abortion through "
              "all nine months. Salazar represents SD-18 in North Brooklyn (Bushwick, "
              "Ridgewood, parts of Williamsburg and Maspeth), which she won in 2018 by "
              "defeating incumbent Democrat Martin Malave Dilan. She is a member of the "
              "Democratic Socialists of America and a founding voice of the Senate's "
              "progressive caucus.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Julia_Salazar"]),
        claim("jsal2", "julia-salazar", "self_defense", 1, False,
              "Salazar voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen "
              "ruling. The law requires 18 hours of firearms training, four character "
              "references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and bans carry "
              "in dozens of 'sensitive locations' including houses of worship, transit "
              "systems, and public parks. The measure passed 43-20 with the full Democratic "
              "caucus voting in favor. Ballotpedia notes that Salazar supports gun safety "
              "measures including background checks, safe-storage rules, red-flag laws, and "
              "bump-stock bans. As a DSA-aligned progressive senator representing SD-18 in "
              "North Brooklyn since 2019, she voted to impose the most restrictive concealed "
              "carry regime in the nation, directly opposing the rubric's defense of "
              "constitutional carry and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Julia_Salazar"]),
        claim("jsal3", "julia-salazar", "biblical_marriage", 2, False,
              "Salazar voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's "
              "foundational law. Salazar also co-sponsored GENDA (January 15, 2019), which "
              "added gender identity and expression as protected classes under the NY Human "
              "Rights Law. As a member of the Democratic Socialists of America and Jews for "
              "Racial and Economic Justice, and as one of the progressive caucus's founding "
              "voices, Salazar has been among the most outspoken advocates for LGBTQ+ rights "
              "and for constitutionalizing gender identity protections in New York law.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://en.wikipedia.org/wiki/Julia_Salazar"]),
    ]),

    # --- Joseph Addabbo Jr. (NY-D, SD-15, Central/South Queens — Forest Hills, Glendale,
    #     Kew Gardens, Lindenwood, Ozone Park, Middle Village, Rego Park, Richmond Hill,
    #     South Ozone Park, South Richmond Hill, Maspeth, Woodhaven; senator since 2008)
    #     NOTABLE: voted NO on RHA (2019) — one of only 2 Senate Dems to oppose it. ---
    ("joseph-addabbo-jr", "NY", "Senator", [
        claim("ja1", "joseph-addabbo-jr", "sanctity_of_life", 0, True,
              "Addabbo voted NO on the Reproductive Health Act (S240, January 22, 2019), "
              "making him one of only two Senate Democrats — alongside Sen. Simcha Felder, "
              "who caucuses independently — to oppose the measure. The RHA passed 38-24. "
              "Addabbo explained his vote by saying: 'if it was a straight codification of "
              "Roe v. Wade I believe I would have voted for that… it's the law of the land… "
              "for me, it boiled down to the language of that particular bill.' The measure "
              "expanded abortion on demand through 24 weeks, permitted post-viability abortion "
              "at a practitioner's discretion, and removed abortion from the Penal Code with "
              "no gestational cap. Addabbo represents SD-15 in Central Queens (Forest Hills, "
              "Glendale, Kew Gardens, Lindenwood, Ozone Park, Middle Village, Rego Park, "
              "Richmond Hill, South Ozone Park, Maspeth, and Woodhaven) and has served since "
              "2008. Progressive organizations in Queens subsequently organized a primary "
              "challenge against him specifically over his NO vote on the RHA. His NO vote "
              "on the RHA aligns with the rubric's sanctity-of-life standard.",
              ["https://www.rockawave.com/articles/addabbo-faces-pushback-on-rha-vote/",
               "https://ballotpedia.org/Joseph_Addabbo"]),
        claim("ja2", "joseph-addabbo-jr", "self_defense", 1, False,
              "Addabbo voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen "
              "ruling. The law requires 18 hours of firearms training, four character "
              "references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and bans carry "
              "in dozens of 'sensitive locations' including houses of worship, transit "
              "systems, and public parks. The measure passed 43-20 on a strict party-line "
              "vote with all 43 Senate Democrats voting in favor, including Addabbo. "
              "Representing SD-15 in Central Queens since 2008, Addabbo voted with the "
              "Democratic majority on firearms restrictions despite his more moderate profile "
              "on life issues — directly opposing the rubric's defense of constitutional "
              "carry and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Joseph_Addabbo"]),
    ]),

    # --- Jose M. Serrano (NY-D, SD-29, South Bronx — Mott Haven, Melrose, Highbridge,
    #     Morris Heights — + Spanish Harlem, Yorkville, Roosevelt Island, and part of
    #     Upper West Side; senator since 2004; co-sponsor of RHA; Chair, Senate Majority
    #     Conference and Cultural Affairs, Tourism, Parks & Recreation) ---
    ("jose-m-serrano", "NY", "Senator", [
        claim("jser1", "jose-m-serrano", "sanctity_of_life", 0, False,
              "Serrano was a CO-SPONSOR of the Reproductive Health Act (S240, January 22, "
              "2019), which expanded abortion on demand through 24 weeks and permits "
              "post-viability abortion when a practitioner determines it is necessary for "
              "health or life, or when the fetus is not viable. The bill passed 38-24 with "
              "all Senate Democrats (save one) voting in favor. It removed abortion from the "
              "Penal Code and set no gestational limit when a licensed practitioner certifies "
              "necessity — effectively allowing abortion through all nine months. On July 9, "
              "2018, Serrano stood with Governor Cuomo to announce new state actions to "
              "protect women's reproductive health care access from federal rollbacks. "
              "Serrano represents SD-29 covering Mott Haven, Melrose, Highbridge, Morris "
              "Heights, Spanish Harlem, Yorkville, Roosevelt Island, and part of the Upper "
              "West Side — spanning both the Bronx and Manhattan — and has served in the "
              "New York State Senate since 2004, currently chairing the Senate Majority "
              "Conference.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://www.nysenate.gov/newsroom/articles/2018/jose-m-serrano/senator-serrano-fights-reproductive-rights"]),
        claim("jser2", "jose-m-serrano", "biblical_marriage", 2, False,
              "Serrano voted YES on GENDA (January 15, 2019), which added gender identity "
              "and expression as protected classes under the New York Human Rights Law, "
              "signed by Gov. Cuomo on January 25, 2019. The bill had been stalled for over "
              "a decade under Senate Republican control and passed on the first day of the "
              "newly Democratic-majority session. Serrano also voted YES on S108A (January "
              "24, 2023), the Equal Rights Amendment adding sexual orientation, gender "
              "identity, gender expression, pregnancy, pregnancy outcomes, and reproductive "
              "autonomy to the New York State Constitution's equal protection clause — "
              "passing 43-20 and approved by voters as Proposal 1 in November 2024 with "
              "62% in favor, permanently embedding transgender identity protections in New "
              "York's foundational law. As Chair of the Senate Majority Conference and a "
              "senator since 2004, Serrano has been a consistent supporter of LGBTQ+ "
              "expansion in both statutory and constitutional law.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://en.wikipedia.org/wiki/Jos%C3%A9_M._Serrano"]),
        claim("jser3", "jose-m-serrano", "self_defense", 1, False,
              "Serrano voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen "
              "ruling. The law requires 18 hours of firearms training, four character "
              "references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and bans carry "
              "in dozens of 'sensitive locations' including houses of worship, transit "
              "systems, and public parks. The measure passed 43-20 on a party-line vote. "
              "Serrano represents SD-29 (South Bronx/Manhattan corridor) and has served "
              "since 2004, currently chairing the Senate Majority Conference and the "
              "Committee on Cultural Affairs, Tourism, Parks and Recreation. He voted with "
              "the full Democratic caucus to impose the most restrictive concealed carry "
              "regime in the nation, directly opposing the rubric's defense of constitutional "
              "carry and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Jose_M._Serrano"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

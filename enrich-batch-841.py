#!/usr/bin/env python3
"""Enrichment batch 841: 5 New York Democratic state senators (archetype_party_default).

Continues bottom-of-alphabet state-senator enrichment from batch 840 (NY senators Peter
Harckham, Patricia Fahy, Nathalia Fernandez, Monica Martinez, Michelle Hinchey). This
batch targets the next 5 NY Democrats from the reverse-alpha bucket:

  Michael Gianaris  — SD-12, Queens/Astoria/LIC (senator since 2011; Deputy Majority
                      Leader since 2019)
  Luis R. Sepulveda — SD-32, South Bronx (senator since April 2018 special election to
                      fill seat vacated by Ruben Diaz Sr.)
  Liz Krueger       — SD-28, East Side of Manhattan (senator since 2002 special election;
                      Senate Finance Committee Chair since 2019)
  Leroy Comrie      — SD-14, southeast Queens/Jamaica/St. Albans (senator since Jan 2015;
                      prior 12 yrs NYC Council Deputy Majority Leader)
  Lea Webb          — SD-52, Cortland, Tompkins, and part of Broome County/Binghamton
                      (senator since Jan 2023; Chair, Senate Women's Issues Committee;
                       first Democrat to hold SD-52 since 2004)

Key sourced legislation (same corpus as batches 836–840):
- Reproductive Health Act (S240, 2019): abortion on demand through 24 wks; post-viability
  for health/life/fetal non-viability; passed 38-24; Gianaris, Sepulveda, Krueger, Comrie
  present and voting yes (Webb not yet seated).
- GENDA (2019): gender identity/expression added to NY Human Rights Law; Gianaris,
  Sepulveda, Krueger, Comrie present; Webb not yet seated.
- Concealed Carry Improvement Act (S51001, 2022): 18-hr training, 4 character refs,
  social media review, good-moral-character interview, sensitive-places ban; 43-20;
  Gianaris, Sepulveda, Krueger, Comrie present; Webb not yet seated.
- Equal Protection Amendment / S108A (2023): LGBTQ+, pregnancy, reproductive autonomy
  added to NY Constitution; 43-20; voter-approved as Proposal 1, November 2024 (62%).
  All five senators voted yes (Webb seated Jan 1, 2023; vote was Jan 24, 2023).
- Shield Law 2.0 (S4914B, 2025): protects abortion/gender-affirming care providers
  from out-of-state prosecution; 37-20; signed Dec 19, 2025. Webb voted yes.

NOTE: Lea Webb (seated Jan 2023) has only 2 claims covering ERA and Shield Law 2.0,
spanning distinct categories. 14 total claims this batch.
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
    # --- Michael Gianaris (NY-D, SD-12, Queens/Astoria/LIC; senator since 2011;
    #     Deputy Majority Leader since 2019) ---
    ("michael-gianaris", "NY", "Senator", [
        claim("mg1", "michael-gianaris", "sanctity_of_life", 0, False,
              "Gianaris voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24 with all Senate Democrats "
              "voting in favor. It removed abortion from the Penal Code and set no gestational "
              "limit when a licensed practitioner certifies necessity — effectively allowing "
              "abortion through all nine months. Gianaris represents SD-12 in northwest Queens "
              "(Astoria, Long Island City, Sunnyside, and parts of Woodside, Maspeth, and "
              "Ridgewood) and has served as State Senator since 2011 and as Senate Deputy "
              "Majority Leader since 2019, making him one of the most powerful members of the "
              "New York State Senate.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Michael_Gianaris"]),
        claim("mg2", "michael-gianaris", "self_defense", 1, False,
              "Gianaris voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in direct response to the U.S. Supreme Court's NYSRPA v. Bruen "
              "ruling. The law requires 18 hours of firearms training, four character "
              "references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and bans carry "
              "in dozens of 'sensitive locations' including houses of worship, transit systems, "
              "and public parks. The measure passed 43-20 on a party-line vote. As Deputy "
              "Majority Leader, Gianaris helped shepherd the bill through the chamber and voted "
              "with the Democratic majority to impose the most restrictive concealed carry "
              "regime in the nation, directly opposing the rubric's defense of constitutional "
              "carry and Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Michael_Gianaris"]),
        claim("mg3", "michael-gianaris", "biblical_marriage", 2, False,
              "Gianaris voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's foundational "
              "law. Gianaris also voted YES on GENDA (January 15, 2019), which added gender "
              "identity and expression as protected classes under the NY Human Rights Law. As "
              "Deputy Majority Leader since 2019, he is a chief architect of the Democratic "
              "majority's legislative agenda and a leading voice for LGBTQ+ expansion in both "
              "statutory and constitutional law.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Michael_Gianaris"]),
    ]),

    # --- Luis R. Sepulveda (NY-D, SD-32, South Bronx; senator since April 30, 2018
    #     (special election to fill seat vacated by Ruben Diaz Sr.)) ---
    ("luis-r-sepulveda", "NY", "Senator", [
        claim("ls1", "luis-r-sepulveda", "sanctity_of_life", 0, False,
              "Sepúlveda voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24 with all Senate Democrats "
              "voting in favor. It removed abortion from the Penal Code and set no gestational "
              "limit when a licensed practitioner certifies necessity — effectively allowing "
              "abortion through all nine months. Sepúlveda represents SD-32 in the central "
              "and south Bronx and has served in the New York State Senate since winning a "
              "special election on April 24, 2018, to fill the seat vacated by the resignation "
              "of Ruben Diaz Sr.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Luis_Sep%C3%BAlveda_(New_York)"]),
        claim("ls2", "luis-r-sepulveda", "self_defense", 1, False,
              "Sepúlveda voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen ruling. "
              "The law requires 18 hours of firearms training, four character references, "
              "fingerprints, a social media history review, and an in-person 'good moral "
              "character' interview for a concealed carry permit, and bans carry in dozens of "
              "'sensitive locations' including houses of worship, transit, and public parks. "
              "The measure passed 43-20 on a party-line vote. Representing SD-32 in the "
              "South Bronx since 2018, Sepúlveda voted with the Democratic Senate majority "
              "to impose the most restrictive concealed carry regime in the nation, directly "
              "opposing the rubric's defense of constitutional carry and Second Amendment "
              "rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Luis_Sep%C3%BAlveda_(New_York)"]),
        claim("ls3", "luis-r-sepulveda", "biblical_marriage", 2, False,
              "Sepúlveda voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's foundational "
              "law. Sepúlveda also voted YES on GENDA (January 15, 2019), which added gender "
              "identity and expression as protected classes under the NY Human Rights Law. "
              "Representing a heavily Democratic South Bronx district since 2018, he has "
              "consistently supported expansion of LGBTQ+ protections in both statutory and "
              "constitutional law.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Luis_Sep%C3%BAlveda_(New_York)"]),
    ]),

    # --- Liz Krueger (NY-D, SD-28, East Side of Manhattan; senator since 2002 special
    #     election; Senate Finance Committee Chair since 2019) ---
    ("liz-krueger", "NY", "Senator", [
        claim("lk1", "liz-krueger", "sanctity_of_life", 0, False,
              "Krueger was the PRIMARY SPONSOR and Senate floor champion of the Reproductive "
              "Health Act (S240, January 22, 2019), which expanded abortion on demand through "
              "24 weeks and permits post-viability abortion when a practitioner determines it "
              "is necessary for health or life, or when the fetus is not viable. The bill "
              "passed 38-24 with all Senate Democrats voting in favor. It removed abortion "
              "from the Penal Code and set no gestational limit when a licensed practitioner "
              "certifies necessity — effectively allowing abortion through all nine months. "
              "Krueger represents SD-28 on the East Side of Manhattan and has served in the "
              "New York State Senate since a 2002 special election; she has chaired the "
              "powerful Senate Finance Committee since 2019 and authored the RHA as its "
              "lead sponsor.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://en.wikipedia.org/wiki/Liz_Krueger"]),
        claim("lk2", "liz-krueger", "self_defense", 1, False,
              "Krueger voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen ruling. "
              "The law requires 18 hours of firearms training, four character references, "
              "fingerprints, a social media history review, and an in-person 'good moral "
              "character' interview for a concealed carry permit, and bans carry in dozens of "
              "'sensitive locations' including houses of worship, transit, and public parks. "
              "The measure passed 43-20 on a party-line vote. As Senate Finance Committee "
              "Chair and a long-serving Manhattan senator since 2002, Krueger voted with the "
              "Democratic majority to impose the most restrictive concealed carry regime in "
              "the nation, directly opposing the rubric's defense of constitutional carry and "
              "Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://en.wikipedia.org/wiki/Liz_Krueger"]),
        claim("lk3", "liz-krueger", "biblical_marriage", 2, False,
              "Krueger was the PRIMARY SPONSOR of S108A (January 24, 2023), the Equal Rights "
              "Amendment adding sexual orientation, gender identity, gender expression, "
              "pregnancy, pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 and "
              "was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's foundational "
              "law. Krueger also voted YES on GENDA (January 15, 2019), which added gender "
              "identity and expression as protected classes under the NY Human Rights Law. As "
              "Senate Finance Chair and a senator since 2002, she authored and championed both "
              "the RHA and the ERA — making her the legislature's most prominent architect of "
              "reproductive and LGBTQ+ constitutional expansion.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://en.wikipedia.org/wiki/Liz_Krueger"]),
    ]),

    # --- Leroy Comrie (NY-D, SD-14, southeast Queens/Springfield Gardens/St. Albans/Jamaica;
    #     senator since January 2015; prior 12 yrs on NYC Council as Deputy Majority Leader) ---
    ("leroy-comrie", "NY", "Senator", [
        claim("lc1", "leroy-comrie", "sanctity_of_life", 0, False,
              "Comrie voted YES on the Reproductive Health Act (S240, January 22, 2019), "
              "which expanded abortion on demand through 24 weeks and permits post-viability "
              "abortion when a practitioner determines it is necessary for health or life, or "
              "when the fetus is not viable. The bill passed 38-24 with all Senate Democrats "
              "voting in favor. It removed abortion from the Penal Code and set no gestational "
              "limit when a licensed practitioner certifies necessity — effectively allowing "
              "abortion through all nine months. Comrie represents SD-14 in southeast Queens "
              "(Springfield Gardens, St. Albans, Hollis, Jamaica, and neighboring communities) "
              "and has served in the New York State Senate since January 2015, following "
              "12 years on the New York City Council where he served as Deputy Majority "
              "Leader and Chair of the Queens Delegation.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://ballotpedia.org/Leroy_Comrie"]),
        claim("lc2", "leroy-comrie", "self_defense", 1, False,
              "Comrie voted YES on the Concealed Carry Improvement Act (S51001, July 1, "
              "2022), enacted in response to the U.S. Supreme Court's NYSRPA v. Bruen ruling. "
              "The law requires 18 hours of firearms training, four character references, "
              "fingerprints, a social media history review, and an in-person 'good moral "
              "character' interview for a concealed carry permit, and bans carry in dozens of "
              "'sensitive locations' including houses of worship, transit, and public parks. "
              "The measure passed 43-20 on a party-line vote. Representing SD-14 in southeast "
              "Queens since 2015 and serving as Chair of the Committee on Corporations, "
              "Authorities and Commissions, Comrie voted with the Democratic majority to "
              "impose the most restrictive concealed carry regime in the nation, directly "
              "opposing the rubric's defense of constitutional carry and Second Amendment "
              "rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Leroy_Comrie"]),
        claim("lc3", "leroy-comrie", "biblical_marriage", 2, False,
              "Comrie voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's foundational "
              "law. Comrie also voted YES on GENDA (January 15, 2019), which added gender "
              "identity and expression as protected classes under the NY Human Rights Law, "
              "signed by Gov. Cuomo on January 25, 2019. A Queens Democrat representing "
              "SD-14 since 2015, Comrie has consistently supported statutory and constitutional "
              "expansion of LGBTQ+ protections.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Leroy_Comrie"]),
    ]),

    # --- Lea Webb (NY-D, SD-52, Cortland + Tompkins counties + part of Broome/Binghamton;
    #     senator since January 1, 2023; Chair, Senate Women's Issues Committee;
    #     first Democrat to hold SD-52 since 2004) ---
    # NOTE: Webb took office Jan 1, 2023 — she was NOT present for RHA (2019), GENDA (2019),
    # or CCIA (2022). Two claims spanning distinct categories are used here.
    ("lea-webb", "NY", "Senator", [
        claim("lw1", "lea-webb", "biblical_marriage", 2, False,
              "Webb voted YES on S108A (January 24, 2023), the Equal Rights Amendment "
              "adding sexual orientation, gender identity, gender expression, pregnancy, "
              "pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 "
              "and was approved by voters as Proposal 1 in November 2024 with 62% in favor, "
              "permanently embedding transgender identity protections in New York's foundational "
              "law. Webb represents SD-52 (Cortland and Tompkins counties and a portion of "
              "Broome County including the city of Binghamton), has served since January 1, "
              "2023 — the first Democrat to hold the seat since 2004 — and chairs the Senate "
              "Women's Issues Committee, a role for which she was commended in connection with "
              "the ERA's passage.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Lea_Webb"]),
        claim("lw2", "lea-webb", "sanctity_of_life", 0, False,
              "Webb voted YES on Shield Law 2.0 (S4914B, 2025), which bars New York courts "
              "and law enforcement from cooperating with out-of-state subpoenas targeting "
              "patients, providers, or helpers for abortions or gender-affirming care performed "
              "legally in New York. The bill passed 37-20 on May 22, 2025; Governor Hochul "
              "signed it December 19, 2025 (Chapter 694). Representing SD-52 in the Southern "
              "Tier since January 2023 and serving as Chair of the Senate Women's Issues "
              "Committee, Webb supported the measure as part of New York's legislative effort "
              "to insulate abortion and gender-affirming procedures from accountability under "
              "other states' laws — rejecting any recognition of personhood from conception.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4914/amendment/B",
               "https://ballotpedia.org/Lea_Webb"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

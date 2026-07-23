#!/usr/bin/env python3
"""Enrichment batch 839: 5 New York Democratic state senators (archetype_party_default).

Continues bottom-of-alphabet state-senator enrichment from batches 836-838 (ND
senators). Prior sessions exhausted WY-WV-WI-WA-VT-VA-TX-TN-SD-SC-RI-PA-OR-OK-OH;
NY is now the top of the reverse-alpha bucket with 1,100+ archetype_party_default
state senators remaining. This batch targets 5 NY Democrats from the top of the
reverse-sorted bucket — all cast votes on shared legislation (Reproductive Health Act,
Concealed Carry Improvement Act, Equal Rights Amendment) that cleanly maps to rubric
categories.

  Samra Brouk — SD-55, Monroe County/Rochester (took office Jan 2021)
  Sam Sutton — SD-22, Brooklyn (took office May 27, 2025; very new)
  Roxanne Persaud — SD-19, Brooklyn (took office 2015)
  Robert Jackson — SD-31, Manhattan (took office Jan 2019)
  Rachel May — SD-48, Syracuse/Onondaga County (took office Jan 2019)

Key sourced legislation:
- Reproductive Health Act (S240, 2019): abortion on demand through 24 wks; post-viability
  for health/life/fetal non-viability; passed 38-24.
- GENDA (2019): gender identity/expression added to NY Human Rights Law.
- Concealed Carry Improvement Act (S51001, 2022): 18-hr training, 4 character refs,
  social media review, good-moral-character interview, sensitive-places ban; 43-20.
- Equal Protection Amendment / S108 (2023): LGBTQ+, pregnancy, reproductive autonomy
  added to NY Constitution; 43-20; voter-approved as Proposal 1, November 2024.
- Shield Law 2.0 (S4914B, 2025): protects abortion/gender-affirming care providers
  from out-of-state prosecution; 37-20; signed Dec 19, 2025.
- S2533-A (2025): authorizes pharmacists to dispense abortion medication.
- S8257 (2025): IVF/fertility treatment access for Medicaid patients.
- S8256 (2025): sabbath observance religious accommodation from municipal trash fines.

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
    # --- Samra Brouk (NY-D, SD-55, Monroe County/Rochester; took office Jan 2021) ---
    ("samra-brouk", "NY", "Senator", [
        claim("sb1", "samra-brouk", "sanctity_of_life", 0, False,
              "Brouk voted YES on the Shield Law 2.0 (S4914B, 2025), which bars New York courts "
              "and law enforcement from cooperating with out-of-state subpoenas targeting patients, "
              "providers, or helpers for abortions or gender-affirming care performed legally in "
              "New York. Brouk was also a co-introducer of S4914. The bill passed 37-20 on "
              "May 22, 2025; Governor Hochul signed it December 19, 2025 (Chapter 694). A Democrat "
              "representing Senate District 55 in Monroe County (Rochester and eastern suburbs "
              "including Irondequoit, Webster, Penfield, and Pittsford), Brouk has championed "
              "abortion access since taking office in January 2021 as the first Black woman from "
              "Upstate New York to serve in the NY State Senate. She chairs the Senate Mental "
              "Health Committee.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4914/amendment/B",
               "https://ag.ny.gov/press-release/2025/attorney-general-james-celebrates-new-nation-leading-shield-law-protections"]),
        claim("sb2", "samra-brouk", "biblical_marriage", 2, False,
              "Brouk co-introduced and voted YES on S108A (January 24, 2023), the Equal Rights "
              "Amendment that added sexual orientation, gender identity, gender expression, "
              "pregnancy, pregnancy outcomes, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause. The measure passed the Senate 43-20 in the "
              "second of two required legislative sessions. Brouk stated: 'The passage of the Equal "
              "Rights Amendment is an important step forward for New Yorkers — our State "
              "Constitution's equal protection clause has never included protections for sex and "
              "gender. While the radical Supreme Court takes action to strip rights away, we took "
              "action to protect those rights in New York.' Voters approved the amendment as "
              "Proposal 1 in November 2024 with 62% in favor, permanently embedding transgender "
              "identity protections in New York's foundational law.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://ballotpedia.org/Samra_Brouk"]),
        claim("sb3", "samra-brouk", "self_defense", 1, False,
              "Brouk voted YES on the Concealed Carry Improvement Act (S51001, July 1, 2022), "
              "enacted in direct response to the U.S. Supreme Court's NYSRPA v. Bruen ruling. "
              "The law requires 18 hours of firearms training, four character references, "
              "fingerprints, a social media history review, and an in-person 'good moral "
              "character' interview for a concealed carry permit, and bans carry in dozens of "
              "'sensitive locations' including houses of worship, transit systems, Times Square, "
              "and public parks. The measure passed 43-20 on a party-line vote. Representing "
              "SD-55 in Monroe County, Brouk voted with the entire Democratic Senate majority "
              "to impose the most restrictive concealed carry regime in the nation, directly "
              "opposing the rubric's defense of Second Amendment rights.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://ballotpedia.org/Samra_Brouk"]),
    ]),

    # --- Sam Sutton (NY-D, SD-22, Brooklyn; took office May 27, 2025) ---
    ("sam-sutton", "NY", "Senator", [
        claim("ss1", "sam-sutton", "sanctity_of_life", 2, False,
              "In his first weeks in office, Sutton sponsored and passed S8257 (2025), allowing "
              "Federally Qualified Health Centers to access injectable fertility medications at "
              "reduced cost under the federal 340B drug pricing program, extending IVF and "
              "fertility treatment access to low-income Medicaid patients. The Senate passed the "
              "bill unanimously. Sutton explicitly framed the legislation as 'protecting "
              "reproductive freedom': 'Patients should not be denied care because of cost. "
              "Protecting reproductive freedom must include expanding equitable access to "
              "fertility treatment, especially for low-income and underserved New Yorkers.' "
              "Standard IVF protocols routinely produce surplus embryos that are ultimately "
              "discarded or indefinitely frozen — a practice the rubric's sanctity-of-life "
              "standard opposes. Sutton took office May 27, 2025 after winning a special "
              "election in SD-22 (Borough Park, Midwood, Flatbush, Sheepshead Bay, Marine Park) "
              "to succeed Simcha Felder, becoming the first Sephardic Jew elected to the "
              "NY State Senate.",
              ["https://www.nysenate.gov/newsroom/press-releases/2025/sam-sutton/senator-suttons-bill-expanding-fertility-treatment-access",
               "https://ballotpedia.org/Sam_Sutton"]),
        claim("ss2", "sam-sutton", "christian_liberty", 0, True,
              "Sutton sponsored S8256 (2025), exempting sabbath-observant residents from "
              "municipal fines for placing refuse containers on the sidewalk during their "
              "Sabbath — securing a religious accommodation for thousands of Orthodox and "
              "Sephardic Jewish families in SD-22 (Borough Park, Midwood, Flatbush) who are "
              "prohibited by religious law from handling trash on the Sabbath. The Senate passed "
              "the bill in 2025. A 30-year veteran of Sephardic Bikur Holim (a social-service "
              "organization serving the Sephardic Jewish community) and the first Sephardic Jew "
              "elected to the New York State Senate, Sutton used his legislative debut to remove "
              "a government burden on traditional religious observance — aligning with the "
              "rubric's protection of religious free exercise.",
              ["https://www.nysenate.gov/senators/sam-sutton",
               "https://ballotpedia.org/Sam_Sutton"]),
    ]),

    # --- Roxanne Persaud (NY-D, SD-19, Brooklyn; took office 2015) ---
    ("roxanne-persaud", "NY", "Senator", [
        claim("rp1", "roxanne-persaud", "sanctity_of_life", 0, False,
              "Persaud voted YES on the Reproductive Health Act (S240, January 22, 2019), which "
              "expanded abortion on demand through 24 weeks of pregnancy and permits post-viability "
              "abortion when 'necessary to protect the patient's life or health' or when the fetus "
              "is not viable. The measure passed 38-24 with all Senate Democrats voting in favor. "
              "It decriminalized abortion in New York, removed it from the Penal Code, and sets "
              "no gestational limit when a licensed practitioner determines abortion is necessary — "
              "effectively permitting abortion through all nine months. Persaud represents SD-19 "
              "in Brooklyn (Canarsie, East New York, Brownsville, Sheepshead Bay, Marine Park) "
              "and has served since a 2015 special election. A member of the NY Senate Bipartisan "
              "Pro-Choice Legislative Caucus, she chairs the Senate Committee on Social Services.",
              ["https://www.nysenate.gov/legislation/bills/2019/S240",
               "https://www.nysenate.gov/senators/roxanne-j-persaud/about"]),
        claim("rp2", "roxanne-persaud", "biblical_marriage", 2, False,
              "Persaud voted YES on GENDA (January 15, 2019), which added gender identity and "
              "expression as protected classes under the New York Human Rights Law, signed by "
              "Gov. Cuomo January 25, 2019. She also voted YES on S108 (January 24, 2023), the "
              "Equal Rights Amendment that added sexual orientation, gender identity, gender "
              "expression, pregnancy, and reproductive autonomy to the New York State "
              "Constitution's equal protection clause, passing 43-20. Voters approved the ERA "
              "as Proposal 1 in November 2024 with 62% in favor. Persaud's record reflects "
              "consistent support for embedding transgender-ideology protections in both New "
              "York's statutory law and its Constitution across her decade in the Senate.",
              ["https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A",
               "https://www.nysenate.gov/senators/roxanne-j-persaud/about"]),
        claim("rp3", "roxanne-persaud", "self_defense", 1, False,
              "Persaud voted YES on the Concealed Carry Improvement Act (S51001, July 1, 2022), "
              "which responded to the Bruen ruling by requiring 18 hours of training, four "
              "character references, fingerprints, a social media history review, and an in-person "
              "'good moral character' interview for a concealed carry permit, and by banning carry "
              "in dozens of 'sensitive locations.' The law passed 43-20 on a party-line vote. "
              "Persaud also sponsored legislation to establish the NY State Firearm Violence "
              "Research Institute (S7716, 2021) and to close loopholes allowing domestic violence "
              "offenders to obtain firearms in other states (S7792, 2021). Her record across "
              "Brooklyn's SD-19 reflects consistent support for restrictive gun legislation.",
              ["https://legiscan.com/NY/rollcall/S51001/id/1221464",
               "https://www.nysenate.gov/senators/roxanne-j-persaud/about"]),
    ]),

    # --- Robert Jackson (NY-D, SD-31, Manhattan; took office Jan 2019) ---
    ("robert-jackson", "NY", "Senator", [
        claim("rj1", "robert-jackson", "sanctity_of_life", 0, False,
              "Jackson voted YES on the 2019 Reproductive Health Act (S240, 38-24), permitting "
              "abortion on demand through 24 weeks and post-viability abortion when a practitioner "
              "determines it is necessary for health. He co-sponsored S348 (2023-24), the "
              "Reproductive Freedom and Equity Program establishing a state grant fund for "
              "abortion providers and nonprofits to expand access statewide. He also co-sponsored "
              "S2533-A (2025), authorizing pharmacists to dispense abortion medication under "
              "physician non-patient-specific orders and requiring insurance coverage for that "
              "medication; and sponsored S2127 (2025), suspending state-funded travel to states "
              "that restrict abortion access after six weeks. Representing SD-31 in northern "
              "Manhattan (Washington Heights, Inwood, Marble Hill, Hamilton Heights), Jackson — "
              "the first Muslim New York State Senator — has built a consistent record as a "
              "leading Senate advocate for unlimited abortion access since taking office in "
              "January 2019.",
              ["https://www.nysenate.gov/legislation/bills/2023/S2533/amendment/A",
               "https://en.wikipedia.org/wiki/Robert_Jackson_(New_York_politician)"]),
        claim("rj2", "robert-jackson", "biblical_marriage", 4, False,
              "Jackson sponsored S351, requiring New York middle schools and high schools to "
              "incorporate into their curricula the political, economic, and social contributions "
              "and life experiences of LGBTQ+ people — mandating state-directed promotion of "
              "LGBTQ+ identity in public schools. He also co-sponsored S155 (2023), requiring "
              "the use of gender-neutral terms in all New York law, local law, rule, regulation, "
              "ordinance, and resolution, purging gendered language from the entire statutory "
              "code. A co-introducer of the Equal Rights Amendment (S108, 2023) adding LGBTQ+ "
              "identities to the NY State Constitution and an early advocate for marriage equality "
              "during his time on the NYC Council, Jackson's record reflects consistent "
              "legislative promotion of LGBTQ+ ideology through curriculum mandates, statutory "
              "language reform, and constitutional action.",
              ["https://www.nysenate.gov/legislation/bills/2023/S351",
               "https://www.nysenate.gov/legislation/bills/2023/S155"]),
        claim("rj3", "robert-jackson", "self_defense", 1, False,
              "Jackson voted YES on the 2022 Concealed Carry Improvement Act (S51001, 43-20) "
              "and the 2022 gun control package (microstamping requirements, ERPO expansion, "
              "body armor regulations). He sponsored S5476 (2023) imposing an excise tax on "
              "ammunition sales to fund a Gun Violence Impact Fund — re-introduced as S6395 "
              "(2025) — and co-sponsored S6403 (2025), creating a private civil cause of action "
              "against sellers of machine guns, assault weapons, ghost guns, and unfinished frames "
              "and receivers. He also co-sponsored S9137-A (2023-24), prohibiting open carry of "
              "rifles and shotguns. Representing SD-31 in upper Manhattan, Jackson has sponsored "
              "and co-sponsored multiple bills that expand civil liability, tax ammunition, and "
              "restrict firearms — directly opposing the rubric's Second Amendment protections.",
              ["https://legiscan.com/NY/bill/S05476/2023",
               "https://legiscan.com/NY/rollcall/S51001/id/1221464"]),
    ]),

    # --- Rachel May (NY-D, SD-48, Syracuse/Onondaga County; took office Jan 2019) ---
    ("rachel-may", "NY", "Senator", [
        claim("rm1", "rachel-may", "sanctity_of_life", 0, False,
              "May was the primary sponsor of S2533-A (2025), authorizing pharmacists to dispense "
              "abortion medication directly to patients under physician non-patient-specific orders, "
              "removing the requirement for a face-to-face clinical visit, and requiring health "
              "insurance coverage for all abortion medication. She stated: 'By passing this bill, "
              "we can ensure women receive the care they need, when they need it, from a provider "
              "they trust.' She also voted YES on the 2019 Reproductive Health Act (38-24) and "
              "the Shield Law 2.0 (S4914B, 2025) protecting abortion providers from out-of-state "
              "prosecution, and explicitly campaigned to 'fight for universal health care and "
              "reproductive rights.' Representing SD-48 (Syracuse and parts of Onondaga and "
              "Cayuga counties) since January 2019, May serves as Majority Steering Chair and "
              "chairs the Consumer Protection Committee.",
              ["https://www.nysenate.gov/legislation/bills/2025/S2533/amendment/A",
               "https://www.nysenate.gov/newsroom/press-releases/2025/rachel-may/senator-rachel-may-advances-more-two-dozen-bills-through"]),
        claim("rm2", "rachel-may", "biblical_marriage", 4, False,
              "May voted YES on GENDA (January 2019) adding gender identity/expression to the "
              "NY Human Rights Law, and YES on S108 (January 24, 2023), the Equal Rights "
              "Amendment embedding LGBTQ+ protections in the NY State Constitution (43-20; "
              "voter-approved November 2024 with 62% in favor). She sponsored S7677 (2023-24), "
              "requiring all public libraries receiving state aid to adopt policies prohibiting "
              "the removal of books based on 'partisan or doctrinal disapproval' — legislation "
              "specifically designed to protect LGBTQ+ content from removal from library "
              "collections. A former Stanford Ph.D. and university sustainability director "
              "representing upstate SD-48 (Syracuse, Onondaga County), May has consistently "
              "voted to embed LGBTQ+ content in public institutions and constitutional law.",
              ["https://www.nysenate.gov/legislation/bills/2023/S7677",
               "https://www.nysenate.gov/legislation/bills/2023/S108/amendment/A"]),
        claim("rm3", "rachel-may", "self_defense", 1, False,
              "May voted YES on the 2022 Concealed Carry Improvement Act (S51001, 43-20) and "
              "sponsored S8125 (2023-24), creating a private civil right of action against gun "
              "industry members who design or market firearms and firearm-related products to "
              "minors — re-introduced as S4388 (2025) when the prior bill lapsed. The bill "
              "imposes civil liability on manufacturers and dealers for marketing targeting "
              "underage buyers. Representing SD-48 in upstate Central New York (Syracuse, "
              "Onondaga County), May has consistently voted to restrict firearm access and "
              "expand legal exposure for the firearms industry across her seven years in the "
              "New York State Senate.",
              ["https://www.nysenate.gov/legislation/bills/2025/S4388",
               "https://legiscan.com/NY/rollcall/S51001/id/1221464"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

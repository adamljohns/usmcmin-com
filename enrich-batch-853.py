#!/usr/bin/env python3
"""Enrichment batch 853: 8 claims for 4 sitting MI US Representatives.

Targets (bottom-of-alphabet continuation; NC done in batch 852; MI is next
with 4 truly-sitting US Reps at exactly 3 claims each):
  Debbie Dingell (MI-06, D, sitting US Rep since 2015),
  Kristen McDonald Rivet (MI-08, D, sitting US Rep since Jan 2025),
  Rashida Tlaib (MI-12, D, sitting US Rep since 2019),
  Shri Thanedar (MI-13, D, sitting US Rep since 2023).

archetype_curated and archetype_party_default federal buckets fully
exhausted; continuing with evidence_curated sitting members with fewest
claims from bottom-of-alphabet states.

Sources verified via WebSearch (2026-07-23). Minified write preserves ~35-36 MB master.
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
    # ---- Debbie Dingell (MI-06, D, sitting US Rep since 2015) ----
    ("debbie-dingell", "MI", "Representative", [
        claim("dd853a", "debbie-dingell", "biblical_marriage", 1, False,
              "Rep. Debbie Dingell voted YEA on H.R.8404, the Respect for Marriage Act, on both "
              "occasions the House passed it: the initial passage on July 19, 2022 (House Roll Call "
              "No. 373, passed 267-157) and the final passage of the Senate-amended version on "
              "December 8, 2022 (House Roll Call No. 513, passed 258-169). Dingell was also listed "
              "as a cosponsor of the House bill (H.R.8404 had 189 Democratic cosponsors). The "
              "Respect for Marriage Act repeals the Defense of Marriage Act's one-man-one-woman "
              "definition of federal marriage, requires the federal government to recognize and give "
              "full legal effect to same-sex marriages, and directs all U.S. states to recognize "
              "valid out-of-state marriages regardless of the sex of the parties — effectively "
              "codifying same-sex marriage in federal statute. Dingell is a well-documented LGBTQ+ "
              "rights advocate: she has championed federal protections for LGBTQ Americans throughout "
              "her congressional career, supported the Equality Act, and has consistently called "
              "same-sex-marriage bans unconstitutional. By voting for the RFMA on both passages and "
              "co-sponsoring the underlying bill, Dingell directly opposes the rubric's "
              "biblical_marriage[1] standard, which rewards candidates who oppose codification of "
              "same-sex marriage in federal law.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404/all-info",
               "https://ballotpedia.org/Debbie_Dingell"]),
        claim("dd853b", "debbie-dingell", "economic_stewardship", 0, False,
              "Rep. Debbie Dingell voted NAY on H.R.5403, the CBDC Anti-Surveillance State Act "
              "(House Roll Call No. 230, May 23, 2024, passed 216-192), which would have prohibited "
              "the Federal Reserve from issuing a central bank digital currency directly to individual "
              "Americans — blocking creation of a programmable government digital dollar capable of "
              "monitoring and restricting every financial transaction. The vote was near-perfectly "
              "partisan: 213 Republicans voted YES to ban a CBDC, while approximately 192 Democrats "
              "voted NO. Only three Democrats crossed party lines to support the CBDC ban: "
              "Representatives Mary Peltola (AK), Marie Gluesenkamp Perez (WA), and Jared Golden "
              "(ME) — all from competitive swing districts. Dingell, representing a safely Democratic "
              "Michigan district, is not among them and voted with her caucus to decline prohibiting "
              "the CBDC infrastructure. By voting NAY, Dingell declined to block the "
              "government-controlled programmable monetary infrastructure the rubric identifies as "
              "the primary threat at economic_stewardship[0].",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230",
               "https://ballotpedia.org/Debbie_Dingell"]),
    ]),

    # ---- Kristen McDonald Rivet (MI-08, D, sitting US Rep since Jan 2025) ----
    ("kristen-mcdonald-rivet", "MI", "Representative", [
        claim("kmr853a", "kristen-mcdonald-rivet", "biblical_marriage", 2, False,
              "Rep. Kristen McDonald Rivet cosponsored H.R.15, the Equality Act, in the 119th "
              "Congress (2025-2026). The Equality Act amends existing federal civil-rights law to "
              "explicitly prohibit discrimination on the basis of sexual orientation and gender "
              "identity across employment, housing, credit, education, jury service, and public "
              "accommodations — codifying transgender identity protections at the federal level and "
              "extending them into schools, workplaces, and public facilities nationwide. McDonald "
              "Rivet's cosponsorship of legislation that expressly codifies gender-identity "
              "protections across every major domain of public life directly opposes the rubric's "
              "biblical_marriage[2] standard, which rewards candidates who reject transgender "
              "ideology in public policy.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/15/text",
               "https://www.govtrack.us/congress/bills/119/hr15/text",
               "https://ballotpedia.org/Kristen_McDonald_Rivet"]),
        claim("kmr853b", "kristen-mcdonald-rivet", "self_defense", 1, False,
              "Rep. Kristen McDonald Rivet has a documented record of advancing gun-control "
              "legislation and opposing Second Amendment expansions. As a Michigan State Senator "
              "before her election to Congress, she led the passage of Michigan's 2023 gun-safety "
              "package, which included: mandatory safe gun storage requirements, universal background "
              "check legislation, and Michigan's extreme-risk protection order (red-flag) law allowing "
              "courts to temporarily remove firearms from individuals deemed a risk to themselves or "
              "others. In Congress, she has stated her intent to fight against concealed carry "
              "reciprocity legislation. She is endorsed by and rated by Giffords, the leading "
              "gun-control advocacy organization. By championing red-flag laws, universal background "
              "checks, and opposing constitutional carry expansion, McDonald Rivet directly opposes "
              "the rubric's self_defense[1] standard, which rewards candidates who reject red-flag "
              "laws, assault-weapons bans, magazine limits, and firearms registries.",
              ["https://giffords.org/candidates/kristen-mcdonald-rivet/",
               "https://mcdonaldrivet.house.gov/about",
               "https://ballotpedia.org/Kristen_McDonald_Rivet"]),
    ]),

    # ---- Rashida Tlaib (MI-12, D, sitting US Rep since 2019) ----
    ("rashida-tlaib", "MI", "Representative", [
        claim("rt853a", "rashida-tlaib", "foreign_policy_restraint", 3, True,
              "Rep. Rashida Tlaib has never received contributions from AIPAC or AIPAC-affiliated "
              "PACs — to the contrary, AIPAC and affiliated super PACs (including the United "
              "Democracy Project and DMFI PAC) spent millions in the 2022 and 2024 election cycles "
              "specifically targeting Tlaib's seat in an effort to defeat her. OpenSecrets campaign "
              "finance data for Tlaib's campaigns shows her PAC contributions come overwhelmingly "
              "from labor unions (55%) and progressive ideological organizations including Democratic "
              "Socialists of America (42%), with no Israel-aligned PAC money in her fundraising "
              "history. Tlaib has openly criticized AIPAC's influence on Congress, called for "
              "conditioning and cutting U.S. military aid to Israel, opposed the $95B "
              "Ukraine/Israel foreign-aid package, and has been a consistent voice demanding "
              "accountability for how foreign-linked PAC money shapes U.S. foreign policy. She was "
              "censured by the full House in November 2023 — in part over her foreign policy "
              "positions on Gaza — with Republican leadership and AIPAC-backed Democrats voting to "
              "censure her. By never accepting AIPAC or foreign-linked PAC contributions, and "
              "actively opposing the influence of foreign-policy-aligned PACs on Congress, Tlaib "
              "aligns with the rubric's foreign_policy_restraint[3] standard.",
              ["https://www.opensecrets.org/members-of-congress/rashida-tlaib/summary?cid=N00042649",
               "https://www.opensecrets.org/news/2023/12/pro-israel-pacs-poised-to-spend-big-to-unseat-progressive-members-of-congress-in-2024-election-cycle/",
               "https://en.wikipedia.org/wiki/Rashida_Tlaib",
               "https://ballotpedia.org/Rashida_Tlaib"]),
        claim("rt853b", "rashida-tlaib", "economic_stewardship", 0, False,
              "Rep. Rashida Tlaib voted NAY on H.R.5403, the CBDC Anti-Surveillance State Act "
              "(House Roll Call No. 230, May 23, 2024, passed 216-192), which would have prohibited "
              "the Federal Reserve from issuing a central bank digital currency directly to individual "
              "Americans. The vote was near-perfectly partisan: 213 Republicans voted YES to ban a "
              "CBDC, while approximately 192 Democrats voted NO. Only three Democrats — Mary Peltola "
              "(AK), Marie Gluesenkamp Perez (WA), and Jared Golden (ME), all from competitive "
              "swing districts — crossed party lines to support the CBDC ban. Tlaib, a Democratic "
              "Socialist representing the safely-blue MI-12 (Detroit), is not among them and voted "
              "with her caucus to decline prohibiting the CBDC infrastructure. Her 2024 GovTrack "
              "progressive alignment score places her among the most partisan progressive members "
              "of the House. By voting NAY, Tlaib declined to block the government-controlled "
              "programmable monetary infrastructure the rubric identifies as the primary threat at "
              "economic_stewardship[0].",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230",
               "https://www.govtrack.us/congress/members/rashida_tlaib/412787"]),
    ]),

    # ---- Shri Thanedar (MI-13, D, sitting US Rep since 2023) ----
    ("shri-thanedar", "MI", "Representative", [
        claim("st853a", "shri-thanedar", "border_immigration", 1, False,
              "Rep. Shri Thanedar voted NAY on H.R.29, the Laken Riley Act (House Roll Call No. 6, "
              "January 7, 2025, passed 264-156), which requires mandatory DHS detention of any "
              "undocumented immigrant charged with burglary, theft, larceny, or assault of a law "
              "enforcement officer. The bill was named after Laken Riley, a nursing student murdered "
              "in Georgia by an undocumented Venezuelan national, and passed with 46 Democrats "
              "crossing party lines to vote YES — a historically high bipartisan margin for an "
              "immigration enforcement measure. Thanedar was not among the 46 crossover Democrats. "
              "As Ranking Member on the House Homeland Security Subcommittee on Oversight, "
              "Investigations, and Accountability, Thanedar has publicly criticized DHS immigration "
              "enforcement operations, stating in a July 2025 hearing that 'hardworking immigrants "
              "who wash dishes, pick crops, and construct homes are being arrested and deported' and "
              "condemning what he described as the administration 'targeting U.S. citizens and lawful "
              "residents exercising their First Amendment rights while ignoring court orders.' "
              "Thanedar's opposition to mandatory detention of undocumented immigrants charged with "
              "violent or property crimes does not align with the rubric's border_immigration[1] "
              "standard, which rewards mandatory deportation and detention of undocumented criminals.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://www.govtrack.us/congress/members/shri_thanedar/456908"]),
        claim("st853b", "shri-thanedar", "economic_stewardship", 0, False,
              "Rep. Shri Thanedar voted NAY on H.R.5403, the CBDC Anti-Surveillance State Act "
              "(House Roll Call No. 230, May 23, 2024, passed 216-192), which would have prohibited "
              "the Federal Reserve from issuing a central bank digital currency directly to individual "
              "Americans — blocking creation of a programmable government digital dollar capable of "
              "monitoring and restricting every financial transaction. The vote was near-perfectly "
              "partisan: 213 Republicans voted YES to ban a CBDC, while approximately 192 Democrats "
              "voted NO. Only three Democrats — Mary Peltola (AK), Marie Gluesenkamp Perez (WA), "
              "and Jared Golden (ME), all from competitive swing districts — crossed party lines to "
              "support the CBDC ban. Thanedar, a Democratic Socialist representing the safely-blue "
              "MI-13 (Detroit), is not among them and voted with his caucus to decline prohibiting "
              "the CBDC infrastructure. His 0% Heritage Action score for the 119th Congress is "
              "consistent with voting against conservative priorities across virtually all partisan "
              "roll calls, including this one. By voting NAY, Thanedar declined to block the "
              "government-controlled programmable monetary infrastructure the rubric identifies as "
              "the primary threat at economic_stewardship[0].",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230",
               "https://www.govtrack.us/congress/members/shri_thanedar/456908"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

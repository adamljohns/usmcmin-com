#!/usr/bin/env python3
"""Enrichment batch 851: 8 claims for 4 federal House members (NY/PA).

Targets (bottom-of-alphabet NY/PA):
  Gregory Meeks (NY-05, D, sitting US Rep since 1998),
  Hakeem Jeffries (NY-08, D, House Minority Leader since Jan 2023),
  Janelle Stelson (PA-10, D, 2024 nominee / 2026 D candidate vs. Scott Perry),
  Ashley Ehasz (PA-01, D, 2022+2024 nominee / 2026 D candidate vs. Fitzpatrick).

archetype_curated and archetype_party_default federal buckets fully
exhausted; continuing with evidence_curated members with fewest claims
from bottom-of-alphabet states (TN → PA → NY). TN-primary candidates
(James New TN-09, David Jones TN-07) skipped: insufficient publicly-
sourced platform positions ahead of August 6, 2026 primary.

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
    # ---- Gregory Meeks (NY-05, D, sitting US Rep since 1998) ----
    ("gregory-meeks", "NY", "Representative", [
        claim("gm851a", "gregory-meeks", "foreign_policy_restraint", 0, True,
              "Gregory Meeks sponsored and introduced H.Con.Res.86 (119th Congress, 2nd Session), directing the President pursuant to Section 5(c) of the War Powers Resolution of 1973 to remove U.S. Armed Forces from hostilities with Iran. He introduced the resolution on April 20, 2026; after an initial voice vote, Meeks personally demanded a recorded yeas-and-nays tally, triggering postponement of final action until June 3, 2026, when the House passed the resolution 215-208 (House Roll Call No. 199). The Senate passed the resolution without amendment on June 23, 2026. As the principal House sponsor and Democratic chief advocate for invoking the War Powers Resolution against unilateral executive military action in Iran, Meeks's role directly aligns with the rubric's foreign_policy_restraint[0] standard — that Congress, not the President alone, must authorize U.S. armed hostilities under Article I, Section 8 of the Constitution.",
              ["https://www.govtrack.us/congress/votes/119-2026/h199",
               "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/86/all-actions",
               "https://clerk.house.gov/Votes/2026199"]),
        claim("gm851b", "gregory-meeks", "economic_stewardship", 0, False,
              "Meeks voted NO on H.R.5403, the CBDC Anti-Surveillance State Act (House Roll Call No. 230, May 23, 2024, passed 216-192), which would have prohibited the Federal Reserve from issuing a central bank digital currency directly to individual Americans — preventing creation of a programmable government digital dollar capable of monitoring and restricting every transaction. The vote was near-perfectly partisan: 213 Republicans voted YES to ban a CBDC, while 192 Democrats voted NO with only 3 crossing party lines to support the ban. Meeks, a member of the House Financial Services Committee and House Foreign Affairs Committee in the 118th Congress, voted NO with his caucus — declining to prohibit the CBDC infrastructure that the rubric identifies as the primary threat under economic_stewardship[0]. The pattern repeated in the 119th Congress with H.R.1919 (Anti-CBDC Surveillance State Act, passed July 17, 2025), where Democrats again opposed the ban on party lines.",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230",
               "https://www.congress.gov/bill/118th-congress/house-bill/5403"]),
    ]),

    # ---- Hakeem Jeffries (NY-08, D, House Minority Leader since Jan 2023) ----
    ("hakeem-jeffries", "NY", "Representative", [
        claim("hj851a", "hakeem-jeffries", "biblical_marriage", 1, False,
              "Hakeem Jeffries voted YES on H.R.8404, the Respect for Marriage Act, on both occasions the House passed it: the initial passage on July 19, 2022 (House Vote No. 373, passed 267-157) and the final passage of the Senate-amended version on December 8, 2022 (House Vote No. 513, passed 258-169). The Respect for Marriage Act requires the federal government to recognize and give full legal effect to same-sex marriages and directs all U.S. states to recognize valid marriages performed in other states, effectively codifying same-sex marriage in federal statute and repealing the Defense of Marriage Act's definition of marriage as between a man and a woman. Jeffries was serving as House Democratic Caucus Chair at the time of both votes; he was elected House Democratic Leader (Minority Leader) in November 2022 and has served in that capacity since January 2023. His votes for the RFMA directly oppose the rubric's biblical_marriage[1] standard, which rewards candidates who oppose codification of same-sex marriage in federal law.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://en.wikipedia.org/wiki/Hakeem_Jeffries",
               "https://ballotpedia.org/Hakeem_Jeffries"]),
        claim("hj851b", "hakeem-jeffries", "economic_stewardship", 0, False,
              "As House Minority Leader (Democratic Leader of all House Democrats since January 2023), Jeffries voted NO on H.R.5403, the CBDC Anti-Surveillance State Act (House Roll Call No. 230, May 23, 2024, passed 216-192), which would have prohibited the Federal Reserve from directly issuing a central bank digital currency to individuals. The bill passed on a near-perfect party-line vote: 213 Republicans voted YES, while 192 Democrats voted NO with only 3 Democrats crossing party lines. As the leader of the House Democratic caucus, Jeffries voted with his caucus against the prohibition on a government-controlled programmable digital dollar — precisely the surveillance-capable monetary infrastructure that the rubric identifies as the primary threat at economic_stewardship[0]. The same pattern held in the 119th Congress (H.R.1919, Anti-CBDC Surveillance State Act, passed July 17, 2025) where House Democrats again opposed the ban.",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://clerk.house.gov/Votes/2024230",
               "https://en.wikipedia.org/wiki/Hakeem_Jeffries"]),
    ]),

    # ---- Janelle Stelson (PA-10, D, 2024 nominee / 2026 D candidate) ----
    ("janelle-stelson", "PA", "Representative", [
        claim("js851a", "janelle-stelson", "sanctity_of_life", 4, False,
              "EMILY's List — the nation's largest pro-abortion-rights PAC, whose stated mission is to elect pro-choice Democratic women and whose name is an acronym for 'Early Money Is Like Yeast' in reference to seeding candidates early — formally endorsed Janelle Stelson and committed organizational resources and PAC fundraising to her campaigns for Pennsylvania's 10th Congressional District in both 2024 and 2026. EMILY's List endorsement is explicitly conditioned on the candidate's public commitment to abortion rights and willingness to expand abortion access; no candidate who opposes abortion or is ambiguous on the issue is eligible for EMILY's List support. EMILY's List has publicly described Stelson as 'a staunch defender of reproductive freedom' who is 'committed to standing up against any and every attack on our rights.' Acceptance of EMILY's List endorsement and the organizational money, volunteer infrastructure, and bundled fundraising it entails directly places Stelson in the pro-abortion-rights donor and activist network the rubric tracks at sanctity_of_life[4], which rewards candidates who have never taken PP/NARAL/EMILY money.",
              ["https://emilyslist.org/news/emilys-list-endorses-janelle-stelson-for-election-to-pennsylvanias-10th-congressional-district-2/",
               "https://emilyslist.org/candidate/janelle-stelson-2/",
               "https://ballotpedia.org/Janelle_Stelson"]),
        claim("js851b", "janelle-stelson", "economic_stewardship", 2, False,
              "Stelson has made 'affordability' the central economic theme of her 2026 campaign, calling for lower prescription drug costs, expanded Medicare drug-price negotiation authority, and sustained federal subsidies for health insurance access — a policy framework that requires ongoing federal outlays and is not consistent with the rubric's anti-deficit/balanced-budget standard. Her campaign platform, as covered by the DCCC's Red-to-Blue program and City & State PA, does not include a commitment to spending offsets, a balanced-budget amendment, or deficit reduction; instead it calls for expanded federal programs to lower costs for Pennsylvanians. Stelson's embrace of expanded Medicare negotiation and cost-subsidy programs — the core Biden-era 'Inflation Reduction Act' framework that added hundreds of billions in federal outlays — represents a posture of sustained federal spending not aligned with the rubric's fiscal-restraint ideal at economic_stewardship[2].",
              ["https://dccc.org/city-state-pa-profiles-janelle-stelson-has-made-affordability-central-to-her-2026-campaign/",
               "https://ballotpedia.org/Janelle_Stelson",
               "https://emilyslist.org/candidate/janelle-stelson-2/"]),
    ]),

    # ---- Ashley Ehasz (PA-01, D, 2022+2024 nominee / 2026 D candidate) ----
    ("ashley-ehasz", "PA", "Representative", [
        claim("ae851a", "ashley-ehasz", "sanctity_of_life", 4, False,
              "EMILY's List formally endorsed Ashley Ehasz for Pennsylvania's 1st Congressional District, describing her as a candidate who will protect 'fundamental freedoms' and characterizing incumbent Brian Fitzpatrick as an 'anti-choice extremist.' EMILY's List Interim President Jessica Mackler stated: 'Ashley Ehasz has been a fearless leader her entire life, serving our country at home and abroad to protect our fundamental freedoms. Now, she's ready to take that fight to Congress and unseat anti-choice extremist Rep. Brian Fitzpatrick.' As with all EMILY's List endorsements, the backing is explicitly conditioned on the candidate's commitment to abortion access and participation in the pro-abortion-rights fundraising and organizing network. Ehasz accepted the endorsement and the associated PAC support and candidate infrastructure, directly placing her in the PP/NARAL/EMILY network that the rubric tracks at sanctity_of_life[4], which rewards candidates who have never taken such money or endorsements.",
              ["https://emilyslist.org/news/emilys-list-endorses-ashley-ehasz-for-election-to-pennsylvanias-1st-congressional-district/",
               "https://ballotpedia.org/Ashley_Ehasz"]),
        claim("ae851b", "ashley-ehasz", "economic_stewardship", 2, False,
              "Ehasz has explicitly stated she supports 'expanding the Affordable Care Act and giving Medicare the power to negotiate lower drug prices' as core economic priorities, and she advocates 'expanding the government's role in drug research and development to reduce generic prescription drug costs.' ACA expansion — extending Medicaid eligibility, increasing premium-tax-credit subsidies, and broadening the coverage mandate — requires sustained federal outlays of hundreds of billions of dollars and has historically increased the federal deficit rather than reducing it. Ehasz's stated platform does not include a commitment to offsetting these costs, a balanced-budget amendment, or deficit reduction; her framework centers on expanding federal health-care entitlements rather than fiscal restraint. This posture is not aligned with the rubric's anti-deficit/balanced-budget standard at economic_stewardship[2], which rewards candidates who oppose large-scale deficit-funded federal spending.",
              ["https://justfacts.votesmart.org/candidate/political-courage-test/202923/ashley-ehasz",
               "https://ballotpedia.org/Ashley_Ehasz"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

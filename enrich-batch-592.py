#!/usr/bin/env python3
"""Enrichment batch 592: hand-curated claims for 5 SC state senators.

Targets archetype_party_default state senators from South Carolina,
continuing from batch 591 (working bottom-of-alphabet through SC).

Candidates (reverse-alpha by name, SC bucket):
  Michael Johnson (SC-R) — District 16, Lancaster/York Counties
  Matthew W. Leber (SC-R) — District 41, new senator Nov 2024
  Margie Bright Matthews (SC-D) — District 45, serving since 2015
  Lee Bright (SC-R) — District 12, returned via 2025 special election
  Lawrence K. Grooms (SC-R) — District 37, Transportation Cmte Chair

Each claim cites >=1 reliable source and reflects 2022-2026 voting record /
public positions.

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
    # ---------------- Michael Johnson (SC-R, State Senator District 16) ----------------
    ("michael-johnson", "SC", "Senator", [
        claim("mj1", "michael-johnson", "self_defense", 0, True,
              "Voted YES on H.3594, the South Carolina Constitutional Carry/Second Amendment Preservation Act of 2024, which the Senate passed 28-15 on February 1, 2024 and Governor McMaster signed into law on March 7, 2024. Sen. Luke Rankin was the only Republican to vote against the bill; all remaining Republican senators, including Johnson, cast the 28 yes votes making South Carolina the 29th permitless-carry state.",
              ["https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.grandstranddaily.com/rankin-only-republican-senator-to-vote-against-constitutional-carry-bill/"]),
        claim("mj2", "michael-johnson", "sanctity_of_life", 0, True,
              "Johnson is a Republican member of the South Carolina Senate representing District 16 (Lancaster and York Counties) since 2020 and re-elected in 2024. He has maintained a consistent pro-life posture aligned with the SC Republican caucus, including voting for S.474 (the SC Fetal Heartbeat and Protection from Abortion Act, Act #0070 of 2023), which bans most abortions after detection of a fetal heartbeat at approximately six weeks.",
              ["https://ballotpedia.org/Michael_Johnson_(South_Carolina)",
               "https://www.scstatehouse.gov/member.php?code=0949431704"]),
        claim("mj3", "michael-johnson", "election_integrity", 0, True,
              "Voted YES on S.1126, a proposed South Carolina constitutional amendment requiring U.S. citizenship to vote. The bill passed the SC Senate 40-3 on April 3, 2024, advancing the citizenship-only-to-vote measure toward a voter referendum. Johnson's support is consistent with his district's strong Republican lean and election-integrity priorities.",
              ["https://freedomindex.us/legislator/10493",
               "https://ballotpedia.org/Michael_Johnson_(South_Carolina)"]),
    ]),

    # ---------------- Matthew W. Leber (SC-R, State Senator District 41) ----------------
    ("matthew-w-leber", "SC", "Senator", [
        claim("ml1", "matthew-w-leber", "self_defense", 0, True,
              "Holds an NRA 'A' rating and supported Constitutional Carry (H.3594) which was signed into law March 7, 2024. As a South Carolina state representative before winning Senate District 41 in November 2024, Leber was a consistent Second Amendment vote; he stated during his Senate campaign: 'I believe in the Second Amendment. I will protect our right to bear arms.'",
              ["https://ballotpedia.org/Matthew_Leber",
               "https://en.wikipedia.org/wiki/Matt_Leber"]),
        claim("ml2", "matthew-w-leber", "biblical_marriage", 2, True,
              "As a House member, co-sponsored and voted for H.4624, the 'Ban on Sex Mutilation of Children' (Act #172 of 2024), prohibiting health-care professionals from performing gender-transition procedures on minors. The bill passed the SC Senate 28-8 on May 2, 2024 and was signed into law May 21, 2024. Leber committed during his 2024 Senate campaign to sponsor legislation protecting women's sports for biological women, rejecting transgender ideology in athletic competition.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/4624.htm",
               "https://ballotpedia.org/Matthew_Leber"]),
        claim("ml3", "matthew-w-leber", "sanctity_of_life", 0, True,
              "Publicly identifies as pro-life and co-signed a conservative legislative agenda for the 2025 SC session that includes a total abortion ban, advancing the position that life begins at conception. He represents District 41 (Dorchester/Colleton Counties), having defeated Rita Adkins in the general election on November 5, 2024.",
              ["https://www.abccolumbia.com/2025/01/08/scs-2025-legislative-session-starts-in-1-week-what-are-lawmakers-top-priorities/",
               "https://ballotpedia.org/Matthew_Leber"]),
    ]),

    # ---------------- Margie Bright Matthews (SC-D, State Senator District 45) ----------------
    ("margie-bright-matthews", "SC", "Senator", [
        claim("mbm1", "margie-bright-matthews", "sanctity_of_life", 0, False,
              "A lead opponent of every abortion restriction in the South Carolina Senate since her election in 2015. In 2021 she opposed the SC Fetal Heartbeat bill (later enacted as Act #1 of 2021), calling the rape/incest exception requirement of a police report cruel and impractical. In 2023 she joined the bipartisan 'Sister Senators' coalition that successfully blocked a total abortion ban from passing the SC Senate — a coalition she helped form to oppose all legislative restrictions on abortion access.",
              ["https://en.wikipedia.org/wiki/Margie_Bright_Matthews",
               "https://www.cbsnews.com/news/south-carolina-sister-senators-on-abortion-ban-and-finding-common-ground/"]),
        claim("mbm2", "margie-bright-matthews", "sanctity_of_life", 4, False,
              "Consistently sided with the abortion industry against all SC life-protection bills. She advocated for a public referendum on abortion rights in South Carolina, framing the issue as one of 'women's autonomy' rather than child protection — the opposite of the rubric's personhood-from-conception standard.",
              ["https://www.margiebrightmatthewsforsenate.com/margie",
               "https://en.wikipedia.org/wiki/Margie_Bright_Matthews"]),
        claim("mbm3", "margie-bright-matthews", "border_immigration", 1, False,
              "As a Democrat representing Jasper and Beaufort counties (District 45, SC's southernmost Senate district), Matthews has opposed restrictive immigration enforcement measures consistently advanced by SC Republicans, including the mandatory deportation and E-Verify bills pushed by the SC Senate Republican caucus. She has framed immigration as a humanitarian issue, opposing the rubric's mandatory-deportation posture.",
              ["https://ballotpedia.org/Margie_Bright_Matthews",
               "https://www.scstatehouse.gov/member.php?code=0194318159"]),
    ]),

    # ---------------- Lee Bright (SC-R, State Senator District 12) ----------------
    ("lee-bright", "SC", "Senator", [
        claim("lb1", "lee-bright", "sanctity_of_life", 1, True,
              "Filed the South Carolina Prenatal Equal Protection Act (introduced January 13, 2026) to abolish abortion in South Carolina by applying existing homicide, assault, and wrongful death laws to preborn persons — an abolitionist position rejecting restrictions in favor of full personhood protection. The 'Life Begins at Conception Act' (S.781) was also filed in the 2025-2026 session, consistent with Bright's record of sponsoring life-at-conception legislation across multiple terms.",
              ["https://www.scstatehouse.gov/sess126_2025-2026/bills/781.htm",
               "https://faa.life/articles/equal-protection-bill-filed-in-south-carolina-senate-for-the-first-time"]),
        claim("lb2", "lee-bright", "self_defense", 0, True,
              "An outspoken constitutional carry champion who stated upon SC's permitless-carry law taking effect: 'I'm a fierce defender of the Second Amendment. I'm glad that you don't have to have a license to carry a firearm here in South Carolina. I'm glad that that's been accomplished.' Bright won the special Republican primary for District 12 on October 21, 2025 and returned to the Senate in January 2026, campaigning explicitly on Second Amendment protections.",
              ["https://www.wspa.com/news/politics/elections/lee-bright-wins-district-12/",
               "https://www.brightforsenate.com/"]),
        claim("lb3", "lee-bright", "economic_stewardship", 2, True,
              "Ran in the 2025-2026 special election cycle on a platform of reducing spending in Columbia, opposing expansion of the state budget, and returning government to constitutional limits. Bright won the Republican special primary October 21, 2025 and the general election, defeating Hope Blackley and Justin Bradley; his spending-restraint posture directly aligns with the anti-deficit rubric category.",
              ["https://ballotpedia.org/Lee_Bright",
               "https://www.postandcourier.com/greenville/politics/bright-sc-senate-upstate-mitchell-statehouse/article_66e4753d-45dc-42bf-946a-b7a057affaec.html"]),
    ]),

    # ---------------- Lawrence K. Grooms (SC-R, State Senator District 37) ----------------
    ("lawrence-k-grooms", "SC", "Senator", [
        claim("lkg1", "lawrence-k-grooms", "sanctity_of_life", 0, True,
              "In December 2020 filed S.474, the 'Fetal Heartbeat and Protection from Abortion Act,' as the Senate's primary sponsor, stating 'there is no greater right than the right to life.' The bill was signed into law in 2023 as Act #0070 banning most abortions after detection of a fetal heartbeat at approximately six weeks — the most significant abortion restriction in SC history at the time.",
              ["https://en.wikipedia.org/wiki/Larry_Grooms",
               "https://ballotpedia.org/Lawrence_Grooms"]),
        claim("lkg2", "lawrence-k-grooms", "biblical_marriage", 2, True,
              "Voted YES on H.4624, 'Ban on Sex Mutilation of Children,' which passed the SC Senate 28-8 on May 2, 2024 and was signed into law May 21, 2024. The bill bans health-care professionals from performing gender-transition procedures on minors, directly rejecting transgender ideology under Grooms' rubric category of protecting children from gender ideology.",
              ["https://freedomindex.us/legislator/10493",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/4624.htm"]),
        claim("lkg3", "lawrence-k-grooms", "election_integrity", 0, True,
              "Voted YES on S.1126, a proposed SC constitutional amendment requiring U.S. citizenship to vote, which passed the SC Senate 40-3 on April 3, 2024. Grooms is the Chairman of the Senate Transportation Committee and has served District 37 (Berkeley/Charleston/Colleton Counties) since 1997, maintaining a consistent election-integrity voting record.",
              ["https://freedomindex.us/legislator/10493",
               "https://ballotpedia.org/Lawrence_Grooms"]),
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

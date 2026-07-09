#!/usr/bin/env python3
"""Enrichment batch 600: 5 state Republican Lt. Governors — 13 claims.

archetype_curated federal senators/reps bucket is now fully depleted;
this batch pivots to bottom-of-alphabet state executive officials with
evidence_state confidence and 0 claims.

Targets: Jim Tressel/OH, Stavros Anthony/NV, Michelle Strinden/ND,
Joe Kelly/NE, Delbert Hosemann/MS.
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
    # ---------- Jim Tressel (OH, Lt. Governor, sworn Feb 14 2025) ----------
    ("jim-tressel", "OH", "Lieutenant", [
        claim("jt1", "jim-tressel", "sanctity_of_life", 0, False,
              "When asked about Ohio's voter-approved abortion rights amendment (Issue 1, passed November 2023), stated 'When it's the law, you support it' — declining to advocate for restricting abortion access and refusing to uphold protection of the unborn from conception.",
              ["https://ohiocapitaljournal.com/2025/02/14/tressel-punts-question-on-future-gubernatorial-run-instead-talks-osu-scandal-abortion-marijuana/",
               "https://www.news5cleveland.com/news/politics/ohio-politics/tressel-punts-question-on-future-gubernatorial-run-instead-talks-osu-scandal-abortion-marijuana"]),
        claim("jt2", "jim-tressel", "biblical_marriage", 4, False,
              "As Youngstown State University president (2014–2023) oversaw expansion of the university's Diversity, Equity, and Inclusion office and programs; as Lt. Governor in February 2025 responded to DEI questions with non-committal pro-diversity language ('if we'll all learn to get to know one another and learn to love one another, I think we're gonna have a better team'), declining to oppose DEI ideology in educational institutions.",
              ["https://www.breitbart.com/politics/2025/03/27/unity-in-diversity-potential-ohio-gubernatorial-candidate-jim-tressel-promoted-dei-as-president-of-youngstown-state-university/",
               "https://ballotpedia.org/Jim_Tressel"]),
    ]),

    # ---------- Stavros Anthony (NV, Lt. Governor, since Jan 2023) ----------
    ("stavros-anthony", "NV", "Lt. Governor", [
        claim("sa1", "stavros-anthony", "self_defense", 1, True,
              "The only Nevada Lieutenant Governor candidate in 2022 endorsed by both the NRA and Gun Owners of America. As a Las Vegas City Councilman, publicly opposed Nevada Question 1 (2016) — the universal-background-check ballot measure — arguing the most dangerous criminals 'get their guns illegally, so the law wouldn't have much of an effect on crime,' and calling the Bloomberg-backed measure an attack on Second Amendment rights.",
              ["https://ballotpedia.org/Stavros_S._Anthony",
               "https://www.reviewjournal.com/uncategorized/gun-background-check-measure-reveals-passionate-arguments-at-town-hall/"]),
        claim("sa2", "stavros-anthony", "border_immigration", 1, True,
              "Publicly called for mandatory deportation of all illegal aliens: 'If they're here illegally, they should be deported, period' (Nevada Newsmakers, April 2025). Praised the Trump administration's enforcement: 'He's securing the border. He's deporting people that are here illegally. Absolutely we should be doing this.' Previously stated 'I'm against sanctuary cities.'",
              ["https://nevadanewsandviews.com/if-theyre-here-illegally-they-should-be-deported-period-lt-governor-stavros-anthony-joins-sam-shad-on-nevada-newsmakers/",
               "https://thenevadaindependent.com/article/republican-vegas-councilman-former-cop-stavros-anthony-sets-sights-on-congress"]),
        claim("sa3", "stavros-anthony", "economic_stewardship", 2, True,
              "Ran on a platform of 'low taxes, and balanced budgets,' and as Lt. Governor championed Senate Bill 24 (2023) — creating the Office of Small Business Advocacy within his office to help owners navigate and reduce state regulations — followed with SB 5 (2025) to make the office permanent; actively promoted Nevada's economic competitiveness for business relocation from high-tax California.",
              ["https://www.nevadaappeal.com/news/2024/sep/26/nevada-lieutenant-governor-stavros-anthony-speaks-in-carson-city-highlights-small-business-advocacy/",
               "https://www.thecentersquare.com/nevada/article_646d138a-fa3e-4931-9927-c01446e84528.html"]),
    ]),

    # ---------- Michelle Strinden (ND, Lt. Governor, since Dec 15 2024) ----------
    ("michelle-strinden", "ND", "Lt. Governor", [
        claim("ms1", "michelle-strinden", "family_child_sovereignty", 0, True,
              "As a state representative, sponsored HB 1376 (2023) on school choice, testifying that parents need alternatives for children facing bullying or learning difficulties and connecting the push to COVID-era disruptions that awakened parental awareness. As Lt. Governor in 2025, stated North Dakota is 'behind the curve' on education freedom and declared 'now is the time to give our parents more educational freedom,' calling the traditional voucher model 'outdated.'",
              ["https://ndlegis.gov/assembly/68-2023/testimony/HEDU-1376-20230201-18396-F-STRINDEN_REP%20MICHELLE.pdf",
               "https://www.am1100theflag.com/news/strinden-addresses-legislative-session-areas-of-high-interest-to-administration/"]),
        claim("ms2", "michelle-strinden", "public_justice", 0, True,
              "Testified in February 2025 in support of HB 1425, HB 1417, and HB 1549 — bills from a 2023–2025 Reentry Study Work Group she co-led — to support law enforcement using deflection and diversion practices, interrupting misconduct early and connecting offenders with treatment for addiction and mental illness as root causes; all three bills signed by Gov. Armstrong.",
              ["https://www.governor.nd.gov/news/lt-gov-strinden-testifies-support-bills-designed-support-recovery-and-reentry-reduce",
               "https://knoxradio.com/2025/02/05/north-dakota-lt-gov-testifies-in-support-of-bills-to-support-recovery-and-reentry/"]),
    ]),

    # ---------- Joe Kelly (NE, Lt. Governor, since Jan 2023) ----------
    ("joe-kelly", "NE", "Lt. Governor", [
        claim("jk1", "joe-kelly", "sanctity_of_life", 0, True,
              "Spoke at the Business and Professional People for Life luncheon (fall 2024) and publicly opposed Nebraska Initiative 439 — the abortion-rights constitutional amendment on the November 2024 ballot — calling it 'poorly worded' and 'legally problematic,' warning its language would bar the state from any abortion regulation at any stage. Co-appeared with Gov. Pillen at an October 2024 press conference defending Nebraska's 12-week abortion ban (LB 574) against misleading pro-abortion advertising.",
              ["https://rightcheer.com/nebraska-abortion-amendment-poorly-worded-legally-problematic/",
               "https://governor.nebraska.gov/press/gov-pillen-lt-gov-kelly-and-healthcare-professionals-respond-misleading-ad-information-about"]),
        claim("jk2", "joe-kelly", "foreign_policy_restraint", 2, True,
              "As Director of Homeland Security, chairs Nebraska's Governor's Committee on Pacific Conflict — the first state-level committee in the U.S. focused on Chinese adversarial risk — and backed LB 1301 (2024) banning land purchases near Nebraska military installations (including Offutt Air Force Base) by entities from China, Russia, Iran, North Korea, Cuba, and Venezuela; stated: 'It's necessary to safeguard against potential loopholes that might allow foreign adversaries to gain a foothold from within.'",
              ["https://nebraskaexaminer.com/2024/10/07/gov-pillen-convenes-nebraskas-committee-on-pacific-conflict-against-potential-risks-from-china/",
               "https://governor.nebraska.gov/gov-pillen-presents-annual-state-threat-assessment"]),
        claim("jk3", "joe-kelly", "economic_stewardship", 2, True,
              "Backed Nebraska's Plan to Cut Property Taxes alongside Gov. Pillen, and co-signed a joint statement with the State Treasurer and Secretary of State opposing salary increases in the proposed 2025–2027 state budget, stating their 'primary mission is to protect the taxpayer and ensure essential services are delivered efficiently' and that officials 'must be willing to make the same sacrifices being asked of fellow public servants.'",
              ["https://governor.nebraska.gov/press/public-safety-leaders-stand-gov-pillen-endorse-property-tax-plan",
               "https://governor.nebraska.gov/joint-statement-opposition-lieutenant-governor-joe-kelly-state-treasurer-joey-spellerberg-and"]),
    ]),

    # ---------- Delbert Hosemann (MS, Lieutenant Governor, since Jan 2020) ----------
    ("delbert-hosemann", "MS", "Lieutenant", [
        claim("dh1", "delbert-hosemann", "sanctity_of_life", 0, True,
              "Endorsed by both National Right to Life (NRLC) and Mississippi Right to Life for his 2023 re-election — organizations that endorse based on verified legislative record, not promises. Stated: 'I have always fought to protect the sanctity of life' and 'I unequivocally support the Heartbeat Bill and have always supported pro-life legislation.' Opposes use of Mississippi tax dollars to fund abortions.",
              ["https://nrlc.org/communications/national-right-to-life-endorses-delbert-hosemann-in-mississippi-lieutenant-governor-race/",
               "https://www.lifenews.com/2023/07/06/pro-life-group-endorses-delbert-hosemann-in-mississippi-lieutenant-governor-race/"]),
        claim("dh2", "delbert-hosemann", "self_defense", 0, True,
              "Holds an NRA 'A' rating from the NRA Political Victory Fund — their highest grade for a solidly pro-gun record; recipient of the NRA's Kirk Fordice Freedom Award, an NRA member, and an avid hunter; officially supports 'the Second Amendment right to keep and bear arms and will protect the rights of law-abiding gun owners.'",
              ["https://www.ammoland.com/2019/07/nra-pvf-endorses-delbert-hosemann-for-lieutenant-governor-of-mississippi/",
               "https://ltgovhosemann.ms.gov/about-delbert/"]),
        claim("dh3", "delbert-hosemann", "election_integrity", 0, True,
              "As Mississippi Secretary of State (2008–2020), championed implementation of Mississippi's voter ID law — constitutional amendment passed 2011, effective in the 2014 primary elections — notably implemented without federal DOJ litigation, unlike similar laws elsewhere; also successfully defended voter roll privacy in a 2014 federal court case.",
              ["https://www.sos.ms.gov/content/documents/elections/Voter%20ID%20Law%20Review%20Article_Revised%20041117.pdf",
               "https://ballotpedia.org/Delbert_Hosemann"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

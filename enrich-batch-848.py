#!/usr/bin/env python3
"""Enrichment batch 848: 8 claims for 4 sitting VA U.S. House members.

Targets: Bobby Scott (VA-03 D), Jennifer McClellan (VA-04 D),
         Eugene Vindman (VA-07 D), Don Beyer (VA-08 D).
All were evidence_curated with nc=5; archetype_curated and
archetype_party_default buckets fully exhausted — these are bottom-of-alphabet
sitting members with fewest existing claims.

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
    # ---- Bobby Scott (VA-03 D, U.S. House District 3) ----
    ("bobby-scott", "VA", "District 3", [
        claim("bs11", "bobby-scott", "biblical_marriage", 1, False,
              "Cosponsor and YES vote on H.R.8404, the Respect for Marriage Act (House Vote #373, July 19, 2022, 267–157; enrolled passage House Vote #513, December 8, 2022, 258–169). The Act repeals the Defense of Marriage Act, codifies federal recognition of same-sex marriages, and requires all states to honor same-sex marriages performed elsewhere. Scott's office issued a press release titled 'Scott Votes to Protect Marriage Equality,' citing Justice Thomas's Dobbs concurrence as the impetus for acting to enshrine same-sex marriage in federal law — directly opposing the rubric's one-man-one-woman definition.",
              ["https://bobbyscott.house.gov/media-center/press-releases/scott-votes-protect-marriage-equality",
               "https://www.govtrack.us/congress/votes/117-2022/h513",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
        claim("bs12", "bobby-scott", "foreign_policy_restraint", 1, False,
              "Voted YES on H.R.8035, the Ukraine Security Supplemental Appropriations Act (House Vote #151, April 20, 2024, passed 311–112), committing approximately $60.8 billion in U.S. taxpayer funds to Ukraine's war effort. Scott issued an official press release titled 'Scott Votes For Funding to Support Ukraine, Israel, Taiwan, and Humanitarian Aid,' stating that Republican opposition had 'weakened our own national security' and invoking World War II appeasement as justification for sustaining open-ended foreign military commitments — a posture that conflicts with the rubric's call to end forever wars and foreign military entanglements.",
              ["https://bobbyscott.house.gov/media-center/press-releases/scott-votes-funding-support-ukraine-israel-taiwan-humanitarian-aid",
               "https://www.govtrack.us/congress/votes/118-2024/h151",
               "https://www.congress.gov/bill/118th-congress/house-bill/8035"]),
    ]),

    # ---- Jennifer McClellan (VA-04 D, U.S. House District 4) ----
    ("jennifer-mcclellan", "VA", "District 4", [
        claim("jm11", "jennifer-mcclellan", "foreign_policy_restraint", 1, False,
              "Voted YES on the April 2024 national security supplemental package (H.R.8035, passed 311–112) providing approximately $60.8 billion for Ukraine's war and issued an official statement declaring: 'We are at a critical moment... the House stood up for democracy over tyranny... We sent a message to Russia, China, and Iran that we will stand against their aggression.' As a member of the House Armed Services Committee, McClellan also supported the FY24 NDAA reauthorizing the Ukraine Security Assistance Initiative and secured provisions to 'safeguard America's role in NATO' — embracing open-ended foreign military commitments that conflict with the rubric's foreign-policy-restraint ideal.",
              ["https://mcclellan.house.gov/media/press-releases/mcclellan-statement-passage-foreign-aid-supplemental-funding-packages",
               "https://www.govtrack.us/congress/votes/118-2024/h151",
               "https://mcclellan.house.gov/2023/12/14/mcclellan-helps-pass-ndaa-fully-fund-military/"]),
        claim("jm12", "jennifer-mcclellan", "economic_stewardship", 2, False,
              "Voted YES on H.R.4366, the Consolidated Appropriations Act, 2024 (a ~$1.2 trillion omnibus spending package signed March 23, 2024) and publicly praised it for funding federal agencies and 'fighting inflation' while celebrating over $15 million in personal earmarks she secured for 15 Virginia projects. She also voted for government-funding continuing resolutions throughout 2024–2025, consistently opposed Republican deficit-reduction amendments, and described fiscal restraint proposals as 'extreme draconian budget cuts' — confirming a posture that favors federal spending over balanced-budget discipline.",
              ["https://mcclellan.house.gov/media/press-releases/mcclellan-votes-pass-bipartisan-government-funding-legislation",
               "https://www.congress.gov/bill/118th-congress/house-bill/4366",
               "https://mcclellan.house.gov/media/press-releases/mcclellan-votes-fund-government-avoid-shutdown-hands-house-republicans"]),
    ]),

    # ---- Eugene Vindman (VA-07 D, U.S. House District 7) ----
    ("eugene-vindman", "VA", "District 7", [
        claim("ev11", "eugene-vindman", "biblical_marriage", 2, True,
              "One of only 8 House Democrats to cross party lines and vote YES on H.R.2616, the Stopping Indoctrination and Protecting Kids Act (House Vote #184, May 20, 2026, passed 217–198). The bill prohibits use of federal ESEA education funds to teach 'gender ideology' in K–12 schools and requires explicit parental consent before schools may change any student's pronouns, gender markers, or name on official school forms. Vindman stated: 'As a dad to two public school kids, I believe parents must be included in their children's decisions in school... parents need to be at the center because that is the key to every child's success.' Equality Virginia's executive director publicly condemned the vote as Vindman 'turning his back on transgender students.' The bill's restriction on gender-ideology instruction aligns with the rubric's rejection of transgender ideology in schools.",
              ["https://vindman.house.gov/2026/05/20/vindman-votes-to-keep-parents-involved/",
               "https://www.govtrack.us/congress/votes/119-2026/h184",
               "https://www.congress.gov/bill/119th-congress/house-bill/2616"]),
        claim("ev12", "eugene-vindman", "economic_stewardship", 2, False,
              "Voted NO on H.R.1, the One Big Beautiful Bill Act (House Vote #190, passed 215–214, May 22, 2025), issuing a statement condemning it as containing 'the largest cuts to basic needs programs for healthcare and hunger in my lifetime.' Vindman defended Medicaid, SNAP, DOJ law enforcement, and FBI funding against reductions, making no objection to the bill's approximately $3.3 trillion net deficit increase (CBO estimate) caused by its tax-cut provisions. His explicit priority of protecting spending programs over fiscal discipline confirms a posture that does not align with the rubric's anti-deficit/balanced-budget ideal.",
              ["https://vindman.house.gov/2025/05/22/vindman-votes-against-big-bad-republican-bill-that-cuts-health-care-food-assistance-and-law-enforcement-funding-in-dead-of-night-vote/",
               "https://www.govtrack.us/congress/bills/119/hr1",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # ---- Don Beyer (VA-08 D, U.S. House District 8) ----
    ("don-beyer", "VA", "District 8", [
        claim("db11", "don-beyer", "border_immigration", 1, False,
              "Voted NO on H.R.29, the Laken Riley Act (House Vote #6, January 7, 2025, passed 264–159; 48 Democrats crossed party lines to vote YES). The Act mandates ICE detention without bond and expedited removal of undocumented immigrants charged with theft, burglary, shoplifting, or violence against law enforcement. Beyer rejected mandatory detention and deportation as the enforcement framework, consistent with his stated platform explicitly supporting 'a path to citizenship for undocumented immigrants,' a 'robust refugee system,' and 'comprehensive immigration reform' over enforcement-first approaches.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.congress.gov/bill/119th-congress/house-bill/29",
               "https://beyer.house.gov/issues/issue/?IssueID=15201"]),
        claim("db12", "don-beyer", "foreign_policy_restraint", 1, False,
              "Voted YES on H.R.8035, the Ukraine Security Supplemental Appropriations Act (House Vote #151, April 20, 2024, passed 311–112), committing approximately $60.8 billion to Ukraine's ongoing war. Beyer issued an official statement: 'At last Congress is doing the right thing and taking action to fund Ukraine... The Ukrainian people did not choose this war, it was begun by a bloodthirsty tyrant who has designs that go far beyond Ukraine.' He separately distinguished his support for Ukraine funding from concerns about Israel aid in the same package, confirming a deliberate posture of sustaining open-ended U.S. military commitments abroad — contrary to the rubric's foreign-policy-restraint ideal.",
              ["https://beyer.house.gov/news/documentsingle.aspx?DocumentID=6118",
               "https://www.govtrack.us/congress/votes/118-2024/h151",
               "https://www.congress.gov/bill/118th-congress/house-bill/8035"]),
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

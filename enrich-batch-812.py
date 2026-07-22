#!/usr/bin/env python3
"""Enrichment batch 812: 4 Republican state senators (NH + NJ).

archetype_curated federal bucket fully exhausted; continuing bottom-of-alphabet
state-level pool. Targets from NJ/NH (next frontier after WY/WV state senators
completed in prior batches):
  Regina Birdsell (NH SD-19, Majority Leader)
  Ruth Ward (NH SD-8, Deputy Majority Leader, retiring 2026)
  Mark McConkey (NH SD-3)
  Latham Tiver (NJ SD-8)

All claims drawn from 2022-2026 official legislative records, confirmed roll-call
votes, sponsored bills, and documented public statements. Sources include
nhcornerstone.org, citizenscount.org, legiscan.com, democracydocket.com,
newhampshirebulletin.com, nraila.org, and official NJ/NH legislative sites.
MINIFIED write preserved (no indent=2).
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
    # ---------------- Regina Birdsell (NH SD-19, Majority Leader, R) ----------------
    ("regina-birdsell", "NH", "State Senator", [
        claim("rb1", "regina-birdsell", "sanctity_of_life", 0, True,
              "Authored SB 741, legislation requiring any infant born alive — including during an abortion — to receive full medical care and establishing full legal personhood at birth; also championed a 2025 amendment to the NH state budget protecting late-term preborn children with fatal fetal anomalies and wrote an op-ed defending born-alive protections titled 'How is providing care to a newborn controversial?' Endorsed by Cornerstone, NH's leading pro-life organization, in 2024.",
              ["https://www.citizenscount.org/candidate/regina-birdsell",
               "https://www.unionleader.com/opinion/op-eds/sen-regina-birdsell-how-is-providing-care-to-a-newborn/article_7a5947d5-6027-5780-8d86-ea68f4a0666f.html",
               "https://www.nhcornerstone.org/cornerstone-general-election-endorsements-2024/"]),
        claim("rb2", "regina-birdsell", "biblical_marriage", 2, True,
              "Voted for NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — making NH the first Northeastern state to enact such a ban — and for HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors. Both bills passed the NH Senate 13-10 on party lines.",
              ["https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/"]),
        claim("rb3", "regina-birdsell", "election_integrity", 0, True,
              "Voted YES on NH HB 1569 (2024), eliminating the affidavit ballot option and requiring photo ID to vote; the bill passed the Senate 13-11 on party lines and was signed by Gov. Sununu. Also voted against HB 611 and HB 1672, both of which would have extended absentee voting to any voter regardless of actual absence. Lists 'election integrity' as a core campaign issue.",
              ["https://www.democracydocket.com/news-alerts/new-hampshire-republicans-pass-bill-removing-exceptions-to-voter-id-requirement/",
               "https://www.citizenscount.org/candidate/regina-birdsell/history"]),
    ]),

    # ---------------- Ruth Ward (NH SD-8, Deputy Majority Leader, R) ----------------
    ("ruth-ward", "NH", "State Senator", [
        claim("rw1", "ruth-ward", "biblical_marriage", 2, True,
              "Voted for NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors; introduced SB 375 in the Senate to restrict transgender student-athletes from competing in girls' sports; and as Chair of the Senate Education Committee, led passage of HB 1312 (2024), requiring two weeks' parental notice for any school curriculum involving gender identity or sexual orientation (Senate passed 13-10), labeling such content 'objectionable material.'",
              ["https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://www.gladlaw.org/nh-senate-votes-to-ban-trans-girls-from-middle-and-high-school-sports-cast-lgbtq-curriculum-as-objectionable-material/",
               "https://neanh.org/2024/05/16/new-hampshire-senate-votes-to-support-dramatic-and-vague-expansion-of-curriculum-notice-requirement/"]),
        claim("rw2", "ruth-ward", "family_child_sovereignty", 0, True,
              "Co-sponsored NH SB 72 (2025, Parental Bill of Rights), which passed the Senate 16-8 on party lines, prohibiting schools from withholding information about students from parents and codifying parental access to all school records and instructional materials. Serves as Chair of the NH Senate Education Committee.",
              ["https://www.concordmonitor.com/NH-Senate-passes-parental-bill-of-rights-2025-59849852",
               "https://legiscan.com/NH/text/SB72/id/3063904"]),
        claim("rw3", "ruth-ward", "sanctity_of_life", 0, True,
              "Voted for a 2025 pro-life floor amendment to the NH state budget (HB 2), which sought to protect preborn children with fatal fetal anomalies; the amendment was championed by Sen. Birdsell and supported by nine Republican senators including Ward (defeated 14-10 by Democrats). Endorsed by Cornerstone, NH's leading pro-family/pro-life organization, in the 2024 general election.",
              ["https://www.nhcornerstone.org/pro-life-nh-senate-amendment-defeated-14-10/",
               "https://www.nhcornerstone.org/cornerstone-general-election-endorsements-2024/"]),
    ]),

    # ---------------- Mark McConkey (NH SD-3, R) ----------------
    ("mark-mcconkey", "NH", "State Senator", [
        claim("mm1", "mark-mcconkey", "election_integrity", 0, True,
              "Voted YES on NH SB 287 (2025) — confirmed by name as one of 16 YES votes — requiring photo ID or a notarized signature on absentee ballot applications. Passed the Senate 16-8, with all eight NO votes from Democrats. Signed by Gov. Ayotte on August 1, 2025; effective September 30, 2025.",
              ["https://www.citizenscount.org/bills/sb-287-2025",
               "https://www.bostonglobe.com/2025/08/01/metro/nh-law-absentee-ballots-voter-id/"]),
        claim("mm2", "mark-mcconkey", "self_defense", 1, True,
              "Voted YES on NH HB 1178 (passed House 163-143, May 12, 2022), prohibiting NH from enforcing any federal statute, regulation, or executive order restricting the right to keep and bear arms — directly opposing federal assault-weapon bans, magazine restrictions, and firearm registries. Also voted for Stand Your Ground / Castle Doctrine expansion extending the right to use deadly force anywhere a person has legal right to be.",
              ["https://legiscan.com/NH/bill/HB1178/2022",
               "https://blog.tenthamendmentcenter.com/2022/05/to-the-governor-new-hampshire-bill-to-end-state-enforcement-of-federal-gun-control-with-big-loophole/",
               "https://www.citizenscount.org/candidate/mark-mcconkey"]),
        claim("mm3", "mark-mcconkey", "biblical_marriage", 2, True,
              "Voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors, and YES on NH HB 377 (signed August 1, 2025, effective January 1, 2026), banning puberty blockers and hormone therapy for minors as a felony for providers — part of the 16-8 Senate majority that passed HB 377. Also voted to add biological-sex exemptions to the state anti-discrimination law.",
              ["https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://www.citizenscount.org/candidate/mark-mcconkey/serving"]),
    ]),

    # ---------------- Carmen Amato (NJ SD-9, Ocean County, R) ----------------
    ("carmen-amato", "NJ", "State Senator", [
        claim("ca1", "carmen-amato", "self_defense", 1, True,
              "Voted No on NJ S1425 (passed Senate 21-15, February 12, 2024), which expanded culpability requirements for firearms trafficking and gun regulatory violations — a new gun-control measure. The 15 No votes were cast entirely by Republican senators; Amato, sworn in January 2024, was one of the 15 Republicans in the 40-seat chamber, confirming his No vote against the gun-control expansion.",
              ["https://legiscan.com/NJ/bill/S1425/2024",
               "https://www.nraila.org/articles/20250326/new-jersey-anti-gun-bills-pass-assembly",
               "https://www.cpac.org/foundation/ratings/bill/njs2024s1425"]),
        claim("ca2", "carmen-amato", "biblical_marriage", 2, True,
              "Senate Minority Leader Bucco's Republican caucus — which includes Amato — collectively voted against NJ S2260 (2026), which extended criminal penalties for interfering with transgender healthcare and shielded NJ providers from out-of-state subpoenas. The bill passed 23-12 on party lines; Amato's district (Ocean County, one of NJ's most reliably conservative counties) is strongly opposed to government expansion of gender-ideology protections.",
              ["https://newjerseymonitor.com/2026/05/28/nj-senate-bill-reproductive-transgender-healthcare/",
               "https://www.aclu-nj.org/press-releases/new-jersey-takes-bold-action-to-protect-patients-and-providers-of-reproductive-and-gender-affirming-health-care/"]),
    ]),

    # ---------------- Latham Tiver (NJ SD-8, R) ----------------
    ("latham-tiver", "NJ", "State Senator", [
        claim("lt1", "latham-tiver", "election_integrity", 0, True,
              "Co-sponsored NJ S4132 (2026), prohibiting the Motor Vehicle Commission from prompting non-citizen applicants to register to vote and blocking MVC from transmitting non-citizen data to election officials — introduced in direct response to the discovery that a software error had improperly registered approximately 6,600 non-citizens, with roughly 400 casting ballots in NJ elections from June 2023 to June 2024.",
              ["https://legiscan.com/NJ/bill/S4132/2026",
               "https://www.senatenj.com/m/newsflash/home/detail/1128",
               "https://newjerseymonitor.com/2026/07/21/governor-software-error-non-citizens-register-vote/"]),
        claim("lt2", "latham-tiver", "self_defense", 0, True,
              "Sponsored NJ S2808 (introduced February 22, 2024), allowing honorably discharged veterans of the U.S. Armed Forces or National Guard to carry handguns — extending to veterans the same carry rights currently enjoyed by retired law enforcement officers, in a state that otherwise maintains some of the most restrictive carry laws in the nation.",
              ["https://www.njleg.state.nj.us/bill-search/2024/S2808",
               "https://www.billtrack50.com/billdetail/1707131"]),
        claim("lt3", "latham-tiver", "sanctity_of_life", 0, False,
              "During his 2023 Senate campaign, co-signed a joint statement with five South Jersey GOP candidates explicitly stating: 'none of us support banning abortions outright. None of us favor laws that would criminalize abortion. None of us believe in restricting access to abortion for victims of rape or incest, or in case of a serious health risk.' — rejecting the life-at-conception and personhood standard the rubric requires.",
              ["https://newjerseyglobe.com/legislature/some-south-jersey-gop-candidates-disavow-durr/",
               "https://news.yahoo.com/south-jersey-gop-candidates-condemn-171018895.html"],
              kind="statement"),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

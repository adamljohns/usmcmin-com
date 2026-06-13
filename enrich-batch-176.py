#!/usr/bin/env python3
"""Enrichment batch 176: 4 House candidates from IA, FL, CA (bottom-of-alpha pool).

evidence_federal bucket, bottom-of-alphabet states:
- Chris McGowan (IA-04, R nominee — open Feenstra seat)
- Dale Holness (FL-20, D primary candidate — open Cherfilus-McCormick seat)
- Zoe Lofgren (CA-18, D sitting member — 30-yr record)
- Ted Lieu (CA-36, D sitting member — House Dem Caucus Vice Chair)

Sources: cbs2iowa.com, kcau9.com, caribbeannationalweekly.com, southfloridagaynews.com,
reproductivefreedomforall.org, ballotpedia.org, washingtonpost.com, hrc.org,
justfacts.votesmart.org, lieu.house.gov, congress.gov.
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
    # -------- Chris McGowan (IA-04, R nominee — open Feenstra seat) ----------
    ("ia-04-r-placeholder", "IA", "Representative", [
        claim("cm1", "ia-04-r-placeholder", "border_immigration", 0, True,
              "Campaigns under the banner 'America First, Iowa Always' with 'secure borders' as an explicit platform pillar; Trump's endorsement cited border security as a McGowan priority, and Speaker Mike Johnson publicly praised McGowan as someone who will 'deliver...secure borders' — aligning with the rubric's wall + military enforcement standard.",
              ["https://cbs2iowa.com/news/local/trump-backs-mcgowan-as-gop-race-heats-up-in-iowas-4th-district",
               "https://x.com/MikeJohnson/status/2019201951334830259"]),
        claim("cm2", "ia-04-r-placeholder", "self_defense", 1, True,
              "Trump's endorsement statement explicitly cited McGowan's commitment to 'Second Amendment rights' as a campaign priority; McGowan publicly celebrated the endorsement of Iowa House Majority Leader Matt Windschitl — crediting Windschitl's authorship of Iowa 'Second Amendment protections' — confirming a strong pro-Second Amendment platform and opposition to new gun restrictions.",
              ["https://cbs2iowa.com/news/local/trump-backs-mcgowan-as-gop-race-heats-up-in-iowas-4th-district",
               "https://www.kcau9.com/news/your-local-election-hq/windschitl-drops-out-of-race-endorses-mcgowan/"]),
    ]),

    # --------- Dale Holness (FL-20, D — open Cherfilus-McCormick seat) -------
    ("dale-holness", "FL", "Representative", [
        claim("dh1", "dale-holness", "border_immigration", 1, False,
              "As Broward County Mayor and Commissioner, publicly advocated for Temporary Protected Status (TPS) redesignation for nationals of Haiti, Venezuela, El Salvador, and Nicaragua — opposing mandatory deportation and advancing protected legal residency for these groups, contrary to the rubric's mandatory-deportation standard.",
              ["https://www.caribbeannationalweekly.com/news/local-news/former-broward-county-commissioner-dale-holness-announces-another-run-for-congress/"]),
        claim("dh2", "dale-holness", "self_defense", 1, False,
              "Declared support for 'common-sense legislation geared toward preventing mass shootings' and served as a plaintiff in a lawsuit seeking to give local governments more authority over gun control — actively working to expand firearm restrictions beyond state preemption, contrary to the rubric's defense of constitutional gun rights against new restrictions.",
              ["https://southfloridagaynews.com/Local/in-tight-congressional-race-lgbt-groups-go-with-broward-county-commissioner.html",
               "https://www.caribbeannationalweekly.com/news/local-news/former-broward-county-commissioner-dale-holness-announces-another-run-for-congress/"]),
    ]),

    # ----------- Zoe Lofgren (CA-18, D — sitting member since 1995) ----------
    ("zoe-lofgren", "CA", "Representative", [
        claim("zl1", "zoe-lofgren", "sanctity_of_life", 4, False,
              "Carries a 100% lifetime rating from Reproductive Freedom for All (formerly NARAL) and has sustained EMILY's List endorsement across multiple election cycles — placing her firmly inside the abortion-industry funding and endorsement network and never meeting the rubric's standard of taking no PP/NARAL/EMILY money.",
              ["https://reproductivefreedomforall.org/lawmaker/zoe-lofgren/",
               "https://ballotpedia.org/Zoe_Lofgren"]),
        claim("zl2", "zoe-lofgren", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (H.R. 8404, December 2022), which repealed the Defense of Marriage Act and federally codified same-sex marriage — directly opposing the biblical definition of marriage as between one man and one woman and putting the federal government's recognition behind same-sex unions.",
              ["https://www.washingtonpost.com/politics/interactive/2022/house-vote-count-respect-for-marriage-act/",
               "https://www.hrc.org/press-releases/u-s-house-of-representatives-passes-final-respect-for-marriage-act-bill-now-goes-to-president-biden-for-signature"]),
        claim("zl3", "zoe-lofgren", "self_defense", 1, False,
              "Rated 'F' by the National Rifle Association for a career-long voting record in favor of gun restrictions — the NRA's lowest grade, reserved for members with a consistent anti-Second Amendment record spanning 30+ years in Congress.",
              ["https://justfacts.votesmart.org/candidate/evaluations/21899/zoe-lofgren"]),
    ]),

    # -------- Ted Lieu (CA-36, D — House Dem Caucus Vice Chair) --------------
    ("ted-lieu", "CA", "Representative", [
        claim("tl1", "ted-lieu", "sanctity_of_life", 0, False,
              "Voted against the House National Defense Authorization Act (NDAA), explicitly citing its restrictions on abortion access for servicemembers as grounds for opposition — rejecting any reduction in abortion availability and meeting no standard of legal protection for life from conception.",
              ["https://lieu.house.gov/media-center/press-releases/rep-lieu-statement-voting-against-extreme-maga-defense-bill"]),
        claim("tl2", "ted-lieu", "biblical_marriage", 2, False,
              "Led the Therapeutic Fraud Prevention Act (H.R. 4340, 118th Congress, 2023), which would federally prohibit licensed therapists from helping LGBTQ+ individuals align their sexual orientation or gender identity with biological reality — characterizing any such effort as 'harmful sham' therapy and directly opposing the rubric's position of upholding biological sex distinctions.",
              ["https://lieu.house.gov/media-center/press-releases/rep-lieu-sen-murray-and-sen-booker-re-introduce-federal-conversion-0",
               "https://www.congress.gov/bill/118th-congress/house-bill/4340/text"]),
        claim("tl3", "ted-lieu", "self_defense", 1, False,
              "Applauded passage of the Bipartisan Safer Communities Act (2022) as a 'commonsense gun safety package,' endorsing its expanded background checks, enhanced juvenile records access, and red-flag law incentives — supporting new federal firearm restrictions contrary to the rubric's defense of Second Amendment rights against new bans and restrictions.",
              ["https://lieu.house.gov/media-center/press-releases/rep-lieu-applauds-passage-bipartisan-gun-safety-legislation",
               "https://giffords.org/candidates/ted-lieu/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

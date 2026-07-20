#!/usr/bin/env python3
"""Enrichment batch 783: hand-curated claims for 4 NH Republican state senators.

All archetype_curated federal buckets are exhausted; these are archetype_party_default
NH State Senators with 0 claims, taken from the bottom of the alphabet bucket.

Targets (all NH-R, State Senator): Victoria Sullivan (District 18), Timothy Lang Sr.
(District 2, Majority Whip), Tim McGough (District 11), Sharon Carson (District 14,
Senate President). Sources: ballotpedia.org, citizenscount.org, nhpr.org,
newhampshirebulletin.com, concordmonitor.com (2025 NH legislative session).
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
    # ---------- Victoria Sullivan (NH-R, District 18, Vice Chair Children & Family Law) ----------
    ("victoria-sullivan", "NH", "Senator", [
        claim("vs1", "victoria-sullivan", "family_child_sovereignty", 0, True,
              "Sullivan sponsored 2025 NH Senate legislation imposing criminal penalties on anyone who transports a minor across state lines for a surgical procedure or abortion termination without parental consent — a direct assertion of parental authority over minors' medical decisions. She also championed the Parental Bill of Rights requiring schools to disclose student records and program information to parents.",
              ["https://ballotpedia.org/Victoria_Sullivan",
               "https://concordmonitor.com/nh-house-and-senate-pass-parental-rights-bills-concord-monitor-61578614",
               "https://newhampshirebulletin.com/2025/03/27/nh-house-votes-to-criminalize-helping-minors-receive-abortions-but-avoids-the-word-abortion/"]),
        claim("vs2", "victoria-sullivan", "biblical_marriage", 2, True,
              "Serving as NH Senate Vice Chair of Children & Family Law, Sullivan supported HB 377 (2025), the Republican-majority legislation that makes it a Class B felony for medical professionals to administer puberty blockers or cross-sex hormones to minors for gender-transition purposes — signed by Gov. Ayotte in August 2025. The bill rejects the premise that biological sex can be overridden by gender identity in children's health care.",
              ["https://www.nhpr.org/nh-news/2025-08-04/ayotte-signs-two-bills-banning-transgender-health-care-for-youth",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/"]),
    ]),

    # ---------- Timothy Lang Sr. (NH-R, District 2, Senate Majority Whip) ----------
    ("timothy-lang-sr", "NH", "Senator", [
        claim("tl1", "timothy-lang-sr", "self_defense", 1, True,
              "Lang voted to prohibit public colleges and universities from regulating the possession or carrying of firearms and non-lethal weapons on campus — effectively codifying campus carry rights in NH. He has stated that NH consistently ranks among the top three safest states and needs no additional gun-control laws.",
              ["https://www.citizenscount.org/candidate/timothy-lang-sr/serving",
               "https://ballotpedia.org/Timothy_Lang_Sr."]),
        claim("tl2", "timothy-lang-sr", "biblical_marriage", 2, True,
              "As NH Senate Majority Whip, Lang voted for HB 377 (2025), the legislation making it a Class B felony to administer puberty blockers or cross-sex hormone treatments to minors for gender-transition purposes. He also voted to ban K-12 schools from making sexually harmful material available to students — protecting children from age-inappropriate sexual ideology.",
              ["https://www.citizenscount.org/candidate/timothy-lang-sr/serving",
               "https://www.nhpr.org/nh-news/2025-06-06/new-hampshire-senate-passes-restrictions-on-transgender-health-care-for-minors"]),
        claim("tl3", "timothy-lang-sr", "border_immigration", 2, True,
              "Lang voted for the 2025 NH anti-sanctuary legislation prohibiting state and local governments from adopting policies that block law enforcement cooperation with federal immigration authorities (including 287(g) program participation), and supported a broader package of immigration enforcement bills advanced by the Republican Senate majority.",
              ["https://www.nhpr.org/nh-news/2025-05-16/nh-senate-advances-anti-sanctuary-city-bills-but-stops-short-on-other-house-priorities",
               "https://www.citizenscount.org/candidate/timothy-lang-sr/serving"]),
    ]),

    # ---------- Tim McGough (NH-R, District 11) ----------
    ("tim-mcgough", "NH", "Senator", [
        claim("tmg1", "tim-mcgough", "border_immigration", 2, True,
              "McGough listed 'No Sanctuary Cities in NH' as a core legislative priority and voted for the 2025 NH Senate's anti-sanctuary city legislation prohibiting state and local governments from adopting policies that impede federal immigration enforcement cooperation — signed by Gov. Ayotte in 2025.",
              ["https://ballotpedia.org/Tim_McGough",
               "https://www.nhpr.org/nh-news/2025-05-16/nh-senate-advances-anti-sanctuary-city-bills-but-stops-short-on-other-house-priorities"]),
        claim("tmg2", "tim-mcgough", "public_justice", 0, True,
              "McGough sponsored legislation imposing mandatory minimum sentences for the distribution of controlled drugs resulting in death, targeting fentanyl and other deadly narcotics traffickers. He also backed enhanced criminal penalties for fentanyl-related offenses — holding drug dealers accountable for overdose deaths.",
              ["https://ballotpedia.org/Tim_McGough",
               "https://en.wikipedia.org/wiki/Tim_McGough"]),
    ]),

    # ---------- Sharon Carson (NH-R, District 14, NH Senate President 2025) ----------
    ("sharon-carson", "NH", "Senator", [
        claim("sc1", "sharon-carson", "self_defense", 1, True,
              "Carson is a member of the Pro-Gun New Hampshire Council of Advisors and has opposed gun-control restrictions throughout her 17-year Senate tenure. She has consistently voted to protect NH's strong firearms-liberty culture, opposing new restrictions on law-abiding gun owners.",
              ["https://www.citizenscount.org/candidate/sharon-carson",
               "https://ballotpedia.org/Sharon_Carson"]),
        claim("sc2", "sharon-carson", "family_child_sovereignty", 0, True,
              "As NH Senate President in 2025, Carson voted for SB 295, which completely removed the household-income cap on participation in the Education Freedom Account (EFA) program — maximizing parental school choice for all NH families regardless of income. She has supported EFA expansion in every legislative session since the program's creation.",
              ["https://www.citizenscount.org/candidate/sharon-carson/serving",
               "https://ballotpedia.org/Sharon_Carson"]),
        claim("sc3", "sharon-carson", "biblical_marriage", 2, True,
              "Carson voted to add an exception to NH's anti-sex-discrimination law permitting sex-segregated bathrooms, sports, and prisons — defending biological sex as a meaningful legal classification and rejecting the premise that transgender identity overrides legal sex distinctions in all-sex-separated spaces.",
              ["https://www.citizenscount.org/candidate/sharon-carson/serving",
               "https://ballotpedia.org/Sharon_Carson"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collision."""
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

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

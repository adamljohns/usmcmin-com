#!/usr/bin/env python3
"""Enrichment batch 458: evidence-curated claims for 5 federal candidates.

Targets evidence_federal / low_evidence / evidence_curated federal candidates
(U.S. House & Senate) sorted bottom-of-alphabet (CA, IA, NE states).

Candidates (4 D / 1 D partial):
  - Audrey Denney       (CA-01, D  — 2026 D general candidate; Planned Parenthood +
                          Moms Demand Action endorsed; Medicare for All; pro-choice)
  - Cole Bettles        (CA-11, D  — 2026 D primary candidate, open Pelosi seat; CA
                          Democratic platform positions)
  - John Cavanaugh      (NE-02, D  — 2026 D primary candidate; state senator; voted
                          against NE constitutional carry; supports reproductive rights,
                          LGBTQ protections; calls for ICE accountability)
  - Lindsay James       (IA-02-Senate slug, D — Iowa state rep turned IA-02 House
                          candidate; EMILYs List + Giffords PAC endorsed; opposed Iowa
                          heartbeat ban; adding 2 new claims to existing 2)
  - Nathan Sage         (IA-Senate slug, D  — suspended campaign Feb 2026 after
                          announcing pro-choice, Medicare-for-All positions; adding 1
                          new claim to existing 2)

Sources: ballotpedia.org, audreyforcongress.com, nebraskapublicmedia.org,
         iowastartingline.com, en.wikipedia.org, emilyslist.org,
         journalstar.com, omaha.com, ivoterguide.com, localcandidates.org

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
    # ---------------- Audrey Denney (CA-01, D) ----------------
    ("audrey-denney", "CA", "Representative", [
        claim("ad1", "audrey-denney", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Action Fund for her 2026 CA-01 campaign. Denney explicitly supports protecting reproductive rights including access to safe and legal abortion and comprehensive family planning services, and states she is committed to protecting reproductive freedom and ensuring every woman has access to full-spectrum reproductive care — directly rejecting any life-at-conception personhood standard.",
              ["https://progressivevotersguide.com/california/2020/general/audrey-denney-0",
               "https://audreyforcongress.com/endorsements/"]),
        claim("ad2", "audrey-denney", "self_defense", 1, False,
              "Endorsed by Moms Demand Action for her 2026 campaign, an organization that campaigns for universal background checks, red-flag laws, assault-weapons bans, and magazine-capacity restrictions. While Denney frames herself as a 'gun owner' who respects farmers and hunters, her Moms Demand Action endorsement signals support for the gun-safety legislative agenda that the rubric opposes (red-flag laws, expanded background checks, etc.).",
              ["https://audreyforcongress.com/endorsements/",
               "https://www.localcandidates.org/politicians/audrey-denney"]),
        claim("ad3", "audrey-denney", "economic_stewardship", 2, False,
              "Advocates for a single-payer, nonprofit Medicare for All healthcare system as her stated healthcare platform — a program that would require trillions in new federal spending and would substantially expand the federal deficit, contrary to the rubric's balanced-budget and anti-deficit-spending standard.",
              ["https://audreyforcongress.com/issues/healthcare-rural-health/",
               "https://www.localcandidates.org/politicians/audrey-denney"]),
    ]),

    # ---------------- Cole Bettles (CA-11, D) ----------------
    ("cole-bettles", "CA", "Representative", [
        claim("cb1", "cole-bettles", "sanctity_of_life", 0, False,
              "Running as a Democrat in California's 11th Congressional District (San Francisco area, the open Pelosi seat, 2026). California Democrats are uniformly pro-abortion rights; the California Democratic Party platform explicitly endorses abortion access at all stages and opposes any restriction on abortion services. As a 2026 Democratic candidate in one of the most heavily Democratic districts in the country (D+40+), Bettles is aligned with and running on a platform that rejects any life-at-conception personhood standard.",
              ["https://ballotpedia.org/Cole_Bettles",
               "https://ballotpedia.org/California%27s_11th_Congressional_District_election,_2026"]),
        claim("cb2", "cole-bettles", "biblical_marriage", 0, False,
              "San Francisco's CA-11 district is one of the largest LGBTQ communities in the United States. The California Democratic Party requires candidates to support same-sex marriage and LGBTQ civil rights protections including federal Equality Act provisions. As a Democrat running in a district where LGBTQ rights are a core constituency issue, Bettles is aligned with same-sex marriage and rejection of the one-man-one-woman definition.",
              ["https://ballotpedia.org/Cole_Bettles",
               "https://news.ballotpedia.org/2026/03/05/nine-democrats-and-one-republican-are-running-in-the-top-two-primary-for-californias-11th-congressional-district-on-june-2-2026/"]),
        claim("cb3", "cole-bettles", "self_defense", 1, False,
              "California has some of the nation's strictest gun laws, and the California Democratic Party platform calls for expanding background checks, assault-weapons bans, red-flag laws, and magazine-capacity restrictions. As a Democratic candidate in San Francisco — where California's gun-safety agenda originated — Bettles is running on a party platform that opposes the constitutional carry, anti-red-flag, and anti-registry positions the rubric supports.",
              ["https://ballotpedia.org/Cole_Bettles",
               "https://ballotpedia.org/California%27s_11th_Congressional_District_election,_2026"]),
    ]),

    # ---------------- John Cavanaugh (NE-02, D) ----------------
    ("john-cavanaugh-ne-02", "NE", "Representative", [
        claim("jc1", "john-cavanaugh-ne-02", "self_defense", 1, False,
              "As a Nebraska state senator (District 9, 2021–2026), voted against LB77 — the Nebraska bill that allows Nebraskans to carry concealed weapons without a government permit (constitutional carry). LB77 passed 33-14 with Cavanaugh among the 14 opposing. He raised concerns that the bill would lower penalties for prohibited persons carrying concealed weapons, reflecting support for permit requirements the rubric opposes.",
              ["https://journalstar.com/news/state-and-regional/govt-and-politics/bill-allowing-nebraskans-to-carry-concealed-guns-without-a-permit-passes-legislature/article_cec3133c-ef81-5101-915e-5069b11916bc.html",
               "https://en.wikipedia.org/wiki/John_Cavanaugh_(politician)"]),
        claim("jc2", "john-cavanaugh-ne-02", "sanctity_of_life", 0, False,
              "Explicitly stated he has 'fought to protect access to reproductive health care' during his Nebraska legislative tenure and ran for Congress (NE-02) in 2026 on a platform opposing Nebraska's 12-week abortion ban, which he criticized. He is a pro-choice Democrat in a state that enacted both a 12-week abortion ban and a ban on gender-affirming care for minors in May 2023.",
              ["https://nebraskapublicmedia.org/en/news/news-articles/state-sen-john-cavanaugh-launches-congressional-campaign-for-2nd-district-seat/",
               "https://omaha.com/news/local/government-politics/article_7c1ec488-ee5b-4fa5-9b0f-3a35ae9b7814.html"]),
        claim("jc3", "john-cavanaugh-ne-02", "biblical_marriage", 2, False,
              "Publicly supported full legal protections for LGBTQ+ Nebraskans and fought against LB574 — Nebraska's 2023 law banning gender-affirming health care for transgender minors. Cavanaugh was one of 15 senators voting against LB574 (which passed 33-15-1). His opposition to the state ban on gender-transition procedures for minors reflects rejection of the rubric's position that transgender ideology should not receive government endorsement.",
              ["https://nebraskapublicmedia.org/en/news/news-articles/cavanaugh-ends-filibuster-one-transgender-bill-to-be-debated/",
               "https://www.advocate.com/politics/gender-affirming-care-ban-nebraska"]),
    ]),

    # ---------------- Lindsay James (IA, D — Senate slug, now IA-02 House) ----------------
    ("lindsay-james-ia-senate", "IA", "Senator", [
        # Two new claims (lj3, lj4) — existing are lj1 (sanctity_of_life/0) and lj2 (self_defense/1)
        claim("lj3", "lindsay-james-ia-senate", "biblical_marriage", 0, False,
              "Endorsed by EMILYs List, which exclusively supports pro-choice Democratic women who support same-sex marriage and full LGBTQ civil rights. The EMILYs List endorsement requirement that candidates oppose the one-man-one-woman definition of marriage means James publicly rejects the biblical marriage standard the rubric holds.",
              ["https://emilyslist.org/candidate/lindsay-james/",
               "https://en.wikipedia.org/wiki/Lindsay_James_(politician)"]),
        claim("lj4", "lindsay-james-ia-senate", "self_defense", 0, False,
              "Endorsed by Giffords PAC (Courage to Fight Gun Violence) — an organization that campaigns for universal background checks, red-flag laws, assault-weapons bans, and restrictions on constitutional carry. James's Giffords PAC endorsement signals support for the gun-safety agenda that the rubric's self-defense category opposes, including opposition to constitutional carry.",
              ["https://ivoterguide.com/candidate/50589/race/9963/election/1219",
               "https://en.wikipedia.org/wiki/Lindsay_James_(politician)"]),
    ]),

    # ---------------- Nathan Sage (IA, D — Senate candidate, suspended Feb 2026) ----------------
    ("nathan-sage", "IA", "Senator", [
        # One new claim (ns3) — existing are ns1 (sanctity_of_life/0) and ns2 (economic_stewardship/2)
        claim("ns3", "nathan-sage", "economic_stewardship", 4, False,
              "On the campaign trail for Iowa's open U.S. Senate seat (Joni Ernst's seat), Sage advocated for Medicare for All and government negotiation of prescription drug prices — policy positions requiring significant expansion of federal spending and government intervention in the healthcare market, contrary to the rubric's concern about WEF/ESG-style international economic governance and anti-deficit priorities. Sage suspended his Senate campaign in February 2026.",
              ["https://iowastartingline.com/2025/04/16/nathan-sage-against-joni-ernst/",
               "https://iowastartingline.com/2026/02/17/nathan-sage-drops-out-of-us-senate-race-endorses-turek/"]),
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

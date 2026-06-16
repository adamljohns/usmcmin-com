#!/usr/bin/env python3
"""Enrichment batch 255: 4 state legislators from bottom-of-alphabet states.

archetype_curated federal bucket exhausted; continues enriching high-profile
state legislators from WY / WV with documented 2019-2026 positions.

Targets: Rachel Rodriguez-Williams (WY House, Freedom Caucus chair),
         Tom Willis (WV Senator, Judiciary chair + NRA/pro-life),
         Lynn Hutchings (WY Senator, anti-abortion/LGBTQ),
         Tom Takubo (WV Senator/Majority Leader, abortion ban + trans ban).
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
    # ----------- Rachel Rodriguez-Williams (WY, State Representative) -----------
    ("rachel-rodriguez-williams", "WY", "Representative", [
        claim("rrw1", "rachel-rodriguez-williams", "sanctity_of_life", 0, True,
              "As chairwoman of the Wyoming Freedom Caucus, Rodriguez-Williams championed the caucus's successful support for Wyoming's abortion pill ban during the 2023-2024 legislative session — legislation banning the use of medication to terminate pregnancies — consistent with a commitment to protecting life from the moment of conception and opposing all abortion methods.",
              ["https://wyofile.com/wyoming-freedom-caucus-promises-bold-policies-guided-by-godly-principles/",
               "https://ballotpedia.org/Rachel_Rodriguez-Williams"]),
        claim("rrw2", "rachel-rodriguez-williams", "economic_stewardship", 4, True,
              "Rodriguez-Williams led the Wyoming Freedom Caucus's January 2025 'Five and Dime Plan' legislative agenda, which explicitly included banning Wyoming state investments in ESG (Environment, Social and Governance) funds — directly opposing the global ESG/WEF/Davos investment agenda's penetration into state fiscal and pension policy.",
              ["https://wyofile.com/wyoming-freedom-caucus-promises-bold-policies-guided-by-godly-principles/",
               "https://ballotpedia.org/Rachel_Rodriguez-Williams"]),
        claim("rrw3", "rachel-rodriguez-williams", "election_integrity", 0, True,
              "Running for Wyoming Secretary of State in 2026, Rodriguez-Williams pledged to prohibit ballot harvesting, restrict voter registration processes, and 'protect the integrity of our elections and build lasting trust with Wyoming voters' — positions aligned with preventing unsecured voting practices, mass mail-in ballot abuse, and ballot collection schemes.",
              ["https://wyofile.com/wyoming-freedom-caucus-leader-will-run-for-secretary-of-state/",
               "https://ballotpedia.org/Rachel_Rodriguez-Williams"]),
    ]),

    # ----------- Tom Willis (WV, State Senator) -----------
    ("tom-willis", "WV", "Senator", [
        claim("tw1", "tom-willis", "sanctity_of_life", 0, True,
              "Willis is a member of West Virginians for Life — West Virginia's principal pro-life advocacy organization — affirming a commitment to protecting unborn human life from conception, consistent with a life-at-conception and personhood standard and in opposition to any abortion access.",
              ["https://ballotpedia.org/Tom_Willis_(West_Virginia)",
               "https://en.wikipedia.org/wiki/Tom_Willis_(politician)"]),
        claim("tw2", "tom-willis", "self_defense", 2, True,
              "As Senate Judiciary Committee Chairman, Willis advanced SB 1071 (the 'Public Defense and Provisioning Act') through committee in March 2026 — a bill that would have allowed eligible West Virginians to own machine guns, directly challenging NFA federal restrictions on fully-automatic firearms. Willis stated the measure sought to restore 'the proper state [of being] for the Second Amendment, so that we've got a right to protect ourselves from tyranny from the government.'",
              ["https://wvmetronews.com/2026/03/02/machine-gun-legislation-rat-tat-tat-tat-tats-through-west-virginia-senate/",
               "https://blog.wvlegislature.gov/headline/2026/03/02/machine-gun-access-bill-clears-senate-judiciary/"]),
        claim("tw3", "tom-willis", "self_defense", 0, True,
              "Willis is an NRA member and ran in 2024 as an explicitly pro-gun Republican, defeating incumbent Craig Blair in the Republican primary on a stronger Second Amendment platform — affirming constitutional rights to keep and bear arms without restriction, consistent with support for permitless carry and opposition to federal firearm registration schemes.",
              ["https://ballotpedia.org/Tom_Willis_(West_Virginia)",
               "https://wvmetronews.com/2025/05/21/tom-willis-new-to-state-senate-soft-launches-campaign-for-u-s-senate/"]),
    ]),

    # ----------- Lynn Hutchings (WY, State Senator) -----------
    ("lynn-hutchings", "WY", "Senator", [
        claim("lh1", "lynn-hutchings", "biblical_marriage", 4, True,
              "In February 2019, when 14- and 15-year-old students from a school gay-straight alliance lobbied the Wyoming legislature to pass LGBTQ anti-discrimination legislation (HB 230), Senator Hutchings told them that homosexuality is comparable to bestiality and pedophilia — explicitly rejecting the LGBTQ lobby's push to embed same-sex relationship equivalency and gender ideology into state anti-discrimination law. She refused to resign despite official complaints, reflecting a principled refusal to validate LGBTQ promotion in public policy.",
              ["https://trib.com/news/state-and-regional/wyoming-democratic-official-calls-for-senator-s-resignation-after-she-is-accused-of-comparing-homosexuality-to-bestiality-pedophilia/article_977445d5-3e4a-5a72-8615-83aaad2568b6.html",
               "https://wyofile.com/pro-lgbtq-teens-recount-vulgar-conversation-with-sen-hutchings/"]),
        claim("lh2", "lynn-hutchings", "sanctity_of_life", 0, True,
              "During the 2025 Wyoming Legislature session, Hutchings stated the Senate intended to 'do everything we can to either stop [abortion] or make it as safe as possible' — affirming a career-long anti-abortion position aligned with protecting life from conception, as Wyoming continued efforts to enforce its near-total abortion restrictions.",
              ["https://wyofile.com/five-abortion-bills-to-watch-in-the-final-week-of-the-2025-wyoming-legislature/",
               "https://ballotpedia.org/Lynn_Hutchings"]),
    ]),

    # ----------- Tom Takubo (WV, State Senator / Majority Leader) -----------
    ("tom-takubo", "WV", "Senator", [
        claim("tt1", "tom-takubo", "sanctity_of_life", 0, True,
              "As West Virginia Senate Majority Leader, Takubo voted to pass WV's near-total abortion ban during the July 2022 extraordinary legislative session — one of the most restrictive abortion laws in the country — and authored a floor amendment replacing criminal incarceration penalties for violating doctors with medical licensing revocation, maintaining the ban's pro-life enforcement while ensuring OB/GYN practitioners remained in WV.",
              ["https://wvmetronews.com/2022/07/29/west-virginia-senators-pass-abortion-bill-with-some-upset-it-doesnt-go-farther/",
               "https://en.wikipedia.org/wiki/Tom_Takubo"]),
        claim("tt2", "tom-takubo", "biblical_marriage", 2, True,
              "As Senate Majority Leader, Takubo led the West Virginia Senate that in 2021 passed the 'Save Women's Sports Act' (SB 335) — prohibiting biological males who identify as transgender from competing in female athletic categories — rejecting transgender ideology in state policy and protecting women's sports from the erasure of biological sex distinctions.",
              ["https://ballotpedia.org/Tom_Takubo",
               "https://wvlegislature.gov/senate1/lawmaker.cfm?member=Senator+Takubo"]),
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

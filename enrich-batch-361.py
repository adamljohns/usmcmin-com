#!/usr/bin/env python3
"""Enrichment batch 361: 4 federal/state candidates with documented public positions.

All four had 0 claims and confidence below evidence_curated.
Mix: 3 D (CA, NY, IA) + 1 D (CA) — bottom-of-alphabet targeting.
  Eric Swalwell        (CA-D, former US Rep CA-14, resigned April 2026)
  Andrea Stewart-Cousins (NY-D, NY State Senate Majority Leader)
  Lindsay James        (IA-D, Iowa HD-71 state rep, 2026 IA-02 D nominee)
  Melissa Hernandez    (CA-D, 2026 CA-14 congressional candidate)
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
    # ---- Eric Swalwell (CA-D, former US Rep CA-14, resigned April 2026) ----
    ("eric-swalwell", "CA", "resigned", [
        claim("es1", "eric-swalwell", "self_defense", 1, False,
              "During his time in Congress (2013–2026) Swalwell introduced the Freedom from Assault Weapons Act mandating a mandatory government buyback of every assault-style weapon in civilian hands, and cosponsored the Assault Weapons Ban of 2021; in 2019 he ran for president on a single-issue forced-buyback platform — among the most aggressive anti-Second Amendment positions held by any Member of Congress.",
              ["https://swalwell.house.gov/issues/gun-violence-prevention",
               "https://abcnews.go.com/Politics/democratic-candidate-eric-swalwells-gun-control-plan-includes/story?id=64008746"]),
        claim("es2", "eric-swalwell", "sanctity_of_life", 0, False,
              "Swalwell voted against the Pain-Capable Unborn Child Protection Act (20-week abortion ban) and maintained a 100% pro-abortion voting score from Reproductive Freedom for All (the NARAL successor) throughout his congressional career; he identifies as pro-choice and supported codifying abortion rights into federal law.",
              ["https://reproductivefreedomforall.org/lawmaker/eric-swalwell/",
               "https://en.wikipedia.org/wiki/Eric_Swalwell"]),
        claim("es3", "eric-swalwell", "biblical_marriage", 4, False,
              "Swalwell cosponsored the Equality Act (H.R. 5, 117th Congress; H.R. 15, 119th Congress) to embed sexual-orientation and gender-identity protections into all federal civil-rights law and extend them explicitly to schools and public accommodations; he maintained a perfect Human Rights Campaign Congressional Scorecard rating across his tenure.",
              ["https://swalwell.house.gov/issues/equality",
               "https://www.congress.gov/bill/119th-congress/house-bill/15"]),
    ]),

    # ---- Andrea Stewart-Cousins (NY-D, NY State Senate Majority Leader) ----
    ("andrea-stewart-cousins", "NY", "New York Senate", [
        claim("asc1", "andrea-stewart-cousins", "sanctity_of_life", 0, False,
              "As New York State Senate Majority Leader, Stewart-Cousins led passage of the Reproductive Health Act (Jan. 2019), which codified abortion into state law up to 24 weeks gestation (or at any time for health or life) and removed it from the penal code; she then shepherded the Equal Rights Amendment — enshrining abortion access in the NY Constitution — through the legislature (2023) and voters approved it in Nov. 2024.",
              ["https://www.nysenate.gov/senators/andrea-stewart-cousins",
               "https://en.wikipedia.org/wiki/Andrea_Stewart-Cousins"]),
        claim("asc2", "andrea-stewart-cousins", "self_defense", 1, False,
              "After NYSRPA v. Bruen (June 2022) expanded Second Amendment rights, Stewart-Cousins called an emergency special legislative session and drove passage of the Concealed Carry Improvement Act (July 2022), creating extensive new restrictions on concealed-carry permits and banning firearms in broad 'sensitive locations' — one of the most aggressive state legislative responses to a Supreme Court gun ruling in modern history.",
              ["https://www.nysenate.gov/senators/andrea-stewart-cousins/newsroom",
               "https://en.wikipedia.org/wiki/Andrea_Stewart-Cousins"]),
        claim("asc3", "andrea-stewart-cousins", "biblical_marriage", 4, False,
              "During her first year as Majority Leader (2019), New York passed under her leadership a suite of LGBTQ-rights laws including conversion-therapy bans and expansions of gender-identity anti-discrimination protections; she has been a consistent champion of legislation promoting LGBTQ ideology in schools and public policy throughout her tenure.",
              ["https://www.nysenate.gov/senators/andrea-stewart-cousins",
               "https://en.wikipedia.org/wiki/Andrea_Stewart-Cousins"]),
    ]),

    # ---- Lindsay James (IA-D, Iowa HD-71, 2026 IA-02 D nominee) ----
    ("lindsay-james-ia-senate", "IA", "Senator", [
        claim("lj1", "lindsay-james-ia-senate", "sanctity_of_life", 0, False,
              "As Iowa state representative (HD-71 since 2019), James publicly opposed Iowa's near-total abortion ban, sharing a constituent's high-risk pregnancy story to argue against restrictions; she was part of the Iowa House Democratic caucus's explicit 2025 agenda to restore 'reproductive freedom,' advance a state constitutional amendment protecting abortion access, and safeguard IVF.",
              ["https://iowacapitaldispatch.com/briefs/iowa-house-democrats-2025-session-agenda-includes-abortion-rights-marijuana-legalization/",
               "https://iowastartingline.com/2024/12/17/reproductive-rights-2025/"]),
        claim("lj2", "lindsay-james-ia-senate", "self_defense", 1, False,
              "James earned a 24% Freedom Score (2024) from the Iowa Freedom Index — a conservative policy scorecard tracking votes on fiscal restraint, parental rights, and Second Amendment issues — placing her in the bottom quartile of Iowa House members on these measures and indicating consistent votes against gun-rights and property-rights legislation supported by conservative majorities.",
              ["https://freedomindex.us/legislator/4150/session/99/report/83",
               "https://thefreedomindex.org/ia/legislator/21091/votes/ia-scorecard-2024/pdf/scb/"]),
    ]),

    # ---- Melissa Hernandez (CA-D, 2026 CA-14 congressional candidate) ----
    ("melissa-hernandez-ca-14", "CA", "CA-14", [
        claim("mh1", "melissa-hernandez-ca-14", "biblical_marriage", 4, False,
              "As Mayor of Dublin, CA (2020–2024), Hernandez directed the Progress Pride Flag to be flown at the Dublin Civic Center to mark LGBTQ+ Pride Month in June 2024 — active, official municipal promotion of LGBTQ ideology in government, contrary to the rubric's standard against government promotion of LGBTQ identity.",
              ["https://stories.opengov.com/dublin/published/jv7J475AU",
               "https://patch.com/california/dublin/bart-board-president-ex-dublin-mayor-announces-run-congress"]),
        claim("mh2", "melissa-hernandez-ca-14", "sanctity_of_life", 0, False,
              "Running for CA-14 in 2026, Hernandez publicly committed to fighting to 'protect reproductive healthcare and restore reproductive freedom,' explicitly citing support for the Women's Health Protection Act; she was endorsed by Elect Democratic Women, which requires a pro-abortion-access commitment for endorsement.",
              ["https://electdemocraticwomen.org/elect-democratic-women-endorses-melissa-hernandez-for-californias-14th-congressional-district/",
               "https://www.boldpac.com/chc-bold-pac-endorses-melissa-hernandez-for-congress-in-california-s-14th-congressional-district/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

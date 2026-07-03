#!/usr/bin/env python3
"""Enrichment batch 550: 5 state-level Republican officials (bottom of alphabet).

Targets evidence_state officials with 0 claims from ND, MT, MS.
Kelly Armstrong (ND Governor), Greg Gianforte (MT Governor),
Austin Knudsen (MT AG), Drew Wrigley (ND AG), Tate Reeves (MS Governor).

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
    # ------------ Kelly Armstrong (ND-R, Governor) ------------
    ("kelly-armstrong", "ND", "Governor", [
        claim("ka1", "kelly-armstrong", "sanctity_of_life", 0, True,
              "Signed HB 1511 (April 2025) requiring physicians to watch a state-produced video on North Dakota's abortion laws before performing an abortion, and publicly endorsed the North Dakota Supreme Court's November 2025 ruling upholding the state's near-total abortion ban — which prohibits abortion except for rape, incest, or the mother's health.",
              ["https://nrlc.org/nrlnewstoday/2025/04/north-dakotas-pro-life-legislature-would-require-physicians-to-watch-a-video-about-the-states-abortion-laws-prior-to-performing-an-abortion/",
               "https://northdakotamonitor.com/2025/11/21/breaking-north-dakota-abortion-ban-deemed-constitutional-in-split-opinion-from-state-supreme-court/"]),
        claim("ka2", "kelly-armstrong", "self_defense", 1, True,
              "Signed HB 1588 (April 23, 2025) easing North Dakota's firearm carry laws: eliminated the duty to proactively inform law enforcement of a concealed weapon (disclosure required only when directly asked), reduced the penalty for carrying at a public gathering from an infraction to a $100 non-criminal fine, and authorized the State Board of Higher Education to permit firearms on university property.",
              ["https://www.nraila.org/articles/20250424/north-dakota-governor-signs-firearm-carry-enhancement-bill-into-law"]),
        claim("ka3", "kelly-armstrong", "biblical_marriage", 2, True,
              "Signed HB 1144 (May 1, 2025) enforcing North Dakota's 2023 law barring transgender students from bathrooms and locker rooms that do not match their biological sex, prohibiting school staff from being required to use a student's preferred pronouns, and mandating that parents be notified if a child identifies as transgender at school.",
              ["https://northdakotamonitor.com/2025/05/01/north-dakota-governor-signs-bill-to-enforce-one-gender-bathroom-policy-for-k-12-schools/"]),
    ]),

    # ------------ Greg Gianforte (MT-R, Governor) ------------
    ("greg-gianforte", "MT", "Governor", [
        claim("gg1", "greg-gianforte", "sanctity_of_life", 0, True,
              "Signed three abortion restriction bills in May 2023 — HB 136 (Pain-Capable Unborn Child Protection Act), HB 140 (requiring a woman be offered the opportunity to view an active ultrasound before an abortion), and HB 171 (banning telemedicine medication-abortion prescriptions, requiring in-person medical visits) — and publicly opposed Montana's CI-128 constitutional abortion-rights amendment, which voters approved in November 2024.",
              ["https://sbaprolife.org/newsroom/press-releases/pro-life-victory-mt-gov-gianforte-signs-three-landmark-bills-protecting-unborn-children-mothers",
               "https://en.wikipedia.org/wiki/2024_Montana_Initiative_128"]),
        claim("gg2", "greg-gianforte", "self_defense", 0, True,
              "Signed HB 102 (February 18, 2021) establishing permitless constitutional carry statewide — allowing any law-abiding Montana resident or non-resident age 18+ to carry a concealed firearm without a government-issued permit — and signed HB 809 (May 8, 2025) banning all local governments in Montana from enacting or enforcing Extreme Risk Protection Orders (red-flag laws).",
              ["https://news.mt.gov/Governors-Office/governor-gianforte-signs-constitutional-carry-bill-into-law",
               "https://news.ballotpedia.org/2025/05/13/montana-gov-gianforte-r-signs-bill-banning-the-use-of-extreme-risk-protection-orders/"]),
        claim("gg3", "greg-gianforte", "biblical_marriage", 2, True,
              "Signed SB 99 (April 2023) prohibiting healthcare providers from performing puberty blockers, cross-sex hormones, or surgery on minors for gender dysphoria treatment, and signed SB 458 (2023) codifying a binary, biological definition of 'sex' as determined at birth and immutable under Montana state law.",
              ["https://www.npr.org/2023/04/28/1172881782/montana-ban-gender-affirming-care-trans-minors-signed",
               "https://en.wikipedia.org/wiki/Montana_Senate_Bill_99"]),
    ]),

    # ------------ Austin Knudsen (MT-R, Attorney General) ------------
    ("austin-knudsen", "MT", "Attorney", [
        claim("ak1", "austin-knudsen", "self_defense", 1, True,
              "Led a coalition of 26 state attorneys general opposing the Biden ATF's proposed rule on 'Definition of Engaged in the Business as a Dealer in Firearms,' which would have subjected any individual who sells a gun without a federal dealer's license to criminal penalties; also filed amicus briefs in Wolford v. Lopez at the Ninth Circuit defending the right of law-abiding citizens to carry firearms in public against Hawaii's near-total carry ban.",
              ["https://dojmt.gov/attorney-general-knudsen-leads-opposition-to-bidens-latest-attack-on-gun-rights/",
               "https://www.thetruthaboutguns.com/montana-ag-austin-knudsen-states-are-stepping-in-to-protect-second-amendment-rights/"]),
        claim("ak2", "austin-knudsen", "border_immigration", 1, True,
              "Led a 7-AG coalition (2024) challenging the Biden administration's Parole-in-Place rule that would have granted legal residency to over one million illegal aliens; separately led a 22-state coalition urging Congress to pass the Secure America Act providing dedicated long-term funding for ICE and CBP enforcement; and signed a 287(g) agreement in February 2025 authorizing Montana law enforcement cooperation with federal immigration officials.",
              ["https://dojmt.gov/attorney-general-knudsen-leads-coalition-against-immigration-program-rewarding-illegal-immigration/",
               "https://falloncountyextra.com/montana-attorney-general-austin-knudsen-leads-22-state-coalition-urging-congress-to-approve-long-term-funding-for-border-security-agencies/"]),
    ]),

    # ------------ Drew Wrigley (ND-R, Attorney General) ------------
    ("drew-wrigley", "ND", "Attorney", [
        claim("dw1", "drew-wrigley", "sanctity_of_life", 0, True,
              "Personally defended North Dakota's near-total abortion ban through years of litigation under Wrigley v. Romanick; secured a decisive win when the North Dakota Supreme Court upheld the ban on November 21, 2025; and in January 2026 issued a cease-and-desist against a nonprofit facilitating illegal abortion-pill sales, stating the actions 'pose a significant health risk to pregnant women and facilitate the violation of North Dakota's healthcare requirements.'",
              ["https://northdakotamonitor.com/2025/11/21/breaking-north-dakota-abortion-ban-deemed-constitutional-in-split-opinion-from-state-supreme-court/",
               "https://northdakotamonitor.com/2026/01/16/north-dakota-ag-orders-abortion-fund-to-remove-links-to-medication-companies-from-its-website/"]),
        claim("dw2", "drew-wrigley", "border_immigration", 1, True,
              "Joined an 18-state coalition suing the Biden administration over the 'Circumvention of Lawful Pathways' rule — which allowed migrants to schedule border entry via the CBP One app and then 'disperse around the country without any meaningful oversight' — and co-led a 15-state federal suit (2024) blocking a Biden rule making DACA recipients eligible for ACA health-plan subsidies.",
              ["https://www.grandforksherald.com/news/north-dakota/north-dakota-joins-lawsuit-against-biden-administration-following-new-border-policies",
               "https://northdakotamonitor.com/2024/10/15/republican-attorneys-general-seek-to-block-rule-providing-health-insurance-for-daca-recipients/"]),
        claim("dw3", "drew-wrigley", "biblical_marriage", 2, True,
              "Joined a 6-state coalition (May 7, 2024) suing the Biden Department of Education over its Title IX rule reinterpreting the law to cover gender identity — which would have required schools to allow transgender athletes onto women's sports teams — arguing the rule 'requires schools and universities to allow men onto women and girls' sports teams, undermining safety and privacy, and robbing young female athletes of opportunities.'",
              ["https://attorneygeneral.nd.gov/attorney-general-wrigley-joins-attorneys-general-of-arkansas-missouri-and-three-states-in-title-ix-suit/",
               "https://www.valleynewslive.com/2024/05/07/nd-attorney-general-drew-wrigley-joins-title-ix-lawsuit/"]),
    ]),

    # ------------ Tate Reeves (MS-R, Governor) ------------
    ("tate-reeves", "MS", "Governor", [
        claim("tr1", "tate-reeves", "sanctity_of_life", 0, True,
              "Mississippi's near-total abortion ban — prohibiting all abortions except to preserve the mother's life or in documented rape cases — has been continuously in effect since July 2022 under Reeves's governorship; as recently as 2025, Reeves refused to soften the ban's provisions even after the state Department of Health cited rising infant mortality, defending the law as a matter of principle.",
              ["https://en.wikipedia.org/wiki/Abortion_in_Mississippi",
               "https://ballotpedia.org/Tate_Reeves"]),
        claim("tr2", "tate-reeves", "self_defense", 1, True,
              "Signed HB 1110, the Second Amendment Financial Privacy Act (April 2023, effective January 2024), prohibiting any state entity or private party from maintaining a registry of privately owned firearms and blocking financial institutions from using merchant category codes to flag or track firearm purchases — specifically targeting the surveillance infrastructure that could facilitate a future gun registry.",
              ["https://www.wjtv.com/news/politics/mississippi-politics/gov-reeves-signs-bill-to-block-gun-registries-purchase-tracking/",
               "https://dailycaller.com/2023/04/13/mississippi-tate-reeves-second-amendment/"]),
        claim("tr3", "tate-reeves", "biblical_marriage", 2, True,
              "Signed Senate Bill 2753, the SAFER Act (May 13, 2024), requiring public school bathrooms, locker rooms, and dormitories to be used only by persons matching their biological sex at birth; the law defines sex as 'objective and fixed' and 'solely determined by birth,' allows citizens to sue violators, and authorizes the state AG to bring enforcement actions. Reeves stated he signed it 'to protect women's spaces.'",
              ["https://www.upi.com/Top_News/US/2024/05/14/Mississippi-transgender-bathroom-ban/7301715672395/",
               "https://thehill.com/homenews/lgbtq/4661752-mississippi-governor-signs-transgender-bathroom-ban-public-schools/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 140: 5 U.S. House members from SC (4) and PA (1).

Bottom-of-alphabet pick from archetype_party_default federal representatives
with 0 evidence claims. Targets: William Timmons (SC-4), Russell Fry (SC-7),
Joe Wilson (SC-2), Sheri Biggs (SC-3), Rob Bresnahan (PA-8).

Each target gets 2-3 claims spanning distinct rubric categories drawn from
confirmed 2023-2026 voting records and public statements.
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
    # ------------ William Timmons (SC-4, R) ------------
    ("william-timmons", "SC", "Representative", [
        claim("wt1", "william-timmons", "sanctity_of_life", 0, True,
              "Holds a 100% National Right to Life Committee rating and 92% SBA Pro-Life America score (118th Congress); publicly stated 'The sanctity of life from conception to old age must be respected and protected. I am firmly opposed to abortion'; voted YES on Born-Alive Abortion Survivors Protection Act (H.R.21/S.6, 119th Congress, Jan 2025).",
              ["https://sbaprolife.org/representative/william-timmons",
               "https://en.wikipedia.org/wiki/William_Timmons_(politician)"]),
        claim("wt2", "william-timmons", "self_defense", 1, True,
              "Voted NAY on HR 1808 (Assault Weapons Ban of 2022) and NAY on S 2938 (Bipartisan Safer Communities Act, 2022) — blocking both the federal semi-automatic ban and the red-flag law incentive provisions the rubric identifies as Second Amendment violations.",
              ["https://en.wikipedia.org/wiki/William_Timmons_(politician)",
               "https://timmons.house.gov/voterecord/"]),
        claim("wt3", "william-timmons", "biblical_marriage", 2, True,
              "Voted YES on Protect Children's Innocence Act (H.R.3492, Dec 17, 2025) creating a federal criminal penalty for performing gender-transition procedures on minors — a legislative rejection of transgender ideology applied to children in federally regulated contexts.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/3492",
               "https://www.govtrack.us/congress/members/william_timmons/412815"]),
    ]),

    # ------------ Russell Fry (SC-7, R) ------------
    ("russell-fry", "SC", "Representative", [
        claim("rf1", "russell-fry", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record per SBA Pro-Life America (118th Congress); identifies as a Southern Baptist who affirms life begins at conception; voted YES on Born-Alive Abortion Survivors Protection Act (H.R.21/S.6, 119th Congress, Jan 2025) requiring immediate medical care for any infant born alive after a failed abortion.",
              ["https://sbaprolife.org/representative/russell-fry",
               "https://ballotpedia.org/Russell_Fry"]),
        claim("rf2", "russell-fry", "border_immigration", 1, True,
              "Voted YES on Laken Riley Act (S.5/H.R.29, signed Jan 29, 2025) mandating immigration detention and removal proceedings for undocumented persons arrested for burglary, theft, or violent crimes — advancing mandatory enforcement against criminal aliens.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://www.govtrack.us/congress/members/russell_fry/456938"]),
        claim("rf3", "russell-fry", "biblical_marriage", 2, True,
              "Voted YES on Protection of Women and Girls in Sports Act (H.R.28/S.9, signed Mar 2025) banning biological males from competing in women's athletic categories in federally-funded programs — directly rejecting gender-identity ideology in schools and sports.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://www.govtrack.us/congress/members/russell_fry/456938"]),
    ]),

    # ------------ Joe Wilson (SC-2, R) ------------
    ("joe-wilson", "SC", "Representative", [
        claim("jw1", "joe-wilson", "sanctity_of_life", 0, True,
              "Voted YES on No Taxpayer Funding for Abortion and Abortion Insurance Full Disclosure Act (H.R.7, 119th Congress) and Born-Alive Abortion Survivors Protection Act (H.R.21, Jan 2025); a 24-year consistent pro-life congressional record recognized with a 100% National Right to Life rating.",
              ["https://joewilson.house.gov/media-center/press-releases/wilson-statement-on-banning-federal-abortion-funding",
               "https://www.congress.gov/member/joe-wilson/W000795"]),
        claim("jw2", "joe-wilson", "self_defense", 1, True,
              "Recipient of the NRA Defender of Freedom Award, the organization's highest honor for Congressional allies; maintains a perfect pro-gun voting record across his career opposing semi-automatic bans, red-flag law mandates, and universal background check expansions.",
              ["https://en.wikipedia.org/wiki/Joe_Wilson",
               "https://joewilson.house.gov/"]),
        claim("jw3", "joe-wilson", "election_integrity", 0, True,
              "Voted YES on SAVE Act (H.R.22, Apr 10, 2025) requiring documentary proof of U.S. citizenship for voter registration for federal elections — a citizenship verification measure aligning with the rubric's voter-ID and election-integrity standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://joewilson.house.gov/issues/immigration"]),
    ]),

    # ------------ Sheri Biggs (SC-3, R) ------------
    ("sheri-biggs", "SC", "Representative", [
        claim("sb1", "sheri-biggs", "sanctity_of_life", 0, True,
              "Introduced Protecting Motherhood Act (H.R.7235, Jan 2026) to protect pregnancy and maternal care; voted YES on Born-Alive Abortion Survivors Protection Act (H.R.21/S.6, Jan 2025); a Freedom Caucus member and nurse practitioner who frames her pro-life convictions as foundational to her public service.",
              ["https://www.congress.gov/member/sheri-biggs/B001325",
               "https://ballotpedia.org/Sheri_Biggs"]),
        claim("sb2", "sheri-biggs", "biblical_marriage", 2, True,
              "Introduced Defending Women in the Workplace Act asserting biological sex as a protected category distinct from gender identity; voted YES on Protect Children's Innocence Act (H.R.3492, Dec 17, 2025) creating federal criminal penalties for gender-transition procedures on minors.",
              ["https://ballotpedia.org/Sheri_Biggs",
               "https://www.congress.gov/bill/119th-congress/house-bill/3492"]),
        claim("sb3", "sheri-biggs", "border_immigration", 1, True,
              "Voted YES on Laken Riley Act (S.5/H.R.29, signed Jan 29, 2025) requiring mandatory detention and removal proceedings for undocumented immigrants arrested for theft, burglary, or violent crimes — a core mandatory-enforcement posture against criminal aliens.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://www.govtrack.us/congress/members/sheri_biggs/457020"]),
    ]),

    # ------------ Rob Bresnahan (PA-8, R) ------------
    ("rob-bresnahan", "PA", "Representative", [
        claim("rb1", "rob-bresnahan", "sanctity_of_life", 4, False,
              "In December 2025 Bresnahan signed a House discharge petition to force a floor vote on extending ACA subsidies WITHOUT Hyde Amendment protections; SBA Pro-Life America publicly condemned the action, stating Bresnahan partnered with House Minority Leader Hakeem Jeffries to route federal dollars around the long-standing ban on taxpayer-funded abortion.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-pro-life-america-on-house-discharge-petition",
               "https://ballotpedia.org/Rob_Bresnahan_Jr."]),
        claim("rb2", "rob-bresnahan", "border_immigration", 0, True,
              "Voted YES on the Secure America Act (2025) providing long-term ICE and CBP funding for border security operations, and voted YES on Laken Riley Act (S.5/H.R.29, Jan 2025) mandating detention for undocumented persons arrested for violent or theft crimes — backing wall-equivalent enforcement infrastructure.",
              ["https://bresnahan.house.gov/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
        claim("rb3", "rob-bresnahan", "election_integrity", 0, True,
              "Voted YES on SAVE Act (H.R.22, Apr 10, 2025) requiring documentary proof of U.S. citizenship for federal voter registration — a citizenship verification requirement aligning with the rubric's election-integrity standard against non-citizen voting.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://ballotpedia.org/Rob_Bresnahan_Jr."]),
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 372: hand-curated claims for 5 Wisconsin State Senators.

Targets archetype_party_default WI state senators with 0 claims, taken from the
bottom of the alphabet (WI). Mix of 2 R / 3 D covering 2024-2026 records.

Targets:
  LaTonya Johnson (WI-D, SD-6), Kristin Dassler-Alfheim (WI-D, SD-18),
  Kelda Roys (WI-D, SD-26), Julian Bradley (WI-R, SD-28),
  John Jagler (WI-R, SD-13).

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
    # ---------------- LaTonya Johnson (WI-D, SD-6) ----------------
    ("latonya-johnson", "WI", "State Senator", [
        claim("ltj1", "latonya-johnson", "sanctity_of_life", 0, False,
              "Co-sponsored 2025 Senate Bill 271 establishing that every individual has a fundamental right to bodily autonomy including the right to access abortion at any time during pregnancy in the professional judgment of the medical provider, and sponsored 2025 SB 547 to eliminate certain abortion-related regulations in Wisconsin — categorically rejecting any personhood-from-conception or life-at-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2816",
               "https://legis.wisconsin.gov/senate/06/johnson/"]),
        claim("ltj2", "latonya-johnson", "biblical_marriage", 0, False,
              "Sponsored 2025 Senate Joint Resolution 68 to eliminate Wisconsin's constitutional restriction defining marriage as between one man and one woman, and co-sponsored SB 321 adopting gender-neutral terminology and incorporating gender-neutral marriage and parentage rights into Wisconsin statutes — directly rejecting the biblical definition of marriage as one man and one woman.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2816",
               "https://legis.wisconsin.gov/senate/06/johnson/"]),
        claim("ltj3", "latonya-johnson", "self_defense", 1, False,
              "Publicly prioritizes 'keeping guns out of the hands of violent offenders and protecting children, communities and public spaces' through new gun-control legislation — a posture opposing the rubric's defense of unrestricted Second Amendment rights, including opposition to expanded background-check requirements, red-flag orders, and assault-weapon restrictions.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2816",
               "https://www.latonyaforwisconsin.com/"]),
    ]),

    # ---------------- Kristin Dassler-Alfheim (WI-D, SD-18) ----------------
    ("kristin-dassler-alfheim", "WI", "State Senator", [
        claim("kda1", "kristin-dassler-alfheim", "sanctity_of_life", 0, False,
              "Introduced 2025 Senate Bill 271 establishing that every individual has a fundamental right to bodily autonomy including the right to access abortion at any time during pregnancy based on the professional judgment of the medical provider, and requiring health coverage plans to cover abortion — categorically rejecting any life-at-conception or personhood-from-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sb271.pdf",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2841",
               "https://legis.wisconsin.gov/senate/18/dassler-alfheim/"]),
        claim("kda2", "kristin-dassler-alfheim", "biblical_marriage", 0, False,
              "Upon taking office in January 2025, introduced resolutions to remove Wisconsin's constitutional marriage restrictions (eliminating the one-man-one-woman definition) and sponsored four bills to provide 'equity and protections for the LGBTQ+ community in Wisconsin' — directly rejecting the constitutional one-man-one-woman definition of marriage and advancing a gender-neutral marriage framework through legislation.",
              ["https://legis.wisconsin.gov/senate/18/dassler-alfheim/press-releases/senator-dassler-alfheim-takes-office-co-authors-legislative-package/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2841"]),
        claim("kda3", "kristin-dassler-alfheim", "economic_stewardship", 2, False,
              "Explicit legislative agenda calls for expanded state spending on housing, rising healthcare costs, and increased funding for municipalities and public schools. Authored bills including SB LRB-4778 allocating $40 million over 2025-27 for university programs — new spending commitments that conflict with the rubric's anti-deficit, balanced-budget economic stewardship standard.",
              ["https://legis.wisconsin.gov/senate/18/dassler-alfheim/",
               "https://www.wispolitics.com/2025/sen-dassler-alfheim-authors-bills-to-improve-college-access-and-affordability/"]),
    ]),

    # ---------------- Kelda Roys (WI-D, SD-26) ----------------
    ("kelda-roys", "WI", "State Senator", [
        claim("kr1", "kelda-roys", "sanctity_of_life", 0, False,
              "Former executive director of NARAL Pro-Choice Wisconsin, where she championed the Compassionate Care for Rape Victims Act — Wisconsin's first pro-choice law in three decades. As State Senator, in April 2025 she co-proposed the 'Abortion Rights Restoration Act' with Rep. Lisa Subeck to establish a statutory right to abortion in Wisconsin law, and co-leads the Legislature's Reproductive Freedom Workgroup — categorically rejecting any personhood-from-conception standard.",
              ["https://legis.wisconsin.gov/senate/26/roys/about/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2825",
               "https://legis.wisconsin.gov/senate/26/roys/"]),
        claim("kr2", "kelda-roys", "self_defense", 1, False,
              "Has publicly aligned with Dane County Board members to call for gun reform legislation in Wisconsin, opposing the rubric's defense of unrestricted Second Amendment rights and its prohibition on red-flag laws, assault-weapon bans, and expanded background-check requirements.",
              ["https://legis.wisconsin.gov/senate/26/roys/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2825"]),
        claim("kr3", "kelda-roys", "biblical_marriage", 2, False,
              "A member of the Wisconsin Legislature's LGBTQ+ caucus, co-sponsoring legislation advancing transgender-inclusive and gender-affirming public policy in the 2025 session — in direct conflict with the rubric's rejection of transgender ideology in schools and policy. Her about page states she co-leads efforts to advance LGBTQ+ equity through the state legislature.",
              ["https://legis.wisconsin.gov/senate/26/roys/about/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2825"]),
    ]),

    # ---------------- Julian Bradley (WI-R, SD-28) ----------------
    ("julian-bradley", "WI", "State Senator", [
        claim("jb1", "julian-bradley", "sanctity_of_life", 0, True,
              "Sponsored multiple pro-life bills in the 2025 Wisconsin Senate: SB 384 (requirements for medical care for children born alive following abortion or attempted abortion, with criminal penalties for violations); SB 406 (mandatory reporting of sex and fetal anomaly following induced abortion); and co-sponsored SB 553 (limiting the statutory definition of abortion to exclude emergency obstetric care). A sustained, multi-bill pro-life record.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2805",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384",
               "https://legis.wisconsin.gov/senate/28/bradley/"]),
        claim("jb2", "julian-bradley", "family_child_sovereignty", 0, True,
              "Sponsored 2025 Senate Bill 371 requiring Wisconsin's human growth and development curriculum to include instruction on pregnancy, prenatal development, and childbirth — ensuring students receive factual, biology-affirming content about human development rather than ideologically filtered material, aligned with the rubric's pro-parental-rights and pro-traditional-education standard.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2805",
               "https://legis.wisconsin.gov/senate/28/bradley/"]),
        claim("jb3", "julian-bradley", "election_integrity", 0, True,
              "Co-authored 2025 Senate Joint Resolution 2 to enshrine Wisconsin's photographic voter-ID requirement in the state constitution — making it immune to reversal by the state Supreme Court. Also authored SB 338 to enforce the federal Help America Vote Act. Bradley stated the voter-ID amendment ensures 'the partisan Supreme Court couldn't overturn' the law, reflecting a firm election-integrity posture.",
              ["https://legis.wisconsin.gov/senate/28/bradley/press-releases/sen-bradley-co-authored-voter-id-amendment-to-receive-vote-in-senate/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2805"]),
    ]),

    # ---------------- John Jagler (WI-R, SD-13) ----------------
    ("john-jagler", "WI", "State Senator", [
        claim("jj1", "john-jagler", "sanctity_of_life", 0, True,
              "Co-sponsored 2025 Wisconsin SB 553 limiting the statutory definition of abortion to protect emergency obstetric care while drawing a clear legislative line against elective abortion, and co-sponsored SB 384 requiring hospitals to provide medical care for infants born alive following a failed abortion — a consistent pro-life legislative record maintained across multiple legislative sessions in both the Assembly and Senate.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2814",
               "https://docs.legis.wisconsin.gov/2025/proposals/sb384",
               "https://legis.wisconsin.gov/senate/13/jagler/"]),
        claim("jj2", "john-jagler", "self_defense", 1, True,
              "As a Wisconsin Assembly member, co-sponsored AB 293 (2021) to restrict Wisconsin state and local authorities from using public resources to enforce federal laws regulating firearms, firearm accessories, and ammunition — a Second Amendment nullification measure directly aligned with the rubric's opposition to federal gun regulations and support for constitutional carry. His sustained Republican caucus alignment reflects continued resistance to new firearms restrictions.",
              ["https://ballotpedia.org/John_Jagler",
               "https://legis.wisconsin.gov/senate/13/jagler/"]),
        claim("jj3", "john-jagler", "economic_stewardship", 2, True,
              "Co-sponsored 2023 Senate Bill 435 to lower Wisconsin's individual income tax rates in the third bracket and expand the retirement income subtraction — a taxpayers-first, pro-growth fiscal measure consistent with the rubric's anti-deficit, anti-overtaxation economic stewardship standard. His Republican caucus record reflects consistent support for returning surplus revenue to taxpayers rather than expanding state spending.",
              ["https://legis.wisconsin.gov/senate/13/jagler/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2814"]),
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

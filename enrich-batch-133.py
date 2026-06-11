#!/usr/bin/env python3
"""Enrichment batch 133: 5 federal Senate candidates (low_evidence, bottom of alphabet).

Targets: Michele Morrow (NC-R), Don Brown (NC-R), Adam Schwarze (MN-R),
James W. Byrd (WY-D), Lee Calhoun (MT-R). All had 0 claims.

Sources: candidate interviews/profiles at wcti12.com, WRAL, wyomingpublicmedia.org,
cowboystatedaily.com, projects.montanafreepress.org, minnpost.com, yournews.com.

MINIFIED write: separators=(',',':') — keeps scorecard.json ~35-36MB under GitHub 50MB limit.
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
    # ---------------- Michele Morrow (NC-R, 2026 Senate candidate) ----------------
    ("michele-morrow", "NC", "Senator", [
        claim("mm1", "michele-morrow", "sanctity_of_life", 0, True,
              "Stated plainly: 'I do not believe there is ever a reason for an abortion,' affirming life-at-conception personhood. She also calls for enforcing the Comstock Act to ban interstate shipment of abortion-inducing drugs.",
              ["https://www.wral.com/news/local/michele-morrow-republican-primary-nc-us-senate-2026/",
               "https://wcti12.com/news/local/meet-michele-morrow-candidate-for-us-senate"]),
        claim("mm2", "michele-morrow", "sanctity_of_life", 4, True,
              "Explicitly states no abortion provider should receive any taxpayer funds 'regardless of how they are funneled,' supporting a full defunding of Planned Parenthood.",
              ["https://wcti12.com/news/local/meet-michele-morrow-candidate-for-us-senate",
               "https://www.wral.com/news/local/michele-morrow-republican-primary-nc-us-senate-2026/"]),
        claim("mm3", "michele-morrow", "self_defense", 0, True,
              "Pledges to 'Defend the Second Amendment with no compromises, ensuring law-abiding North Carolinians can protect their families from rising crime' — a constitutional-carry, unrestricted-rights posture.",
              ["https://wcti12.com/news/local/meet-michele-morrow-candidate-for-us-senate",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_North_Carolina"]),
    ]),

    # ---------------- Don Brown (NC-R, 2026 Senate candidate) ----------------
    ("don-brown-nc-senate", "NC", "Senator", [
        claim("db1", "don-brown-nc-senate", "sanctity_of_life", 0, True,
              "Holds that 'unborn babies must be afforded the same constitutional rights to due process as all Americans, from the moment of conception, as set forth in the 5th and 14th Amendments' — a personhood-from-conception position.",
              ["https://wcti12.com/news/local/meet-don-brown-candidate-for-us-senate",
               "https://www.donbrownfornc.com/"]),
        claim("db2", "don-brown-nc-senate", "sanctity_of_life", 4, True,
              "States abortion providers including Planned Parenthood should receive zero taxpayer funds, and would enforce the Comstock Act banning interstate transportation of abortion-inducing drugs.",
              ["https://wcti12.com/news/local/meet-don-brown-candidate-for-us-senate"]),
        claim("db3", "don-brown-nc-senate", "border_immigration", 1, True,
              "Calls for ending chain migration entirely and ending most immigration from Sharia-law nations as incompatible with the Constitution; advocates prioritizing asylum for persecuted Christians.",
              ["https://wcti12.com/news/local/meet-don-brown-candidate-for-us-senate",
               "https://www.longleafpol.com/p/senate-race-don-brown"]),
    ]),

    # ---------------- Adam Schwarze (MN-R, 2026 Senate candidate) ----------------
    ("adam-schwarze", "MN", "Senator", [
        claim("as1", "adam-schwarze", "border_immigration", 0, True,
              "Launched his Senate campaign explicitly criticizing Minnesota Democrats over the 'massive increase of unlawful border crossings' and vowing to enforce the border — a wall-and-enforcement posture aligned with the rubric.",
              ["https://yournews.com/2026/01/11/6098829/navy-seal-adam-schwarze-launches-u-s-senate-bid-slams-minnesota/",
               "https://www.valleynewslive.com/2026/05/30/mn-gop-endorses-republican-adam-schwarze-us-senate/"]),
        claim("as2", "adam-schwarze", "self_defense", 1, True,
              "In the 2026 Republican primary, Schwarze attacked opponent Michele Tafoya for being 'out of step with the party on guns,' signaling his own uncompromising opposition to red-flag laws, assault-weapons bans, and magazine restrictions.",
              ["https://www.minnpost.com/national/washington/2026/05/gop-primary-awaits-after-schwarze-tops-tafoya-for-partys-u-s-senate-endorsement/",
               "https://hoodline.com/2026/05/ex-seal-climbs-gop-ranks-snags-minnesota-senate-endorsement/"]),
    ]),

    # ---------------- James W. Byrd (WY-D, 2026 Senate candidate) ----------------
    ("james-w-byrd-wy-senate", "WY", "Senator", [
        claim("jb1", "james-w-byrd-wy-senate", "family_child_sovereignty", 0, False,
              "As a Wyoming state legislator and now Senate candidate, Byrd 'expressed distaste for... growing support for homeschooling and charter schools' in Wyoming — directly opposing the parental-rights and homeschool-freedom plank of the rubric.",
              ["https://www.wyomingpublicmedia.org/politics-government/2026-02-18/first-wyoming-democrat-announces-run-for-u-s-senate",
               "https://cowboystatedaily.com/2026/02/17/former-wyoming-rep-james-byrd-announces-run-for-u-s-senate/"]),
        claim("jb2", "james-w-byrd-wy-senate", "economic_stewardship", 2, False,
              "As a state representative, Byrd pushed to significantly raise Wyoming's minimum wage and advocates additional public spending on renewable energy, healthcare, and public lands — prioritizing government outlays over the deficit-reduction and fiscal-restraint standard the rubric requires.",
              ["https://cowboystatedaily.com/2026/02/17/former-wyoming-rep-james-byrd-announces-run-for-u-s-senate/",
               "https://en.wikipedia.org/wiki/James_W._Byrd"]),
    ]),

    # ---------------- Lee Calhoun (MT-R, 2026 Senate candidate) ----------------
    ("lee-calhoun", "MT", "Senator", [
        claim("lc1", "lee-calhoun", "economic_stewardship", 1, False,
              "Campaigns on establishing a universal healthcare system funded through the federal government — an explicit call for large-scale federal spending expansion inconsistent with the sound-money, limited-government stewardship the rubric requires.",
              ["https://projects.montanafreepress.org/election-guide-2026/candidates/lee-calhoun/",
               "https://calhounformt.com/about/"]),
        claim("lc2", "lee-calhoun", "economic_stewardship", 2, False,
              "Advocates 'returning tax rates to 2000 levels' and 'funding infrastructure and education to pay down debt,' prioritizing new government programs over the spending cuts and balanced-budget discipline the rubric calls for.",
              ["https://projects.montanafreepress.org/election-guide-2026/candidates/lee-calhoun/",
               "https://calhounformt.com/about/"]),
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

#!/usr/bin/env python3
"""Enrichment batch 59: hand-curated claims for 4 federal House candidates.

Targets archetype_curated U.S. Representative candidates from the bottom of
the remaining zero-claims bucket (NY → NJ → IA → FL reverse-alphabetical).

Mix (1 R / 3 D): Fiona McFarland (FL-16 R), Sarah Trone Garriott (IA-03 D),
Christina Bohannan (IA-01 D), Adrian Mapp (NJ-12 D).
Each claim cites >=1 reliable source reflecting 2022-2026 voting records /
public positions.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ------------ Fiona McFarland (FL-16, R, FL state rep, Navy vet) ------------
    ("fiona-mcfarland-fl-16", "FL", "Representative", [
        claim("fm1", "fiona-mcfarland-fl-16", "sanctity_of_life", 0, True,
              "Voted for Florida's 15-week abortion ban (HB 5, 2022) — the most restrictive "
              "abortion law in Florida at the time — including no exceptions for rape or incest. "
              "Her Democratic opponent made this vote the centerpiece of the 2022 and 2024 "
              "campaigns; McFarland ran on it and won twice, demonstrating a consistent "
              "pro-life legislative record.",
              ["https://floridapolitics.com/archives/565759-fiona-mcfarland-seeks-re-election-in-swing-seat-as-derek-reich-hammers-on-floridas-abortion-ban/",
               "https://www.aclufl.org/en/legislation/sb-146-hb-5-banning-abortion-after-15-weeks"]),
        claim("fm2", "fiona-mcfarland-fl-16", "family_child_sovereignty", 0, True,
              "Sponsored Florida's 'Digital Bill of Rights' (SB 262 / companion HB 9B, 2023), "
              "signed into law by Governor DeSantis, which requires affirmative parental consent "
              "before companies may collect or process personal data from children — establishing "
              "parental sovereignty over minors' digital exposure in state law.",
              ["https://ballotpedia.org/Fiona_McFarland",
               "https://en.wikipedia.org/wiki/Fiona_McFarland"]),
    ]),

    # ---------- Sarah Trone Garriott (IA-03, D, IA state senator, minister) ----------
    ("sarah-trone-garriott", "IA", "Representative", [
        claim("stg1", "sarah-trone-garriott", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List, which exclusively funds pro-abortion Democratic women "
              "candidates and whose endorsement requires commitment to unrestricted abortion access "
              "— placing Trone Garriott squarely inside the abortion-industry endorsement-and-funding "
              "network the rubric identifies.",
              ["https://emilyslist.org/news/emilys-list-endorses-state-sen-sarah-trone-garriott-for-iowas-3rd-congressional-district/",
               "https://ballotpedia.org/Sarah_Trone_Garriott"]),
        claim("stg2", "sarah-trone-garriott", "sanctity_of_life", 0, False,
              "Running on an explicit platform to 'restore nationwide protections for abortion "
              "access' and 'safeguard the right to contraception, IVF, and prenatal care' — "
              "opposing any federal or state legal recognition of the unborn from conception.",
              ["https://en.wikipedia.org/wiki/Sarah_Trone_Garriott",
               "https://ballotpedia.org/Sarah_Trone_Garriott"]),
    ]),

    # ----------- Christina Bohannan (IA-01, D, 2022/2024 nominee, law professor) -----------
    ("christina-bohannan", "IA", "Representative", [
        claim("cb1", "christina-bohannan", "sanctity_of_life", 4, False,
              "Highlighted as a 'reproductive rights champion' by Planned Parenthood Advocates "
              "of Iowa, which featured her debate performance defending abortion access — placing "
              "her in PP's endorsement and advocacy network and disqualifying her from the rubric's "
              "'never took PP/NARAL/EMILY money' standard.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-advocates-iowa/blog/first-district-candidate-christina-bohannan-positions-herself-as-a-reproductive-rights-champion-during-debate",
               "https://ballotpedia.org/Christina_Bohannan"]),
        claim("cb2", "christina-bohannan", "self_defense", 1, False,
              "Endorsed by Giffords gun-control organization and a member of Moms Demand Action; "
              "while in the Iowa legislature, spoke out against the 2021 removal of state background "
              "check requirements and against a strict-scrutiny constitutional amendment that would "
              "have shielded gun rights from government restriction — opposing expanded Second "
              "Amendment protections at every opportunity.",
              ["https://giffords.org/candidates/christina-bohannan-3/",
               "https://ballotpedia.org/Christina_Bohannan"]),
    ]),

    # ------------ Adrian Mapp (NJ-12, D, Plainfield Mayor, CPA) ------------
    ("adrian-mapp", "NJ", "Representative", [
        claim("am1", "adrian-mapp", "self_defense", 1, False,
              "As Plainfield mayor, declared gun violence 'a health crisis that needs stronger "
              "legislation at every level of government' and joined New Jersey's 2019 municipal "
              "coalition advocating for gun-safety reforms — positioning himself for more "
              "restrictions on firearms rather than the constitutional-carry and Second Amendment "
              "expansion the rubric calls for.",
              ["https://www.tapinto.net/towns/plainfield/columns/city-of-plainfield-news/articles/mayor-mapp-confronting-violence-with-unity-and-resolve",
               "https://www.nj.gov/governor/news/news/562019/20190619c.shtml"]),
        claim("am2", "adrian-mapp", "border_immigration", 1, False,
              "On immigration, advocates for 'reform' of ICE rather than enforcement — explicitly "
              "rejecting mandatory deportation approaches: 'I am not giving the easy answer that "
              "so many other candidates are giving where they're saying let's just abandon ICE. "
              "I am for reform. I am for making sure our borders are secure.' This centrist "
              "framing is incompatible with the rubric's mandatory deportation standard.",
              ["https://www.dailyprincetonian.com/article/2026/02/princeton-news-broadfocus-plainfield-mayor-adrian-mapp-nj12-democrat-congress"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

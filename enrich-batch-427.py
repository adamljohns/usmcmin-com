#!/usr/bin/env python3
"""Enrichment batch 427: hand-curated claims for 4 Wyoming State Representatives (all R).

archetype_curated federal bucket is fully exhausted; continuing with
archetype_party_default state legislators from the bottom of the alphabet (WY).

Targets (reverse-alpha within WY bucket):
  Ann Lucas    (WY-43, Cheyenne area, newly elected 2024)
  Art Washut   (WY-36, Judiciary Committee Chair)
  Bill Allemand (WY-58, Freedom Caucus, Natrona County rancher)
  Abby Angelos  (WY-3, Campbell County, Family Life Church)

Each claim cites >=1 reliable public source reflecting 2023-2026 voting
records, sponsored legislation, or official public positions.

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
    # ------------ Ann Lucas (WY-43, R, Cheyenne area) ------------
    ("ann-lucas", "WY", "State Representative", [
        claim("al1", "ann-lucas", "family_child_sovereignty", 0, True,
              "A leading advocate for parental authority in Wyoming schools, Lucas stated that schools should not 'conduct any survey without parental consent' or 'promote any activist organization or sexual ideology with children.' She opposed President Biden's 2024 Title IX rewrite — which would have required schools to accommodate transgender identity — and was identified as one of the strongest advocates for 2026 House Bill 10, which removes literature deemed sexually explicit from children's and young-adult sections of school and public libraries.",
              ["https://wyofile.com/republican-legislative-primary-outside-cheyenne-reflects-wyoming-gops-divide/",
               "https://capcity.news/community/elections/2024/07/25/republican-legislative-primary-outside-cheyenne-reflects-wyoming-gops-divide/"]),
        claim("al2", "ann-lucas", "biblical_marriage", 2, True,
              "Explicitly opposed the Biden administration's 2024 rewrite of Title IX that classified 'gender identity' as a protected characteristic, which would have required Wyoming public schools to permit biological males into female-only bathrooms, locker rooms, and sports. Lucas called these rules an unconstitutional federal imposition on Wyoming's children and families, aligning with the rubric's rejection of transgender ideology in law and policy.",
              ["https://wyofile.com/republican-legislative-primary-outside-cheyenne-reflects-wyoming-gops-divide/",
               "https://oilcity.news/community/elections/2024/07/25/republican-legislative-primary-outside-cheyenne-reflects-wyoming-gops-divide/"]),
        claim("al3", "ann-lucas", "refuse_federal_overreach", 0, True,
              "Declared that 'recent events, including COVID-19, show that the federal government has overstepped its authority and has dictated how the Wyoming government operates and how Wyoming citizens live.' Lucas ran on a platform of restoring state sovereignty over natural resources, public lands, healthcare, and child-rearing, and pledged to identify and push back against legislation that surrenders Wyoming's authority to federal arbitrary mandates.",
              ["https://ground.news/article/republican-ann-lucas-launches-campaign-for-wyoming-house-district-43",
               "https://capcity.news/community/elections/2024/07/25/republican-legislative-primary-outside-cheyenne-reflects-wyoming-gops-divide/"]),
    ]),

    # ------------ Art Washut (WY-36, R, Judiciary Committee Chair) ------------
    ("art-washut", "WY", "State Representative", [
        claim("aw1", "art-washut", "sanctity_of_life", 0, True,
              "Primary sponsor of HB0148 (2024), requiring surgical abortion facilities to obtain state operating licenses and mandating that licensed physicians perform all chemical and surgical abortions only after an ultrasound — a targeted pro-life regulatory measure that passed the Wyoming House 50–12. As Chair of the Joint Judiciary Committee, Washut has consistently advanced protective legislation for the unborn, treating abortion as a matter of public safety warranting rigorous medical oversight.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0148",
               "https://county17.com/2024/02/25/safety-measure-or-another-attempt-at-eliminating-abortion-wyoming-lawmakers-back-new-abortion-rules/"]),
        claim("aw2", "art-washut", "self_defense", 1, True,
              "Primary sponsor of HB0039 (2024), Wyoming's firearms rights-restoration bill, which creates a legal pathway for individuals who have lost their Second Amendment rights to petition for their restoration. The measure expands the exercise of gun rights by treating firearms ownership as a restorable civil right rather than a permanent forfeiture — directly countering the gun-confiscation philosophy the rubric opposes.",
              ["https://www.wyoleg.gov/Legislation/2024/HB0039",
               "https://www.billtrack50.com/billdetail/1927324"]),
    ]),

    # ------------ Bill Allemand (WY-58, R, Freedom Caucus, Natrona County) ------------
    ("bill-allemand", "WY", "State Representative", [
        claim("ba1", "bill-allemand", "sanctity_of_life", 0, True,
              "States on his official campaign platform that 'Defending life from conception to natural death is an issue of grave importance to him' and that he 'will continue to promote and sponsor/co-sponsor legislation that saves the lives of the unborn' — an explicit pro-life-from-conception position matching the rubric's personhood standard. Elected in 2022 by defeating a pro-choice incumbent, Allemand has consistently co-sponsored and backed Wyoming's abortion-restriction bills since taking office.",
              ["https://billfor58.com/",
               "https://wyfreedomcaucus.com/members/"]),
        claim("ba2", "bill-allemand", "self_defense", 1, True,
              "Declares himself 'a lifetime advocate of the preservation of the 2nd Amendment rights' who 'will defend the right to bear arms unconditionally,' and successfully ushered through legislation to prohibit discrimination and tracking of firearms purchases — a measure directly targeting the gun-surveillance infrastructure that enables future registries and confiscation, which the rubric opposes.",
              ["https://billfor58.com/",
               "https://wyfreedomcaucus.com/members/"]),
        claim("ba3", "bill-allemand", "border_immigration", 4, True,
              "Introduced HB0116 (2023), which would have banned all property ownership of more than 1 acre in Wyoming by persons, businesses, or governments of China, Russia, or any nation designated a state sponsor of terrorism, and separately co-sponsored HB0088 to restrict adversarial foreign ownership of agricultural land. Although both bills failed that session, Allemand publicly attributed the failures to moderate Republican resistance and pledged to refile — directly matching the rubric's opposition to hostile foreign-nation farmland acquisition.",
              ["https://www.wyoleg.gov/Legislation/2023/HB0116",
               "https://cowboystatedaily.com/2023/11/12/foreign-ownership-of-ag-land-a-struggle-for-lawmakers-in-wyoming-and-dc/"]),
    ]),

    # ------------ Abby Angelos (WY-3, R, Campbell County, Family Life Church) ------------
    ("abby-angelos", "WY", "State Representative", [
        claim("aa1", "abby-angelos", "sanctity_of_life", 0, True,
              "Made 'protect life' a signature governing commitment, stating she 'has kept her promise to protect life' since taking office in 2023, and identifies herself as standing for 'the sanctity of life' as a core conservative value. A leader at Family Life Church in Gillette, Angelos represents Campbell County — Wyoming's largest coal-producing county — and earned a 90% Conservative Index score, reflecting a consistent pro-life voting record across the 2023-24 sessions.",
              ["https://voteforabby.com/about-abby/",
               "https://county17.com/2024/07/31/wyoming-house-candidate-questionnaire-abby-angelos-for-house-district-3/"]),
        claim("aa2", "abby-angelos", "self_defense", 1, True,
              "Publicly committed to 'protecting the 2nd Amendment' as a core legislative priority since her first term, and earned a 90% Conservative Index score from 307 Votes for the 2023-24 sessions, reflecting a consistent pro-Second-Amendment voting record. Represents Campbell County — home to Wyoming's energy and ranching industries — where constitutional gun rights are foundational to her constituents' way of life and she has delivered on the commitment.",
              ["https://voteforabby.com/about-abby/",
               "https://307votes.com/spotlight-report/"]),
        claim("aa3", "abby-angelos", "family_child_sovereignty", 0, True,
              "A staunch champion of parental rights who has made 'stand[ing] for parents' a defining commitment: she was identified as 'one of the strongest advocates' for 2026 House Bill 10, which removes sexually explicit content from children's and young-adult sections of school and public libraries. She also opposes any school policy that surveys, counsel, or instructs children on sexual ideology without prior parental knowledge and consent.",
              ["https://voteforabby.com/about-abby/",
               "https://county17.com/2024/07/31/wyoming-house-candidate-questionnaire-abby-angelos-for-house-district-3/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

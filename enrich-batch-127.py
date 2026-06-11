#!/usr/bin/env python3
"""Enrichment batch 127: evidence-curated claims for 5 federal candidates.

Targets evidence_federal candidates from bottom of alphabet (VA + GA) with 0 claims.
Mix (3 R GA / 2 D VA):
  Rick Allen (GA-R, US Rep GA-12), Austin Scott (GA-R, US Rep GA-08),
  Brian Jack (GA-R, US Rep GA-03), Elaine Luria (VA-D, former/2026 US Rep VA-02),
  Suhas Subramanyam (VA-D, US Rep VA-10).
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
    # ---------------- Rick Allen (GA-R, US Representative GA-12) ----------------
    ("rick-allen", "GA", "Representative", [
        claim("ra1", "rick-allen", "sanctity_of_life", 0, True,
              "Co-sponsored the Born-Alive Abortion Survivors Protection Act (H.R. 962) and personally sought unanimous consent for its floor consideration; also co-sponsored H.R. 18 to make the Hyde Amendment permanent, maintaining a 100% SBA Pro-Life voting record through 2025.",
              ["https://sbaprolife.org/representative/rick-allen",
               "https://allen.house.gov/voterecord/"]),
        claim("ra2", "rick-allen", "self_defense", 1, True,
              "A lifelong NRA member who received NRA-PVF endorsement in 2020 and has consistently voted against firearm bans, universal background-check mandates, and red-flag laws that would infringe on Second Amendment rights.",
              ["https://www.nrapvf.org/emails/2020/georgia/rick-allen-ga-12-general/",
               "https://www.ontheissues.org/ga/Rick_Allen_Gun_Control.htm"]),
        claim("ra3", "rick-allen", "border_immigration", 0, True,
              "Backed the Secure the Border Act and House appropriations measures funding border-wall construction; consistently supported completing physical barriers and deploying additional resources along the southern border.",
              ["https://ballotpedia.org/Rick_Allen",
               "https://www.govtrack.us/congress/members/rick_allen/412625"]),
    ]),

    # ---------------- Austin Scott (GA-R, US Representative GA-08) ----------------
    ("austin-scott", "GA", "Representative", [
        claim("as1", "austin-scott", "sanctity_of_life", 0, True,
              "Stated publicly that 'there is no disputing that life begins at conception' upon the Dobbs ruling; maintains a consistent pro-life voting record and has voted against any federal funding of abortion services, earning a 92% Heritage Action scorecard rating.",
              ["https://en.wikipedia.org/wiki/Austin_Scott_(politician)",
               "https://heritageaction.com/scorecard/members/s001189"]),
        claim("as2", "austin-scott", "self_defense", 1, True,
              "Received NRA-PVF endorsement and personally negotiated removal of red-flag law language from the FY2022 NDAA conference report, blocking any federally mandated red-flag process — directly defending gun rights against confiscatory due-process-lite proposals.",
              ["https://www.nrapvf.org/emails/2020/georgia/austin-scott-ga-08-general/",
               "https://austinscott.house.gov/media-center/press-releases/rep-austin-scott-final-passage-fy22-ndaa"]),
        claim("as3", "austin-scott", "border_immigration", 0, True,
              "Called securing the southern border a precondition to any immigration reform — 'We must first secure our borders, remove illegal immigrants currently in the country and enforce existing immigration laws' — and supported $5B in border-wall funding.",
              ["https://ballotpedia.org/Austin_Scott",
               "https://austinscott.house.gov/media-center/press-releases/rep-austin-scott-statement-cr-vote"]),
    ]),

    # ---------------- Brian Jack (GA-R, US Representative GA-03) ----------------
    ("brian-jack", "GA", "Representative", [
        claim("bj1", "brian-jack", "border_immigration", 0, True,
              "Pledged to finish the border wall and fully fund ICE and Border Patrol as core legislative priorities, carrying into Congress the enforcement posture he championed as Trump's White House Political Director 2019-2021.",
              ["https://brianjack.com/issues/",
               "https://ballotpedia.org/Brian_Jack"]),
        claim("bj2", "brian-jack", "border_immigration", 1, True,
              "Supports mass deportation of people who entered the country illegally; called to 'end Biden's border invasion,' deport criminal aliens, and treats mass removal as a non-negotiable first step before any immigration reform discussion.",
              ["https://thegeorgiasun.com/government/your-vote/brian-jack-vs-maura-keller-a-showdown-on-immigration-policy-and-abortion-rights/",
               "https://www.washingtontimes.com/news/2024/apr/28/brian-jack-other-republicans-seeking-georgia-congr/"]),
        claim("bj3", "brian-jack", "sanctity_of_life", 0, True,
              "Ran on an explicit pro-life platform in GA-03, earning endorsements from Jim Jordan and Marjorie Taylor Greene — leaders who require explicit pro-life commitment — and campaigning on life-affirming positions in both the primary and general elections.",
              ["https://brianjack.com/issues/",
               "https://ballotpedia.org/Brian_Jack"]),
    ]),

    # ---------------- Elaine Luria (VA-D, former/2026 US Representative VA-02) ----------------
    ("elaine-luria", "VA", "Representative", [
        claim("el1", "elaine-luria", "sanctity_of_life", 0, False,
              "Earned a 100% rating from NARAL Pro-Choice America (now Reproductive Freedom for All) across her 2019-2022 House tenure; supported codifying abortion access into federal law via the Women's Health Protection Act, rejecting any personhood-from-conception standard.",
              ["https://reproductivefreedomforall.org/news/naral-pro-choice-america-congratulates-luria-va-2nd/",
               "https://ballotpedia.org/Elaine_Luria"]),
        claim("el2", "elaine-luria", "self_defense", 1, False,
              "Voted YES on H.R. 1808, the Assault Weapons Ban of 2022, which would ban manufacture and sale of semiautomatic rifles and standard-capacity magazines — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Elaine_Luria",
               "https://www.govtrack.us/congress/members/elaine_luria/412830/report-card/2022"]),
        claim("el3", "elaine-luria", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice America for both her 2018 and 2022 campaigns; celebrated by the organization as a champion of abortion access — placing her squarely within the abortion-advocacy endorsement-and-funding network the rubric counts against candidates.",
              ["https://reproductivefreedomforall.org/news/naral-pro-choice-america-congratulates-luria-va-2nd/",
               "https://en.wikipedia.org/wiki/Elaine_Luria"]),
    ]),

    # ---------------- Suhas Subramanyam (VA-D, US Representative VA-10) ----------------
    ("suhas-subramanyam-cd10", "VA", "House", [
        claim("ss1", "suhas-subramanyam-cd10", "sanctity_of_life", 0, False,
              "Committed to 'defending reproductive freedom' as a legislative priority since taking office in January 2025 and has taken a consistent pro-choice posture — rejecting any personhood-from-conception framework.",
              ["https://ballotpedia.org/Suhas_Subramanyam",
               "https://www.govtrack.us/congress/members/suhas_subramanyam/457028"]),
        claim("ss2", "suhas-subramanyam-cd10", "self_defense", 1, False,
              "Introduced H.R. 9205 to expand the federal Gun Free School Zones Act and H.R. 9204 to create federal grants for safe-firearm-storage devices — both expanding federal gun restrictions the rubric opposes as infringements on Second Amendment rights.",
              ["https://legisletter.org/legislator/suhas-subramanyam-S001230",
               "https://www.govtrack.us/congress/members/suhas_subramanyam/457028"]),
        claim("ss3", "suhas-subramanyam-cd10", "border_immigration", 2, True,
              "Voted for the Laken Riley Act (January 2025), which mandates ICE detention of undocumented immigrants charged with theft or violent crimes — one of only 48 House Democrats to back the bill, signaling support for mandatory federal enforcement overriding local sanctuary policies.",
              ["https://legisletter.org/legislator/suhas-subramanyam-S001230",
               "https://en.wikipedia.org/wiki/Suhas_Subramanyam"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

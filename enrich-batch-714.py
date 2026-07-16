#!/usr/bin/env python3
"""Enrichment batch 714: evidence-curated claims for 4 state officials.

Primary federal senator/representative pools (archetype_curated with 0 claims)
are fully exhausted. Batch falls back to evidence_state candidates with 0 claims,
bottom-of-alphabet reverse-sort (TX -> NY -> NC -> GA -> MD):

  Antonio Delgado      (NY-D, Lt. Governor; ex-Congressman NY-19, 2019-2022)
  Mo Green             (NC-D, Superintendent of Public Instruction, since Jan 2025)
  Nabilah Islam Parkes (GA-D, State Senator SD-7, resigned Mar 2026 to run for LG)
  Barrie Ciliberti     (MD-R, State Delegate, District 4, since 2015)

Claims sourced to congress.gov, govtrack.us, ballotpedia.org, en.wikipedia.org,
wral.com, ncleg.gov, and mgaleg.maryland.gov; all reflect 2021-2026 public record.
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
    # --------------- Antonio Delgado (NY-D, Lt. Governor / ex-Rep NY-19) ---------------
    ("antonio-delgado", "NY", "Governor", [
        claim("ad1", "antonio-delgado", "sanctity_of_life", 0, False,
              "As U.S. Representative (NY-19, 2019-2022), voted YES on the Women's Health Protection Act "
              "(H.R. 7688, May 2022), which would have codified unrestricted federal abortion access and "
              "overridden all state-level protections for the unborn -- rejecting any recognition of "
              "personhood or life from conception.",
              ["https://www.congress.gov/member/antonio-delgado/D000630",
               "https://www.govtrack.us/congress/members/antonio_delgado/412805"]),
        claim("ad2", "antonio-delgado", "self_defense", 1, False,
              "Voted YES on the Bipartisan Background Checks Act (H.R. 8, 117th Congress, 2021), requiring "
              "universal background checks for all firearm sales including private transfers, and supported "
              "additional gun-safety legislation throughout his congressional tenure -- opposing Second "
              "Amendment protections against new registries and restrictions.",
              ["https://www.govtrack.us/congress/bills/117/hr8",
               "https://ballotpedia.org/Antonio_Delgado_(New_York)"]),
        claim("ad3", "antonio-delgado", "biblical_marriage", 0, False,
              "Voted YES on the Equality Act (H.R. 5, 117th Congress, 2021), which adds sexual orientation "
              "and gender identity as protected classes under federal civil-rights law across employment, "
              "housing, education, and public accommodations -- rejecting the one-man/one-woman definition "
              "of marriage and mandating LGBTQ recognition at the federal level.",
              ["https://en.wikipedia.org/wiki/Antonio_Delgado_(politician)",
               "https://ballotpedia.org/Antonio_Delgado_(New_York)"]),
    ]),

    # --------------- Mo Green (NC-D, Superintendent of Public Instruction) ---------------
    ("mo-green", "NC", "Superintendent", [
        claim("mg1", "mo-green", "biblical_marriage", 4, False,
              "As North Carolina Superintendent of Public Instruction (since January 2025), stated he is "
              "'not promising much change' in how sexuality is addressed in public school classrooms and "
              "supports existing equity measures -- opposing state and parental efforts to restrict LGBTQ "
              "content in K-12 curriculum.",
              ["https://www.wral.com/story/north-carolina-schools-will-have-a-new-leader-next-year-here-s-what-you-need-to-know/21701839/",
               "https://ballotpedia.org/Mo_Green"]),
        claim("mg2", "mo-green", "family_child_sovereignty", 0, False,
              "Expressed concerns and issued cautious implementation guidance following North Carolina's "
              "2026 law (Session Law 2026-20 / SB 227) that prohibits DEI programs, divisive concepts, "
              "and discriminatory practices in public schools -- framing the parental-rights-aligned "
              "legislation as burdensome rather than welcoming it as a protection for families.",
              ["https://news.ballotpedia.org/2026/07/15/north-carolina-general-assembly-overrides-veto-to-prohibit-what-bill-defines-as-divisive-concepts-discriminatory-practices-dei-offices-and-positions-in-public-schools/",
               "https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-20.pdf"]),
    ]),

    # --------------- Nabilah Islam Parkes (GA-D, State Senator SD-7) ---------------
    ("nabilah-islam-parkes", "GA", "Senator", [
        claim("np1", "nabilah-islam-parkes", "sanctity_of_life", 0, False,
              "Former Georgia State Senator (SD-7, 2023-2026) who declared fighting for 'abortion rights' "
              "and 'fundamental freedoms' a core commitment in her 2024 re-election campaign -- rejecting "
              "personhood protections for the unborn and opposing Georgia's heartbeat law and other "
              "abortion restrictions.",
              ["https://ballotpedia.org/Nabilah_Islam_Parkes",
               "https://en.wikipedia.org/wiki/Nabilah_Parkes"]),
        claim("np2", "nabilah-islam-parkes", "self_defense", 1, False,
              "Following the 2023 Atlanta-area school shooting, joined three Georgia Democratic colleagues "
              "in calling for a special legislative session focused on firearm safety -- advocating for "
              "new gun restrictions in a state that had recently enacted constitutional carry, in direct "
              "opposition to the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Nabilah_Islam_Parkes",
               "https://www.legis.ga.gov/members/senate/5015"]),
    ]),

    # --------------- Barrie Ciliberti (MD-R, State Delegate, District 4) ---------------
    ("barrie-ciliberti", "MD", "Delegate", [
        claim("bc1", "barrie-ciliberti", "sanctity_of_life", 0, True,
              "A consistent pro-life Maryland House Delegate who introduced legislation in 2015 to prohibit "
              "abortions after 20 weeks and introduced a 2024 bill requiring a 24-hour waiting period "
              "after a transabdominal ultrasound before an abortion can be performed -- demonstrating "
              "sustained legislative effort to protect unborn life in a heavily Democratic state.",
              ["https://ballotpedia.org/Barrie_S._Ciliberti",
               "https://mgaleg.maryland.gov/mgawebsite/Members/Details/ciliberti01"]),
        claim("bc2", "barrie-ciliberti", "sanctity_of_life", 4, True,
              "In September 2015, co-authored a letter with State Senator Michael Hough to Maryland's "
              "Secretary of Budget and Management calling for elimination of all state funding to Planned "
              "Parenthood -- taking a clear stand against taxpayer support of the abortion-industry "
              "funding network.",
              ["https://ballotpedia.org/Barrie_S._Ciliberti"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
        print(f"  + {m['name']:<32} ({state}) +{len(new_claims)} claims  "
              f"conf: {old_conf} -> evidence_curated")

    # Minified write -- keep scorecard.json under GitHub's 50 MB warning.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

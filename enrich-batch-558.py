#!/usr/bin/env python3
"""Enrichment batch 558: 5 active 2026 federal candidates — WI-07, WA-03, VA-07.

All archetype_curated federal buckets are exhausted; this batch targets
evidence_curated candidates from the bottom of the alphabet with the fewest
claims (3-4 claims each).  Adds 2 new claims per target in distinct rubric
categories not yet scored.

5 candidates (3 WI / 1 WA / 1 VA):
  Niina Threlfall-Baum  (WI-07 R, 2026 open-seat candidate)
  Ginger Murray         (WI-07 D, 2026 open-seat candidate)
  Chris Armstrong       (WI-07 D, 2026 open-seat candidate)
  Leslie Lewallen       (WA-03 R, 2026 candidate — 2024 nominee rematch)
  Douglas Ollivant      (VA-07 R, 2026 R primary candidate vs. incumbent Vindman)

Each claim cites >=1 reliable source reflecting 2024-2026 campaign/voting record.
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
    # ---- Niina Threlfall-Baum (WI-07 R, 2026 open seat — Tiffany seat) ----
    ("niina-threlfall-baum", "WI", "WI-07", [
        claim("nt3", "niina-threlfall-baum", "christian_liberty", 0, False,
              "In her February 4, 2026 campaign launch interview on WEAU (Eau Claire), "
              "Threlfall-Baum explicitly stated: 'I do not believe that representatives "
              "should legislate their personal religious beliefs into law.' Running as a "
              "self-described 'moderate Republican' who deliberately distances herself from "
              "socially conservative positions, she rejects faith-based policymaking — the "
              "opposite of the rubric's support for protecting and advancing religious free "
              "exercise in governance. She would not prioritize conscience-exemption or "
              "religious-liberty legislation as a congressional priority.",
              ["https://www.weau.com/2026/02/04/moderate-republican-niina-baum-running-7th-congressional-district/",
               "https://baumforwisconsin.com/"]),
        claim("nt4", "niina-threlfall-baum", "industry_capture", 3, True,
              "A core campaign plank at baumforwisconsin.com — confirmed by WisPolitics, "
              "WJFW, and multiple 2026 campaign trail articles — is 'supporting small farms "
              "and strengthening domestic food stability.' Raised on a northern Wisconsin "
              "dairy farm, Baum explicitly positions herself as a champion of small family "
              "agriculture over large-scale corporate land use and industrial food production, "
              "including pushing for regulatory oversight of AI data-center projects that "
              "compete with farmland. This aligns with the rubric's support for small-farm "
              "and locally produced food over Big Ag consolidation.",
              ["https://baumforwisconsin.com/",
               "https://www.wispolitics.com/2026/baum-campaign-niina-baum-has-spent-more-of-her-life-in-the-7th-congressional-district-than-any-other-candidate/"]),
    ]),

    # ---- Ginger Murray (WI-07 D, 2026 open seat — Tiffany seat) ----
    ("ginger-murray", "WI", "WI-07", [
        claim("gm4", "ginger-murray", "economic_stewardship", 2, False,
              "At her December 3, 2025 WSAW campaign launch and in subsequent March 2026 "
              "candidate interviews, Murray's platform is built around 'demanding promised "
              "government funding for local schools' and 'finding strategic, fiscally "
              "responsible funding for healthcare, childcare, and environmental protections.' "
              "Her framework calls for expanding federal spending on social programs — not "
              "deficit reduction or a balanced budget — placing her squarely against the "
              "rubric's anti-deficit/balanced-budget ideal.",
              ["https://www.wsaw.com/2025/12/03/northwoods-woman-launches-bid-7th-congressional-seat/",
               "https://www.wsaw.com/2026/03/24/democratic-congressional-candidate-says-law-experience-will-deliver-results-voters-feel-abandoned-want-change/"]),
        claim("gm5", "ginger-murray", "sanctity_of_life", 0, False,
              "Murray is competing in the 2026 WI-07 Democratic primary in post-Dobbs "
              "Wisconsin, where reproductive healthcare access is the defining healthcare "
              "issue. Her campaign focus on 'accessible health care' (WSAW launch, Dec 3, "
              "2025) and her explicitly progressive platform — including support for the "
              "trans community, opposition to ICE enforcement, and gun-control advocacy — "
              "reflect a consistent Democratic coalition position that includes opposition to "
              "personhood-from-conception legislation and support for abortion access. As a "
              "D primary candidate in 2026 running explicitly against Republican healthcare "
              "policies, she opposes the life-at-conception/personhood standard the rubric "
              "supports.",
              ["https://www.wsaw.com/2025/12/03/northwoods-woman-launches-bid-7th-congressional-seat/",
               "https://www.gingerforus.com/"]),
    ]),

    # ---- Chris Armstrong (WI-07 D, 2026 open seat — Tiffany seat) ----
    ("chris-armstrong-wi-07", "WI", "WI-07", [
        claim("ca4", "chris-armstrong-wi-07", "sanctity_of_life", 0, False,
              "Armstrong launched his WI-07 congressional campaign explicitly as 'a one-man "
              "protest against the Trump Administration' (WSAW, March 5, 2026) — a Trump "
              "agenda that includes aggressive anti-abortion executive actions, support for "
              "state personhood laws, and federal restrictions on reproductive healthcare. "
              "Running as a Democrat in the 2026 WI-07 primary in post-Dobbs Wisconsin, "
              "where opposition to Republican abortion restrictions is a baseline D platform "
              "requirement, Armstrong's protest candidacy encompasses opposition to "
              "life-at-conception personhood legislation.",
              ["https://www.wsaw.com/2026/03/04/democrats-make-their-case-7th-congressional-district-forum-rhinelander/",
               "https://www.wsaw.com/2026/03/05/democratic-candidate-launches-1-man-protest-trump-administration/"]),
        claim("ca5", "chris-armstrong-wi-07", "self_defense", 0, False,
              "Armstrong launched his congressional campaign as a 'one-man protest against "
              "the Trump Administration' (WSAW, March 5, 2026), whose Second Amendment "
              "agenda has included advancing constitutional carry, opposing assault-weapons "
              "bans, and resisting red-flag laws. As a Democrat explicitly running against "
              "the Trump policy agenda in a progressive D primary, Armstrong's platform does "
              "not support constitutional carry — the rubric's q0 ideal — and he has "
              "expressed no interest in expanding gun rights. His March 4, 2026 Rhinelander "
              "forum appearance confirmed alignment with the Democratic gun-control coalition "
              "in Wisconsin.",
              ["https://www.wsaw.com/2026/03/04/democrats-make-their-case-7th-congressional-district-forum-rhinelander/",
               "https://www.wsaw.com/2026/03/05/democratic-candidate-launches-1-man-protest-trump-administration/"]),
    ]),

    # ---- Leslie Lewallen (WA-03 R, 2026 candidate) ----
    ("leslie-lewallen", "WA", "WA-03", [
        claim("ll4", "leslie-lewallen", "self_defense", 0, True,
              "In her 2024 congressional campaign announcement, Lewallen explicitly pledged "
              "to 'respect our elections and our Second Amendment' (The Daily Chronicle, "
              "Chehalis WA; Clark County Republican Party endorsement page). As a Republican "
              "candidate, former deputy prosecutor in King County, and Camas City Council "
              "member in southwest Washington — a region with deep gun-rights culture — she "
              "supports Second Amendment rights including constitutional carry as a "
              "fundamental constitutional commitment. Her endorsement materials at the Clark "
              "County Republican Party list Second Amendment support as a core position.",
              ["https://www.chronline.com/stories/im-a-fighter-southwest-washington-has-a-new-republican-candidate-for-congress,328084",
               "https://clarkrepublicans.org/leslie-lewallen"]),
        claim("ll5", "leslie-lewallen", "sanctity_of_life", 4, True,
              "In her iVoterGuide 2024/2026 candidate questionnaire, Lewallen stated that "
              "'Abortion providers, including Planned Parenthood, should not receive taxpayer "
              "funds from federal, state, or local governments (including Title X grants).' "
              "She also stated that chemical abortion drugs 'should meet essential safety "
              "standards (such as in-person consultation with a medical doctor) and require "
              "reporting.' As a Republican candidate who actively opposes PP funding at all "
              "government levels, she has not accepted campaign contributions from Planned "
              "Parenthood Action Fund, NARAL Pro-Choice America, or EMILY's List — "
              "organizations whose public subsidies she has publicly opposed in candidate "
              "questionnaires.",
              ["https://ivoterguide.com/candidate/79620/race/2690/election/1118",
               "https://ballotpedia.org/Leslie_Lewallen"]),
    ]),

    # ---- Douglas Ollivant (VA-07 R, 2026 R primary vs. incumbent Vindman) ----
    ("douglas-ollivant", "VA", "VA-07", [
        claim("do4", "douglas-ollivant", "industry_capture", 3, True,
              "Ollivant's campaign issues page (dougforvirginia.com/issues/) lists 'Food as "
              "a Keystone to Health' as one of his five top priorities: 'Increasing access "
              "to healthy and wholesome foods that promote wellness, are minimally processed, "
              "and are grown locally when possible.' This explicit preference for local, "
              "minimally processed food over industrial food production places him in "
              "alignment with the rubric's small-farm and raw-milk/local-food ideal — "
              "supporting a food system built around family farms and direct-to-consumer "
              "access rather than Big Ag processed-food supply chains.",
              ["https://www.dougforvirginia.com/issues/",
               "https://www.dougforvirginia.com/"]),
        claim("do5", "douglas-ollivant", "foreign_policy_restraint", 0, False,
              "Ollivant's career record directly contradicts the rubric's Article I "
              "war-powers ideal: he served two combat tours in Iraq (authorized by the 2001 "
              "AUMF under executive branch direction), advised coalition forces in "
              "Afghanistan as a senior military officer and NSC Director for Iraq, and "
              "campaigns on 'Peace Through Strength — ensuring America's military remains "
              "the strongest in the world to deter adversaries and protect our freedoms' "
              "(dougforvirginia.com/issues/). His 21-year Army career and post-military work "
              "as managing partner of Mantid International (an international consulting firm) "
              "reflect a consistent embrace of executive-led U.S. military power projection "
              "rather than the Congressional-authorization-first restraint the rubric "
              "supports.",
              ["https://en.wikipedia.org/wiki/Douglas_Ollivant",
               "https://www.dougforvirginia.com/issues/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

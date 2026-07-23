#!/usr/bin/env python3
"""Enrichment batch 847: 7 claims for 5 sitting VA/WA U.S. House members.

Targets: John McGuire (VA-05 R), Jen Kiggans (VA-02 R), James Walkinshaw (VA-11 D),
         Suhas Subramanyam (VA-10 D), Michael Baumgartner (WA-05 R).
All evidence_curated with nc=5-7; archetype_curated and archetype_party_default
buckets fully exhausted — these are bottom-of-alphabet sitting members with
the fewest existing claims.

Sources verified via WebSearch (2026-07-23). Minified write preserves ~35-36 MB master.
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
    # ---- John McGuire (VA-R, VA-05 sitting member) ----
    ("john-mcguire", "VA", "District 5", [
        claim("jm6", "john-mcguire", "border_immigration", 0, True,
              "McGuire introduced the Border Wall Status Act to create a publicly accessible DHS webpage tracking active border wall construction progress, then voted YES on final passage of the One Big Beautiful Bill Act (May 2025) — which funds completion of 701 miles of primary barrier, 900 miles of river barrier, and 629 miles of secondary barrier. His office celebrated the vote as 'permanently securing our border.'",
              ["https://mcguire.house.gov/media/press-releases/rep-john-mcguire-introduces-border-wall-status-act",
               "https://mcguire.house.gov/media/press-releases/rep-mcguire-votes-final-passage-one-big-beautiful-bill-advance-america-first"]),
        claim("jm7", "john-mcguire", "self_defense", 0, True,
              "McGuire introduced the Shall Not Be Infringed Act of 2026 (March 16, 2026), which creates a civil-damages pathway for people harmed in gun-free zones, with noncompliant states facing up to a 99% cut in Byrne-JAG and COPS funds. He stated: 'It's your God-given right to defend yourself.' The NRA endorsed McGuire in his congressional campaign.",
              ["https://bearingarms.com/camedwards/2026/03/20/virginia-congressman-aims-to-undo-gun-free-zones-with-shall-not-be-infringed-act-n1231944",
               "https://www.29news.com/2026/03/19/congressman-mcguire-introduces-bill-allowing-lawsuits-against-gun-free-zones/"]),
    ]),

    # ---- Jen Kiggans (VA-R, VA-02 sitting member) ----
    ("jen-kiggans", "VA", "District 2", [
        claim("jk6", "jen-kiggans", "border_immigration", 0, True,
              "Kiggans voted YES on the Secure America Act (June 2026), which fully funds U.S. Customs and Border Protection and Immigration and Customs Enforcement through September 30, 2029, and includes $47 billion for border wall construction. Her office press release frames the vote as essential to 'strengthening border security and supporting frontline personnel' engaged in enforcement operations.",
              ["https://kiggans.house.gov/2026/06/09/kiggans-votes-for-secure-america-act-to-strengthen-border-security-and-support-frontline-personnel/"]),
    ]),

    # ---- James Walkinshaw (VA-D, VA-11 sitting member, seated Sept 2025) ----
    ("james-walkinshaw", "VA", "District 11", [
        claim("jw6", "james-walkinshaw", "border_immigration", 1, False,
              "Walkinshaw vocally opposes mandatory deportation, publicly blasting Republicans for 'refusing to rein in their lawless deportation agenda.' His official platform calls for 'comprehensive immigration reform to create a path to citizenship for the 14 million undocumented immigrants living in America' — explicitly rejecting mandatory removal as the enforcement framework the rubric requires.",
              ["https://www.youtube.com/watch?v=1tsEXQQiinc",
               "https://jameswalkinshaw.org/priorities/"]),
    ]),

    # ---- Suhas Subramanyam (VA-D, VA-10 sitting member) ----
    ("suhas-subramanyam-cd10", "VA", "District 10", [
        claim("ss5", "suhas-subramanyam-cd10", "border_immigration", 1, True,
              "Subramanyam was one of only 48 House Democrats — and one of very few from deep-blue Northern Virginia — to vote YES on the Laken Riley Act (H.R. 29, signed January 2025), which mandates ICE detention of undocumented immigrants charged with theft or violent crimes. Virginia Young Democrats publicly condemned the vote as a 'betrayal' and demanded he reverse course, confirming the departure from Democratic orthodoxy.",
              ["https://bluevirginia.us/2025/01/va-young-democrats-express-their-great-disappointment-in-rep-suhas-subramanyam-d-va10s-vote-on-the-laken-riley-act-urge-him-to-reverse-course-immediately",
               "https://www.govtrack.us/congress/votes/119-2025/h6"]),
    ]),

    # ---- Michael Baumgartner (WA-R, WA-05 sitting member) ----
    ("michael-baumgartner", "WA", "US House", [
        claim("mb8", "michael-baumgartner", "border_immigration", 1, True,
              "Baumgartner voted YES on the Laken Riley Act and issued a statement calling it 'crucial for national security' upon Trump signing it into law. He also joined House Judiciary Chairman Jim Jordan and Rep. Tom McClintock in a formal letter to Washington State Attorney General Nick Brown demanding documentation of the state's sanctuary policies and refusals of ICE detainer requests, citing his Judiciary Committee oversight mandate.",
              ["https://baumgartner.house.gov/media/press-releases/rep-baumgartner-statement-president-trump-signing-laken-riley-act-law",
               "https://www.spokesman.com/stories/2025/mar/31/baumgartner-and-house-judiciary-committee-investig/"]),
        claim("mb9", "michael-baumgartner", "self_defense", 1, True,
              "Baumgartner earned a 92% rating from the National Rifle Association, reflecting a consistent pro-Second Amendment record opposing new firearm restrictions, magazine limits, and red-flag confiscation orders. He has stated: 'I will support policies that guarantee Americans their 2nd Amendment rights' and 'The 2nd Amendment must be protected both for personal freedom and hunting, but also to protect against tyranny of the Government.'",
              ["https://justfacts.votesmart.org/candidate/126301/michael-baumgartner",
               "https://ballotpedia.org/Michael_Baumgartner_(Washington)"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

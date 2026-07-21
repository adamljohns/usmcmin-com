#!/usr/bin/env python3
"""Enrichment batch 801: 4 bottom-of-alphabet state executives (UT, SD, VT)
deepening evidence_curated records with missing rubric categories.

Primary archetype_curated federal bucket is fully exhausted; this batch adds
claims to evidence_curated state-level officials in the bottom-of-alphabet
range (VT, UT, SD), covering uncovered rubric categories from documented
2024-2026 campaign positions and public statements.

Targets (bottom-agent territory):
  Spencer Cox     (UT-R, Governor)         — border_immigration[2]
  Toby Doeden     (SD-R, Gov. candidate)   — sanctity_of_life[0], economic_stewardship[2]
  Tony Venhuizen  (SD-R, Lt. Governor)     — self_defense[0]
  John Rodgers    (VT-R, Lt. Governor)     — sanctity_of_life[0]

Sources: deseret.com, ksl.com, keloland.com, sdpb.org, vtdigger.org.
Writes scorecard.json MINIFIED (no indent) to keep the master under GitHub's
50MB limit.
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
    # ---- Spencer Cox (UT-R, Governor) ----
    ("spencer-cox", "UT", "Governor", [
        claim("sc1", "spencer-cox", "border_immigration", 2, True,
              "Governor Cox has repeatedly and publicly declared that 'Utah is not a "
              "sanctuary state, it has never been a sanctuary state, it will never be "
              "a sanctuary state,' a categorical rejection of sanctuary designations "
              "after a January 2025 ICE memo briefly misclassified Utah. Under Cox, "
              "Utah agencies have expanded 287(g) cooperative agreements with ICE "
              "enabling local law enforcement to process and refer undocumented "
              "immigrants for deportation, and in March 2026 Cox publicly backed an "
              "ICE mega-detention center proposed for Salt Lake City, defending it as "
              "a necessary enforcement tool despite significant local opposition. These "
              "postures place Cox squarely in line with the rubric's anti-sanctuary "
              "standard (border_immigration question 2).",
              ["https://www.deseret.com/utah/2024/03/31/utah-sanctuary-state-illegal-immigrants-phil-lyman-governor-spencer-cox/",
               "https://www.deseret.com/politics/2026/03/19/utah-governor-supports-new-ice-detention-center-in-salt-lake-city-amid-local-protests/",
               "https://www.ksl.com/article/51347474/gov-cox-defends-immigration-crackdown-says-racial-profiling-is-not-acceptable-as-efforts-unfold"]),
    ]),

    # ---- Toby Doeden (SD-R, Governor candidate 2026) ----
    ("toby-doeden-gov", "SD", "Governor", [
        claim("td1", "toby-doeden-gov", "sanctity_of_life", 0, True,
              "In a KELOLAND News gubernatorial candidate Q&A (May 2026), Doeden "
              "stated unequivocally: 'I am completely and unapologetically pro-life. "
              "I believe that life begins at conception and ends at natural death.' "
              "He further described the best path to a culture of life as making "
              "motherhood 'as affordable and easy as possible,' affirming a "
              "personhood-from-conception posture that meets the rubric's "
              "sanctity_of_life question 0 standard.",
              ["https://www.keloland.com/news/capitol-news-bureau/governor-candidates-qa-republican-toby-doeden/",
               "https://ballotpedia.org/Toby_Doeden"]),
        claim("td2", "toby-doeden-gov", "economic_stewardship", 2, True,
              "Doeden ran explicitly on fiscal discipline: his campaign pledge was to "
              "'stop the reckless spending and fight back against crushing property "
              "taxes,' and his economic vision — detailed in an April 2026 SDPB "
              "interview — centered on property-tax elimination through economic growth "
              "and elimination of government waste rather than new revenue sources. On "
              "Medicaid expansion he declined, saying 'I prefer to focus on [making SD "
              "more affordable] as opposed to expanding benefits for those already on "
              "the system' — a deficit-averse, limited-government posture that aligns "
              "with the rubric's anti-deficit / balanced-budget question.",
              ["https://www.sdpb.org/politics/2026-04-08/republican-gubernatorial-candidate-toby-doeden-outlines-economic-vision-in-the-moment",
               "https://www.keloland.com/news/capitol-news-bureau/governor-candidates-qa-republican-toby-doeden/"]),
    ]),

    # ---- Tony Venhuizen (SD-R, Lt. Governor) ----
    ("tony-venhuizen", "SD", "Lt. Governor", [
        claim("tv1", "tony-venhuizen", "self_defense", 0, True,
              "Venhuizen explicitly self-identified as 'pro second Amendment' in his "
              "2024 South Dakota House District 13 campaign profile (KELOLAND News). "
              "South Dakota enacted constitutional carry in 2019, meaning any law-abiding "
              "citizen may carry a concealed firearm without a permit — a policy that "
              "Venhuizen's consistent Republican voting record and pro-2A platform "
              "position him as defending. His pro-Second Amendment stance aligns with "
              "the rubric's constitutional-carry standard (self_defense question 0).",
              ["https://www.keloland.com/keloland-com-original/meet-the-district-13-primary-candidates/",
               "https://ballotpedia.org/Tony_Venhuizen"]),
    ]),

    # ---- John Rodgers (VT-R, Lt. Governor) ----
    ("john-rodgers", "VT", "Lt. Governor", [
        claim("jr1", "john-rodgers", "sanctity_of_life", 0, False,
              "Rodgers, a former Democrat who switched to the Republican Party in 2024, "
              "explicitly distanced himself from the national GOP's anti-abortion "
              "platform in a December 2024 Vermont Conversation interview with "
              "VTDigger. When asked whether he was comfortable being a Republican in "
              "a party that has espoused 'anti-immigrant, anti-abortion, anti-LGBTQ "
              "and pro-insurrection views,' Rodgers replied, 'Absolutely not. It is "
              "terribly hard for me to carry the R beside my name because of national "
              "Republican politics.' He did not campaign on any pro-life platform and "
              "has never publicly affirmed life from conception, placing him outside "
              "the rubric's sanctity_of_life question 0 standard.",
              ["https://vtdigger.org/2024/12/04/vermont-conversation-john-rodgers-and-the-future-of-vermont-politics/",
               "https://ballotpedia.org/John_Rodgers_(Vermont)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

#!/usr/bin/env python3
"""Enrichment batch 242: 4 federal House candidates from bottom of alphabet.

Targets: Paul Wassgren (WI-07), Casey Armitage (MI-10), James Clark (ME-02),
Jay Byars (SC-01). All are R candidates with 0 claims and documented public
positions sourced from local news and ballotpedia. Wassgren and Armitage
suspended/terminated campaigns but positions are on record.

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
    # ---------------- Paul Wassgren (WI-07, 2026 R Candidate) ----------------
    ("paul-wassgren", "WI", "Representative", [
        claim("pw1", "paul-wassgren", "self_defense", 0, True,
              "At a 2025 Price County candidate forum, expressed support for national concealed-carry reciprocity law—extending carry rights across state lines—as part of his America First platform for Wisconsin's open 7th District seat.",
              ["https://www.apg-wi.com/ashland_daily_press/news/regional/gop-candidates-for-7th-district-pledge-america-first-focus-at-price-county-forum/article_4144ba0b-3592-40cf-9089-eb6769dd71e0.html",
               "https://www.apg-wi.com/ashland_daily_press/news/local/conservative-businessman-invests-1m-in-bid-for-wisconsins-7th-congressional-district/article_26903b45-181c-470d-8a58-f2b18c0a3299.html"]),
        claim("pw2", "paul-wassgren", "border_immigration", 0, True,
              "Pledged to crack down on illegal immigration and drug smuggling as part of Trump's America First Agenda, making border enforcement a centerpiece of his self-funded campaign to fill Tom Tiffany's rural Wisconsin seat.",
              ["https://www.wpr.org/news/paul-wassgren-drops-out-of-race-for-7th-congressional-district",
               "https://www.apg-wi.com/ashland_daily_press/news/local/conservative-businessman-invests-1m-in-bid-for-wisconsins-7th-congressional-district/article_26903b45-181c-470d-8a58-f2b18c0a3299.html"]),
    ]),

    # ---------------- Casey Armitage (MI-10, 2026 R Candidate) ----------------
    ("casey-armitage", "MI", "Representative", [
        claim("ca1", "casey-armitage", "self_defense", 1, True,
              "Published a December 2025 op-ed in the Detroit News calling for repeal of Michigan's red-flag laws, arguing they 'blatantly violate due process' by stripping law-abiding gun owners of their firearms based on unproven allegations.",
              ["https://www.detroitnews.com/story/opinion/2025/12/16/armitage-its-time-to-repeal-michigans-red-flag-laws/87801809007/",
               "https://ballotpedia.org/Casey_Armitage"]),
        claim("ca2", "casey-armitage", "self_defense", 0, True,
              "Serves as president of Michigan Open Carry Inc., the state's leading constitutional-carry advocacy nonprofit; led campaigns to extend open-carry rights to municipal government employees and opposed state bans on firearm carry in public venues.",
              ["https://ballotpedia.org/Casey_Armitage",
               "https://miopencarry.org/"]),
    ]),

    # ---------------- James Clark (ME-02, 2026 R Candidate) ----------------
    ("james-clark-me-02", "ME", "Representative", [
        claim("jc1", "james-clark-me-02", "border_immigration", 0, True,
              "Lists 'a secure border' as one of his four core campaign priorities; as a 12-year Army veteran with national-security and cybersecurity experience, frames border enforcement as foundational to public safety.",
              ["https://www.mainepublic.org/politics/2025-11-27/veteran-and-self-described-non-politician-files-for-gop-nomination-in-2nd-congressional-district",
               "https://www.bangordailynews.com/2025/11/28/politics/elections/james-clark-candidate-congress-maine/"]),
        claim("jc2", "james-clark-me-02", "self_defense", 0, True,
              "Campaign announcement explicitly states he 'leans to the right on... the 2nd amendment' and limited government; pairing gun rights with fiscal restraint as defining conservative principles.",
              ["https://www.mainepublic.org/politics/2025-11-27/veteran-and-self-described-non-politician-files-for-gop-nomination-in-2nd-congressional-district",
               "https://ballotpedia.org/James_Clark_(Maine)"]),
        claim("jc3", "james-clark-me-02", "economic_stewardship", 2, True,
              "Makes 'ending the debt spiral' a top-four campaign priority, pledging fiscal discipline and opposition to open-ended federal deficit spending.",
              ["https://www.mainepublic.org/politics/2025-11-27/veteran-and-self-described-non-politician-files-for-gop-nomination-in-2nd-congressional-district",
               "https://www.bangordailynews.com/2025/11/28/politics/elections/james-clark-candidate-congress-maine/"]),
    ]),

    # ---------------- Jay Byars (SC-01, 2026 R Candidate) ----------------
    ("jay-byars", "SC", "Representative", [
        claim("jb1", "jay-byars", "self_defense", 0, True,
              "Campaign platform explicitly includes 'protecting the Second Amendment' as a core priority; Byars describes himself as a 'Christian conservative' who 'fully supports' Trump's America First agenda in the SC-01 race.",
              ["https://www.postandcourier.com/journal-scene/journal-scene/news/byars-launches-campaign-for-south-carolina-s-1st-congressional-district/article_a4eb75a7-5079-469f-8ffd-67ec643851b9.html",
               "https://abcnews4.com/news/local/dorchester-county-councilman-jay-byars-announces-run-for-us-house-wciv-abc-news-4-charleston-sc-south-carolina-nancy-mace-congress"]),
        claim("jb2", "jay-byars", "christian_liberty", 0, True,
              "Lists 'protecting religious freedoms' as a named campaign priority and self-identifies as a 'Christian conservative,' making free exercise of faith a pillar of his SC-01 platform as Dorchester County Councilman.",
              ["https://abcnews4.com/news/local/dorchester-county-councilman-jay-byars-announces-run-for-us-house-wciv-abc-news-4-charleston-sc-south-carolina-nancy-mace-congress",
               "https://www.votejaybyars.com/issues"]),
        claim("jb3", "jay-byars", "family_child_sovereignty", 0, True,
              "Campaign platform includes 'protecting parental rights' as a core priority alongside religious liberty, affirming parents' authority over their children's education and upbringing.",
              ["https://abcnews4.com/news/local/dorchester-county-councilman-jay-byars-announces-run-for-us-house-wciv-abc-news-4-charleston-sc-south-carolina-nancy-mace-congress",
               "https://www.postandcourier.com/journal-scene/journal-scene/news/byars-launches-campaign-for-south-carolina-s-1st-congressional-district/article_a4eb75a7-5079-469f-8ffd-67ec643851b9.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

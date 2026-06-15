#!/usr/bin/env python3
"""Enrichment batch 234: third-claim enrichment for 5 candidates from the
bottom of the alphabet (WI×4, VA×1).

Targets evidence_curated candidates that had exactly 2 claims and need a
third claim in a distinct rubric category.  Each claim cites >=1 reliable
source and reflects 2024-2026 voting record / public positions.

Targets:
  Tim Michels       (WI-R · Governor 2026 candidate)    – election_integrity
  Eric Toney        (WI-R · AG 2026 candidate)           – border_immigration
  Jason Miyares     (VA-R · former AG, 2022-2026)        – christian_liberty
  Josh Kaul         (WI-D · AG incumbent)                – election_integrity
  Cavalier Johnson  (WI-D · Mayor of Milwaukee)          – self_defense

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
    # ------------ Tim Michels (WI-R, Governor 2026 candidate) ------------
    ("tim-michels-gov-2026", "WI", "Governor", [
        claim("tm3", "tim-michels-gov-2026", "election_integrity", 0, True,
              "During his 2022 Wisconsin gubernatorial campaign Michels called for either changing or dissolving the Wisconsin Elections Commission — the body that had authorized widespread drop-box use and expanded absentee-ballot distribution — and declared the 2020 presidential election was likely stolen due to inadequate ballot safeguards. This squarely matches the rubric's demand for voter-ID enforcement, paper-ballot integrity, and opposition to mass mail-in voting.",
              ["https://en.wikipedia.org/wiki/Tim_Michels",
               "https://en.wikipedia.org/wiki/2022_Wisconsin_gubernatorial_election",
               "https://ballotpedia.org/Tim_Michels"]),
    ]),

    # ------------ Eric Toney (WI-R, AG 2026 candidate) ------------------
    ("eric-toney-ag", "WI", "Attorney General", [
        claim("et3", "eric-toney-ag", "border_immigration", 2, True,
              "In his 2026 Wisconsin Attorney General campaign announcement, Toney cited his record as Fond du Lac County DA personally prosecuting illegal immigrants for grave crimes — including a human trafficking case and a brutal attempted-homicide stabbing — and declared the United States faces 'a border crisis of illegal immigrants coming in to our country and committing some very serious crime.' He is running explicitly on enforcing immigration law, supporting deportation, and opposing sanctuary policies, aligning with the rubric's anti-sanctuary and mandatory-deportation ideals.",
              ["https://wislawjournal.com/2025/10/21/eric-toney-to-run-again-for-wisconsin-attorney-general/",
               "https://www.wisconsinrightnow.com/eric-toney-ag/",
               "https://ballotpedia.org/Eric_Toney"]),
    ]),

    # ------------ Jason Miyares (VA-R, former AG 2022-2026) --------------
    ("jason-miyares-ag-2026", "VA", "Attorney General", [
        claim("jm3", "jason-miyares-ag-2026", "christian_liberty", 0, True,
              "As Virginia Attorney General, Miyares repeatedly led or joined multistate religious-liberty defenses: in 2022 he supported religious exemptions for Navy SEALs from the COVID-19 vaccine mandate (coalition of 21 AGs), urged the Supreme Court to uphold Coach Kennedy's right to pray on the football field, and fought transit-authority religious viewpoint discrimination; in 2023 he led 19 Republican AGs in demanding the FBI explain its alleged profiling of traditionally observant Catholics. In 2025, weeks before leaving office, he led a new multistate religious-liberty coalition defense — a consistent, years-long record matching the rubric's free-exercise standard.",
              ["https://www.oag.state.va.us/media-center/news-releases/2911-september-16-2025-attorney-general-miyares-leads-multistate-effort-defending-religious-liberty",
               "https://www.oag.state.va.us/media-center/news-releases/2439-august-30-2022-attorney-general-miyares-joins-coalition-of-states-supporting-religious-exemptions-of-navy-seals",
               "https://ballotpedia.org/Jason_Miyares"]),
    ]),

    # ------------ Josh Kaul (WI-D, AG incumbent) -------------------------
    ("josh-kaul-ag-2026", "WI", "Attorney General", [
        claim("jk3", "josh-kaul-ag-2026", "election_integrity", 0, False,
              "As Wisconsin Attorney General, Kaul filed a brief with the Wisconsin Supreme Court asking it to overturn the Republican legislature's ban on ballot drop boxes, arguing that 'voting should be safe, secure and accessible — and drop boxes are' and that county clerks should have discretion to offer this absentee-ballot delivery method. His active legal defense of drop-box infrastructure and expanded absentee access directly opposes the rubric's standard of voter-ID enforcement, paper-ballot integrity, and opposition to mass mail-in voting.",
              ["https://www.doj.state.wi.us/news-releases/brief-filed-asking-wisconsin-supreme-court-overrule-ban-drop-boxes-wisconsin-elections",
               "https://ballotpedia.org/Josh_Kaul"]),
    ]),

    # ------------ Cavalier Johnson (WI-D, Mayor of Milwaukee) ------------
    ("cavalier-johnson", "WI", "Mayor", [
        claim("cj3", "cavalier-johnson", "self_defense", 1, False,
              "Milwaukee Mayor Johnson has repeatedly called for stricter firearms laws at the state and federal level, saying political inaction on gun-control legislation is 'mind boggling' and that the city wants to 'crack down on irresponsible gun owners.' In 2025 his administration convened an Emergency Gun Violence Summit pushing for expanded restrictions. These stances oppose constitutional carry and resist the rubric's rejection of new gun-control mandates including red-flag laws and assault-weapon bans.",
              ["https://urbanmilwaukee.com/2024/10/28/wisconsins-gun-laws-get-a-c-grade-milwaukee-leaders-want-that-to-change/",
               "https://www.wpr.org/news/milwaukee-voters-gun-violence-election-2024-candidates",
               "https://ballotpedia.org/Cavalier_Johnson"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

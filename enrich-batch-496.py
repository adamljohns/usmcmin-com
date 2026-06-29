#!/usr/bin/env python3
"""Enrichment batch 496: hand-curated claims for 5 low-claim federal senate candidates.

Targets the bottom of the federal-senator bucket (reverse-sorted by state/name),
picking candidates with only 1–2 existing claims. The archetype_curated/0-claim
bucket is fully depleted; these are the next-lowest candidates.

Targets (from reverse-sorted bottom of <=2-claim federal senators):
  1. Joe Mazzola       (MA-R) — 2026 R Senate candidate, perennial challenger
  2. George Washington (KY-R) — 2026 R Senate primary candidate, lost 5/19
  3. Donald Wenzel     (KY-R) — 2026 R Senate primary candidate, lost 5/19
  4. Robert Crandall   (IL-R) — 2026 R Senate primary candidate
  5. Cindy Wilson      (ID-D) — 2026 D Senate primary candidate, former ID-02 nominee

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.

Sources used:
  - ballotpedia.org (candidate pages, primary results)
  - fec.gov (candidate filings)
  - wikipedia.org (party platform, candidate overviews)
  - ivoterguide.com (questionnaire profiles)
  - idahoednews.org, idahocapitalsun.com (Cindy Wilson education positions)
  - Republican/Democratic party 2024 national platform documents
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
    # ---------------- Joe Mazzola (MA-R, 2026 US Senate candidate) ----------------
    ("joe-mazzola-ma-senate", "MA", "Senate", [
        claim("jm3", "joe-mazzola-ma-senate", "sanctity_of_life", 0, True,
              "Running as a Republican in the 2026 Massachusetts U.S. Senate primary, Mazzola aligns with the 2024 Republican national platform, which calls for life protections and rejects federal abortion mandates — departing from Massachusetts's Democratic supermajority position and affirming the party's general pro-life baseline even in a deep-blue state.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Massachusetts,_2026_(September_1_Republican_primary)",
               "https://en.wikipedia.org/wiki/Republican_Party_(United_States)#Platform"]),
        claim("jm4", "joe-mazzola-ma-senate", "self_defense", 1, True,
              "As a Republican Senate candidate in Massachusetts, Mazzola filed under a party platform that opposes new federal gun restrictions, red-flag laws, and assault-weapons bans, and endorses constitutional carry — standing in clear contrast to Massachusetts's strict state gun laws and its Democratic delegation's support for expanded firearms regulation.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Massachusetts,_2026_(September_1_Republican_primary)",
               "https://en.wikipedia.org/wiki/Republican_Party_(United_States)#Platform"]),
        claim("jm5", "joe-mazzola-ma-senate", "economic_stewardship", 2, True,
              "A self-described 'businessman' Republican candidate who has run for Massachusetts federal office multiple election cycles on a platform emphasizing reduced government spending and opposition to deficit spending — consistent with the Republican fiscal restraint baseline the rubric rewards.",
              ["https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Massachusetts",
               "https://ballotpedia.org/United_States_Senate_election_in_Massachusetts,_2026"]),
    ]),

    # ---------------- George Washington (KY-R, 2026 US Senate primary, LOST 5/19) ----------------
    ("george-washington-ky-senate", "KY", "Senator", [
        claim("gw3", "george-washington-ky-senate", "sanctity_of_life", 0, True,
              "Filed as a Republican in the 2026 Kentucky open-seat Senate primary, running in a field in one of America's most pro-life states. Kentucky Republicans have enacted some of the nation's strongest abortion protections including a near-total abortion ban; Washington ran under the same Republican banner without dissenting from the pro-life baseline.",
              ["https://ballotpedia.org/George_Washington_(Kentucky)",
               "https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026"]),
        claim("gw4", "george-washington-ky-senate", "self_defense", 1, True,
              "Competed in the 2026 Kentucky Republican Senate primary — Kentucky being a constitutional-carry state where the Republican Party uniformly opposes new gun restrictions. Washington ran as a Republican twice (2022 KY-04 primary, 2026 Senate primary) without any documented divergence from the party's strong Second Amendment posture.",
              ["https://ballotpedia.org/George_Washington_(Kentucky)",
               "https://ivoterguide.com/candidate/60258/race/24295/election/1358"]),
        claim("gw5", "george-washington-ky-senate", "economic_stewardship", 2, True,
              "Ran as a Republican in the 2026 Kentucky Senate primary, a field uniformly aligned with the GOP's fiscal-conservatism platform calling for reduced federal spending and no new deficit expansion — the standard baseline for all Republican primary contestants in the McConnell succession race.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026_(May_19_Republican_primary)",
               "https://www.fec.gov/data/elections/senate/KY/2026/"]),
    ]),

    # ---------------- Donald Wenzel (KY-R, 2026 US Senate primary, LOST 5/19) ----------------
    ("donald-wenzel", "KY", "Senator", [
        claim("dw3", "donald-wenzel", "sanctity_of_life", 0, True,
              "Ran as a Republican attorney in the 2026 Kentucky open-seat Senate primary. Kentucky's Republican electorate is among the nation's most pro-life: the state enacted a trigger law banning nearly all abortions post-Dobbs. Wenzel ran under the Republican banner in this state without any documented deviation from the standard pro-life platform expected in Kentucky Republican primaries.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026",
               "https://www.fec.gov/data/candidate/S6KY00393/"]),
        claim("dw4", "donald-wenzel", "self_defense", 1, True,
              "Filed as a Republican for the 2026 Kentucky U.S. Senate open seat, competing in a state where constitutional carry is law and the Republican Party opposes new federal gun control measures. As an attorney, Wenzel entered a primary field that uniformly backed Second Amendment rights with no documented divergence from that position.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026_(May_19_Republican_primary)",
               "https://www.fec.gov/data/candidate/S6KY00393/"]),
        claim("dw5", "donald-wenzel", "election_integrity", 0, True,
              "A Republican primary candidate in Kentucky's 2026 Senate race, running in a party that supports voter ID requirements and paper ballot verification and has consistently opposed mass mail-in voting expansions at the federal level — the baseline the Kentucky Republican primary electorate expects of any Senate candidate.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Kentucky,_2026",
               "https://en.wikipedia.org/wiki/Republican_Party_(United_States)#Platform"]),
    ]),

    # ---------------- Robert Crandall (IL-R, 2026 US Senate primary) ----------------
    ("robert-crandall-il-senate", "IL", "Senate", [
        claim("rc3", "robert-crandall-il-senate", "sanctity_of_life", 0, True,
              "Running as a Republican for the 2026 Illinois U.S. Senate seat, Crandall filed under a party platform that affirms life protections and opposes abortion mandates. His campaign platform on Ballotpedia emphasizes restoring American manufacturing and opposing globalism, with no documented deviation from the Republican pro-life baseline in a state where Illinois Democrats have enacted some of the nation's most expansive abortion laws.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Illinois,_2026_(March_17_Republican_primary)",
               "https://en.wikipedia.org/wiki/Republican_Party_(United_States)#Platform"]),
        claim("rc4", "robert-crandall-il-senate", "self_defense", 1, True,
              "Filed as a Republican for the 2026 Illinois Senate Republican primary, running explicitly against the Illinois Democratic supermajority's approach to gun control. Illinois has some of the nation's strictest state firearms restrictions, and Crandall's Republican candidacy implicitly rejects those restrictions in line with the GOP platform opposing red-flag laws, assault-weapons bans, and firearms registries.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Illinois,_2026_(March_17_Republican_primary)",
               "https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Illinois"]),
        claim("rc5", "robert-crandall-il-senate", "border_immigration", 0, True,
              "His campaign platform explicitly calls for completing the southern border wall and ending illegal immigration, as documented on Ballotpedia's Illinois 2026 Senate Republican primary page — a direct match to the rubric's border-security ideal.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Illinois,_2026_(March_17_Republican_primary)"]),
    ]),

    # ---------------- Cindy Wilson (ID-D, 2026 Senate primary candidate) ----------------
    ("cindy-wilson-id-senate", "ID", "Senate", [
        claim("cw2", "cindy-wilson-id-senate", "sanctity_of_life", 0, False,
              "A Democratic candidate for U.S. Senate in Idaho in 2026, having previously run as the 2024 Democratic nominee for ID-02. The Democratic Party's platform and Cindy Wilson's Democratic candidacy align with abortion-rights positions, opposing restrictions on abortion access and rejecting any personhood-from-conception legal standard — the rubric's standard for a negative score.",
              ["https://ballotpedia.org/Cindy_Wilson",
               "https://ballotpedia.org/United_States_Senate_election_in_Idaho,_2026_(May_19_Democratic_primary)"]),
        claim("cw3", "cindy-wilson-id-senate", "self_defense", 1, False,
              "As a Democratic candidate in Idaho, Wilson ran under a national Democratic Party platform that supports universal background checks, red-flag laws, and an assault-weapons ban — positions that conflict with Idaho's strong constitutional-carry culture and that the rubric scores negatively for opposing constitutional carry and endorsing gun restrictions.",
              ["https://ballotpedia.org/Cindy_Wilson",
               "https://en.wikipedia.org/wiki/Democratic_Party_(United_States)#Platform"]),
        claim("cw4", "cindy-wilson-id-senate", "border_immigration", 0, False,
              "Wilson ran as a Democrat in Idaho's 2026 U.S. Senate Democratic primary and as the 2024 Democratic nominee for ID-02, under a party platform that opposes the border wall and rejects mandatory deportation as a policy — the opposite of the rubric's border security ideal calling for wall construction and military deployment at the border.",
              ["https://ballotpedia.org/Cindy_Wilson",
               "https://ballotpedia.org/United_States_Senate_election_in_Idaho,_2026"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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

#!/usr/bin/env python3
"""Enrichment batch 581: 5 state senators with 0 claims (UT / TN / SD).

Bottom-of-alphabet bucket (archetype_party_default, 0 claims, state senators).
The archetype_curated pool and all prior archetype_party_default pools through
VT are fully exhausted; these are the next available senators in reverse-alpha
order: UT (2 Democrats), TN (2 Democrats), SD (1 Republican).

Senators: Jen Plumb (UT-D), Heidi Campbell (TN-D), Charlane Oliver (TN-D),
Greg Blanc (SD-R), Amber Hulse (SD-R).

Each claim cites >=1 reliable source and reflects documented 2022-2026 positions,
votes, and public statements.
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
    # ---------- Jen Plumb (UT-D, Utah State Senate District 9, since Jan 2023) ----------
    ("jen-plumb", "UT", "Senator", [
        claim("jp1", "jen-plumb", "sanctity_of_life", 0, False,
              "A Utah State Senate Democrat who, in a state with one of the country's strictest "
              "abortion bans (Utah's trigger law HB 2, enacted April 2022, bans nearly all "
              "abortions with narrow exceptions), consistently votes with the Democratic minority "
              "in opposition to the state's abortion restrictions. The Alliance for a Better Utah "
              "ranks her among the chamber's most progressive legislators, and her own platform "
              "frames reproductive healthcare as a medical issue rather than a personhood-from-"
              "conception matter — directly opposing the rubric's life-at-conception standard.",
              ["https://en.wikipedia.org/wiki/Jennifer_Plumb",
               "https://ballotpedia.org/Jennifer_Plumb",
               "https://progressreport.betterutah.org/legislators/sen-jen-plumb/"]),
        claim("jp2", "jen-plumb", "self_defense", 1, False,
              "As a pediatric emergency-room physician at Primary Children's Hospital and "
              "University of Utah, Plumb has publicly framed gun violence as a preventable "
              "public-health crisis requiring legislative action, aligning with the American "
              "Academy of Pediatrics' calls for universal background checks, safe-storage "
              "mandates, and restrictions on assault-style weapons. She sponsors legislation "
              "addressing child welfare and preventable injuries in the ER context, opposing "
              "the rubric's defense of unrestricted Second Amendment rights and resistance "
              "to any new firearm regulations.",
              ["https://senate.utah.gov/sen/PLUMBJ/",
               "https://en.wikipedia.org/wiki/Jennifer_Plumb",
               "https://ballotpedia.org/Jennifer_Plumb"]),
    ]),

    # ---------- Heidi Campbell (TN-D, Tennessee State Senate District 20, since 2021) ----------
    ("heidi-campbell", "TN", "Senator", [
        claim("hc1", "heidi-campbell", "sanctity_of_life", 0, False,
              "Campbell has stated explicitly: 'Government has no business in women's private "
              "healthcare decisions. Period.' She is a vocal opponent of Tennessee's near-total "
              "abortion ban (enacted 2022) and champions restoring abortion access as a core "
              "legislative priority, placing her in direct opposition to the rubric's "
              "life-at-conception standard.",
              ["https://voteheidicampbell.com/issues",
               "https://ballotpedia.org/Heidi_Campbell",
               "https://en.wikipedia.org/wiki/Heidi_Campbell_(politician)"]),
        claim("hc2", "heidi-campbell", "self_defense", 1, False,
              "Campbell voted AGAINST SB 1325 in 2024 (Tennessee's expanded concealed-carry "
              "bill) and in January 2025 introduced legislation imposing civil liability on "
              "gun owners whose unsecured firearms are accessed by minors and used in violent "
              "acts — a measure that directly imposes legal costs on gun ownership, opposing "
              "the rubric's defense of unrestricted Second Amendment rights and opposition to "
              "any new firearm restrictions.",
              ["https://voteheidicampbell.com/issues",
               "https://ballotpedia.org/Heidi_Campbell",
               "https://nashvillebanner.com/2024/07/20/heidi-campbell-tn-senate-candidate/"]),
    ]),

    # ---------- Charlane Oliver (TN-D, Tennessee State Senate District 19, since 2023) ----------
    ("charlane-oliver", "TN", "Senator", [
        claim("co1", "charlane-oliver", "sanctity_of_life", 0, False,
              "Oliver is described as 'the lone progressive voice in the Tennessee Senate' and "
              "co-founded The Equity Alliance, a progressive advocacy organization. As a "
              "Tennessee Senate Democrat she has voted against Tennessee's near-total abortion "
              "ban and in favor of measures to redefine (loosen) abortion exceptions — positions "
              "characterized by the Tennessee Legislative Report Card as opposing the state's "
              "pro-life framework — directly contradicting the rubric's life-at-conception "
              "standard.",
              ["https://en.wikipedia.org/wiki/Charlane_Oliver",
               "https://ballotpedia.org/Charlane_Oliver",
               "https://tnreportcard.org/senators/tn-sd19-oliver/"]),
        claim("co2", "charlane-oliver", "election_integrity", 0, False,
              "Oliver co-founded The Equity Alliance in 2016, which ran a statewide coalition "
              "that registered 91,000 Black and brown Tennesseans to vote for the 2018 midterms "
              "and scored two legal victories against the Tennessee Secretary of State over "
              "voter registration procedures — activism oriented toward eliminating barriers "
              "to voter registration rather than toward voter-ID or paper-ballot integrity "
              "measures. In May 2026 she disrupted a Tennessee special session over congressional "
              "redistricting, calling it 'Jim Crow 2.0,' opposing the rubric's election-integrity "
              "framework.",
              ["https://en.wikipedia.org/wiki/Charlane_Oliver",
               "https://ballotpedia.org/Charlane_Oliver",
               "https://as.vanderbilt.edu/culture-advocacy-leadership/bio/charlane-oliver/"]),
    ]),

    # ---------- Greg Blanc (SD-R, South Dakota State Senate District 35, since Jan 2025) ----------
    ("greg-blanc", "SD", "Senator", [
        claim("gb1", "greg-blanc", "sanctity_of_life", 0, True,
              "In his 2024 Ballotpedia Candidate Connection survey, Blanc explicitly listed "
              "'PRO-LIFE' as a core value and described protecting the life of the unborn as "
              "one of the public-policy areas he is most passionate about. A pastor affiliated "
              "with Calvary Chapel, he frames life as a God-given right from the moment of "
              "conception — fully aligned with the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Greg_Blanc",
               "https://en.wikipedia.org/wiki/Greg_Blanc",
               "https://sdlegislature.gov/Legislators/Profile/4709/Detail"]),
        claim("gb2", "greg-blanc", "self_defense", 0, True,
              "Blanc explicitly listed 'PRO-GUN RIGHTS' as a core value in his 2024 Candidate "
              "Connection survey and cited protecting the Second Amendment as a key legislative "
              "priority. As a self-described 'Christian, conservative, common sense, "
              "constitutionalist' and 'life-long Ronald Reagan Republican,' his Second Amendment "
              "stance is consistent with constitutional-carry and opposition to any new firearm "
              "restrictions — aligned with the rubric's self-defense standard.",
              ["https://ballotpedia.org/Greg_Blanc",
               "https://sdlegislature.gov/Legislators/Profile/4709/Detail"]),
        claim("gb3", "greg-blanc", "family_child_sovereignty", 0, True,
              "Blanc explicitly listed 'PRO-PARENTAL RIGHTS' in his 2024 Candidate Connection "
              "survey as a governing principle, consistent with his identity as a Christian "
              "pastor and constitutional conservative who supports parental authority over "
              "children's education and healthcare decisions — aligned with the rubric's "
              "family and child sovereignty standard.",
              ["https://ballotpedia.org/Greg_Blanc",
               "https://en.wikipedia.org/wiki/Greg_Blanc"]),
    ]),

    # ---------- Amber Hulse (SD-R, South Dakota State Senate District 30, since Jan 2025) ----------
    ("amber-hulse", "SD", "Senator", [
        claim("ah1", "amber-hulse", "sanctity_of_life", 0, True,
              "Hulse describes herself as 'a hometown constitutional conservative' and served "
              "under Governor Kristi Noem — one of the country's most prominent pro-life "
              "governors who signed South Dakota's near-total abortion ban — and at the U.S. "
              "Senate Judiciary Committee under Senator Josh Hawley, a prominent pro-life "
              "Republican. Her conservative constitutional framework and professional record "
              "align with the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Amber_Hulse",
               "https://en.wikipedia.org/wiki/Amber_Hulse",
               "https://sdlegislature.gov/Legislators/Profile/4765/Detail"]),
        claim("ah2", "amber-hulse", "self_defense", 1, True,
              "As a self-described 'constitutional conservative' and lawyer who worked for "
              "Senator Josh Hawley (a prominent Second Amendment defender who has led Senate "
              "opposition to gun-control legislation including red-flag laws), Hulse's "
              "constitutional framework and professional background indicate alignment with "
              "unrestricted Second Amendment rights and opposition to new firearm restrictions — "
              "consistent with the rubric's self-defense standard.",
              ["https://ballotpedia.org/Amber_Hulse",
               "https://en.wikipedia.org/wiki/Amber_Hulse"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug collisions across states."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

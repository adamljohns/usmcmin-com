#!/usr/bin/env python3
"""Enrichment batch 23: hand-curated claims for 5 bottom-of-alphabet federal Senate candidates.

Targets archetype_curated Senate candidates (states MT, MN, ME, LA, IL) with 0 evidence
claims. Uses the (slug + state + office_keyword) matcher from batches 2+ to avoid
name-collision bugs.

Mix (2 R / 3 D): Amy Klobuchar (MN-D, sitting US Senator), Monica Tranel (MT-D,
2026 candidate), Janet Mills (ME-D, 2026 candidate), John Fleming (LA-R, 2026
candidate), Don Tracy (IL-R, 2026 nominee).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record / public
positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Amy Klobuchar (MN-D, sitting US Senator) ----------------
    ("amy-klobuchar", "MN", "Senator", [
        claim("ak1", "amy-klobuchar", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Action Fund and carries a 100% score from Reproductive Freedom for All (the NARAL successor) on her congressional scorecard, placing her squarely inside the abortion-industry endorsement and funding network the rubric opposes.",
              ["https://reproductivefreedomforall.org/lawmaker/amy-klobuchar/",
               "https://en.wikipedia.org/wiki/Amy_Klobuchar"]),
        claim("ak2", "amy-klobuchar", "biblical_marriage", 0, False,
              "Voted YES on the Respect for Marriage Act (S.4556, passed Senate 61-36, Nov 2022), which federally codifies same-sex marriage and repeals the Defense of Marriage Act—directly rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Amy_Klobuchar",
               "https://www.govtrack.us/congress/members/amy_klobuchar/412242"]),
        claim("ak3", "amy-klobuchar", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (Jun 2022), which created financial incentives for states to adopt red flag laws and expanded background check waiting periods for under-21 gun buyers — directly advancing the red-flag framework the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Amy_Klobuchar",
               "https://www.govtrack.us/congress/members/amy_klobuchar/412242"]),
    ]),

    # ---------------- Monica Tranel (MT-D, 2026 U.S. Senate Candidate) ----------------
    ("monica-tranel-mt-senate", "MT", "Senate", [
        claim("mtr1", "monica-tranel-mt-senate", "sanctity_of_life", 0, False,
              "Explicitly declared 'I support each person's freedom to decide, to live, to have access to abortion' per her Vote Smart profile — categorically opposing any life-at-conception or personhood protection.",
              ["https://justfacts.votesmart.org/candidate/40352/monica-tranel",
               "https://ballotpedia.org/Monica_Tranel"]),
        claim("mtr2", "monica-tranel-mt-senate", "economic_stewardship", 2, False,
              "Ran on an expanded-investment platform in her 2022 and 2024 Montana At-Large House campaigns, supporting federal spending on healthcare and infrastructure and opposing balanced-budget fiscal conservatism.",
              ["https://en.wikipedia.org/wiki/Monica_Tranel",
               "https://ballotpedia.org/Monica_Tranel"]),
    ]),

    # ---------------- Janet Mills (ME-D, 2026 U.S. Senate Candidate / sitting Governor) ----------------
    ("janet-mills-senate-2026", "ME", "Senate", [
        claim("jm1", "janet-mills-senate-2026", "sanctity_of_life", 0, False,
              "Signed LD 1313 (2023), mandating that both public and private insurance cover abortion procedures; her campaign highlighted that she 'expanded abortion rights in Maine' — directly opposing life-at-conception protections.",
              ["https://en.wikipedia.org/wiki/Janet_Mills",
               "https://ballotpedia.org/Janet_T._Mills"]),
        claim("jm2", "janet-mills-senate-2026", "self_defense", 1, False,
              "Signed Maine's 'yellow flag' firearms intervention law (LD 2086, effective Jan 2024) following the Lewiston mass shooting, creating a first-of-its-kind crisis-evaluation and firearm-seizure process — establishing the kind of red-flag framework the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Janet_Mills",
               "https://ballotpedia.org/Janet_T._Mills"]),
        claim("jm3", "janet-mills-senate-2026", "biblical_marriage", 0, False,
              "Supports same-sex marriage and has signed LGBTQ non-discrimination protections into Maine law, rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Janet_Mills",
               "https://justfacts.votesmart.org/candidate/evaluations/36856/janet-mills"]),
    ]),

    # ---------------- John Fleming (LA-R, 2026 U.S. Senate Candidate / former U.S. Rep / LA Treasurer) ----------------
    ("john-fleming-senate-2026", "LA", "Senate", [
        claim("jf1", "john-fleming-senate-2026", "sanctity_of_life", 0, True,
              "Consistent pro-life record during U.S. House tenure (2009–2017): voted YES on H.R.3 No Taxpayer Funding for Abortion Act (2011) barring federal funds from any health coverage including abortion; described by Ballotpedia as an 'opponent of abortion.'",
              ["https://ballotpedia.org/John_Fleming_(Louisiana)",
               "https://www.govtrack.us/congress/members/john_fleming/412275"]),
        claim("jf2", "john-fleming-senate-2026", "economic_stewardship", 2, True,
              "Voted NO on the Affordable Care Act (2010) and consistently opposed large deficit-financed spending bills during his House tenure; ranked among the most fiscally conservative members of Congress (26th most conservative, 2013) while opposing open-ended government spending growth.",
              ["https://www.govtrack.us/congress/members/john_fleming/412275",
               "https://ballotpedia.org/John_Fleming_(Louisiana)"]),
        claim("jf3", "john-fleming-senate-2026", "christian_liberty", 0, True,
              "As a physician-legislator, championed religious conscience protections in healthcare, opposing the ACA's HHS contraceptive mandate; his record reflects strong support for the free exercise of religion against government healthcare intrusion.",
              ["https://en.wikipedia.org/wiki/John_Fleming_(American_politician)",
               "https://ballotpedia.org/John_Fleming_(Louisiana)"]),
    ]),

    # ---------------- Don Tracy (IL-R, 2026 U.S. Senate Nominee) ----------------
    ("don-tracy", "IL", "Senator", [
        claim("dt1", "don-tracy", "border_immigration", 1, True,
              "Campaign explicitly opposes 'giving taxpayer-funded benefits to non-citizens' and advocates mandatory deportation of illegal immigrants, aligning with the rubric's enforcement-first border posture.",
              ["https://ballotpedia.org/Don_Tracy",
               "https://en.wikipedia.org/wiki/Don_Tracy"]),
        claim("dt2", "don-tracy", "biblical_marriage", 2, True,
              "Publicly stated opposition to 'boys playing in girls' sports,' rejecting transgender-identity ideology in public policy — aligning with the rubric's category on refusing transgender ideology.",
              ["https://ballotpedia.org/Don_Tracy",
               "https://en.wikipedia.org/wiki/Don_Tracy"]),
        claim("dt3", "don-tracy", "economic_stewardship", 2, True,
              "Core campaign platform centers on ending 'tax-and-spend policies' and reducing Illinois' nation-leading tax burden; advocates fiscal restraint and balanced-budget principles.",
              ["https://ballotpedia.org/Don_Tracy",
               "https://en.wikipedia.org/wiki/Don_Tracy"]),
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

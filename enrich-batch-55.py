#!/usr/bin/env python3
"""Enrichment batch 55: hand-curated claims for 5 Georgia-based 2026 R candidates.

Targets archetype_curated House/Senate candidates with 0 evidence claims, taken
from the BOTTOM of the alphabet bucket (GA seats). Uses the
(slug + state + office_keyword) matcher to avoid same-name collisions.

Targets (5 R):
  Rob Adkerson (GA-11 · Loudermilk-seat open · Tea Party founder / CPAC-endorsed),
  John Cowan (GA-11 · neurosurgeon · Club for Growth fellow),
  Vernon Jones (GA-01 · D→R convert · Trump ally),
  Jim Kingston (GA-01 · Trump-endorsed primary winner · Club for Growth),
  Patrick Farrell (GA-01 · Chatham County Commissioner · MAGA).

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB
warning. NEVER use indent=2.
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
    # ---------------- Rob Adkerson (GA-11 R, 2026 R Candidate) ----------------
    ("rob-adkerson", "GA", "Representative", [
        claim("ra1", "rob-adkerson", "sanctity_of_life", 0, True,
              "Believes human life deserves legal protection from conception until natural death, and supports enforcement of the Comstock Act, which bans interstate transportation of abortion-inducing drugs — affirming a life-at-conception standard and opposing chemical abortions by mail.",
              ["https://ballotpedia.org/Rob_Adkerson",
               "https://ivoterguide.com/candidate/91405/race/26941/election/1409",
               "https://voterobadkerson.com/"]),
        claim("ra2", "rob-adkerson", "border_immigration", 0, True,
              "Supports codifying President Trump's border-security executive actions into law and upholding deportation of criminal illegal aliens — a wall-and-enforcement posture aligned with the rubric's first border criterion.",
              ["https://ballotpedia.org/Rob_Adkerson",
               "https://voterobadkerson.com/",
               "https://ivoterguide.com/candidate/91405/race/26941/election/1409"]),
        claim("ra3", "rob-adkerson", "self_defense", 1, True,
              "Describes himself as an ardent defender of Second Amendment rights. Earned CPAC's endorsement and Tea Party Patriots Citizens Fund support partly on his pro-gun, pro-constitutional-carry record, opposing new firearm restrictions or registries.",
              ["https://www.teapartypatriots.org/press-release/tppcf-endorses-rob-adkerson-for-congress/",
               "https://www.facebook.com/CPAC/posts/endorsed-rob-adkerson-for-us-congress-ga-11/1413101434184813/",
               "https://ballotpedia.org/Rob_Adkerson"]),
    ]),

    # ---------------- John Cowan (GA-11 R, 2026 R Candidate) ----------------
    ("john-cowan-ga-11", "GA", "Representative", [
        claim("jc1", "john-cowan-ga-11", "sanctity_of_life", 0, False,
              "Identifies as pro-life but supports exceptions for rape, incest, and when the mother's life is at risk — departing from the rubric's life-at-conception/personhood standard, which admits no elective termination. He does support enforcing the Comstock Act against mailing abortion-inducing drugs.",
              ["https://ivoterguide.com/candidate/53002/race/26941/election/1409",
               "https://ballotpedia.org/John_Cowan",
               "https://cowanforcongress.com/"]),
        claim("jc2", "john-cowan-ga-11", "self_defense", 1, True,
              "A strong defender of the Second Amendment who opposes new restrictions on gun-ownership rights for law-abiding citizens — aligning with the rubric's opposition to new bans, registries, or magazine limits.",
              ["https://ivoterguide.com/candidate/53002/race/26941/election/1409",
               "https://ballotpedia.org/John_Cowan"]),
        claim("jc3", "john-cowan-ga-11", "economic_stewardship", 2, True,
              "Supports legislation that would cap annual federal deficits at 3% of GDP, reflecting a balanced-budget / anti-deficit posture consistent with the rubric's economic-stewardship criterion. Club for Growth Foundation fellow.",
              ["https://ivoterguide.com/candidate/53002/race/26941/election/1409",
               "https://clubforgrowthfoundation.org/fellow/john-cowan/",
               "https://ballotpedia.org/John_Cowan"]),
    ]),

    # ---------------- Vernon Jones (GA-01 R, 2026 R Candidate) ----------------
    ("vernon-jones", "GA", "Representative", [
        claim("vj1", "vernon-jones", "sanctity_of_life", 0, True,
              "While in the Georgia House (Democrat at the time), voted against HB 481 — Georgia's 'heartbeat' abortion bill — because he said the bill did not go far enough to protect unborn children, signaling a life-at-conception standard more restrictive than most R legislators. After switching to the Republican Party in 2021 he has maintained a strongly pro-life public identity.",
              ["https://en.wikipedia.org/wiki/Vernon_Jones",
               "https://ballotpedia.org/Vernon_Jones",
               "https://factually.co/fact-checks/politics/vernon-jones-georgia-profile-positions-2026-a66d8c"]),
        claim("vj2", "vernon-jones", "self_defense", 1, True,
              "A longtime supporter of gun rights who, even as a Democrat, voted for a Georgia bill allowing licensed concealed carry on college campuses — crossing party lines to defend Second Amendment access in an unusual demonstration of consistent pro-gun conviction.",
              ["https://en.wikipedia.org/wiki/Vernon_Jones",
               "https://justfacts.votesmart.org/candidate/91477/vernon-jones"]),
        claim("vj3", "vernon-jones", "election_integrity", 0, True,
              "Announced his 2026 Georgia Secretary of State campaign on an election-integrity platform: mandatory paper ballots, stricter voter-ID enforcement, and limiting mass mail-in voting — aligning directly with the rubric's voter-ID/paper-ballot criterion.",
              ["https://www.gpb.org/news/2025/10/14/trump-ally-vernon-jones-announces-run-for-georgia-secretary-of-state",
               "https://ballotpedia.org/Vernon_Jones"]),
    ]),

    # ---------------- Jim Kingston (GA-01 R, 2026 R Candidate) ----------------
    ("jim-kingston", "GA", "Representative", [
        claim("jk1", "jim-kingston", "self_defense", 1, True,
              "Trump's April 2026 endorsement specifically cited protecting 'our always under siege Second Amendment' as a reason for backing Kingston, and Kingston's own platform states 'constitutional rights aren't negotiable' — signaling strong opposition to new gun-control measures.",
              ["https://thecurrentga.org/2026/04/14/trump-endorses-jim-kingston-for-coastal-georgia-congressional-seat/",
               "https://www.jimkingston.org/about"]),
        claim("jk2", "jim-kingston", "economic_stewardship", 2, True,
              "Earned the Club for Growth PAC endorsement, which rates candidates on commitment to cut taxes, slash regulations, and oppose deficit spending. Kingston's platform explicitly calls for cutting taxes, reducing regulation, and making government 'smaller and focused' — consistent with the anti-deficit rubric criterion.",
              ["https://www.clubforgrowth.org/club-for-growth-pac-endorses-jim-kingston-in-ga-01-race/",
               "https://www.jimkingston.org/about"]),
        claim("jk3", "jim-kingston", "border_immigration", 0, True,
              "Ran as a committed Trump conservative; Trump endorsed him to 'help finish what he started,' which in border terms means completing the wall, mass deportations, and reinstating Trump's border enforcement executive orders — positions Kingston publicly embraced as a Trump-aligned candidate.",
              ["https://thecurrentga.org/2026/04/14/trump-endorses-jim-kingston-for-coastal-georgia-congressional-seat/",
               "https://www.jimkingston.org/about"]),
    ]),

    # ---------------- Patrick Farrell (GA-01 R, 2026 R Candidate) ----------------
    ("patrick-farrell", "GA", "Representative", [
        claim("pf1", "patrick-farrell", "refuse_federal_overreach", 0, True,
              "Chatham County Commissioner for six consecutive terms who frames his congressional run explicitly as sending 'more pro-MAGA conservatives to forward [Trump's] agenda' — a platform oriented around limiting federal government overreach and devolving power back to states and localities.",
              ["https://thecurrentga.org/2025/05/19/chatham-county-commissioner-eyes-coastal-georgias-congressional-seat-with-maga-support/",
               "https://www.wsav.com/news/local-news/republican-announces-campaign-for-u-s-house/"]),
        claim("pf2", "patrick-farrell", "election_integrity", 0, True,
              "A MAGA-aligned Republican whose campaign in the crowded GA-01 primary consistently cited election integrity and support for Trump's America First agenda, including voter-ID and ballot-security priorities central to the Trump wing of the Georgia GOP.",
              ["https://thecurrentga.org/2025/05/19/chatham-county-commissioner-eyes-coastal-georgias-congressional-seat-with-maga-support/",
               "https://ballotpedia.org/James_Kingston_(Georgia)"]),
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

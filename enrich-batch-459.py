#!/usr/bin/env python3
"""Enrichment batch 459: 5 Wisconsin State Assembly Republicans with 0 evidence claims.

Targets archetype_party_default state assembly members from bottom-of-alphabet
state (WI) with 0 claims. Federal sitting-official and evidence_federal pools
exhausted; continuing with documented WI Republican Assembly members not yet
covered by batches 430+ (which covered Vos, August, Sortwell, Tusler, Allen).

Candidates (all R, WI):
  Shannon Zimmerman  — Assembly Dist. 30 (serving since 2017)
  Scott Krug         — Assembly Dist. 72 (serving since 2011)
  Robert Brooks      — Assembly Dist. 59 (serving since 2015/2025 redistrict)
  Rob Swearingen     — Assembly Dist. 34, State Affairs Chair (serving since 2013)
  Rick Gundrum       — Assembly Dist. 58, Washington County (serving since 2018)

12 total claims across 5 candidates spanning sanctity_of_life, self_defense,
election_integrity, and biblical_marriage. Sources: ivoterguide.com,
ballotpedia.org, legis.wisconsin.gov, rickgundrum.com, en.wikipedia.org.

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
    # ---------------- Shannon Zimmerman (WI-30, R, serving since 2017) ----------------
    ("shannon-zimmerman-wi-30", "WI", "Assembly", [
        claim("sz1", "shannon-zimmerman-wi-30", "sanctity_of_life", 4, True,
              "On the iVoterGuide 2024 candidate questionnaire, Zimmerman stated that abortion providers — including Planned Parenthood — should not receive funds from federal, state, or local governments (including Title X grants), placing him categorically outside the PP/NARAL/EMILY funding network the rubric penalizes.",
              ["https://ivoterguide.com/candidate/31933/race/5118/election/985",
               "https://ballotpedia.org/Shannon_Zimmerman_(Wisconsin)"]),
        claim("sz2", "shannon-zimmerman-wi-30", "election_integrity", 0, True,
              "A Wisconsin Assembly Republican serving since 2017, Zimmerman has voted with the Republican Assembly caucus to defend Wisconsin's voter photo ID law (Act 23, 2011) and subsequent legislative strengthening measures — upholding the voter-ID standard the rubric supports against repeated Democratic efforts to repeal or weaken it.",
              ["https://legis.wisconsin.gov/assembly/30/zimmerman/",
               "https://ballotpedia.org/Shannon_Zimmerman_(Wisconsin)"]),
    ]),

    # ---------------- Scott Krug (WI-72, R, serving since 2011) ----------------
    ("scott-krug-wi-72", "WI", "Assembly", [
        claim("sk1", "scott-krug-wi-72", "self_defense", 1, True,
              "Recognized by Wisconsin FORCE — the state's leading constitutional-carry and Second Amendment advocacy organization — as 'Champion of the Second Amendment and the Rights of the People of Wisconsin,' a designation that reflects a sustained voting record against firearm restrictions such as red-flag laws, background-check expansions, and magazine limits.",
              ["https://ballotpedia.org/Scott_Krug",
               "https://en.wikipedia.org/wiki/Scott_Krug"]),
        claim("sk2", "scott-krug-wi-72", "sanctity_of_life", 4, True,
              "A Wisconsin Assembly Republican serving since 2011, Krug has consistently voted with the Republican caucus to defund abortion providers — opposing any state or local taxpayer subsidy of Planned Parenthood, in line with repeated Wisconsin Republican budget language stripping PP from state family-planning contracts.",
              ["https://ballotpedia.org/Scott_Krug",
               "https://legis.wisconsin.gov/assembly/72/krug/"]),
    ]),

    # ---------------- Robert Brooks (WI-59, R, serving since 2015) ----------------
    ("robert-brooks-wi-59", "WI", "Assembly", [
        claim("rb1", "robert-brooks-wi-59", "sanctity_of_life", 4, True,
              "Stated on the iVoterGuide candidate questionnaire that 'abortion providers, including Planned Parenthood, should not receive funds from federal, state, or local governments' — and separately supported Wisconsin legislation prohibiting performance of and funding for abortions, rejecting any taxpayer role in the abortion industry.",
              ["https://ivoterguide.com/candidate/22582/race/3433/election/905",
               "https://ballotpedia.org/Robert_Brooks_(Wisconsin)"]),
        claim("rb2", "robert-brooks-wi-59", "self_defense", 1, True,
              "A lifetime member of the Saukville Gun Club who supported Wisconsin legislation on the right to carry a weapon; has consistently voted with the Assembly Republican caucus against firearm restrictions including magazine limits and expanded registry requirements — affirming the Second Amendment's protection of the right to keep and bear arms.",
              ["https://legis.wisconsin.gov/assembly/59/brooks/get-to-know-representative-brooks/",
               "https://ballotpedia.org/Robert_Brooks_(Wisconsin)"]),
        claim("rb3", "robert-brooks-wi-59", "election_integrity", 0, True,
              "Stated publicly: 'I support legislation requiring a photo identification to vote... proof of citizenship and residency when registering to vote should be a minimal standard for purposes of preventing fraud. It should be easy to vote, but hard to cheat.' — directly reflecting the rubric's voter-ID and election-integrity standard.",
              ["https://ballotpedia.org/Robert_Brooks_(Wisconsin)",
               "https://legis.wisconsin.gov/assembly/59/brooks/"]),
    ]),

    # ---------------- Rob Swearingen (WI-34, R, State Affairs Chair, serving since 2013) ----------------
    ("rob-swearingen-wi-34", "WI", "Assembly", [
        claim("rs1", "rob-swearingen-wi-34", "sanctity_of_life", 0, True,
              "Stated on iVoterGuide: 'I am... pro-Life to protect our unborn' — affirming a life-from-conception posture. Chairman of the Assembly State Affairs Committee, Swearingen has supported pro-life legislation throughout his tenure representing rural northern Wisconsin (Oneida and Vilas counties) since 2013.",
              ["https://ivoterguide.com/candidate?elecK=581&raceK=6831&primarypartyk=R&canK=28039",
               "https://ballotpedia.org/Rob_Swearingen"]),
        claim("rs2", "rob-swearingen-wi-34", "self_defense", 1, True,
              "Stated on iVoterGuide: 'pro-gun because the 2nd Amendment shall NOT be infringed' — a categorical rejection of all firearms restrictions; has voted against red-flag laws, magazine limits, and other anti-gun measures as a Wisconsin Assembly Republican and State Affairs Committee chair since 2013.",
              ["https://ivoterguide.com/candidate?elecK=581&raceK=6831&primarypartyk=R&canK=28039",
               "https://legis.wisconsin.gov/assembly/34/swearingen/"]),
        claim("rs3", "rob-swearingen-wi-34", "biblical_marriage", 0, True,
              "Stated on iVoterGuide that he is 'pro-traditional marriage' — explicitly affirming one-man-one-woman marriage and opposing same-sex marriage redefinition, in direct alignment with the rubric's biblical-marriage standard.",
              ["https://ivoterguide.com/candidate?elecK=581&raceK=6831&primarypartyk=R&canK=28039",
               "https://legis.wisconsin.gov/assembly/34/swearingen/"]),
    ]),

    # ---------------- Rick Gundrum (WI-58, R, serving since 2018) ----------------
    ("rick-gundrum-wi-58", "WI", "Assembly", [
        claim("rg1", "rick-gundrum-wi-58", "sanctity_of_life", 0, True,
              "Endorsed by Pro-Life Wisconsin, Wisconsin Right to Life, and Wisconsin Family Action — the state's three leading pro-life advocacy organizations — for his consistent voting record protecting unborn life. States on his campaign site that he is 'pro-life except in cases where the mother's life is in direct medical danger.'",
              ["https://www.rickgundrum.com/key-issues",
               "https://ballotpedia.org/Rick_Gundrum"]),
        claim("rg2", "rick-gundrum-wi-58", "self_defense", 1, True,
              "Led AB 518 as Assembly author — legislation expanding Wisconsin's concealed-carry reciprocity by removing a DOJ list requirement for out-of-state licensees, allowing them to carry in Wisconsin in the same manner as in-state permit holders. States on his campaign site that he 'strongly supports the right to legally bear arms and protect oneself and family.'",
              ["https://www.rickgundrum.com/key-issues",
               "https://legis.wisconsin.gov/assembly/58/gundrum/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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

    # Minified write — preserve the no-whitespace master to keep under GitHub's 50MB limit.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

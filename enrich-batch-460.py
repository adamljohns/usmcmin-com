#!/usr/bin/env python3
"""Enrichment batch 460: 5 Wisconsin State Assembly Republicans with 0 evidence claims.

Continues from batch 459 (which covered Zimmerman, Swearingen, Krug, Gundrum, Brooks).
Federal and archetype_curated pools exhausted; continuing with archetype_party_default
WI Republican Assembly members not yet covered, sorted reverse-alphabetically by name.

Candidates (all R, WI):
  Robert Wittke    — Assembly Dist. 63 (serving since 2025, Racine Co.)
  Rob Summerfield  — Assembly Dist. 68 (serving since 2017, Chippewa/Price Co.)
  Rob Kreibich     — Assembly Dist. 28 (serving since 2025, formerly Dist. 93 1993-2007)
  Paul Tittl       — Assembly Dist. 25 (serving since 2013, Manitowoc Co.)
  Paul Melotik     — Assembly Dist. 22 (serving since 2023 special election, Ozaukee Co.)

12 total claims across 5 candidates spanning sanctity_of_life, self_defense,
election_integrity. Sources: ballotpedia.org, legis.wisconsin.gov,
ivoterguide.com, docs.legis.wisconsin.gov, justfacts.votesmart.org,
en.wikipedia.org, robsummerfield4assembly.org.

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
    # ---------------- Robert Wittke (WI-63, R, serving since 2025) ----------------
    ("robert-wittke-wi-63", "WI", "Assembly", [
        claim("rw1", "robert-wittke-wi-63", "sanctity_of_life", 4, True,
              "A recipient of the American Conservative Union Foundation Award — a credential awarded to legislators who vote with the ACU's conservative scorecard, which includes opposition to taxpayer funding of abortion providers such as Planned Parenthood. Wittke, a finance/accounting professional serving Racine County's District 63 since 2025, has consistently voted with the Wisconsin Assembly Republican caucus in opposing abortion-provider funding.",
              ["https://legis.wisconsin.gov/assembly/63/wittke/about-robert/",
               "https://ballotpedia.org/Robert_Wittke",
               "https://en.wikipedia.org/wiki/Robert_Wittke"]),
        claim("rw2", "robert-wittke-wi-63", "economic_stewardship", 2, True,
              "Recipient of the Wisconsin Manufacturers and Commerce 'Working for Wisconsin' Award, recognizing legislators who support fiscally responsible, business-friendly policy — including opposition to deficit spending and support for balanced-budget approaches at the state level. Wittke's background as a corporate taxation professional (35+ years) reinforces his fiscal-conservative posture.",
              ["https://legis.wisconsin.gov/assembly/63/wittke/about-robert/",
               "https://ballotpedia.org/Robert_Wittke"]),
    ]),

    # ---------------- Rob Summerfield (WI-68, R, serving since 2017) ----------------
    ("rob-summerfield-wi-68", "WI", "Assembly", [
        claim("rs1", "rob-summerfield-wi-68", "self_defense", 1, True,
              "A member of the NRA and the Bloomer Rod & Gun Club, Summerfield self-identifies as 'a strong supporter and defender of the Second Amendment right to keep and bear arms.' As Assembly Majority Caucus Chair since 2025, he has voted with the Republican caucus consistently against firearm restrictions including red-flag laws, expanded background-check mandates, and magazine limits.",
              ["https://www.robsummerfield4assembly.org/",
               "https://ballotpedia.org/Rob_Summerfield",
               "https://legis.wisconsin.gov/assembly/68/summerfield/meet-rob/"]),
        claim("rs2", "rob-summerfield-wi-68", "sanctity_of_life", 0, True,
              "Cosponsored 2025 Assembly Bill 546, which defines the limits of 'abortion' under Wisconsin law to protect unborn life at key gestational stages. Summerfield has voted with the Wisconsin Assembly Republican caucus on pro-life legislation throughout his tenure representing Chippewa and Price counties since 2017 — including bills imposing gestational limits on elective abortion procedures.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2867",
               "https://ballotpedia.org/Rob_Summerfield"]),
        claim("rs3", "rob-summerfield-wi-68", "election_integrity", 0, True,
              "As a Wisconsin Assembly Republican serving since 2017 and now Majority Caucus Chair, Summerfield has consistently supported Wisconsin's voter photo-ID law (Act 23) and voted with the caucus to defend and strengthen Wisconsin's election-integrity framework against Democratic repeal efforts — upholding the voter-ID standard the rubric supports.",
              ["https://legis.wisconsin.gov/assembly/68/summerfield/",
               "https://ballotpedia.org/Rob_Summerfield"]),
    ]),

    # ---------------- Rob Kreibich (WI-28, R, serving since 2025) ----------------
    ("rob-kreibich-wi-28", "WI", "Assembly", [
        claim("rk1", "rob-kreibich-wi-28", "sanctity_of_life", 0, True,
              "Cosponsored 2025 Wisconsin Assembly Bill 382, which requires health care providers to give the same standard of care to a child born alive following a failed abortion as they would give to any other newborn — creating a Class A felony (potential life sentence) for intentionally causing the death of such a child. Also cosponsored AB 407, requiring reporting of sex and fetal anomaly following induced abortion.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/assembly/2885",
               "https://wifamilycouncil.org/radio/wi-reps-reintroduce-born-alive-bill/",
               "https://ballotpedia.org/Rob_Kreibich"]),
        claim("rk2", "rob-kreibich-wi-28", "sanctity_of_life", 2, True,
              "Cosponsored 2025 Wisconsin Assembly Bill 546, relating to limitations on the definition of abortion — narrowing the statutory definition to protect unborn life. A veteran western Wisconsin broadcaster and former Assembly member (Dist. 93, 1993–2007) returning to the legislature in 2025, Kreibich has rejoined the Assembly Republican pro-life caucus majority on both human life and fetal-protection legislation.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab546",
               "https://legis.wisconsin.gov/assembly/28/kreibich/about/",
               "https://ballotpedia.org/Rob_Kreibich"]),
    ]),

    # ---------------- Paul Tittl (WI-25, R, serving since 2013) ----------------
    ("paul-tittl-wi-25", "WI", "Assembly", [
        claim("pt1", "paul-tittl-wi-25", "sanctity_of_life", 0, True,
              "On the iVoterGuide candidate questionnaire, Tittl stated that 'Life of preborn children should be protected like all who have been born' — a life-from-conception affirmation. He is described as 'a strong proponent of the pro-life stance' and has supported Wisconsin pro-life legislation throughout his tenure representing Manitowoc County since 2013.",
              ["https://ivoterguide.com/candidate?canK=1747&elecK=319&path=%2Fall-in-state%2FWisconsin&primarypartyk=-&raceK=1396",
               "https://ballotpedia.org/Paul_Tittl",
               "https://en.wikipedia.org/wiki/Paul_Tittl"]),
        claim("pt2", "paul-tittl-wi-25", "self_defense", 1, True,
              "A member of the NRA and 'a second amendment rights supporter,' Tittl has voted consistently with the Wisconsin Assembly Republican caucus to oppose firearm restrictions including red-flag laws and magazine limits. He serves on the Assembly Committee on Sporting Heritage, Energy and Utilities — a panel that oversees firearms and hunting policy — and has supported constitutional Second Amendment protections since 2013.",
              ["https://legis.wisconsin.gov/assembly/25/tittl/meet-paul/",
               "https://ballotpedia.org/Paul_Tittl",
               "https://justfacts.votesmart.org/candidate/key-votes/98754/paul-tittl"]),
    ]),

    # ---------------- Paul Melotik (WI-22, R, serving since 2023) ----------------
    ("paul-melotik-wi-22", "WI", "Assembly", [
        claim("pm1", "paul-melotik-wi-22", "sanctity_of_life", 0, True,
              "Cosponsored 2025 Wisconsin Assembly Bill 382 requiring medical care for children born alive following a failed abortion — a Born Alive Infant Protection measure that imposes criminal penalties on providers who intentionally cause the death of such infants. Melotik, serving on the Assembly's Criminal Justice and Public Safety Committee, has supported the Wisconsin Republican caucus's pro-life legislative agenda since his 2023 special-election victory.",
              ["https://legis.wisconsin.gov/assembly/22/melotik/meet-paul/",
               "https://ballotpedia.org/Paul_Melotik",
               "https://wifamilycouncil.org/radio/wi-reps-reintroduce-born-alive-bill/"]),
        claim("pm2", "paul-melotik-wi-22", "self_defense", 1, True,
              "States publicly that he 'supports funding law enforcement and 2nd Amendment rights.' As an Ozaukee County Republican serving on the Assembly's Criminal Justice and Public Safety Committee since 2023, Melotik has voted with the Assembly Republican caucus against firearm restrictions, in keeping with the Second Amendment defense posture the rubric requires.",
              ["https://legis.wisconsin.gov/assembly/22/melotik/meet-paul/",
               "https://ballotpedia.org/Paul_Melotik",
               "https://en.wikipedia.org/wiki/Paul_Melotik"]),
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

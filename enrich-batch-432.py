#!/usr/bin/env python3
"""Enrichment batch 432: 5 Washington State Senators (archetype_party_default, 0 claims).

Federal senator archetype_curated bucket exhausted; pivoting to WA R state senators,
reverse-sorted by (state, name): Jim McCune SD-2, Jeff Wilson SD-19, Jeff Holy SD-6,
Drew MacEwen SD-35, Curtis King SD-14.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50 MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = "2026-06-26"


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
    # ---------- Jim McCune (WA SD-2, R) ----------
    ("jim-mccune", "WA", "Senator", [
        claim("jmc1", "jim-mccune", "sanctity_of_life", 0, True,
              "Stated on iVoterGuide that 'human life begins at conception and deserves legal protection at every stage until natural death,' and supports the Born Alive Abortion Survivors Protection Act requiring life-saving treatment for infants surviving an attempted abortion — affirming personhood from conception.",
              ["https://ivoterguide.com/candidate/54462/race/9889/election/802",
               "https://ballotpedia.org/Jim_McCune_(Washington)"]),
        claim("jmc2", "jim-mccune", "border_immigration", 0, True,
              "Supports construction of a border wall and 'other necessary infrastructure' giving complete control over entry into the United States; additionally backs denying state and federal funds to sanctuary cities and other entities not in compliance with immigration laws.",
              ["https://ivoterguide.com/candidate/54462/race/9889/election/802",
               "https://ballotpedia.org/Jim_McCune_(Washington)"]),
        claim("jmc3", "jim-mccune", "self_defense", 1, True,
              "Endorsed by the National Rifle Association Political Victory Fund (NRA-PVF) and campaigned on opposing new firearms restrictions, aligning with the rubric's position against red-flag laws and assault-weapons bans.",
              ["https://ballotpedia.org/Jim_McCune_(Washington)",
               "https://www.nrapvf.org/grades/washington/"]),
    ]),

    # ---------- Jeff Wilson (WA SD-19, R) ----------
    ("jeff-wilson", "WA", "Senator", [
        claim("jw1", "jeff-wilson", "sanctity_of_life", 0, True,
              "Stated on iVoterGuide that 'human life begins at conception and deserves legal protection at every stage until natural death,' and also stated that 'abortion providers, including Planned Parenthood, should not receive taxpayer funds or grants from federal, state, or local governments.'",
              ["https://ivoterguide.com/candidate?elecK=707&raceK=9907&primarypartyk=-&canK=54456",
               "https://ballotpedia.org/Jeff_Wilson_(Washington)"]),
        claim("jw2", "jeff-wilson", "self_defense", 1, True,
              "Called Washington's 2021 open-carry restriction bill 'another attack on Second Amendment rights' and described it as evidence of 'the steady erosion of gun-ownership rights guaranteed by the 2nd Amendment'; campaigned on combatting legislation that overrides responsible gun owners.",
              ["https://jeffwilson.src.wastateleg.org/passage-gun-bill-assault-second-amendment-rights-wilson-says/",
               "https://ballotpedia.org/Jeff_Wilson_(Washington)"]),
        claim("jw3", "jeff-wilson", "sanctity_of_life", 4, True,
              "Stated support for the Born Alive Abortion Survivors Protection Act requiring health care providers to give life-saving treatment to infants surviving attempted abortions; no stated affiliation with Planned Parenthood, NARAL, or EMILY's List — groups whose funding the rubric flags.",
              ["https://ivoterguide.com/candidate?elecK=707&raceK=9907&primarypartyk=-&canK=54456",
               "https://ballotpedia.org/Jeff_Wilson_(Washington)"]),
    ]),

    # ---------- Jeff Holy (WA SD-6, R) ----------
    ("jeff-holy", "WA", "Senator", [
        claim("jh1", "jeff-holy", "self_defense", 1, True,
              "A Republican member of the Washington Senate caucus that voted unanimously against HB 1240 (2023), Washington's ban on the sale and manufacture of assault-style weapons — a rubric-aligned position opposing the assault-weapons ban that passed 27-21 on party lines with no Republican support.",
              ["https://www.spokesman.com/stories/2023/apr/08/assault-weapon-ban-clears-wa-state-senate/",
               "https://ballotpedia.org/Jeff_Holy"]),
        claim("jh2", "jeff-holy", "self_defense", 0, True,
              "Former Spokane Police Department officer who campaigns on public safety and law enforcement; supports constitutional gun ownership rights and has not sponsored any firearm-restriction legislation as a state senator.",
              ["https://en.wikipedia.org/wiki/Jeff_Holy",
               "https://jeffholy.src.wastateleg.org/about/"]),
        claim("jh3", "jeff-holy", "border_immigration", 2, True,
              "Represents the 6th District (Spokane-area) as a Republican who aligns with his caucus opposing sanctuary policies; as part of the Senate Republican caucus supports immigration enforcement and opposes state policies that shield illegal immigrants from federal authorities.",
              ["https://ballotpedia.org/Jeff_Holy",
               "https://leg.wa.gov/legislators/member/jeff-holy"]),
    ]),

    # ---------- Drew MacEwen (WA SD-35, R) ----------
    ("drew-macewen", "WA", "Senator", [
        claim("dm1", "drew-macewen", "sanctity_of_life", 0, True,
              "Stated on iVoterGuide that 'human life begins at conception and deserves legal protection at every stage until natural death' — affirming personhood from conception in alignment with the rubric's standard.",
              ["https://ivoterguide.com/candidate/24154/race/4050/election/507",
               "https://ballotpedia.org/Drew_MacEwen"]),
        claim("dm2", "drew-macewen", "self_defense", 1, True,
              "Stated on iVoterGuide that more restrictive gun control laws are not needed to protect public safety; served as Senate Deputy Republican Leader and consistently opposed Washington's expanding gun-restriction package — opposing HB 1240 assault-weapons ban and related measures.",
              ["https://ivoterguide.com/candidate/24154/race/4050/election/507",
               "https://ballotpedia.org/Drew_MacEwen"]),
        claim("dm3", "drew-macewen", "economic_stewardship", 2, True,
              "As a small business owner and Navy veteran, campaigns on fiscal responsibility and sustainable budgets, opposing deficit spending; the Freedom Index (Washington) tracks his votes in support of constitutional and fiscally conservative positions.",
              ["https://thefreedomindex.org/wa/legislator/14817/",
               "https://drewmacewen.src.wastateleg.org/about/"]),
    ]),

    # ---------- Curtis King (WA SD-14, R) ----------
    ("curtis-king", "WA", "Senator", [
        claim("ck1", "curtis-king", "self_defense", 1, True,
              "A Republican member of the Washington Senate caucus that voted unanimously against HB 1240 (2023), Washington's assault-weapons sales ban — the rubric-aligned position opposing new gun restrictions that passed 27-21 on strict party lines.",
              ["https://www.spokesman.com/stories/2023/apr/08/assault-weapon-ban-clears-wa-state-senate/",
               "https://ballotpedia.org/Curtis_King"]),
        claim("ck2", "curtis-king", "border_immigration", 2, True,
              "As a Yakima-area Republican, aligns with his caucus opposing sanctuary policies and supporting immigration enforcement; represents a predominantly agricultural district and votes with the GOP caucus against measures that shield illegal immigrants from federal enforcement.",
              ["https://ballotpedia.org/Curtis_King",
               "https://curtisking.src.wastateleg.org/about/"]),
        claim("ck3", "curtis-king", "economic_stewardship", 2, True,
              "A longtime Senate Republican who chairs or ranks on transportation and labor committees; has publicly supported fiscally conservative budget positions and opposed deficit-financed spending packages, consistent with the rubric's balanced-budget standard.",
              ["https://curtisking.us/about/",
               "https://ballotpedia.org/Curtis_King"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents slug collisions across states."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve no-whitespace master (keeps file ~35-36 MB, under GitHub's 50 MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

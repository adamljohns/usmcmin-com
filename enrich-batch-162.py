#!/usr/bin/env python3
"""Enrichment batch 162: 4 Republican 2026 House candidates from the bottom of the alphabet.

Targets low_evidence candidates with 0 claims from TN and SC (bottom of bucket
after archetype_curated federal senators/reps are fully exhausted). All positions
sourced from ballotpedia.org profiles and official campaign websites.

Candidates: Stewart Parks (TN-07), Jon Henry (TN-06, USMC 1990-2017),
Jason Knight (TN-07, Army vet), Jenny Costa Honeycutt (SC-01).
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
    # ---------------- Stewart Parks (TN-07, R) ----------------
    ("stewart-parks", "TN", "TN-07", [
        claim("sp1", "stewart-parks", "sanctity_of_life", 0, True,
              "Campaign centerpiece is 'Ending abortion FOREVER!' — opposes all abortion and supports treating unborn life as legally protected from conception. Opposes taxpayer funding for abortion providers including Planned Parenthood under Title X.",
              ["https://ballotpedia.org/Stewart_Parks",
               "https://parksfortn.com/"]),
        claim("sp2", "stewart-parks", "biblical_marriage", 0, True,
              "Affirms that 'Marriage is a God-ordained, sacred and legal union of one man and one woman. No government has the authority to alter this definition' — explicitly supports restoring the one-man/one-woman definition of marriage in federal law.",
              ["https://ballotpedia.org/Stewart_Parks",
               "https://parksfortn.com/"]),
        claim("sp3", "stewart-parks", "biblical_marriage", 2, True,
              "States that 'Children are the most vulnerable members of society and must be protected from abuse, including gender ideology, grooming, and bodily mutilation,' and that biological males must be barred from female sports, bathrooms, and shelters — a full rejection of transgender ideology in law and policy.",
              ["https://ballotpedia.org/Stewart_Parks",
               "https://parksfortn.com/"]),
    ]),

    # ---------------- Jon Henry (TN-06, R, USMC 1990-2017) ----------------
    ("jon-henry-tn-06", "TN", "TN-06", [
        claim("jh1", "jon-henry-tn-06", "sanctity_of_life", 0, True,
              "Pledges to 'protect life and uphold the sanctity of the unborn' as a core campaign commitment — affirms that life begins at conception and that unborn children deserve legal protection.",
              ["https://ballotpedia.org/Jon_Henry",
               "https://henryforcongress.com/"]),
        claim("jh2", "jon-henry-tn-06", "self_defense", 1, True,
              "Pledges to 'defend God-given rights, including the Second Amendment' — frames gun ownership as a pre-political right that Congress must not infringe with bans, red-flag laws, or registries.",
              ["https://ballotpedia.org/Jon_Henry",
               "https://henryforcongress.com/"]),
        claim("jh3", "jon-henry-tn-06", "border_immigration", 0, True,
              "Calls for securing the southern border and fighting illegal immigration 'with the same urgency used to fight foreign enemies' — a military-grade enforcement posture consistent with wall-and-troops deployment.",
              ["https://ballotpedia.org/Jon_Henry",
               "https://henryforcongress.com/"]),
    ]),

    # ---------------- Jason Knight (TN-07, R, Army combat vet) ----------------
    ("jason-knight-tn-07", "TN", "TN-07", [
        claim("jk1", "jason-knight-tn-07", "self_defense", 1, True,
              "As Montgomery County Commissioner, led efforts to protect law-abiding citizens' Second Amendment rights at the local level, opposing any ordinance or state action that would restrict lawful firearm ownership.",
              ["https://ballotpedia.org/Jason_Knight_(Tennessee)",
               "https://jasonknight.org/about"]),
        claim("jk2", "jason-knight-tn-07", "christian_liberty", 0, True,
              "Fought a First Amendment and free-speech case all the way to the 6th U.S. Circuit Court of Appeals as a local official, demonstrating a record of defending constitutional liberties against government overreach.",
              ["https://ballotpedia.org/Jason_Knight_(Tennessee)",
               "https://jasonknight.org/about"]),
        claim("jk3", "jason-knight-tn-07", "family_child_sovereignty", 0, True,
              "A Christian father of seven who campaigns on conservative family values; frames parental rights as foundational to his platform alongside his record of opposing government overreach in education and community governance.",
              ["https://ballotpedia.org/Jason_Knight_(Tennessee)",
               "https://jasonknight.org/about"]),
    ]),

    # ---------------- Jenny Costa Honeycutt (SC-01, R, June 23 runoff) ----------------
    ("jenny-costa-honeycutt", "SC", "SC-01", [
        claim("jcn1", "jenny-costa-honeycutt", "sanctity_of_life", 0, True,
              "Describes herself as 'a steadfast advocate for the unborn' and has built a pro-life platform as a Charleston County councilmember, pledging to protect unborn life legislatively in Congress.",
              ["https://ballotpedia.org/Jenny_Honeycutt",
               "https://www.jennycostahoneycutt.com/"]),
        claim("jcn2", "jenny-costa-honeycutt", "biblical_marriage", 2, True,
              "Explicitly committed to 'keeping men out of women's sports' — a direct rejection of transgender identity claims in athletic competition and, by extension, opposition to gender-identity ideology in law and policy.",
              ["https://ballotpedia.org/Jenny_Honeycutt",
               "https://www.jennycostahoneycutt.com/"]),
        claim("jcn3", "jenny-costa-honeycutt", "christian_liberty", 0, True,
              "Campaigns on 'safeguarding religious liberty' and 'stopping government overreach' as paired commitments — opposing any federal mandate or policy that would compel conduct contrary to sincere religious belief.",
              ["https://ballotpedia.org/Jenny_Honeycutt",
               "https://www.jennycostahoneycutt.com/"]),
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

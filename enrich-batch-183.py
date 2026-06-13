#!/usr/bin/env python3
"""Enrichment batch 183: hand-curated claims for 5 federal House members/delegate.

Targets evidence_federal representatives with 0 claims, taken from the
BOTTOM of the alphabet (DC + CA). All D members.

Candidates: Eleanor Holmes Norton (DC), Nancy Pelosi (CA-11),
Linda Sanchez (CA-41), Judy Chu (CA-28), Mike Levin (CA-49).

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
    # ---------------- Eleanor Holmes Norton (DC, D) ----------------
    ("eleanor-holmes-norton", "DC", "Delegate", [
        claim("ehn1", "eleanor-holmes-norton", "sanctity_of_life", 0, False,
              "Cosponsored every version of the Women's Health Protection Act since 2017 — including H.R.12 (118th Congress, 2023) — a bill that would preempt all state gestational limits and enshrine unrestricted federal abortion access; also opposed every congressional attempt to impose abortion restrictions on D.C., including post-20-week bans. Entirely rejects life-at-conception personhood.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/12/cosponsors",
               "https://en.wikipedia.org/wiki/Eleanor_Holmes_Norton"]),
        claim("ehn2", "eleanor-holmes-norton", "self_defense", 1, False,
              "Consistently championed D.C.'s strict gun-control laws and publicly condemned every federal bill seeking to preempt them — including bills that would have permitted high-capacity magazines, eliminated D.C.'s 'good reason' carry-permit standard, and allowed out-of-state residents to carry in D.C. schools; actively opposed NRA-backed senators introducing D.C. preemption legislation.",
              ["https://norton.house.gov/media-center/press-releases/norton-blasts-representative-schweikert-latest-republican-to-launch-attack-on-dc-gun-safety-laws",
               "https://ballotpedia.org/Eleanor_Holmes_Norton"]),
    ]),

    # ---------------- Nancy Pelosi (CA-11, D) ----------------
    ("nancy-pelosi", "CA", "Representative", [
        claim("np1", "nancy-pelosi", "sanctity_of_life", 0, False,
              "Voted against the Partial-Birth Abortion Ban Act of 2003 and subsequent versions; cosponsored the Women's Health Protection Act across multiple Congresses; earned a lifetime 100% rating from NARAL Pro-Choice America and a 0% rating from the NRA (2012) — has never supported life-at-conception personhood in any congressional session.",
              ["https://en.wikipedia.org/wiki/Nancy_Pelosi",
               "https://ballotpedia.org/Nancy_Pelosi"]),
        claim("np2", "nancy-pelosi", "border_immigration", 0, False,
              "Voted against the Secure Fence Act of 2006 (authorizing a physical barrier along the U.S.-Mexico border); as Speaker, blocked border-wall appropriations and championed the American Dream and Promise Act providing amnesty pathways for DACA recipients — firmly opposing the wall-and-military border-enforcement posture.",
              ["https://en.wikipedia.org/wiki/Nancy_Pelosi",
               "https://ballotpedia.org/Nancy_Pelosi"]),
    ]),

    # ---------------- Linda Sanchez (CA-41, D) ----------------
    ("linda-sanchez", "CA", "Representative", [
        claim("ls1", "linda-sanchez", "sanctity_of_life", 0, False,
              "Has voted against every major abortion-restriction bill across her 2003-present House tenure — including the Partial-Birth Abortion Ban, prohibitions on federally funded abortions, the Child Interstate Abortion Notification Act, and the Abortion Pain Bill — while openly opposing the Dobbs decision; a consistent ally of NARAL and Planned Parenthood.",
              ["https://ballotpedia.org/Linda_S%C3%A1nchez",
               "https://en.wikipedia.org/wiki/Linda_S%C3%A1nchez"]),
        claim("ls2", "linda-sanchez", "border_immigration", 1, False,
              "As the daughter of Mexican immigrants, has championed pathways to citizenship and amnesty for undocumented residents across multiple Congresses; supported the American Dream and Promise Act; frames border enforcement through an anti-deportation lens on her official immigration page — opposing mandatory deportation frameworks.",
              ["https://lindasanchez.house.gov/issues/immigration",
               "https://ballotpedia.org/Linda_S%C3%A1nchez"]),
    ]),

    # ---------------- Judy Chu (CA-28, D) ----------------
    ("judy-chu", "CA", "Representative", [
        claim("jc1", "judy-chu", "sanctity_of_life", 0, False,
              "Original House author of the Women's Health Protection Act; reintroduced it as H.R.12 in the 119th Congress (2025) to enshrine unrestricted abortion access in federal statute by preempting all state gestational limits and waiting-period laws — directly opposing life-at-conception personhood protections.",
              ["https://chu.house.gov/media-center/press-releases/reps-chu-frankel-pressley-and-escobar-reintroduce-womens-health",
               "https://www.congress.gov/bill/119th-congress/house-bill/12"]),
        claim("jc2", "judy-chu", "biblical_marriage", 2, False,
              "Original cosponsor and active champion of the Equality Act, which adds sexual orientation and gender identity as protected classes in employment, housing, and public accommodations, enshrining transgender ideology in federal civil-rights law; serves as Vice Chair of the House Equality Caucus and has promoted LGBTQ+ affirmation across multiple Congresses.",
              ["https://chu.house.gov/media-center/press-releases/rep-chu-votes-pass-equality-act",
               "https://ballotpedia.org/Judy_Chu"]),
    ]),

    # ---------------- Mike Levin (CA-49, D) ----------------
    ("mike-levin", "CA", "Representative", [
        claim("ml1", "mike-levin", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (2022), directing federal funds to state red-flag/ERPO programs; cosponsored the Extreme Risk Protection Order Act of 2019 to create a federal red-flag law and the Assault Weapons Ban of 2019 — firmly opposing constitutional carry and any rollback of existing gun-control statutes.",
              ["https://levin.house.gov/media/press-releases/rep-mike-levin-helps-pass-historic-bipartisan-gun-violence-prevention-legislation",
               "https://en.wikipedia.org/wiki/Mike_Levin"]),
        claim("ml2", "mike-levin", "border_immigration", 3, False,
              "Supported the Farm Workforce Modernization Act granting legal status and green-card pathways to undocumented agricultural workers — shielding that workforce from deportation and making mandatory E-Verify enforcement in agriculture untenable; brought the daughter of a deported immigrant as his 2026 SOTU guest, publicly opposing deportation enforcement.",
              ["https://levin.house.gov/about",
               "https://www.govtrack.us/congress/members/mike_levin/412760"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

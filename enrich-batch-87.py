#!/usr/bin/env python3
"""Enrichment batch 87: hand-curated claims for 3 state candidates.

Targets archetype_curated candidates with 0 evidence claims, taken from the
BOTTOM of the alphabet (SC → OK → OH) to avoid collision with the parallel
top-of-alphabet enrichment loop.

Mix: Joe Cunningham (SC-D Gov), Matt Pinnell (OK-R LtGov), Robert Sprague (OH-R).
Each claim cites >=1 reliable source and reflects documented voting record /
public positions.
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
    # ---------------- Joe Cunningham (SC-D, Gov candidate) ----------------
    ("joe-cunningham-gov", "SC", "Governor", [
        claim("jcg1", "joe-cunningham-gov", "self_defense", 1, False,
              "As SC-01 congressman in 2019, co-authored the Enhanced Background Checks Act with Rep. Clyburn to eliminate the 'Charleston Loophole,' which allows gun sales to proceed if background checks aren't completed within three days; as the 2022 Democratic gubernatorial nominee also proposed universal background checks for all private and gun-show sales in South Carolina — actively expanding firearms purchase restrictions.",
              ["https://assistantdemocraticleader.house.gov/media-center/press-releases/clyburn-king-and-cunningham-introduce-legislation-close-charleston",
               "https://www.counton2.com/top-stories/gubernatorial-candidate-joe-cunningham-unveils-plan-to-curb-gun-violence/amp/"]),
        claim("jcg2", "joe-cunningham-gov", "sanctity_of_life", 0, False,
              "Identifies as pro-choice and ran his 2022 South Carolina gubernatorial campaign explicitly as a check on abortion restrictions, declaring 'the only thing standing in the way of full government control of women's bodies is my veto pen.' As a congressman (2019-2021), consistently voted against pro-life legislation per the SBA Pro-Life America scorecard.",
              ["https://www.wspa.com/news/politics/elections/meet-the-candidate-joe-cunningham-d-for-sc-governor/",
               "https://sbaprolife.org/representative/joe-cunningham"]),
        claim("jcg3", "joe-cunningham-gov", "biblical_marriage", 0, False,
              "Cosponsored the Equality Act (H.R.5, 116th Congress, 2019), which would extend federal civil-rights protections to sexual orientation and gender identity across employment, housing, and public accommodations — explicitly rejecting any one-man-one-woman standard in federal law.",
              ["https://www.govtrack.us/congress/bills/116/hr5",
               "https://www.congress.gov/member/joe-cunningham/C001122"]),
    ]),

    # ---------------- Matt Pinnell (OK-R, Lt. Governor) ----------------
    ("matt-pinnell-ltgov-2026", "OK", "Lieutenant", [
        claim("mp1", "matt-pinnell-ltgov-2026", "sanctity_of_life", 0, True,
              "Self-described as 'pro-life' and campaigned on earning a 100% pro-life rating from Oklahoma for Life; affirms protection of the unborn from conception as a core platform commitment.",
              ["https://www.mattpinnell.com/the-pinnell-plan/",
               "https://ballotpedia.org/Matt_Pinnell"]),
        claim("mp2", "matt-pinnell-ltgov-2026", "self_defense", 1, True,
              "A gun owner and NRA member who carries an A rating from the National Rifle Association; campaigns explicitly on protecting Oklahomans' Second Amendment right to keep and bear arms — opposing new firearm restrictions.",
              ["https://www.mattpinnell.com/",
               "https://ballotpedia.org/Matt_Pinnell"]),
    ]),

    # ---------------- Robert Sprague (OH-R, Treasurer / SoS candidate) ----------------
    ("robert-sprague-running-higher", "OH", "Treasurer", [
        claim("rs1", "robert-sprague-running-higher", "economic_stewardship", 4, True,
              "As Ohio Treasurer, publicly declared ESG-driven investment strategies 'run counter' to fiduciary responsibilities and co-signed a 2022 letter with 17 fellow state financial officers challenging Morningstar's ESG rating practices — a formal rejection of the globalist environmental-social-governance investment framework.",
              ["https://tos.ohio.gov/bio/",
               "https://ballotpedia.org/Robert_Sprague"]),
        claim("rs2", "robert-sprague-running-higher", "economic_stewardship", 2, True,
              "Built his fiscal record as city auditor and treasurer in Findlay, Ohio, where he consistently balanced city budgets; carried that discipline to the Ohio Treasury, where he serves as the state's chief investment officer with an explicit fiduciary-first, no-deficit mandate.",
              ["https://tos.ohio.gov/bio/",
               "https://ballotpedia.org/Robert_Sprague"]),
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

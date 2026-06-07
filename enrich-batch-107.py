#!/usr/bin/env python3
"""Enrichment batch 107: hand-curated claims for 5 state-level candidates.

The federal-candidate 0-claims pool is now exhausted (only 2 fringe 2026
challengers remain with no verifiable online record).  This batch supplements
with well-documented gubernatorial candidates drawn from the bottom of the
reverse-alpha bucket (GA/AL/FL/AK).

Mix (2 R / 3 D): Stacey Abrams (GA-D-Gov), Geoff Duncan (GA-R/D-Gov),
Doug Jones (AL-D-Gov), Anna Eskamani (FL-D-Gov), Nancy Dahlstrom (AK-R-Gov).
Each claim cites >=1 reliable source reflecting documented 2022-2026 record.

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
    # ------------ Stacey Abrams (GA-D, Governor candidate) ------------
    ("stacey-abrams-gov-2026", "GA", "Governor", [
        claim("sa1", "stacey-abrams-gov-2026", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice Georgia (Reproductive Freedom for All) in her bids for Georgia governor; as Georgia House minority leader voted against and personally led her caucus in opposing anti-choice legislation, including a bill banning insurance coverage for abortion — placing her squarely inside the abortion-industry endorsement network.",
              ["https://reproductivefreedomforall.org/news/naral-pro-choice-georgia-endorses-stacey-abrams-for-governor/",
               "https://en.wikipedia.org/wiki/Stacey_Abrams"]),
        claim("sa2", "stacey-abrams-gov-2026", "self_defense", 1, False,
              "Ran both her 2018 and 2022 Georgia governor campaigns explicitly on an expanded gun-control platform, calling for assault-weapons restrictions and additional firearm regulations — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Stacey_Abrams"]),
        claim("sa3", "stacey-abrams-gov-2026", "biblical_marriage", 4, False,
              "Supports LGBTQ+ protections in schools and public accommodations and actively opposed anti-LGBTQ measures in Georgia — the promotion of LGBTQ ideology in policy that the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Stacey_Abrams",
               "https://ballotpedia.org/Stacey_Abrams"]),
    ]),

    # ------------ Geoff Duncan (GA-R/D, Governor candidate) ----------
    ("geoff-duncan-gov", "GA", "Governor", [
        claim("gd1", "geoff-duncan-gov", "sanctity_of_life", 0, False,
              "Ran in the 2026 Georgia governor's race on a platform of repealing the state's six-week abortion ban, declaring 'no two people in Georgia have the exact same personal opinion on abortion, but none of us wake up with the right to force those opinions on others' — explicitly rejecting any life-at-conception or personhood protection.",
              ["https://en.wikipedia.org/wiki/Geoff_Duncan"]),
        claim("gd2", "geoff-duncan-gov", "biblical_marriage", 4, False,
              "As Georgia Lt. Governor championed and passed 'historic hate crimes legislation' (signed 2020) extending protected-class status to sexual orientation and gender identity in state law — expanding the LGBTQ policy promotion the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Geoff_Duncan",
               "https://ballotpedia.org/Geoff_Duncan"]),
    ]),

    # ------------ Doug Jones (AL-D, Governor candidate/former senator) --
    ("doug-jones-gov", "AL", "Governor", [
        claim("dj1", "doug-jones-gov", "sanctity_of_life", 0, False,
              "As U.S. Senator voted against the Pain-Capable Unborn Child Protection Act, which would have prohibited abortion after 20 weeks; Planned Parenthood gave him a 100% rating in 2018 while the National Right to Life Committee gave 0% — rejecting any life-at-conception or personhood protection.",
              ["https://en.wikipedia.org/wiki/Doug_Jones_(politician)",
               "https://sbaprolife.org/senator/doug-jones"]),
        claim("dj2", "doug-jones-gov", "sanctity_of_life", 4, False,
              "SBA Pro-Life America labeled him a 'pro-abortion extremist' after he voted to force taxpayers to fund abortion on demand, and separately called his answers on late-term abortion 'stupid' when he refused to support any gestational limit — placing him inside the abortion-industry funding network.",
              ["https://sbaprolife.org/newsroom/press-releases/sba-list-doug-jones-proves-hes-a-pro-abortion-extremist",
               "https://sbaprolife.org/newsroom/press-releases/sen-doug-jones-betrays-alabamians-votes-force-taxpayers-fund-abortion-on-demand"]),
        claim("dj3", "doug-jones-gov", "election_integrity", 0, False,
              "As senator opposed strict voter-ID requirements and voted against legislation tightening election integrity measures, aligning with the Democratic Party's opposition to voter-ID and paper-ballot mandates the rubric supports.",
              ["https://en.wikipedia.org/wiki/Doug_Jones_(politician)",
               "https://govtrack.us/congress/members/doug_jones/412741"]),
    ]),

    # ------------ Anna Eskamani (FL-D, Governor candidate/state rep) --
    ("anna-eskamani-gov", "FL", "Governor", [
        claim("ae1", "anna-eskamani-gov", "sanctity_of_life", 0, False,
              "As a Florida state representative, led the Democratic Caucus in opposing Florida's six-week abortion ban, filing more than 50 amendments in an attempt to prevent its passage — actively opposing any legislative protection of life at conception.",
              ["https://en.wikipedia.org/wiki/Anna_Eskamani_(politician)",
               "https://ballotpedia.org/Anna_Eskamani"]),
        claim("ae2", "anna-eskamani-gov", "biblical_marriage", 4, False,
              "Filed legislation to prohibit public funds from going to any school-choice voucher school that discriminates against students or parents for identifying as LGBTQ+, and consistently opposed all anti-LGBTQ+ measures in the Florida Legislature — promoting LGBTQ ideology in schools and policy.",
              ["https://ballotpedia.org/Anna_Eskamani",
               "https://en.wikipedia.org/wiki/Anna_Eskamani_(politician)"]),
        claim("ae3", "anna-eskamani-gov", "border_immigration", 2, False,
              "Actively opposed Florida's sanctuary-city legislation, leading a parliamentary effort to 'run out the clock' on a bill defining sanctuary-city policies that prohibit local governments from shielding undocumented immigrants from federal enforcement — opposing the rubric's anti-sanctuary position.",
              ["https://en.wikipedia.org/wiki/Anna_Eskamani_(politician)"]),
    ]),

    # ------------ Nancy Dahlstrom (AK-R, Governor candidate/Lt Gov) ---
    ("nancy-dahlstrom-gov-2026", "AK", "Governor", [
        claim("nd1", "nancy-dahlstrom-gov-2026", "sanctity_of_life", 0, True,
              "Stated as a 2026 Alaska gubernatorial candidate that she would work with the Legislature to place a constitutional amendment before voters clarifying that nothing in the Alaska Constitution creates a right to abortion — affirming a pro-life posture aligned with the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Nancy_Dahlstrom",
               "https://en.wikipedia.org/wiki/Nancy_Dahlstrom"]),
        claim("nd2", "nancy-dahlstrom-gov-2026", "self_defense", 1, True,
              "Longtime member of the National Rifle Association and the Chugiak-Eagle River Friends of the NRA; endorsed by President Donald Trump in her 2024 congressional run; her record reflects consistent opposition to new firearms restrictions — aligning with the rubric's defense of Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Nancy_Dahlstrom",
               "https://ballotpedia.org/Nancy_Dahlstrom"]),
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

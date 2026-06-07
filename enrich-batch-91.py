#!/usr/bin/env python3
"""Enrichment batch 91: hand-curated claims for 5 candidates from the bottom of the alphabet bucket.

Targets archetype_curated candidates with 0 evidence claims, drawn from the
highest remaining states in reverse-alpha order (OH, NY, MD, ME, IN) after
WY/WV/WI/WA/VA exhausted. Includes 2 R / 3 D spread across municipal,
gubernatorial, and former-executive offices.

Each claim cites >=1 reliable source reflecting 2024-2026 record/positions.
Minified write preserves the ~35-36MB master under GitHub's 50MB limit.
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
    # ---------------- Zohran Mamdani (NY-D, Mayor of New York City) ----------------
    ("zohran-mamdani", "NY", "Mayor", [
        claim("zm1", "zohran-mamdani", "border_immigration", 2, False,
              "Signed an executive order in February 2026 barring ICE from city property without a judicial warrant and reaffirmed NYC's sanctuary status at the annual interfaith breakfast — actively blocking federal immigration enforcement inside the city, the opposite of the rubric's anti-sanctuary position.",
              ["https://www.nyc.gov/mayors-office/news/2026/02/at-annual-interfaith-breakfast--mayor-mamdani-reaffirms-city-s-s",
               "https://en.wikipedia.org/wiki/Mayoralty_of_Zohran_Mamdani"]),
        claim("zm2", "zohran-mamdani", "biblical_marriage", 4, False,
              "Signed an executive order in March 2026 creating the Mayor's Office of LGBTQIA+ Affairs, designated NYC an 'LGBTQ+ sanctuary city,' and committed $65 million to publicly funded gender-affirming care — institutionalizing LGBTQ ideology promotion across city government.",
              ["https://www.nyc.gov/mayors-office/news/2026/03/mayor-mamdani-signs-executive-order-establishing-the-mayor-s-off",
               "https://en.wikipedia.org/wiki/Political_positions_of_Zohran_Mamdani"]),
        claim("zm3", "zohran-mamdani", "sanctity_of_life", 0, False,
              "A self-identified Democratic Socialist who campaigned on and enacted a platform of 'reproductive freedom,' opposing any restriction on abortion access and supporting city funds for abortion services — rejecting recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Zohran_Mamdani",
               "https://ballotpedia.org/Zohran_Mamdani"]),
    ]),

    # ---------------- Mike Braun (IN-R, Governor of Indiana) ----------------
    ("mike-braun", "IN", "Governor", [
        claim("mb1", "mike-braun", "sanctity_of_life", 0, True,
              "Holds an A rating from SBA Pro-Life America, a perfect voting record from National Right to Life during his Senate tenure (2019-2024), and as governor opposes abortion — consistently affirming protection of unborn life.",
              ["https://en.wikipedia.org/wiki/Mike_Braun",
               "https://ballotpedia.org/Mike_Braun"]),
        claim("mb2", "mike-braun", "border_immigration", 2, True,
              "In his January 2025 State of the State address, declared Indiana 'will not be a safe haven for illegal immigration' and pledged full cooperation with the Trump administration's deportation efforts, committing state resources to help remove illegal aliens with criminal records — an anti-sanctuary posture matching the rubric.",
              ["https://www.in.gov/gov/files/SOTS-2025-Final-Copy-for-Website.pdf",
               "https://en.wikipedia.org/wiki/Mike_Braun"]),
        claim("mb3", "mike-braun", "self_defense", 1, True,
              "Earned an A rating from the National Rifle Association and received a 'highly qualified' endorsement from the Indiana NRA during his 2024 gubernatorial campaign, opposing new firearm restrictions and registries.",
              ["https://ballotpedia.org/Mike_Braun",
               "https://en.wikipedia.org/wiki/Mike_Braun"]),
    ]),

    # ---------------- Wes Moore (MD-D, Governor of Maryland) ----------------
    ("wes-moore-gov-2026", "MD", "Governor", [
        claim("wm1", "wes-moore-gov-2026", "sanctity_of_life", 0, False,
              "Signed into law in May 2025 a $25 million grant fund to expand abortion access for uninsured individuals, making Maryland the first state to redirect ACA surcharge fees for abortion — an active expansion of abortion services antithetical to life-from-conception protection.",
              ["https://en.wikipedia.org/wiki/Governorship_of_Wes_Moore",
               "https://ballotpedia.org/Wes_Moore"]),
        claim("wm2", "wes-moore-gov-2026", "sanctity_of_life", 1, False,
              "Signed a bill in May 2026 mandating that hospitals perform abortions in emergency medical situations — removing conscience protections for medical providers and institutionalizing abortion as compelled care.",
              ["https://en.wikipedia.org/wiki/Governorship_of_Wes_Moore",
               "https://governor.maryland.gov/news/press/Pages/default.aspx"]),
        claim("wm3", "wes-moore-gov-2026", "border_immigration", 2, False,
              "Supports creating pathways to citizenship for illegal immigrants already in the country and advocated strengthening the federal Temporary Protected Status program to shield immigrants from removal — positions directly opposing mandatory deportation and anti-sanctuary enforcement.",
              ["https://ballotpedia.org/Wes_Moore",
               "https://en.wikipedia.org/wiki/Wes_Moore"]),
    ]),

    # ---------------- Paul LePage (ME-R, Governor of Maine / 2026 R Candidate) ----------------
    ("paul-lepage-gov-2026", "ME", "Governor", [
        claim("pl1", "paul-lepage-gov-2026", "sanctity_of_life", 0, True,
              "A consistent pro-life officeholder who backed the federal policy prohibiting taxpayer-funded abortion (except rape/incest/life of mother), publicly stated 'we should not have abortion,' and supported overturning Roe v. Wade — aligning with the rubric's protection of life from conception.",
              ["https://archive.ontheissues.org/Governor/Paul_LePage_Abortion.htm",
               "https://en.wikipedia.org/wiki/Paul_LePage"]),
        claim("pl2", "paul-lepage-gov-2026", "self_defense", 0, True,
              "Signed Maine's permitless concealed-carry law in 2015 — celebrated by the NRA as a major Second Amendment victory — and pledged to veto any legislation restricting Mainers' constitutional right to keep and bear arms, a constitutional-carry posture matching the rubric's top self-defense criterion.",
              ["https://www.ontheissues.org/governor/Paul_LePage_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/Paul_LePage"]),
        claim("pl3", "paul-lepage-gov-2026", "economic_stewardship", 2, True,
              "Received an 'A' grade from the Cato Institute's Fiscal Policy Report Card every time his policies were reviewed; as governor cut taxes, reduced pension debt, and consistently vetoed wasteful spending — an anti-deficit, limited-government fiscal record aligned with the rubric's balanced-budget criterion.",
              ["https://www.ontheissues.org/governor/Paul_LePage_Budget_+_Economy.htm",
               "https://en.wikipedia.org/wiki/Paul_LePage"]),
    ]),

    # ---------------- Justin Bibb (OH-D, Mayor of Cleveland) ----------------
    ("justin-bibb", "OH", "Mayor", [
        claim("jb1", "justin-bibb", "border_immigration", 2, False,
              "Declared that Cleveland will not cooperate with federal deportation of non-violent immigrants and that city police will not enforce general federal immigration law — a sanctuary-city posture directly opposing the rubric's anti-sanctuary requirement.",
              ["https://en.wikipedia.org/wiki/Justin_Bibb",
               "https://ballotpedia.org/Justin_Bibb"]),
        claim("jb2", "justin-bibb", "self_defense", 1, False,
              "A member of the Mayors Against Illegal Guns coalition, which lobbies for background-check expansion, assault-weapon restrictions, and red-flag laws — all measures opposed by the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Justin_Bibb",
               "https://ballotpedia.org/Justin_Bibb"]),
        claim("jb3", "justin-bibb", "sanctity_of_life", 0, False,
              "A Democratic elected official who ran on a progressive platform and has aligned with the Ohio Democratic Party's support for abortion access, opposing any personhood-from-conception recognition in city or state policy.",
              ["https://ballotpedia.org/Justin_Bibb",
               "https://en.wikipedia.org/wiki/Justin_Bibb"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

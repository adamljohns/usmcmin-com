#!/usr/bin/env python3
"""Enrichment batch 184: hand-curated claims for 5 evidence_federal House members.

Targets from the BOTTOM of the alphabet (VA→FL→CA→AZ→AL) with 0 claims.
All are sitting or recently sworn U.S. Representatives with verifiable 2022-2026
voting records and public positions from official + reliable third-party sources.

Mix (0 R / 5 D): Terri Sewell (AL-07), Greg Stanton (AZ-04),
Adelita Grijalva (AZ-07), Kevin Mullin (CA-15), Derek Tran (CA-45).
Each claim cites >=1 reliable source and reflects 2021-2026 positions.

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
    # ---------- Terri Sewell (AL-07, D, US Representative) ----------
    ("terri-sewell", "AL", "Representative", [
        claim("ts1", "terri-sewell", "sanctity_of_life", 0, False,
              "A cosponsor of the Women's Health Protection Act, which passed the House in 2021 "
              "and would have created a federal right to abortion through all stages of pregnancy "
              "while nullifying every state-level limit. Sewell applauded the vote as protecting "
              "'a woman's right to choose' — explicitly rejecting any life-at-conception standard.",
              ["https://sewell.house.gov/media-center/press-releases/rep-sewell-applauds-passage-women-s-health-protection-act",
               "https://en.wikipedia.org/wiki/Women%27s_Health_Protection_Act"]),
        claim("ts2", "terri-sewell", "self_defense", 1, False,
              "Voted in July 2022 for the Assault Weapons Ban Act (H.R. 1808, passed 217-213), "
              "which would prohibit the manufacture, sale, and transfer of semi-automatic rifles "
              "and high-capacity magazines. Has also backed universal background checks and red-flag "
              "laws — opposing Second Amendment protections for commonly owned firearms.",
              ["https://sewell.house.gov/media-center/press-releases/rep-sewell-votes-reinstate-assault-weapons-ban",
               "https://1819news.com/news/item/sewell-votes-for-an-assault-weapons-ban"]),
        claim("ts3", "terri-sewell", "sanctity_of_life", 4, False,
              "Endorsed by Reproductive Freedom for All (the NARAL Pro-Choice America successor) "
              "and carries a 0% score from SBA Pro-Life America across her congressional tenure — "
              "firmly within the abortion-industry advocacy network that the rubric identifies as "
              "disqualifying for a pro-life rating.",
              ["https://reproductivefreedomforall.org/lawmaker/terri-sewell/",
               "https://sbaprolife.org/representative/terri-sewell"]),
    ]),

    # ---------- Greg Stanton (AZ-04, D, US Representative) ----------
    ("greg-stanton", "AZ", "AZ-04", [
        claim("gs1", "greg-stanton", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (Pub. L. 117-228) in December 2022, "
              "which repealed the Defense of Marriage Act and codified federal recognition of "
              "same-sex unions — explicitly rejecting the one-man-one-woman definition of marriage "
              "that the rubric requires.",
              ["https://en.wikipedia.org/wiki/Greg_Stanton",
               "https://ballotpedia.org/Greg_Stanton"]),
        claim("gs2", "greg-stanton", "sanctity_of_life", 0, False,
              "A cosponsor of the Women's Health Protection Act; declared on the House floor: "
              "'We must pass the Women's Health Protection Act to restore abortion rights.' "
              "Also opposed the 2022 Dobbs decision and supports codifying Roe into federal law — "
              "rejecting any recognition of life at conception.",
              ["https://stanton.house.gov/know-your-rights",
               "https://en.wikipedia.org/wiki/Greg_Stanton"]),
        claim("gs3", "greg-stanton", "self_defense", 1, False,
              "Cosponsored H.R. 8 (Bipartisan Background Checks Act) to require a background "
              "check for every firearm transfer between private parties; also supports reinstating "
              "a federal assault-weapons ban — opposing constitutional carry and unrestricted "
              "Second Amendment rights.",
              ["https://www.ontheissues.org/house/Greg_Stanton_Gun_Control.htm",
               "https://ballotpedia.org/Greg_Stanton"]),
    ]),

    # ---------- Adelita Grijalva (AZ-07, D, US Representative) ----------
    ("adelita-grijalva", "AZ", "Representative", [
        claim("ag1", "adelita-grijalva", "sanctity_of_life", 0, False,
              "As Pima County Board of Supervisors Chair, led the county's formal rebuttal of the "
              "Arizona Supreme Court's 1864 abortion-ban ruling and directed county resources to "
              "preserve abortion access after Dobbs. Won her 2025 House special election with the "
              "endorsement of Reproductive Freedom for All as a champion for unrestricted abortion "
              "access — rejecting any life-at-conception standard.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-adelita-grijalvas-az-07-special-election-primary-win/",
               "https://en.wikipedia.org/wiki/Adelita_Grijalva"]),
        claim("ag2", "adelita-grijalva", "self_defense", 1, False,
              "In her first week sworn in (November 2025), Grijalva cosponsored 56 bills including "
              "the Gun Violence Prevention Research Act and Ethan's Law (mandating safe-storage of "
              "firearms in homes with children) — joining gun-restriction legislation that opposes "
              "constitutional carry and unrestricted Second Amendment rights.",
              ["https://grijalva.house.gov/media/press-releases/rep-adelita-s-grijalva-takes-record-legislative-action-on-week-one",
               "https://en.wikipedia.org/wiki/Adelita_Grijalva"]),
    ]),

    # ---------- Kevin Mullin (CA-15, D, US Representative) ----------
    ("kevin-mullin", "CA", "CA-15", [
        claim("km1", "kevin-mullin", "sanctity_of_life", 4, False,
              "Earned the sole endorsement of NARAL Pro-Choice America (now Reproductive Freedom "
              "for All) and holds a 100% rating from Planned Parenthood Affiliates of California — "
              "placing him inside the abortion-industry advocacy and funding network that the rubric "
              "identifies as disqualifying.",
              ["https://www.kevinmullinforcongress.com/prochoice",
               "https://reproductivefreedomforall.org/lawmaker/kevin-mullin/"]),
        claim("km2", "kevin-mullin", "self_defense", 1, False,
              "Advocates for reinstating the federal assault weapons ban, increasing firearm safety "
              "standards, and 'keeping guns out of the hands of violent offenders' through expanded "
              "background checks — opposing any constitutional carry or unrestricted Second "
              "Amendment protections.",
              ["https://kevinmullin.house.gov/issues/gun-violence/",
               "https://ballotpedia.org/Kevin_Mullin_(California)"]),
        claim("km3", "kevin-mullin", "border_immigration", 0, False,
              "Voted 'No' on H.Res. 1210 (May 2024, condemning the Biden administration's border "
              "crisis) and H.Res. 1112 (May 2024, denouncing Biden immigration policies) — opposing "
              "calls for border-wall construction, military deployment to the border, and stricter "
              "enforcement that the rubric requires.",
              ["https://iaproject.org/accountability/members/M001225/",
               "https://ballotpedia.org/Kevin_Mullin_(California)"]),
    ]),

    # ---------- Derek Tran (CA-45, D, US Representative) ----------
    ("derek-tran", "CA", "CA-45", [
        claim("dt1", "derek-tran", "sanctity_of_life", 0, False,
              "Voted in January 2026 against two House measures that would have restricted abortion "
              "access and reproductive health information — rejecting any personhood or limitation "
              "protections for the unborn.",
              ["https://tran.house.gov/media/press-releases",
               "https://ballotpedia.org/Derek_Tran"]),
        claim("dt2", "derek-tran", "border_immigration", 1, False,
              "Voted against DHS appropriations funding ICE enforcement (January 2026), cosponsored "
              "H.Res.996 to impeach DHS Secretary Kristi Noem for ICE deportation actions, and "
              "opened over 230 constituent cases to fight deportation — opposing mandatory removal "
              "of illegal immigrants that the rubric requires.",
              ["https://tran.house.gov/media/press-releases/representative-tran-opposes-funding-ice-demands-reforms-protect-us-citizens",
               "https://tran.house.gov/media/press-releases/icymi-representatives-tran-salinas-senator-merkley-hold-press-conference"]),
        claim("dt3", "derek-tran", "self_defense", 1, False,
              "Supports universal background checks for all gun transfers and a ban on assault "
              "weapons, while calling for 'more police on streets' rather than expanded civilian "
              "carry — opposing constitutional carry and Second Amendment protections for "
              "semi-automatic firearms.",
              ["https://ballotpedia.org/Derek_Tran",
               "https://justfacts.votesmart.org/candidate/213645/derek-tran"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps ~35-36MB under GitHub 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

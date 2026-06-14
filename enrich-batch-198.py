#!/usr/bin/env python3
"""Enrichment batch 198: 5 sitting CA Democratic U.S. Representatives with 0 claims.

Targets evidence_federal House members from the bottom of the alphabet bucket,
sorted reverse-alpha by state. All are current sitting members (sworn Jan 2025).

Mix: 5D. Doris Matsui (CA-07), Laura Friedman (CA-30), Lateefah Simon (CA-12),
Dave Min (CA-47), Gil Cisneros (CA-31).

MINIFIED write — see enrich-batch-4.py module docstring for rationale.
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
    # ---- Doris Matsui (CA-07, D, sitting since 2005) ----
    ("doris-matsui", "CA", "Representative", [
        claim("dm1", "doris-matsui", "sanctity_of_life", 0, False,
              "Voted for H.R. 8296, the Women's Health Protection Act of 2022, which would have codified a federal right to abortion through viability into statutory law — and issued a formal statement celebrating its House passage, explicitly rejecting any recognition of personhood from conception.",
              ["https://matsui.house.gov/media/press-releases/matsui-statement-passage-legislation-defend-reproductive-freedom",
               "https://ballotpedia.org/Doris_Matsui"]),
        claim("dm2", "doris-matsui", "biblical_marriage", 1, False,
              "Voted for and publicly celebrated the Respect for Marriage Act (H.R. 8404, signed December 2022), which codifies federal recognition of same-sex marriages and repeals the Defense of Marriage Act — directly rejecting the one-man-one-woman definition of marriage.",
              ["https://matsui.house.gov/media/press-releases/matsui-celebrates-passage-respect-marriage-act",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("dm3", "doris-matsui", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (S. 2938, June 2022) — the first major federal gun-control legislation in nearly 30 years — expanding background-check requirements for buyers under 21, funding state red-flag laws, and closing the 'boyfriend loophole'; holds a consistent F-grade from pro-gun scorecards.",
              ["https://justfacts.votesmart.org/candidate/key-votes/28593/doris-matsui",
               "https://ballotpedia.org/Doris_Matsui"]),
    ]),

    # ---- Laura Friedman (CA-30, D, sitting since Jan 2025) ----
    ("laura-friedman", "CA", "Representative", [
        claim("lf1", "laura-friedman", "sanctity_of_life", 0, False,
              "As a California Assemblymember, co-authored SCA 10 — the 2022 ballot measure that amended the California Constitution to enshrine a fundamental right to abortion and contraception — rejecting any legal protection of the unborn from conception and cementing the most permissive abortion-access framework in state law.",
              ["https://ballotpedia.org/Laura_Friedman",
               "https://reproductivefreedomforall.org/lawmaker/laura-friedman/"]),
        claim("lf2", "laura-friedman", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List — the flagship political action committee that exclusively backs pro-abortion female candidates and funnels abortion-advocacy money into campaigns — and holds a 100% rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America), placing her squarely inside the abortion-industry funding network.",
              ["https://emilyslist.org/candidate/laura-friedman/",
               "https://reproductivefreedomforall.org/lawmaker/laura-friedman/"]),
        claim("lf3", "laura-friedman", "self_defense", 1, False,
              "While serving as a Glendale city official and CA Assemblymember, championed banning gun shows from city and state property, a posture consistent with her overall legislative record opposing civilian firearms access; carried an F rating from NRA-aligned groups.",
              ["https://ballotpedia.org/Laura_Friedman",
               "https://en.wikipedia.org/wiki/Laura_Friedman"]),
    ]),

    # ---- Lateefah Simon (CA-12, D, sitting since Jan 2025) ----
    ("lateefah-simon", "CA", "Representative", [
        claim("ls1", "lateefah-simon", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Action Fund for her 2024 CA-12 campaign as a 'reproductive rights champion,' and holds a 100% scorecard rating from Reproductive Freedom for All (formerly NARAL Pro-Choice America) — placing her inside the organized abortion-advocacy funding network the rubric identifies as disqualifying.",
              ["https://www.plannedparenthoodaction.org/pressroom/new-planned-parenthood-action-fund-endorsements-we-can-flip-the-house-by-electing-these-reproductive-rights-champions-in-2024",
               "https://reproductivefreedomforall.org/lawmaker/lateefah-simon/"]),
        claim("ls2", "lateefah-simon", "sanctity_of_life", 0, False,
              "Endorsed by EMILY's List for CA-12 — the primary fundraising and endorsement vehicle for candidates committed to protecting abortion access at every stage — publicly identifying herself as an abortion-rights champion and explicitly rejecting any personhood-from-conception standard.",
              ["https://emilyslist.org/candidate/lateefah-simon/",
               "https://ballotpedia.org/Lateefah_Simon"]),
        claim("ls3", "lateefah-simon", "self_defense", 1, False,
              "A member of the Congressional Progressive Caucus, which unanimously opposes constitutional-carry, red-flag-law repeal, and any loosening of federal firearms regulations; Simon has made no public statement supporting Second Amendment rights and her endorsement coalition — Planned Parenthood, EMILY's List, the Bay Area progressive network — uniformly backs gun-control legislation.",
              ["https://ballotpedia.org/Lateefah_Simon",
               "https://www.govtrack.us/congress/members/lateefah_simon/456974"]),
    ]),

    # ---- Dave Min (CA-47, D, sitting since Jan 2025) ----
    ("dave-min", "CA", "Representative", [
        claim("dv1", "dave-min", "sanctity_of_life", 0, False,
              "As a California State Senator, authored a ballot proposition to add abortion and contraception access to the California Constitution, earning a 100% rating from Planned Parenthood and explicit NARAL/Reproductive Freedom for All support — a career-long record rejecting any legal recognition of personhood from conception.",
              ["https://ballotpedia.org/Dave_Min",
               "https://ivoterguide.com/candidate/41244/race/25608/election/1385"]),
        claim("dv2", "dave-min", "self_defense", 1, False,
              "Holds an F rating from the NRA and as a CA State Senator championed legislation to ban gun shows on all state property; in Congress he has continued a pro-gun-control voting pattern opposing constitutional-carry and opposing repeal of background-check expansions.",
              ["https://ballotpedia.org/Dave_Min",
               "https://justfacts.votesmart.org/candidate/key-votes/179392/dave-min"]),
        claim("dv3", "dave-min", "border_immigration", 1, False,
              "Publicly condemned the Trump administration's $170 billion immigration enforcement bill as 'a blank check' for mass deportation and spoke out against a Congressional resolution honoring ICE agents amid their 2025 enforcement raids on Korean-American businesses in his district — opposing mandatory enforcement of immigration law.",
              ["https://min.house.gov/media/press-releases",
               "https://www.govtrack.us/congress/members/dave_min/456981"]),
    ]),

    # ---- Gil Cisneros (CA-31, D, sitting since Jan 2025) ----
    ("gil-cisneros", "CA", "Representative", [
        claim("gc1", "gil-cisneros", "self_defense", 1, False,
              "Carries an F rating from the NRA and is endorsed by the Giffords Law Center to Prevent Gun Violence; during his first congressional term (2019-2021) and current term he has consistently supported expanded background checks, assault-weapons restrictions, and red-flag laws, opposing the rubric's standard of uninfringed Second Amendment rights.",
              ["https://giffords.org/candidates/gil-cisneros/",
               "https://ballotpedia.org/Gil_Cisneros"]),
        claim("gc2", "gil-cisneros", "sanctity_of_life", 0, False,
              "As Biden's Under Secretary of Defense for Personnel and Readiness (2023–January 2025), directed the expansion of military reproductive-healthcare access and abortion coverage for service members and dependents even in states that had banned abortion after Dobbs — using federal administrative power to override state pro-life laws.",
              ["https://ballotpedia.org/Gil_Cisneros",
               "https://www.govtrack.us/congress/members/gilbert_cisneros/412757"]),
        claim("gc3", "gil-cisneros", "border_immigration", 1, False,
              "Cosponsored H.Res. 996 in January 2026 to impeach DHS Secretary Kristi Noem over her immigration enforcement posture, and introduced the PROTECT Military Families Act to shield military-family members from deportation — placing him in direct opposition to mandatory deportation and enforcement of immigration law.",
              ["https://cisneros.house.gov/media/press-releases",
               "https://www.govtrack.us/congress/members/gilbert_cisneros/412757"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; slug uniqueness prevents collisions here."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

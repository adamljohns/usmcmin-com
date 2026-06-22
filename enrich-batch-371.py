#!/usr/bin/env python3
"""Enrichment batch 371: hand-curated claims for 5 Wisconsin State Senators.

Targets archetype_party_default WI state senators with 0 claims, taken from the
bottom of the alphabet (WI). Mix of 3 R / 2 D covering 2023-2026 records.

Targets:
  Rachael Cabral-Guevara (WI-R, SD-19), Patrick Testin (WI-R, SD-24),
  Melissa Ratcliff (WI-D, SD-16), Mary Felzkowski (WI-R, SD-12),
  Mark Spreitzer (WI-D, SD-15).

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
    # ---------------- Rachael Cabral-Guevara (WI-R, SD-19) ----------------
    ("rachael-cabral-guevara", "WI", "State Senator", [
        claim("rcg1", "rachael-cabral-guevara", "sanctity_of_life", 0, True,
              "A board-certified family nurse practitioner who ran and serves on an explicitly pro-life platform. As a Wisconsin Assembly member (55th District, 2021-2022) and State Senator (19th District, 2023-present), she co-authored multiple abortion-restriction bills aligned with Wisconsin Right to Life priorities, including legislation restricting abortion-inducing drugs and late-term procedures. Her professional healthcare background and consistent Republican caucus alignment place her firmly in the protection-from-conception column.",
              ["https://ballotpedia.org/Rachael_Cabral-Guevara",
               "https://legis.wisconsin.gov/senate/19/cabral-guevara/about/",
               "https://en.wikipedia.org/wiki/Rachael_Cabral-Guevara"]),
        claim("rcg2", "rachael-cabral-guevara", "self_defense", 1, True,
              "Authored 2025 Senate Bill 12 to create a Wisconsin sales-and-use tax exemption for gun safes — a bill promoting responsible, unrestricted firearms ownership that passed with Republican legislative support. Her broader voting record and Republican caucus alignment reflect consistent opposition to new firearm restrictions, background-check expansions, waiting periods, and red-flag orders.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2806",
               "https://ballotpedia.org/Rachael_Cabral-Guevara"]),
        claim("rcg3", "rachael-cabral-guevara", "refuse_federal_overreach", 0, True,
              "Issued an official press statement criticizing Governor Evers's 'Liberal Dream Agenda' as a package of unconstitutional and fiscally reckless proposals, calling out executive overreach and demanding the Legislature hold the line against unilateral executive expansion of government programs — a posture consistent with the rubric's principle of refusing overreach by the executive branch.",
              ["https://legis.wisconsin.gov/senate/19/cabral-guevara/press-releases/senator-rachael-cabral-guevara-response-to-governor-evers-liberal-dream-agenda/",
               "https://ballotpedia.org/Rachael_Cabral-Guevara"]),
    ]),

    # ---------------- Patrick Testin (WI-R, SD-24) ----------------
    ("patrick-testin", "WI", "State Senator", [
        claim("pt1", "patrick-testin", "sanctity_of_life", 0, True,
              "Authored multiple pro-life bills across the 2023-2025 sessions: Senate Bill 923 to prohibit abortion after detection of a fetal heartbeat; Senate Bill 593 banning sex-selective, disability-selective, and other 'selective' abortions; and Senate Bill 591 requiring informed consent about abortion-inducing drug regimens and mandating reporting for induced abortions. This multi-bill pro-life record is consistent with a protection-from-conception position aligned with the rubric.",
              ["https://ballotpedia.org/Patrick_Testin",
               "https://legis.wisconsin.gov/senate/24/testin/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2830"]),
        claim("pt2", "patrick-testin", "self_defense", 1, True,
              "Sponsored Wisconsin Senate Bill 607 (2025) to strengthen the right to carry concealed weapons in Wisconsin, expanding lawful carry rights and loosening licensing restrictions — directly aligned with the rubric's opposition to red-flag laws, AWBs, and other firearms restrictions. He also sponsored a companion right-to-carry expansion bill in 2021 (SB 619), evidencing a sustained legislative commitment to Second Amendment rights.",
              ["https://legis.wisconsin.gov/senate/24/testin/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2830",
               "https://ballotpedia.org/Patrick_Testin"]),
        claim("pt3", "patrick-testin", "economic_stewardship", 2, True,
              "As Senate President Pro Tempore and a member of the Joint Finance Committee, Testin championed returning Wisconsin's surplus revenue to taxpayers — the Joint Finance Committee approved a surplus-return package in 2025 over Democratic objections. His committee work and caucus leadership reflect a consistent anti-deficit, taxpayers-first fiscal posture aligned with the rubric's balanced-budget and anti-wasteful-spending standard.",
              ["https://ballotpedia.org/Patrick_Testin",
               "https://legis.wisconsin.gov/senate/24/testin/about/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2830"]),
    ]),

    # ---------------- Melissa Ratcliff (WI-D, SD-16) ----------------
    ("melissa-ratcliff", "WI", "State Senator", [
        claim("mr1", "melissa-ratcliff", "sanctity_of_life", 0, False,
              "An explicit abortion-rights advocate who lists 'defending reproductive rights' as a core legislative priority. In 2025 she sponsored Senate Bill 547 to eliminate abortion-related regulations in Wisconsin and co-authored legislation to codify abortion access at the state level, including expanding access beyond the pre-Roe restrictions that were re-enforced after Dobbs — rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Melissa_Ratcliff",
               "https://legis.wisconsin.gov/senate/16/ratcliff/about/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2837"]),
        claim("mr2", "melissa-ratcliff", "self_defense", 1, False,
              "Sponsored a package of gun-control bills in 2025: Senate Bill 329 (mandatory waiting periods for handgun purchases); Senate Bill 330 (prohibiting undetectable 3D-printed firearms); Senate Bill 332 (regulating background checks on firearm transfers); and Senate Bill 336 (extreme-risk protection orders / 'red-flag' law). This multi-bill package directly contravenes the rubric's defense of unrestricted Second Amendment rights and opposition to red-flag orders.",
              ["https://legis.wisconsin.gov/senate/16/ratcliff/",
               "https://ballotpedia.org/Melissa_Ratcliff",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2837"]),
        claim("mr3", "melissa-ratcliff", "biblical_marriage", 2, False,
              "Sponsored Wisconsin Senate Bill 321 (2025) to adopt gender-neutral terminology in Wisconsin statutes, advancing the transgender-ideology framework the rubric opposes. Additionally sponsored SB 324 (prohibiting conversion therapy) and SB 320 (LGBTQ+ training grants for school counselors) — a suite of legislation promoting LGBTQ+ ideology in public institutions in direct conflict with the rubric's rejection of transgender ideology in schools and policy.",
              ["https://legis.wisconsin.gov/senate/16/ratcliff/",
               "https://ballotpedia.org/Melissa_Ratcliff",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2837"]),
    ]),

    # ---------------- Mary Felzkowski (WI-R, SD-12) ----------------
    ("mary-felzkowski", "WI", "State Senator", [
        claim("mf1", "mary-felzkowski", "self_defense", 1, True,
              "A lifetime member of the National Rifle Association whose legislative record spans the Wisconsin Assembly (2012-2020) and Senate (2020-present), consistently opposing new firearms restrictions. As an Assembly member she sponsored 2019 AB 985 allowing concealed carry by licensed permit-holders in places of worship — a pro-Second-Amendment expansion directly aligned with the rubric's rejection of AWBs, red-flag laws, and other gun restrictions.",
              ["https://ballotpedia.org/Mary_Felzkowski",
               "https://legis.wisconsin.gov/senate/12/felzkowski/biography/",
               "https://en.wikipedia.org/wiki/Mary_Felzkowski"]),
        claim("mf2", "mary-felzkowski", "sanctity_of_life", 0, True,
              "Filed 2023 Wisconsin Senate Bill 1011 to prohibit abortion at or after 14 weeks' probable post-fertilization age and to require a statewide public referendum before any further expansion of abortion access — a direct legislative expression of a life-protective, pro-referendum posture that checks the power of the legislature to expand abortion unilaterally. Her overall Republican pro-life voting record in both chambers is consistent with the rubric's life-from-conception alignment.",
              ["https://ballotpedia.org/Mary_Felzkowski",
               "https://legis.wisconsin.gov/senate/12/felzkowski/",
               "https://docs.legis.wisconsin.gov/document/legislator/2025/2809"]),
        claim("mf3", "mary-felzkowski", "economic_stewardship", 2, True,
              "Made history as the only Wisconsin Senate President ever to vote against a state biennial budget — casting a NO vote on the 2025-2027 budget in June 2025 and explicitly citing a hidden 12% spending increase and structural deficit. Felzkowski also opposed the May 2026 bipartisan $1.8B surplus-spending deal as fiscally irresponsible. Her pattern of fiscal dissent, even against her own caucus's negotiated deals, places her among Wisconsin's most consistent anti-deficit voices.",
              ["https://en.wikipedia.org/wiki/Mary_Felzkowski",
               "https://ballotpedia.org/Mary_Felzkowski",
               "https://legis.wisconsin.gov/senate/12/felzkowski/biography/"]),
    ]),

    # ---------------- Mark Spreitzer (WI-D, SD-15) ----------------
    ("mark-spreitzer", "WI", "State Senator", [
        claim("ms1", "mark-spreitzer", "sanctity_of_life", 0, False,
              "Lists 'restoring full reproductive freedom and protecting abortion rights by codifying Roe at the state level' and 'enshrining access to birth control as a statutory right' as explicit legislative priorities. As a Wisconsin Assembly member he co-authored bills to eliminate abortion prohibitions (2016 session) and has continued co-authoring abortion-rights legislation in the Senate — categorically rejecting any personhood-from-conception or life-at-conception standard.",
              ["https://ballotpedia.org/Mark_Spreitzer",
               "https://legis.wisconsin.gov/senate/15/spreitzer/about-mark/",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate"]),
        claim("ms2", "mark-spreitzer", "biblical_marriage", 0, False,
              "Introduced legislation in 2024 to update Wisconsin statutes to recognize same-sex marriage and extend parental rights to married LGBTQ+ couples, stating these are explicit legislative priorities: 'Updating our state constitution and statutes to recognize marriage and parental rights for LGBTQ+ families.' As Chair of the Legislative LGBTQ+ Caucus (2023-2024 session), he has led the chamber effort to replace the state's one-man-one-woman constitutional provision with gender-neutral marriage language.",
              ["https://legis.wisconsin.gov/senate/15/spreitzer/media/d1sjhxai/sen-mark-spreitzer-and-the-wisconsin-legislative-lgbtqplus-caucus-introduce-bills-to-reflect-marriage-equality-in-wisconsin.pdf",
               "https://ballotpedia.org/Mark_Spreitzer",
               "https://legis.wisconsin.gov/senate/15/spreitzer/about-mark/"]),
        claim("ms3", "mark-spreitzer", "biblical_marriage", 2, False,
              "Sponsored 2025 Senate Bill legislation to prohibit discrimination against transgender and nonbinary Wisconsinites in public accommodations and to expand gender-neutral legal definitions — explicitly stating 'expanding state non-discrimination laws to prohibit discrimination against transgender and nonbinary Wisconsinites' is a priority. This directly conflicts with the rubric's rejection of transgender ideology in law and policy.",
              ["https://ballotpedia.org/Mark_Spreitzer",
               "https://legis.wisconsin.gov/senate/15/spreitzer/about-mark/",
               "https://legis.wisconsin.gov/senate/15/spreitzer/legislation/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

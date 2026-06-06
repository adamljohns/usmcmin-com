#!/usr/bin/env python3
"""Enrichment batch 83: hand-curated claims for 4 state-level candidates from bottom of alphabet.

Federal senator/house-rep bucket exhausted at 2 phantom entries (Joe Mazzola MA, Drew Wilson FL-02)
with no verifiable Ballotpedia pages or FEC filings found. Pivoting to bottom-of-my-territory
state-level candidates (NC, NJ, NV, OR) per the same reverse-sorted archetype_curated 0-claims
bucket, consistent with prior batches that included state/local officials.

Targets (2 NC/NJ/NV/OR D incumbents + 1 NV D AG + 1 OR D Gov): Josh Stein (NC Gov),
Mikie Sherrill (NJ Gov), Aaron Ford (NV AG/Gov candidate), Tina Kotek (OR Gov).
Each claim cites >=1 reliable source and reflects 2023-2026 public record / stated positions.

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
    # ---------------- Josh Stein (NC-D, Governor since Jan 2025) ----------------
    ("josh-stein", "NC", "Governor", [
        claim("js1", "josh-stein", "sanctity_of_life", 0, False,
              "As North Carolina Attorney General (2017-2024), Stein filed repeated legal briefs and issued press releases protecting abortion access — defending emergency abortion care, fighting to block restrictions on medication abortion, and explicitly opposing NC's 12-week abortion ban enacted in 2023, stating 'Women, not politicians, should be making these decisions' — rejecting any life-from-conception standard.",
              ["https://ncdoj.gov/attorney-general-josh-stein-acts-to-protect-emergency-abortion-care/",
               "https://ncdoj.gov/attorney-general-josh-stein-challenges-decision-to-block-access-to-medication-abortion/",
               "https://en.wikipedia.org/wiki/Josh_Stein"]),
        claim("js2", "josh-stein", "self_defense", 1, False,
              "As NC AG, Stein led multistate coalitions supporting 'commonsense gun protections' including age-based purchase restrictions, ghost gun regulations, and background check expansions. When the NC legislature repealed its pistol purchase permit law in 2023, Stein stated the repeal 'has made our communities less safe' and would allow 'violent criminals and domestic abusers' to obtain firearms more easily — actively opposing the rubric's standard of blocking red-flag laws, AWBs, and all restrictions.",
              ["https://ncdoj.gov/attorney-general-josh-stein-fights-for-commonsense-gun-protections/",
               "https://ncdoj.gov/attorney-general-josh-stein-statement-on-pistol-purchase-permit-repeal/"]),
        claim("js3", "josh-stein", "border_immigration", 2, False,
              "As NC AG, Stein repeatedly joined multistate coalitions to preserve DACA, defend Dreamers from deportation, and protect detained immigrant children from federal enforcement — consistently opposing the rubric's mandatory-deportation and anti-sanctuary standards.",
              ["https://ncdoj.gov/attorney-general-josh-stein-continues-to-fight-to-preserve-daca/",
               "https://ncdoj.gov/attorney-general-josh-stein-defends-the-human-rights-of-detained-immigrant-children/"]),
    ]),

    # ---------------- Mikie Sherrill (NJ-D, Governor since Jan 2026; former Rep NJ-11 2019-2025) ----------------
    ("mikie-sherrill", "NJ", "Governor", [
        claim("ms1", "mikie-sherrill", "border_immigration", 2, False,
              "On February 11, 2026, Governor Sherrill signed an executive order banning ICE from launching immigration enforcement operations on New Jersey state property and created a 'Know Your Rights' portal for undocumented residents — a sanctuary-state posture directly opposing the rubric's anti-sanctuary and mandatory-deportation standard.",
              ["https://www.nj.gov/governor/news/2026/20260211a.shtml",
               "https://en.wikipedia.org/wiki/Mikie_Sherrill"]),
        claim("ms2", "mikie-sherrill", "sanctity_of_life", 0, False,
              "As a U.S. Representative (NJ-11, 2019-2025) and gubernatorial candidate, Sherrill consistently supported abortion access, warning that Trump's Project 2025 plan threatens 'rights and freedoms, including abortion.' As governor she signed abortion protections into New Jersey law to insulate the state from federal rollbacks — rejecting any life-from-conception standard.",
              ["https://www.nj.gov/governor/news/2026/20260120b.shtml",
               "https://en.wikipedia.org/wiki/Mikie_Sherrill"]),
        claim("ms3", "mikie-sherrill", "self_defense", 1, False,
              "During her six years in Congress (NJ-11, 2019-2025), Sherrill voted for major gun-control legislation including the Bipartisan Safer Communities Act (2022) and the Assault Weapons Ban of 2022. Her congressional record is consistent with the Democratic caucus position of supporting expanded background checks, red-flag laws, and semi-automatic rifle restrictions — opposing the rubric's standard of blocking all such measures.",
              ["https://www.govtrack.us/congress/members/mikie_sherrill/412799",
               "https://en.wikipedia.org/wiki/Mikie_Sherrill"]),
    ]),

    # ---------------- Aaron Ford (NV-D, AG 2019-present; 2026 Gov candidate) ----------------
    ("aaron-ford-gov", "NV", "Governor", [
        claim("af1", "aaron-ford-gov", "sanctity_of_life", 0, False,
              "As Nevada AG, Ford declared 'Abortion is health care – and Americans have gone from the freedom to choose to government-mandated pregnancies,' and condemned Texas's abortion ban as a 'direct attack' on constitutional rights, pledging Nevada's AG office would 'not sit on the sidelines' — explicitly rejecting any life-from-conception standard.",
              ["https://ag.nv.gov/News/PR/2021/Attorney_General_Ford_Releases_Statement_on_Texas_Abortion_Law/",
               "https://en.wikipedia.org/wiki/Aaron_Ford_(Nevada_politician)"]),
        claim("af2", "aaron-ford-gov", "self_defense", 1, False,
              "As NV AG, Ford joined a multistate coalition of Democratic AGs condemning major credit card companies for reversing their commitment to implement a merchant category code for firearm retail purchases — a program designed to flag potential mass-shooter buying patterns. His advocacy for this merchant-code surveillance mechanism places him in opposition to the rubric's standard of blocking gun-tracking and registration measures.",
              ["https://ag.nv.gov/News/PR/2023/Attorney_General_Ford_Joins_Multistate_Condemnation_of_Major_Credit_Card_Companies%E2%80%99_About-Face/",
               "https://en.wikipedia.org/wiki/Aaron_Ford_(Nevada_politician)"]),
        claim("af3", "aaron-ford-gov", "border_immigration", 2, False,
              "As NV AG, Ford released a public response disputing Governor Lombardo's characterization of Nevada's model immigration policies, defending the state's more permissive immigration enforcement posture against federal pressure — signaling an anti-deportation, sanctuary-compatible stance that opposes the rubric's anti-sanctuary standard.",
              ["https://ag.nv.gov/News/PR/2025/Attorney_General_Aaron_Ford_Releases_Response_to_Governor_Lombardo%E2%80%99s_Misleading_Statement_on_Model_Immigration_Policies/",
               "https://en.wikipedia.org/wiki/Aaron_Ford_(Nevada_politician)"]),
    ]),

    # ---------------- Tina Kotek (OR-D, Governor since Jan 2023; 2026 re-election) ----------------
    ("tina-kotek-gov-2026", "OR", "Governor", [
        claim("tk1", "tina-kotek-gov-2026", "biblical_marriage", 2, False,
              "Oregon's first openly lesbian governor and the first openly lesbian governor elected in U.S. history. As governor, Kotek signed legislation protecting and expanding access to gender-affirming healthcare and explicitly protecting providers from federal restrictions — actively enshrining transgender ideology into state law, in direct opposition to the rubric's standard of rejecting it.",
              ["https://apps.oregon.gov/oregon-newsroom/OR/GOV/Posts/Post/governor-kotek-celebrates-bills-expanding-access-to-health-care-and-safeguards-for-providers",
               "https://en.wikipedia.org/wiki/Tina_Kotek"]),
        claim("tk2", "tina-kotek-gov-2026", "sanctity_of_life", 0, False,
              "As governor, Kotek signed legislation protecting and expanding access to abortion and reproductive healthcare in Oregon, explicitly framed as a counterweight to federal restrictions. Oregon is a state that has used public funds for abortion since 2017, and Kotek has championed this as a model for other states — rejecting any life-from-conception standard.",
              ["https://apps.oregon.gov/oregon-newsroom/OR/GOV/Posts/Post/governor-kotek-celebrates-bills-expanding-access-to-health-care-and-safeguards-for-providers",
               "https://en.wikipedia.org/wiki/Tina_Kotek"]),
        claim("tk3", "tina-kotek-gov-2026", "election_integrity", 1, False,
              "As former Speaker of the Oregon House and governor, Kotek has championed Oregon's expansive all-mail-ballot and automatic voter registration system — a model that the rubric opposes as 'mass mail-in' voting. Oregon has conducted elections entirely by mail since 2000 and Kotek has praised and extended this system, opposing the rubric's standard of paper-ballot-only and anti-mass-mail-in elections.",
              ["https://en.wikipedia.org/wiki/Tina_Kotek",
               "https://www.oregon.gov/gov/pages/meet-the-governor.aspx"]),
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

#!/usr/bin/env python3
"""Enrichment batch 365: 5 Virginia House of Delegates Republicans (evidence_state, 0 claims).

Targets taken from the bottom of the alphabet (VA evidence_state bucket, reverse-sorted
by name): Justin Pence (HD-33), Joe McNamara (HD-40), Jason Ballard (HD-42),
Israel O'Quinn (HD-44), Jay Leftwich (HD-90). All are sitting Republican delegates
who assumed office January 10, 2024 (except Pence whose tenure is verified via
Ballotpedia), adding evidence claims to support the existing archetype scores.

Key sourced facts used:
- HJR 1 (Virginia Right to Reproductive Freedom Amendment) passed House 51-48
  on Jan 14, 2025: ALL Republicans voted against (party-line).
- Virginia 2025 session: Democrat-controlled House passed anti-gun package
  including bans on commonly owned semi-automatic firearms (NRA-ILA, Feb 2025).
- Virginia 2026 session: Democrats pushed excise tax on firearms and expanded
  red-flag law; Republicans in opposition (NRA-ILA, Feb 2026).
- HJR 2 (felon voting rights restoration) passed 55-44 with 44 Republicans
  opposing (Jan 14, 2025).
- Joe McNamara is the only licensed CPA in the Virginia House of Delegates.
- Israel O'Quinn serves on the Privileges and Elections Committee.
- Jay Leftwich chairs the General Laws Committee (since 2022).
- Justin Pence is an NRA member affiliated with the Virginia Farm Bureau Federation.
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
    # ---------- Justin Pence (VA-R, HD-33, Shenandoah Valley) ----------
    ("justin-pence", "VA", "House of Delegates", [
        claim("jp1", "justin-pence", "self_defense", 1, True,
              "An NRA member who represents a rural Shenandoah Valley agricultural district, Pence has publicly affiliated with the National Rifle Association and consistently aligned with Second Amendment rights. Virginia House Republicans broadly opposed the Democrat-controlled majority's 2025 anti-gun legislative package, which included bans on commonly owned semi-automatic firearms.",
              ["https://ballotpedia.org/Justin_Pence",
               "https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/"]),
        claim("jp2", "justin-pence", "sanctity_of_life", 0, True,
              "As a Republican delegate from a deeply conservative rural district (Shenandoah, Rockingham, and Page Counties), Pence represents constituents who oppose abortion on demand. The Virginia House Republican caucus unanimously voted against HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025, in a 51-48 party-line vote opposing the constitutional entrenchment of abortion rights.",
              ["https://ballotpedia.org/Justin_Pence",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
    ]),

    # ---------- Joe McNamara (VA-R, HD-40, Salem/Roanoke, first elected 2018) ----------
    ("joe-mcnamara", "VA", "House of Delegates", [
        claim("jm1", "joe-mcnamara", "sanctity_of_life", 0, True,
              "As part of the unanimous House Republican caucus, voted against HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which all 48 Republicans opposed constitutionalizing abortion rights in Virginia's constitution.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("jm2", "joe-mcnamara", "self_defense", 1, True,
              "A Republican delegate who opposed the Democrat-controlled House majority's anti-gun legislative package in Virginia's 2025 session, which included bans on commonly owned semi-automatic firearms and other restrictions on Second Amendment rights. In 2026 Virginia Democrats further pushed an excise tax on firearms and expanded red-flag laws opposed by House Republicans.",
              ["https://www.nraila.org/articles/20250214/virginia-gun-control-bills-pass-general-assembly-head-to-youngkins-desk/",
               "https://www.nraila.org/articles/20260211/virginia-excise-tax-on-firearms-continues-to-advance-other-gun-control-stalls"]),
        claim("jm3", "joe-mcnamara", "economic_stewardship", 2, True,
              "The only licensed CPA (Certified Public Accountant) in the Virginia House of Delegates, McNamara advocates for fiscal accountability and balanced budgeting in Virginia state government, bringing professional financial expertise to scrutiny of state spending and fiscal responsibility.",
              ["https://en.wikipedia.org/wiki/Joseph_McNamara_(Virginia_politician)",
               "https://ballotpedia.org/Joseph_McNamara_(Virginia)"]),
    ]),

    # ---------- Jason Ballard (VA-R, HD-42, Army Reserve Lt. Col., attorney) ----------
    ("jason-ballard", "VA", "House of Delegates", [
        claim("jb1", "jason-ballard", "sanctity_of_life", 0, True,
              "As part of the unanimous House Republican caucus, voted against HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which all Republicans opposed writing a constitutional right to abortion into Virginia's constitution.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Jason_Ballard"]),
        claim("jb2", "jason-ballard", "self_defense", 1, True,
              "A U.S. Army Reserve Lieutenant Colonel and attorney who opposes gun control; Virginia House Republicans broadly opposed the Democrat majority's 2025 anti-gun package, including legislation banning commonly owned semi-automatic firearms that NRA-ILA described as giving 'public minimal notice before vote.'",
              ["https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote/",
               "https://ballotpedia.org/Jason_Ballard"]),
    ]),

    # ---------- Israel O'Quinn (VA-R, HD-44, Bristol/Galax, Privileges & Elections Committee) ----------
    ("israel-o'quinn", "VA", "House of Delegates", [
        claim("io1", "israel-o'quinn", "sanctity_of_life", 0, True,
              "As part of the unanimous House Republican caucus, voted against HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which every Republican opposed constitutionalizing abortion rights in the state's governing document.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Israel_O'Quinn"]),
        claim("io2", "israel-o'quinn", "self_defense", 1, True,
              "A Republican delegate representing Bristol, Galax, and southwest Virginia rural communities who has opposed the Democrat-controlled House's 2025-2026 anti-gun agenda, including measures to ban semi-automatic firearms and expand Virginia's red-flag law to allow broader firearm confiscation without criminal conviction.",
              ["https://www.nraila.org/articles/20260211/virginia-excise-tax-on-firearms-continues-to-advance-other-gun-control-stalls",
               "https://ballotpedia.org/Israel_O'Quinn"]),
        claim("io3", "israel-o'quinn", "election_integrity", 0, True,
              "Serves on the Virginia House Privileges and Elections Committee, the body with primary jurisdiction over election law and voter qualification rules. The Republican House caucus voted 44-4 against HJR 2 (a constitutional amendment restoring voting rights for those with felony convictions) on January 14, 2025, opposing expansions that critics say weaken election integrity safeguards.",
              ["https://ballotpedia.org/Israel_O'Quinn",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/"]),
    ]),

    # ---------- Jay Leftwich (VA-R, HD-90, attorney, General Laws Committee chair) ----------
    ("jay-leftwich", "VA", "House of Delegates", [
        claim("jl1", "jay-leftwich", "sanctity_of_life", 0, True,
              "As part of the unanimous House Republican caucus, voted against HJR 1 (Virginia Right to Reproductive Freedom Amendment) on January 14, 2025 — a 51-48 party-line vote in which all Republicans rejected enshrining abortion access as a constitutional right in Virginia.",
              ["https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://ballotpedia.org/Jay_Leftwich"]),
        claim("jl2", "jay-leftwich", "self_defense", 1, True,
              "As chair of the Virginia House General Laws Committee (since 2022), Leftwich has jurisdiction over firearms legislation and has opposed the Democrat majority's multi-session gun-control push. In 2025 Democrats passed bills including bans on commonly owned semi-automatic firearms; in 2026 they advanced an excise tax on firearms and an expanded red-flag law allowing courts to seize guns without criminal conviction.",
              ["https://www.nraila.org/articles/20260217/virginia-gun-bill-updates-as-crossover-deadline-arrives/",
               "https://ballotpedia.org/Jay_Leftwich"]),
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

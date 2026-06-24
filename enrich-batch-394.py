#!/usr/bin/env python3
"""Enrichment batch 394: hand-curated claims for 5 Virginia House of Delegates Republicans.

Archetype_curated federal bucket is fully exhausted. Targets are evidence_state candidates
at the bottom of the alphabet (VA) with 0 claims:
  Hillary Pugh Kent (HD-67), Eric Zehr (HD-51), Eric Phillips (HD-48),
  Ellen McLaughlin (HD-36), Delores Riley Oates (HD-31).

Sources: vavoterguide.com, ericphillipsforva.com, zehrfordelegate.org, LIS Virginia,
Virginia Mercury, WHRO, WVTF, OSV News, ballotpedia.org.

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
    # -------- Hillary Pugh Kent (VA-R, House of Delegates HD-67) --------
    ("hillary-pugh-kent", "VA", "District 67", [
        claim("hpk1", "hillary-pugh-kent", "sanctity_of_life", 0, True,
              "Opposes removing parental consent for minors seeking abortions and supports the Born Alive Infant Protection Act. In January 2025 she was among all 46 House Republicans who voted NO on the Virginia Reproductive Freedom Constitutional Amendment (51–48 party-line vote), rejecting the Democrat-backed proposal to enshrine unlimited abortion access in the state constitution.",
              ["https://www.vavoterguide.com/candidate/house-of-delegates/hillary-pugh-kent/",
               "https://www.osvnews.com/radical-abortion-amendment-passes-virginia-general-assembly-despite-pro-life-advocacy/"]),
        claim("hpk2", "hillary-pugh-kent", "family_child_sovereignty", 0, True,
              "On her official campaign platform, Kent pledges to 'fight to protect parental rights and families,' opposing legislation that would undermine parental authority over children's education and medical decisions.",
              ["https://www.hillarypughkentva.com/about-hillary",
               "https://ballotpedia.org/Hillary_Pugh_Kent"]),
    ]),

    # -------- Eric Zehr (VA-R, House of Delegates HD-51) --------
    ("eric-zehr", "VA", "District 51", [
        claim("ez1", "eric-zehr", "sanctity_of_life", 0, True,
              "On his campaign platform, Zehr affirmed 'the God given right of every American citizen to Life, Liberty, and the Pursuit of Happiness from the instant of conception,' backed the Born Alive Infant Protection Act, and opposed removing parental consent requirements for minors seeking abortions — a fully pro-life record in the Virginia House of Delegates.",
              ["https://www.zehrfordelegate.org/",
               "https://cardinalnews.org/2023/11/08/republican-eric-zehr-trounces-incumbent-del-matt-fariss-in-3-way-race-in-house-district-51/"]),
        claim("ez2", "eric-zehr", "self_defense", 1, True,
              "A committed Second Amendment defender who introduced HB 1230 (2025) permitting trained school board employees to carry firearms on school property and HB 1235 (2025) converting a protective order into a temporary concealed handgun permit. Also championed a resolution supporting Liberty University's campus carry initiative. When House Democrats passed a sweeping 2026 gun control package including an assault-weapon ban, Zehr declared: 'It's just one erosion after another against our Second Amendment. It's that simple.'",
              ["https://lis.virginia.gov/bill-details/20251/HB1235",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("ez3", "eric-zehr", "election_integrity", 0, True,
              "Lists 'integrity of elections' as a core legislative priority; supports in-person Election Day voting with an auditable paper trail and opposes no-excuse mass mail-in voting as a threat to reliable election outcomes.",
              ["https://www.zehrfordelegate.org/",
               "https://ballotpedia.org/Eric_Zehr"]),
    ]),

    # -------- Eric Phillips (VA-R, House of Delegates HD-48) --------
    ("eric-phillips", "VA", "District 48", [
        claim("ep1", "eric-phillips", "sanctity_of_life", 0, True,
              "'A strong Christian active in his church, Eric is unapologetically pro-life. As the father of three children and a new grandfather, Eric believes life is precious and begins at conception,' per his official campaign bio. He voted NO on the Virginia Reproductive Freedom Constitutional Amendment with all House Republicans.",
              ["https://www.ericphillipsforva.com",
               "https://www.osvnews.com/radical-abortion-amendment-passes-virginia-general-assembly-despite-pro-life-advocacy/"]),
        claim("ep2", "eric-phillips", "self_defense", 1, True,
              "A lifelong hunter and strong Second Amendment advocate who 'has supported legislation that expands gun rights across the Commonwealth and defends the rights enshrined in our Constitution,' according to his campaign website. Voted against the sweeping 2026 House Democratic gun control package.",
              ["https://www.ericphillipsforva.com",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("ep3", "eric-phillips", "refuse_state_overreach", 0, True,
              "Believes in 'limiting government intrusion into our daily lives' and opposes unnecessary tax burdens on families, consistently supporting smaller, less intrusive state government in Richmond.",
              ["https://www.ericphillipsforva.com",
               "https://www.vpap.org/legislators/380864-eric-phillips/"]),
    ]),

    # -------- Ellen McLaughlin (VA-R, House of Delegates HD-36) --------
    ("ellen-mclaughlin", "VA", "District 36", [
        claim("em1", "ellen-mclaughlin", "sanctity_of_life", 0, True,
              "Voted NO on the Virginia Reproductive Freedom Constitutional Amendment in January 2025 alongside all 46 House Republicans (51–48 partisan vote), rejecting the Democrat-backed proposal to enshrine an unlimited right to abortion in the Virginia constitution. The 2026 second-session vote also passed along party lines (64–34) with all Republicans opposed.",
              ["https://www.osvnews.com/radical-abortion-amendment-passes-virginia-general-assembly-despite-pro-life-advocacy/",
               "https://www.whro.org/health/2026-02-13/a-constitutional-amendment-on-reproductive-rights-is-headed-to-virginias-ballot-heres-what-it-would-do"]),
        claim("em2", "ellen-mclaughlin", "self_defense", 1, True,
              "Voted with all House Republicans against the sweeping gun control package passed by House Democrats in February 2026, which included a ban on the sale of assault-style weapons, large-capacity magazine restrictions, and penalties for visible handguns in unattended vehicles.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.whro.org/virginia-government/2026-02-06/house-democrats-pass-sweeping-gun-control-package-over-gop-objections"]),
    ]),

    # -------- Delores Riley Oates (VA-R, House of Delegates HD-31) --------
    ("delores-riley-oates", "VA", "District 31", [
        claim("dro1", "delores-riley-oates", "biblical_marriage", 2, True,
              "In January 2025, Oates introduced HB 1809 to ban biological males from competing on female school sports teams, requiring all school athletic teams to be designated male, female, or coed, with a doctor's note verifying biological sex for anyone seeking to participate in sex-designated competition. Governor Glenn Youngkin, Attorney General Jason Miyares, and Lt. Governor Winsome Earle Sears publicly backed the bill.",
              ["https://www.whro.org/virginia-government/2025-01-16/virginia-republicans-back-additional-regulations-for-transgender-student-athletes",
               "https://www.wvtf.org/news/2025-01-15/virginia-republicans-back-additional-regulations-for-transgender-student-athletes"]),
        claim("dro2", "delores-riley-oates", "sanctity_of_life", 0, True,
              "Voted NO on the Virginia Reproductive Freedom Constitutional Amendment in January 2025, standing with all 46 House Republicans against the Democrat-backed measure to write unlimited abortion access into the state constitution (51–48 party-line vote).",
              ["https://www.osvnews.com/radical-abortion-amendment-passes-virginia-general-assembly-despite-pro-life-advocacy/",
               "https://www.whro.org/health/2026-02-13/a-constitutional-amendment-on-reproductive-rights-is-headed-to-virginias-ballot-heres-what-it-would-do"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

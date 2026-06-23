#!/usr/bin/env python3
"""Enrichment batch 388: hand-curated claims for 5 Virginia state officials.

Targets evidence_state officials with 0 claims from Virginia (VA), continuing
the bottom-of-alphabet state sweep after WA/WI (batch 387).

Officials: Jay Jones (VA AG), Don Scott (VA Speaker HD-88),
Chris Head (VA State Senate SD-3), Hillary Pugh Kent (VA HD-67),
Eric Phillips (VA HD-48).

Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Jay Jones (VA, Attorney General) ----------------
    ("jay-jones", "VA", "Attorney", [
        claim("jj1", "jay-jones", "sanctity_of_life", 4, False,
              "Served on the Virginia Planned Parenthood Board of Directors before becoming Attorney General, and on Day One in office (January 17, 2026) joined lawsuits to protect federal Medicaid reimbursements for Planned Parenthood services — placing him squarely inside the abortion-industry network the rubric identifies as disqualifying.",
              ["https://www.oag.state.va.us/media-center/news-releases/2948-january-17th-2026-attorney-general-jones-announces-day-one-actions-to-keep-virginians-safe-lower-costs-and-protect-fundamental-rights",
               "https://virginiaindependentnews.com/elections/jay-jones-promises-to-protect-reproductive-rights-if-elected-virginias-attorney-general/"]),
        claim("jj2", "jay-jones", "border_immigration", 4, False,
              "In February 2026 argued before the U.S. Supreme Court to defend birthright citizenship against President Trump's executive order restricting it — directly opposing the rubric's call for the government to end automatic birthright citizenship as an immigration-enforcement tool.",
              ["https://www.oag.state.va.us/media-center/news-releases/2967-attorney-general-jay-jones-defends-birthright-citizenship-at-u-s-supreme-court",
               "https://www.13newsnow.com/article/news/local/virginia/virginia-ag-jay-jones-coalition-defending-birthright-citizenship-supreme-court-case/291-8e9b5ef1-e212-4e8f-8e45-8065bd0b3c95"]),
        claim("jj3", "jay-jones", "self_defense", 1, False,
              "As Attorney General-elect, sought to extend the deadline for filing a notice of appeal in a Virginia gun-law case so that he could assess and potentially defend state firearm restrictions upon taking office, and previously described fighting 'the gun lobby to keep families safe' as a career priority — signaling intent to use the AG office to uphold gun-control measures rather than oppose them.",
              ["https://wset.com/news/local/attorney-general-elect-jay-jones-seeks-extension-in-virginia-gun-law-appeal-background-checks-december-2025",
               "https://www.jayjones.com/meet-jay/"]),
    ]),

    # ---------------- Don Scott (VA, Speaker HD-88) ----------------
    ("don-scott", "VA", "Speaker", [
        claim("ds1", "don-scott", "sanctity_of_life", 0, False,
              "As Speaker of the Virginia House of Delegates, stewarded HJR 1 — the constitutional amendment establishing a fundamental right to abortion ('reproductive freedom') — through the House in back-to-back sessions: 51-48 in January 2025 and 64-34 in January 2026, fulfilling the two-session requirement to place the amendment on the 2026 ballot.",
              ["https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/",
               "https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality"]),
        claim("ds2", "don-scott", "biblical_marriage", 1, False,
              "As Speaker, led the House to pass HJR 9 — the constitutional amendment adding same-sex marriage protections to the Virginia Constitution — by 58-35 in 2025 and again in 2026, advancing both sessions of the two-session requirement to send the measure to voters; he is the first Black Speaker in Virginia history and has championed the full Democratic social agenda.",
              ["https://www.vpm.org/news/2025-01-15/virginia-house-abortion-voting-rights-marriage-equality",
               "https://news.ballotpedia.org/2025/01/27/virginias-two-session-rule-for-constitutional-amendment-house-of-delegates-election-could-affect-the-future-of-proposed-amendments-on-abortion-marriage-and-voting/"]),
        claim("ds3", "don-scott", "self_defense", 1, False,
              "Led the House of Delegates in passing HB 21, Virginia's sweeping assault-weapons ban, 62-35 in February 2026 over unanimous Republican opposition; the bill prohibits the future sale, manufacture, and import of semiautomatic centerfire rifles and pistols that accept magazines over 15 rounds, and was subsequently signed by Governor Spanberger in May 2026.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://virginiamercury.com/2026/05/15/spanberger-signs-assault-weapons-ban-package-of-criminal-justice-and-energy-bills/"]),
    ]),

    # ---------------- Chris Head (VA, State Senate SD-3) ----------------
    ("chris-head", "VA", "Senate", [
        claim("ch1", "chris-head", "sanctity_of_life", 0, True,
              "Voted against SJR 247, the Virginia constitutional amendment establishing a state right to 'reproductive freedom' (abortion), in the January 21, 2025 Senate floor vote — one of 18 Republican senators who unanimously rejected the measure on a 21-18 party-line vote, protecting unborn life against constitutionalization of abortion access.",
              ["https://lis.virginia.gov/bill-details/20251/SJ247",
               "https://www.vpm.org/news/2025-01-20/virginia-constitutional-amendments-abortion-marriage-equality-voting-rights"]),
        claim("ch2", "chris-head", "self_defense", 1, True,
              "Voted against the Democrats' 2026 gun-control package in the Virginia Senate — a set of bills that included an assault-weapons ban (prohibiting the future sale of semiautomatic centerfire rifles and pistols accepting magazines over 15 rounds) and universal-background-check expansion, which Republicans in both chambers unanimously opposed and the NRA pledged to challenge in court.",
              ["https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk",
               "https://virginiamercury.com/2026/04/14/spanberger-amends-signs-sweeping-gun-legislation-reshaping-virginias-firearm-laws/"]),
    ]),

    # ---------------- Hillary Pugh Kent (VA, HD-67) ----------------
    ("hillary-pugh-kent", "VA", "District 67", [
        claim("hpk1", "hillary-pugh-kent", "sanctity_of_life", 0, True,
              "Voted against HJR 1 — the Virginia constitutional amendment establishing a fundamental right to abortion — in the January 14, 2025 House floor vote (51-48 party-line, all 48 Republicans opposed) and again in the January 15, 2026 repeat passage (64-34), consistently opposing the constitutionalization of abortion access across both required sessions.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/"]),
        claim("hpk2", "hillary-pugh-kent", "self_defense", 1, True,
              "Voted against HB 21 and the Democrats' 2026 gun-control package in the Virginia House — including the assault-weapons ban that passed 62-35 over unanimous Republican objection — defending law-abiding Virginians' right to own commonly used semiautomatic firearms against a ban the NRA has pledged to fight in court.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260315/virginia-legislature-adjourns-from-2026-session-anti-gun-bills-on-governors-desk"]),
    ]),

    # ---------------- Eric Phillips (VA, HD-48) ----------------
    ("eric-phillips", "VA", "District 48", [
        claim("ep1", "eric-phillips", "sanctity_of_life", 0, True,
              "Voted against HJR 1 — the Virginia constitutional amendment codifying abortion as a fundamental right — on January 14, 2025 (51-48 party-line, all Republicans opposed) and in the 2026 repeat passage (64-34); Phillips, a Republican small-business owner first elected in a January 2024 special election, has consistently stood against Democrat-led abortion-expansion efforts.",
              ["https://lis.virginia.gov/bill-details/20251/HJ1",
               "https://cardinalnews.org/2026/01/15/house-of-delegates-passes-four-constitutional-amendments-on-the-first-day-of-the-2026-general-assembly-session/"]),
        claim("ep2", "eric-phillips", "self_defense", 1, True,
              "Voted against HB 21 and the 2026 Virginia gun-control package — including the assault-weapons ban (62-35, all Republicans opposed) that bans future sales of semiautomatic rifles and pistols accepting magazines over 15 rounds — aligning with Virginia gun-rights groups that are mounting a legal challenge to the laws.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.insurancejournal.com/news/east/2026/06/23/874887.htm"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

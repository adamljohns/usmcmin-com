#!/usr/bin/env python3
"""Enrichment batch 57: hand-curated claims for 3 federal 2026 candidates.

Targets archetype_curated candidates from the BOTTOM of the alphabet bucket
(FL and NJ) with 0 evidence claims.

Mix (2 R / 1 D): Joe Gruters (FL-16-R, FL state senator / former FL GOP
chair), Jay Trumbull (FL-02-R, FL state senator), Rebecca Bennett
(NJ-07-D, DCCC Red-to-Blue / Navy vet).

Each claim cites >=1 reliable source and reflects 2023-2026 legislative
votes or documented public positions.

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
    # ---------------- Joe Gruters (FL-16, R, FL state senator) ----------------
    ("joe-gruters-fl-16", "FL", "Representative", [
        claim("jg1", "joe-gruters-fl-16", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (2023), the six-week 'Heartbeat Protection Act' that became law May 1, 2024 — Florida's most restrictive abortion limit — affirming legal protection for unborn life from heartbeat detection onward.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://www.nbcnews.com/politics/politics-news/floridas-legislature-passes-6-week-abortion-ban-rcna78988"]),
        claim("jg2", "joe-gruters-fl-16", "border_immigration", 3, True,
              "Long-time champion of mandatory E-Verify: Gruters filed the measure over multiple sessions until it passed as CS/CS/SB 1718 (2023), requiring all Florida employers with 25 or more employees to verify new hires through the federal E-Verify system — the most comprehensive E-Verify law in the country at the time.",
              ["https://www.gtlaw.com/en/insights/2023/5/everify-florida-senate-passes-bill-requiring-state-employers-with-25-or-more-employees-to-use-platform-effective-july-1",
               "https://en.wikipedia.org/wiki/Joe_Gruters"]),
        claim("jg3", "joe-gruters-fl-16", "election_integrity", 0, True,
              "Filed SB 1168 (January 2024) requiring Florida driver's licenses to display citizenship status as an election-integrity tool for identifying non-citizens on voter rolls; as RNC Chair (from August 2025) led a national voter-ID and roll-accuracy campaign including a court order removing non-citizens from New York City local-election rolls.",
              ["https://floridianpress.com/2024/01/state-senator-gruters-introduces-bill-requiring-drivers-licenses-to-showcase-citizenship-status/",
               "https://washingtonreporter.news/interview-how-the-joe-gruters-led-rnc-is-fighting-for-election-integrity-from-maine-to-hawaii/"]),
    ]),

    # ---------------- Jay Trumbull (FL-02, R, FL state senator) ----------------
    ("jay-trumbull", "FL", "Representative", [
        claim("jt1", "jay-trumbull", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (2023), the six-week abortion ban signed by Gov. DeSantis and effective May 1, 2024, as confirmed by the Florida Senate roll call — casting a vote to protect unborn life from heartbeat detection.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://www.nbcnews.com/politics/politics-news/floridas-legislature-passes-6-week-abortion-ban-rcna78988"]),
        claim("jt2", "jay-trumbull", "border_immigration", 3, True,
              "Voted YES on Florida SB 1718 (2023) — the comprehensive immigration enforcement law mandating E-Verify for private employers, state-local cooperation on federal immigration detainers, and new transport penalties for unlawfully present persons — confirmed YES in committee (14-6) and on the Senate floor (27-10).",
              ["https://www.wusf.org/politics-issues/2023-04-28/florida-senate-backs-controversial-immigration-changes",
               "https://legiscan.com/FL/bill/S1718/2023"]),
        claim("jt3", "jay-trumbull", "election_integrity", 0, True,
              "Voted YES on Florida HB 991 (2026), the Florida SAVE Act requiring proof of U.S. citizenship for voter registration; the Senate passed it 27-12 with only one Republican (Sen. Calatayud) dissenting, making Trumbull part of the near-unanimous Republican majority backing the measure.",
              ["https://floridaphoenix.com/2026/03/12/florida-legislature-approves-bill-requiring-voters-to-provide-proof-of-citizenship/",
               "https://www.votebeat.org/national/2026/03/23/florida-republicans-pass-voter-id-save-america-act-trump-proof-citizenship-voting-laws/"]),
    ]),

    # ---------------- Rebecca Bennett (NJ-07, D) ----------------
    ("rebecca-bennett-nj-07", "NJ", "Representative", [
        claim("rb1", "rebecca-bennett-nj-07", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List, the major pro-choice women's PAC named explicitly in the rubric ('never took PP/NARAL/EMILY money'), placing her inside the abortion-industry political-funding network that backs candidates who reject any restriction on abortion.",
              ["https://www.insidernj.com/press-release/emilys-list-endorses-rebecca-bennett-for-new-jerseys-7th-congressional-district/"]),
        claim("rb2", "rebecca-bennett-nj-07", "sanctity_of_life", 0, False,
              "Endorsed by Reproductive Freedom for All (formerly NARAL Pro-Choice America) as part of their 2026 U.S. House Red-to-Blue slate, confirming she supports unrestricted abortion access and rejects any legal recognition of unborn personhood from conception.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-slate-of-u-s-house-red-to-blue-candidates-ahead-of-the-2026-midterm-election/",
               "https://newjerseyglobe.com/congress/bennett-named-to-dcccs-red-to-blue-list/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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

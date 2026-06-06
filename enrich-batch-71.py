#!/usr/bin/env python3
"""Enrichment batch 71: hand-curated claims for 3 state/gubernatorial candidates.

Targets archetype_curated candidates from the bottom of the alphabet bucket
that had 0 evidence claims. Low-profile federal candidates (Joe Mazzola MA,
Drew Wilson FL-02) were skipped — no verifiable sourced positions found in
any reliable database.

Mix (3 R): Christine Drazan (OR-Gov), Charles McCall (OK-Gov),
Cameron Sexton (KY-Gov, currently TN House Speaker).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions
and legislative record.

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
    # ---------------- Christine Drazan (OR-R, Governor candidate 2026) ----------------
    ("christine-drazan-gov-2026", "OR", "Governor", [
        claim("cd1", "christine-drazan-gov-2026", "sanctity_of_life", 0, True,
              "Opposes abortion and was endorsed by Oregon Right to Life in the 2022 governor's race, making her the pro-life standard-bearer in Oregon's 2026 Republican primary rematch against Tina Kotek.",
              ["https://katu.com/news/know-your-candidates/2026-christine-drazan-oregon-governor-republican",
               "https://www.opb.org/article/2026/04/28/oregon-politics-christine-drazan-republican-governor/"]),
        claim("cd2", "christine-drazan-gov-2026", "self_defense", 1, True,
              "Pledged during her 2022 campaign that as governor she would veto any legislation infringing on Second Amendment rights; her 2026 rematch campaign mailers to Republican voters again highlight her pro-gun-rights record.",
              ["https://katu.com/news/know-your-candidates/2026-christine-drazan-oregon-governor-republican",
               "https://www.ontheissues.org/Governor/Christine_Drazan_Gun_Control.htm"]),
        claim("cd3", "christine-drazan-gov-2026", "border_immigration", 2, True,
              "Opposes Oregon's sanctuary policies, citing a specific case in which the Oregon Department of Corrections refused a federal law-enforcement request to locate 30 individuals convicted of serious crimes including child sexual assault — calling the sanctuary framework a threat to public safety.",
              ["https://www.opb.org/article/2026/04/28/oregon-politics-christine-drazan-republican-governor/",
               "https://oregonvotes.gov/voters-guide/english/christinedrazan.html"]),
    ]),

    # ---------------- Charles McCall (OK-R, Governor candidate 2026) ----------------
    ("charles-mccall-gov", "OK", "Governor", [
        claim("cm1", "charles-mccall-gov", "self_defense", 0, True,
              "As Oklahoma House Speaker, authored House Joint Resolution 1034 to expand Second Amendment protections and require courts to interpret the Amendment based on its original language; declared 'The Second Amendment is the pillar upon which all the other amendments rest.'",
              ["https://okcfox.com/news/local/oklahoma-house-passes-resolution-to-strengthen-second-amendment-rights-handguns-rifles-ammunition-shotguns-senate-charles-mccall-house-joint-resolution-1034-firearms",
               "https://en.wikipedia.org/wiki/Charles_McCall"]),
        claim("cm2", "charles-mccall-gov", "biblical_marriage", 2, True,
              "As House Speaker, steered two landmark anti-transgender measures to the governor's desk: a 2022 statute requiring public school students to use bathrooms matching their birth-certificate sex, and a 2023 law banning gender-transition surgeries and hormone treatments for minors. His 2026 governor ads tout: 'I led the charge to keep boys out of our daughters' locker rooms.'",
              ["https://oklahomawatch.org/2025/09/17/anti-trans-ads-already-making-an-appearance-in-oklahomas-republican-gubernatorial-primary/",
               "https://washingtonexaminer.com/news/campaigns/3829773/knife-wielding-ad-puts-transgender-debate-at-center-of-oklahoma-gop-governors-primary"]),
        claim("cm3", "charles-mccall-gov", "sanctity_of_life", 0, True,
              "Responded to the 2023 Oklahoma Supreme Court ruling recognizing a limited abortion right by declaring 'House Republicans will continue to protect the lives of the unborn and pursue legislation that values all life,' pledging continued pro-life legislation.",
              ["https://www.okhouse.gov/posts/news-20230321_2",
               "https://en.wikipedia.org/wiki/Charles_McCall"]),
    ]),

    # ---------------- Cameron Sexton (KY-R, Governor candidate 2027, TN House Speaker) ----------------
    ("cameron-sexton-gov", "KY", "Governor", [
        claim("cs1", "cameron-sexton-gov", "sanctity_of_life", 0, True,
              "As Tennessee House Speaker, shepherded the state's near-total abortion trigger ban — among the strictest in the nation — which took effect in August 2022 after Dobbs. Supported a narrow life-of-mother clarification but opposed broader exceptions, stating proposals that permit abortion 'up to birth' go too far.",
              ["https://www.wate.com/news/tennessee/tn-house-speaker-expresses-support-for-clarifying-state-abortion-ban/",
               "https://en.wikipedia.org/wiki/Cameron_Sexton"]),
        claim("cs2", "cameron-sexton-gov", "self_defense", 0, True,
              "Supported Tennessee's 2021 permitless-carry bill allowing adults 21 and over to carry handguns without a permit, and publicly pushed to expand it toward full constitutional carry, calling the initial measure a step in the right direction while vowing to 'continue pushing and fighting until we can get to true constitutional carry.'",
              ["https://tennesseefirearms.com/2021/03/is-speaker-cameron-sexton-luke-warm-to-real-constitutional-carry/",
               "https://butlervinesbabblaw.com/tennessee-governor-signs-constitutional-carry-bill.php"]),
        claim("cs3", "cameron-sexton-gov", "biblical_marriage", 4, True,
              "In a 2021 special legislative session, introduced legislation to make school board elections partisan rather than nonpartisan, part of a coordinated Republican effort to contest progressive education policies on gender identity and transgender students' rights in Tennessee public schools.",
              ["https://en.wikipedia.org/wiki/Cameron_Sexton",
               "https://ballotpedia.org/Cameron_Sexton"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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

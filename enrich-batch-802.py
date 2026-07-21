#!/usr/bin/env python3
"""Enrichment batch 802: 5 bottom-of-alphabet state executives (WY + WV).

Targets: Chuck Gray (WY SOS), Keith Kautz (WY AG), Mark Hunt (WV Auditor),
Larry Pack (WV Treasurer), Kent Leonhardt (WV Ag Commissioner).
All are evidence_curated with 2-3 existing claims; this batch adds 9 new
claims spanning election_integrity, sanctity_of_life, border_immigration,
economic_stewardship, refuse_federal_overreach, and industry_capture.

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
    # ------------ Chuck Gray (WY-R, Secretary of State) ------------
    ("chuck-gray", "WY", "Secretary of State", [
        claim("cg-b802-1", "chuck-gray", "election_integrity", 1, True,
              "Championed HB 156 (signed 2025), making Wyoming the first state to require documentary proof of citizenship AND residency for voter registration in all elections; Gray called the measure his 'number one priority' and personally presented the new requirements at a national election officials conference.",
              ["https://sos.wyo.gov/Media/2025/SoS_Release_2025-04-10.pdf",
               "https://www.wyomingnews.com/news/local_news/secretary-of-state-chuck-gray-presents-wyomings-new-voting-requirements-at-national-conference/article_0aec9365-450e-4907-b27a-189bcfa42520.html"]),
        claim("cg-b802-2", "chuck-gray", "election_integrity", 3, True,
              "As part of his 15-bill 2026 election-reform package, Gray proposed requiring pen-and-paper ballots as Wyoming's default voting method, arguing paper ballots provide greater security, auditability, and public confidence in election results.",
              ["https://www.wyomingnews.com/laramieboomerang/laramieboomerang/news/secretary-gray-calls-for-15-more-election-reform-bills-this-year/article_f103dae1-fbcb-4c10-a025-c5808e69fa69.html"]),
    ]),

    # ------------ Keith Kautz (WY-R, Attorney General, appointed) ------------
    ("keith-kautz", "WY", "Attorney General", [
        claim("kk-b802-1", "keith-kautz", "sanctity_of_life", 0, True,
              "In April 2026 Kautz personally argued before Natrona County District Court to uphold Wyoming's Human Heartbeat Act, telling the judge 'That's when we know there is life to protect' — a rare instance of an Attorney General personally appearing in court to defend a state abortion restriction.",
              ["https://wyofile.com/judge-mulls-whether-to-halt-wyomings-heartbeat-abortion-restrictions-amid-legal-challenge/"]),
        claim("kk-b802-2", "keith-kautz", "border_immigration", 2, True,
              "As Wyoming's chief state law enforcement officer, Kautz operates within and publicly supports Wyoming's formal 287(g) agreement with ICE — signed under Governor Gordon — authorizing Wyoming Highway Patrol troopers to carry out federal immigration enforcement, making Wyoming an active anti-sanctuary partner in border security.",
              ["https://www.foxnews.com/politics/gop-governor-greenlights-state-troopers-join-ice-immigration-crackdown"]),
    ]),

    # ------------ Mark Hunt (WV-R, State Auditor) ------------
    ("mark-hunt", "WV", "State Auditor", [
        claim("mh-b802-1", "mark-hunt", "economic_stewardship", 2, True,
              "In his first year in office, Hunt renegotiated West Virginia's OpenGov government-transparency software contract, cutting the annual cost from over $4 million to approximately $1.5 million — saving WV taxpayers $2.5 million per year through targeted fiscal oversight of state vendor contracts.",
              ["https://www.wsaz.com/2025/08/19/west-virginia-state-auditor-touts-re-negotiated-contract-with-opengov/"]),
    ]),

    # ------------ Larry Pack (WV-R, State Treasurer) ------------
    ("larry-pack", "WV", "State Treasurer", [
        claim("lp-b802-1", "larry-pack", "economic_stewardship", 2, True,
              "Ran on an explicit fiscal-discipline platform: 'The state government should live within its means and not spend more money than it has,' and pledged as treasurer to ensure public pension funds are invested 'wisely and responsibly' — rejecting deficit spending and reckless investment strategies.",
              ["https://ballotpedia.org/Larry_Pack_(West_Virginia)",
               "https://www.theintelligencer.net/news/top-headlines/2023/08/republican-larry-pack-to-run-for-west-virginia-treasurer/"]),
        claim("lp-b802-2", "larry-pack", "economic_stewardship", 4, True,
              "In February 2025 Pack proposed and won approval from the WV Board of Treasury Investments to prohibit short-term fund investments in Chinese-owned companies, and separately proposed full divestment of Chinese companies from all state long-term investment boards, citing national security and China's adversarial posture toward West Virginia's interests.",
              ["https://wvtreasury.gov/About/Press-Releases/details/treasurer-pack-applauds-wvbti-for-approving-policy-to-prohibit-short-term-funds-from-chinese-owned-companies",
               "https://wvtreasury.gov/About/Press-Releases/details/treasurer-pack-to-propose-divestment-of-chinese-owned-companies-in-west-virginia-investment-boards"]),
    ]),

    # ------------ Kent Leonhardt (WV-R, Commissioner of Agriculture) ------------
    ("kent-leonhardt", "WV", "Commissioner", [
        claim("kl-b802-1", "kent-leonhardt", "refuse_federal_overreach", 1, True,
              "Publicly documented USDA federal interference with West Virginia's micro dairy rule before the state could implement it, stating 'the USDA put a stop to that, prior to us implementing our rule' — a direct case of federal overreach that Leonhardt navigated around to eventually restore small-farm dairy access.",
              ["https://www.wvpublic.org/government/2020-10-20/w-va-s-department-of-agriculture-race-supporting-the-small-farm"]),
        claim("kl-b802-2", "kent-leonhardt", "industry_capture", 2, True,
              "Explicitly reoriented the WV Department of Agriculture from what he called a 'heavy-handed regulatory agency' to an 'educate-before-regulate agency,' stating that government's role is to 'encourage a free market' rather than destroy small farm businesses with 'lawsuits and burdensome regulations.'",
              ["https://www.wvpublic.org/government/2020-10-20/w-va-s-department-of-agriculture-race-supporting-the-small-farm",
               "https://www.kentforwv.com/issues"]),
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

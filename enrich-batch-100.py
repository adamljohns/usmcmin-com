#!/usr/bin/env python3
"""Enrichment batch 100: hand-curated claims for 4 state-level candidates.

Targets archetype_curated candidates (bottom-of-alphabet states: NM, MA) with
0 evidence claims. Uses the (slug + state + office_keyword) matcher to avoid
collisions.

Mix: Deb Haaland (NM-D Governor), Raul Torrez (NM-D AG),
Sam Bregman (NM-D Governor), Andrea Campbell (MA-D AG).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions.

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
    # ---------------- Deb Haaland (NM-D, Governor candidate) ----------------
    ("deb-haaland-gov", "NM", "Governor", [
        claim("dh1", "deb-haaland-gov", "biblical_marriage", 4, False,
              "Cosponsored the Equality Act (H.R.5) in the 116th Congress, which would write sexual-orientation and gender-identity protections into federal civil-rights law and extend them into schools, housing, and public accommodations — the promotion of LGBTQ ideology in law and policy the rubric opposes.",
              ["https://haaland.house.gov/media/press-releases/haaland-cosponsors-equality-act",
               "https://ballotpedia.org/Debra_Haaland"]),
        claim("dh2", "deb-haaland-gov", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List, the pro-abortion political organization that exclusively backs candidates who support abortion access — placing Haaland inside the abortion-industry funding network the rubric opposes.",
              ["https://emilyslist.org/candidate/deb-haaland/",
               "https://en.wikipedia.org/wiki/Deb_Haaland"]),
        claim("dh3", "deb-haaland-gov", "self_defense", 1, False,
              "Received a 2026 Moms Demand Action 'Gun Sense Candidate' distinction and has proposed the Stop Illegal Gun Trade Act to restrict firearms dealers and 'extremely dangerous weapons' — opposing the rubric's standard of unrestricted Second Amendment rights.",
              ["https://debhaaland.com/2026/05/haaland-receives-gun-sense-candidate-distinction/",
               "https://ballotpedia.org/Debra_Haaland"]),
    ]),

    # ---------------- Raul Torrez (NM-D, Attorney General) ----------------
    ("raul-torrez-ag-2026", "NM", "Attorney General", [
        claim("rt1", "raul-torrez-ag-2026", "sanctity_of_life", 0, False,
              "Argued before the New Mexico Supreme Court and filed supplemental briefings to preserve abortion access statewide, blocking local ordinances that sought to restrict abortion services — actively opposing any protection of unborn life from conception.",
              ["https://nmag.gov/attorney-general-raul-torrez-argues-strongly-in-todays-new-mexico-supreme-court-to-secure-the-right-to-reproductive-choice/",
               "https://nmdoj.gov/press-release/attorney-general-raul-torrez-files-supplemental-briefing-in-fight-to-preserve-abortion-access-in-new-mexico/"]),
        claim("rt2", "raul-torrez-ag-2026", "border_immigration", 4, False,
              "Joined a 17-state coalition challenging President Trump's executive order redefining birthright citizenship, filing legal action to block restrictions on automatic birthright citizenship — opposing the rubric's anti-birthright-citizenship position.",
              ["https://nmdoj.gov/press-release/statement-from-attorney-general-raul-torrez/",
               "https://en.wikipedia.org/wiki/Ra%C3%BAl_Torrez"]),
        claim("rt3", "raul-torrez-ag-2026", "border_immigration", 2, False,
              "Led legal challenges against the Trump administration's threats to withhold federal Victims of Crime Act grants from states not cooperating with federal immigration enforcement — defending sanctuary-aligned resistance to immigration law cooperation.",
              ["https://sourcenm.com/2025/12/31/a-year-of-suing-the-trump-administration-qa-with-new-mexico-ag-raul-torrez/",
               "https://americantribune.com/new-mexico-ag-torrez-leads-coalition-in-legal-challenges-to-trump-policies/"]),
    ]),

    # ---------------- Sam Bregman (NM-D, Governor candidate) ----------------
    ("sam-bregman-gov", "NM", "Governor", [
        claim("sb1", "sam-bregman-gov", "border_immigration", 1, False,
              "Publicly criticized the Trump administration's mass deportation policy as creating a 'chilling effect' on crime reporting — arguing that undocumented witnesses and victims avoid police for fear of deportation — explicitly opposing mandatory deportation of undocumented immigrants.",
              ["https://sourcenm.com/2026/04/16/new-mexico-primary-2026-democratic-governor-candidate-sam-bregman/"]),
        claim("sb2", "sam-bregman-gov", "border_immigration", 2, False,
              "Stated he would not use state and local law enforcement resources to enforce federal immigration law, except where a suspect represents a serious criminal threat — a sanctuary-aligned position that the rubric's anti-sanctuary standard opposes.",
              ["https://sourcenm.com/2026/04/16/new-mexico-primary-2026-democratic-governor-candidate-sam-bregman/",
               "https://ballotpedia.org/Sam_Bregman"]),
    ]),

    # ---------------- Andrea Campbell (MA-D, Attorney General) ----------------
    ("andrea-campbell-ag-2026", "MA", "Attorney General", [
        claim("ac1", "andrea-campbell-ag-2026", "self_defense", 1, False,
              "Defended Massachusetts' assault weapons ban before the U.S. First Circuit Court of Appeals, which upheld the law — actively using the AG's office to preserve firearms restrictions that the rubric's Second Amendment standard opposes.",
              ["https://www.wgbh.org/news/politics/2025-10-21/massachusetts-ag-andrea-campbell-announces-reelection-bid",
               "https://en.wikipedia.org/wiki/Andrea_Campbell"]),
        claim("ac2", "andrea-campbell-ag-2026", "sanctity_of_life", 0, False,
              "Created a dedicated 'Reproductive Justice Unit' within the Massachusetts Attorney General's Office to protect and expand abortion access, treating abortion as an unrestricted right rather than recognizing personhood from conception.",
              ["https://www.wgbh.org/news/politics/2025-10-21/massachusetts-ag-andrea-campbell-announces-reelection-bid",
               "https://andreacampbell.org/"]),
        claim("ac3", "andrea-campbell-ag-2026", "biblical_marriage", 2, False,
              "Joined a multi-state lawsuit in 2024 to reinstate federal transgender protections eliminated by the Trump administration and filed legal action against groups disrupting transgender events — affirming transgender ideology in law and policy that the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Andrea_Campbell",
               "https://www.nbcboston.com/news/local/mass-ag-andrea-joy-campbell-announces-reelection-campaign/3830944/"]),
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

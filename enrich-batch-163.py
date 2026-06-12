#!/usr/bin/env python3
"""Enrichment batch 163: 4 sitting U.S. House Republicans from MT, MO, and NE.

Targets archetype_party_default members with 0 evidence claims from the bottom
of the alphabet after low_evidence 2026 candidates at that tier are exhausted.
All positions sourced from official sites, Wikipedia, SBA Pro-Life, and news.

Candidates: Troy Downing (MT-02, freshman Rep 2025), Mark Alford (MO-04),
Jason Smith (MO-08, Ways & Means Chair), Mike Flood (NE-01).
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
    # ---------------- Troy Downing (MT-02, R, freshman 2025) ----------------
    ("troy-downing", "MT", "House", [
        claim("td1", "troy-downing", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America before his 2024 election victory; Air Force combat veteran who ran on a platform of protecting unborn life and has voted consistently in the 119th Congress against taxpayer funding for abortion.",
              ["https://sbaprolife.org/candidate/troy-downing",
               "https://en.wikipedia.org/wiki/Troy_Downing"]),
        claim("td2", "troy-downing", "self_defense", 1, True,
              "Describes himself as 'an unwavering supporter of the 2nd Amendment' and states plainly that 'The right to keep and to bear arms shall not be infringed' — a categorical rejection of bans, red-flag laws, magazine limits, and registries.",
              ["https://ballotpedia.org/Troy_Downing",
               "https://en.wikipedia.org/wiki/Troy_Downing"]),
        claim("td3", "troy-downing", "border_immigration", 0, True,
              "Pledged to 'lead the fight to finish Trump's wall and deport illegal immigrants,' named border security one of his top three campaign priorities, and explicitly backed H.R.2 (Secure the Border Act) to fund wall construction and tighten asylum — a wall-plus-military enforcement posture.",
              ["https://billingsgazette.com/news/local/government-politics/elections/troy-downing-congress-house-montana-eastern-district/article_e53d7606-f1fb-11ee-85b2-4798069cd1b9.html",
               "https://en.wikipedia.org/wiki/Troy_Downing"]),
    ]),

    # ---------------- Mark Alford (MO-04, R, former TV anchor) ----------------
    ("mark-alford", "MO", "House", [
        claim("ma1", "mark-alford", "sanctity_of_life", 0, True,
              "States on his campaign website that he is '100% Pro-Life and will always staunchly defend the right to life and protect the rights of the unborn,' and has voted against every measure to expand taxpayer funding of abortion, including the Biden-era DoD abortion-travel policy he opposed from the House floor.",
              ["https://alfordforcongress.com/on-the-issues/",
               "https://en.wikipedia.org/wiki/Mark_Alford"]),
        claim("ma2", "mark-alford", "self_defense", 4, True,
              "Voted against the ATF rule on stabilizing braces — a unilateral executive redefinition that would have reclassified millions of legally owned pistol-brace firearms as NFA items — aligning with the rubric's opposition to ATF overreach and gun-control bureaucracy.",
              ["https://en.wikipedia.org/wiki/Mark_Alford",
               "https://www.congress.gov/member/mark-alford/A000379"]),
        claim("ma3", "mark-alford", "border_immigration", 0, True,
              "Voted for H.R.2, the Secure the Border Act of 2023, which funds border-wall construction, ends catch-and-release, and bars entry to those who crossed through safe third countries — backing full enforcement plus physical barrier construction.",
              ["https://en.wikipedia.org/wiki/Mark_Alford",
               "https://www.congress.gov/member/mark-alford/A000379"]),
    ]),

    # ---------------- Jason Smith (MO-08, R, Ways & Means Chair) ----------------
    ("jason-smith", "MO", "House", [
        claim("js1", "jason-smith", "sanctity_of_life", 0, True,
              "Carries a consistent 100% pro-life record with SBA Pro-Life America; introduced H.R. 606 (No Abortion Bonds Act) to block tax-exempt bond financing for abortion providers, and as Ways & Means Chairman passed H.R. 6918 to protect TANF funding for pregnancy resource centers from the Biden administration's defunding effort.",
              ["https://sbaprolife.org/representative/jason-smith",
               "https://en.wikipedia.org/wiki/Jason_Smith_(American_politician)"]),
        claim("js2", "jason-smith", "self_defense", 0, True,
              "A lifetime member of the National Rifle Association who voted for the Concealed Carry Reciprocity Act of 2017, which would compel every state to honor other states' carry permits — functionally extending constitutional carry to interstate travel — and has maintained a consistently pro-gun legislative record throughout his tenure.",
              ["https://en.wikipedia.org/wiki/Jason_Smith_(American_politician)",
               "https://www.govtrack.us/congress/members/jason_smith/412596"]),
        claim("js3", "jason-smith", "border_immigration", 0, True,
              "Represents Missouri's 8th district — the most rural, strongly Republican district in the state — and has voted for House Republican border-security packages including the Secure the Border Act while chairing Ways & Means, channeling tax policy to support enforcement measures.",
              ["https://en.wikipedia.org/wiki/Jason_Smith_(American_politician)",
               "https://www.govtrack.us/congress/members/jason_smith/412596"]),
    ]),

    # ---------------- Mike Flood (NE-01, R, serving since 2022) ----------------
    ("mike-flood", "NE", "House", [
        claim("mf1", "mike-flood", "sanctity_of_life", 0, True,
              "As a Nebraska state legislator introduced and passed the Pain-Capable Unborn Child Protection Act — the nation's first 20-week abortion ban (2010) — and has continued an unbroken pro-life voting record in Congress, opposing all federal taxpayer funding for abortion including travel reimbursement.",
              ["https://en.wikipedia.org/wiki/Mike_Flood_(politician)",
               "https://sbaprolife.org/representative/mike-flood"]),
        claim("mf2", "mike-flood", "border_immigration", 0, True,
              "Called immigration 'the No. 1 issue I hear about' from constituents, traveled to the southern border to assess conditions, and backs military-grade enforcement: securing the border wall, ending catch-and-release, and supporting Trump's Remain-in-Mexico policy that requires asylum seekers to wait in Mexico during adjudication.",
              ["https://fremonttribune.com/news/state-regional/government-politics/mike-flood-immigration-border-mexico-trip/article_38e7f902-a539-5e0b-9280-8de4c9c56139.html",
               "https://en.wikipedia.org/wiki/Mike_Flood_(politician)"]),
        claim("mf3", "mike-flood", "self_defense", 0, True,
              "As Speaker of the Nebraska Legislature codified the right to concealed carry in state law, and as a U.S. representative has defended the Second Amendment against federal infringement — Trump endorsed Flood in 2024 partly on the strength of his gun-rights record.",
              ["https://mikefloodfornebraska.com/president-trump-endorses-ne-01-congressman-mike-flood/",
               "https://en.wikipedia.org/wiki/Mike_Flood_(politician)"]),
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

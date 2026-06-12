#!/usr/bin/env python3
"""Enrichment batch 151: hand-curated claims for 5 TX U.S. Representatives.

Targets archetype_party_default / evidence_federal TX House members with 0 claims,
taken from the bottom of the non-exhausted federal bucket.

Mix (2 R / 3 D): Morgan Luttrell (TX-8, R), Jodey Arrington (TX-19, R),
Veronica Escobar (TX-16, D), Sylvia Garcia (TX-29, D), Henry Cuellar (TX-28, D).
Each claim cites >=1 reliable source and reflects 2022-2025 voting
record / public positions.

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
    # ---------------- Morgan Luttrell (TX-8, R) ----------------
    ("morgan-luttrell", "TX", "Representative", [
        claim("ml1", "morgan-luttrell", "self_defense", 2, True,
              "Voted YES on H.R.1 — the One Big Beautiful Bill Act (signed July 4, 2025) — which included the Hearing Protection Act provision completely removing suppressors from the National Firearms Act, the most significant NFA rollback in decades.",
              ["https://luttrell.house.gov/media/press-releases/luttrell-statement-final-passage-one-big-beautiful-bill",
               "https://www.nraila.org/articles/20250703/congress-passes-the-one-big-beautiful-bill-now-headed-to-president-trump"]),
        claim("ml2", "morgan-luttrell", "border_immigration", 0, True,
              "A decorated Navy SEAL who ran on 'finish the Wall' and voted for H.R.1 (One Big Beautiful Bill Act, 2025), which supporters describe as the greatest single investment in border security and military assets in U.S. history — consistent with the wall-plus-military rubric posture.",
              ["https://ballotpedia.org/Morgan_Luttrell",
               "https://en.wikipedia.org/wiki/Morgan_Luttrell"]),
        claim("ml3", "morgan-luttrell", "sanctity_of_life", 4, True,
              "Voted for H.R.1 (One Big Beautiful Bill Act, signed July 4, 2025), which included a one-year Medicaid defunding of Planned Parenthood — directly reducing the largest abortion provider's federal subsidy and placing him outside the PP funding network.",
              ["https://luttrell.house.gov/media/press-releases/luttrell-statement-final-passage-one-big-beautiful-bill",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---------------- Jodey Arrington (TX-19, R) ----------------
    ("jodey-arrington", "TX", "Representative", [
        claim("ja1", "jodey-arrington", "economic_stewardship", 2, True,
              "As House Budget Committee Chairman, opened the May 2025 'Fiscal State of the Nation' hearing by declaring the country's finances 'in a dire state and condition and rapidly in decline' — a fiscal-hawk posture consistent with the rubric's anti-deficit, balanced-budget standard.",
              ["https://arrington.house.gov/news/documentsingle.aspx?DocumentID=3889",
               "https://en.wikipedia.org/wiki/Jodey_Arrington"]),
        claim("ja2", "jodey-arrington", "border_immigration", 0, True,
              "As Budget Committee Chairman, authored and passed H.R.1 — the One Big Beautiful Bill Act (signed July 4, 2025) — describing it as delivering 'the greatest single investment in border security and national defense,' including wall construction funding and military border deployment.",
              ["https://arrington.house.gov/news/documentsingle.aspx?DocumentID=3947",
               "https://arrington.house.gov/news/documentsingle.aspx?DocumentID=3862"]),
        claim("ja3", "jodey-arrington", "sanctity_of_life", 4, True,
              "Authored and shepherded H.R.1 (One Big Beautiful Bill Act, signed July 4, 2025) through the Budget Committee; the legislation included a one-year Medicaid defunding of Planned Parenthood, the bill's central pro-life provision.",
              ["https://arrington.house.gov/news/documentsingle.aspx?DocumentID=3947",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---------------- Veronica Escobar (TX-16, D) ----------------
    ("veronica-escobar", "TX", "Representative", [
        claim("ve1", "veronica-escobar", "sanctity_of_life", 0, False,
              "A co-introducer of the Women's Health Protection Act (WHPA) in the 118th Congress, legislation that would federally codify abortion access and override all state pro-life protections — rejecting any recognition of personhood or protection for the unborn.",
              ["https://en.wikipedia.org/wiki/Veronica_Escobar",
               "https://reproductivefreedomforall.org/news/naral-pro-choice-america-applauds-house-democrats-reintroduction-of-womens-health-protection-act/"]),
        claim("ve2", "veronica-escobar", "self_defense", 1, False,
              "Voted YES on H.R.1808 — the Assault Weapons Ban of 2022 — which passed the House 217-213 with all yes votes from Democrats; the bill would ban the manufacture and sale of semi-automatic rifles and high-capacity magazines, directly opposing the rubric's anti-AWB position.",
              ["https://en.wikipedia.org/wiki/Assault_Weapons_Ban_of_2022",
               "https://www.govtrack.us/congress/members/veronica_escobar/412825"]),
        claim("ve3", "veronica-escobar", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (signed Dec. 13, 2022), which codifies federal recognition of same-sex unions and requires states to recognize same-sex marriages — directly opposing the one-man-one-woman definition the rubric requires.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://www.govtrack.us/congress/members/veronica_escobar/412825"]),
    ]),

    # ---------------- Sylvia Garcia (TX-29, D) ----------------
    ("sylvia-garcia", "TX", "Representative", [
        claim("sg1", "sylvia-garcia", "sanctity_of_life", 0, False,
              "Supports codifying abortion rights into federal law and has stated the Supreme Court's Dobbs decision was 'a historic failure'; backs the Women's Health Protection Act to override state pro-life laws — rejecting any fetal personhood standard.",
              ["https://en.wikipedia.org/wiki/Sylvia_Garcia",
               "https://www.govtrack.us/congress/members/sylvia_garcia/412827"]),
        claim("sg2", "sylvia-garcia", "border_immigration", 1, False,
              "Lead sponsor of the American Dream and Promise Act (H.R.16, 118th Congress), which creates a path to lawful permanent residence for DACA recipients and those holding Temporary Protected Status — directly opposing the rubric's mandatory-deportation and enforcement-first standards.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/16",
               "https://en.wikipedia.org/wiki/Sylvia_Garcia"]),
        claim("sg3", "sylvia-garcia", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (signed Dec. 13, 2022), codifying federal recognition of same-sex unions — opposing the one-man-one-woman marriage definition the rubric requires.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://ballotpedia.org/Sylvia_Garcia"]),
    ]),

    # ---------------- Henry Cuellar (TX-28, D) ----------------
    ("henry-cuellar", "TX", "Representative", [
        claim("hc1", "henry-cuellar", "sanctity_of_life", 0, True,
              "The only House Democrat to vote against the Women's Health Protection Act — the bill to federally codify abortion rights — and consistently identified as the only anti-abortion Democrat in the U.S. House; SBA Pro-Life America notes his record of opposing the most extreme pro-abortion appropriations amendments.",
              ["https://en.wikipedia.org/wiki/Henry_Cuellar",
               "https://sbaprolife.org/representative/henry-cuellar",
               "https://reproductivefreedomforall.org/news/naral-pro-choice-america-denounces-henry-cuellar-for-vote-against-womens-health-protection-act/"]),
        claim("hc2", "henry-cuellar", "biblical_marriage", 2, True,
              "In 2025, was one of only two House Democrats to vote for the Protection of Women and Girls in Sports Act, which bans transgender-identifying males from participating in federally funded women's and girls' sports — breaking sharply with his party on the transgender-ideology question.",
              ["https://en.wikipedia.org/wiki/Henry_Cuellar",
               "https://ballotpedia.org/Henry_Cuellar"]),
        claim("hc3", "henry-cuellar", "election_integrity", 0, True,
              "One of only four House Democrats to vote YES on the SAVE Act (April 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections — a strict voter-verification measure aligned with the rubric's election-integrity position.",
              ["https://en.wikipedia.org/wiki/Henry_Cuellar",
               "https://ballotpedia.org/Henry_Cuellar"]),
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

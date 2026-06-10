#!/usr/bin/env python3
"""Enrichment batch 120: hand-curated claims for 4 sitting U.S. Representatives
running for Senate in 2026 (bottom of reverse-alpha archetype_party_default pool).

archetype_curated federal senator bucket reduced to 1 obscure perennial candidate
(Joe Mazzola, MA) with no findable sourced positions; archetype_curated U.S.
Representative bucket is empty.  Next available sourced targets taken from the
bottom of the archetype_party_default federal-Senate pool (TX, NH, MN, MI).

Targets (all D): Jasmine Crockett (TX), Chris Pappas (NH), Angie Craig (MN),
Haley Stevens (MI).  Each claim cites >=1 reliable source and reflects
2024–2026 voting record / public positions.

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
    # ---------------- Jasmine Crockett (TX-D, US Rep TX-30, 2026 TX Senate primary) ----------------
    ("jasmine-crockett", "TX", "Representative", [
        claim("jc1", "jasmine-crockett", "sanctity_of_life", 0, False,
              "Endorsed by Reproductive Freedom for All with a perfect pro-choice congressional scorecard; sponsored the Abortion Care Awareness Act of 2024 (H.R.7684), a bill to fund public health campaigns promoting abortion access and countering what it terms 'abortion stigma' — rejecting any legal recognition of life or personhood from conception.",
              ["https://reproductivefreedomforall.org/lawmaker/jasmine-crockett/",
               "https://www.congress.gov/bill/118th-congress/house-bill/7684"]),
        claim("jc2", "jasmine-crockett", "self_defense", 1, False,
              "Advocates for a federal ban on assault-style semi-automatic weapons, stating that private ownership of such firearms is 'the equivalent of some of these people having a cannon … people literally have almost no chance of surviving when some of these weapons are used' — directly opposing the rubric's rejection of any assault-weapons ban or magazine restriction.",
              ["https://en.wikipedia.org/wiki/Jasmine_Crockett",
               "https://ballotpedia.org/Jasmine_Crockett"]),
    ]),

    # ---------------- Chris Pappas (NH-D, US Rep NH-01, 2026 NH Senate candidate) ----------------
    ("chris-pappas", "NH", "Senate", [
        claim("cp1", "chris-pappas", "border_immigration", 1, True,
              "One of only 46 House Democrats to cross party lines and vote YES on the Laken Riley Act (S.5 / H.R.29, signed into law January 2025), which mandates ICE detention of undocumented immigrants charged with theft or violent crimes — a bipartisan enforcement vote that aligns with the rubric's mandatory-detention/enforcement standard on immigration.",
              ["https://en.wikipedia.org/wiki/Laken_Riley_Act",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
        claim("cp2", "chris-pappas", "sanctity_of_life", 0, False,
              "Has publicly supported passing federal legislation to restore abortion rights after the Supreme Court's Dobbs decision, and his House voting record has earned him poor marks from SBA Pro-Life America for consistently opposing protections for the unborn — rejecting any life-at-conception or personhood standard.",
              ["https://en.wikipedia.org/wiki/Chris_Pappas_(American_politician)",
               "https://sbaprolife.org/representative/chris-pappas"]),
    ]),

    # ---------------- Angie Craig (MN-D, US Rep MN-02, 2026 MN Senate candidate) ----------------
    ("angie-craig", "MN", "Representative", [
        claim("ac1", "angie-craig", "sanctity_of_life", 0, False,
              "Carries a 100% pro-choice scorecard from Reproductive Freedom for All and a 0% / failing rating from SBA Pro-Life America; voted for the Women's Health Protection Act and measures expanding abortion coverage under federal programs — opposing any legal recognition of personhood or protection for the unborn from conception.",
              ["https://reproductivefreedomforall.org/lawmaker/angie-craig/",
               "https://sbaprolife.org/representative/angie-craig"]),
        claim("ac2", "angie-craig", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act of 2022 — the most expansive federal gun legislation in nearly three decades — which enhanced background checks for buyers aged 18–21, closed the 'boyfriend loophole,' and created financial incentives for states to enact red-flag laws, directly opposing the rubric's rejection of expanded background checks and red-flag legislation.",
              ["https://en.wikipedia.org/wiki/Angie_Craig",
               "https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act"]),
    ]),

    # ---------------- Haley Stevens (MI-D, US Rep MI-11, 2026 MI Senate candidate) ----------------
    ("haley-stevens", "MI", "Senate", [
        claim("hs1", "haley-stevens", "sanctity_of_life", 0, False,
              "Has voted consistently against protections for unborn children and to eliminate prohibitions on taxpayer funding for abortion both domestically and internationally; tracked by SBA Pro-Life America as having a failing pro-life House voting record — rejecting any personhood-from-conception or life-at-conception standard.",
              ["https://sbaprolife.org/representative/haley-stevens",
               "https://en.wikipedia.org/wiki/Haley_Stevens"]),
        claim("hs2", "haley-stevens", "self_defense", 1, False,
              "Introduced H.R.9003, the Keep Illegal Handguns Out of the Mail Act (119th Congress, 2026), targeting firearm transfers through mail systems; voted for the Bipartisan Safer Communities Act of 2022, which expanded background checks and incentivized state red-flag laws — opposing the rubric's blanket rejection of new background-check expansions and red-flag legislation.",
              ["https://www.congress.gov/member/haley-stevens/S001215",
               "https://en.wikipedia.org/wiki/Haley_Stevens"]),
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

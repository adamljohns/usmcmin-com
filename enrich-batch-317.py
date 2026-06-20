#!/usr/bin/env python3
"""Enrichment batch 317: 3rd distinct-category claims for 5 evidence_curated candidates.

Mix of 1 SC federal candidate (needs a 3rd claim) and 4 WY state senators continuing
the reverse-alpha pipeline from batches 314-316. Picks up after Evie Brennan (E) from
batch 315; next in reverse alpha within WY is Eric Barlow (E), Dan Laursen (D),
Dan Dockstader (D), Cheri Steinmetz (C).

Targets:
  Alex Pelbath         (SC-01 R, LOST 2026 primary)  — christian_liberty[0]=True
                         (January 2026 "Jesus-loving, God-fearing America First family";
                          May 2026 "Christian conservative values are under attack")
  Eric Barlow          (WY R, State Sen / 2026 gov)   — sanctity_of_life[0]=True
                         (supported near-total abortion ban + med-abortion ban 2023 as
                          House Speaker; 2026 gubernatorial pledge: "fiercely defend...
                          the sanctity of life")
  Dan Laursen          (WY R, State Sen)               — family_child_sovereignty[0]=True
                         (Senate co-sponsor HB199 2025, Wyoming Freedom Scholarship Act;
                          universal $7K school-choice vouchers; Senate passed 20-11)
  Dan Dockstader       (WY R, State Sen)               — election_integrity[0]=True
                         (voted with 26-4 Wyoming Senate majority for HB0156 2025;
                          Wyoming became first state to require proof of citizenship
                          to vote at all election levels)
  Cheri Steinmetz      (WY R, State Sen)               — border_immigration[2]=True
                         (primary sponsor SF0124 2025, Wyoming Illegal Immigration:
                          Identify, Report, Detain and Deport bill; authored guest column
                          defending immigration enforcement in Wyoming)

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


TARGETS = [
    # -------- Alex Pelbath (SC-01, R, retired USAF Colonel; LOST 2026 R primary ~10.86%) --------
    ("alex-pelbath", "SC", "SC-01", [
        claim("ap3", "alex-pelbath", "christian_liberty", 0, True,
              "In a January 2026 WE THE PALMETTO interview, Pelbath described his family as 'a "
              "Jesus-loving, God-fearing America First family.' At the May 2026 SC-01 Lowcountry "
              "Republican debate, he declared that 'Christian conservative values are under attack' "
              "— placing active Christian faith and religious liberty at the center of his campaign "
              "identity, consistent with the rubric's christian_liberty[0] standard.",
              ["https://www.live5news.com/2026/01/23/we-palmetto-meet-candidate-alex-pelbath-sc-01/",
               "https://abcnews4.com/news/local/we-need-leaders-not-politicians-in-dc-sc-01-candidate-lays-out-campaign-goals-wciv-abc-news-4-charleston-lowcountry-south-carolina-1st-congressional-district-alex-pelbath-nancy-mace-mac-deford-mark-smith-jack-ellison-sam-mccown-mayra-rivera-vazquez"]),
    ]),

    # -------- Eric Barlow (WY R, State Senator / 2026 gubernatorial candidate) --------
    ("eric-barlow", "WY", "State Senator", [
        claim("eba3", "eric-barlow", "sanctity_of_life", 0, True,
              "As Wyoming House Speaker (2021-2023), Barlow supported both a near-total abortion ban "
              "and a separate medication abortion ban in 2023, placing him squarely in the pro-life "
              "legislative majority on Wyoming's most consequential abortion votes of that session. "
              "When announcing his 2026 gubernatorial campaign, Barlow reiterated that as governor he "
              "would 'fiercely defend your rights, including the Second Amendment and the sanctity of "
              "life' — affirming a sustained pro-life posture consistent with the rubric's "
              "sanctity_of_life[0] standard.",
              ["https://ballotpedia.org/Eric_Barlow",
               "https://wyofile.com/sen-eric-barlow-will-run-for-wyoming-governor/"]),
    ]),

    # -------- Dan Laursen (WY R, State Senator, District 19) --------
    ("dan-laursen", "WY", "State Senator", [
        claim("dl3", "dan-laursen", "family_child_sovereignty", 0, True,
              "Listed as a Senate co-sponsor of Wyoming House Bill 199 (2025), 'The Wyoming Freedom "
              "Scholarship Act,' which creates a universal school-choice program providing up to $7,000 "
              "per child to any Wyoming family — regardless of income — for private-school tuition and "
              "related educational expenses for pre-K through high-school students. The Wyoming Senate "
              "passed HB 199 on third reading 20-11, enacting what advocates called a landmark "
              "expansion of parental authority over children's education, consistent with the rubric's "
              "family_child_sovereignty[0] standard.",
              ["https://greybullstandard.com/content/debate-over-school-choice-bill-continues",
               "https://wyomingfamily.org/hb0199-wyoming-freedom-scholarship-act/"]),
    ]),

    # -------- Dan Dockstader (WY R, State Senator, District 16; former Senate President) --------
    ("dan-dockstader", "WY", "State Senator", [
        claim("dd3", "dan-dockstader", "election_integrity", 0, True,
              "Voted with the Wyoming Senate Republican majority for HB0156 (2025), which requires "
              "documentary proof of U.S. citizenship and 30 days of in-state residency before a person "
              "may register to vote in any Wyoming election — from municipal through national. The bill "
              "passed the Wyoming Senate 26-4 on its third reading. The law took effect July 1, 2025 "
              "and made Wyoming the first state in the nation to impose such a comprehensive "
              "proof-of-citizenship voter-registration requirement at all election levels, directly "
              "satisfying the rubric's election_integrity[0] ballot-security standard.",
              ["https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/"]),
    ]),

    # -------- Cheri Steinmetz (WY R, State Senator, District 3) --------
    ("cheri-steinmetz", "WY", "State Senator", [
        claim("cs3", "cheri-steinmetz", "border_immigration", 2, True,
              "Primary sponsor of Wyoming Senate File 124 (2025), 'Illegal Immigration — Identify, "
              "Report, Detain and Deport,' which would have required Wyoming law-enforcement officers "
              "to inquire about the immigration status of any person they detain and to hand over "
              "anyone unable to prove lawful presence to federal authorities. Steinmetz co-sponsored "
              "the bill alongside Sens. Hutchings, Kolb, and Pearson and personally authored a guest "
              "column — 'Guarding the Heartland: Why Immigration Security Matters in Wyoming' — "
              "articulating an anti-sanctuary stance and direct cooperation with ICE, consistent with "
              "the rubric's border_immigration[2] standard.",
              ["https://wyofile.com/sweeping-state-immigration-crackdown-to-get-wyoming-committee-hearing/",
               "https://www.wyomingnews.com/opinion/guest_column/steinmetz-guarding-the-heartland-why-immigration-security-matters-in-wyoming/article_41ee5850-d902-11ef-a264-23b0dcba5868.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher (slug + state + office keyword) — prevents collision."""
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

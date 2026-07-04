#!/usr/bin/env python3
"""Enrichment batch 557: 5 state senators — bottom-of-alphabet fill (TN + SD).

Federal-senator and US-House buckets are now exhausted (archetype_curated and
archetype_party_default both empty). Moving to state-level officials from the
bottom of the alphabet: Tennessee (TN) then South Dakota (SD).

5 candidates (5 R):
  Dawn White      (TN-R, State Senator, District 13 — Murfreesboro)
  Ed Jackson      (TN-R, State Senator, District 25 — West Tennessee)
  Brent Taylor    (TN-R, State Senator, District 31 — Memphis/Shelby County)
  Taffy Howard    (SD-R, State Senator, District 34)
  Tom Pischke     (SD-R, State Senator, District 25)

Each claim cites >=1 reliable source and reflects 2021-2026 record/positions.
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
    # ---------------- Dawn White (TN-R, State Senator District 13) ----------------
    ("dawn-white", "TN", "State Senator", [
        claim("dw1", "dawn-white", "biblical_marriage", 2, True,
              "A listed co-sponsor of Tennessee SB 1 / HB 1 (113th General Assembly, 2023) — the SAFE Act banning puberty blockers, cross-sex hormones, and gender surgeries for minors seeking gender-affirming care. The Senate passed 26–6 on January 26, 2023; the legislation was signed March 2, 2023, and upheld by the U.S. Supreme Court in June 2025. Wikipedia's article on the bill lists White explicitly among the Senate co-sponsors.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1"]),
        claim("dw2", "dawn-white", "sanctity_of_life", 0, True,
              "Publicly co-sponsored legislation to completely defund Planned Parenthood in Tennessee and states on her campaign issues page that she 'fought to make sure abortion providers aren't able to receive one cent of taxpayer money.' Also supported Tennessee's Human Life Protection Act — the near-total abortion ban enacted 2022 and in effect from August 2022 — affirming protection of the unborn from conception.",
              ["https://www.votedawn.com/issues",
               "https://ballotpedia.org/Dawn_White"]),
        claim("dw3", "dawn-white", "family_child_sovereignty", 0, True,
              "As Chair of the Tennessee Senate Education Committee (2025–2026), advanced SB 1585 — a major expansion of the state's private-school voucher (Education Savings Account) program — through committee on a 5–4 vote and championed it on the Senate floor, directly expanding parents' ability to direct public education dollars to the school of their choice. Also cast a deciding vote against taxpayer-funded tuition for illegal immigrants.",
              ["https://tennesseelookout.com/2025/03/27/tennessee-senate-targets-school-boards-superintendents-associations/",
               "https://www.wkrn.com/news/tennessee-politics/tn-senate-education-committee-members-ask-tsba-to-voluntarily-submit-all-communications-related-to-school-voucher-bill/"]),
    ]),

    # ---------------- Ed Jackson (TN-R, State Senator District 25) ----------------
    ("ed-jackson", "TN", "State Senator", [
        claim("ej1", "ed-jackson", "sanctity_of_life", 0, True,
              "Self-described '100% pro-life' who affirms life begins at conception; was a leading advocate for the 'Yes on 1' Tennessee constitutional amendment protecting the unborn. Co-sponsored TN SB 1 (2023) — the SAFE Act — and holds a consistent pro-life rating from Tennessee Right to Life. Campaign materials confirm: 'I believe every life is sacred from conception to natural death.'",
              ["https://www.edjacksonforsenate.com/",
               "https://ballotpedia.org/Ed_Jackson"]),
        claim("ej2", "ed-jackson", "border_immigration", 3, True,
              "Lead Senate sponsor of SB 1915 / HB 1710 (114th General Assembly, 2026) — part of Tennessee's 'Immigration 2026' package — requiring state and local agencies to use E-Verify before providing any public benefits to persons without proof of citizenship or legal status. Also created a Centralized Immigration Enforcement Division to coordinate with federal immigration authorities, and strengthened the sanctuary-city ban by making violations a Class E felony for local officials. The Senate adopted these bills March 31, 2026.",
              ["https://tennesseelookout.com/2026/02/09/tennessee-gop-bill-would-require-immigration-checks-for-local-government-aid/",
               "https://tennesseelookout.com/2026/03/31/tennessee-senate-adopts-non-citizen-jobs-benefits-bills/"]),
        claim("ej3", "ed-jackson", "self_defense", 0, True,
              "NRA member holding an A-rating from the National Rifle Association for his 2nd Amendment legislative record; is also a member of the Tennessee Firearms Association. Publicly states he 'will stand against any legislation that strips Tennesseans of this historic right.' Consistently votes against gun-control measures in the Tennessee Senate.",
              ["https://ballotpedia.org/Ed_Jackson",
               "https://www.edjacksonforsenate.com/"]),
    ]),

    # ---------------- Brent Taylor (TN-R, State Senator District 31) ----------------
    ("brent-taylor", "TN", "State Senator", [
        claim("bt1", "brent-taylor", "biblical_marriage", 2, True,
              "A listed co-sponsor of Tennessee SB 1 / HB 1 (113th General Assembly, 2023) — the SAFE Act banning gender-affirming medical care (puberty blockers, cross-sex hormones, and surgical procedures) for minors — which passed the Senate 26–6 and was upheld by the U.S. Supreme Court in June 2025. Also supported legislation declaring that teachers are NOT required to use a student's preferred pronouns, protecting teacher conscience rights against compelled speech.",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1"]),
        claim("bt2", "brent-taylor", "self_defense", 0, True,
              "Filed and sponsored SB 1503 (2023), legislation to lower Tennessee's permitless-carry age from 21 to 18, allowing adults 18–20 to carry a handgun without a government-issued permit. Received an endorsement from the NRA Political Victory Fund (NRA-PVF). Also supported legislation protecting firearm manufacturers and retailers from frivolous civil litigation under state law.",
              ["https://www.actionnews5.com/2023/04/13/some-tenn-lawmakers-seek-lower-permitless-carry-age-18/"]),
        claim("bt3", "brent-taylor", "border_immigration", 2, True,
              "Prime Senate sponsor of SB 0227 (114th General Assembly, 2025) authorizing civil damages lawsuits against charitable organizations if a person they housed who is unlawfully present in the United States subsequently commits a crime — ending nonprofit safe harbor for harboring illegal immigrants. Also co-sponsored HB 322 / SB 392, creating the new Tennessee state crime of 'human smuggling' and criminalizing the harboring of illegal immigrants.",
              ["https://www.wbir.com/article/news/state/tn-senate-passes-bill-hold-housing-nonprofits-liable-for-crimes-committed-by-clients-in-the-us-illegally/51-3f793627-9810-4baf-8440-8854861311f7",
               "https://tennesseelookout.com/2025/04/03/tennessee-senate-oks-bill-to-hold-charities-liable-for-aiding-immigrants-who-later-commit-crime/"]),
    ]),

    # ---------------- Taffy Howard (SD-R, State Senator District 34) ----------------
    ("taffy-howard", "SD", "State Senator", [
        claim("th1", "taffy-howard", "biblical_marriage", 2, True,
              "Co-sponsored SD HB 1217 (2021) — the Fairness in Women's Sports Act — requiring athletic participation to be based on biological sex, effectively barring transgender girls from competing on girls' teams at K-12 and collegiate levels. When Governor Noem returned the bill with amendments rather than signing it, Howard publicly argued for a full veto override on the floor, calling Noem's changes 'very substantive' and urging colleagues to 'use our backbone.' The override failed 45–24, two votes short. Holds a 100% Family Heritage Action rating.",
              ["https://legiscan.com/SD/bill/HB1217/2021",
               "https://www.keloland.com/keloland-com-original/updates-from-veto-day-in-pierre/"]),
        claim("th2", "taffy-howard", "family_child_sovereignty", 0, True,
              "Co-sponsored SD SB 113 (2025) — 'an act to provide protections for parental rights' — codifying parental rights in education including participation in school organizations. Voted yes on the bill in the Senate State Affairs Committee (6–3 on February 7, 2025) and yes on full Senate passage February 11, 2025. Holds a 94% CPAC lifetime rating (CPAC Conservative Excellence Award) and a 100% Family Heritage Action score; served as Vice Chair of the SD House Appropriations Committee.",
              ["https://www.billsponsor.com/bills/667719/south-dakota-senate-bill-113-session-2025",
               "https://www.cpac.org/bio/sd-taffy-howard"]),
        claim("th3", "taffy-howard", "christian_liberty", 0, True,
              "Explicitly stated in campaign materials that 'religious liberty is at risk in the United States and deserves the highest level of protection in the law,' and opposes any requirement that individuals or businesses provide services that violate their moral or religious beliefs. A U.S. Air Force veteran, she frames religious conscience as a foundational liberty requiring the strongest legal protection.",
              ["https://ballotpedia.org/Taffy_Howard",
               "https://www.cpac.org/bio/sd-taffy-howard"]),
    ]),

    # ---------------- Tom Pischke (SD-R, State Senator District 25) ----------------
    ("tom-pischke", "SD", "State Senator", [
        claim("tp1", "tom-pischke", "family_child_sovereignty", 0, True,
              "Prime Senate sponsor of SD SB 224 (2025), which establishes a rebuttable presumption of joint physical custody (50/50 starting point) in initial custody determinations — directly limiting judicial discretion to remove a fit parent from a child's daily life without clear evidence. Motivated by personal experience: 'I went from being an active father of three to a visitor in my children's lives.' The Senate passed SB 224 on a 20–14 vote. Also voted yes on SB 113 (2025) protecting parental rights in education.",
              ["https://www.keloland.com/keloland-com-original/2-child-support-bills-die-custody-rebuttal-passes/",
               "https://www.billsponsor.com/bills/667719/south-dakota-senate-bill-113-session-2025"]),
        claim("tp2", "tom-pischke", "biblical_marriage", 2, True,
              "Co-sponsored SD HB 1217 (2021) — the Fairness in Women's Sports Act — prohibiting transgender girls from competing on girls' athletic teams. Previously sponsored a House bill restricting gender ideology discussions in classrooms, stating: 'I'm still confused as to what woman-ness and man-ness is, so I don't know why we'd be teaching that to someone in the fourth grade.' Earned a 100% CPAC Conservative Excellence Award for the 2023 South Dakota legislative session and an 80% SD Citizens for Liberty rating in 2024 (2nd highest in the full Senate).",
              ["https://legiscan.com/SD/bill/HB1217/2021",
               "https://www.cpac.org/us/statements/01-18-2024/cpac-releases-south-dakota-legislative-scorecard-exposing-a-republican-legislature-that-struggles-to-pass-even-the-mildest-of-conservative-policies"]),
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

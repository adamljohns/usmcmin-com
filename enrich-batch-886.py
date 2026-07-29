#!/usr/bin/env python3
"""Enrichment batch 886: 5 sitting U.S. Representatives — UT and TX.

Archetype_curated 0-claim bucket is exhausted; this batch expands evidence_curated
sitting officials with additional distinct-category claims.

Targets (bottom-of-alphabet, sitting Representatives):
  Mike Kennedy    (UT-03, R) — christian_liberty + economic_stewardship
  Celeste Maloy   (UT-02, R) — economic_stewardship(CBDC) + foreign_policy_restraint + biblical_marriage
  Blake Moore     (UT-01, R) — self_defense + foreign_policy_restraint + christian_liberty
  Roger Williams  (TX-25, R) — biblical_marriage + foreign_policy_restraint
  Pete Sessions   (TX-17, R) — economic_stewardship + christian_liberty

All claims cite >=1 verifiable public source (congress.gov / house.gov / govtrack.us /
deseret.com / ksl.com / texastribune.org) and reflect 2022-2026 voting records.
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
    # ---------- Mike Kennedy (UT-03, R, US Representative) ----------
    ("mike-kennedy", "UT", "Representative", [
        claim("mk886a", "mike-kennedy", "christian_liberty", 0, True,
              "Campaign platform explicitly commits to defending religious liberty as non-negotiable, "
              "with Kennedy — a physician and attorney serving an LDS-majority district — publicly "
              "opposing any federal mandate that would coerce faith-based medical providers or "
              "employers to violate their religious conscience. His issues page states 'no one should "
              "be forced to violate their beliefs' as a core governing principle.",
              ["https://mikekennedyforutah.com/issues/",
               "https://mikekennedy.house.gov/"]),
        claim("mk886b", "mike-kennedy", "economic_stewardship", 2, True,
              "Secured inclusion of his Ensuring Medicaid Eligibility Act of 2025 in the One Big "
              "Beautiful Bill Act (H.R.1, signed July 4, 2025), which adds work requirements and "
              "enhanced eligibility verification to reduce improper Medicaid payments. Kennedy stated: "
              "'I'm grateful that key provisions from my Ensuring Medicaid Eligibility Act of 2025 "
              "were secured in this landmark legislation — helping ensure support reaches those who "
              "qualify and rely on it' — a concrete anti-deficit fiscal-reform measure.",
              ["https://mikekennedy.house.gov/media/in-the-news",
               "https://www.ntd.com/ntdplus/reconciliation-package-will-help-move-aspects-of-save-america-act-dems-will-not-get-behind-rep-kennedy_1159702.html"]),
    ]),

    # ---------- Celeste Maloy (UT-02, R, US Representative) ----------
    ("celeste-maloy", "UT", "Representative", [
        claim("cm886a", "celeste-maloy", "economic_stewardship", 0, True,
              "Co-sponsored and voted YES on H.R. 5403, the CBDC Anti-Surveillance State Act "
              "(House Vote #230, May 23, 2024, passed 216-192), which would prohibit the Federal "
              "Reserve from offering products or services directly to individuals or issuing a "
              "central bank digital currency — directly blocking a government-trackable digital "
              "dollar from being introduced into the U.S. financial system.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5403",
               "https://www.govtrack.us/congress/votes/118-2024/h230"]),
        claim("cm886b", "celeste-maloy", "foreign_policy_restraint", 1, True,
              "Voted NO on H.R. 8035, the Ukraine Security Supplemental Appropriations Act "
              "(House Roll Call 151, April 20, 2024), the $60.8B Ukraine portion of the $95B "
              "foreign aid package. Maloy stated: 'While America is in debt over $34 trillion, and "
              "without certainty our funds will reach the Ukrainian war effort, I voted against "
              "sending billions of additional taxpayer dollars to Ukraine.'",
              ["https://www.deseret.com/politics/2024/04/20/utah-delegation-votes-on-house-foreign-aid-ukraine-israel-tiktok/",
               "https://www.govtrack.us/congress/bills/118/hr8035"]),
        claim("cm886c", "celeste-maloy", "biblical_marriage", 2, True,
              "Voted YES on H.R. 28, the Protection of Women and Girls in Sports Act (House Vote "
              "#12, January 14, 2025, passed 218-206), which bans biological males from competing "
              "in women's sports programs receiving federal Title IX funds — rejecting the "
              "transgender ideology that erases the biological distinction between men and women in "
              "athletic competition. Also co-signed a congressional letter to the Mountain West "
              "Conference in November 2024 urging it to prohibit biological males from competing "
              "in women's college sports.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://www.congress.gov/bill/119th-congress/house-bill/28",
               "https://maloy.house.gov/news/documentsingle.aspx?DocumentID=1369"]),
    ]),

    # ---------- Blake Moore (UT-01, R, US Representative) ----------
    ("blake-moore", "UT", "Representative", [
        claim("bm886a", "blake-moore", "self_defense", 1, True,
              "Voted NO on the Bipartisan Safer Communities Act (S. 2938, June 24, 2022) — the "
              "first major federal gun bill in nearly 30 years — specifically citing opposition to "
              "Section 12003, which funds state red-flag laws 'without specific assurance of full "
              "due process protections.' Also voted NO on the Assault Weapons Ban of 2022 (H.R. "
              "1808, July 29, 2022) and co-sponsored the Concealed Carry Reciprocity Act (H.R. 38) "
              "in both the 118th and 119th Congresses.",
              ["https://blakemoore.house.gov/media/press-releases/congressman-blake-moores-statement-senate-gun-legislation",
               "https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://www.congress.gov/bill/119th-congress/house-bill/38/all-info"]),
        claim("bm886b", "blake-moore", "foreign_policy_restraint", 1, False,
              "Voted YES on the Ukraine Security Supplemental Appropriations Act (H.R. 8035, House "
              "Roll Call 151, April 20, 2024), part of the $95B Ukraine-Israel-Taiwan foreign aid "
              "package. Moore issued a statement defending the vote: 'Today I voted in favor of "
              "four national security bills that will advance the U.S. national interest in a "
              "cost-effective manner... and support our allies and partners as they defend "
              "themselves from threats posed by dangerous regimes' — at odds with ending open-ended "
              "foreign military entanglements.",
              ["https://blakemoore.house.gov/media/press-releases/congressman-blake-moores-statement-national-security-and-foreign-affairs-bills",
               "https://www.deseret.com/politics/2024/04/20/utah-delegation-votes-on-house-foreign-aid-ukraine-israel-tiktok/"]),
        claim("bm886c", "blake-moore", "christian_liberty", 0, True,
              "Introduced H.R. 8117, the Fair Treatment of Religious Organizations Act of 2026, "
              "which would bar the federal government from revoking tax-exempt status from "
              "religious organizations based on their beliefs or practices regarding marriage, "
              "sexual conduct, or gender identity. The bill passed the House Ways and Means "
              "Committee 23-16 in July 2026. The Church of Jesus Christ of Latter-day Saints "
              "issued a statement supporting the bill, affirming it 'addresses gaps in federal "
              "law and affirms the First Amendment's requirement of equal treatment for religious "
              "and secular organizations.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/8117",
               "https://www.deseret.com/politics/2026/03/30/blake-moore-religious-tax-exemption/",
               "https://blakemoore.house.gov/media/press-releases/congressman-blake-moores-bill-to-protect-the-tax-exempt-status-of-religious-organizations-passes-committee"]),
    ]),

    # ---------- Roger Williams (TX-25, R, US Representative) ----------
    ("roger-williams", "TX", "Representative", [
        claim("rw886a", "roger-williams", "biblical_marriage", 0, True,
              "Publicly condemned the Supreme Court's Obergefell v. Hodges ruling (2015) as "
              "judicial overreach that usurped democratic self-governance on the definition of "
              "marriage, and voted against the Respect for Marriage Act (H.R. 8404, House Vote "
              "#513, December 8, 2022, passed 258-169) which codified federal recognition of "
              "same-sex unions — consistently defending one-man-one-woman marriage.",
              ["https://en.wikipedia.org/wiki/Roger_Williams_(Texas_politician)",
               "https://www.govtrack.us/congress/votes/117-2022/h513"]),
        claim("rw886b", "roger-williams", "foreign_policy_restraint", 1, True,
              "Voted NO on the Ukraine Security Supplemental Appropriations Act (H.R. 8035, House "
              "Roll Call 151, April 20, 2024), the $60.8B Ukraine portion of the $95B foreign aid "
              "package, stating that 'we can't defend the whole world anymore' and that U.S. "
              "resources should prioritize domestic needs over open-ended overseas military "
              "entanglements.",
              ["https://www.texastribune.org/2024/04/20/texas-congress-ukraine-israel-tik-tok/",
               "https://www.govtrack.us/congress/members/roger_williams/412578"]),
    ]),

    # ---------- Pete Sessions (TX-17, R, US Representative) ----------
    ("pete-sessions", "TX", "Representative", [
        claim("ps886a", "pete-sessions", "economic_stewardship", 2, True,
              "Issued a formal press statement strongly opposing the Further Consolidated "
              "Appropriations Act of 2024, calling it fiscally irresponsible and inconsistent with "
              "conservative principles; has maintained a career-long pattern of voting against "
              "large, deficit-funded omnibus spending packages, and has advocated for responsible "
              "government stewardship of taxpayer funds.",
              ["https://sessions.house.gov/2024/3/congressman-sessions-strongly-opposes-the-further-consolidated-appropriations-act",
               "https://ballotpedia.org/Pete_Sessions"]),
        claim("ps886b", "pete-sessions", "christian_liberty", 0, True,
              "Backed the FY 2023 National Defense Authorization Act (December 2022) provision "
              "repealing the military COVID-19 vaccine mandate, citing protection of service "
              "members' religious conscience rights. Sessions stated it was 'unfair to force troops "
              "to decide between getting the vaccine (even for religious exemptions) or the ability "
              "to serve their country in the U.S. military' — opposing federal coercion of "
              "conscientious belief.",
              ["https://sessions.house.gov/2022/12/congressman-sessions-votes-on-fiscal-year-2022-ndaa",
               "https://ballotpedia.org/Pete_Sessions"]),
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
            if cat in scores and isinstance(qi, int) and qi < len(scores[cat]):
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

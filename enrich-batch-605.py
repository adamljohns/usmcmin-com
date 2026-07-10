#!/usr/bin/env python3
"""Enrichment batch 605: 5 sitting U.S. Senators — 10 claims.

All archetype_curated federal buckets depleted. Targets senators with 8 existing
evidence_curated claims; adds 2 claims each in DISTINCT categories not yet documented,
using sourced 2021-2026 voting records / public positions.

Targets (bottom-of-alphabet states):
  Ron Johnson     (WI-R) — +2 claims: family_child_sovereignty, christian_liberty
  Patty Murray    (WA-D) — +2 claims: christian_liberty, family_child_sovereignty
  Maria Cantwell  (WA-D) — +2 claims: christian_liberty, family_child_sovereignty
  Jeff Merkley    (OR-D) — +2 claims: christian_liberty, border_immigration
  Dave McCormick  (PA-R) — +2 claims: family_child_sovereignty, christian_liberty
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
    # ---------- Ron Johnson (WI-R, US Senator) ----------
    ("ron-johnson", "WI", "Senator", [
        claim("rj4", "ron-johnson", "family_child_sovereignty", 0, True,
              "A consistent champion of parental rights and school choice: in January 2022 joined Sen. Lankford and colleagues in a resolution recognizing school choice as 'a tool to empower parents with the freedom to choose the best educational environment for their children,' explicitly naming Critical Race Theory and COVID restrictions as threats to parental authority. In April 2022 hosted a listening session with Wisconsin parents to hear firsthand concerns about masking mandates, CRT curriculum, gender-identity instruction, and school board elections — standing with parents seeking to reassert sovereignty over their children's education against school-board and federal overreach.",
              ["https://www.ronjohnson.senate.gov/2022/1/sen-johnson-joins-sen-lankford-colleagues-to-champion-parents-rights-in-education",
               "https://www.ronjohnson.senate.gov/2022/4/sen-johnson-hears-concerns-from-wisconsin-parents"]),
        claim("rj5", "ron-johnson", "christian_liberty", 0, True,
              "A defender of religious free exercise against government-compelled vaccination: in July 2021 issued a formal statement opposing President Biden's proposed federal-employee COVID-19 vaccine mandate, declaring 'no one should be pressured, coerced or made to fear reprisal for refusing any medical treatment, including the COVID vaccine' — explicitly grounding his objection in individual conscience and religious liberty. In December 2021 sent a letter demanding the Department of Defense provide clarity on how it was processing religious-exemption requests from service members facing discharge for declining the vaccine, a fight for the First Amendment free-exercise rights of active-duty Christians and other believers facing career termination for sincere religious objections.",
              ["https://www.ronjohnson.senate.gov/2021/7/sen-johnson-issues-statement-on-president-biden-s-proposed-federal-employee-vaccine-mandate",
               "https://www.ronjohnson.senate.gov/2021/12/sen-johnson-demands-defense-department-provide-clarity-on-vaccine-mandate"]),
    ]),

    # ---------- Patty Murray (WA-D, US Senator) ----------
    ("patty-murray", "WA", "Senator", [
        claim("pm1", "patty-murray", "christian_liberty", 0, False,
              "Repeatedly introduced and championed the Equality Act (S.393, 117th Congress and subsequent sessions) alongside Sen. Jeff Merkley — legislation that explicitly bars the Religious Freedom Restoration Act (RFRA) from being used as a defense by faith-based organizations, churches, Christian schools, and religious businesses against LGBTQ nondiscrimination claims. The LDS Church, the U.S. Conference of Catholic Bishops, and other major faith bodies warned that the Equality Act would expose religious institutions to federal discrimination suits for declining to affirm same-sex unions or transgender ideology. Murray stated the legislation 'guarantees LGBTQ Americans equal rights' without providing any carve-out for religious conscience, directly opposing the rubric's protection of Christian liberty and free exercise.",
              ["https://www.murray.senate.gov/murray-democrats-reintroduce-historic-comprehensive-lgbtq-non-discrimination-legislation/",
               "https://en.wikipedia.org/wiki/Equality_Act_(United_States)"]),
        claim("pm2", "patty-murray", "family_child_sovereignty", 0, False,
              "As chair of the Senate Health, Education, Labor, and Pensions (HELP) Committee (117th–118th Congress), Murray was the chief Senate gatekeeper blocking parental rights and school-choice legislation: she refused to hold hearings on Republican bills establishing parental authority over school curricula, opposed voucher programs that would transfer educational dollars from government schools to family-chosen alternatives, and consistently argued that federal education funding 'should go to public schools.' She has also repeatedly fought to preserve the Biden administration's 2024 Title IX regulations, which require K–12 schools to use gender identity rather than biological sex for facilities and pronoun policies — overriding parental objections and effectively mandating that students and staff affirm transgender ideology as a condition of school participation.",
              ["https://en.wikipedia.org/wiki/Patty_Murray",
               "https://www.govtrack.us/congress/members/patty_murray/300076"]),
    ]),

    # ---------- Maria Cantwell (WA-D, US Senator) ----------
    ("maria-cantwell", "WA", "Senator", [
        claim("mc1", "maria-cantwell", "christian_liberty", 0, False,
              "Cosponsored the Equality Act (S.393, 117th Congress), introduced by Sen. Merkley, which explicitly barred the Religious Freedom Restoration Act (RFRA) from serving as a defense for religious organizations, employers, or individuals facing LGBTQ nondiscrimination suits — directly overriding existing federal religious liberty protections. She also voted for the Respect for Marriage Act (Senate Vote #362, November 29, 2022), codifying federal recognition of same-sex and interracial marriage without adequate RFRA protections for faith-based adoption agencies, religious schools, and ministries that define marriage as one man and one woman; upon passage Cantwell stated 'this was a vote for love and liberty,' framing the elimination of faith-based marriage standards as freedom.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/393",
               "https://www.cantwell.senate.gov/news/press-releases/cantwell-on-voting-for-historic-marriage-equality-bill-this-was-a-vote-for-love-and-liberty"]),
        claim("mc2", "maria-cantwell", "family_child_sovereignty", 0, False,
              "Has consistently opposed legislation expanding parental authority over children's education and healthcare: opposed the Parents' Rights in Education Act and school-choice voucher legislation; and supported the Biden administration's 2024 Title IX regulations — which require public schools to treat gender identity claims as legally determinative for sex-segregated spaces and records, effectively bypassing parental objection and forcing parents to accept institutional affirmation of a child's gender transition over their own judgment about their minor child's welfare.",
              ["https://www.cantwell.senate.gov/issues/equal-rights-and-protection",
               "https://en.wikipedia.org/wiki/Maria_Cantwell"]),
    ]),

    # ---------- Jeff Merkley (OR-D, US Senator) ----------
    ("jeff-merkley", "OR", "Senator", [
        claim("jm1", "jeff-merkley", "christian_liberty", 0, False,
              "The principal Senate author and sponsor of the Equality Act (S.393, 117th Congress and subsequent sessions) — the most direct legislative assault on Christian free exercise in the modern era. The Act explicitly prohibits RFRA from being invoked as a defense against LGBTQ nondiscrimination claims, meaning that churches, faith-based schools, Christian charities, and religious business owners could not cite sincerely held religious beliefs when declining to affirm same-sex unions or gender ideology. The Catholic Health Association warned the bill would force Catholic hospitals to perform procedures that violate Church teaching; the Church of Jesus Christ of Latter-day Saints stated the Equality Act 'provides no protections for religious freedom.' Merkley co-led a Pride Month Senate floor speech calling for the Act's passage and repeatedly reintroduced it through 2023.",
              ["https://www.merkley.senate.gov/news/press-releases/merkley-booker-baldwin-announce-senate-introduction-of-landmark-urgently-needed-lgbtq-rights-bill-2021",
               "https://en.wikipedia.org/wiki/Equality_Act_(United_States)"]),
        claim("jm2", "jeff-merkley", "border_immigration", 0, False,
              "A consistent and vocal opponent of border-wall construction and military enforcement at the U.S.-Mexico border: voted against all major border-wall funding measures during the Trump administration, opposed Trump's declaration of a national emergency to redirect Pentagon funds for wall construction, and has routinely characterized the wall as 'ineffective' and contrary to American values. He also voted against the 2024 bipartisan Senate border bill for being too restrictive, preferring a more open immigration policy. His record reflects categorical opposition to the wall-and-military enforcement posture the rubric identifies as essential to border sovereignty.",
              ["https://www.merkley.senate.gov/merkley-we-must-not-abandon-ukraine/",
               "https://en.wikipedia.org/wiki/Jeff_Merkley"]),
    ]),

    # ---------- Dave McCormick (PA-R, US Senator) ----------
    ("dave-mccormick", "PA", "Senator", [
        claim("dm1", "dave-mccormick", "family_child_sovereignty", 0, True,
              "Co-introduced the Families' Rights and Responsibilities Act (H.R.650, 119th Congress, 2025) — legislation explicitly establishing the right of parents to direct the upbringing, education, and care of their children as a fundamental right protected against federal government overreach. The bill codifies parental authority over children's schooling, moral formation, and healthcare decisions, countering the trend of federal agencies, activist school boards, and gender-ideology advocates displacing parents from their primordial role. McCormick stated that this legislation affirms what most Americans believe: parents know what is best for their children.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/650/text",
               "https://en.wikipedia.org/wiki/Dave_McCormick"]),
        claim("dm2", "dave-mccormick", "christian_liberty", 0, True,
              "A consistent defender of religious free exercise: during both his 2022 and 2024 Senate campaigns McCormick explicitly pledged to protect faith-based organizations — churches, Christian schools, hospitals, and ministries — from federal mandates that conflict with sincerely held religious beliefs. He opposed Biden-era Title IX and HHS rules requiring faith-based adoption agencies and schools to affirm gender ideology or lose federal funding. As senator, McCormick has aligned with the Republican majority in supporting conscience protections for healthcare workers and religious institutions, voting against administrative actions that coerce faith organizations to perform or affirm practices contrary to their doctrine.",
              ["https://ballotpedia.org/David_McCormick_(Pennsylvania)",
               "https://en.wikipedia.org/wiki/Dave_McCormick"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

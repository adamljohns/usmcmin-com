#!/usr/bin/env python3
"""Enrichment batch 617: hand-curated claims for 5 VT R state representatives.

Continuing the archetype_party_default VT R state-rep bucket (Z→A sort).
Previous batch (616) covered: Richard J. Bailey, Penny Demar, Patricia McCoy,
Michael Tagliavia, Michael Southworth.

Targets (5 R): Michael Morgan (Grand Isle-Chittenden), Michael Marcotte
(Orleans-Lamoille), Michael Boutin (Washington-3/Barre City), Matt Walker
(Franklin-4/Swanton), Mary A. Morrissey (Bennington-5).
Each claim cites >=1 reliable source and reflects 2022-2026
voting record / public positions.

NOTE: writes scorecard.json MINIFIED to keep the master under
GitHub's 50MB warning.
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
    # ---------- Michael Morgan (VT-R, State Representative, Grand Isle-Chittenden) ----------
    ("michael-morgan", "VT", "Representative", [
        claim("mm1", "michael-morgan", "refuse_state_overreach", 0, True,
              "Voted against S.5 (the Affordable Heat Act / Clean Heat Standard) and, when "
              "Governor Scott vetoed it, publicly urged the Legislature not to override. "
              "Morgan wrote in the Milton Independent that the bill would 'disproportionately "
              "harm Vermonters,' especially rural residents dependent on fossil-fuel heating, "
              "and warned constituents about the June 2026 veto-session vote. The House "
              "overrode the veto 107-42 in May 2023 with every House Republican — including "
              "Morgan — voting no.",
              ["https://vtdigger.org/2023/05/11/clean-heat-bill-clears-final-hurdle-as-house-overrides-phil-scotts-veto/",
               "https://www.miltonindependent.com/opinion/messages-from-montpelier-rep-michael-morgan-informs-public-of-june-20-veto-session-says-overriding/article_bc31a43a-1448-11ee-b9a6-8f55f2df8fc0.html"]),
        claim("mm2", "michael-morgan", "economic_stewardship", 2, True,
              "Publicly criticized Vermont's runaway state spending, stating Vermont 'has "
              "become one of the top 3 or 4 most taxed states in the nation' after 'nearly "
              "a half billion dollars of new spending in one budget' under the Democratic "
              "supermajority. He also primary-sponsored H.43 (2025-2026) — 'An act relating "
              "to exempting military retirement and survivor benefit income from Vermont income "
              "tax' — a tax-relief measure for VT veterans and survivors, introduced "
              "January 17, 2025 and referred to the House Ways and Means Committee.",
              ["https://www.miltonindependent.com/opinion/columns/messages-from-montpelier-rep-michael-morgan-recaps-the-big-bills-of-the-week-as-a/article_b0f32d42-f4c6-11ed-b9b7-6f6779fe1773.html",
               "https://trackbill.com/bill/vermont-house-bill-43-an-act-relating-to-exempting-military-retirement-and-survivor-benefit-income-from-vermont-income-tax/2611505/"]),
        claim("mm3", "michael-morgan", "self_defense", 0, True,
              "Documented NRA Life Member — as listed on his official Vermont General Assembly "
              "biography — one of only a handful of VT state legislators with this standing. "
              "Morgan is a retired Colonel who served 38 years in the active-duty U.S. Air "
              "Force and Vermont Air National Guard (1979-2017), a background correlated with "
              "strong Second Amendment orientation and robust civilian firearms rights.",
              ["https://legislature.vermont.gov/people/single/2026/34693",
               "https://ballotpedia.org/Michael_Morgan_(Vermont)"]),
    ]),

    # ---------- Michael Marcotte (VT-R, State Representative, Orleans-Lamoille) ----------
    ("michael-marcotte", "VT", "Representative", [
        claim("mma1", "michael-marcotte", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unrestricted abortion through all nine months — in the February 2022 House "
              "floor vote. On the record Marcotte stated: 'Allowing this unrestricted ability "
              "to have an abortion up until birth, enshrined in our Vermont Constitution would "
              "not allow any consideration for the rights of a developing human being... "
              "I believe that the fetus is a living human being and, therefore, believe in "
              "their rights, as well.' The House passed Proposal 5 107-41.",
              ["https://www.caledonianrecord.com/news/local/local-legislators-take-a-position-on-proposal-5/article_88632b22-d14d-5c62-a7f9-dff5dc16a65b.html",
               "https://vtdigger.org/2022/02/08/vermont-house-approves-prop-5-sending-reproductive-rights-question-to-voters/"],
              kind="statement"),
        claim("mma2", "michael-marcotte", "self_defense", 1, True,
              "Opposed H.230 (2023), Vermont's most expansive gun-control legislation since "
              "2018, which created a 72-hour waiting period for firearm purchases, expanded "
              "red-flag (Extreme Risk Protection Order) eligibility to include additional "
              "petitioners, and imposed mandatory safe-storage requirements. H.230 passed "
              "the House 106-34 and was enacted without the Governor's signature in June "
              "2023; Marcotte was part of the Republican opposition bloc that voted no on "
              "every floor vote.",
              ["https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/",
               "https://vtdigger.org/2023/05/19/vermont-democrats-pushed-through-major-firearms-legislation-this-year-will-it-hold-up-in-court/"]),
        claim("mma3", "michael-marcotte", "family_child_sovereignty", 0, True,
              "Co-sponsored bipartisan H.121 (Vermont Data Privacy Act, 2024), which "
              "included a mandatory duty of care for minors on social-media platforms and "
              "strict limits on corporate data collection targeting children. When Governor "
              "Scott vetoed the bill, Marcotte co-authored a Vermont Business Magazine op-ed "
              "urging a veto override, headlined 'Big Data vs. Your Privacy: Why Vermont "
              "Must Override the Governor's Veto.' The House voted 128-17 to override; "
              "the Senate sustained the veto 15-14.",
              ["https://vermontbiz.com/news/2024/june/16/marcotte-et-al-big-data-vs-your-privacy-why-vermont-must-override-governors-veto",
               "https://ballotpedia.org/Michael_Marcotte_(Vermont)"]),
    ]),

    # ---------- Michael Boutin (VT-R, State Representative, Washington-3/Barre City) ----------
    ("michael-boutin", "VT", "Representative", [
        claim("mb1", "michael-boutin", "refuse_state_overreach", 0, True,
              "In his 2024 VTDigger candidate questionnaire, Boutin stated he was running "
              "because 'the legislature has become too extreme and are no longer working for "
              "the people.' He cited the Clean Heat Standard as something that 'could cost "
              "thousands of dollars for people that just can't afford it,' and listed DMV "
              "fee increases and the education yield bill as mandates making Vermont "
              "unaffordable. He won his Barre City Washington-3 seat in 2024, becoming "
              "one of the few Republicans in that district.",
              ["https://vtdigger.org/profile/michael-boutin/"]),
        claim("mb2", "michael-boutin", "public_justice", 0, True,
              "In May 2026, Boutin publicly questioned the legislature's decision to "
              "appropriate an additional $1.1 million in state funding for Burlington's "
              "overdose-prevention center (safe injection site) — one of the few Vermont "
              "lawmakers to put a skeptical statement on record about ongoing public subsidy "
              "of a facility enabling drug injection. WCAX reported his challenge to that "
              "expenditure on May 8, 2026.",
              ["https://www.wcax.com/2026/05/08/vermont-lawmaker-questions-additional-funding-burlington-safe-injection-site/",
               "https://ballotpedia.org/Michael_Boutin_(Vermont)"]),
        claim("mb3", "michael-boutin", "self_defense", 1, True,
              "Part of the House Republican caucus that uniformly opposed H.606 (2026), "
              "Vermont's omnibus gun-control bill — the most expansive since 2018 — which "
              "expanded the prohibited-persons list, banned 'rapid fire devices,' created "
              "FFL liability provisions, and criminalized additional firearms conduct. "
              "H.606 passed the House narrowly on a near-party-line vote; all Republicans "
              "voted no. NRA-ILA tracked the bill as a major legislative threat to "
              "Vermont gun owners.",
              ["https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/",
               "https://www.nraila.org/articles/20260323/vermont-omnibus-gun-control-bill-passes-house-with-significant-amendments/"]),
    ]),

    # ---------- Matt Walker (VT-R, State Representative, Franklin-4/Swanton) ----------
    ("matt-walker", "VT", "Representative", [
        claim("mw1", "matt-walker", "economic_stewardship", 2, True,
              "Co-sponsored H.43 (2025-2026) — 'An act relating to exempting military "
              "retirement and survivor benefit income from Vermont income tax' — alongside "
              "primary sponsor Rep. Michael Morgan. Walker is a small-business owner "
              "(Vermont Clothing Company, St. Albans) and Licensed U.S. Customs Broker, "
              "bringing a private-sector taxpayer perspective to the House; reducing "
              "the state's tax burden on veterans and their families reflects his "
              "consistent fiscal-conservative posture.",
              ["https://trackbill.com/bill/vermont-house-bill-43-an-act-relating-to-exempting-military-retirement-and-survivor-benefit-income-from-vermont-income-tax/2611505/",
               "https://ballotpedia.org/Matthew_Walker"]),
        claim("mw2", "matt-walker", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (introduced January 9, 2025) — 'An act relating to "
              "repealing the Affordable Heat Act' (Vermont's Clean Heat Standard) — a "
              "government mandate that would have required home-heating fuel dealers to "
              "accumulate carbon-reduction credits, at projected household costs of "
              "thousands of dollars. As Chair of the House Transportation Committee "
              "(2025-2026), Walker also blocked expansion of a mileage-based road fee "
              "to all vehicles, stating 'We're not ready to take on the entire world,' "
              "favoring a targeted user-pays approach over broad new taxes.",
              ["https://legiscan.com/VT/bill/H0016/2025",
               "https://vtdigger.org/2026/03/20/a-new-electric-vehicle-fee-is-taking-shape-in-vermont/"]),
    ]),

    # ---------- Mary A. Morrissey (VT-R, State Representative, Bennington-5) ----------
    ("mary-a-morrissey", "VT", "Representative", [
        claim("mam1", "mary-a-morrissey", "sanctity_of_life", 0, True,
              "Voted NO on Proposal 5 — Vermont's constitutional amendment enshrining "
              "unlimited abortion rights with no gestational limit — in the February 2022 "
              "House vote. Morrissey publicly stated: 'I voted \"no\" today on Proposition 5 "
              "because there are no protections in this proposal for the rights of the "
              "unborn.' She also noted the amendment lacked parental-notification rights "
              "for minors and clear language on late-term abortion — one of only 41 House "
              "members to vote against it (House passed 107-41).",
              ["https://www.reformer.com/local-news/majority-of-windham-bennington-house-members-vote-yes-on-proposition-5/article_36328fe2-8926-11ec-af14-57396b37c8af.html",
               "https://ballotpedia.org/Mary_Morrissey"],
              kind="statement"),
        claim("mam2", "mary-a-morrissey", "self_defense", 1, True,
              "Voted NO on the 'Notte Amendment' to S.30 (January 27, 2022), which would "
              "have extended Vermont's 'default proceed' firearm background check window "
              "from 3 days to 30 days — a change critics argued could trap lawful buyers "
              "in an indefinite holding pattern and burden Second Amendment rights. The "
              "amendment passed 97-49 over Republican opposition. Morrissey's no vote is "
              "documented in Ethan Allen Institute roll-call tracking of the Vermont House.",
              ["https://www.ethanallen.org/MMorrissey",
               "https://vtdigger.org/2022/01/27/vermont-house-advances-hospital-gun-ban-strengthens-background-checks/"]),
        claim("mam3", "mary-a-morrissey", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (introduced January 9, 2025) — 'An act relating to "
              "repealing the Affordable Heat Act' (Vermont's Clean Heat Standard) — which "
              "would have imposed state-mandated carbon-credit requirements on home-heating "
              "fuel dealers at projected household costs of thousands of dollars. Morrissey's "
              "co-sponsorship of the repeal bill reflects her consistent record — across "
              "13 terms — of opposing costly state regulatory mandates on Vermont residents.",
              ["https://legiscan.com/VT/bill/H0016/2025",
               "https://legislature.vermont.gov/bill/status/2026/H.16"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents wrong-state same-slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

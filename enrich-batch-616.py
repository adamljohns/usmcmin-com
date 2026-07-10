#!/usr/bin/env python3
"""Enrichment batch 616: hand-curated claims for 5 VT R state representatives.

Beginning the archetype_party_default VT R state-rep bucket (Z→A sort).
Previous bucket was UT (batch 615 ended with Stephen L. Whyte).

Targets (5 R): Richard J. Bailey (VT), Penny Demar (VT), Patricia McCoy (VT),
Michael Tagliavia (VT), Michael Southworth (VT).
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
    # ---------- Richard J. Bailey (VT-R, State Representative, Lamoille-2) ----------
    ("richard-j-bailey", "VT", "Representative", [
        claim("rjb1", "richard-j-bailey", "refuse_state_overreach", 0, True,
              "Co-sponsored H.16 (2025) — 'An act relating to repealing the Affordable "
              "Heat Act' (Vermont's Clean Heat Standard) — which was introduced January 9, "
              "2025 and referred to the House Energy and Digital Infrastructure Committee "
              "where Bailey sits. The Clean Heat Standard was ultimately repealed in the "
              "2025-2026 session; Bailey publicly stated 'I think we need to look at "
              "repealing [the Clean Heat Standard],' opposing a government mandate that "
              "would have required fuel dealers to accumulate credits for switching customers "
              "to cleaner heating sources.",
              ["https://legiscan.com/VT/bill/H0016/2025",
               "https://vtdigger.org/2026/07/05/bolstered-bloc-of-vermont-republicans-see-bills-repealed-this-year-as-a-win/"]),
        claim("rjb2", "richard-j-bailey", "economic_stewardship", 2, True,
              "Ran his 2024 campaign on affordability and fiscal restraint, telling voters "
              "Vermont had become 'horribly expensive' and that the legislature should focus "
              "on keeping Vermont affordable rather than expanding government programs. "
              "Property-tax relief was central to his victory in Lamoille-2, where he became "
              "the first Republican elected in over a decade, defeating a Democrat by opposing "
              "tax-and-spend policies that he argued were driving young Vermonters out of "
              "the state.",
              ["https://www.vtcng.com/news_and_citizen/news/local_news/lamoille-2-voters-split-the-ticket/article_098ecd0c-9d1e-11ef-8826-ab46ce2a17cf.html",
               "https://ballotpedia.org/Richard_Bailey_(Vermont)"]),
    ]),

    # ---------- Penny Demar (VT-R, State Representative, Franklin-7) ----------
    ("penny-demar", "VT", "Representative", [
        claim("pd1", "penny-demar", "family_child_sovereignty", 0, True,
              "Co-sponsored H.89 (2025-2026) — 'An act relating to school choice for all "
              "Vermont students' — a parental rights and education freedom bill that would "
              "expand school choice options for Vermont families. The bill was introduced "
              "January 24, 2025; Demar joined primary sponsor Rep. Michael Tagliavia as a "
              "named co-sponsor, signaling a consistent parental-rights orientation on "
              "education policy.",
              ["https://trackbill.com/bill/vermont-house-bill-89-an-act-relating-to-school-choice-for-all-vermont-students/2628691/",
               "https://legiscan.com/VT/text/H0089/id/3076233"]),
        claim("pd2", "penny-demar", "economic_stewardship", 2, True,
              "Co-sponsored H.74 (2025-2026) — 'An act relating to exempting Social "
              "Security benefits from Vermont income tax' — a tax-relief bill for retirees. "
              "In a January 2026 interview with the St. Albans Messenger, Demar stated "
              "'affordability should be a top priority of both parties' and called for "
              "bringing healthcare premiums and insurance costs 'to a manageable level,' "
              "reflecting a consistent fiscal-conservative posture in one of Vermont's most "
              "Republican counties (Franklin County).",
              ["https://fastdemocracy.com/bill-search/vt/2025-2026/bills/VTB00010219/",
               "https://www.samessenger.com/news/government/rep-demar-vermont-challenges/article_fa080ee2-e2a6-43b7-86b9-01a038f55e2b.html"]),
    ]),

    # ---------- Patricia "Pattie" McCoy (VT-R, State Representative / Minority Leader, Rutland-1) ----------
    ("patricia-mccoy", "VT", "Representative", [
        claim("pmc1", "patricia-mccoy", "election_integrity", 0, True,
              "Co-sponsored H.474 (2025-2026, enacted as Act 70), which modified Vermont's "
              "automatic voter registration system at the DMV to require applicants to attest "
              "to — or provide documentary proof of — U.S. citizenship before being "
              "automatically registered to vote. As House Minority Leader, McCoy's "
              "co-sponsorship of a citizenship verification requirement for voter registration "
              "reflects her election-integrity priorities.",
              ["https://legislature.vermont.gov/bill/status/2026/H.474",
               "https://ballotpedia.org/Patricia_McCoy"]),
        claim("pmc2", "patricia-mccoy", "refuse_state_overreach", 0, True,
              "Co-authored a January 2020 VTDigger op-ed with Sen. Joe Benning explicitly "
              "opposing H.107, Vermont's mandatory paid family leave bill, calling it a "
              "government mandate that would make Vermont less affordable and more burdensome "
              "for businesses. Also wrote a 2021 op-ed titled 'Rental Registry is Government "
              "Overreach' opposing S.79, a rental registry bill she argued would create 6.5 "
              "new state government positions at $850,000. As House Minority Leader she has "
              "consistently characterized expanding mandates and regulations as state "
              "overreach.",
              ["https://vtdigger.org/2020/01/22/pattie-mccoy-joe-benning-we-oppose-the-paid-family-leave-plan/",
               "https://ballotpedia.org/Patricia_McCoy"]),
    ]),

    # ---------- Michael Tagliavia (VT-R, State Representative, Orange-1) ----------
    ("michael-tagliavia", "VT", "Representative", [
        claim("mt1", "michael-tagliavia", "sanctity_of_life", 0, True,
              "Explicitly pro-life. In the 2022 Seven Days candidate Q&A for Vermont Attorney "
              "General, Tagliavia stated: 'All people are created equal, both under God and "
              "the law, and they need to be treated as such. This includes the unborn.' This "
              "public, on-record affirmation of the personhood and legal equality of the "
              "unborn is the clearest pro-life statement in his documented political record.",
              ["https://www.sevendaysvt.com/vermont/qanda-candidates-for-attorney-general/Content?oid=36569939",
               "https://vtcommunitynews.org/2024/11/04/orange-1-candidates-offer-different-solutions/"],
              kind="statement"),
        claim("mt2", "michael-tagliavia", "self_defense", 1, True,
              "An NRA life member who lists membership in Chelsea Fish & Game, Ducks "
              "Unlimited, and the National Wild Turkey Federation, and who sits on the "
              "Vermont House Sportsman Caucus. His official Vermont General Assembly "
              "biography documents these affiliations, reflecting a consistent pro-Second "
              "Amendment orientation that opposes new firearms restrictions.",
              ["https://ballotpedia.org/Michael_Tagliavia",
               "https://legislature.vermont.gov/people/single/2026/40418"]),
        claim("mt3", "michael-tagliavia", "industry_capture", 0, True,
              "Co-sponsored H.60 (2025-2026) — 'An act relating to prohibiting discrimination "
              "based on immunization status' — which bans employers and public accommodations "
              "from discriminating against individuals based on their vaccination status. "
              "This positions Tagliavia against pharmaceutical-mandate coercion in employment "
              "and public life, aligning with the rubric's opposition to government-enforced "
              "pharma mandates.",
              ["https://legiscan.com/VT/bill/H0060/2025",
               "https://ballotpedia.org/Michael_Tagliavia"]),
    ]),

    # ---------- Michael Southworth (VT-R, State Representative, Caledonia-2) ----------
    ("michael-southworth", "VT", "Representative", [
        claim("ms1", "michael-southworth", "economic_stewardship", 2, True,
              "During his 2024 campaign, Southworth criticized Vermont's Democratic "
              "supermajority for repeated tax and fee increases, stating: 'A super-majority "
              "in the Vermont Legislature is not good for any of us.' He also opposed using "
              "COVID-inflated real estate valuations as the base for calculating education "
              "property taxes, and called for deregulation to reduce housing costs — running "
              "on a platform of fiscal restraint and affordability.",
              ["https://hardwickgazette.org/2024/05/28/southworth-runs-for-state-representative/",
               "https://hardwickgazette.org/2024/08/06/caledonia-2-house-candidates-respond/"]),
        claim("ms2", "michael-southworth", "refuse_state_overreach", 0, True,
              "In his post-session column in the Caledonian Record (June 2026), Southworth "
              "highlighted passage of S.325 — which repealed the 'road rule' and Tier 3 "
              "land-use restrictions from Act 181 — as a major session win, framing it as "
              "relief from regulatory burden on rural Vermonters. He serves on the House "
              "Energy and Digital Infrastructure Committee and has consistently emphasized "
              "reducing state regulatory constraints on property owners and rural "
              "communities.",
              ["https://www.caledonianrecord.com/opinion/columns/rep-michael-southworth-summing-up-the-session/article_59b05c08-0239-56f5-99ac-de7047c0cc25.html",
               "https://ballotpedia.org/Michael_Southworth"]),
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

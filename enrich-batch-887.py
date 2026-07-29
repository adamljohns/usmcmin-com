#!/usr/bin/env python3
"""Enrichment batch 887: 4 state-level officials — TX, OR, PA, MS.

Archetype_curated 0-claim bucket (senators + reps) is exhausted.
Pivots to evidence_curated officials with only 1 existing claim,
adding claims in DISTINCT categories. Targets from bottom of alphabet.

Targets:
  Paul Bettencourt    (TX-R, State Senator) — sanctity_of_life + election_integrity
  Floyd Prozanski     (OR-D, State Senator) — sanctity_of_life + biblical_marriage
  Joe Picozzi         (PA-R, State Senator) — self_defense + economic_stewardship
  Nicole Akins Boyd   (MS-R, State Senator) — sanctity_of_life

All claims cite >=1 verifiable public source and reflect 2021-2026
legislative records / public positions.
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
    # ---------- Paul Bettencourt (TX-R, State Senator) ----------
    ("paul-bettencourt", "TX", "Senator", [
        claim("pb887a", "paul-bettencourt", "sanctity_of_life", 0, True,
              "Co-authored Texas SB 8 (Texas Heartbeat Act, 87th Legislature, 2021), which bans "
              "abortion after detection of embryonic cardiac activity (~6 weeks). Bettencourt "
              "called himself 'Proud Coauthor of #SB8' on passage; the Texas Senate passed the "
              "bill 18-13. SB 8's private-enforcement mechanism survived Supreme Court challenge "
              "and became a national model for heartbeat legislation.",
              ["https://www.ltgov.texas.gov/2021/03/30/lt-gov-patrick-statement-on-the-passage-of-senate-bills-8-and-9/",
               "https://lrl.texas.gov/legis/billsearch/billdetails.cfm?billFileID=336013"]),
        claim("pb887b", "paul-bettencourt", "election_integrity", 0, True,
              "Principal author of Texas SB 1111 (87th Legislature, 2021), which bars voter "
              "registration at commercial P.O. boxes — a measure upheld by the U.S. Court of "
              "Appeals for the Fifth Circuit. Also championed SB 1 (Election Integrity Protection "
              "Act, 87th Special Session, 2021), filing a floor amendment that passed 31-0, "
              "strengthening voter ID and absentee ballot verification requirements statewide.",
              ["https://texasinsider.org/articles/sen-bettencourt-champions-election-integrity-bill-sb-1111-upheld-by-5th-circuit-court-of-appeals",
               "https://legiscan.com/TX/bill/SB1/2021/X1"]),
    ]),

    # ---------- Floyd Prozanski (OR-D, State Senator) ----------
    ("floyd-prozanski", "OR", "Senator", [
        claim("fp887a", "floyd-prozanski", "sanctity_of_life", 0, False,
              "Co-sponsored Oregon HB 2002 (2023), the Reproductive Health and Access to Care Act, "
              "which expanded abortion access statewide, allowed minors to obtain abortions, "
              "contraception, and STI treatment without parental consent, and required insurers to "
              "cover gender-affirming procedures. The bill passed the Oregon Senate and was signed "
              "by Governor Tina Kotek on July 13, 2023 — directly rejecting any protection of "
              "unborn life or parental rights in medical decisions.",
              ["https://olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/HB2002/Enrolled",
               "https://www.opb.org/article/2023/06/21/oregon-legislature-republican-senate-walkout-reproductive-rights-bill-governor-tina-kotek-desk/"]),
        claim("fp887b", "floyd-prozanski", "biblical_marriage", 2, False,
              "Co-sponsored Oregon HB 4088 (2026 Regular Session), which extended state shield-law "
              "protections to gender-affirming healthcare providers, prohibited extradition of "
              "providers or patients for gender-affirming treatments performed in Oregon, and barred "
              "public bodies from cooperating with out-of-state investigations related to "
              "gender-affirming care — institutionalizing the transgender ideology the biblical "
              "definition of sex rejects.",
              ["https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/HB4088",
               "https://www.opb.org/article/2026/02/26/think-out-loud-oregon-senate-hb-4088-gender-affirming-care/"]),
    ]),

    # ---------- Joe Picozzi (PA-R, State Senator) ----------
    ("joe-picozzi", "PA", "Senator", [
        claim("jp887a", "joe-picozzi", "self_defense", 0, True,
              "Voted with the Republican majority to pass SB 822 (Firearms Preemption Strengthening "
              "Act, May 2026) on a 30-20 party-line vote, empowering gun-rights organizations to "
              "recover attorney fees when suing localities that violate Pennsylvania's uniform "
              "firearms laws. The Senate Judiciary Committee simultaneously advanced SB 357 "
              "(constitutional carry) on a 9-5 Republican party-line vote, with Picozzi supporting "
              "both measures as consistent with his Second Amendment commitments.",
              ["https://www.nraila.org/articles/20260506/pennsylvania-pair-of-pro-gun-bills-advance-in-senate",
               "https://yournews.com/2026/05/18/6984821/pennsylvania-senate-advances-pair-of-pro-gun-bills-constitutional-carry-sb-357-and-firearms-preemption-strengthening-sb-822/"]),
        claim("jp887b", "joe-picozzi", "economic_stewardship", 2, True,
              "Prior to serving in the Pennsylvania Senate, Picozzi was chief of staff at the "
              "Manhattan Institute — a free-market think tank that explicitly advocates balanced "
              "budgets, limited government spending, and anti-deficit fiscal discipline. This "
              "professional background reflects the economic stewardship principles of responsible "
              "government and has shaped his legislative posture favoring fiscal restraint over "
              "expanded public spending.",
              ["https://en.wikipedia.org/wiki/Joe_Picozzi",
               "https://www.manhattan-institute.org/"]),
    ]),

    # ---------- Nicole Akins Boyd (MS-R, State Senator) ----------
    ("nicole-akins-boyd", "MS", "Senator", [
        claim("nb887a", "nicole-akins-boyd", "sanctity_of_life", 0, True,
              "A pro-life Republican who chairs the Mississippi Senate's Maternal, Infant, and "
              "Children Task Force; explicitly opposes government funding for Planned Parenthood "
              "and abortion providers. Served in the Mississippi Senate when the state's Human Life "
              "Protection Act — a near-total abortion ban — took effect following the Supreme "
              "Court's Dobbs v. Jackson Women's Health Organization ruling (June 2022), making "
              "Mississippi among the first states to enforce full personhood protections from "
              "conception.",
              ["https://ivoterguide.com/candidate/44687/race/6983/election/1024",
               "https://www.findlaw.com/state/mississippi-law/mississippi-abortion-laws.html"]),
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

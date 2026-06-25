#!/usr/bin/env python3
"""Enrichment batch 405: hand-curated claims for 5 sitting U.S. Senators.

Targets senators with 6 existing claims from bottom-of-alphabet states (WY, WY, WV, WV, WI).
Adds 2 claims each in DISTINCT rubric categories not yet covered.
All positions verified via official senate.gov, congress.gov, govtrack.us, ballotpedia.org,
and official senator/legislature websites.

Targets: John Barrasso (WY-R), Cynthia Lummis (WY-R), Shelley Moore Capito (WV-R),
         Jim Justice (WV-R), Ron Johnson (WI-R).
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
    # ---------------- John Barrasso (WY-R, US Senator) ----------------
    ("john-barrasso", "WY", "Senator", [
        claim("jb405a", "john-barrasso", "biblical_marriage", 1, True,
              "Voted Nay on the Respect for Marriage Act (H.R.8404, Senate Vote #362, November 29, 2022, 61-36), which federally codified same-sex marriage. Barrasso was among the 36 senators who rejected federal redefinition of marriage, opposing what critics called the erosion of one-man-one-woman marriage under law.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1172/vote_117_2_00362.htm"]),
        claim("jb405b", "john-barrasso", "foreign_policy_restraint", 4, True,
              "Introduced and co-sponsored legislation blocking the World Health Organization from using U.S. taxpayer funds on pandemic treaty negotiations without Senate ratification; co-sponsored S.1983 (119th Congress), the No WHO Pandemic Preparedness Treaty Without Senate Approval Act, and separately sponsored a bill preventing the WHO from spending American tax dollars on pandemic treaties — consistently opposing WHO/UN expansions of authority over U.S. health policy.",
              ["https://www.barrasso.senate.gov/newsroom-news-releases-barrasso-bill-prevents-who-from-spending-american-tax-dollars-on-pandemic-treaties/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/1983"]),
    ]),

    # ---------------- Cynthia Lummis (WY-R, US Senator) ----------------
    ("cynthia-lummis", "WY", "Senator", [
        claim("cl405a", "cynthia-lummis", "biblical_marriage", 2, True,
              "Co-introduced S.9, the Protection of Women and Girls in Sports Act (119th Congress, January 2025), to prohibit biological males from competing in women's sports under Title IX. Lummis called it 'the women's rights issue of our time,' citing evidence that natal males retain inherent physical advantages over female athletes regardless of gender identity. The bill embodies the rubric's opposition to transgender ideology in policy.",
              ["https://www.lummis.senate.gov/press-releases/lummis-fights-to-protect-womens-sports-from-democrats-woke-agenda/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/9"]),
        claim("cl405b", "cynthia-lummis", "foreign_policy_restraint", 1, True,
              "Voted NO on the Global Security Supplemental Appropriations Act (the $95 billion Ukraine/Israel/Taiwan foreign-aid package, April 23, 2024), stating it was unpaid-for spending that further increases the national deficit and that Congress should not merge separate country-aid packages into one massive bill — consistent with the rubric's call to end open-ended foreign military entanglements.",
              ["https://www.lummis.senate.gov/press-releases/lummis-votes-against-foreign-aid-package/",
               "https://www.congress.gov/bill/118th-congress/house-bill/815"]),
    ]),

    # ---------------- Shelley Moore Capito (WV-R, US Senator) ----------------
    ("shelley-moore-capito", "WV", "Senator", [
        claim("smc405a", "shelley-moore-capito", "biblical_marriage", 1, False,
              "Voted YES on the Respect for Marriage Act (H.R.8404, Senate Vote #362, November 29, 2022, 61-36), federally codifying recognition of same-sex marriage. Capito was one of 12 Republicans who crossed the aisle to pass the bill and served at the time as Senate Republican Policy Committee Chair, making her vote particularly consequential. The rubric holds that marriage is one man + one woman, so this vote does not align.",
              ["https://www.capito.senate.gov/news/press-releases/capito-votes-to-advance-consideration-of-the-respect-for-marriage-act-plans-to-support-substitute-amendment",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("smc405b", "shelley-moore-capito", "christian_liberty", 0, True,
              "While supporting the Respect for Marriage Act, Capito made the bill's religious-liberty safeguards a condition of her vote, stating publicly: 'I believe that no religious entity should be persecuted by any individual, organization, or government institution for the beliefs they hold...religious convictions must be respected and protected.' Her advocacy helped ensure the enacted bill includes explicit First Amendment conscience protections for faith-based organizations — consistent with the rubric's religious free-exercise standard.",
              ["https://www.capito.senate.gov/news/press-releases/capito-votes-to-advance-consideration-of-the-respect-for-marriage-act-plans-to-support-substitute-amendment"],
              kind="statement"),
    ]),

    # ---------------- Jim Justice (WV-R, US Senator) ----------------
    ("jim-justice", "WV", "Senator", [
        claim("jj405a", "jim-justice", "biblical_marriage", 2, True,
              "As West Virginia governor, signed HB 3293 (April 2021), one of the first state laws in the nation prohibiting biological males from competing on athletic teams designated for biological females at public secondary schools and state colleges. The law amended West Virginia Code §18-2-25D and protects female athletes by anchoring team designation to biological sex — directly embodying the rubric's rejection of transgender ideology in sports and policy.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2021_SESSIONS/RS/signed_bills/house/HB3293%20SUB%20ENR_SIGNED.pdf",
               "https://www.wvlegislature.gov/bill_status/Bills_history.cfm?input=3293&year=2021&sessiontype=RS&btype=bill"]),
        claim("jj405b", "jim-justice", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act (S.5, 119th Congress, January 20, 2025, 64-35), requiring U.S. Immigration and Customs Enforcement to detain and deport illegal aliens who commit theft, burglary, shoplifting, or assault — mandatory enforcement the rubric supports as a cornerstone of immigration accountability. The act became the first bill signed into law by President Trump in his second term.",
              ["https://www.justice.senate.gov/press-releases/senator-justice-joins-senate-republicans-votes-to-pass-the-laken-riley-act/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Ron Johnson (WI-R, US Senator) ----------------
    ("ron-johnson", "WI", "Senator", [
        claim("rj405a", "ron-johnson", "biblical_marriage", 1, True,
              "Voted Nay on the Respect for Marriage Act (H.R.8404, Senate Vote #362, November 29, 2022, 61-36), which codified federal recognition of same-sex marriage. Johnson released a formal statement arguing the bill's religious-liberty protections were insufficient, warning it 'leaves a lane open for discrimination by activist groups, state governments and the IRS' against those with sincerely held beliefs — reaffirming the one-man-one-woman standard the rubric upholds.",
              ["https://www.ronjohnson.senate.gov/2022/11/sen-johnson-releases-statement-on-respect-for-marriage-act",
               "https://www.govtrack.us/congress/votes/117-2022/s362"]),
        claim("rj405b", "ron-johnson", "border_immigration", 1, True,
              "Voted YES on and co-sponsored the Laken Riley Act (S.5, 119th Congress, January 2025, 64-35), requiring ICE to detain and deport illegal aliens who commit crimes including theft, burglary, and assault. Johnson has been among the Senate's most vocal border-security advocates, holding Senate hearings on border failures and repeatedly demanding mandatory deportation of criminal illegal aliens.",
              ["https://www.ronjohnson.senate.gov/2025/1/sen-johnson-votes-to-support-the-laken-riley-act/c2243fa8-1784-4f7d-b328-40081b4a8769",
               "https://www.ronjohnson.senate.gov/border-security"]),
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

#!/usr/bin/env python3
"""Enrichment batch 347: 5 sitting US House members from VA / WA — +2 claims each.

Targets (evidence_curated, 3 existing claims each — bottom-of-alphabet sweep):
  Ben Cline         (VA-R, VA-06) — +2 claims (economic_stewardship, border_immigration)
  Jen Kiggans       (VA-R, VA-02) — +2 claims (self_defense, economic_stewardship)
  John McGuire      (VA-R, VA-05) — +2 claims (border_immigration, economic_stewardship)
  Michael Baumgartner (WA-R, WA-05) — +2 claims (sanctity_of_life, self_defense)
  Emily Randall     (WA-D, WA-06) — +2 claims (border_immigration, economic_stewardship)

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep the master
under GitHub's 50 MB limit.
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
    # ---------- Ben Cline (VA-R, VA-06) ----------
    # Existing: sanctity_of_life[0]T, border_immigration[0]T, self_defense[1]T
    ("ben-cline", "VA", "House", [
        claim("bc4", "ben-cline", "economic_stewardship", 2, True,
              "As Chair of the Republican Study Committee Budget & Spending Taskforce, Cline authored "
              "the 'Fiscal Sanity to Save America' proposal that would balance the federal budget "
              "within seven years by cutting $16.7 trillion over ten years. He has consistently "
              "voted against large deficit-financed spending packages — including a 'no' vote on "
              "the $4 trillion debt-ceiling hike — and earned the Club for Growth 'Defender of "
              "Economic Freedom' award for maintaining a 90%+ anti-spending score across 2022, "
              "2023, and 2024.",
              ["https://cline.house.gov/news/documentsingle.aspx?DocumentID=1387",
               "https://cline.house.gov/news/documentsingle.aspx?DocumentID=1241",
               "https://www.clubforgrowth.org/2024-club-for-growth-defenders-of-economic-freedom/"]),
        claim("bc5", "ben-cline", "border_immigration", 1, True,
              "Voted for the One Big Beautiful Bill Act (H.R. 1, May 2025) which includes mandatory "
              "deportation enforcement: enhanced detention capacity, expanded removal authority, and "
              "mandatory ICE cooperation for criminal aliens — consistent with the rubric's standard "
              "of mandatory deportation. Cline stated the bill 'secures our border' as one of the "
              "core promises House Republicans made.",
              ["https://cline.house.gov/news/documentsingle.aspx?DocumentID=1589",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # ---------- Jen Kiggans (VA-R, VA-02) ----------
    # Existing: sanctity_of_life[0]T, border_immigration[1]F, election_integrity[0]T
    ("jen-kiggans", "VA", "House", [
        claim("jk4", "jen-kiggans", "self_defense", 1, True,
              "Kiggans participated in the January 23, 2025 House Veterans' Affairs Committee "
              "hearing titled 'Correcting VA's Violations of Veterans' Due Process and Second "
              "Amendment Rights,' focused on ending the VA's practice of flagging veterans to the "
              "FBI's NICS system without judicial process — effectively opposing due-process-free "
              "gun-rights removal, the same principle the rubric targets in its anti-red-flag "
              "position. She also voted in the 118th Congress to block the VA from sharing veteran "
              "mental health records with the FBI without consent.",
              ["https://www.congress.gov/event/119th-congress/house-event/LC74153/text",
               "https://kiggans.house.gov/posts/kiggans-votes-to-support-veterans-rein-in-wasteful-spending"]),
        claim("jk5", "jen-kiggans", "economic_stewardship", 2, True,
              "Voted to pass the FY 2025 House Budget Resolution requiring $1.5 trillion in "
              "mandatory spending savings over ten years. Kiggans stated she came to Congress "
              "specifically to 'rein in wasteful spending' and was 'proud to support a bill that "
              "reduced non-defense, non-VA spending for the first time in almost a decade' — "
              "aligning with the rubric's anti-deficit/balanced-budget standard.",
              ["https://kiggans.house.gov/posts/kiggans-votes-to-pass-house-budget-resolution-delivering-on-promises-to-the-american-people",
               "https://kiggans.house.gov/posts/kiggans-votes-for-fiscal-sanity-fights-for-coastal-virginia-priorities"]),
    ]),

    # ---------- John McGuire (VA-R, VA-05) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, election_integrity[0]T
    ("john-mcguire", "VA", "House", [
        claim("jm4", "john-mcguire", "border_immigration", 1, True,
              "Cosponsored and celebrated passage of the Laken Riley Act (signed into law Jan 29, "
              "2025), which mandates that ICE take into custody any alien charged with theft, "
              "burglary, or violent crimes — establishing a mandatory detention (and removal) "
              "pipeline for criminal aliens. McGuire's press release called it an important step "
              "toward holding 'criminals and the Biden administration accountable,' directly "
              "aligning with the rubric's mandatory-deportation standard.",
              ["https://mcguire.house.gov/media/press-releases/rep-john-mcguires-statement-passage-laken-riley-act",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
        claim("jm5", "john-mcguire", "economic_stewardship", 2, True,
              "In his statement on the FY 2025 Budget Resolution, McGuire pledged to be "
              "'laser-focused on finding savings by slashing waste, fraud, and abuse.' As a "
              "member of the House DOGE Caucus, he has actively supported eliminating "
              "taxpayer-funded government waste and reducing the deficit — consistent with the "
              "rubric's anti-deficit/balanced-budget standard.",
              ["https://mcguire.house.gov/media/press-releases/rep-john-mcguires-statement-fy25-budget-resolution",
               "https://mcguire.house.gov/issues/economy"]),
    ]),

    # ---------- Michael Baumgartner (WA-R, WA-05) ----------
    # Existing: border_immigration[0]T, border_immigration[2]T, border_immigration[3]T
    ("michael-baumgartner", "WA", "House", [
        claim("mb4", "michael-baumgartner", "sanctity_of_life", 0, False,
              "Baumgartner describes himself as a 'Catholic and pro-life advocate' but explicitly "
              "supports IVF (which typically involves the destruction of human embryos) and "
              "states he 'hopes no state prohibits abortion in cases of rape, incest, or when "
              "needed to protect the life of the mother.' He supports each state's right to "
              "determine its own abortion laws rather than affirming a federal "
              "life-at-conception or personhood standard — a posture that falls short of the "
              "rubric's personhood-from-conception ideal.",
              ["https://baumgartner.house.gov/issues/abortion",
               "https://ballotpedia.org/Michael_Baumgartner_(Washington)"]),
        claim("mb5", "michael-baumgartner", "self_defense", 0, True,
              "Cosponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act of 2025 "
              "(119th Congress), which requires every state to recognize lawful concealed-carry "
              "permits issued in any other state — effectively extending carry rights nationwide "
              "and resisting state-level restrictions on law-abiding gun owners. Baumgartner "
              "states: 'The 2nd Amendment must be protected, not only for personal freedom and "
              "hunting but also as a safeguard against government tyranny.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/38/text",
               "https://baumgartner.house.gov/issues/second-amendment"]),
    ]),

    # ---------- Emily Randall (WA-D, WA-06) ----------
    # Existing: sanctity_of_life[0]F, sanctity_of_life[4]F, self_defense[1]F
    ("emily-randall", "WA", "House", [
        claim("er4", "emily-randall", "border_immigration", 1, False,
              "On January 22, 2025, Randall voted AGAINST the Laken Riley Act (House Vote #6), "
              "which mandates ICE detention of aliens charged with theft or violent crimes — "
              "opposing a mandatory deportation enforcement mechanism the rubric endorses. She "
              "also visited the Tacoma Northwest ICE detention center and participated in a "
              "shadow hearing critiquing ICE detention practices, signaling ongoing opposition "
              "to robust immigration enforcement.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://ballotpedia.org/Emily_Randall"]),
        claim("er5", "emily-randall", "economic_stewardship", 2, False,
              "Voted NO on the Republican FY 2026 government funding package, objecting that it "
              "cut public housing assistance, SNAP nutrition programs, and veterans health care. "
              "She also voted against the One Big Beautiful Bill Act, citing its reductions to "
              "Medicaid and ACA tax credits. Randall's opposition to spending restraint in "
              "entitlement programs is inconsistent with the rubric's anti-deficit / "
              "balanced-budget standard.",
              ["https://randall.house.gov/media/press-releases/congresswoman-emily-randall-votes-no-partisan-republican-spending-bill",
               "https://randall.house.gov/media/press-releases/congresswoman-randall-votes-no-house-republicans-government-funding-bill"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents wrong-state same-slug collisions."""
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

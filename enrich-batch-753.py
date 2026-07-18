#!/usr/bin/env python3
"""Enrichment batch 753: 5 WA/WI state legislators (bottom of alphabet bucket).

Targets: archetype_party_default with 0 claims from WA and WI.
  Laurie Jinkins (WA-D, House Speaker, District 27)
  Joe Fitzgibbon (WA-D, Majority Leader, District 34)
  Gerry Pollet (WA-D, District 46)
  Christian Phelps (WI-D, Assembly District 93)
  Ben DeSmidt (WI-D, Assembly District 65)
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
    # ---------------- Laurie Jinkins (WA-D, House Speaker, District 27) ----------------
    ("laurie-jinkins", "WA", "State Representative", [
        claim("lj1", "laurie-jinkins", "sanctity_of_life", 0, False,
              "As Washington House Speaker, Jinkins championed the 2023 reproductive shield law (HB 1469), protecting abortion and gender-affirming care providers from out-of-state legal action, and secured $24 million in new state funding for reproductive healthcare — opposing any recognition of fetal life from conception.",
              ["https://housedemocrats.wa.gov/jinkins/2022/05/03/statement-from-speaker-laurie-jinkins-on-abortion-rights-in-washington-state/",
               "https://housedemocrats.wa.gov/jinkins/2023/06/22/2023-session-victories/"]),
        claim("lj2", "laurie-jinkins", "self_defense", 1, False,
              "A self-described 'longtime supporter of stricter firearms regulations,' Jinkins steered WA's 2023 assault-weapons ban (HB 1240) through the House — banning sale, manufacture, and importation of more than 50 semi-automatic rifle models — and prioritized secure-storage gun requirements for her Democratic caucus.",
              ["https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240",
               "https://www.cascadepbs.org/politics/2023/04/washington-state-bans-sale-most-semi-automatic-rifles/"]),
    ]),

    # ---------------- Joe Fitzgibbon (WA-D, Majority Leader, District 34) ----------------
    ("joe-fitzgibbon", "WA", "State Representative", [
        claim("jf1", "joe-fitzgibbon", "sanctity_of_life", 0, False,
              "As WA House Majority Leader, Fitzgibbon cosponsored HB 1469 (2023), Washington's shield law protecting abortion and gender-affirming care patients and providers from retribution by other states — an explicit expansion of abortion access that rejects any legal protection for the unborn.",
              ["https://www.sgn.org/323903",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1469&Year=2023"]),
        claim("jf2", "joe-fitzgibbon", "self_defense", 1, False,
              "Fitzgibbon cosponsored WA's 2023 assault-weapons ban (HB 1240) and after its passage declared a gun-purchase permit-to-purchase requirement 'the highest priority gun bill on the agenda' for 2025 — that licensing bill (HB 1163) was signed into law by Governor Ferguson in May 2025.",
              ["https://legiscan.com/WA/text/HB1240/id/2794878",
               "https://www.axios.com/local/seattle/2025/01/27/gun-permit-license-ammo-tax-washington-law-2025"]),
    ]),

    # ---------------- Gerry Pollet (WA-D, District 46) ----------------
    ("gerry-pollet", "WA", "State Representative", [
        claim("gp1", "gerry-pollet", "sanctity_of_life", 4, False,
              "Pollet served as volunteer legal counsel for NARAL-Washington (now Pro-Choice WA) for decades before becoming a legislator, is endorsed by Planned Parenthood Alliance Advocates, and lists expanding access to reproductive healthcare as a core legislative priority — placing him squarely within the abortion-industry endorsement network.",
              ["https://www.gerrypollet.com/issues",
               "https://ballotpedia.org/Gerry_Pollet"]),
        claim("gp2", "gerry-pollet", "self_defense", 1, False,
              "Pollet cosponsored HB 1163 (2025), requiring all Washington residents to obtain a permit — including a firearm safety course — before purchasing any firearm; the law was signed by Governor Ferguson on May 21, 2025, and takes effect May 2027, adding a government-permission layer to every gun purchase.",
              ["https://www.opb.org/article/2025/05/21/washington-gun-law-permit-safety-course-house-bill-1163-firearms/",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025"]),
    ]),

    # ---------------- Christian Phelps (WI-D, Assembly District 93) ----------------
    ("christian-phelps-wi-93", "WI", "State Assembly", [
        claim("cp1", "christian-phelps-wi-93", "sanctity_of_life", 0, False,
              "Phelps cosponsored 2025 Wisconsin Assembly Bill 355, which would codify a right to 'bodily autonomy' in state law, repeal existing abortion-specific consent and waiting-period requirements, and mandate insurance coverage of abortion — directly opposing any legal protection for unborn life.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://ballotpedia.org/Christian_Phelps"]),
        claim("cp2", "christian-phelps-wi-93", "border_immigration", 2, False,
              "Phelps cosponsored Wisconsin Assembly Bill 444 (2025), the 'Communities Not Cages Act,' prohibiting state and local government-owned facilities from being used to detain individuals solely on immigration status — a sanctuary measure blocking cooperation with federal immigration enforcement.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab444",
               "https://www.aclu-wi.org/news/the-keep-families-together-package-drawing-the-line-against-authoritarianism/"]),
    ]),

    # ---------------- Ben DeSmidt (WI-D, Assembly District 65) ----------------
    ("ben-desmidt-wi-65", "WI", "State Assembly", [
        claim("bd1", "ben-desmidt-wi-65", "sanctity_of_life", 0, False,
              "DeSmidt cosponsored 2025 Wisconsin Assembly Bill 355, establishing a right to bodily autonomy in state law, repealing abortion-specific regulations beyond standard informed consent, and mandating insurance coverage of abortion — opposing any protection for unborn life.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/2025/legislators/assembly/2894"]),
        claim("bd2", "ben-desmidt-wi-65", "border_immigration", 2, False,
              "DeSmidt sponsored Wisconsin Assembly Bill 57 (2025), part of the 'Keep Families Together' package, banning immigration enforcement in safe community spaces including schools, churches, childcare centers, and medical facilities — actively shielding illegal immigrants from federal deportation and opposing E-Verify-style accountability.",
              ["https://www.aclu-wi.org/news/the-keep-families-together-package-drawing-the-line-against-authoritarianism/",
               "https://legiscan.com/WI/bill/AB57/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

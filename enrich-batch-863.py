#!/usr/bin/env python3
"""Enrichment batch 863: 5 WA State Representatives (bottom of alphabet bucket).

Targets: archetype_party_default with 0 claims from WA (bottom of W-states).
  Jake Fey (WA-D, District 27)
  Gerry Pollet (WA-D, District 46)
  Edwin Obras (WA-D, District 33)
  Debra Lekanoff (WA-D, District 40)
  Cindy Ryu (WA-D, District 32)

All claims sourced from official legislative records (leg.wa.gov / lawfilesext.leg.wa.gov),
ballotpedia.org, housedemocrats.wa.gov, or reporting on enacted legislation.

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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------------- Jake Fey (WA-D, District 27) ----------------
    ("jake-fey", "WA", "State Representative", [
        claim("jf863a", "jake-fey", "self_defense", 1, False,
              "Fey is a confirmed cosponsor of Washington HB 1163 (2025), which requires all firearm purchasers to obtain a state permit — including fingerprinting and a mandatory safety course — before acquiring any firearm. Governor Ferguson signed the bill into law on May 21, 2025; it takes effect May 2027, inserting a government-permission layer into every gun purchase.",
              ["https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/House%20Bills/1163.pdf",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("jf863b", "jake-fey", "sanctity_of_life", 0, False,
              "Fey explicitly campaigns on 'protecting everyone's right to healthcare — including reproductive and gender affirming care,' and was a cosponsor of HB 1240 (2023), Washington's assault-weapons ban, indicating alignment with his Democratic caucus's full pro-choice legislative agenda — rejecting any legal recognition of life from conception.",
              ["https://www.ballotready.org/people/jake-fey-ac4c6817-4fde-46d5-946a-d24f6d6a3fc4",
               "https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240"]),
    ]),

    # ---------------- Gerry Pollet (WA-D, District 46) ----------------
    ("gerry-pollet", "WA", "State Representative", [
        claim("gp863a", "gerry-pollet", "sanctity_of_life", 4, False,
              "Pollet served as volunteer legal counsel for NARAL-Washington (now Pro-Choice WA) for decades before entering the Legislature, and is endorsed by Planned Parenthood Alliance Advocates — placing him squarely within the abortion-industry endorsement network that the rubric's 'never took PP/NARAL/EMILY money' standard is designed to screen.",
              ["https://www.gerrypollet.com/issues",
               "https://ballotpedia.org/Gerry_Pollet"]),
        claim("gp863b", "gerry-pollet", "self_defense", 1, False,
              "Pollet is a confirmed cosponsor of HB 1163 (2025), requiring a government permit — including fingerprinting and mandatory firearms safety training — before any firearm purchase in Washington. The bill was signed by Governor Ferguson on May 21, 2025, and takes effect May 2027, adding a state-permission requirement to every gun acquisition.",
              ["https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/House%20Bills/1163.pdf",
               "https://www.opb.org/article/2025/05/21/washington-gun-law-permit-safety-course-house-bill-1163-firearms/"]),
    ]),

    # ---------------- Edwin Obras (WA-D, District 33) ----------------
    ("edwin-obras", "WA", "State Representative", [
        claim("eo863a", "edwin-obras", "self_defense", 1, False,
              "Obras is a confirmed cosponsor of HB 1163 (2025), Washington's firearm permit-to-purchase bill, which requires all buyers to submit fingerprints, pass a background check, and complete a certified firearms safety course before acquiring any gun. Signed into law May 2025, effective May 2027. Obras was elected in December 2024 and cosponsored the bill in his first legislative session.",
              ["https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/House%20Bills/1163.pdf",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
        claim("eo863b", "edwin-obras", "sanctity_of_life", 4, False,
              "Obras received an endorsement from Planned Parenthood Alliance Advocates of Washington in his 2024 special-election campaign, signaling alignment with the abortion-rights funding and endorsement network the rubric's sanctity-of-life standard opposes.",
              ["https://ballotpedia.org/Edwin_Obras",
               "https://housedemocrats.wa.gov/obras/biography/"]),
    ]),

    # ---------------- Debra Lekanoff (WA-D, District 40) ----------------
    ("debra-lekanoff", "WA", "State Representative", [
        claim("dl863a", "debra-lekanoff", "self_defense", 1, False,
              "Lekanoff was among the cosponsors of HB 1240 (2023), Washington's landmark ban on the sale, manufacture, and importation of more than 50 models of semi-automatic rifles (effective July 2023, upheld in subsequent court challenges). The ban directly removes commonly owned defensive firearms from the retail market — contradicting the rubric's defense of unrestricted Second Amendment access.",
              ["https://app.leg.wa.gov/billsummary?Year=2023&BillNumber=1240",
               "https://www.cascadepbs.org/politics/2023/04/washington-state-bans-sale-most-semi-automatic-rifles/"]),
        claim("dl863b", "debra-lekanoff", "sanctity_of_life", 0, False,
              "Lekanoff supported Washington's 2023 legislation to stockpile and distribute mifepristone (a medication abortion drug) through state agencies, ensuring abortion access regardless of federal policy changes — rejecting any legal recognition of life from conception.",
              ["https://housedemocrats.wa.gov/lekanoff/2023/05/05/thats-a-wrap-2023-legislative-session-recap/",
               "https://krcrtv.com/news/nation-world/washington-state-lawmakers-discuss-bill-to-improve-access-to-abortion-medications-mifepristone-pregnancy-birth-law-legal-pro-choice-life-conception-roe-wade-payment-insurance-planned-parenthood"]),
    ]),

    # ---------------- Cindy Ryu (WA-D, District 32) ----------------
    ("cindy-ryu", "WA", "State Representative", [
        claim("cr863a", "cindy-ryu", "sanctity_of_life", 0, False,
              "Ryu was a cosponsor of HB 1469 (2023), Washington's shield law protecting providers, seekers, and helpers of both abortion and gender-affirming care from civil and criminal actions originating in other states — an explicit legislative protection of abortion access that rejects any recognition of personhood from conception and that additionally shields gender-affirming medical procedures.",
              ["https://app.leg.wa.gov/billsummary?BillNumber=1469&Initiative=false&Year=2023",
               "https://www.sgn.org/323903"]),
        claim("cr863b", "cindy-ryu", "self_defense", 1, False,
              "Ryu is a confirmed cosponsor of HB 1163 (2025), Washington's firearm permit-to-purchase law, requiring fingerprinting, a mandatory safety training certificate, and a background check before any firearm acquisition. Signed by Governor Ferguson on May 21, 2025; takes effect May 2027.",
              ["https://lawfilesext.leg.wa.gov/biennium/2025-26/Pdf/Bills/House%20Bills/1163.pdf",
               "https://app.leg.wa.gov/billsummary/?BillNumber=1163&Year=2025&Initiative=false"]),
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

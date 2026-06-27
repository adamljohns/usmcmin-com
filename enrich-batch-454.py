#!/usr/bin/env python3
"""Enrichment batch 454: 4 state-level candidates (1 VA, 3 TX) — evidence_state → evidence_curated.

Bottom-of-alphabet targets (evidence_state confidence, 0 claims, reverse-sorted):
  - Dan Helmer (VA-D, HD-10) — chief patron VA assault-firearms ban enacted 2026; abortion-access champion
  - Shelby Slawson (TX-R, HD-59) — Texas Right to Life champion; 100 pct pro-gun Texas Gun Rights rating
  - Nate Schatzline (TX-R, HD-93) — HB 1375 bookstore obscene-content liability; pro-life position
  - Terri Leo-Wilson (TX-R, HD-23) — three-term SBOE anti-CRT crusader; voted for SB 14 trans-ban for minors
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
    # ---------- Dan Helmer (VA-D, HD-10) ----------
    ("dan-helmer", "VA", "House of Delegates", [
        claim("dh1", "dan-helmer", "self_defense", 1, False,
              "Chief patron of Virginia HB 217 (2026 Regular Session) — the most sweeping assault-firearms ban in Virginia history, signed and enacted May 14, 2026 — which makes it a Class 1 misdemeanor to import, sell, manufacture, purchase, or transfer assault firearms, and bans magazines holding more than 15 rounds. Any person convicted is barred from purchasing, possessing, or transporting a firearm for three years. Helmer shepherded the bill through both chambers of the Democrat-controlled General Assembly; it takes effect July 1, 2026.",
              ["https://lis.virginia.gov/bill-details/20261/HB217",
               "https://ballotpedia.org/Dan_Helmer"]),
        claim("dh2", "dan-helmer", "sanctity_of_life", 0, False,
              "In his 2024 Democratic primary campaign for Virginia's 10th Congressional District, Helmer named 'expanding access to abortion' as a core policy priority alongside gun control. He has also supported the Virginia Legislature's 2025-2026 effort to enshrine a state constitutional right to reproductive freedom including abortion; the proposed amendment cleared both chambers of the General Assembly and will appear on the 2026 Virginia ballot.",
              ["https://ballotpedia.org/Dan_Helmer",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
    ]),

    # ---------- Shelby Slawson (TX-R, HD-59) ----------
    ("shelby-slawson", "TX", "State Representative", [
        claim("ss1", "shelby-slawson", "sanctity_of_life", 0, True,
              "Elected to the Texas House in 2020 with Texas Right to Life PAC backing over a 10-term Republican incumbent who had cast 10 votes in favor of late-term abortion provisions; earned a 93% 'Faith & Family Champion' rating from Texas Values Action for her 2023 voting record — among the highest scores in the full House.",
              ["https://www.texasrighttolifepac.com/pro-life-conservatives-declare-victory-in-republican-runoff-races/",
               "https://txvaluesaction.org/legislator/shelby-slawson/"]),
        claim("ss2", "shelby-slawson", "self_defense", 0, True,
              "Returned a 100% pro-gun candidate survey to Texas Gun Rights ahead of her 2020 general election; Texas Gun Rights identified her predecessor J.D. Sheffield as one of the 'anti-gun Republicans who went down in flames' citing his weak carry-rights record, and credited Slawson's 100% survey as the pro-gun alternative. She has since supported all Texas constitutional carry and firearms-freedom legislation.",
              ["https://txgunrights.org/latest-news/anti-gun-republicans-go-down-in-flames",
               "https://ballotpedia.org/Shelby_Slawson"]),
    ]),

    # ---------- Nate Schatzline (TX-R, HD-93) ----------
    ("nate-schatzline", "TX", "State Representative", [
        claim("ns1", "nate-schatzline", "family_child_sovereignty", 0, True,
              "Chief patron of HB 1375 (89th Texas Legislature, 2025) imposing civil liability on bookstores that sell books with legally obscene content — specifically targeting the growing availability of sexually explicit material in retail outlets frequented by minors. Schatzline stated the bill responds to arguments that parents can simply purchase at bookstores books too explicit for school libraries, aiming to close that loophole for child protection.",
              ["https://ballotpedia.org/Nate_Schatzline",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A4355"]),
        claim("ns2", "nate-schatzline", "sanctity_of_life", 0, True,
              "Publicly supports restrictions on abortion with an exception only when the mother's life is at risk — rejecting elective abortion while protecting the mother's life — consistent with a near-life-at-conception standard and aligned with his support for Texas's Human Life Protection Act and Heartbeat Act. He is joining the National Faith Advisory Board (working with the Trump White House) following his 2026 voluntary retirement from the House.",
              ["https://ballotpedia.org/Nate_Schatzline",
               "https://en.wikipedia.org/wiki/Nate_Schatzline"]),
    ]),

    # ---------- Terri Leo-Wilson (TX-R, HD-23) ----------
    ("terri-leo-wilson", "TX", "State Representative", [
        claim("tlw1", "terri-leo-wilson", "family_child_sovereignty", 0, True,
              "Served three consecutive terms on the Texas State Board of Education (SBOE) where she led systematic reviews of instructional materials to oppose Critical Race Theory and 'liberal indoctrination,' personally spending hundreds of hours scrutinizing textbook content to align curriculum with Texas parents' values. She carried this parental-rights and curriculum-oversight mission into the Texas House, where she serves on the Public Education Committee.",
              ["https://en.wikipedia.org/wiki/Terri_Leo-Wilson",
               "https://ballotpedia.org/Terri_Leo-Wilson"]),
        claim("tlw2", "terri-leo-wilson", "biblical_marriage", 2, True,
              "Voted for Senate Bill 14 (88th Legislature, 2023) — the Texas SAFE Act — prohibiting health care providers from performing puberty-suppression prescriptions, cross-sex hormone therapy, or gender-reassignment surgeries on minors, with penalties including medical-license revocation and withdrawal of Medicaid funding from violating providers. The bill passed the Texas House 85-56 on a party-line vote and was signed into law June 2, 2023.",
              ["https://en.wikipedia.org/wiki/Terri_Leo-Wilson",
               "https://ballotpedia.org/Terri_Leo-Wilson"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 632: hand-curated claims for 2 Oklahoma State Senators.

Senators: Bill Coleman (SD-10), Brenda Stanley (SD-42).
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
    # --- Bill Coleman (OK SD-10, State Senator — Ponca City/Osage-Kay counties) ---
    ("bill-coleman", "OK", "State Senator", [
        claim("bc1", "bill-coleman", "sanctity_of_life", 0, True,
              "Coleman voted YES on SB 918 (2021), Oklahoma's abortion trigger law reactivating the state's pre-Roe criminal abortion statute (21 O.S. §861) upon any SCOTUS ruling restoring state authority over abortion; the Senate passed it 38-9 on March 10, 2021, and Gov. Stitt signed it April 27, 2021.",
              ["https://legiscan.com/OK/bill/SB918/2021",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=sb918&Session=2100"]),
        claim("bc2", "bill-coleman", "election_integrity", 0, True,
              "Coleman voted YES on SJR 48 (2022), a joint resolution to elevate Oklahoma's photo voter-ID requirement from statute into the state constitution, applying it to all authorized voting methods; the Senate passed it 41-7 on March 22, 2022.",
              ["https://legiscan.com/OK/bill/SJR48/2022",
               "http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/SJR48_VOTES.HTM"]),
        claim("bc3", "bill-coleman", "family_child_sovereignty", 0, True,
              "Coleman voted YES on HB 1775 (2021), the Oklahoma Dignity in Education Act prohibiting K-12 public schools from requiring students to affirm race- or sex-based concepts such as inherent privilege or collective guilt; the Senate passed it 38-9.",
              ["https://legiscan.com/OK/bill/HB1775/2021",
               "https://www.oklegislature.gov/BillInfo.aspx?Bill=hb1775&Session=2100"]),
    ]),

    # --- Brenda Stanley (OK SD-42, State Senator — Midwest City/Del City) ---
    ("brenda-stanley", "OK", "State Senator", [
        claim("bs1", "brenda-stanley", "sanctity_of_life", 0, True,
              "Stanley voted YES on HB 4327 (2022), Oklahoma's near-total abortion ban from conception, prohibiting all abortions except to save the mother's life or in reported rape/incest cases, with civil enforcement by private citizens against providers; the Senate passed it 35-10 on April 28, 2022, and Gov. Stitt signed it.",
              ["https://www.oklegislature.gov/BillInfo.aspx?Bill=HB4327&Session=2200",
               "https://oksenate.gov/press-releases/full-senate-approves-legislation-giving-greater-protection-lives-unborn-babies"]),
        claim("bs2", "brenda-stanley", "border_immigration", 0, False,
              "Stanley voted YES on SB 1591 (2022), authored by a Democrat senator, to allow undocumented Oklahoma residents to obtain state driver's licenses by substituting an ITIN for a Social Security number; the bill passed the Senate 30-11 on March 24, 2022 before dying in the House. Eleven Republican senators voted no.",
              ["https://legiscan.com/OK/rollcall/SB1591/id/1156514",
               "https://kfor.com/news/oklahoma-legislature/bill-would-allow-undocumented-workers-to-get-drivers-licenses/"]),
        claim("bs3", "brenda-stanley", "christian_liberty", 0, False,
              "On April 4, 2024, Stanley cast a decisive NO vote in the Senate Health and Human Services Committee to kill HB 3214, the Medical Right-of-Conscience Act, which would have shielded religious healthcare providers from being compelled to perform abortions, gender-transition procedures, or other conscience-violating procedures; the committee deadlocked 6-6, with Stanley in the nay bloc.",
              ["https://www.oklegislature.gov/BillInfo.aspx?Bill=hb3214&Session=2400",
               "https://oklahomavoice.com/2024/04/04/panel-kills-oklahoma-bill-allowing-doctors-to-deny-certain-medical-treatments/"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

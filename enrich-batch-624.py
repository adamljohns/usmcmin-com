#!/usr/bin/env python3
"""Enrichment batch 624: hand-curated claims for 3 Pennsylvania State Senators.

Targets archetype_party_default PA state senators with 0 claims. All are
sitting Republican members of the Pennsylvania Senate with documented
voting records on key rubric issues.

Senators: Michele Brooks (SD-50), Patrick J. Stefano (SD-32), Lisa Baker (SD-20).
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
    # --- Michele Brooks (PA SD-50, State Senator) ---
    ("michele-brooks", "PA", "State Senator", [
        claim("mb1", "michele-brooks", "sanctity_of_life", 0, True,
              "Brooks co-sponsored SB 956 (2021-2022), a joint resolution proposing a Pennsylvania constitutional amendment declaring 'the policy of Pennsylvania is to protect the life of every unborn child from conception to birth' and that nothing in the Constitution grants a right to abortion or public funding thereof; the resolution passed the Senate 28-21.",
              ["https://www.palegis.us/legislation/bills/2021/sb0956",
               "https://www.legis.state.pa.us/cfdocs/billinfo/bill_history.cfm?syear=2021&sind=0&body=S&type=B&bn=956"]),
        claim("mb2", "michele-brooks", "self_defense", 0, True,
              "Brooks co-sponsored SB 565 (2021-2022), the Constitutional Carry Act eliminating Pennsylvania's permit requirement for concealed carry; the bill passed the Senate 29-21 and the House 107-92 before being vetoed by Governor Wolf in December 2021.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565"]),
        claim("mb3", "michele-brooks", "election_integrity", 0, True,
              "Brooks co-sponsored SB 422 (2021-2022), which amended the Pennsylvania Election Code to require photo voter identification at the polls for in-person voting.",
              ["https://www.palegis.us/legislation/bills/2021/sb422",
               "https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=422"]),
    ]),

    # --- Patrick J. Stefano (PA SD-32, State Senator) ---
    ("patrick-j-stefano", "PA", "State Senator", [
        claim("pjs1", "patrick-j-stefano", "sanctity_of_life", 0, True,
              "Stefano co-introduced SB 956 (2021-2022), a joint resolution proposing a constitutional amendment declaring Pennsylvania's policy is 'to protect the life of every unborn child from conception to birth' and that no right to abortion or public funding exists in the Pennsylvania Constitution.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?bn=956&body=S&sInd=0&sYear=2021&type=B",
               "https://ballotpedia.org/Patrick_Stefano"]),
        claim("pjs2", "patrick-j-stefano", "election_integrity", 0, True,
              "Stefano co-sponsored SB 735 (2021-2022), a proposed constitutional amendment requiring every Pennsylvania voter to present valid identification at the polls for every election; the amendment passed the Senate with bipartisan support.",
              ["https://www.palegis.us/legislation/bills/2021/sb735",
               "https://ballotpedia.org/Voter_ID_in_Pennsylvania"]),
        claim("pjs3", "patrick-j-stefano", "self_defense", 3, True,
              "Stefano has introduced Castle Doctrine expansion legislation across multiple sessions, most recently SB 1269 (2025-2026) extending self-defense protections to the property line; the bill passed the Pennsylvania Senate 49-0.",
              ["https://www.palegis.us/legislation/bills/2025/sb1269",
               "https://www.palegis.us/senate/co-sponsorship/memo?memoID=44090"]),
    ]),

    # --- Lisa Baker (PA SD-20, State Senator) ---
    ("lisa-baker", "PA", "State Senator", [
        claim("lb1", "lisa-baker", "self_defense", 0, True,
              "As Senate Judiciary Committee Chair, Baker advanced SB 565 (constitutional carry) out of committee in 2021 — the bill passed the full Senate 29-21 — and again advanced SB 357 (a renewed permitless carry bill) in 2026, demonstrating a consistent commitment to Second Amendment rights.",
              ["https://www.pasenategop.com/news/baker-judiciary-committee-advances-constitutional-carry-as-senate-sends-preemption-expansion-to-the-house/",
               "https://www.senatorbaker.com/2026/05/06/baker-judiciary-committee-advances-constitutional-carry-as-senate-sends-preemption-expansion-to-the-house/"]),
        claim("lb2", "lisa-baker", "election_integrity", 2, True,
              "Baker sponsored SB 1200 (2022) to ban ballot drop boxes in Pennsylvania and separately sponsored SB 982 to prohibit private funding (such as Zuckerberg-style grants) from being used in Pennsylvania election operations.",
              ["https://ballotpedia.org/Lisa_Baker_(Pennsylvania)",
               "https://www.legis.state.pa.us/cfdocs/legis/home/member_information/senate_bio.cfm?id=1077"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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

    # Minified write -- preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

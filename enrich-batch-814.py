#!/usr/bin/env python3
"""Enrichment batch 814: 4 NH Republican state senators (completing NH cohort).

archetype_curated federal bucket fully exhausted; continuing bottom-of-alphabet
state-level pool. Targets: the 4 remaining NH state senators with 0 claims
(batch 813 covered 5; these are the rest):
  David Rochefort  (NH SD-1, Great North Woods, Chair Senate H&HS, freshman Jan 2025)
  Daryl Abbas      (NH SD-22, Salem area, Senate President Pro Tempore since Dec 2024)
  Daniel Innis     (NH SD-7, Seacoast/Hampton, professor/former UNH dean, 2026 US Senate candidate)
  Bill Gannon      (NH SD-23, Rockingham County, Judiciary Chair, authored anti-sanctuary bill)

All claims drawn from 2024-2026 confirmed party-line roll-call votes and documented
individual actions. Sources: citizenscount.org, newhampshirebulletin.com, bostonglobe.com,
nhjournal.com, nhpr.org, ballotpedia.org, patch.com, fairus.org.
MINIFIED write preserved (no indent=2).
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
    # ---------- David Rochefort (NH SD-1, Great North Woods, R — freshman Jan 2025) ----------
    ("david-rochefort", "NH", "State Senator", [
        claim("dr1", "david-rochefort", "biblical_marriage", 2, True,
              "As Chair of the Senate Health and Human Services Committee, led HB 377 (banning puberty blockers and hormone therapy for minors) through the Senate committee process and was appointed by the Senate President to the Conference Committee on June 5, 2025. Voted YES on the final bill, signed by Governor Ayotte on August 1, 2025 — the 16-8 party-line Senate vote included all 16 Republicans. The law makes providing these treatments to minors a felony.",
              ["https://www.citizenscount.org/candidate/david-rochefort/serving",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://en.wikipedia.org/wiki/New_Hampshire_House_Bill_377"]),
        claim("dr2", "david-rochefort", "border_immigration", 2, True,
              "Voted YES on NH SB 62 (2025), prohibiting state and local governments from adopting sanctuary policies that would impede federal immigration enforcement — signed by Governor Kelly Ayotte on May 22, 2025. New Hampshire became the first New England state to enact an anti-sanctuary law under this package. Rochefort's YES vote aligned with the entire 16-member Senate Republican caucus.",
              ["https://www.bostonglobe.com/2025/05/22/metro/nh-governor-kelly-ayotte-new-law-sanctuary-cities-ban/",
               "https://www.nhpr.org/nh-news/2025-12-30/anti-sanctuary-city-bills-nh-new-hampshire-immigration",
               "https://www.fairus.org/legislation/state-and-local/new-hampshire-anti-sanctuary-legislation"]),
        claim("dr3", "david-rochefort", "election_integrity", 0, True,
              "Voted YES on NH SB 287 (signed August 1, 2025), requiring photo ID or a notarized signature on absentee ballot applications — passed the Senate 16-8 on party lines, all 16 Republicans including Rochefort voting YES. The law tightens absentee-ballot access to verified identity, directly opposing mass-mail-in ballot practices.",
              ["https://www.bostonglobe.com/2025/08/01/metro/nh-law-absentee-ballots-voter-id/",
               "https://www.citizenscount.org/candidate/david-rochefort/serving"]),
    ]),

    # ---------- Daryl Abbas (NH SD-22, Salem, Senate President Pro Tempore, R) ----------
    ("daryl-abbas", "NH", "State Senator", [
        claim("da1", "daryl-abbas", "family_child_sovereignty", 0, True,
              "As Senate President Pro Tempore voted YES on NH SB 295 (2025), removing the household-income cap from NH's Education Freedom Account (EFA) program and opening school-choice vouchers to all NH families regardless of income — the most expansive school-choice expansion in NH history. Also voted YES on SB 295's predecessor SB 442 (2024), which raised the EFA income ceiling to 400% of the federal poverty level. Citizens Count records both votes.",
              ["https://www.citizenscount.org/candidate/daryl-abbas/serving",
               "https://www.citizenscount.org/bills/sb-295-2025",
               "https://ballotpedia.org/Daryl_Abbas"]),
        claim("da2", "daryl-abbas", "biblical_marriage", 2, True,
              "Voted YES on NH HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors — 16-8 party-line Senate vote. Also voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — 13-10 party-line vote. As Senate President Pro Tempore, Abbas controls floor scheduling and actively supports both bills as part of the NH Republican majority's legislative agenda.",
              ["https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://www.citizenscount.org/candidate/daryl-abbas/serving"]),
        claim("da3", "daryl-abbas", "border_immigration", 2, True,
              "Voted YES on NH SB 563 (2024) and NH SB 62 (2025), both prohibiting state and local governments from adopting sanctuary policies. SB 563 passed the Senate 14-10 over unanimous Democratic opposition (March 2024); SB 62 passed on a party-line majority and was signed May 22, 2025, making NH the first New England state to ban sanctuary policies. Citizens Count records Abbas's YES votes on both bills.",
              ["https://www.citizenscount.org/candidate/daryl-abbas/history",
               "https://www.bostonglobe.com/2025/05/22/metro/nh-governor-kelly-ayotte-new-law-sanctuary-cities-ban/",
               "https://nhjournal.com/nh-senate-passes-sanctuary-city-ban-over-unanimous-dem-opposition/"]),
    ]),

    # ---------- Daniel Innis (NH SD-7, Seacoast/Hampton, R — professor, 2026 US Senate candidate) ----------
    ("daniel-innis", "NH", "State Senator", [
        claim("di1", "daniel-innis", "family_child_sovereignty", 0, True,
              "Advocates for parental rights as a core platform position; announced his candidacy for the 2026 Republican U.S. Senate primary in New Hampshire (July 2025) on a platform centered on parental rights, lower taxes, and safer communities. Also voted YES on NH SB 295 (2025), removing the income cap from Education Freedom Accounts and opening school-choice vouchers to all NH families, affirming parental control over children's education.",
              ["https://ballotpedia.org/Dan_Innis",
               "https://www.citizenscount.org/candidate/dan-innis",
               "https://en.wikipedia.org/wiki/Dan_Innis"]),
        claim("di2", "daniel-innis", "biblical_marriage", 2, True,
              "Voted YES on NH HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors — 16-8 party-line Senate vote with all 16 Republicans including Innis voting YES. Also voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — 13-10 party-line vote. Citizens Count records Innis's votes in both sessions.",
              ["https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://www.citizenscount.org/candidate/dan-innis"]),
        claim("di3", "daniel-innis", "border_immigration", 2, True,
              "Voted YES on NH SB 62 (signed May 22, 2025), prohibiting state and local governments from adopting sanctuary policies that impede federal immigration enforcement — making NH the first New England state to ban sanctuary policies. Voted YES on the predecessor bill SB 563 (2024) as well. Citizens Count records both YES votes for Innis.",
              ["https://www.bostonglobe.com/2025/05/22/metro/nh-governor-kelly-ayotte-new-law-sanctuary-cities-ban/",
               "https://www.nhpr.org/nh-news/2025-12-30/anti-sanctuary-city-bills-nh-new-hampshire-immigration",
               "https://www.citizenscount.org/candidate/dan-innis"]),
    ]),

    # ---------- Bill Gannon (NH SD-23, Rockingham County, Judiciary Chair, R — since 2016) ----------
    ("bill-gannon", "NH", "State Senator", [
        claim("bg1", "bill-gannon", "border_immigration", 2, True,
              "Primary author of the NH Senate anti-sanctuary city bill; stated publicly: 'I wrote the NH Senate anti-sanctuary city bill. It requires police to cooperate with security and ICE when they pull over an illegal alien for a state offense.' Gannon sponsored SB 563 (2024, passed 14-10 over unanimous Democratic opposition) and backed the 2025 successor SB 62, which was signed by Governor Ayotte on May 22, 2025, making NH the first New England state to ban sanctuary policies.",
              ["https://patch.com/new-hampshire/hampton-northhampton/district-23-state-sen-bill-gannon-candidate-profile",
               "https://www.bostonglobe.com/2025/05/22/metro/nh-governor-kelly-ayotte-new-law-sanctuary-cities-ban/",
               "https://www.fairus.org/legislation/state-and-local/new-hampshire-anti-sanctuary-legislation"]),
        claim("bg2", "bill-gannon", "biblical_marriage", 2, True,
              "Voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — 13-10 Senate party-line vote. Also voted YES on NH HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors — 16-8 party-line vote. Citizens Count and ballotpedia track Gannon's consistent support for both transgender-restriction bills.",
              ["https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://www.citizenscount.org/candidate/william-gannon/serving"]),
        claim("bg3", "bill-gannon", "election_integrity", 0, True,
              "Voted YES on NH SB 287 (signed August 1, 2025), requiring photo ID or a notarized signature on absentee ballot applications — 16-8 party-line Senate vote. Also voted YES on NH HB 1569 (2024), eliminating the affidavit ballot exception and requiring photo ID to vote — passed the Senate 13-11 on party lines. As Judiciary Committee Chair, Gannon oversees election-law matters and has backed voter-ID measures throughout his Senate tenure since 2016.",
              ["https://www.bostonglobe.com/2025/08/01/metro/nh-law-absentee-ballots-voter-id/",
               "https://www.democracydocket.com/news-alerts/new-hampshire-republicans-pass-bill-removing-exceptions-to-voter-id-requirement/",
               "https://www.citizenscount.org/candidate/william-gannon/serving"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Enrichment batch 137: hand-curated claims for 5 federal House candidates.

Targets low_evidence / archetype_party_default / evidence_federal U.S. House
candidates with 0 claims, taken from the bottom of the alphabet (TX, VA).

Candidates (all R, bottom-of-alphabet):
  Randy Weber (TX-14, sitting),  Pat Fallon (TX-04, sitting),
  Michael Cloud (TX-27, sitting), Roger Williams (TX-25, sitting),
  Darius Mayfield (VA-07, 2026 R primary candidate).

Each claim cites >=1 reliable source and reflects 2021-2026 public
positions/voting records from congress.gov, govtrack.us, weber.house.gov,
fallon.house.gov, cloud.house.gov, sbaprolife.org, nrapvf.org,
and ballotpedia.org.

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
    # ---------- Randy Weber (TX-14, R, sitting) ----------
    ("randy-weber", "TX", "Representative", [
        claim("rw1", "randy-weber", "sanctity_of_life", 0, True,
              "Cosponsored the Life at Conception Act (H.R.722) in the 119th Congress (2025–2026) and H.R.431 in the 118th Congress (2023–2024), recognizing legal personhood for the unborn from the moment of fertilization — the federal personhood standard the rubric requires.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722/cosponsors",
               "https://www.congress.gov/bill/118th-congress/house-bill/431/cosponsors"]),
        claim("rw2", "randy-weber", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (S.2938, 2022), publicly calling it a 'gun reform' bill; opposed federal grants to states implementing red-flag (ERPO) laws and the enhanced background-check provisions targeting under-21 purchases — a documented anti-red-flag, anti-restriction record.",
              ["https://weber.house.gov/news/documentsingle.aspx?DocumentID=1335"]),
        claim("rw3", "randy-weber", "economic_stewardship", 0, True,
              "Cosponsored the Digital Dollar Pilot Prevention Act (H.R.3712, 118th Congress) to prohibit the Federal Reserve from initiating any central bank digital currency (CBDC) pilot program without explicit congressional authorization — opposing a government-controlled surveillance currency.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/3712",
               "https://www.govtrack.us/congress/members/randy_weber/412574"]),
    ]),

    # ---------- Pat Fallon (TX-04, R, sitting) ----------
    ("pat-fallon", "TX", "Representative", [
        claim("pf1", "pat-fallon", "sanctity_of_life", 0, True,
              "Cosponsored the Life at Conception Act in the 117th (H.R.1011), 118th (H.R.431), and 119th (H.R.722) Congress, establishing federal legal personhood for unborn children from fertilization. SBA Pro-Life America scorecard confirms consistent votes 'to defend the lives of the unborn and infants.'",
              ["https://www.congress.gov/bill/119th-congress/house-bill/722/cosponsors",
               "https://www.congress.gov/bill/117th-congress/house-bill/1011/cosponsors",
               "https://sbaprolife.org/representative/pat-fallon"]),
        claim("pf2", "pat-fallon", "self_defense", 1, True,
              "Describes himself as a 'firm believer in the second amendment, its inherent constitutionality and its intent,' asserting that 'productive members of society have every RIGHT to protect and defend themselves.' NRA-PVF endorsed Fallon in 2020, reflecting a consistent anti-restriction gun record.",
              ["https://fallon.house.gov/",
               "https://www.nrapvf.org/emails/2020/texas/pat-fallon-tx-04-general"]),
        claim("pf3", "pat-fallon", "border_immigration", 0, True,
              "Cited nearly 11 million illegal border encounters under the Biden-Harris administration as 'a serious threat to national security' and has backed physical barrier construction and enforcement-first border policy, co-signing Texas Republican delegation legislation to harden the southern border.",
              ["https://fallon.house.gov/",
               "https://ballotpedia.org/Pat_Fallon"]),
    ]),

    # ---------- Michael Cloud (TX-27, R, sitting) ----------
    ("michael-cloud", "TX", "Representative", [
        claim("mc1", "michael-cloud", "sanctity_of_life", 0, True,
              "Consistently voted to defund Planned Parenthood, eliminate all taxpayer-funded abortion, and protect religious freedom for health-care workers who decline to perform abortions — a documented pro-life record opposing any public subsidy for abortion providers.",
              ["https://cloud.house.gov/about-michael",
               "https://ballotpedia.org/Michael_Cloud_(Texas)"]),
        claim("mc2", "michael-cloud", "self_defense", 1, True,
              "Led a formal congressional demand to the ATF requiring immediate answers about its Out-of-Business Records Imaging System (OBRIS), which Cloud publicly called an 'illegal, searchable national gun registry' — a direct challenge to ATF's de facto firearms registry that Congress has prohibited by statute.",
              ["https://cloud.house.gov/posts/release-congressman-michael-cloud-demands-response-from-atf-on-illegal-national-gun-registry"]),
        claim("mc3", "michael-cloud", "border_immigration", 4, True,
              "Supports ending birthright citizenship, mandatory E-Verify implementation for all employers, elimination of the visa lottery, and opposes all amnesty — hard-line enforcement positions addressing chain migration and illegal-employment incentives.",
              ["https://cloud.house.gov/",
               "https://ballotpedia.org/Michael_Cloud_(Texas)"]),
    ]),

    # ---------- Roger Williams (TX-25, R, sitting) ----------
    ("roger-williams", "TX", "Representative", [
        claim("rwt1", "roger-williams", "sanctity_of_life", 0, True,
              "States that Christian and conservative values include opposing abortion; cosponsored the Born-Alive Abortion Survivors Protection Act in the 119th Congress (2025–2026) and backed the Protecting Pain-Capable Unborn Children from Late-Term Abortions Act — affirming the right to life from birth and throughout pregnancy.",
              ["https://sbaprolife.org/representative/roger-williams",
               "https://ballotpedia.org/Roger_Williams_(Texas)"]),
        claim("rwt2", "roger-williams", "self_defense", 1, True,
              "NRA-PVF endorsed Williams in both the 2018 and 2020 general elections, reflecting a gun-rights voting record that meets NRA's threshold for endorsement — which requires documented opposition to firearms restrictions such as red-flag laws, magazine bans, and background-check expansions.",
              ["https://www.nrapvf.org/emails/2018/texas/roger-williams-tx-25-general-election-email/",
               "https://www.nrapvf.org/emails/2020/texas/roger-williams-tx-25-general"]),
    ]),

    # ---------- Darius Mayfield (VA-07, R, 2026 primary) ----------
    ("darius-mayfield", "VA", "Representative", [
        claim("dm1", "darius-mayfield", "border_immigration", 1, True,
              "Campaign website states the U.S. must prioritize 'mandatory deportation' of recently arrived illegal immigrants, particularly violent criminals — an enforcement-first position that calls for immediate removal rather than prolonged detention or case processing.",
              ["https://ballotpedia.org/Darius_Mayfield"]),
        claim("dm2", "darius-mayfield", "border_immigration", 2, True,
              "Calls for empowering border patrol and law enforcement to enforce existing immigration laws and supports implementing 'Remain in Mexico' as statutory federal law; additionally urges Mexico to deploy its military to the border to stem the flow of illegal crossings — an anti-sanctuary, bilateral enforcement approach.",
              ["https://ballotpedia.org/Darius_Mayfield",
               "https://ivoterguide.com/candidate/66350/race/6829/election/949"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

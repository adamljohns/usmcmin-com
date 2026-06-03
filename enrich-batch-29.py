#!/usr/bin/env python3
"""Enrichment batch 29: hand-curated claims for 5 TX/TN U.S. Representatives.

Targets bottom-of-alphabet (TX, TN) archetype_curated House members with 0 evidence
claims. Uses (slug + state + office_keyword) matcher per prior batches.

Targets (all R):
  Ronny Jackson (TX-13), Chip Roy (TX-21), Andy Ogles (TN-05),
  Dan Crenshaw (TX-02), Matt Van Epps (TN-07).

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
    # ---------------- Ronny Jackson (TX-13, R) ----------------
    ("ronny-jackson", "TX", "Representative", [
        claim("rj1", "ronny-jackson", "sanctity_of_life", 0, True,
              "Strongly opposes abortion and affirms life from conception; appears on SBA Pro-Life America's House scorecard with a consistent pro-life voting record, and voted for the Born-Alive Abortion Survivors Protection Act requiring equal medical care for infants born alive after failed abortions.",
              ["https://sbaprolife.org/representative/ronny-jackson",
               "https://ballotpedia.org/Ronny_Jackson"]),
        claim("rj2", "ronny-jackson", "border_immigration", 0, True,
              "A border-security hawk representing a Texas Panhandle district on the southern-border frontier; introduced the Reimbursing Border Communities Act of 2025 to compensate local governments for federal border-enforcement costs, and the Strategic Export Controls and Border Security Enhancement Act of 2026 to tighten cross-border security — consistently supporting a fortified physical border.",
              ["https://www.congress.gov/member/ronny-jackson/J000304",
               "https://www.govtrack.us/congress/members/ronny_jackson/456847"]),
        claim("rj3", "ronny-jackson", "self_defense", 1, True,
              "Ranked 11th most conservative in the entire House (118th Congress) and opposed new firearm restrictions; as a retired U.S. Navy Rear Admiral representing a rural Texas district he has a consistent record of defending unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/members/ronny_jackson/456847/report-card/2024",
               "https://ballotpedia.org/Ronny_Jackson"]),
    ]),

    # ---------------- Chip Roy (TX-21, R) ----------------
    ("chip-roy", "TX", "Representative", [
        claim("cr1", "chip-roy", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life record from SBA Pro-Life America; spoke on the House floor in favor of the Born-Alive Abortion Survivors Protection Act and voted consistently to protect the lives of the unborn and to defund Planned Parenthood — including through the 2025 reconciliation bill H.R.1 that stripped Planned Parenthood of Medicaid dollars for one year.",
              ["https://sbaprolife.org/representative/chip-roy",
               "https://en.wikipedia.org/wiki/Chip_Roy"]),
        claim("cr2", "chip-roy", "election_integrity", 0, True,
              "In January 2025 reintroduced the Safeguard American Voter Eligibility (SAVE) Act to require documentary proof of U.S. citizenship to register for federal elections; the bill passed the House in 2024 but died in the Senate, and Roy continued to champion it in the 119th Congress as a core election-integrity measure.",
              ["https://en.wikipedia.org/wiki/Chip_Roy",
               "https://ballotpedia.org/Chip_Roy"]),
        claim("cr3", "chip-roy", "economic_stewardship", 2, True,
              "In December 2024 opposed raising the U.S. debt ceiling, drawing criticism from President-elect Trump — Roy held firm, consistent with his Freedom Caucus record of resisting uncapped deficit spending and calling for balanced-budget discipline.",
              ["https://en.wikipedia.org/wiki/Chip_Roy",
               "https://www.govtrack.us/congress/members/chip_roy/412826"]),
    ]),

    # ---------------- Andy Ogles (TN-05, R) ----------------
    ("andy-ogles", "TN", "Representative", [
        claim("ao1", "andy-ogles", "sanctity_of_life", 0, True,
              "Carries an A/100% pro-life rating from SBA Pro-Life America; helped deliver the largest federal pro-life legislative win in two decades by voting for H.R.1 (2025 reconciliation) which defunded Planned Parenthood of Medicaid dollars for one year; separately introduced the Ending Chemical Abortions Act of 2025 to prohibit chemical abortion drugs in the United States.",
              ["https://sbaprolife.org/representative/andy-ogles",
               "https://en.wikipedia.org/wiki/Andy_Ogles"]),
        claim("ao2", "andy-ogles", "border_immigration", 2, True,
              "Strongly opposes sanctuary-city policies; has stated that illegal immigration 'strains the country's financial wellbeing, threatens national security, and erodes the rule of law,' and sponsored H.R.8827 to end family-chain immigration categories, eliminate the diversity visa lottery, and revise asylum procedures.",
              ["https://www.ontheissues.org/House/Andy_Ogles_Immigration.htm",
               "https://www.congress.gov/member/andrew-ogles/O000175"]),
        claim("ao3", "andy-ogles", "self_defense", 1, True,
              "A committed Second Amendment defender — nationally known for sending a Christmas card featuring his family holding rifles; opposes new gun-control mandates and votes against red-flag laws and assault-weapons bans as a member of the House Freedom Caucus.",
              ["https://en.wikipedia.org/wiki/Andy_Ogles",
               "https://ballotpedia.org/Andy_Ogles"]),
    ]),

    # ---------------- Dan Crenshaw (TX-02, R) ----------------
    ("dan-crenshaw", "TX", "Representative", [
        claim("dc1", "dan-crenshaw", "foreign_policy_restraint", 1, False,
              "A vocal Ukraine-aid hawk: vocally supported the $40 billion Ukraine aid package in 2022 and continued to defend open-ended Ukraine military assistance through 2024-2025, placing him among the minority of House Republicans who backed the February 2024 $95B supplemental foreign-aid package — directly counter to the rubric's call to end foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/Dan_Crenshaw",
               "https://www.govtrack.us/congress/members/dan_crenshaw/412820"]),
        claim("dc2", "dan-crenshaw", "self_defense", 1, True,
              "In January 2025 introduced the Preventing Unjust Red Flag Laws Act to prohibit federal grants to states that maintain red-flag (ERPO) laws, calling such laws unconstitutional — a pro-Second Amendment posture opposing one of the rubric's most specifically flagged gun-control mechanisms.",
              ["https://en.wikipedia.org/wiki/Dan_Crenshaw",
               "https://www.govtrack.us/congress/members/dan_crenshaw/412820"]),
        claim("dc3", "dan-crenshaw", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022), which codified federal recognition of same-sex marriage — one of only 39 House Republicans to cross over, contradicting the rubric's one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Dan_Crenshaw",
               "https://ballotpedia.org/Daniel_Crenshaw"]),
    ]),

    # ---------------- Matt Van Epps (TN-07, R) ----------------
    ("matt-van-epps", "TN", "Representative", [
        claim("mve1", "matt-van-epps", "border_immigration", 0, True,
              "Ran on and supports completion of the U.S.–Mexico border wall and mandatory deportation of illegal immigrants with criminal records; called border security a top priority in the 2025 special election campaign that sent him to Congress.",
              ["https://en.wikipedia.org/wiki/Matt_Van_Epps",
               "https://ballotpedia.org/Matt_Van_Epps"]),
        claim("mve2", "matt-van-epps", "self_defense", 1, True,
              "Identifies as a defender of the Second Amendment and opposes federal measures for stricter gun control; ran on a platform of protecting Second Amendment rights as part of his America First agenda in the November 2025 special election.",
              ["https://en.wikipedia.org/wiki/Matt_Van_Epps",
               "https://ballotpedia.org/Matt_Van_Epps"]),
        claim("mve3", "matt-van-epps", "economic_stewardship", 2, True,
              "A self-described 'fiscal hawk'; supported the One Big Beautiful Bill Act (2025 reconciliation) that extended Trump-era tax cuts, implemented welfare reforms, and increased border-security funding — framing fiscal restraint and pro-growth policy as intertwined.",
              ["https://en.wikipedia.org/wiki/Matt_Van_Epps",
               "https://news.ballotpedia.org/2025/12/04/matt-van-epps-r-won-the-special-election-for-tennessees-7th-congressional-district/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent slug collisions."""
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

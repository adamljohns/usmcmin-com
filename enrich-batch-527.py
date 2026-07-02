#!/usr/bin/env python3
"""Enrichment batch 527: 8 claims across 4 candidates (OH/OK/TX).

archetype_curated + 0-claim buckets fully exhausted. Targets sitting federal
members with 3 existing claims, adding 2 distinct-category claims each to
fill uncovered rubric dimensions.

Targets (bottom-of-alphabet states OH/OK/TX):
  Warren Davidson  (OH-08 R, sitting US Rep)  — self_defense, economic_stewardship
  Stephanie Bice   (OK-05 R, sitting US Rep)  — election_integrity, economic_stewardship
  Greg Casar       (TX-35 D, sitting US Rep)  — election_integrity, economic_stewardship
  Frank Lucas      (OK-03 R, sitting US Rep)  — election_integrity, economic_stewardship

Sources: davidson.house.gov, congress.gov, govtrack.us, bice.house.gov,
         casar.house.gov, lucas.house.gov, en.wikipedia.org, votesmart.org.

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
    # -------- Warren Davidson (OH-08 R, sitting US Representative) --------
    ("warren-davidson", "OH", "Representative", [
        claim("wd4", "warren-davidson", "self_defense", 1, True,
              "Davidson voted Nay on H.R. 8 ('Bipartisan Background Checks Act of 2021,' March 11, 2021) and H.R. 1446 ('Enhanced Background Checks Act,' March 11, 2021), which would have closed the private-sale background-check exemption and extended Brady Act waiting periods. In a press release titled 'Davidson Opposes Democrat Gun Grabs,' he called the bills 'an unconstitutional two-for-one attack on Americans' Second and Fourth Amendment rights' and stated they 'make criminals out of law-abiding Americans and force all gun owners to go through government-licensed agents just to borrow a hunting rifle.' He holds a 92% NRA Political Victory Fund rating and explicitly opposes red flag laws, magazine bans, and expanded restrictions on lawful transfers, limiting restrictions only to prior-convicted felons and those adjudicated mentally dangerous.",
              ["https://davidson.house.gov/2021/3/davidson-opposes-democrat-gun-grabs",
               "https://justfacts.votesmart.org/candidate/evaluations/166760/warren-davidson",
               "https://en.wikipedia.org/wiki/Warren_Davidson"]),
        claim("wd5", "warren-davidson", "economic_stewardship", 0, True,
              "Davidson was the lead House sponsor of the CBDC Anti-Surveillance State Act (H.R. 5403, 118th Congress), which passed the House 216-192 on May 23, 2024. The bill prohibits the Federal Reserve from issuing a central bank digital currency (CBDC) directly to individuals or maintaining CBDC accounts. Davidson issued a statement after passage calling CBDCs 'an existential threat to western civilization' and 'a dystopian surveillance tool corrupting money into a tool for coercion and control.' He also separately condemned state-level CBDC initiatives as a 'back door' attempt to legalize government-controlled digital currency, and in 2025 raised concerns that a related Senate bill's statutory CBDC prohibition would expire in 2030, effectively giving the next administration a 'go-live date' for a federal digital dollar.",
              ["https://davidson.house.gov/press-releases?id=06C1B210-DE60-498F-9FE8-217B6012B1A6",
               "https://davidson.house.gov/2023/3/rep-davidson-condemns-state-efforts-to-legalize-cbdcs",
               "https://www.congress.gov/bill/118th-congress/house-bill/5403"]),
    ]),

    # -------- Stephanie Bice (OK-05 R, sitting US Representative) --------
    ("stephanie-bice", "OK", "Representative", [
        claim("sb4", "stephanie-bice", "election_integrity", 0, True,
              "Bice co-sponsored H.R. 22 (the Safeguard American Voter Eligibility Act — SAVE Act, 119th Congress) and voted Yea on its final passage April 10, 2025 (220-208, every House Republican in favor). The SAVE Act requires documentary proof of U.S. citizenship — such as a passport or birth certificate — to register to vote in federal elections and provides states tools to remove non-citizens from voter rolls. Bice issued a press release stating: 'Securing our elections is of paramount importance, which is why I was proud to vote in favor of the SAVE Act. This bill ensures that we protect the votes of American citizens; making it easy to vote and hard to cheat. We must strengthen our election security, improve voter confidence, and ensure American citizens are the only ones voting.'",
              ["https://bice.house.gov/media/press-releases/bice-votes-pass-election-integrity-bill",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("sb5", "stephanie-bice", "economic_stewardship", 2, True,
              "Bice has maintained a consistent anti-deficit voting record across multiple Congresses. She voted Yea on H.R. 2811 (the Limit, Save, Grow Act of 2023, passed the House April 26, 2023, 217-215), which would have capped discretionary spending at FY2022 levels and reduced projected deficits by approximately $4.8 trillion over 10 years. She has previously voted against raising the debt ceiling, including releasing statements titled 'Bice Votes Against Raising Debt Ceiling A Third Time' and 'Bice Again Votes No on Raising the Debt Ceiling,' and her official issues page identifies reining in 'Washington's irresponsible spending' as a top fiscal priority.",
              ["https://bice.house.gov/media/press-releases/bice-votes-against-raising-debt-ceiling-third-time",
               "https://bice.house.gov/issues/budget-and-spending",
               "https://www.congress.gov/bill/118th-congress/house-bill/2811"]),
    ]),

    # -------- Greg Casar (TX-35 D, sitting US Representative) --------
    ("greg-casar", "TX", "Representative", [
        claim("gc4", "greg-casar", "election_integrity", 0, False,
              "On April 10, 2025, Casar voted Nay on H.R. 22 (the SAVE Act), which passed 220-208 with all Republicans and only four Democrats in favor; the remaining 208 Democrats — including Casar — voted against it. The SAVE Act would require documentary proof of U.S. citizenship to register to vote in federal elections. As chair of the Congressional Progressive Caucus and a champion of 'civil rights and voting rights for all people,' Casar opposes proof-of-citizenship voter-registration requirements, which his caucus characterizes as voter suppression — a position directly contrary to the rubric's voter-ID and election-integrity standard.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://casar.house.gov/"]),
        claim("gc5", "greg-casar", "economic_stewardship", 2, False,
              "Casar voted Nay on H.R. 2811 (the Limit, Save, Grow Act of 2023), which the House passed April 26, 2023, 217-215 with zero Democratic votes — all 213 Democrats, including Casar, voted against it. The bill would have capped discretionary spending at FY2022 levels and reduced projected deficits by approximately $4.8 trillion over 10 years. As chair of the Congressional Progressive Caucus and a longtime labor organizer who fights for 'an economy that works for working families,' Casar consistently supports higher federal expenditure programs and opposes deficit-reduction legislation that involves spending cuts — directly contrary to the rubric's anti-deficit and balanced-budget fiscal standard.",
              ["https://www.govtrack.us/congress/votes/118-2023/h199",
               "https://www.congress.gov/bill/118th-congress/house-bill/2811/summary/00",
               "https://en.wikipedia.org/wiki/Greg_Casar"]),
    ]),

    # -------- Frank Lucas (OK-03 R, sitting US Representative) --------
    ("frank-lucas", "OK", "Representative", [
        claim("fl4", "frank-lucas", "election_integrity", 0, True,
              "Lucas voted Yea on H.R. 22 (the SAVE Act, 119th Congress, passed April 10, 2025, 220-208) requiring documentary proof of U.S. citizenship to register to vote in federal elections. Lucas has also consistently opposed federal election-administration takeovers: his official website carries a post titled 'Lucas Opposes Democrats' Federal Election Takeover,' referring to H.R. 1 (the For the People Act of 2021), which would have nationalized election rules, overridden state voter-ID laws, and mandated automatic voter registration and mass mail-in balloting — each provision directly contrary to the rubric's voter-ID, paper-ballot, and anti-mass-mail-in election-integrity standards.",
              ["https://lucas.house.gov/posts/lucas-opposes-democrats-federal-election-takeover",
               "https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("fl5", "frank-lucas", "economic_stewardship", 2, True,
              "Lucas voted for and praised passage of H.R. 2811 (the Limit, Save, Grow Act of 2023, passed April 26, 2023, 217-215), stating its top priorities were 'to limit Washington's irresponsible spending, save taxpayers money, and grow the American economy' and criticizing the 'highest level of deficit spending in the history of our country' under the prior Congress. His official website also carries a post titled 'Lucas Votes Against Massive Spending Bill Disguised as Stimulus Package,' reflecting a consistent record of opposing large unfunded spending — directly aligning with the rubric's anti-deficit and balanced-budget fiscal standard.",
              ["https://lucas.house.gov/posts/lucas-statement-on-house-gop-plan-addressing-debt-ceiling-applauds-passage-of-limit-save-grow-act",
               "https://lucas.house.gov/posts/lucas-votes-against-massive-spending-bill-disguised-as-stimulus-package",
               "https://www.congress.gov/bill/118th-congress/house-bill/2811"]),
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

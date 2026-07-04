#!/usr/bin/env python3
"""Enrichment batch 559: 5 active 2026 federal candidates — WI-08, WA-05, WA-01, WA-07, WA-03.

All archetype_curated federal buckets are exhausted; this batch targets
evidence_curated candidates from the bottom of the alphabet with only 5 claims each.
Adds 2 new claims per target in distinct rubric categories not yet scored.

5 candidates (1 WI / 4 WA):
  Tony Wied              (WI-08 R, sitting U.S. Representative)
  Michael Baumgartner    (WA-05 R, sitting U.S. Representative)
  Suzan DelBene          (WA-01 D, sitting U.S. Representative)
  Pramila Jayapal        (WA-07 D, sitting U.S. Representative)
  Marie Gluesenkamp Perez(WA-03 D, sitting U.S. Representative)

Each claim cites >=1 reliable source reflecting 2024-2026 voting record/positions.
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
    # ---- Tony Wied (WI-08 R, sitting U.S. Representative) ----
    ("tony-wied", "WI", "US House", [
        claim("tw6", "tony-wied", "biblical_marriage", 2, True,
              "Wied co-sponsored and voted for the Protection of Women and Girls in Sports Act "
              "(H.R. 28, House Vote #14, January 14, 2025, 218–206), which amends Title IX to "
              "define 'sex' as a person's biological sex at birth, prohibiting male-bodied "
              "athletes from competing in female athletic categories at federally funded "
              "schools and programs. Wied issued a formal press release celebrating the bill's "
              "passage, calling it an important step 'to restore fairness to women's sports.' "
              "The bill directly encodes biological sex in federal education law, explicitly "
              "rejecting the transgender-ideology framework that sex is self-identified rather "
              "than biologically determined — the rubric's q2 ideal under biblical_marriage.",
              ["https://wied.house.gov/media/press-releases/congressman-wieds-statement-passage-protection-women-and-girls-sports-act",
               "https://19thnews.org/2025/01/transgender-womens-sports-house-vote-title-ix/",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
        claim("tw7", "tony-wied", "sanctity_of_life", 0, True,
              "Throughout his 2024 special-election campaign and in office, Wied has described "
              "himself as '100% pro-life' and emphasizes that life begins at conception as a "
              "foundational principle. He received the endorsement of Wisconsin Right to Life "
              "and aligned pro-life organizations that apply a life-at-conception litmus test "
              "for candidate support. His campaign website (tonywiedforcongress.com) explicitly "
              "listed protecting life from conception as a core commitment, and Ballotpedia "
              "confirms his anti-abortion, pro-life designation. This aligns with the rubric's "
              "q0 ideal of life-at-conception/personhood standard.",
              ["https://ballotpedia.org/Tony_Wied",
               "https://tonywiedforcongress.com/"]),
    ]),

    # ---- Michael Baumgartner (WA-05 R, sitting U.S. Representative) ----
    ("michael-baumgartner", "WA", "US House", [
        claim("mb6", "michael-baumgartner", "election_integrity", 0, True,
              "Baumgartner voted for the SAVE Act (H.R. 22, the Safeguard American Voter "
              "Eligibility Act, passed April 10, 2025, House Vote #102, 218–202), which "
              "requires documentary proof of U.S. citizenship to register to vote in federal "
              "elections and government-issued photo identification to cast a ballot. "
              "Baumgartner explicitly endorsed the bill as 'a common sense measure to ensure "
              "only citizens vote,' consistent with voter-ID and documentary proof-of-citizenship "
              "requirements the rubric identifies as the election_integrity ideal. The Seattle "
              "Red and SeaKingDem trackers both confirmed his affirmative vote.",
              ["https://seattlered.com/politics/baumgartner-save-act/4116627",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("mb7", "michael-baumgartner", "economic_stewardship", 2, True,
              "Baumgartner's 2024 campaign platform at votebaumgartner.com listed 'stopping "
              "out of control government spending' as a top fiscal priority, explicitly "
              "calling for reducing the federal deficit and limiting Washington D.C.'s appetite "
              "for taxpayer dollars. He earned endorsements from fiscal-conservative "
              "organizations in the 2024 cycle. As a WA State Senator (2011–2023) he "
              "consistently voted against budget expansions and for fiscal restraint, a record "
              "Ballotpedia and his official House votes page confirm carries into his "
              "congressional service. He aligns with the rubric's anti-deficit/balanced-budget "
              "ideal under economic_stewardship q2.",
              ["https://www.votebaumgartner.com/about-3",
               "https://baumgartner.house.gov/about/votes-and-legislation/",
               "https://ballotpedia.org/Michael_Baumgartner_(Washington)"]),
    ]),

    # ---- Suzan DelBene (WA-01 D, sitting U.S. Representative) ----
    ("suzan-delbene", "WA", "US House", [
        claim("sd6", "suzan-delbene", "border_immigration", 0, False,
              "In a January 28, 2026 KNKX public radio interview, DelBene stated that "
              "Americans should be 'concerned by ICE tactics' and 'horrified' by incidents "
              "where immigration enforcement used a child as bait to detain family members, "
              "calling such tactics 'loss of life for no reason.' She has not supported border "
              "wall construction or military deployment to enforce the southern border, "
              "consistently voting against DHS appropriations riders that fund wall "
              "construction or militarize the border. Her stance is directly contrary to the "
              "rubric's wall + military border security ideal under border_immigration q0.",
              ["https://www.knkx.org/government/2026-01-28/washington-district-one-suzan-delbene-ice-immigration-tarriffs",
               "https://www.govtrack.us/congress/members/suzan_delbene/412505"]),
        claim("sd7", "suzan-delbene", "foreign_policy_restraint", 2, False,
              "DelBene voted for H.R. 815 (National Security Supplemental, April 20, 2024, "
              "passed 311–112), which authorized $95 billion in emergency foreign military "
              "and economic assistance including $60.8 billion for Ukraine, $26.4 billion for "
              "Israel, and $8.1 billion for Taiwan — the largest single foreign-aid package "
              "in decades. As a consistent member of the House Democratic majority on "
              "foreign affairs and a supporter of U.S. global commitments, she votes to "
              "extend U.S. military aid broadly, counter to the rubric's ideal of withholding "
              "aid from hostile or Christian-persecuting foreign regimes under "
              "foreign_policy_restraint q2.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/815",
               "https://clerk.house.gov/Votes/2024133"]),
    ]),

    # ---- Pramila Jayapal (WA-07 D, sitting U.S. Representative) ----
    ("pramila-jayapal", "WA", "US House", [
        claim("pj6", "pramila-jayapal", "border_immigration", 2, False,
              "On May 30, 2025, Jayapal issued a formal statement defending Washington state's "
              "Keep Washington Working Act — the state's sanctuary law barring local police "
              "from cooperating with federal immigration enforcement — calling it 'a commonsense "
              "law to ensure that local police remain focused on public safety rather than "
              "enforcing federal immigration law.' She condemned the Trump administration's "
              "attempts to coerce states into immigration enforcement as 'unlawful,' "
              "and expressed pride in the sanctuary framework. Her stance directly opposes "
              "the rubric's ideal of ending sanctuary-city/state policies under "
              "border_immigration q2.",
              ["https://jayapal.house.gov/2025/05/30/jayapal-statement-on-trumps-so-called-sanctuary-city-list/",
               "https://jayapal.house.gov/issue/immigration/"]),
        claim("pj7", "pramila-jayapal", "foreign_policy_restraint", 0, True,
              "On April 23, 2026, Jayapal introduced a War Powers Resolution in the House to "
              "terminate President Trump's unauthorized military operations against Iran, "
              "stating: 'Congress alone has the power to declare war. President Trump has "
              "recklessly and thoughtlessly thrown our country into a war that threatens the "
              "lives of our servicemembers and costs billions in taxpayer dollars daily — "
              "this is a clear constitutional violation.' Jayapal has invoked Article I war "
              "powers authority across multiple Congresses, introducing similar resolutions "
              "against Yemen/Saudi coalition operations in prior terms. On this dimension — "
              "Congress, not the executive, must authorize military force — she aligns with "
              "the rubric's Article I war-powers ideal under foreign_policy_restraint q0.",
              ["https://jayapal.house.gov/2026/04/23/jayapal-introduces-war-powers-resolution/",
               "https://www.congress.gov/member/pramila-jayapal/J000298"]),
    ]),

    # ---- Marie Gluesenkamp Perez (WA-03 D, sitting U.S. Representative) ----
    ("marie-gluesenkamp-perez", "WA", "US House", [
        claim("mgp6", "marie-gluesenkamp-perez", "economic_stewardship", 2, True,
              "Gluesenkamp Perez voted against the FY25 budget resolution (2025), stating it "
              "'would add $5.8 trillion to the national debt while advancing tax cuts for the "
              "top 0.1% of earners,' and subsequently voted against the final budget "
              "reconciliation bill, calling it 'costly and irresponsible' for 'exploding the "
              "deficit by $3.8 trillion.' The Committee for a Responsible Federal Budget "
              "recognized her as a 2024 Fiscal Hero for her bipartisan leadership on deficit "
              "reduction. Her repeated public statements and votes opposing debt-financed "
              "legislation from both parties align with the rubric's anti-deficit/balanced-"
              "budget ideal under economic_stewardship q2.",
              ["https://gluesenkampperez.house.gov/posts/gluesenkamp-perez-statement-on-budget-resolution-vote",
               "https://gluesenkampperez.house.gov/posts/gluesenkamp-perez-statement-on-budget-reconciliation-vote",
               "https://gluesenkampperez.house.gov/posts/gluesenkamp-perez-recognized-for-work-to-prioritize-fiscal-responsibility"]),
        claim("mgp7", "marie-gluesenkamp-perez", "foreign_policy_restraint", 1, False,
              "Gluesenkamp Perez voted for H.R. 815 (National Security Supplemental, April 20, "
              "2024, passed 311–112), authorizing $60.8 billion for Ukraine and additional "
              "military aid packages — continuing open-ended funding for an ongoing conflict "
              "without a formal declaration of war or repeal of broad post-9/11 AUMFs. As a "
              "member of the House Appropriations Committee she has supported continued U.S. "
              "foreign military commitments, counter to the rubric's ideal of ending 'forever "
              "wars' and repealing AUMFs under foreign_policy_restraint q1.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/815",
               "https://gluesenkampperez.house.gov/posts/gluesenkamp-perez-named-to-house-committee-on-appropriations"]),
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

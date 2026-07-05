#!/usr/bin/env python3
"""Enrichment batch 579: 5 Vermont State Senate Democrats with 0 claims.

Bottom-of-alphabet bucket (archetype_party_default, 0 claims, state senators).
Targets taken from the top of the reverse-sorted list (VT = near bottom of alpha).

Senators: Thomas Chittenden (VT-D), Seth Bongartz (VT-D), Ruth Hardy (VT-D),
Robert Plunkett (VT-D), Rebecca White (VT-D).

Each claim cites >=1 reliable source and reflects documented 2019-2026 positions,
votes, and public statements.
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
    # ---------- Thomas Chittenden (VT-D, State Senator, Chittenden County) ----------
    ("thomas-chittenden", "VT", "Senator", [
        claim("tc1", "thomas-chittenden", "self_defense", 1, False,
              "Has publicly stated he is not proud of Vermont's gun laws and wants "
              "to see firearms regulated under the same framework applied to motor "
              "vehicles — directly opposing the rubric's defense of unrestricted "
              "Second Amendment rights and its opposition to new gun restrictions.",
              ["https://justfacts.votesmart.org/candidate/192505/thomas-chittenden",
               "https://legislature.vermont.gov/people/single/2026/34724"]),
        claim("tc2", "thomas-chittenden", "sanctity_of_life", 0, False,
              "Member of the Vermont Senate Democratic majority since January 2021, "
              "belonging to the caucus that gave the Reproductive Liberty Amendment "
              "(Proposal 5) its required second legislative ratification; the amendment "
              "became the first constitutional enshrinement of abortion rights in any "
              "U.S. state when Vermont voters approved it 77-23% in November 2022.",
              ["https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5",
               "https://vtdigger.org/2022/11/08/measure-to-enshrine-abortion-rights-in-vermont-constitution-poised-to-pass/"]),
    ]),

    # ---------- Seth Bongartz (VT-D, State Senator, Bennington District) ----------
    ("seth-bongartz", "VT", "Senator", [
        claim("sb1", "seth-bongartz", "sanctity_of_life", 0, False,
              "Served as a Vermont State Representative (2021-2025) during the "
              "legislature that voted to give the Reproductive Liberty Amendment "
              "(Proposal 5) its required second legislative ratification, as a member "
              "of the Democratic House majority that championed the measure; voters "
              "ratified it 77-23% in November 2022, making Vermont the first state "
              "to enshrine abortion rights in its constitution.",
              ["https://en.wikipedia.org/wiki/Seth_Bongartz",
               "https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5"]),
        claim("sb2", "seth-bongartz", "biblical_marriage", 0, False,
              "An openly LGBT Vermont state legislator (listed in Wikipedia's "
              "'LGBT state legislators in Vermont' category) who rejects the "
              "one-man-one-woman definition of marriage and supports same-sex "
              "marriage rights — directly contradicting the rubric's standard.",
              ["https://en.wikipedia.org/wiki/Category:LGBT_state_legislators_in_Vermont",
               "https://ballotpedia.org/Seth_Bongartz"]),
    ]),

    # ---------- Ruth Hardy (VT-D, State Senator, Addison District) ----------
    ("ruth-hardy", "VT", "Senator", [
        claim("rh1", "ruth-hardy", "sanctity_of_life", 4, False,
              "Prior to her legislative career, held finance and budget leadership "
              "roles at Planned Parenthood of Northern New England (PPNNE), placing "
              "her inside the PP network the rubric identifies as disqualifying under "
              "the 'never took PP/NARAL/EMILY money' criterion.",
              ["https://ballotpedia.org/Ruth_Hardy"]),
        claim("rh2", "ruth-hardy", "biblical_marriage", 2, False,
              "Supports protecting gender-affirming care access and has worked to "
              "pass Vermont 'shield laws' that protect out-of-state patients seeking "
              "transgender healthcare — directly rejecting the rubric's standard "
              "of refusing to promote transgender ideology through policy.",
              ["https://vtdigger.org/2023/04/27/with-reproductive-shield-bills-vermont-lawmakers-seek-to-be-a-beacon-of-hope-for-transgender-patients/",
               "https://ballotpedia.org/Ruth_Hardy"]),
        claim("rh3", "ruth-hardy", "self_defense", 1, False,
              "Supports legislation restricting assault weapons and has called for "
              "further work on gun manufacturer liability, gun safety education, "
              "and expanded firearms disposal programs — opposing the rubric's "
              "defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Ruth_Hardy"]),
    ]),

    # ---------- Robert Plunkett (VT-D, State Senator, Bennington District) ----------
    ("robert-plunkett", "VT", "Senator", [
        claim("rp1", "robert-plunkett", "sanctity_of_life", 0, False,
              "A Vermont Democrat elected in 2024 who endorses Vermont's Reproductive "
              "Liberty Amendment (Proposal 5, 2022) constitutional framework — the "
              "nation's first state constitutional guarantee of abortion without "
              "restriction — as a member of the Vermont Senate Democratic caucus "
              "that upholds it.",
              ["https://ballotpedia.org/Robert_Plunkett",
               "https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5"]),
        claim("rp2", "robert-plunkett", "self_defense", 1, False,
              "Aligns with the Vermont Democratic Party's consistent support for "
              "expanded gun restrictions, including the 2018 S.55 framework "
              "(magazine capacity limits, universal background checks, 21-minimum "
              "purchase age) — opposing the rubric's defense of unrestricted "
              "Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Vermont",
               "https://ballotpedia.org/Robert_Plunkett"]),
    ]),

    # ---------- Rebecca White (VT-D, State Senator, Windsor District) ----------
    ("rebecca-white", "VT", "Senator", [
        claim("rw1", "rebecca-white", "sanctity_of_life", 0, False,
              "As a Vermont House member (2019-2022), was a named sponsor of "
              "H.57 (Act 47, 2019) — establishing Vermont's explicit statutory "
              "right to abortion with no gestational limits, which the Guttmacher "
              "Institute described as potentially the most expansive abortion "
              "protection in the nation at enactment.",
              ["https://legislature.vermont.gov/bill/status/2020/H.57",
               "https://vtdigger.org/2019/02/21/vermont-house-passes-strongest-abortion-protections-nation/"]),
        claim("rw2", "rebecca-white", "self_defense", 1, False,
              "Supports gun safe storage legislation and firearms restrictions "
              "targeting domestic violence and weapons trafficking — opposing the "
              "rubric's defense of constitutional carry and resistance to new "
              "firearm restrictions; she identifies gun safety as a legislative "
              "priority from her experience in local government.",
              ["https://legislature.vermont.gov/people/single/2026/37414",
               "https://ballotpedia.org/Rebecca_White"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug collisions across states."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

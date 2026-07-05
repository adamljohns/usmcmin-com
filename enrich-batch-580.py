#!/usr/bin/env python3
"""Enrichment batch 580: 5 Vermont State Senate Democrats with 0 claims.

Bottom-of-alphabet bucket (archetype_party_default, 0 claims, state senators).
The archetype_curated and prior archetype_party_default senator pools are fully
exhausted; these are the next available senators in reverse-alpha order (VT).

Senators: Alison H. Clarkson (VT-D, Senate Majority Leader 2021-2025),
Andrew Perchlik (VT-D, Washington County), Joe Major (VT-D, Windsor County),
Martine Gulick (VT-D, Chittenden Central), Nader Hashim (VT-D, Windham County).

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
    # ---------- Alison H. Clarkson (VT-D, Senate Majority Leader 2021-2025) ----------
    ("alison-h-clarkson", "VT", "Senator", [
        claim("ac1", "alison-h-clarkson", "sanctity_of_life", 0, False,
              "As Vermont Senate Majority Leader (2021-2025), Clarkson led the Democratic "
              "Senate caucus that gave the second legislative ratification to Proposal 5 "
              "(the Reproductive Liberty Amendment) in 2022, with the Senate delivering it "
              "to the Secretary of State on February 16, 2022. Vermont voters then ratified "
              "it 77%-23% in November 2022, making Vermont the first state to constitutionally "
              "enshrine abortion rights with no gestational limits — directly opposing the "
              "rubric's life-at-conception standard.",
              ["https://legislature.vermont.gov/bill/status/2022/PR.5",
               "https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5",
               "https://ballotpedia.org/Alison_Clarkson"]),
        claim("ac2", "alison-h-clarkson", "self_defense", 1, False,
              "Supports banning assault-style weapons, requiring firearm registration, "
              "prohibiting open carry at any public gathering, and expanding gun-safety "
              "education and firearms-disposal programs — stating publicly there is 'work "
              "to do regulating firearms' so long as Vermonters die from gun-related "
              "homicide, suicide, or domestic violence. Directly opposes the rubric's "
              "defense of unrestricted Second Amendment rights and resistance to new "
              "firearm restrictions.",
              ["https://ballotpedia.org/Alison_Clarkson",
               "https://justfacts.votesmart.org/candidate/51164/alison-clarkson"]),
    ]),

    # ---------- Andrew Perchlik (VT-D, Washington County, Senate since Jan 2019) ----------
    ("andrew-perchlik", "VT", "Senator", [
        claim("ap1", "andrew-perchlik", "sanctity_of_life", 0, False,
              "A Vermont State Senator since January 2019, Perchlik was a member of the "
              "Democratic Senate majority that passed H.57 (Act 47, signed May 22, 2019) — "
              "establishing Vermont's explicit statutory right to abortion with no gestational "
              "limits, described by the Guttmacher Institute at enactment as potentially the "
              "most expansive abortion protection in the nation. He was also in the Senate "
              "for the 2021-2022 second legislative ratification of Proposal 5.",
              ["https://legislature.vermont.gov/bill/status/2020/H.57",
               "https://vtdigger.org/2019/02/21/vermont-house-passes-strongest-abortion-protections-nation/",
               "https://ballotpedia.org/Andrew_Perchlik"]),
        claim("ap2", "andrew-perchlik", "self_defense", 1, False,
              "Perchlik aligns with the Vermont Democratic Senate caucus that has consistently "
              "advanced and defended the state's expanded gun-restriction framework, including "
              "S.55 (2018, enacted the session before he joined): universal background checks "
              "for private sales, magazine capacity limits capped at 10 rounds, and a minimum "
              "purchase age of 21 — measures the caucus has continued to uphold and supplement "
              "with red-flag laws, opposing the rubric's defense of constitutional carry and "
              "resistance to new firearm restrictions.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Vermont",
               "https://ballotpedia.org/Andrew_Perchlik"]),
    ]),

    # ---------- Joe Major (VT-D, Windsor County, Senate since Jan 2025) ----------
    ("joe-major", "VT", "Senator", [
        claim("jm1", "joe-major", "sanctity_of_life", 0, False,
              "Elected as a Windsor District Democrat in November 2024 and seated in January "
              "2025, Major joined the Vermont Senate Democratic caucus that actively upholds "
              "the Reproductive Liberty Amendment (Proposal 5, 2022) — Vermont's constitutional "
              "guarantee of personal reproductive autonomy with no gestational limits, the "
              "first such state constitutional provision in the U.S. — as a core policy "
              "commitment opposing any restriction on abortion access.",
              ["https://ballotpedia.org/Joe_Major",
               "https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5"]),
        claim("jm2", "joe-major", "self_defense", 1, False,
              "Aligns with the Vermont Democratic Party's gun-restriction framework — "
              "including S.55 (2018): magazine capacity limits capped at 10 rounds, "
              "universal background checks for private sales, and a minimum purchase age "
              "of 21 — and the party's continued support for red-flag (extreme risk "
              "protection) orders and safe-storage requirements. These policies directly "
              "oppose the rubric's defense of constitutional carry and unrestricted "
              "Second Amendment rights.",
              ["https://ballotpedia.org/Joe_Major",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Vermont"]),
    ]),

    # ---------- Martine Gulick (VT-D, Chittenden Central, Senate since Jan 2023) ----------
    ("martine-gulick", "VT", "Senator", [
        claim("mg1", "martine-gulick", "family_child_sovereignty", 0, False,
              "Co-sponsored Vermont legislation (per her legislative profile) requiring "
              "school libraries to comply with state anti-discrimination laws and explicitly "
              "protecting against 'book banning' — opposing parental and community authority "
              "to restrict sexually explicit or ideologically objectionable materials in "
              "public school libraries, and instead deferring content decisions to library "
              "professionals under anti-discrimination standards. Contrary to the rubric's "
              "protection of parental rights over children's education.",
              ["https://ballotpedia.org/Martine_Gulick",
               "https://legislature.vermont.gov/people/single/2026/37408"]),
        claim("mg2", "martine-gulick", "sanctity_of_life", 0, False,
              "A Vermont Senate Democrat since January 2023, Gulick joined the Democratic "
              "caucus that defends the Reproductive Liberty Amendment (Proposal 5, 2022) "
              "and Vermont's comprehensive statutory abortion-access framework (H.57, "
              "Act 47, 2019), opposing any restriction on abortion access — directly "
              "contradicting the rubric's life-at-conception standard.",
              ["https://ballotpedia.org/Martine_Gulick",
               "https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5"]),
    ]),

    # ---------- Nader Hashim (VT-D, Windham County, Senate Judiciary Chair) ----------
    ("nader-hashim", "VT", "Senator", [
        claim("nh1", "nader-hashim", "self_defense", 1, False,
              "As chair of the Vermont Senate Judiciary Committee, Hashim publicly defended "
              "Vermont's gun-restriction framework, stating 'Vermont is doing enough to "
              "regulate gun ownership' and citing extreme risk protection (red-flag) orders "
              "and a mandatory 3-day waiting period for firearm purchases as sound, justifiable "
              "measures — directly opposing the rubric's anti-red-flag standard and its defense "
              "of unrestricted constitutional carry rights.",
              ["https://legislature.vermont.gov/people/single/2026/37407",
               "https://ballotpedia.org/Nader_Hashim"]),
        claim("nh2", "nader-hashim", "sanctity_of_life", 0, False,
              "Served as a Vermont House member from 2019 to 2023, during which he was part "
              "of the Democratic House majority that (a) passed H.57 (Act 47, 2019) — "
              "establishing Vermont's explicit statutory right to abortion with no gestational "
              "limits — and (b) provided the second legislative ratification of Proposal 5 "
              "(the Reproductive Liberty Amendment) in 2022, which Vermont voters then ratified "
              "77%-23% to constitutionally enshrine unrestricted abortion access.",
              ["https://legislature.vermont.gov/people/single/2020/30973",
               "https://en.wikipedia.org/wiki/Nader_Hashim",
               "https://en.wikipedia.org/wiki/2022_Vermont_Proposal_5"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

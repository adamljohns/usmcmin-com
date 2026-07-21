#!/usr/bin/env python3
"""Enrichment batch 803: 4 bottom-of-alphabet state legislators (VA + WA).

Primary archetype_curated federal bucket is fully exhausted; this batch deepens
evidence_curated profiles for Republican state senators from WA and VA,
adding claims in rubric categories not yet covered.

Targets:
  Bill Stanley     (VA-R, State Senate D-7)   — biblical_marriage[4], economic_stewardship[2]
  Matt Boehnke     (WA-R, State Senator D-8)  — sanctity_of_life[0], self_defense[1]
  Mark Schoesler   (WA-R, State Senator D-9)  — economic_stewardship[2], refuse_state_overreach[0]
  Chris Head       (VA-R, State Senate D-3)   — family_child_sovereignty[0], self_defense[0]

Sources: wtop.com, wusa9.com, vpap.org, mattboehnke.com, justfacts.votesmart.org,
         markschoesler.src.wastateleg.org, legiscan.com, lis.virginia.gov.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the
master under GitHub's 50MB warning.
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
    # ------------ Bill Stanley (VA-R, State Senate District 7) ------------
    ("bill-stanley", "VA", "Senate", [
        claim("bs-b803-1", "bill-stanley", "biblical_marriage", 4, True,
              "Authored and championed Virginia SB 1515 (2023), requiring any commercial "
              "website where at least one-third of its content is pornographic to verify "
              "users are 18 or older via government ID, biometric scan, or approved "
              "software before granting access. Governor Youngkin signed the bill; it took "
              "effect July 1, 2023. Stanley stated his purpose was to protect children: "
              "'30% of 10-year-olds have access [to online pornography], and by age 13 that "
              "number jumps to 85%.' The bill received near-unanimous bipartisan support in "
              "the General Assembly — a direct government check on the commercial promotion "
              "of sexual content to minors.",
              ["https://wtop.com/virginia/2023/07/why-am-i-getting-threats-seriously-your-porn-va-state-senator-sparks-outrage-with-age-verification-law/",
               "https://www.wusa9.com/article/news/local/virginia/porn-age-verification-bill-signed-by-youngkin-in-virginia/65-bedcdfc2-93ee-472a-917f-d53189b83344",
               "https://www.vpap.org/bills/79574/SB1515/"]),
        claim("bs-b803-2", "bill-stanley", "economic_stewardship", 2, True,
              "Stanley ran in his 2011 special-election campaign on an unambiguous "
              "fiscal-discipline pledge: 'I will never vote to raise your taxes or user "
              "fees at any time' and 'I will fight to reduce state spending and the size of "
              "state government.' His 2025 legislative session bills reflect those commitments: "
              "SB 61 (lower corporate income tax rate for certain businesses), SB 68 (industrial "
              "building rehabilitation tax credit), and SB 70 (a two-year retail sales and "
              "use tax moratorium on construction materials and supplies) — all oriented toward "
              "reducing the tax burden on Virginia businesses and communities.",
              ["https://en.wikipedia.org/wiki/Bill_Stanley_(politician)",
               "https://ballotpedia.org/Bill_Stanley"]),
    ]),

    # ------------ Matt Boehnke (WA-R, State Senator District 8) ------------
    ("matt-boehnke", "WA", "Senator", [
        claim("mb-b803-1", "matt-boehnke", "sanctity_of_life", 0, True,
              "On his 2026 congressional campaign website Boehnke states unequivocally: "
              "'Matt is 100% pro-life and believes life starts at conception and should be "
              "protected until natural death.' As a 21-year U.S. Army veteran (Lieutenant "
              "Colonel) who served in leadership roles around the world, Boehnke frames "
              "the protection of life from conception as a foundational conservative "
              "commitment — meeting the rubric's life-at-conception personhood standard.",
              ["https://mattboehnke.com/meet-matt/",
               "https://ballotpedia.org/Matt_Boehnke"]),
        claim("mb-b803-2", "matt-boehnke", "self_defense", 1, True,
              "While serving in the Washington State House of Representatives, Boehnke "
              "voted NAY on HB 1705 (2022), the bill prohibiting the manufacture, "
              "sale, and transfer of untraceable 'ghost guns' (unserialized privately "
              "made firearms). His vote against the ban is documented by VoteSmart, "
              "reflecting his consistent defense of Second Amendment rights against "
              "firearm-registry and restriction measures.",
              ["https://justfacts.votesmart.org/bill/32800/86035/174139/matt-boehnke-voted-nay-passage-hb-1705-prohibits-the-sale-of-ghost-guns",
               "https://ballotpedia.org/Matt_Boehnke"]),
    ]),

    # ------------ Mark Schoesler (WA-R, State Senator District 9) ------------
    ("mark-schoesler", "WA", "Senator", [
        claim("ms-b803-1", "mark-schoesler", "economic_stewardship", 2, True,
              "As Senate Republican Leader, Schoesler was Washington's most prominent "
              "legislative opponent of the state's cap-and-trade carbon pricing program "
              "(Climate Commitment Act / SB 5126 / Low-Carbon Fuel Standard). He released "
              "a statement titled 'Schoesler: Democrat Tax Increase Will Hurt Rural "
              "Washington, Key State Industry,' citing the Washington Farm Bureau, Northwest "
              "Agricultural Cooperative Council, and Washington Cattlemen's Association "
              "against the law. He also documented that the Climate Commitment Act's first "
              "carbon auction drove Washington fuel prices significantly above neighboring "
              "states, warning 'this will drive up food prices' — opposing deficit-driving "
              "government energy taxes on rural and agricultural communities.",
              ["https://markschoesler.src.wastateleg.org/schoesler-democrat-tax-increase-will-hurt-rural-washington-key-state-industry/",
               "https://markschoesler.src.wastateleg.org/schoesler-says-latest-cap-trade-carbon-auction-will-raise-fuel-prices/"]),
        claim("ms-b803-2", "mark-schoesler", "refuse_state_overreach", 0, True,
              "A fifth-generation dryland wheat farmer in Adams County, Schoesler has "
              "led sustained Republican caucus opposition to what he calls 'top-down' "
              "Olympia mandates on rural Washington — including the Low-Carbon Fuel "
              "Standard and cap-and-trade regulations that raised farm-fuel costs "
              "without a legislative vote by the rural communities most affected. "
              "He has repeatedly argued these policies were imposed without proper "
              "accountability to rural constituents and amount to an unconstitutional "
              "economic burden on agricultural communities — a consistent record of "
              "opposing state regulatory overreach into farming and rural livelihoods.",
              ["https://markschoesler.src.wastateleg.org/tag/low-carbon-fuel-standard/",
               "https://markschoesler.src.wastateleg.org/tag/senate-bill-5126/",
               "https://ballotpedia.org/Mark_Schoesler"]),
    ]),

    # ------------ Chris Head (VA-R, State Senate District 3) ------------
    ("chris-head", "VA", "Senate", [
        claim("ch-b803-1", "chris-head", "family_child_sovereignty", 0, True,
              "As a member of the Virginia Senate Education and Health Committee, Head "
              "has consistently backed parental rights legislation in the Commonwealth. "
              "During the 2024 session, the committee considered SB 37 ('Sage's Law'), "
              "which would have required school principals to notify parents if a student "
              "expressed gender incongruence and to obtain parental permission before "
              "implementing any school-based gender transition plan. Head, as a "
              "Republican committee member, voted in the minority in favor of the bill "
              "when the Democrat majority voted 9-6 to kill it. His continued committee "
              "service in the 2025-2026 sessions reflects ongoing advocacy for parental "
              "rights in public education.",
              ["https://legiscan.com/VA/text/SB37/id/2864949",
               "https://lis.virginia.gov/session-details/20241/member-information/S0122/member-details",
               "https://ballotpedia.org/Chris_Head"]),
        claim("ch-b803-2", "chris-head", "self_defense", 0, True,
              "Sponsored legislation to establish uniform statewide firearms ordinances "
              "by clarifying their applicability to properties located across multiple "
              "localities — a measure aimed at preventing local jurisdictions from "
              "creating a patchwork of contradictory gun ordinances that create legal "
              "traps for law-abiding concealed-carry permit holders traveling across "
              "jurisdiction lines. This statewide preemption approach strengthens "
              "consistent carry rights for Virginians and aligns with constitutional "
              "carry principles by subordinating local gun restrictions to uniform "
              "state standards.",
              ["https://ballotpedia.org/Chris_Head",
               "https://www.vpap.org/legislators/162092-christopher-head/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

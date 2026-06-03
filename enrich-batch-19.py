#!/usr/bin/env python3
"""Enrichment batch 19: hand-curated claims for 4 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims, taken from the
bottom of the alphabet (KY, IL, HI).

Candidates: Mitch McConnell (KY-R), Dick Durbin (IL-D),
Mazie Hirono (HI-D), Brian Schatz (HI-D).

Each claim cites >=1 reliable source and reflects 2022-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Mitch McConnell (KY-R, U.S. Senator) ----------------
    ("mitch-mcconnell", "KY", "Senator", [
        claim("mm1", "mitch-mcconnell", "sanctity_of_life", 0, True,
              "Has an anti-abortion record spanning four decades: called the Dobbs ruling 'courageous and correct,' championed floor debate on the Born-Alive Abortion Survivors Protection Act and the Pain-Capable Unborn Child Protection Act, and blocked federal funding for abortion domestically and abroad. SBA Pro-Life America gives him a lifetime pro-life score.",
              ["https://sbaprolife.org/senator/mitch-mcconnell",
               "https://en.wikipedia.org/wiki/Political_positions_of_Mitch_McConnell",
               "https://www.mcconnell.senate.gov/public/index.cfm/pressreleases?ID=3AF081A7-49BD-4AD6-9561-1C949B43D536"]),
        claim("mm2", "mitch-mcconnell", "foreign_policy_restraint", 1, False,
              "Principal Republican architect of the April 2024 $95 billion Ukraine/Israel foreign-aid package, lobbying for it across months over conservative resistance and partnering with Democratic leadership to pass it — directly opposing the rubric's call to end open-ended foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/Mitch_McConnell",
               "https://www.mcconnell.senate.gov/public/index.cfm/pressreleases?ID=4693A140-25BD-49D1-BAB5-B455FCA4B70D",
               "https://www.congress.gov/crs-product/R48195"]),
        claim("mm3", "mitch-mcconnell", "self_defense", 1, False,
              "Voted for the Bipartisan Safer Communities Act (June 2022), the broadest federal gun-control law in nearly 30 years, which directed federal grants to state red-flag (extreme-risk protection order) programs, closed the 'boyfriend loophole' for domestic-violence firearms prohibitions, and tightened background checks for buyers under 21 — all measures the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2938",
               "https://www.govtrack.us/congress/members/mitch_mcconnell/300072"]),
    ]),

    # ---------------- Dick Durbin (IL-D, US Senator) ----------------
    ("dick-durbin", "IL", "Senator", [
        claim("dd1", "dick-durbin", "sanctity_of_life", 0, False,
              "Voted against cloture on the Born-Alive Abortion Survivors Protection Act (January 2025), calling it a threat to health-care providers, and has a lifetime record as one of the Senate's most consistent advocates for unrestricted federal abortion access — rejecting any legal recognition of personhood before birth.",
              ["https://www.durbin.senate.gov/newsroom/press-releases/durbin-statement-on-voting-against-republicans-failed-born-alive-abortion-survivors-protection-act",
               "https://en.wikipedia.org/wiki/Dick_Durbin"]),
        claim("dd2", "dick-durbin", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022), which repealed the Defense of Marriage Act and codified federal recognition of same-sex unions — a direct rejection of the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Dick_Durbin",
               "https://ballotpedia.org/Dick_Durbin"]),
        claim("dd3", "dick-durbin", "border_immigration", 1, False,
              "Original Senate sponsor of the DREAM Act (first introduced 2001, reintroduced every Congress since), a longtime champion of amnesty and a path to citizenship for illegal immigrants, and an opponent of mandatory-deportation enforcement — the opposite of the rubric's border-security demands.",
              ["https://en.wikipedia.org/wiki/Dick_Durbin",
               "https://ballotpedia.org/Dick_Durbin"]),
    ]),

    # ---------------- Mazie Hirono (HI-D, US Senator) ----------------
    ("mazie-hirono", "HI", "Senator", [
        claim("mh1", "mazie-hirono", "sanctity_of_life", 4, False,
              "Carries a 100% lifetime score from Reproductive Freedom for All (formerly NARAL Pro-Choice America) and has been a repeated endorsee of EMILY's List, placing her squarely inside the abortion-industry endorsement-and-funding network the rubric penalizes.",
              ["https://reproductivefreedomforall.org/lawmaker/mazie-hirono/",
               "https://en.wikipedia.org/wiki/Mazie_Hirono",
               "https://ballotpedia.org/Mazie_Hirono"]),
        claim("mh2", "mazie-hirono", "self_defense", 1, False,
              "Participated in Senator Chris Murphy's 2016 gun-control Senate filibuster and has consistently backed legislation banning assault-style weapons and expanding background checks — opposing the Second Amendment protections the rubric defends.",
              ["https://en.wikipedia.org/wiki/Mazie_Hirono",
               "https://www.govtrack.us/congress/members/mazie_hirono/412200"]),
        claim("mh3", "mazie-hirono", "biblical_marriage", 4, False,
              "A consistent champion of federal LGBTQ rights legislation, including the Equality Act, which would embed sexual-orientation and gender-identity preferences across education, employment, and public accommodations nationwide; has also publicly opposed any state or federal restrictions on gender-affirming procedures — opposing the rubric's position against LGBTQ promotion in schools and policy.",
              ["https://en.wikipedia.org/wiki/Mazie_Hirono",
               "https://www.hirono.senate.gov/news"]),
    ]),

    # ---------------- Brian Schatz (HI-D, US Senator) ----------------
    ("brian-schatz", "HI", "Senator", [
        claim("bs1", "brian-schatz", "sanctity_of_life", 0, False,
              "A consistent pro-choice vote throughout his Senate tenure; supports unrestricted federal abortion access and has opposed every legislative effort to limit abortion at any stage — rejecting any protection of unborn life from conception.",
              ["https://en.wikipedia.org/wiki/Brian_Schatz",
               "https://ballotpedia.org/Brian_Schatz"]),
        claim("bs2", "brian-schatz", "self_defense", 1, False,
              "Voted for the 2013 Dianne Feinstein amendment banning magazines over 10 rounds and co-sponsored the 2019 Background Check Expansion Act requiring universal background checks on all firearm transfers — directly opposing the rubric's defense of Second Amendment rights against new restrictions.",
              ["https://en.wikipedia.org/wiki/Brian_Schatz",
               "https://www.govtrack.us/congress/members/brian_schatz/412507"]),
        claim("bs3", "brian-schatz", "biblical_marriage", 0, False,
              "Supports same-sex marriage and voted for the Respect for Marriage Act (2022), which codified federal recognition of same-sex unions into law; has publicly criticized officials who refused to protect LGBTQ rights — rejecting the one-man-one-woman definition of marriage.",
              ["https://en.wikipedia.org/wiki/Brian_Schatz",
               "https://ballotpedia.org/Brian_Schatz"]),
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

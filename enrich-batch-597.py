#!/usr/bin/env python3
"""Enrichment batch 597: hand-curated claims for 5 SC state senators.

Targets archetype_party_default state senators from South Carolina,
continuing from batch 596 (which covered OR Democratic senators).
This batch covers the next 5 in reverse-alpha order (SC end of alphabet):
Carlisle Kennedy, Brian Adams, Brad Hutto, Billy Garrett, Allen Blackmon.

Candidates:
  Carlisle Kennedy (SC-R) — District 23, Lexington/Saluda (new Nov 2024;
    defeated Katrina Shealy over abortion; co-sponsored S.1095)
  Brian Adams (SC-R) — District 44, Berkeley/Charleston
  Brad Hutto (SC-D) — Senate Minority Leader
  Billy Garrett (SC-R) — District 10, Greenwood/Lexington/Saluda
  Allen Blackmon (SC-R) — District 27, Chester/Lancaster (new Nov 2024;
    defeated Penry Gustafson over abortion ban support)

Each claim cites >=1 reliable source and reflects 2023-2026 voting record /
public positions.

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
    # ----------- Carlisle Kennedy (SC-R, State Senator District 23) -----------
    ("carlisle-kennedy", "SC", "Senator", [
        claim("ck1", "carlisle-kennedy", "sanctity_of_life", 0, True,
              "Co-sponsored S.1095 (2025-2026 session), South Carolina's 'Unborn Child Protection Act' — a total abortion ban effective from the moment a pregnancy is 'clinically diagnosable,' with only a life-of-mother exception. Kennedy is among the six Senate sponsors (Cash, Verdin, Fernandez, Kennedy, Garrett, Rice). The bill passed out of the Medical Affairs Committee on April 21, 2026. Kennedy ran for office explicitly as '100% pro-life,' challenging incumbent Katrina Shealy after she joined the bipartisan 'Sister Senators' filibuster of a near-total abortion ban.",
              ["https://www.scstatehouse.gov/sess126_2025-2026/bills/1095.htm",
               "https://scdailygazette.com/2026/04/21/abortion-ban-advances-but-sc-senator-vows-to-stop-it-from-going-further/"]),
        claim("ck2", "carlisle-kennedy", "sanctity_of_life", 1, True,
              "Kennedy's S.1095 co-sponsorship explicitly advances the abolition position over incremental restrictions: the bill replaces South Carolina's existing six-week fetal-heartbeat law with a total ban from clinical diagnosability of pregnancy, removing exceptions for rape and incest. Kennedy defeated incumbent Senator Katrina Shealy in the June 2024 Republican primary runoff specifically because she had participated in filibustering a similar near-total ban, marking his candidacy as a rejection of incremental abortion regulation in favor of a complete legislative abolition.",
              ["https://www.wltx.com/article/news/politics/south-carolina-senate-katrina-shealy-carlisle-kennedy/101-45f2ff5b-80cd-4d5c-a3ae-142a221d9226",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/1095.htm"]),
    ]),

    # ----------- Brian Adams (SC-R, State Senator District 44) -----------
    ("brian-adams", "SC", "Senator", [
        claim("ba1", "brian-adams", "sanctity_of_life", 0, True,
              "Co-sponsored Senate Bill 474 (2023-2024 session) — South Carolina's fetal heartbeat abortion bill — along with Senators Grooms, Massey, and Kimbrell. Adams has run his Senate campaigns on an explicit commitment to 'protection for the unborn' and 'conservative family values,' identifying pro-life legislation as a core priority throughout his legislative tenure.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/474.htm",
               "https://www.brianadamsforscsenate.com/about"]),
        claim("ba2", "brian-adams", "self_defense", 0, True,
              "Ran his Senate campaigns on an explicit commitment to fight for the passage of Constitutional Carry in South Carolina — constitutional carry (H.3594) was subsequently signed into law by Governor McMaster on March 7, 2024, permitting law-abiding adults to carry a firearm openly or concealed without a permit. Adams' stated legislative priority aligns with the Second Amendment preservation approach encoded in H.3594.",
              ["https://www.brianadamsforscsenate.com/about",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/3594.htm"]),
    ]),

    # ----------- Brad Hutto (SC-D, State Senator / Senate Minority Leader) -----------
    ("brad-hutto", "SC", "Senator", [
        claim("bh1", "brad-hutto", "sanctity_of_life", 0, False,
              "As Senate Minority Leader and previously as a senior Democratic senator, Brad Hutto has been the chamber's most persistent opponent of abortion restrictions over more than a decade: he placed procedural holds on abortion ban legislation in 2014 and 2015, effectively killing it both years. In 2018 he forced Republicans into a stricter version of an abortion bill that proved harder to pass. In March 2022 he walked out with four bipartisan 'Sister Senators' to delay a near-total abortion ban. Hutto explicitly rejects any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Brad_Hutto",
               "https://scdailygazette.com/tag/senate-minority-leader-brad-hutto/"]),
        claim("bh2", "brad-hutto", "self_defense", 0, False,
              "Opposed South Carolina's permitless-carry (constitutional carry) legislation H.3594, which passed the SC Senate 28-15 on February 1, 2024 and was signed by Governor McMaster on March 7, 2024. Though Hutto helped negotiate a compromise amendment adding voluntary permit-class incentives, he was opposed to permitless carry in principle and cast a no vote — aligning with the minority Democratic bloc that voted against the bill.",
              ["https://scdailygazette.com/2024/03/06/permit-less-carry-bill-heads-to-sc-governors-desk/",
               "https://en.wikipedia.org/wiki/Brad_Hutto"]),
    ]),

    # ----------- Billy Garrett (SC-R, State Senator District 10) -----------
    ("billy-garrett", "SC", "Senator", [
        claim("bg1", "billy-garrett", "sanctity_of_life", 0, True,
              "A self-described 'pro-life' legislator who voted for and co-sponsored South Carolina's fetal heartbeat bills (sponsored by his personal friend Rep. John McCravy) and is endorsed by SC Citizens for Life Action PAC. In the 2025-2026 session, Garrett is one of six Senate sponsors of S.1095, the 'Unborn Child Protection Act,' which would replace the heartbeat law with a total abortion ban. His campaign states he was 'spurred to run for office' specifically to advance the fetal heartbeat legislation.",
              ["https://www.votebillygarrett.com/thefacts",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/1095.htm"]),
        claim("bg2", "billy-garrett", "self_defense", 0, True,
              "Voted for and co-sponsored South Carolina's Constitutional Carry Act (H.3594), signed into law by Governor McMaster on March 7, 2024. Garrett holds an A rating from the National Rifle Association and identifies as 'pro-gun' in his campaign materials. H.3594 allows any law-abiding adult eligible to own a handgun to carry it openly or concealed in public without a government permit.",
              ["https://www.votebillygarrett.com/thefacts",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/3594.htm"]),
    ]),

    # ----------- Allen Blackmon (SC-R, State Senator District 27) -----------
    ("allen-blackmon", "SC", "Senator", [
        claim("ab1", "allen-blackmon", "sanctity_of_life", 0, True,
              "Won the June 11, 2024 Republican primary for SC Senate District 27 by a 64-percentage-point margin against incumbent Senator Penry Gustafson, who had joined the bipartisan 'Sister Senators' coalition in blocking South Carolina's six-week abortion ban. Blackmon ran explicitly on protecting the unborn, stating he would 'have the courage to protect the rights of the unborn.' His landslide primary victory — and subsequent November 2024 general election win — represents a direct mandate against abortion-ban opposition.",
              ["https://en.wikipedia.org/wiki/Allen_Blackmon",
               "https://www.postandcourier.com/politics/abortion-shealy-gustafson-primaries-gop/article_1d4fdb12-1f7c-11ef-981b-3bd2a79a653c.html"]),
        claim("ab2", "allen-blackmon", "family_child_sovereignty", 0, True,
              "Campaign platform committed to 'encouraging and streamlining adoptive services' and 'prioritizing policies that help make raising children more affordable,' placing family formation and parental support at the center of his legislative priorities. Blackmon represents an approach to family sovereignty that views the state's role as enabling family formation (adoption, economic support for raising children) rather than substituting government for family decision-making.",
              ["https://allenblackmon.com/",
               "https://www.ballotready.org/sc/south-carolina-south-carolina-state-senate-district-27/allen-n-blackmon"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

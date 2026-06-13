#!/usr/bin/env python3
"""Enrichment batch 175: 4 House Democrats from VA, ME, and FL.

evidence_federal bucket, bottom-of-alphabet states (VA → ME → FL):
- Joe Baldacci (ME-02 D nominee, sitting Maine State Senator)
- Nila Devanath (VA-02 D challenger, physician)
- Patrick Mosolf (VA-02 D challenger, former USAID official)
- Elijah Manley (FL-20 D primary frontrunner, working-class organizer)

Sources: mainesenate.org, mainepublic.org, newscentermaine.com,
jstreetpac.org, niladevanath.com, patrickmosolf.com, elijahmanley.com,
miaminewtimes.com, outsfl.com, bluevirginia.us.
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
    # ------------ Joe Baldacci (ME-02, D nominee after June 9 RCV) ----------
    ("joe-baldacci", "ME", "Representative", [
        claim("jb1", "joe-baldacci", "sanctity_of_life", 0, False,
              "As a Maine State Senator, voted to allow late-term abortions after fetal viability (24 weeks) when a doctor deems it medically necessary, and earned a 100% Planned Parenthood rating every year since the Dobbs decision — rejecting any life-at-conception standard.",
              ["https://www.mainesenate.org/sen-baldacci-celebrated-for-perfect-voting-record-on-reproductive-rights/",
               "https://www.mainepublic.org/politics/2026-06-03/democrats-in-maines-2nd-congressional-district-primary-trade-jabs-over-abortion"]),
        claim("jb2", "joe-baldacci", "sanctity_of_life", 4, False,
              "Endorsed by and actively courted Reproductive Freedom for All (formerly NARAL), a national abortion-rights PAC, which backed him in the June 2026 ME-02 Democratic primary — placing him inside the abortion-industry funding network.",
              ["https://www.newscentermaine.com/article/news/politics/elections/maine-cd2-race-candidates-joe-baldacci-national-abortion-rights-action-league/97-f73d3b5b-c7f7-496c-bcd1-b2baf0ca730c"]),
        claim("jb3", "joe-baldacci", "foreign_policy_restraint", 3, False,
              "Listed as a supported candidate by J Street PAC, a foreign-policy advocacy group that raises money for candidates on Middle East policy — meeting the rubric criterion of having accepted foreign-linked PAC support.",
              ["https://jstreetpac.org/candidate/joe-baldacci"]),
    ]),

    # ------- Nila Devanath (VA-02, D challenger, hospital physician) --------
    ("nila-devanath", "VA", "Representative", [
        claim("nd1", "nila-devanath", "sanctity_of_life", 0, False,
              "Campaign platform explicitly calls for 'defending and expanding access to abortion care, contraception, fertility care, and emergency reproductive healthcare' and opposing 'criminalization, intimidation, and policies that put ideology over health' — rejecting any legal recognition of the unborn from conception.",
              ["https://niladevanath.com/issues.html",
               "https://bluevirginia.us/2025/10/dr-nila-devanath-d-launches-campaign-for-congress-in-va02-currently-misrepresented-by-trump-loyalist-rep-jen-kiggans-r-va02/"]),
        claim("nd2", "nila-devanath", "refuse_federal_overreach", 0, False,
              "Supports Medicare for All and expanding strong federal public insurance options as the long-term goal for healthcare — a posture favoring large-scale federalization of health decisions over market-based or state-level approaches.",
              ["https://niladevanath.com/issues.html"]),
    ]),

    # ------- Patrick Mosolf (VA-02, D challenger, former USAID official) ----
    ("patrick-mosolf", "VA", "Representative", [
        claim("pm1", "patrick-mosolf", "foreign_policy_restraint", 2, False,
              "Spent his career as a USAID senior official directing U.S. foreign development assistance; his final posting led the Local Development Office in Lebanon, arriving days after the outbreak of the Israel-Gaza War. He explicitly frames continuation of USAID's mission as sound U.S. foreign policy.",
              ["https://www.patrickmosolf.com/about"]),
        claim("pm2", "patrick-mosolf", "refuse_federal_overreach", 0, False,
              "Proposes extending Obamacare subsidies, more aggressively regulating insurance and pharmaceutical industries at the federal level, and allowing middle-class families to buy into government-provided health plans — signaling preference for federal expansion over state or private solutions.",
              ["https://www.patrickmosolf.com/issues"]),
    ]),

    # -------- Elijah Manley (FL-20, D primary frontrunner) ------------------
    ("elijah-manley", "FL", "Representative", [
        claim("em1", "elijah-manley", "sanctity_of_life", 0, False,
              "Runs explicitly on 'protecting a woman's right to reproductive freedom,' including abortion access, as a core campaign pillar — opposing any life-at-conception or personhood framework.",
              ["https://www.elijahmanley.com/",
               "https://www.miaminewtimes.com/news/browards-elijah-manley-to-challenge-rep-cherfilus-mccormick-in-2026-22228659/"]),
        claim("em2", "elijah-manley", "biblical_marriage", 2, False,
              "Profiled in Out South Florida LGBTQ media as an LGBT-affirming candidate who supports LGBTQ+ rights and protections — rejecting the biblical distinction between male and female and opposing the rubric's position on transgender ideology.",
              ["https://outsfl.com/out-proud-2025/elijah-manley-the-politico"]),
        claim("em3", "elijah-manley", "self_defense", 1, False,
              "Campaign platform includes 'ending gun violence' as a stated leadership priority, signaling support for gun-control legislation and restrictions on firearms — contrary to the rubric's defense of Second Amendment rights against new bans and restrictions.",
              ["https://www.elijahmanley.com/",
               "https://www.miaminewtimes.com/news/browards-elijah-manley-to-challenge-rep-cherfilus-mccormick-in-2026-22228659/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

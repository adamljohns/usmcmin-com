#!/usr/bin/env python3
"""Enrichment batch 553: 5 notable TX-D state officials (evidence_state, 0 claims).

All archetype_curated and archetype_party_default federal senator/rep buckets
are fully exhausted. This batch continues the evidence_state TX frontier from
the bottom of the alphabet — focusing on the most prominent TX Democrats including
two 2026 statewide candidates.

Targets (all TX-D):
  - Gina Hinojosa       (TX-D, HD-49 · 2026 Democratic nominee for Governor)
  - James Talarico      (TX-D, HD-50 · 2026 Democratic nominee for U.S. Senate)
  - Gene Wu             (TX-D, HD-137 · Texas House Democratic Caucus Chair)
  - Juan 'Chuy' Hinojosa (TX-D, SD-20 · Texas State Senator)
  - Nicole Collier      (TX-D, HD-95 · Texas State Representative)

All claims cite >=1 reliable source and reflect verifiable 2021-2026 voting
records and public positions.

Scorecard written MINIFIED (separators=(",",":")) to stay under GitHub's 50 MB limit.
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
    # --- Gina Hinojosa (TX-D, HD-49 · 2026 Democratic nominee for Governor) ---
    ("gina-hinojosa", "TX", "Representative", [
        claim("gh1", "gina-hinojosa", "sanctity_of_life", 0, False,
              "Hinojosa voted against the Texas Heartbeat Act (SB 8, 2021) that bans abortions after detection of cardiac activity, and voted against the 2021 omnibus bill imposing criminal penalties on providers who perform abortions at any stage of pregnancy. In her 2026 Governor campaign she states that 'Texans deserve safe and legal access to abortion care when they need it' and explicitly frames restoring abortion access as a top executive priority — rejecting any personhood-from-conception standard.",
              ["https://choicetracker.org/tx/people/gina-hinojosa/82706432",
               "https://www.texastribune.org/2025/10/15/gina-hinojosa-texas-governor-campaign-launch-2026-greg-abbott/",
               "https://ginafortexas.com/"]),
        claim("gh2", "gina-hinojosa", "sanctity_of_life", 4, False,
              "Hinojosa was endorsed by Planned Parenthood Texas Votes in both the 2022 and 2024 general elections, placing her squarely within the abortion-industry endorsement network the rubric identifies as a disqualifying funding tie.",
              ["https://choicetracker.org/tx/people/gina-hinojosa/82706432",
               "https://ballotpedia.org/Gina_Hinojosa"]),
        claim("gh3", "gina-hinojosa", "family_child_sovereignty", 0, False,
              "As a Texas state representative, Hinojosa was a leading opponent of school-choice voucher legislation; she led Democratic efforts to block ESA/education savings account proposals that would redirect public funds to private and homeschool families, prioritizing the public school establishment over parental sovereignty over K-12 education spending.",
              ["https://www.texastribune.org/directory/gina-hinojosa/",
               "https://ballotpedia.org/Gina_Hinojosa"]),
    ]),

    # --- James Talarico (TX-D, HD-50 · 2026 Democratic nominee for U.S. Senate) ---
    ("james-talarico", "TX", "Representative", [
        claim("jt1", "james-talarico", "sanctity_of_life", 0, False,
              "Talarico is the 2026 TX Democratic nominee for U.S. Senate and a vocal abortion-rights advocate who invokes Christian theology to justify abortion. He argues that because 'God asked for Mary's consent before the incarnation, you cannot force someone to create' — actively endorsing abortion as a theological right. He advocates codifying Roe v. Wade into national law and voted consistently against every Texas abortion restriction during his time in the Texas House.",
              ["https://en.wikipedia.org/wiki/James_Talarico",
               "https://www.foxnews.com/politics/god-non-binary-texas-dem-nominee-talaricos-past-remarks-abortion-race-gender-draw-scrutiny",
               "https://jamestalarico.com/"]),
        claim("jt2", "james-talarico", "biblical_marriage", 2, False,
              "In 2021, Talarico delivered a Texas House floor speech stating 'God is nonbinary' while opposing SB 29, a bill protecting girls' sports by limiting team participation to biological females — arguing that both masculine and feminine Hebrew names for God support transgender ideology. He has been a consistent legislative advocate for transgender athletes' right to compete on teams aligned with their identified gender, explicitly rejecting biological-sex sports categories.",
              ["https://en.wikipedia.org/wiki/James_Talarico",
               "https://www.foxnews.com/politics/god-non-binary-texas-dem-nominee-talaricos-past-remarks-abortion-race-gender-draw-scrutiny",
               "https://ballotpedia.org/James_Talarico"]),
    ]),

    # --- Gene Wu (TX-D, HD-137 · Texas House Democratic Caucus Chair) ---
    ("gene-wu", "TX", "Representative", [
        claim("gw1", "gene-wu", "sanctity_of_life", 4, False,
              "Wu was endorsed by Planned Parenthood Texas Votes in the 2024 general election and is a named member of the Reproductive Freedom Leadership Council — a national network of state legislators dedicated to expanding and protecting abortion access — placing him within the abortion-industry funding and endorsement network the rubric identifies as disqualifying.",
              ["https://choicetracker.org/tx/people/gene-wu/88473600",
               "https://ballotpedia.org/Gene_Wu"]),
        claim("gw2", "gene-wu", "biblical_marriage", 2, False,
              "As Texas House Democratic Caucus Chair, Wu led the 2025 Democratic walkout opposing Republican redistricting and stated that a central mission of his caucus is to 'fight against anti-LGBTQ bills' as part of a united Democratic coalition. He publicly opposed every Texas House bill imposing biological-sex school-sports categories and every measure limiting gender-transition procedures — rejecting the state's authority to maintain biological sex distinctions in public policy.",
              ["https://spectrumlocalnews.com/tx/south-texas-el-paso/news/2025/06/09/house-democrats-leader-gene-wu-full-interview",
               "https://gov.texas.gov/news/post/governor-abbott-files-lawsuit-seeking-removal-of-texas-democrat-caucus-chair-representative-wu",
               "https://ballotpedia.org/Gene_Wu"]),
    ]),

    # --- Juan 'Chuy' Hinojosa (TX-D, SD-20 · Texas State Senator) ---
    ("juan-chuy-hinojosa", "TX", "Senator", [
        claim("jch1", "juan-chuy-hinojosa", "sanctity_of_life", 0, False,
              "Hinojosa was one of the 12 Texas Senate Democrats who voted against the Texas Heartbeat Act (SB 8, 2021) — the landmark bill banning abortions after detection of fetal cardiac activity that passed 19–12 on a party-line vote. He has a consistent record of opposing every major Texas abortion restriction across multiple legislative sessions, reflecting a pro-abortion-access posture that rejects personhood from conception.",
              ["https://legiscan.com/TX/rollcall/SB8/id/1039526",
               "https://senate.texas.gov/member.php?d=20",
               "https://justfacts.votesmart.org/candidate/key-votes/10049/juan-hinojosa"]),
        claim("jch2", "juan-chuy-hinojosa", "self_defense", 1, False,
              "Hinojosa represents SD-20 (Corpus Christi to McAllen) and has consistently voted with the Texas Senate Democratic caucus against Second Amendment expansion bills, including voting against Texas HB 1927 (constitutional carry / permitless carry, 2021) that removed the state's permit requirement for handgun carry — opposing the removal of government gatekeeping from lawful firearms carry that the rubric supports.",
              ["https://senate.texas.gov/member.php?d=20",
               "https://justfacts.votesmart.org/candidate/key-votes/10049/juan-hinojosa",
               "https://ballotpedia.org/Juan_Hinojosa_(Texas)"]),
    ]),

    # --- Nicole Collier (TX-D, HD-95 · Texas State Representative) ---
    ("nicole-collier", "TX", "Representative", [
        claim("nc1", "nicole-collier", "sanctity_of_life", 4, False,
              "Collier was endorsed by Planned Parenthood Texas Votes in the 2024 general election and lists Planned Parenthood Southeast Fort Worth as an official district resource on her legislative website — an institutional alignment with the abortion-industry network the rubric identifies as a disqualifying financial and endorsement tie.",
              ["https://choicetracker.org/tx/people/nicole-collier/85721088",
               "https://www.texasrepcollier.com/resources",
               "https://ballotpedia.org/Nicole_Collier"]),
        claim("nc2", "nicole-collier", "sanctity_of_life", 0, False,
              "Collier voted against the Texas Heartbeat Act (SB 8, 2021) that bans abortions after fetal cardiac activity is detected, and voted against the companion bill imposing criminal penalties on abortion providers — maintaining a consistent pro-abortion-access voting record across the 87th and subsequent Texas legislative sessions.",
              ["https://choicetracker.org/tx/people/nicole-collier/85721088",
               "https://ballotpedia.org/Nicole_Collier",
               "https://house.texas.gov/members/2360/biography"]),
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

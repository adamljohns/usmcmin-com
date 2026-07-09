#!/usr/bin/env python3
"""Enrichment batch 602: 5 state R executives — 12 claims.

All archetype_curated federal senator/rep buckets remain depleted.
Continues bottom-of-alphabet evidence_state enrichment pivot, targeting
statewide R officials with 0 claims in the KY/ID/IA/IN/MO/LA range.

Targets:
  Dave Wasinger     (MO) — Lieutenant Governor (since Jan 2025)
  Nancy Landry      (LA) — Secretary of State (since Jan 2024)
  Russell Coleman   (KY) — Attorney General (since Jan 2024)
  Micah Beckwith    (IN) — Lieutenant Governor (since Jan 2025)
  Raul Labrador     (ID) — Attorney General (since Jan 2023)
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
    # ---------- Dave Wasinger (MO, Lt. Governor, since Jan 2025) ----------
    ("dave-wasinger", "MO", "Lt. Governor", [
        claim("dw1", "dave-wasinger", "sanctity_of_life", 0, True,
              "Received the exclusive 2024 primary endorsement of Missouri Right to Life PAC and declared 'valuing life from conception to natural death is a core principle of my campaign.' After winning the general election, pledged to be a 'pro-life warrior' who would use 'every tool and arsenal' available as Lt. Governor to oppose abortion access.",
              ["https://missourilifepac.org/wp-content/uploads/2024/03/Press-Release-MRL-State-PAC-Issues-Exclusive-Endorsement-of-Wasinger-for-MO-Lt.-Gov.-in-2024-Primary-3-19-24.pdf",
               "https://missouriindependent.com/2024/11/05/david-wasinger-elected-missouri-lieutenant-governor/"]),
        claim("dw2", "dave-wasinger", "self_defense", 1, True,
              "A self-described MAGA conservative affiliated with the NRA who opposes new restrictions on firearms, running on a platform of pushing back against federal government overreach — including on gun-control mandates — and defending constitutional liberties.",
              ["https://ballotpedia.org/David_Wasinger",
               "https://missouriindependent.com/2024/11/05/david-wasinger-elected-missouri-lieutenant-governor/"]),
    ]),

    # ---------- Nancy Landry (LA, Secretary of State, since Jan 2024) ----------
    ("nancy-landry", "LA", "Secretary of State", [
        claim("nl1", "nancy-landry", "election_integrity", 0, True,
              "Released a 2024 election-integrity legislative package that included SB 101 banning ranked-choice voting in Louisiana elections and HB 506 requiring groups conducting voter-registration drives to register with the Secretary of State — both enacted. Also set a goal of replacing Louisiana's voting machines with a system including a paper-ballot component.",
              ["https://www.sos.la.gov/OurOffice/PublishedDocuments/030624LegislativePackagePressRelease_final.pdf",
               "https://www.sos.la.gov/OurOffice/PublishedDocuments/2024Post%20Session%20Press%20Release.pdf"]),
        claim("nl2", "nancy-landry", "election_integrity", 0, True,
              "Made Louisiana the first state to integrate the Trump administration's DOGE voter-list database for voter-roll maintenance (May 2026), calling it a 'cost-free' tool to remove ineligible registrants after the previous administration had blocked such outreach.",
              ["https://www.sos.la.gov/OurOffice/PublishedDocuments/5.21.26%20PR%20DOGE.pdf",
               "https://ballotpedia.org/Nancy_Landry"]),
    ]),

    # ---------- Russell Coleman (KY, Attorney General, since Jan 2024) ----------
    ("russell-coleman", "KY", "Attorney General", [
        claim("rc1", "russell-coleman", "sanctity_of_life", 0, True,
              "As Kentucky AG, enforces the Human Life Protection Act (near-total abortion ban operative since the Dobbs decision) and in 2024 joined a 23-attorney-general coalition filing a brief with the U.S. Supreme Court urging it to stop mail-order abortion pills, calling it 'the next frontier' in protecting unborn life. Describes himself as a 'pro-life, pro-family conservative.'",
              ["https://www.kentuckytoday.com/news/kentucky-ag-joins-coalition-urging-supreme-court-to-stop-mail-order-abortion-pills/article_90022ca9-a4eb-423f-9fc6-d4d4aeaf83b0.html",
               "https://www.ag.ky.gov/Priorities/Protecting-Life/Pages/default.aspx"]),
        claim("rc2", "russell-coleman", "self_defense", 1, True,
              "A lifetime NRA member who grew up carrying firearms; as AG-elect stated that before adding new gun statutes 'we need to start enforcing the statutes that have been on the books for years,' opposing new firearm restrictions such as assault-weapons bans, registries, or expanded background-check mandates.",
              ["https://www.kentuckytoday.com/news/new-kentucky-ag-talks-oldham-county-roots-crime-2a-abortion-transparency/article_3653e172-a1b8-11ee-8393-df9e453b6a81.html",
               "https://ballotpedia.org/Russell_Coleman"]),
    ]),

    # ---------- Micah Beckwith (IN, Lieutenant Governor, since Jan 2025) ----------
    ("micah-beckwith", "IN", "Lieutenant Governor", [
        claim("mb1", "micah-beckwith", "sanctity_of_life", 0, True,
              "A pastor and Executive Director of the Indiana Family Action PAC who during the 2024 campaign called pro-choice Hoosiers 'demonic' and labeled abortion-rights advocacy the 'Jezebel spirit.' Has consistently defended Indiana's near-total abortion ban and frames the sanctity of every unborn life as a foundational biblical conviction.",
              ["https://en.wikipedia.org/wiki/Micah_Beckwith",
               "https://ballotpedia.org/Micah_Beckwith"]),
        claim("mb2", "micah-beckwith", "christian_liberty", 0, True,
              "When Indiana employers and universities mandated COVID-19 vaccines, Beckwith personally wrote approximately 1,400 religious-exemption letters to ensure Hoosiers could keep their jobs and education without being compelled to take the vaccine against their sincere religious beliefs — a direct exercise of First Amendment religious free-exercise protection.",
              ["https://en.wikipedia.org/wiki/Micah_Beckwith",
               "https://www.in.gov/lg/biography/"]),
        claim("mb3", "micah-beckwith", "family_child_sovereignty", 0, True,
              "Led a successful effort on an Indiana public-library board to remove sexually explicit and age-inappropriate materials — including LGBTQ-themed titles — from the young-adult section, resulting in nearly 2,000 titles being relocated, affirming parental authority over children's access to library content.",
              ["https://en.wikipedia.org/wiki/Micah_Beckwith",
               "https://ballotpedia.org/Micah_Beckwith"]),
    ]),

    # ---------- Raul Labrador (ID, Attorney General, since Jan 2023) ----------
    ("raul-labrador", "ID", "Attorney General", [
        claim("rl1", "raul-labrador", "sanctity_of_life", 0, True,
              "Aggressively defended Idaho's Defense of Life Act (near-total abortion ban from fertilization) in federal court, successfully moved to dismiss an EMTALA-based challenge, and won at the Ninth Circuit defending Idaho's abortion-trafficking law — which bars adults from transporting minors across state lines for abortions without parental knowledge.",
              ["https://www.ag.idaho.gov/newsroom/ag-labrador-announces-dismissal-of-emtala-challenge-to-idaho-defense-of-life-act/",
               "https://www.ag.idaho.gov/newsroom/attorney-general-labrador-successfully-defends-idahos-abortion-trafficking-laws-at-ninth-circuit/"]),
        claim("rl2", "raul-labrador", "self_defense", 1, True,
              "Led a 29-state coalition filing an amicus brief against Maryland's assault-weapons ban (AR-15 and similar firearms), led a 27-state coalition challenging California's Assault Weapons Control Act, co-led a 27-state coalition opposing Washington state's 10-round magazine limit, and joined Kansas AG Kris Kobach in suing to block an ATF rule restricting private firearm sales — a consistent pattern of opposing federal and state gun-control restrictions.",
              ["https://www.ag.idaho.gov/newsroom/attorney-general-labrador-leads-29-state-coalition-against-marylands-bizarrely-unconstitutional-gun-ban/",
               "https://www.ag.idaho.gov/newsroom/attorney-general-labrador-leads-nationwide-fight-against-californias-unconstitutional-assault-weapons-ban/",
               "https://www.ag.idaho.gov/newsroom/idaho-joins-multi-state-coalition-in-defense-of-second-amendment/"]),
        claim("rl3", "raul-labrador", "border_immigration", 2, True,
              "As AG, partnered with Texas in defending its sovereign right to secure its own border, joined coalitions opposing the Biden administration's unlawful immigration policies, and filed briefs defending the Trump administration's authority to enforce federal immigration law against sanctuary-city policies — opposing any safe-harbor for illegal immigration.",
              ["https://www.ag.idaho.gov/newsroom/labrador-letter-how-idaho-is-fighting-for-constitutional-rights-nationwide/",
               "https://en.wikipedia.org/wiki/Ra%C3%BAl_Labrador"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

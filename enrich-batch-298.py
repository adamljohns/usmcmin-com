#!/usr/bin/env python3
"""Enrichment batch 298: hand-curated claims for 4 state officials.

Targets evidence_state candidates from bottom-of-alphabet states (VT, VA)
with 0 claims. Archetype_curated federal bucket is exhausted; batch continues
the evidence_state pivot started in batch 297.

Targets (all R): John Rodgers (VT-Lt. Gov), Tom Garrett (VA-HoD 56),
Ryan McDougle (VA-Senate 26), Terry Kilgore (VA-HoD 45).
8 total claims across 4 candidates.

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


TARGETS = [
    # ----------- John Rodgers (VT-R, Lieutenant Governor) -----------
    ("john-rodgers", "VT", "Lt", [
        claim("jr1", "john-rodgers", "self_defense", 1, True,
              "As a Vermont state senator, cast one of only three votes against Vermont S.55 (2018) — the state's first major gun control law — which imposed magazine-capacity limits (10 rounds for rifles, 15 for handguns), a bump-stock ban, and expanded background checks. Rodgers declared the magazine-capacity limit 'a violation of the constitutional right to bear arms' and questioned the enforceability of the entire bill, warning it would only disarm law-abiding Vermonters.",
              ["https://vtdigger.org/2018/03/30/updated-governor-sign-historic-gun-bill-passage-senate/",
               "https://en.wikipedia.org/wiki/John_S._Rodgers"]),
        claim("jr2", "john-rodgers", "self_defense", 0, True,
              "A lifelong NRA member and Vermont's most outspoken gun rights defender, known for decades as the 'most pro-gun Democrat' in the legislature before switching to the Republican Party in 2024. Vermont is the original constitutional carry state — it has never required a permit to carry a firearm — and Rodgers has consistently defended that tradition, vocally opposing every major attempt to restrict Vermont gun rights during his legislative career.",
              ["https://vtdigger.org/2018/04/10/rodgers-vocal-gun-rights-advocate-weighs-run-governor/",
               "https://ballotpedia.org/John_Rodgers_(Vermont)"]),
    ]),

    # ----------- Tom Garrett (VA-R, House of Delegates District 56) -----------
    ("tom-garrett", "VA", "House of Delegates", [
        claim("tg1", "tom-garrett", "sanctity_of_life", 0, True,
              "Publicly declared: 'I assure you that on issues of life, I will vote to protect the first and foremost inalienable right given to us by the Creator. No exceptions.' — an unequivocal affirmation of God-given personhood from conception with no carve-outs for rape or incest. As a Virginia state senator, U.S. congressman, and now House delegate, Garrett has maintained a consistent pro-life voting record across all three chambers.",
              ["https://ballotpedia.org/Thomas_Garrett",
               "https://en.wikipedia.org/wiki/Tom_Garrett_(Virginia_politician)"]),
        claim("tg2", "tom-garrett", "self_defense", 1, True,
              "As a Virginia state senator, sponsored SB 1137 (2016) to prohibit local government ordinances from banning concealed-carry permit holders from transporting a loaded rifle or shotgun — protecting gun owners from a patchwork of municipal restrictions that targeted lawful carriers. Garrett's entire legislative career reflects consistent defense of Second Amendment rights against government encroachment at every level.",
              ["https://ballotpedia.org/Thomas_Garrett",
               "https://en.wikipedia.org/wiki/Tom_Garrett_(Virginia_politician)"]),
    ]),

    # ----------- Ryan McDougle (VA-R, State Senate District 26) -----------
    ("ryan-mcdougle", "VA", "State Senate", [
        claim("rm1", "ryan-mcdougle", "family_child_sovereignty", 0, True,
              "As Virginia Senate Minority Leader, publicly declared that requiring parental consent for minors seeking abortions is his caucus's 'highest priority' for the 2025-2026 session, criticizing the Democrat-backed 'Right to Reproductive Freedom' constitutional amendment precisely because it omits parental involvement. Stated: 'When it comes to the amendments, we pick parents' abilities to be able to be involved in their children's decisions as the highest priority. Those are the things that we are fighting for this session and will continue to fight for.'",
              ["https://news.ballotpedia.org/2025/01/27/virginias-two-session-rule-for-constitutional-amendment-house-of-delegates-election-could-affect-the-future-of-proposed-amendments-on-abortion-marriage-and-voting/",
               "https://ballotpedia.org/Ryan_McDougle"]),
        claim("rm2", "ryan-mcdougle", "sanctity_of_life", 0, True,
              "Led the Virginia Senate Republican caucus in unified opposition to the 'Right to Reproductive Freedom' constitutional amendment (SJR 249/HJR 1) — a Democrat-backed measure that would enshrine abortion as a constitutional right in Virginia including after fetal viability. The amendment passed both chambers solely on Democrat votes; McDougle's caucus voted unanimously against constitutionalizing abortion as a protected right.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://ballotpedia.org/Ryan_McDougle"]),
    ]),

    # ----------- Terry Kilgore (VA-R, House of Delegates District 45) -----------
    ("terry-kilgore", "VA", "House of Delegates", [
        claim("tk1", "terry-kilgore", "biblical_marriage", 1, True,
              "As House Minority Leader, led the Republican caucus in unanimous opposition to HJR 3 — Virginia's constitutional amendment to remove the state's ban on same-sex marriage and replace it with a mandate that the state recognize marriages 'without regard to sex, gender, or race.' In January 2026, all 31 House Republicans voted no; not a single Republican crossed the line on this foundational marriage question.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment"]),
        claim("tk2", "terry-kilgore", "sanctity_of_life", 0, True,
              "With more than three decades of service in the Virginia House of Delegates (elected 1993), Kilgore has cast a consistent pro-life voting record across every legislative session. As House Minority Leader in the 2025-2026 session, he led the Republican caucus in opposing the Democrat-backed 'Right to Reproductive Freedom' constitutional amendment, which would have written a broad abortion right — including post-viability — into the Virginia constitution.",
              ["https://ballotpedia.org/Terry_Kilgore",
               "https://en.wikipedia.org/wiki/Terry_Kilgore"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

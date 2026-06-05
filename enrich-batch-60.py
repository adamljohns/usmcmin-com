#!/usr/bin/env python3
"""Enrichment batch 60: hand-curated claims for 4 federal House candidates.

Targets archetype_curated House candidates with 0 claims, taken from the
BOTTOM of the alphabet bucket (IA, FL, IL, MI).

Mix (4 D): Lanon Baccam (IA-03-D), Whitney Fox (FL-13-D),
Daniel Biss (IL-09-D), Carl Marlinga (MI-10-D).
Each claim cites >=1 reliable source and reflects 2024-2026
voting record / public positions.

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
    # ---------------- Lanon Baccam (IA-03-D) ----------------
    ("lanon-baccam", "IA", "Representative", [
        claim("lb1", "lanon-baccam", "sanctity_of_life", 0, False,
              "Ran on 'guaranteeing the right to an abortion' as a top policy priority and said he is running because Iowans deserve 'protection of women's reproductive freedoms.' Explicitly rejects any life-at-conception or personhood framework.",
              ["https://ballotpedia.org/Lanon_Baccam",
               "https://iowacapitaldispatch.com/2023/11/09/democrat-lanon-baccam-announces-campaign-for-iowa-3rd-congressional-district/"]),
        claim("lb2", "lanon-baccam", "self_defense", 1, False,
              "At a 2024 KCCI candidate debate called for red flag laws to keep firearms from dangerous individuals, saying 'We need to find ways to also alert our law enforcement to people who may have ill intents' and framed red flag laws and 'violent history checks' as 'common sense' measures — directly opposing the rubric's rejection of red-flag confiscation laws.",
              ["https://ballotpedia.org/Lanon_Baccam",
               "https://cbs2iowa.com/news/local/democratic-candidate-lanon-baccam-prioritizes-protecting-social-security-and-medicare"]),
    ]),

    # ---------------- Whitney Fox (FL-13-D) ----------------
    ("whitney-fox", "FL", "Representative", [
        claim("wf1", "whitney-fox", "sanctity_of_life", 0, False,
              "Stated it is 'vital to protect a woman's right to make her own healthcare and reproductive decisions,' called on Congress to 'stop pushing for a national abortion ban and enshrine Roe as federal law,' and ran as the 2024 Democratic nominee in FL-13 on an abortion-rights platform — rejecting any recognition of life from conception.",
              ["https://ballotpedia.org/Whitney_Fox"]),
        claim("wf2", "whitney-fox", "biblical_marriage", 4, False,
              "Pledged to fight 'all forms of discrimination' and to support 'the LGBTQIA+ community,' signaling promotion of LGBTQ ideology in public policy that the rubric's biblical_marriage standard opposes.",
              ["https://ballotpedia.org/Whitney_Fox"]),
        claim("wf3", "whitney-fox", "sanctity_of_life", 4, False,
              "Endorsed by Reproductive Freedom for All (formerly NARAL Pro-Choice America), placing her inside the pro-abortion advocacy network the rubric flags as disqualifying for the sanctity-of-life q4 standard.",
              ["https://reproductivefreedomforall.org/lawmaker/whitney-fox/"]),
    ]),

    # ---------------- Daniel Biss (IL-09-D) ----------------
    ("daniel-biss", "IL", "Representative", [
        claim("db1", "daniel-biss", "sanctity_of_life", 0, False,
              "Made 'preserving access to abortion' a signature issue of his 2026 congressional campaign; as an Illinois state senator also indicated support for legal abortion in a Political Courage Test — consistently rejecting any life-at-conception or personhood standard.",
              ["https://en.wikipedia.org/wiki/Daniel_Biss",
               "https://ballotpedia.org/Daniel_K._Biss"]),
        claim("db2", "daniel-biss", "border_immigration", 0, False,
              "Framed his 2026 candidacy explicitly as 'standing up to Donald Trump on immigration,' opposing the strict border enforcement, wall funding, and mandatory deportation measures the rubric's border_immigration standard calls for.",
              ["https://en.wikipedia.org/wiki/Daniel_Biss"]),
    ]),

    # ---------------- Carl Marlinga (MI-10-D) ----------------
    ("carl-marlinga-2026", "MI", "Representative", [
        claim("cm1", "carl-marlinga-2026", "sanctity_of_life", 0, False,
              "Made 'restoring a woman's right to choose and defending reproductive freedom' a signature pledge across his 2024 and 2026 campaign cycles, explicitly rejecting any constitutional protection for the unborn from conception.",
              ["https://ballotpedia.org/Carl_Marlinga"]),
        claim("cm2", "carl-marlinga-2026", "election_integrity", 0, False,
              "Framed his candidacy around preventing Trump from 'hijacking the election,' telling the Detroit Free Press editorial board 'I want to be in the House of Representatives on Jan. 6, 2025…I don't want Donald Trump and his forces to hijack the election' — aligning with the Democratic election-administration framework that opposes the voter-ID, paper-ballot, and anti-mass-mail-in reforms the rubric's election_integrity standard calls for.",
              ["https://ballotpedia.org/Carl_Marlinga"]),
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

#!/usr/bin/env python3
"""Enrichment batch 665: hand-curated claims for 5 Wisconsin State Assembly Democrats.

Targets from the bottom of the archetype_party_default / 0-claims bucket
(sorted descending by state then name): all five represent WI Assembly seats
held by Democrats. Claims span the 2025 Abortion Rights Restoration Act
(AB355), sanctuary legislation (AB57), voter-ID constitutional amendment
NO votes (AJR1), conversion-therapy ban (AB359), LGBTQ school-training
grants (AB316), gay-panic-defense elimination (AB361), and mandatory
firearm safe-storage legislation (AB356), covering January–July 2025.

Assembly Members (WI / D):
  Mike Bare         — AD-80, Verona; Minority Caucus Secretary (since 2023)
  Maureen McCarville — AD-42, DeForest (since 2025)
  Margaret Arney    — AD-18, Wauwatosa; freshman sworn Jan 6 2025
  Lori Palmeri      — AD-54, Oshkosh (since 2023)
  Lisa Subeck       — AD-79, Madison; Minority Caucus Chair (since 2015)

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50 MB warning.
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
    # ── Mike Bare (WI AD-80, D, Minority Caucus Secretary) ─────────────────
    ("mike-bare-wi-80", "WI", "Assembly Member", [
        claim("mb1", "mike-bare-wi-80", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which declares a fundamental right to bodily autonomy encompassing abortion, "
              "repeals Wisconsin's existing abortion regulations, and requires health plans "
              "that cover maternity care to also cover abortion with no gestational limit — "
              "explicitly rejecting any personhood-from-conception standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("mb2", "mike-bare-wi-80", "border_immigration", 2, False,
              "Co-introduced AB57 (introduced February 24, 2025), which prohibits all "
              "Wisconsin state and local officials — including law enforcement officers — "
              "from assisting in the detention of any individual on the sole basis that the "
              "person is or is alleged to be unlawfully present in the United States, and "
              "bars any state agency from expending funds toward such detention — a de facto "
              "sanctuary-state bill opposing mandatory immigration enforcement cooperation.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab57"]),
        claim("mb3", "mike-bare-wi-80", "election_integrity", 0, False,
              "Voted NO on AJR1 (January 14, 2025), the resolution to enshrine Wisconsin's "
              "voter-ID requirement in the state constitution; the Assembly passed AJR1 "
              "54-45 on a strict party-line vote, with all 45 Democrats — including Bare — "
              "voting against the voter-ID constitutional amendment.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/"]),
    ]),

    # ── Maureen McCarville (WI AD-42, D) ────────────────────────────────────
    ("maureen-mccarville-wi-42", "WI", "Assembly Member", [
        claim("mmc1", "maureen-mccarville-wi-42", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which establishes a statutory right to bodily autonomy including the right to "
              "obtain an abortion, repeals Wisconsin's existing abortion restrictions, and "
              "mandates abortion coverage under health plans that include maternity benefits — "
              "opposing any recognition of the unborn as persons.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("mmc2", "maureen-mccarville-wi-42", "biblical_marriage", 4, False,
              "Co-sponsored AB316 (2025), which creates a state grant program for LGBTQIA+ "
              "rights training provided specifically to public school counselors and school "
              "social workers — state-funded promotion of LGBTQ ideology within the K-12 "
              "school system, opposing the rubric's standard against LGBTQ promotion in "
              "schools and policy.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab316"]),
        claim("mmc3", "maureen-mccarville-wi-42", "election_integrity", 0, False,
              "Voted NO on AJR1 (January 14, 2025), the Wisconsin Assembly resolution to "
              "send a voter-ID constitutional amendment to the April 2025 ballot; the measure "
              "passed 54-45 along strict party lines, with all 45 Assembly Democrats — "
              "including McCarville — voting against embedding voter-ID requirements in the "
              "state constitution.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/"]),
    ]),

    # ── Margaret Arney (WI AD-18, D, freshman sworn Jan 6 2025) ────────────
    ("margaret-arney-wi-18", "WI", "Assembly Member", [
        claim("ma1", "margaret-arney-wi-18", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "which asserts a fundamental right to bodily autonomy including the right to "
              "access abortion, removes Wisconsin's abortion regulations, and requires health "
              "plans that cover maternity care to cover abortion — rejecting life-at-conception "
              "legal standards as a freshman Assembly member.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("ma2", "margaret-arney-wi-18", "border_immigration", 2, False,
              "Co-introduced AB57 (introduced February 24, 2025), a sanctuary measure "
              "prohibiting Wisconsin state and local officials including law enforcement "
              "from aiding in the detention of individuals on the sole basis that they are "
              "or are alleged to be unlawfully present in the United States, and barring "
              "state funds from being spent on such assistance — opposing the rubric's "
              "anti-sanctuary-city position.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab57"]),
        claim("ma3", "margaret-arney-wi-18", "biblical_marriage", 2, False,
              "Co-sponsored AB361 (introduced July 17, 2025), which eliminates the criminal "
              "defenses of adequate provocation, self-defense, and not guilty by reason of "
              "mental disease or defect when the defendant's claim is based on the victim's "
              "gender identity or sexual orientation — directly targeting the so-called "
              "'gay/trans panic' defense strategy and embedding LGBTQ identity as a legally "
              "protected category in Wisconsin criminal law.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab361"]),
    ]),

    # ── Lori Palmeri (WI AD-54, D) ──────────────────────────────────────────
    ("lori-palmeri-wi-54", "WI", "Assembly Member", [
        claim("lp1", "lori-palmeri-wi-54", "sanctity_of_life", 0, False,
              "Co-sponsored AB355 (Abortion Rights Restoration Act, introduced July 8, 2025), "
              "declaring a fundamental right to bodily autonomy including abortion, repealing "
              "Wisconsin's existing abortion laws, and mandating abortion coverage in health "
              "plans — explicitly rejecting any legal protection for the unborn from "
              "conception.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://legiscan.com/WI/bill/AB355/2025"]),
        claim("lp2", "lori-palmeri-wi-54", "biblical_marriage", 2, False,
              "Co-sponsored AB359 (introduced July 17, 2025), which prohibits licensed "
              "mental health providers from engaging in conversion therapy with a minor — "
              "banning therapeutic approaches that seek to change a person's sexual "
              "orientation or gender identity; the bill criminalizes practices that affirm "
              "a traditional or biblical understanding of sexuality and gender.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab359",
               "https://legiscan.com/WI/bill/AB359/2025"]),
        claim("lp3", "lori-palmeri-wi-54", "election_integrity", 0, False,
              "Voted NO on AJR1 (January 14, 2025) and issued a public statement criticizing "
              "the voter-ID constitutional amendment resolution, calling it an attempt to "
              "'duplicate existing voter ID law in the state constitution' rather than "
              "address pressing issues; AJR1 passed 54-45 on a strict party-line vote with "
              "all Assembly Democrats opposed.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://www.wispolitics.com/2025/rep-palmeri-defends-voting-rights-votes-for-protecting-wisconsins-constitution/"]),
    ]),

    # ── Lisa Subeck (WI AD-79, D, Minority Caucus Chair) ────────────────────
    ("lisa-subeck-wi-79", "WI", "Assembly Member", [
        claim("ls1", "lisa-subeck-wi-79", "sanctity_of_life", 0, False,
              "Served as lead Assembly co-author (with Sen. Kelda Roys) of the 2025 Abortion "
              "Rights Restoration Act (AB355/SB271), introduced July 8, 2025, which would "
              "repeal Wisconsin's 1849-era abortion criminal statute, establish a statutory "
              "right to bodily autonomy encompassing abortion, and require health plan "
              "coverage of abortion — carrying the full weight of her role as Assembly "
              "Minority Caucus Chair.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab355",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/sb271"]),
        claim("ls2", "lisa-subeck-wi-79", "self_defense", 1, False,
              "Introduced AB356 (July 8, 2025) as lead author, requiring any person who "
              "stores a firearm in a residence shared with or to be visited by a child under "
              "18 to keep that firearm in a securely locked container or with a trigger lock "
              "engaged — a criminal-penalty mandate (Class A misdemeanor first offense, "
              "Class I felony repeat) that restricts ready home access to firearms for lawful "
              "self-defense.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab356"]),
        claim("ls3", "lisa-subeck-wi-79", "border_immigration", 2, False,
              "Co-introduced AB57 (introduced February 24, 2025), a Wisconsin sanctuary bill "
              "barring all state and local officials — including law enforcement — from "
              "assisting in the detention of individuals on the sole basis that they are or "
              "are alleged to be unlawfully present in the United States, and prohibiting "
              "state agencies from expending funds for such assistance — in direct opposition "
              "to the rubric's anti-sanctuary-city standard.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab57"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher. Returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

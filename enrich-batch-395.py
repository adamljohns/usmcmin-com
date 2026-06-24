#!/usr/bin/env python3
"""Enrichment batch 395: 2 additional claims each for 5 federal Senate candidates.

Targets evidence_curated senators with exactly 3 claims (bottom-of-alphabet order).
archetype_curated bucket was exhausted; these extend partially-enriched candidates
into new rubric categories.

Candidates: Royce White (MN-R), Mike Rogers (MI-R), Lee Calhoun (MT-R),
Don Brown (NC-R, lost primary), Jared Sullivan (NH-D).
Each gets 2 new claims in distinct rubric categories not yet covered.

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
    # ---------------- Royce White (MN-R, US Senator 2026 candidate) ----------------
    ("royce-white", "MN", "Senator", [
        claim("rw1", "royce-white", "biblical_marriage", 2, True,
              "Publicly brands LGBTQ advocacy as 'the church of LGBTQ,' declares the 'LGBTQ agenda' "
              "exercises a 'pervasive effect' on American society that he opposes, and has used "
              "anti-LGBTQ slurs publicly. His 2026 Senate platform runs under the banner "
              "'God, Family, and Country — not globalism,' directly opposing the promotion of "
              "transgender and LGBTQ ideology in public life and schools.",
              ["https://en.wikipedia.org/wiki/Royce_White",
               "https://theweek.com/politics/royce-white-amy-klobuchar-minnesota-jews-women-republicans"]),
        claim("rw2", "royce-white", "foreign_policy_restraint", 1, True,
              "Lists 'forever wars' as one of his three explicit top campaign priorities — alongside "
              "the border and the national debt — framing open-ended U.S. foreign military "
              "entanglements as a product of globalism he opposes. His 'God, Family, and Country — "
              "not globalism' platform treats foreign interventionism as a direct threat to American "
              "citizenship, aligning with the rubric's call to end post-9/11 forever-war "
              "entanglements.",
              ["https://roycewhite.us/",
               "https://en.wikipedia.org/wiki/Royce_White"]),
    ]),

    # ---------------- Mike Rogers (MI-R, US Senator 2026 candidate) ----------------
    ("mike-rogers-mi-senate-2026", "MI", "Senator", [
        claim("mr1", "mike-rogers-mi-senate-2026", "foreign_policy_restraint", 1, False,
              "One of the Republican Party's most aggressive Ukraine hawks: as chairman of the House "
              "Armed Services Committee he co-signed a letter urging the Biden administration to send "
              "Ukraine cluster munitions (DPICM), complained of 'reluctance to provide Ukraine with "
              "the right type and amount of long-range fires,' and — alongside Reps. McCaul and "
              "Turner — demanded on the war's first anniversary that 'President Biden needs to stop "
              "dragging his feet on providing the lethal aid necessary to end this war.' Identified "
              "by HuffPost as one of the GOP's 'Three Mikes — longtime Ukraine allies,' his record "
              "directly conflicts with the rubric's call to end foreign military entanglements.",
              ["https://www.foreign.senate.gov/press/rep/release/risch-wicker-mccaul-rogers-urge-biden-to-send-dpicm-to-ukraine",
               "https://www.huffpost.com/entry/gop-three-mikes-ukraine-allies_n_65caa014e4b01f4a8b01ec06"]),
        claim("mr2", "mike-rogers-mi-senate-2026", "election_integrity", 0, True,
              "After initially dismissing Trump's 2020 fraud allegations as 'conspiracy and hearsay,' "
              "Rogers reversed course and embraced election-integrity rhetoric: he claimed without "
              "contemporaneous evidence that a 'single van' of ballots swung his 2024 Senate loss, "
              "and built his 2026 campaign team with activists who sought to block Michigan's 2020 "
              "ballot certification and individuals pardoned by Trump for their roles in the "
              "fake-electors scheme — positioning him within the election-security reform wing of "
              "the party.",
              ["https://michiganadvance.com/2025/11/21/mike-rogers-once-denounced-election-denial-of-the-2020-election-now-hes-surrounded-by-it/",
               "https://www.wlns.com/capital-rundown/mike-rogers-surrounds-himself-with-election-deniers-ahead-of-2026-election/"]),
    ]),

    # ---------------- Lee Calhoun (MT-R, US Senator 2026 candidate, Daines seat) ----------------
    ("lee-calhoun", "MT", "Senator", [
        claim("lc1", "lee-calhoun", "foreign_policy_restraint", 0, True,
              "Explicitly supports enforcement of the 1973 War Powers Resolution, stating it 'is "
              "currently law and therefore should be enforced unless or until it is rescinded by "
              "Congress' because it 'was enacted precisely to control overreach by the executive "
              "branch relative to wasting the lives and resources of our military in an unnecessary "
              "war' — directly aligning with the rubric's call to restore Congress's Article I "
              "war-authorization power over the executive.",
              ["https://projects.montanafreepress.org/election-guide-2026/candidates/lee-calhoun/",
               "https://calhounformt.com/"]),
        claim("lc2", "lee-calhoun", "border_immigration", 2, False,
              "Openly supports the existence of sanctuary cities, stating he favors 'sanctuary cities "
              "to protect undocumented persons' — directly opposing the rubric's demand for uniform "
              "enforcement of federal immigration law and the elimination of jurisdictions that shield "
              "unlawful immigrants from deportation.",
              ["https://projects.montanafreepress.org/election-guide-2026/candidates/lee-calhoun/",
               "https://ivoterguide.com/candidate/91417/race/27491/election/1419"]),
    ]),

    # ---------------- Don Brown (NC-R, US Senator candidate, lost 3/3/2026 primary) ----------------
    ("don-brown-nc-senate", "NC", "Senator", [
        claim("db1", "don-brown-nc-senate", "self_defense", 1, True,
              "As a constitutional attorney, declared publicly that 'Restrictions on gun ownership "
              "are largely unconstitutional, and I oppose government imposed restrictions upon "
              "firearms ownership' — rejecting red-flag laws, assault-weapons bans, magazine limits, "
              "and registries as violations of the Second Amendment's plain text, in line with the "
              "rubric's defense of unrestricted lawful gun ownership.",
              ["https://ivoterguide.com/candidate/77732/race/24489/election/1371",
               "https://ballotpedia.org/Don_Brown_(North_Carolina)"]),
        claim("db2", "don-brown-nc-senate", "economic_stewardship", 2, True,
              "Proposed eliminating at least two-thirds of all federal agencies and two-thirds of "
              "all non-military federal personnel, with savings applied directly to the national "
              "debt, declaring: 'We have 3.2 million federal employees, over 400 agencies, and yet "
              "the national debt explodes at $37,000 per second.' His proposal for radical agency "
              "cuts to address deficit spending is consistent with the rubric's call for a balanced "
              "budget and opposition to chronic deficit borrowing.",
              ["https://ivoterguide.com/candidate/77732/race/24489/election/1371",
               "https://www.donbrownfornc.com/"]),
    ]),

    # ---------------- Jared Sullivan (NH-D, US Senator 2026 candidate, Shaheen seat) ----------------
    ("jared-sullivan-nh-senate", "NH", "Senator", [
        claim("js1", "jared-sullivan-nh-senate", "biblical_marriage", 2, False,
              "As a New Hampshire state representative, voted FOR HB 368 (2024) to prohibit New "
              "Hampshire from enforcing out-of-state orders removing children from homes for "
              "receiving gender-affirming care and to protect providers of such care; voted AGAINST "
              "a ban on hormone treatments and puberty blockers for minors; and voted AGAINST "
              "parental notification for curriculum covering sexual orientation and gender identity "
              "(HB 1312, 2024). Sullivan's NH House record consistently supports transgender-"
              "affirming law and policy — opposite to the rubric's standard of rejecting government "
              "promotion of transgender ideology.",
              ["https://www.citizenscount.org/candidate/jared-sullivan/serving",
               "https://reproequitynow.org/nhvoterecords"]),
        claim("js2", "jared-sullivan-nh-senate", "family_child_sovereignty", 0, False,
              "Voted against HB 1312 (2024), which would have required New Hampshire public schools "
              "to notify parents at least two weeks before any curriculum on sexual orientation, "
              "gender identity, or gender expression was taught to their children. By opposing "
              "parental notification on gender-related school content, Sullivan sided against the "
              "parental rights and family sovereignty the rubric upholds.",
              ["https://www.citizenscount.org/candidate/jared-sullivan/serving",
               "https://ballotpedia.org/Jared_Sullivan"]),
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""SRC-0823-AFFIRM — rewrite PAC-hygiene questions to affirmative search framing."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCORECARD = ROOT / "data" / "scorecard.json"

SANCTITY_FEDERAL = (
    "FEC / OpenSecrets search found no Planned Parenthood, NARAL, EMILY's List, "
    "or abortion-industry PAC contributions (as of the cited search date)"
)
SANCTITY_STATE = (
    "FEC / state campaign-finance search found no abortion-industry PAC contributions "
    "for state-legislative or statewide-office campaigns (as of the cited search date)"
)
FOREIGN_FEDERAL = (
    "TrackAIPAC / FEC / OpenSecrets search found no AIPAC, pro-Israel-lobby, "
    "or foreign-linked PAC contributions (as of the cited search date)"
)
FOREIGN_STATE = (
    "TrackAIPAC / FEC / state campaign-finance search found no AIPAC, pro-Israel-lobby, "
    "or foreign-linked PAC contributions for state-legislative or statewide campaigns "
    "(as of the cited search date)"
)


def patch_categories(data):
    for cat in data.get("categories", []):
        cid = cat.get("id")
        if cid == "sanctity_of_life":
            qs = list(cat.get("questions") or [None] * 5)
            qss = list(cat.get("questions_state") or [None] * 5)
            qs[4] = SANCTITY_FEDERAL
            qss[4] = SANCTITY_STATE
            cat["questions"] = qs
            cat["questions_state"] = qss
        elif cid == "foreign_policy_restraint":
            qs = list(cat.get("questions") or [None] * 5)
            qss = list(cat.get("questions_state") or [None] * 5)
            qs[3] = FOREIGN_FEDERAL
            qss[3] = FOREIGN_STATE
            cat["questions"] = qs
            cat["questions_state"] = qss


def patch_kiggans(data):
    for cand in data.get("candidates", []):
        if cand.get("slug") != "jen-kiggans":
            continue
        scores = cand.setdefault("scores", {})
        fpr = list(scores.get("foreign_policy_restraint") or [None] * 5)
        while len(fpr) < 5:
            fpr.append(None)
        fpr[3] = False
        scores["foreign_policy_restraint"] = fpr
        return
    raise SystemExit("jen-kiggans not found in scorecard.json")


def main():
    data = json.loads(SCORECARD.read_text())
    patch_categories(data)
    patch_kiggans(data)
    SCORECARD.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("Patched scorecard.json category questions (sanctity_of_life q5, foreign_policy_restraint q4)")
    print("Patched jen-kiggans foreign_policy_restraint[3] = False")


if __name__ == "__main__":
    main()

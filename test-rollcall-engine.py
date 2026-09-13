#!/usr/bin/env python3
"""test-rollcall-engine.py — fixture tests for the roll-call scoring path.

The invariant suite only greps the engine's source. This file runs the actual
predicates on recorded-shape fixtures: ITL polarity, the 124-7 credit-trap gate,
party-line exception, and the D-majority-TRUE / R-majority-FALSE inspection flag.

No network. No LLM. Exit 0 = all pass.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rollcall_score as rs
import rollcall_grammar as g

FAILS, PASSES = [], []


def check(name, ok, detail=""):
    (PASSES if ok else FAILS).append(name)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"\n          {detail}" if detail and not ok else ""))


def test_itl_polarity():
    # YEA on a bill that SUPPORTS the position → TRUE
    check("OTP YEA + yea=support → TRUE",
          rs.cell_verdict("support", "yea", is_itl=False) is True)
    check("OTP NAY + yea=support → FALSE",
          rs.cell_verdict("support", "nay", is_itl=False) is False)
    # ITL reverses: YEA = kill the bill = oppose its policy
    check("ITL YEA + yea=support → FALSE (NH reverse)",
          rs.cell_verdict("support", "yea", is_itl=True) is False)
    check("ITL NAY + yea=support → TRUE (voted against killing it)",
          rs.cell_verdict("support", "nay", is_itl=True) is True)
    check("ITL YEA + yea=oppose → TRUE (killed an opposing bill)",
          rs.cell_verdict("oppose", "yea", is_itl=True) is True)


def test_contested_gate():
    # MD HB1430 class: 124-7 is consensus housekeeping, not a position
    check("124-7 uncontested, no party split → skip",
          rs.vote_is_scoreable(124, 7, [80, 4], [44, 3]) is False)
    # Losing side >= 25%
    check("200-174 contested → keep",
          rs.vote_is_scoreable(200, 174, [10, 160], [190, 14]) is True)
    # Uncontested by margin BUT parties diverged (the party-line exception)
    check("90-10 uncontested margin but D vs R diverged → keep",
          rs.vote_is_scoreable(90, 10, [2, 8], [88, 2]) is True)
    # Tiny caucus (<5) does not count as a party majority
    check("tiny D caucus does not unlock the party-split exception",
          rs.vote_is_scoreable(100, 4, [1, 2], [99, 2]) is False)


def test_polarity_gate():
    # Correct conservative mapping: D majority FALSE, R majority TRUE — do NOT flag
    check("clean party-line (R TRUE / D FALSE) is not inverted",
          rs.polarity_looks_inverted([3, 40], [180, 8]) is False)
    # MD HB444 class: Democrat majority scored TRUE
    check("D majority TRUE (≥5) flags inverted polarity",
          rs.polarity_looks_inverted([30, 4], [10, 20]) is True)
    # MT HB818 class: Republican majority scored FALSE
    check("R majority FALSE (≥5) flags inverted polarity",
          rs.polarity_looks_inverted([2, 20], [8, 48]) is True)
    # Four Democrats TRUE is below the ≥5 floor — do not flag on noise
    check("D TRUE=4 is below the flag floor",
          rs.polarity_looks_inverted([4, 1], [20, 2]) is False)


def test_grammar_fixtures():
    check("NH OTP is final", g.kind("OTP") == "final")
    check("NH OTPA is final", g.kind("OTPA") == "final")
    check("NH ITL is itl (reversed)", g.kind("ITL") == "itl")
    check("Ought to Pass is final", g.kind("Ought to Pass") == "final")
    check("Not Concurred is excluded", g.kind("Senate Amendments NOT Concurred") is None)
    check("Table is excluded", g.kind("Lay on the Table") is None)
    check("second reading is second", g.kind("Second Reading") == "second")
    # scoreable(): second reading only when nothing else exists
    votes = [{"desc": "Second Reading", "yea": 40, "nay": 10},
             {"desc": "OTP", "yea": 41, "nay": 9}]
    picked = g.scoreable(votes)
    check("scoreable prefers OTP over second reading",
          len(picked) == 1 and picked[0][1] == "final")
    only_2nd = g.scoreable([{"desc": "Second Reading", "yea": 40, "nay": 10}])
    check("scoreable falls back to second reading when it is all the bill has",
          len(only_2nd) == 1 and only_2nd[0][1] == "second")
    check("scoreable drops a not-concur vote",
          g.scoreable([{"desc": "Amendments NOT Concurred", "yea": 48, "nay": 2}]) == [])


def test_chamber_fixture():
    """Tiny chamber: one ITL vote on an online-registration bill (yea=oppose)."""
    # Fixture shaped like a LegiScan getRollCall + session people + classifier result.
    cls = {"cat": "election_integrity", "q": 1, "yea": "oppose"}
    is_itl = True
    people = {
        1: {"name": "Alice Aye", "party": "R", "district": "1"},
        2: {"name": "Bob Nay", "party": "D", "district": "2"},
        3: {"name": "Cara Skip", "party": "R", "district": "3"},
    }
    rc_votes = [
        {"people_id": 1, "vote_text": "Yea"},   # ITL YEA = kill bill = oppose online reg = TRUE
        {"people_id": 2, "vote_text": "Nay"},   # ITL NAY = keep bill = support online reg = FALSE
        {"people_id": 3, "vote_text": "NV"},    # never scored
    ]
    cells = {}
    for mv in rc_votes:
        vt = (mv.get("vote_text") or "").strip().lower()
        if vt not in ("yea", "nay"):
            continue
        p = people[mv["people_id"]]
        cells[p["name"]] = rs.cell_verdict(cls["yea"], vt, is_itl)
    check("fixture: ITL YEA on an oppose-mapped bill is TRUE", cells.get("Alice Aye") is True)
    check("fixture: ITL NAY on an oppose-mapped bill is FALSE", cells.get("Bob Nay") is False)
    check("fixture: NV is not a cell", "Cara Skip" not in cells)


def test_engine_wires_helpers():
    eng = open(os.path.join(os.path.dirname(__file__), "legiscan-rollcall-engine.py")).read()
    cr = open(os.path.join(os.path.dirname(__file__), "commit_refinement.py")).read()
    check("engine imports rollcall_score (does not re-declare the predicates)",
          "import rollcall_score" in eng
          and "voted_for_bill = (vt == \"yea\") != is_itl" not in eng)
    check("engine has --refresh-classifications",
          "--refresh-classifications" in eng)
    check("commit_refinement stashes before reset --hard",
          "stash" in cr and "reset" in cr and "restore_stash" in cr)


def main():
    print("rollcall engine fixtures\n")
    test_itl_polarity()
    test_contested_gate()
    test_polarity_gate()
    test_grammar_fixtures()
    test_chamber_fixture()
    test_engine_wires_helpers()
    print(f"\n{'='*60}\n{len(PASSES)} passed, {len(FAILS)} FAILED")
    if FAILS:
        print("FAILED:")
        for f in FAILS:
            print(f"  - {f}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

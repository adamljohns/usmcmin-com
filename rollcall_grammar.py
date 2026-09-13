#!/usr/bin/env python3
"""rollcall_grammar.py — ONE definition of chamber vote grammar.

Chamber vote grammar is the #1 hidden blocker in this pipeline: New Hampshire looked
barren (0 of 364 matchable members) purely because its House abbreviates floor actions
as OTP/OTPA/ITL and the patterns only matched the spelled-out forms. Every state whose
grammar we learn is encoded here.

It lived in TWO copies — legiscan-rollcall-engine.py and rollcall-marquee-hunt.py — and
they DRIFTED: the hunter folded "second reading" into its main final-vote pattern while
the engine accepts second reading only as a fallback. The hunter therefore proposed bills
the engine then rejected, burning LegiScan queries and inflating `no_final_rc`.

Import from here. Do not re-declare these patterns anywhere.
"""
import re

# A decisive floor vote on the bill itself.
FINAL_RC = re.compile(
    r"third reading|final passage|final action|passage|floor vote|concur|ought to pass"
    r"|^otpa?$|\botpa?\b|shall the bill pass|"
    r"roll call results (passed|failed)|read 3rd time|"
    r"house passed|senate passed|passed as amended|passed on final reading", re.I)

# Some chambers take their decisive vote on SECOND reading and never hold a third (North
# Dakota). Treating 2nd reading as final everywhere would swallow procedural votes, so it
# is a FALLBACK: used only when a bill has no other final-type roll call.
SECOND_RC = re.compile(r"second reading|2nd reading", re.I)

# NH kills bills with an "Inexpedient to Legislate" FLOOR vote — a final action with
# REVERSED polarity: YEA on ITL = voting to kill the bill, i.e. against its policy.
ITL_RC = re.compile(r"inexpedient to legislate|^itl$|\bitl\b", re.I)

# Procedural maneuvers — never a recorded position on the policy.
TABLE_RC = re.compile(r"\btable\b|\blay on\b", re.I)
NOT_CONCUR = re.compile(r"not\s+concur", re.I)


def excluded(desc):
    """True if this roll call is procedural and must never be scored.

    'Not concur' is the MT HB818 trap: scoring it would have marked 48 Republican
    sponsors FALSE on their own bill.
    """
    d = desc or ""
    return bool(TABLE_RC.search(d) or NOT_CONCUR.search(d))


def kind(desc):
    """Classify one roll-call description: 'final' | 'itl' | 'second' | None.

    'itl' carries REVERSED polarity — the caller must flip the verdict.
    'second' is only usable when the bill has no 'final' or 'itl' roll call.
    """
    d = desc or ""
    if excluded(d):
        return None
    if ITL_RC.search(d):
        return "itl"
    if FINAL_RC.search(d):
        return "final"
    if SECOND_RC.search(d):
        return "second"
    return None


def scoreable(votes):
    """Given a bill's roll calls, return those the ENGINE would actually score.

    Mirrors the engine's acceptance exactly so the hunter stops proposing bills the
    engine will reject: prefer final/itl; fall back to second reading only if neither
    exists anywhere on the bill.
    """
    tagged = [(v, kind((v or {}).get("desc"))) for v in (votes or [])]
    primary = [(v, k) for v, k in tagged if k in ("final", "itl")]
    if primary:
        return primary
    return [(v, k) for v, k in tagged if k == "second"]

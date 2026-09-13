#!/usr/bin/env python3
"""rollcall_score.py — deterministic vote → cell math, ONE definition.

The roll-call engine's LLM step only CLASSIFIES a bill. Everything after that
(ITL polarity flip, contested-vote gate, party-split exception, inspection-gate
polarity flag) is arithmetic on LegiScan numbers. That arithmetic used to live
inline in legiscan-rollcall-engine.py with no fixture test — a silent invert
would only show up on a named official's public profile.

Import from here. Do not re-implement these predicates in the engine or hunter.
"""


def cell_verdict(yea_means, vote_text, is_itl):
    """Return True if this floor vote supports the rubric position.

    yea_means: 'support' | 'oppose' — what a YEA on the *bill* means for the cell.
    vote_text: 'yea' | 'nay' (absent/NV never reach this function).
    is_itl: YEA on Inexpedient-to-Legislate = voting to KILL the bill (NH).
    """
    voted_for_bill = (vote_text == "yea") != bool(is_itl)
    return (yea_means == "support") == voted_for_bill


def vote_is_scoreable(yea_n, nay_n, d_side, r_side, min_losing=0.25, min_party=5):
    """True if the roll call carries positional signal.

    Keep when (a) the losing side is >=25% of yea+nay, or (b) the parties
    genuinely diverged (majority of D's opposite majority of R's). A 124-7
    charter-FACILITIES vote is consensus housekeeping — scoring it is the
    MD HB1430 misleading-credit trap.
    d_side / r_side are [yea, nay] counts among that party's members.
    """
    tot = int(yea_n) + int(nay_n)
    contested = tot > 0 and min(int(yea_n), int(nay_n)) / tot >= min_losing

    def maj(side):
        y, n = side
        return None if (y + n) < min_party else (y > n)

    dmaj, rmaj = maj(d_side), maj(r_side)
    party_divided = dmaj is not None and rmaj is not None and dmaj != rmaj
    return contested or party_divided


def polarity_looks_inverted(d_tf, r_tf, min_n=5):
    """True if a Democrat majority scored TRUE or a Republican majority FALSE.

    On this Christian-conservative rubric a correct mapping almost never yields
    that shape; when it does the bill is usually polarity-inverted (MD HB444)
    or procedural (MT HB818). d_tf / r_tf are [TRUE_count, FALSE_count].
    """
    dT, dF = d_tf
    rT, rF = r_tf
    return (dT > dF and dT >= min_n) or (rF > rT and rF >= min_n)

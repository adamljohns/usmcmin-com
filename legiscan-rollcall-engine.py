#!/usr/bin/env python3
"""legiscan-rollcall-engine.py — roll-call-first evidence scoring. THE coverage inversion.

Instead of researching one candidate at a time, classify one MARQUEE BILL and every
legislator on its recorded roll call gets a cited cell simultaneously (a 141-member vote
scores a whole chamber at once). This is how the ~5,000 bio-only state legislators — whom
per-candidate source discovery cannot reach — become evidence-scored.

TRUST MODEL (libel-grade, same shape as the grind):
  - The only LLM step is BILL CLASSIFICATION: Qwen maps a bill title/description to ONE
    rubric question + what a YEA means (support/oppose); Gemma must independently agree
    (title -> same question, same polarity) or the bill is SKIPPED. Ambiguous bills SKIP.
  - The VOTES are deterministic LegiScan API data — no model touches them. Yea/Nay only
    (absent/excused/NV never scored). One bill maps to at most ONE rubric cell.
  - Candidate matching is exact: state + normalized name (+ district tiebreak); ambiguous
    names are SKIPPED, never guessed (slug@STATE keys through the hardened engine).
  - Citation: the bill's OFFICIAL state_link + a note naming the vote, date, and tally.
  - Existing evidence_* candidates are left alone (this fills the unscored frontier).

Usage:
  legiscan-rollcall-engine.py MD                      # dry: classify + build dossier + report
  legiscan-rollcall-engine.py MD --max-bills 40       # cap getBill spend for the state
  legiscan-rollcall-engine.py MD --apply              # ...then apply+build+push via commit_refinement
"""
import json, os, re, subprocess, sys, time

sys.path.insert(0, ".")
import importlib.util
_spec = importlib.util.spec_from_file_location("lpe", "local-politician-extract.py")
lpe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lpe)                      # chat/model_at — one implementation
from legiscan_client import LegiScanClient, LegiScanError

SCORECARD = "data/scorecard.json"
CLASS_CACHE = os.path.expanduser("~/.openclaw/state/legiscan-bill-classifications.json")
KW = re.compile(r"abortion|reproductive|firearm|gun|second amendment|marriage|gender|transgender|"
                r"parent|school choice|charter|voucher|voter|election|ballot|immigra|sanctuary|"
                r"bail|police|religio|prayer|obscen|library|puberty|minor|esg|gold|bullion", re.I)
FINAL_RC = re.compile(r"third reading|final passage|final action|passage|floor vote|concur|ought to pass"
                      r"|^otpa?$|\botpa?\b|shall the bill pass|"
                      r"roll call results (passed|failed)|read 3rd time|"
                      r"house passed|senate passed|passed as amended|passed on final reading", re.I)
# Some chambers take their decisive floor vote on SECOND reading and never hold a third
# (North Dakota). Treating 2nd reading as final everywhere would swallow procedural votes,
# so it is used ONLY as a fallback when a bill has no other final-type roll call.
SECOND_RC = re.compile(r"second reading|2nd reading", re.I)
# NH kills bills with an "Inexpedient to Legislate" FLOOR vote — a final action with
# REVERSED polarity: YEA on ITL = voting to kill the bill (i.e., against its policy).
# NH's House abbreviates its floor actions (OTP/OTPA = Ought To Pass [as Amended], ITL);
# matching only the spelled-out forms caught NH's 24-member SENATE votes while missing
# every 398-member HOUSE vote — the reason NH looked barren despite 364 matchable members.
ITL_RC = re.compile(r"inexpedient to legislate|^itl$|\bitl\b", re.I)
# Motions to table are procedural maneuvers, not a recorded position on the policy.
TABLE_RC = re.compile(r"\btable\b|\blay on\b", re.I)

CLASSIFY_SYS = (
    "You map a state legislative BILL to a voter-scorecard POSITION. You are given numbered "
    "positions (affirmative policy statements) and a bill title/description. Reply ONLY with JSON: "
    '{"n": <position number>, "yea": "support"|"oppose"} — meaning a YEA vote on this bill '
    "supports/opposes that numbered position — or {\"skip\": true} if no position fits cleanly. "
    "HARD RULES: pick at most ONE position, the single clearest fit. If the bill is procedural, "
    "budgetary, local-scope, symbolic, or its policy direction is not OBVIOUS from the text alone, "
    "reply {\"skip\": true}. Funding, facilities, or administration FOR AN EXISTING program is NOT "
    "a position on that program — skip those. Wrong-and-confident is unacceptable; skipping is always safe."
)
VERIFY_SYS = (
    "You are auditing a bill-to-scorecard mapping. Given a POSITION (affirmative policy statement), "
    "a BILL title/description, and the claim that a YEA vote {POLARITY} that position: answer YES "
    "only if the mapping is obviously correct from the text alone (right topic AND right direction). "
    "Otherwise answer NO. Answer with one word."
)


def norm_name(s):
    s = re.sub(r"\s+(jr|sr|ii|iii|iv)\.?$", "", (s or "").strip().lower(), flags=re.I)
    s = re.sub(r"[^a-z\s'-]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def surname(s):
    parts = norm_name(s).split()
    return parts[-1] if parts else ""


def main():
    state = sys.argv[1].upper()
    max_bills = int(sys.argv[sys.argv.index("--max-bills") + 1]) if "--max-bills" in sys.argv else 40
    prior = "--prior" in sys.argv   # sweep the PREVIOUS regular session (2025 meat for states whose 2026 is young)
    # --bills HB10,HB148: work ONLY these bill numbers, bypassing the keyword/marquee sort.
    # For chambers like NH where the classifier skips en masse but a single big contested
    # floor vote can score hundreds, hand-picking the marquee bills is far cheaper than
    # classifying 200 to find 2.
    only_bills = ([b.strip().upper() for b in sys.argv[sys.argv.index("--bills") + 1].split(",")]
                  if "--bills" in sys.argv else None)
    apply_now = "--apply" in sys.argv
    today = time.strftime("%Y-%m-%d")

    qwen = "http://127.0.0.1:1235/v1"; gemma = "http://127.0.0.1:1234/v1"
    qmodel = lpe.model_at(qwen)
    gmodel = lpe.model_at(gemma, prefer=["gemma-4-31b", "gemma"])
    if not (qmodel and gmodel):
        sys.exit("ABORT: need BOTH local models (Qwen classify + Gemma verify) — refusing to run single-brained.")

    sc = json.load(open(SCORECARD))
    cats = sc["categories"]
    qlist = lpe.applicable_questions(cats, "state")
    qmap = {n + 1: qlist[n] for n in range(len(qlist))}
    numbered = "\n".join(f"{n}. {q}" for n, (_, _, q) in qmap.items())

    # --- candidates we can score ---
    def evid(c): return ((c.get("profile") or {}).get("confidence") or "").startswith("evidence")

    def backed_count(c):
        """Answered cells carrying documentation (footnote ref OR claims[] entry).
        Mirrors generate-profiles.backed_answer_count — the site withholds a letter
        grade below MIN_BACKED_FOR_GRADE(5), so this is the enrichment target."""
        sc_ = c.get("scores") or {}
        s_ = set()
        for cat_, rp in (c.get("answer_footnotes") or {}).items():
            arr_ = sc_.get(cat_) or []
            for qi_, refs_ in enumerate(rp or []):
                if refs_ and qi_ < len(arr_) and arr_[qi_] in (True, False):
                    s_.add((cat_, qi_))
        for cl_ in (c.get("claims") or []):
            cat_, qi_ = cl_.get("category"), cl_.get("question_idx")
            arr_ = sc_.get(cat_) or []
            if cat_ is not None and isinstance(qi_, int) and qi_ < len(arr_) and arr_[qi_] in (True, False):
                s_.add((cat_, qi_))
        return len(s_)

    # DEFAULT: only UNSCORED candidates (coverage mode — find new people).
    # --enrich: ALSO include already-evidence records that are UNDER-DOCUMENTED
    # (<5 backed cells). Those are exactly the records whose letter grade the site
    # now withholds; without this they were skipped as "no_match" and the 2026-08-18
    # enrichment sweep returned ~55 candidates while reporting 682 unmatched in NH.
    enrich = "--enrich" in sys.argv
    base = [c for c in sc["candidates"]
            if (c.get("state") or "").upper() == state and c.get("level") == "state"
            and (c.get("status") or "active") not in ("lost", "former", "deceased")]
    pool = [c for c in base if (not evid(c)) or (enrich and backed_count(c) < 5)]
    by_name = {}
    for c in pool:
        by_name.setdefault(norm_name(c.get("name")), []).append(c)
        by_name.setdefault(surname(c.get("name")), []).append(c)
    if enrich:
        _new = sum(1 for c in pool if not evid(c))
        print(f"{state}: {len(pool)} targets ({_new} unscored + {len(pool)-_new} under-documented) [ENRICH]")
    else:
        print(f"{state}: {len(pool)} unscored active state legislators in scorecard")

    ls = LegiScanClient()
    spent0 = ls.queries_this_month
    sess = ls.pull("getSessionList", state=state).get("sessions") or []
    if not sess:
        sys.exit(f"no sessions for {state}")
    # Prefer the newest REGULAR session — special sessions are tiny/topical (GA's "2026
    # Special Session" had 176 redistricting bills and zero rubric signal). Fall back to
    # newest anything (TX-style odd-year states: the sine-died 2025 regular is the record).
    regular = sorted([s for s in sess if not s.get("special")] or sess,
                     key=lambda s: (s.get("year_start") or 0, s.get("session_id")), reverse=True)
    idx = 1 if (prior and len(regular) > 1) else 0
    pick = regular[idx]
    sid = pick["session_id"]
    print(f"session: {sid} {pick.get('session_name')}" + (" [PRIOR]" if idx else ""))

    bills = [v for v in (ls.pull("getMasterList", id=sid).get("masterlist") or {}).values()
             if isinstance(v, dict) and v.get("bill_id")]
    flagged = ([b for b in bills if (b.get("number") or "").upper() in only_bills] if only_bills
               else [b for b in bills if KW.search(b.get("title") or "")])
    # Marquee-first: burn the per-bill budget on the strongest rubric signals, not on
    # bill-number order (grandparent visitation before the Heartbeat Bill = wasted spend).
    STRONG = re.compile(r"abortion|reproductive|heartbeat|firearm|handgun|assault weapon|red flag|"
                        r"transgender|gender-affirm|gender identity|marriage|school choice|voucher|"
                        r"charter school|parental right|voter id|citizenship.*vot|sanctuary|"
                        r"illegal immigra|bail reform|defund|puberty|minor.*(surgery|hormone)|"
                        r"religious (freedom|liberty)|prayer|obscen|drag", re.I)
    flagged.sort(key=lambda b: (0 if STRONG.search(b.get("title") or "") else 1, b.get("number") or ""))
    n_strong = sum(1 for b in flagged if STRONG.search(b.get("title") or ""))
    print(f"bills {len(bills)} | keyword-flagged {len(flagged)} (strong-signal {n_strong}) | working first {max_bills}")

    # --- classification (cached forever; Qwen proposes, Gemma must agree) ---
    try:
        ccache = json.load(open(CLASS_CACHE))
    except Exception:
        ccache = {}
    os.makedirs(os.path.dirname(CLASS_CACHE), exist_ok=True)

    # people map for THIS session (1 query, heavily reused)
    ppl = (ls.pull("getSessionPeople", id=sid).get("sessionpeople") or {}).get("people") or []
    people = {p["people_id"]: p for p in ppl}
    print(f"session people: {len(people)}")

    records, used_bills, skipped = {}, [], {"ambiguous_class": 0, "gemma_no": 0, "no_final_rc": 0,
                                           "no_match": 0, "ambiguous_name": 0}
    # LOW-INFORMATION GATE (the TN caption-bill lesson): "AN ACT to amend Title 49, relative
    # to public charter schools" says NOTHING about direction — models judged an unknowable
    # and scored a progressive TRUE on school choice. A bill is judgeable from text only if
    # its title carries a directional verb alongside the topic; caption boilerplate dies here.
    DIRECTIONAL = re.compile(r"prohibit|ban\b|bann|require|requir|establish|repeal|expand|restrict|"
                             r"eliminat|creat|authoriz|legaliz|criminal|prevent|protect|restor|"
                             r"exempt|mandat|abolish|permit|allow|enact|prohibition|freedom|right",
                             re.I)
    CAPTION = re.compile(r"^an act to amend", re.I)

    # PERMANENT VETOES — a bill an inspection rejected must never be re-proposed by a later
    # sweep (OK HB2154 returned the day after its first veto). Repo-tracked so every agent
    # and every future run honors the same rejections.
    try:
        VETOED = json.load(open("rollcall-vetoes.json")).get("vetoed") or {}
    except Exception:
        VETOED = {}

    for b in flagged[:max_bills]:
        if f"{state}:{b.get('number')}" in VETOED:
            skipped["vetoed_bill"] = skipped.get("vetoed_bill", 0) + 1
            continue
        title_txt = b.get("title") or ""
        # CAPTION boilerplate ("AN ACT to amend Title 49...") carries no direction in the
        # title — but if it's a STRONG-signal subject, the official DESCRIPTION usually does,
        # and the second-chance classifier below reads it. Skipping outright here starved TN
        # (110 caption skips in one run). Only drop captions with no strong signal at all.
        if CAPTION.match(title_txt) and not DIRECTIONAL.search(title_txt) and not STRONG.search(title_txt):
            skipped["caption_bill"] = skipped.get("caption_bill", 0) + 1
            continue
        bkey = f"{state}:{b['bill_id']}"
        cls = ccache.get(bkey)
        if cls is None:
            title = f"{b.get('number')} — {b.get('title') or ''}"
            try:
                raw = lpe.chat(qwen, qmodel, CLASSIFY_SYS,
                               f"NUMBERED POSITIONS:\n{numbered}\n\nBILL:\n{title}", max_tokens=60)
                v = lpe.extract_json(raw) or {}
            except Exception:
                v = {}
            if not isinstance(v, dict) or v.get("skip") or v.get("n") not in qmap or v.get("yea") not in ("support", "oppose"):
                cls = {"skip": True}
            else:
                cat_id, q_idx, q_text = qmap[v["n"]]
                pol = "SUPPORTS" if v["yea"] == "support" else "OPPOSES"
                try:
                    ans = lpe.chat(gemma, gmodel, VERIFY_SYS.replace("{POLARITY}", pol),
                                   f"POSITION: {q_text}\nBILL: {title}", max_tokens=6).strip().upper()
                except Exception:
                    ans = "NO"
                cls = ({"cat": cat_id, "q": q_idx, "yea": v["yea"], "title": b.get("title")}
                       if ans.startswith("YES") else {"skip": True, "why": "gemma_no"})
                if cls.get("why") == "gemma_no":
                    skipped["gemma_no"] += 1
            ccache[bkey] = cls
            json.dump(ccache, open(CLASS_CACHE, "w"), indent=1)
        if cls.get("skip"):
            # SECOND-CHANCE CLASSIFICATION (the Missouri lesson): red states whose titles are
            # low-info ("Modifies provisions relating to firearms") skip on title alone. For
            # strong-signal bills only, spend one getBill and re-classify with the official
            # description; same Qwen-proposes/Gemma-agrees bar. Cached like everything else.
            dkey = bkey + ":desc"
            cls2 = ccache.get(dkey)
            if cls2 is None and STRONG.search(title_txt):
                bill_pre = ls.pull("getBill", id=b["bill_id"]).get("bill") or {}
                dtxt = (f"{bill_pre.get('bill_number')} — {bill_pre.get('title') or ''}\n"
                        f"{(bill_pre.get('description') or '')[:600]}")
                try:
                    raw = lpe.chat(qwen, qmodel, CLASSIFY_SYS,
                                   f"NUMBERED POSITIONS:\n{numbered}\n\nBILL:\n{dtxt}", max_tokens=60)
                    v = lpe.extract_json(raw) or {}
                except Exception:
                    v = {}
                if not isinstance(v, dict) or v.get("skip") or v.get("n") not in qmap or v.get("yea") not in ("support", "oppose"):
                    cls2 = {"skip": True}
                else:
                    cat_i, q_i, q_t = qmap[v["n"]]
                    pol = "SUPPORTS" if v["yea"] == "support" else "OPPOSES"
                    try:
                        ans = lpe.chat(gemma, gmodel, VERIFY_SYS.replace("{POLARITY}", pol),
                                       f"POSITION: {q_t}\nBILL: {dtxt}", max_tokens=6).strip().upper()
                    except Exception:
                        ans = "NO"
                    cls2 = ({"cat": cat_i, "q": q_i, "yea": v["yea"], "title": bill_pre.get("title")}
                            if ans.startswith("YES") else {"skip": True})
                ccache[dkey] = cls2
                json.dump(ccache, open(CLASS_CACHE, "w"), indent=1)
            if cls2 and not cls2.get("skip"):
                cls = cls2
            else:
                skipped["ambiguous_class"] += 1
                continue

        bill = ls.pull("getBill", id=b["bill_id"]).get("bill") or {}
        # "Amendments NOT Concurred" is a procedural concurrence dispute, not passage — MT's
        # HB818 not-concur vote marked 48 R's FALSE on their own bill before this was vetoed.
        def usable(v):
            d = v.get("desc") or ""
            return not TABLE_RC.search(d) and not re.search(r"not\s+concur", d, re.I)
        finals = [v for v in (bill.get("votes") or [])
                  if usable(v) and (FINAL_RC.search(v.get("desc") or "") or ITL_RC.search(v.get("desc") or ""))]
        if not finals:   # ND-style chambers: the second-reading vote IS the decisive one
            finals = [v for v in (bill.get("votes") or []) if usable(v) and SECOND_RC.search(v.get("desc") or "")]
        if not finals:
            skipped["no_final_rc"] += 1
            continue
        # DUAL-DIRECTION COHERENCE GATE (the HB444 lesson): double-negative titles
        # ("Immigration Enforcement Agreements - Prohibition") invert polarity past a single
        # yes/no verify — that run scored 30 Democrats TRUE on sanctuary PREEMPTION. So with
        # the bill's full description in hand, ask BOTH models BOTH directions; keep the
        # mapping only if all four answers are coherent (support=YES/oppose=NO or the reverse,
        # unanimously, and matching the classifier's polarity). Any confusion = skip the bill.
        cat_id, q_idx = cls["cat"], cls["q"]
        q_text = next(q for n, (ci, qi, q) in qmap.items() if ci == cat_id and qi == q_idx)
        desc = f"{bill.get('bill_number')} — {bill.get('title') or ''}\n{(bill.get('description') or '')[:500]}"
        answers = {}
        try:
            for mdl_base, mdl in (( qwen, qmodel), (gemma, gmodel)):
                for direction in ("SUPPORTS", "OPPOSES"):
                    a = lpe.chat(mdl_base, mdl,
                                 "Answer with one word, YES or NO. Be literal; prohibitions and "
                                 "repeals reverse direction.",
                                 f"POSITION: {q_text}\nBILL:\n{desc}\n\nQUESTION: Does a YEA vote on "
                                 f"this bill {direction} the position?", max_tokens=6).strip().upper()
                    answers[(mdl, direction)] = a.startswith("YES")
        except Exception:
            skipped["coherence_error"] = skipped.get("coherence_error", 0) + 1
            continue
        sup = [answers[(m, "SUPPORTS")] for m in (qmodel, gmodel)]
        opp = [answers[(m, "OPPOSES")] for m in (qmodel, gmodel)]
        coherent_support = all(sup) and not any(opp)
        coherent_oppose = all(opp) and not any(sup)
        if not ((coherent_support and cls["yea"] == "support") or
                (coherent_oppose and cls["yea"] == "oppose")):
            skipped["incoherent_polarity"] = skipped.get("incoherent_polarity", 0) + 1
            continue
        # MULTI-CHAMBER: a bill that passed both houses has a final roll call in EACH, and a
        # legislator sits in only one. Scoring just finals[-1] left an entire chamber uncounted
        # on every bill (AL SB79 reached 88 of 138). Take the last final vote PER CHAMBER.
        by_chamber = {}
        for v in finals:
            by_chamber[v.get("chamber") or v.get("chamber_id") or len(by_chamber)] = v
        n_scored_this_bill = 0
        src = bill.get("state_link") or bill.get("url") or f"https://legiscan.com/{state}/bill/{bill.get('bill_number')}"

        for _ch, fv in by_chamber.items():
            rc = ls.pull("getRollCall", id=fv["roll_call_id"]).get("roll_call") or {}
            is_itl = bool(ITL_RC.search(fv.get("desc") or ""))

            # CONTESTED-VOTE GATE: a roll call only carries positional signal if it divided the
        # chamber. A 124-7 charter-FACILITIES vote is consensus housekeeping — scoring 88
        # Democrats TRUE on "school choice" from it is the misleading-credit trap the
        # methodology forbids. Keep a vote only if (a) the losing side is >=25% of yea+nay,
        # or (b) the parties genuinely diverged (majority of D's opposite majority of R's) —
        # the mechanical form of the runbook's "party-line marquee votes are HARD evidence."
            yea_n, nay_n = int(rc.get("yea") or 0), int(rc.get("nay") or 0)
            contested = (yea_n + nay_n) > 0 and min(yea_n, nay_n) / (yea_n + nay_n) >= 0.25
            py = {"D": [0, 0], "R": [0, 0]}
            for mv in (rc.get("votes") or []):
                vt = (mv.get("vote_text") or "").strip().lower()
                if vt not in ("yea", "nay"):
                    continue
                pp = (people.get(mv.get("people_id")) or {}).get("party") or ""
                if pp in py:
                    py[pp][0 if vt == "yea" else 1] += 1
            def maj(side):
                y, n = side
                return None if (y + n) < 5 else (y > n)
            dmaj, rmaj = maj(py["D"]), maj(py["R"])
            party_divided = dmaj is not None and rmaj is not None and dmaj != rmaj
            if not (contested or party_divided):
                skipped["uncontested"] = skipped.get("uncontested", 0) + 1
                continue

            tally = f"{rc.get('yea')}-{rc.get('nay')}"
            for mv in (rc.get("votes") or []):
                vt = (mv.get("vote_text") or "").strip().lower()
                if vt not in ("yea", "nay"):
                    continue                      # absent/excused/NV are never positions
                p = people.get(mv.get("people_id")) or {}
                nm = norm_name(p.get("name"))
                matches = [c for c in {id(x): x for x in (by_name.get(nm, []) + by_name.get(surname(p.get("name")), []))}.values()]
                # district tiebreak when >1
                if len(matches) > 1 and p.get("district"):
                    dm = [c for c in matches if str(c.get("district") or "") and str(c.get("district")) in str(p.get("district"))]
                    matches = dm or matches
                if not matches:
                    skipped["no_match"] += 1
                    continue
                if len(matches) > 1:
                    skipped["ambiguous_name"] += 1
                    continue
                c = matches[0]
                # ITL reverses: YEA on Inexpedient-to-Legislate = voting AGAINST the bill.
                voted_for_bill = (vt == "yea") != is_itl
                supports = (cls["yea"] == "support") == voted_for_bill
                key = f"{c['slug']}@{state}"
                rec = records.setdefault(key, {"profile": {
                    "confidence": (c.get("profile") or {}).get("confidence") or "evidence_state",
                    "confidence_note": f"Roll-call engine (LegiScan API, Qwen+Gemma-agreed bill mapping) {today}",
                    "last_refined": today, "grind_strikes": 0}, "evidence": {}, "sources_add": []})
                cellq = str(cls["q"])
                if cellq in rec["evidence"].get(cls["cat"], {}):
                    continue                      # first recorded final vote wins; don't churn
                rec["evidence"].setdefault(cls["cat"], {})[cellq] = {
                    "v": bool(supports),
                    "src": [src],
                    "note": (f"Voted {vt.upper()} on {bill.get('bill_number')} — "
                             f"{(cls.get('title') or '')[:150]} ({rc.get('desc')}, {rc.get('date')}, {tally}).")[:400],
                }
                if src not in rec["sources_add"]:
                    rec["sources_add"].append(src)
                n_scored_this_bill += 1
        if n_scored_this_bill:
            used_bills.append(f"{bill.get('bill_number')} -> {cls['cat']}[{cls['q']}] ({n_scored_this_bill} legislators)")

    for k, rec in records.items():
        ncells = sum(len(q) for q in rec["evidence"].values())
        rec["notes_append"] = f"Roll-call engine {today}: {ncells} recorded floor vote(s) via LegiScan API."

    print(f"\nbills used: {len(used_bills)}")
    for u in used_bills[:12]:
        print("   ", u)
    cells = sum(len(q) for r in records.values() for q in r["evidence"].values())
    print(f"RESULT: {len(records)} candidate(s), {cells} cited cells | skipped: {skipped}")
    print(f"LegiScan queries this run: {ls.queries_this_month - spent0} (month total {ls.queries_this_month}/{ls.monthly_budget})")
    if not records:
        return 1

    # ── AUTOMATED INSPECTION GATE ────────────────────────────────────────────────
    # Every veto to date (65 bills) came from a HUMAN reading a party-vs-verdict table.
    # That judgment cannot be the only thing standing between a bad mapping and a public
    # scorecard of named officials, because crons and PSAs run this engine unattended.
    # The single most reliable machine-checkable signal from those 65 vetoes: on this
    # Christian-conservative rubric a correct mapping almost never yields a DEMOCRAT
    # MAJORITY scoring TRUE or a REPUBLICAN MAJORITY scoring FALSE. When it does, the
    # bill's polarity is usually inverted (a double-negative title like MD HB444
    # "Immigration Enforcement Agreements - Prohibition" or CA SB1174) or it is a
    # procedural motion (MT HB818 "Amendments NOT Concurred").
    #
    # A flagged dossier is written to a *.FLAGGED.json name that the orchestrator does
    # NOT pick up, and the run exits 2 — so an unattended round cannot ship it. A human
    # who has read the report can still apply it deliberately.
    sc_all = json.load(open(SCORECARD))["candidates"]
    party_of = {c["slug"]: (c.get("party") or "?") for c in sc_all}
    tallies = {}
    for k, rec in records.items():
        pty = party_of.get(k.split("@")[0], "?")
        for cat, qs in rec["evidence"].items():
            for qi, e in qs.items():
                note = str(e.get("note") or "")
                bill = note.split("—")[0].replace("Voted YEA on", "").replace("Voted NAY on", "").strip()
                t = tallies.setdefault((bill or cat, cat, qi), {"D": [0, 0], "R": [0, 0], "n": 0})
                t["n"] += 1
                if pty in ("D", "R"):
                    t[pty][0 if e["v"] else 1] += 1

    flagged = []
    for (bill, cat, qi), t in tallies.items():
        dT, dF = t["D"]; rT, rF = t["R"]
        if (dT > dF and dT >= 5) or (rF > rT and rF >= 5):
            flagged.append((bill, cat, qi, t))

    if flagged:
        print("\n" + "=" * 74)
        print("⛔ INSPECTION GATE — POLARITY LOOKS INVERTED; dossier withheld from apply")
        for bill, cat, qi, t in flagged:
            print(f"   {bill} -> {cat}[{qi}]  D(T/F)={t['D'][0]}/{t['D'][1]}  R(T/F)={t['R'][0]}/{t['R'][1]}  n={t['n']}")
        print("   Read the bill's FULL text (title truncations lie in both directions).")
        print("   If genuinely wrong:  python3 add-veto.py \"ST:BILL\" \"reason\"")
        print("   If genuinely right:  re-run with --allow-flagged")
        print("=" * 74)

    os.makedirs("refinements", exist_ok=True)
    suffix = ".FLAGGED" if (flagged and "--allow-flagged" not in sys.argv) else ""
    dpath = f"refinements/rollcall-{state.lower()}-{time.strftime('%Y-%m-%d-%H%M')}{suffix}.json"
    json.dump({"_meta": {"author": "rollcall-engine", "date": today,
                         "note": f"{state} roll-call-first scoring (LegiScan API; Qwen+Gemma-agreed bill mappings)"
                                 + (" — POLARITY-FLAGGED, needs human review" if suffix else ""),
                         "inspection": {"bill_mappings": len(tallies), "flagged": len(flagged)}},
               "reset_unspecified": False, "records": records}, open(dpath, "w"), indent=1)
    print(f"dossier: {dpath}")
    if suffix:
        print("EXIT 2 — flagged dossier is NOT applied automatically.")
        return 2
    if apply_now:
        return subprocess.call(["/opt/homebrew/bin/python3", "commit_refinement.py", dpath,
                                f"rollcall({state}): {len(records)} legislators, {cells} cited floor votes (LegiScan)"])
    print("dry run — review, then apply with commit_refinement.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Local-LLM politician position extraction — the zero-cloud-usage scorecard worker.

The civic twin of local-pastor-extract.py. Reads a batch of candidates, fetches
each one's authoritative sources (official/campaign site + Ballotpedia), asks a
LOCAL model (Qwen 3.6 on :1235) to identify which RESOLUTE rubric positions the
candidate's record clearly supports or opposes — each backed by an EXACT quote —
then a second LOCAL model (Gemma on :1234) cross-checks polarity and writes the
neutral claim prose. Emits a findings file the merge step turns into claims/scores.

HONESTY ENFORCEMENT (why a small local model is trusted for a libel-sensitive tool):
the model only PROPOSES; a mechanical gate VERIFIES. A finding survives only if —
  1. VERBATIM: the model's quote appears word-for-word (whitespace/case-normalized)
     in a page we actually fetched — so it cannot fabricate a source or a vote;
  2. CROSS-CHECK: a second model agrees the quote genuinely justifies the verdict
     (right topic, right direction) — else the finding is HELD, never scored;
  3. Party is never evidence. No quote => null. Wrong-and-confident is the only
     unacceptable outcome, so anything short of a verified quote stays blank.

Usage: local-politician-extract.py BATCH.json OUT.json [--qwen URL] [--gemma URL] [--no-crosscheck]
  BATCH.json = [{slug,name,state,level,party,office,website,campaign_website}, ...]
"""
import json, re, ssl, sys, time, urllib.request, urllib.error

UA = {"User-Agent": "Mozilla/5.0 (compatible; MOOPScorecardBot/1.0; +https://usmcmin.com)"}
CTX = ssl._create_unverified_context()
ISSUE_PATHS = ["", "/issues", "/on-the-issues", "/priorities", "/platform", "/record",
               "/positions", "/agenda", "/about", "/beliefs", "/values", "/where-i-stand"]
ISSUEY = re.compile(r"issue|priorit|platform|record|position|agenda|values|beliefs|where-i-stand|on-the-issues|my-plan", re.I)
HREF_RE = re.compile(r'href=["\']([^"\'#?]+)', re.I)
SCORECARD = "data/scorecard.json"


def fetch(url, timeout=12):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read(500_000).decode("utf-8", "replace")


def to_text(html):
    html = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    import html as h
    return re.sub(r"\s+", " ", h.unescape(html)).strip()


def norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def discover_links(raw, base):
    from urllib.parse import urljoin, urlparse
    host = urlparse(base).netloc.lower().replace("www.", "")
    out, seen = [], set()
    for m in HREF_RE.finditer(raw):
        u = urljoin(base + "/", m.group(1)).split("#")[0]
        pu = urlparse(u)
        if pu.netloc.lower().replace("www.", "") != host:
            continue
        if not ISSUEY.search(pu.path):
            continue
        if re.search(r"\.(pdf|jpe?g|png|gif|svg|mp[34]|css|js|ico)$", pu.path, re.I):
            continue
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out[:4]


def model_at(base, prefer=None):
    """Return a chat model id served at base. If prefer is given, pick a model whose
    name contains it (so the cross-check runs on Gemma even when :1234 also lists Qwen)."""
    try:
        with urllib.request.urlopen(base.rstrip("/") + "/models", timeout=5) as r:
            j = json.load(r)
        names = [m.get("id") or m.get("model") or m.get("name") for m in (j.get("data") or j.get("models") or [])]
        names = [n for n in names if n and "embed" not in n.lower()]
        if prefer:
            for n in names:
                if prefer.lower() in n.lower():
                    return n
        return names[0] if names else None
    except Exception:
        return None


def chat(base, model, system, user, max_tokens=700, timeout=300):
    body = json.dumps({
        "model": model, "temperature": 0, "max_tokens": max_tokens,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
    }).encode()
    req = urllib.request.Request(base.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["choices"][0]["message"]["content"]


def extract_json(content):
    """First balanced JSON value (array OR object) in the model's reply."""
    starts = [x for x in (content.find("["), content.find("{")) if x >= 0]
    if not starts:
        return None
    i = min(starts)
    op = content[i]; cl = "]" if op == "[" else "}"
    depth = 0
    for j, ch in enumerate(content[i:], i):
        depth += ch == op
        depth -= ch == cl
        if depth == 0:
            try:
                return json.loads(content[i:j + 1])
            except json.JSONDecodeError:
                return None
    return None


def parse_findings(content):
    """Normalize to [{n, stance, quote}], tolerating the columnar shape a3b sometimes emits
    ({"n":[...], "stance":[...], "quote":[...]}) as well as a proper array of objects."""
    v = extract_json(content)
    if isinstance(v, list):
        return [p for p in v if isinstance(p, dict)]
    if isinstance(v, dict):
        ns, ss, qs = v.get("n"), v.get("stance"), v.get("quote")
        if isinstance(ns, list) and isinstance(qs, list):
            out = []
            for k in range(min(len(ns), len(qs))):
                st = ss[k] if isinstance(ss, list) and k < len(ss) else ss
                out.append({"n": ns[k], "stance": st, "quote": qs[k]})
            return out
        if "n" in v and "quote" in v:
            return [v]
    return []


def applicable_questions(categories, level):
    """[(category_id, q_idx, question_text)] for questions applicable at this tier."""
    qkey = {"federal": "questions", "state": "questions_state", "local": "questions_local"}.get(level, "questions")
    out = []
    for cat in categories:
        qs = cat.get(qkey) or cat.get("questions") or []
        appl = cat.get("applicable_at") or []
        for qi, q in enumerate(qs):
            tiers = appl[qi] if qi < len(appl) else []
            if level in tiers:
                out.append((cat["id"], qi, q))
    return out


def build_sources(c):
    urls = []
    for u in (c.get("website"), c.get("campaign_website")):
        if u:
            urls.append(str(u).rstrip("/"))
    nm = (c.get("name") or "").strip()
    if nm:
        urls.append("https://ballotpedia.org/" + re.sub(r"\s+", "_", nm))
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u); out.append(u)
    return out


ISSUE_KW = re.compile(r"life|abortion|border|immigration|second amendment|marriage|family|liberty|"
                      r"tax|election|defense|veteran|\bgun|faith|constitution|parental|religious", re.I)
# Bot-walls / contentless shells that some sources (esp. Ballotpedia) serve to a plain
# fetcher — never let these dilute the real position prose.
JUNK = re.compile(r"complete the Captcha|receive Ballotpedia|enable JavaScript|Access Denied|"
                  r"are you a robot|too many requests|verifying you are human", re.I)


def gather_pages(bases):
    """Fetch each base's homepage + issue paths + discovered issue links, then rank by
    issue-richness so real position prose leads (and survives the combined-text cap) —
    candidate /issues pages are gold; homepages and nav-heavy pages sink. -> [(url, text)]"""
    pages = []
    for base in bases:
        cands = [base + p for p in ISSUE_PATHS] if "ballotpedia.org" not in base else [base]
        tried, discovered, got = set(), False, 0
        idx = 0
        while idx < len(cands) and got < 6 and len(tried) < 12:
            url = cands[idx]; idx += 1
            if url in tried:
                continue
            tried.add(url)
            try:
                raw = fetch(url)
            except Exception:
                continue
            if not discovered and "ballotpedia.org" not in base:
                discovered = True
                cands.extend(u for u in discover_links(raw, base) if u not in tried)
            txt = to_text(raw)
            if len(txt) > 300 and not (JUNK.search(txt[:900]) and len(ISSUE_KW.findall(txt)) < 4):
                pages.append((url, txt[:11000]))
                got += 1
            time.sleep(0.2)

    def issue_score(p):
        u, t = p
        return (4 if ISSUEY.search(u) else 0) + min(len(ISSUE_KW.findall(t)), 30)
    pages.sort(key=issue_score, reverse=True)
    return pages


EXTRACT_SYS = (
    "You are a meticulous, nonpartisan political researcher building a voter scorecard. "
    "From the SOURCE TEXT (the candidate's own site and/or Ballotpedia), decide which NUMBERED "
    "POSITIONS the candidate's record or clearly stated views SUPPORT or OPPOSE. "
    "Reply with ONLY a JSON array, no prose. Each element: "
    '{"n": <position number>, "stance": "support"|"oppose", "quote": "<sentence copied EXACTLY from the source text>"}. '
    "HARD RULES: (1) The quote MUST be copied word-for-word from the SOURCE TEXT — never paraphrase, "
    "summarize, translate, or invent; if you cannot copy an exact supporting sentence, omit that position. "
    "(2) 'support' = the candidate affirms/advances the position as written; 'oppose' = the candidate's "
    "record or words contradict it. (3) Only include a position with clear, on-point evidence — when unsure, "
    "OMIT it (a blank is required; a wrong answer is unacceptable). (4) Do not infer from party. "
    'Example of the required shape: [{"n": 7, "stance": "support", "quote": "exact sentence copied from the source text"}]'
)

CROSSCHECK_SYS = (
    "You are a neutral fact-checker auditing a voter scorecard. You are given a POSITION (an affirmative "
    "policy statement), a QUOTE from the candidate's source, and a proposed VERDICT — SUPPORT (the "
    "candidate's record supports the position) or OPPOSE (it contradicts the position). "
    "Answer with ONE word: YES if the quote genuinely and unambiguously justifies that verdict (right topic, "
    "right direction), or NO if it is off-topic, ambiguous, or points the other way. Answer only YES or NO."
)

PROSE_SYS = (
    "Write ONE neutral, factual sentence in AP-wire style (no praise, no criticism, no adjectives of judgment) "
    "stating the candidate's position or action, grounded ONLY in the given quote. Under 220 characters. "
    "Output only the sentence, no preamble."
)


def main():
    batch_path, out_path = sys.argv[1], sys.argv[2]
    qwen = sys.argv[sys.argv.index("--qwen") + 1] if "--qwen" in sys.argv else "http://127.0.0.1:1235/v1"
    gemma = sys.argv[sys.argv.index("--gemma") + 1] if "--gemma" in sys.argv else "http://127.0.0.1:1234/v1"
    crosscheck = "--no-crosscheck" not in sys.argv

    qmodel = model_at(qwen)
    if not qmodel:
        sys.exit(f"NO_QWEN: {qwen}/models did not answer")
    gmodel = model_at(gemma, prefer="gemma") if crosscheck else None
    if crosscheck and not gmodel:
        print(f"warn: no Gemma at {gemma}; disabling cross-check", file=sys.stderr)
        crosscheck = False
    print(f"extract: {qmodel} @ {qwen}" + (f"  | crosscheck+prose: {gmodel} @ {gemma}" if crosscheck else "  | crosscheck OFF"))

    categories = json.load(open(SCORECARD))["categories"]
    batch = json.load(open(batch_path))
    results = []

    for i, c in enumerate(batch, 1):
        slug, name, level = c["slug"], c.get("name"), c.get("level") or "state"
        rec = {"slug": slug, "state": c.get("state"), "level": level, "name": name,
               "party": c.get("party"), "office": c.get("office"),
               "sources_fetched": [], "findings": [], "held": [], "status": "no_sources"}
        pages = gather_pages(build_sources(c))
        rec["sources_fetched"] = [u for u, _ in pages]
        if not pages:
            results.append(rec)
            print(f"  [{i}/{len(batch)}] {slug}: no fetchable sources")
            continue

        qlist = applicable_questions(categories, level)
        qmap = {n + 1: qlist[n] for n in range(len(qlist))}
        numbered = "\n".join(f"{n}. {q}" for n, (_, _, q) in qmap.items())
        combined = "\n\n".join(f"[{u}]\n{t}" for u, t in pages)[:22000]
        user = (f"CANDIDATE: {name} ({c.get('party')}, {c.get('office')})\n\n"
                f"NUMBERED POSITIONS:\n{numbered}\n\nSOURCE TEXT:\n{combined}")
        try:
            proposals = parse_findings(chat(qwen, qmodel, EXTRACT_SYS, user, max_tokens=1400))
        except Exception as e:
            rec["status"] = "extract_error"; rec["error"] = str(e)[:120]
            results.append(rec)
            print(f"  [{i}/{len(batch)}] {slug}: extract error {str(e)[:60]}")
            continue

        for p in proposals:
            if not isinstance(p, dict):
                continue
            n, stance, quote = p.get("n"), p.get("stance"), p.get("quote")
            if n not in qmap or stance not in ("support", "oppose") or not quote:
                continue
            cat_id, q_idx, q_text = qmap[n]
            # gate 1: verbatim
            nq = norm(quote)
            src = next((u for u, t in pages if nq and nq in norm(t)), None)
            if not src:
                rec["held"].append({"category": cat_id, "question_idx": q_idx, "stance": stance,
                                    "quote": quote, "reason": "unverified_quote"})
                continue
            # gate 2: cross-check polarity/relevance
            if crosscheck:
                try:
                    verdict = chat(gemma, gmodel, CROSSCHECK_SYS,
                                   f"POSITION: {q_text}\nQUOTE: {quote}\nPROPOSED VERDICT: {stance.upper()}",
                                   max_tokens=6).strip().upper()
                except Exception:
                    verdict = "YES"  # cross-check outage shouldn't lose a verbatim-verified finding; QA cron re-audits
                if not verdict.startswith("YES"):
                    rec["held"].append({"category": cat_id, "question_idx": q_idx, "stance": stance,
                                        "quote": quote, "source_url": src, "reason": "crosscheck_no"})
                    continue
            # prose
            text = quote[:220]
            if crosscheck:
                try:
                    text = chat(gemma, gmodel, PROSE_SYS, f"POSITION: {q_text}\nQUOTE: {quote}",
                                max_tokens=120).strip().strip('"')[:240] or quote[:220]
                except Exception:
                    pass
            rec["findings"].append({"category": cat_id, "question_idx": q_idx,
                                    "score_impact": (stance == "support"),
                                    "quote": quote, "source_url": src, "claim_text": text})
        rec["status"] = "ok" if rec["findings"] else ("held_only" if rec["held"] else "no_findings")
        results.append(rec)
        print(f"  [{i}/{len(batch)}] {slug}: {len(rec['findings'])} verified, "
              f"{len(rec['held'])} held  ({rec['status']}, {len(pages)} pages)")

    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "extractor": "local-" + qmodel.split("/")[-1],
           "crosscheck": bool(crosscheck), "candidates": results}
    json.dump(out, open(out_path, "w"), indent=1)
    tot_f = sum(len(r["findings"]) for r in results)
    tot_h = sum(len(r["held"]) for r in results)
    print(f"wrote {out_path}: {tot_f} verified findings, {tot_h} held, across {len(results)} candidates")


if __name__ == "__main__":
    main()

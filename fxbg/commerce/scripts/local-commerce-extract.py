#!/usr/bin/env python3
"""Local LLM commerce evidence extraction — verbatim-gated (v0.4).

Fetches each business official site, asks local Qwen for rubric-aligned quotes,
optionally Gemma cross-check. Only VERIFIED quotes become findings.

Usage: local-commerce-extract.py BATCH.json OUT.json [--llm URL] [--no-crosscheck]
"""
from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

UA = {"User-Agent": "C5iSR-CommerceBot/0.4 (+https://usmcmin.com/fxbg/commerce/)"}
CTX = ssl.create_default_context()
DEFAULT_LLM = "http://127.0.0.1:1234/v1"

FACTORS = {
    "financial_integrity": "Licensed, bonded, insured, 501(c)(3), transparent pricing, BBB/regulator signals.",
    "christ_centered_brand": "Explicit Christ-centered / faith-based / gospel / Christian-owned public brand.",
    "community_fruit": "Local employer, community service, charity, long tenure, chamber/community role.",
    "worker_dignity": "Fair wages, benefits, best places to work, documented employment practices.",
}

SYSTEM = """You extract ONLY verbatim quotes from the provided page text for a Fredericksburg VA business directory.
Return JSON array (max 4 items). Each item:
{"factor":"financial_integrity|christ_centered_brand|community_fruit|worker_dignity",
 "band":"green|yellow",
 "quote":"exact substring from page text",
 "note":"one neutral sentence"}
Rules: quote MUST be copy-paste exact from PAGE TEXT. No inference. If nothing fits, return [].
Green = clear affirmative. Yellow = caution/concern only if page explicitly warns or conflicts."""


def fetch(url: str, timeout: int = 14) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read(400_000).decode("utf-8", "replace")


def to_text(html: str) -> str:
    html = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    import html as h

    return re.sub(r"\s+", " ", h.unescape(html)).strip()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def model_at(base: str, prefer: str | None = None) -> str | None:
    try:
        with urllib.request.urlopen(base.rstrip("/") + "/models", timeout=8) as r:
            j = json.load(r)
        names = [m.get("id") or m.get("model") for m in (j.get("data") or [])]
        names = [n for n in names if n and "embed" not in n.lower()]
        if prefer:
            for n in names:
                if prefer.lower() in n.lower():
                    return n
        return names[0] if names else None
    except Exception:
        return None


def chat(base: str, model: str, user: str, max_tokens: int = 600) -> str:
    body = json.dumps(
        {
            "model": model,
            "temperature": 0,
            "max_tokens": max_tokens,
            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        }
    ).encode()
    req = urllib.request.Request(
        base.rstrip("/") + "/chat/completions",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
        return json.load(r)["choices"][0]["message"]["content"]


def parse_findings(raw: str) -> list[dict]:
    raw = raw.strip()
    m = re.search(r"\[[\s\S]*\]", raw)
    if not m:
        return []
    try:
        arr = json.loads(m.group(0))
        return arr if isinstance(arr, list) else []
    except json.JSONDecodeError:
        return []


def verbatim_ok(quote: str, page_text: str) -> bool:
    if not quote or len(quote) < 12:
        return False
    return norm(quote) in norm(page_text)


def crosscheck(base: str, model: str, factor: str, quote: str, band: str) -> bool:
    prompt = (
        f"Factor: {factor}\nBand proposed: {band}\nQuote: {quote}\n"
        "Reply YES if the quote directly supports this factor and band; else NO."
    )
    try:
        ans = chat(base, model, prompt, max_tokens=8).strip().upper()
        return ans.startswith("YES")
    except Exception:
        return False


def process_one(base: str, qwen: str, gemma: str | None, item: dict, cross: bool) -> dict:
    url = (item.get("web") or "").strip()
    out = {**item, "findings": [], "fetch_error": None}
    if not url.startswith("http"):
        out["fetch_error"] = "no_url"
        return out
    try:
        page_text = to_text(fetch(url))
    except Exception as e:
        out["fetch_error"] = str(e)[:200]
        return out
    if len(page_text) < 80:
        out["fetch_error"] = "thin_page"
        return out
    user = f"BUSINESS: {item.get('name')}\nURL: {url}\nGRAY FACTORS: {item.get('gray_factors')}\n\nPAGE TEXT:\n{page_text[:12000]}"
    try:
        raw = chat(base, qwen, user)
    except Exception as e:
        out["fetch_error"] = f"llm:{e}"[:200]
        return out
    verified = []
    for f in parse_findings(raw):
        factor = f.get("factor")
        quote = (f.get("quote") or "").strip()
        band = (f.get("band") or "green").lower()
        if factor not in FACTORS or band not in ("green", "yellow"):
            continue
        if factor not in (item.get("gray_factors") or []):
            continue
        if not verbatim_ok(quote, page_text):
            continue
        if cross and gemma and not crosscheck(base, gemma, factor, quote, band):
            continue
        verified.append(
            {
                "factor": factor,
                "band": band,
                "quote": quote,
                "note": (f.get("note") or "")[:300],
                "source_url": url,
            }
        )
    out["findings"] = verified
    return out


def main() -> None:
    args = sys.argv[1:]
    if len(args) < 2:
        print("usage: local-commerce-extract.py BATCH.json OUT.json [--llm URL] [--no-crosscheck]", file=sys.stderr)
        sys.exit(2)
    batch_path, out_path = args[0], args[1]
    llm = DEFAULT_LLM
    cross = True
    i = 2
    while i < len(args):
        if args[i] == "--llm" and i + 1 < len(args):
            llm = args[i + 1]
            i += 2
        elif args[i] == "--no-crosscheck":
            cross = False
            i += 1
        else:
            i += 1

    batch = json.loads(Path(batch_path).read_text())
    qwen = model_at(llm, "qwen") or model_at(llm)
    gemma = model_at(llm, "gemma") if cross else None
    if not qwen:
        print("no chat model at", llm, file=sys.stderr)
        sys.exit(1)

    results = []
    for item in batch:
        results.append(process_one(llm, qwen, gemma, item, cross))

    payload = {"businesses": results, "llm": llm, "model": qwen}
    Path(out_path).write_text(json.dumps(payload, indent=2))
    n_find = sum(len(r.get("findings") or []) for r in results)
    print(f"wrote {out_path}: {len(results)} businesses, {n_find} verified finding(s)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify business web URLs and refresh digital_integrity scores (v0.4)."""
from __future__ import annotations

import json
import ssl
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "businesses.json"

UA = "C5iSR-CommerceBot/0.4 (+https://usmcmin.com/fxbg/commerce/)"
TIMEOUT = 12
WORKERS = 8


def probe(url: str) -> dict:
    if not url or not url.startswith("http"):
        return {"status": None, "final_url": url, "error": "no_url"}
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            return {
                "status": resp.status,
                "final_url": resp.geturl(),
                "error": None,
            }
    except urllib.error.HTTPError as e:
        if e.code in (405, 403, 501):
            return probe_get(url)
        return {"status": e.code, "final_url": url, "error": str(e.code)}
    except Exception as e:
        return probe_get(url) if "405" in str(e) else {"status": None, "final_url": url, "error": str(e)[:120]}


def probe_get(url: str) -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            return {"status": resp.status, "final_url": resp.geturl(), "error": None}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "final_url": url, "error": str(e.code)}
    except Exception as e:
        return {"status": None, "final_url": url, "error": str(e)[:120]}


def band_from_probe(probe_result: dict, has_phone: bool) -> tuple[str, dict]:
    status = probe_result.get("status")
    err = probe_result.get("error")
    if status and 200 <= status < 400:
        band = "green"
        reason = "verified"
    elif status in (401, 403, 429):
        band = "yellow"
        reason = "reach_blocked"
    elif status and status >= 400:
        band = "yellow" if has_phone else "gray"
        reason = "http_error"
    elif has_phone:
        band = "yellow"
        reason = "site_unreachable_phone_ok"
    else:
        band = "gray"
        reason = "unreachable"
    meta = {
        "band": band,
        "reason": reason,
        "source_count": 1 if band == "green" else 0,
        "concern_count": 1 if band == "yellow" else 0,
        "verified": date.today().isoformat(),
        "http_status": status,
        "error": err,
    }
    return band, meta


def main() -> None:
    data = json.loads(DATA.read_text())
    businesses = data.get("businesses") or []
    urls = {b.get("slug"): (b.get("web") or "").strip() for b in businesses if b.get("slug")}

    probes: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = {pool.submit(probe, u): slug for slug, u in urls.items() if u}
        for fut in as_completed(futs):
            probes[futs[fut]] = fut.result()

    changes = {"green": 0, "yellow": 0, "gray": 0, "unchanged": 0, "dead_sites": 0}
    for biz in businesses:
        slug = biz.get("slug")
        scores = biz.setdefault("scores", {})
        old = scores.get("digital_integrity", "gray")
        url = (biz.get("web") or "").strip()
        if not url:
            band, meta = "gray", {
                "band": "gray",
                "reason": "no_url",
                "source_count": 0,
                "concern_count": 0,
                "verified": date.today().isoformat(),
            }
        else:
            pr = probes.get(slug) or probe(url)
            band, meta = band_from_probe(pr, bool(biz.get("phone")))
            if pr.get("status") is None and not biz.get("phone"):
                changes["dead_sites"] += 1
        scores["digital_integrity"] = band
        scores["digital_integrity_meta"] = meta
        if old == band:
            changes["unchanged"] += 1
        else:
            changes[band] += 1
        biz["updated"] = date.today().isoformat()

    data["digital_verify_pass"] = date.today().isoformat()
    DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print("digital integrity pass", date.today().isoformat())
    print("probed", len(probes), "urls")
    print("changes toward", {k: v for k, v in changes.items() if v and k != "unchanged"})
    print("unchanged", changes["unchanged"])


if __name__ == "__main__":
    main()

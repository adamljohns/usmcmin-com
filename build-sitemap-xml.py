#!/usr/bin/env python3
"""Generate sitemap.xml from the actual HTML file inventory.

Categorizes pages so search engines see the right priorities:
  1.0  homepage
  0.9  primary commerce hubs (mission, coaching, books, shop, about)
  0.8  sub-brand index/landing pages
  0.7  sub-brand detail pages, RESOLUTE Citizen scorecard hubs
  0.6  fitness cert pages, council notes
  0.5  individual candidate profiles (bulk)
  0.4  individual issue pages
Operations dashboards (auth-gated) are excluded — they live in robots.txt Disallow.
"""
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
BASE_URL = "https://usmcmin.com"
TODAY = date.today().isoformat()

# Auth-gated pages — exclude from sitemap, also disallowed in robots.txt
EXCLUDE = {
    "bow-arrow/dashboard.html", "bow-arrow/booking.html",
    "bow-arrow/calendar.html", "bow-arrow/cleaning.html",
    "bow-arrow/comms.html", "bow-arrow/financials.html",
    "bow-arrow/guests.html", "bow-arrow/maintenance.html",
    "c5isr/dashboard.html",
    "finance/financial-command.html", "finance/stewardship-dashboard.html",
}

# Priority overrides for high-value pages
HIGH_PRIORITY = {
    "index.html": (1.0, "weekly"),
    "mission.html": (0.9, "monthly"),
    "coaching.html": (0.9, "monthly"),
    "consulting.html": (0.9, "monthly"),
    "books.html": (0.9, "monthly"),
    "shop.html": (0.9, "monthly"),
    "about.html": (0.9, "monthly"),
    "pricing.html": (0.8, "monthly"),
    "direct-booking.html": (0.8, "monthly"),
    "father.html": (0.8, "monthly"),
    "husband.html": (0.8, "monthly"),
    "citizen.html": (0.8, "weekly"),
    "citizen-table.html": (0.8, "weekly"),
    "citizen-issues.html": (0.7, "weekly"),
    "council-notes.html": (0.6, "weekly"),
    "sitemap.html": (0.5, "monthly"),
    "bow-arrow/index.html": (0.7, "monthly"),
    "c5isr/index.html": (0.7, "monthly"),
    "finance/finance.html": (0.7, "monthly"),
    "finance/financial-intake.html": (0.8, "monthly"),
    "finance/financial-onboarding.html": (0.6, "monthly"),
    "finance/consulting.html": (0.7, "monthly"),
    "fitness/fitness.html": (0.8, "monthly"),
    "fitness/trainer.html": (0.7, "monthly"),
    "melaleuca/index.html": (0.7, "monthly"),
}

def priority_for(rel: str) -> tuple[float, str]:
    if rel in HIGH_PRIORITY:
        return HIGH_PRIORITY[rel]
    if rel.startswith("fitness/cert-"):
        return (0.6, "monthly")
    if rel.startswith("candidates/"):
        return (0.5, "monthly")
    if rel.startswith("issues/"):
        return (0.4, "monthly")
    return (0.5, "monthly")

def collect():
    urls = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".") or rel in EXCLUDE:
            continue
        # Skip the redirect-only stubs — sitemap should point to canonical URLs
        if rel in {"scorecard.html", "scorecard-table.html"}:
            continue
        prio, freq = priority_for(rel)
        urls.append((rel, prio, freq))
    return urls

def render(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for rel, prio, freq in urls:
        loc = f"{BASE_URL}/{rel}" if rel != "index.html" else f"{BASE_URL}/"
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{prio:.1f}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    urls = collect()
    out = ROOT / "sitemap.xml"
    out.write_text(render(urls))
    print(f"Wrote {out} with {len(urls)} URLs")

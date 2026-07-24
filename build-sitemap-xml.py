#!/usr/bin/env python3
"""Generate sitemap.xml index and sitemap shards from the HTML inventory.

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
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
BASE_URL = "https://usmcmin.com"
TODAY = date.today().isoformat()
MAX_URLS_PER_SHARD = 5000

# Auth-gated / private pages — exclude from sitemap, also disallowed in robots.txt.
# Criteria: page shows personal finances, booking ops data, or the login page itself.
# bow-arrow/booking.html and bow-arrow/guests.html are PUBLIC (direct-book + guest info).
EXCLUDE = {
    # Finance dashboards (personal / family financial data)
    "finance/finance.html",
    "finance/financial-command.html",
    "finance/financial-onboarding.html",
    "finance/stewardship-dashboard.html",
    # Crypto dashboard (shows positions)
    "c5isr/dashboard.html",
    # Bow & Arrow ops (internal; shows revenue, expenses, guest data)
    "bow-arrow/dashboard.html",
    "bow-arrow/calendar.html",
    "bow-arrow/cleaning.html",
    "bow-arrow/comms.html",
    "bow-arrow/financials.html",
    "bow-arrow/maintenance.html",
    # Login page itself — no SEO value
    "bow-arrow/login.html",
    # Cohort feed preview — gives away upcoming Telegram posts; keep unindexed
    "ai-boot-camp-heartbeat.html",
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
        # AI Boot Camp — main URL is /ai-boot-camp.html.
    # Bump priority to 0.8 when actively recruiting.
    "ai-boot-camp.html": (0.6, "monthly"),
    "ai-boot-camp-tools.html": (0.5, "monthly"),
    # ai-boot-camp-heartbeat.html intentionally excluded from sitemap —
    # noindex,nofollow on the page itself; URL stays alive for direct links.
    "citizen.html": (0.9, "weekly"),
    "citizen-table.html": (0.8, "weekly"),
    "citizen-issues.html": (0.7, "weekly"),
    "citizen-rankings.html": (0.9, "daily"),     # live A-F leaderboard — primary CTA
    "find-my-reps.html": (0.9, "weekly"),
    "scoring-system.html": (0.85, "monthly"),    # rubric explainer
    "methodology-foreign-influence.html": (0.75, "monthly"),
    "petition.html": (0.8, "monthly"),
    "compare.html": (0.7, "weekly"),
    "races/index.html": (0.85, "weekly"),
    "council-notes.html": (0.6, "weekly"),
    "sitemap.html": (0.5, "monthly"),
    "bow-arrow/index.html": (0.7, "monthly"),
    "c5isr/index.html": (0.7, "monthly"),
    "finance/index.html": (0.8, "monthly"),
    "finance/finance.html": (0.5, "monthly"),
    "finance/financial-intake.html": (0.8, "monthly"),
    "finance/financial-onboarding.html": (0.6, "monthly"),
    "finance/consulting.html": (0.7, "monthly"),
    "fitness/index.html": (0.85, "monthly"),
    "fitness/fitness-intake.html": (0.8, "monthly"),
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
    if rel.startswith("races/"):
        return (0.8, "weekly")
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
        if rel in {"scorecard.html", "scorecard-table.html", "fitness/fitness.html", "resolute.html", "resolute/index.html"}:
            continue
        prio, freq = priority_for(rel)
        urls.append((rel, prio, freq))
    return urls

def loc_for(rel: str) -> str:
    return f"{BASE_URL}/{rel}" if rel != "index.html" else f"{BASE_URL}/"

def shard_name(kind: str, suffix: str | None = None) -> str:
    if suffix:
        return f"sitemap-{kind}-{suffix}.xml"
    return f"sitemap-{kind}.xml"

def shard_key(rel: str) -> str:
    if rel.startswith("candidates/"):
        parts = rel.split("/")
        state = parts[1] if len(parts) > 2 else "misc"
        return f"candidates-{state}"
    if rel.startswith("races/"):
        return "races"
    if rel.startswith("issues/"):
        return "issues"
    return "navigation"

def shard_urls(urls):
    grouped = {}
    for item in urls:
        grouped.setdefault(shard_key(item[0]), []).append(item)

    shards = []
    for key in sorted(grouped):
        items = grouped[key]
        if len(items) <= MAX_URLS_PER_SHARD:
            shards.append((shard_name(key), items))
            continue
        for index in range(0, len(items), MAX_URLS_PER_SHARD):
            chunk = items[index:index + MAX_URLS_PER_SHARD]
            shards.append((shard_name(key, f"{index // MAX_URLS_PER_SHARD + 1:03d}"), chunk))
    return shards

def render_urlset(urls):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for rel, prio, freq in urls:
        lines += [
            "  <url>",
            f"    <loc>{loc_for(rel)}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{prio:.2f}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"

def render_index(shards):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for filename, _urls in shards:
        lines += [
            "  <sitemap>",
            f"    <loc>{BASE_URL}/{filename}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            "  </sitemap>",
        ]
    lines.append("</sitemapindex>")
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    urls = collect()
    shards = shard_urls(urls)

    # Remove old generated shard files so renamed/deleted states do not linger.
    for old in ROOT.glob("sitemap-*.xml"):
        old.unlink()

    for filename, shard in shards:
        (ROOT / filename).write_text(render_urlset(shard))

    out = ROOT / "sitemap.xml"
    out.write_text(render_index(shards))
    print(f"Wrote {out} with {len(urls)} URLs across {len(shards)} shards")

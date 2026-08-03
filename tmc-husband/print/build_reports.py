#!/usr/bin/env python3
"""
build_reports.py — turn the twenty-one study reports into branded PDFs.

    python3 tmc-husband/print/build_reports.py

The reports arrive from Notebook by Gemini as Markdown. Markdown is a source
format, not a reading format: a man who taps "Read the report" on his phone
should not get raw `##` and `|---|` in a monospace wall. This lays each report
out as a proper document in the course's type and color — cover block, running
heads, real tables, pull quotes — and writes it beside the source file.

The Markdown stays in the repo as the source of truth; only the PDF is linked
from the site. Rebuild any time with the command above.
"""

import os
import re
import sys

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import (  # noqa: E402
    Sheet, cover, wrap, ascii_safe,
    MODULE_ACCENTS, NAVY, INK, GRAY, GRAY_LT, WARM, BORDER, WARM as PANEL,
    SERIF, SERIF_B, SERIF_I, SANS, SANS_B, SANS_I,
    ML, MR, MT, MB, USABLE_W, W, H, REPO, COURSE_NAME, MINISTRY,
)

MEDIA = os.path.join(REPO, "assets", "media", "tmc-husband")

# ── Markdown → block list ───────────────────────────────────────────────────
INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITAL = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def strip_inline(text):
    """Markdown emphasis is decoration in these documents, not semantics —
    drop the syntax and keep the words. (Bold-as-lead-in survives as the
    sentence it already is.)"""
    text = LINK.sub(r"\1", text)
    text = INLINE_BOLD.sub(r"\1", text)
    text = INLINE_ITAL.sub(r"\1", text)
    text = INLINE_CODE.sub(r"\1", text)
    return ascii_safe(text.strip())


def parse_markdown(md):
    blocks = []
    lines = md.replace("\r\n", "\n").split("\n")
    i = 0
    para = []

    def flush():
        if para:
            blocks.append(("p", " ".join(para).strip()))
            para.clear()

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            flush()
            i += 1
            continue

        if set(stripped) <= {"-", "*", "_"} and len(stripped) >= 3:
            flush()
            blocks.append(("hr", ""))
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush()
            blocks.append((f"h{len(m.group(1))}", strip_inline(m.group(2))))
            i += 1
            continue

        if stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            blocks.append(("quote", strip_inline(" ".join(quote))))
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            flush()
            header = [strip_inline(c) for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([strip_inline(c) for c in lines[i].strip().strip("|").split("|")])
                i += 1
            blocks.append(("table", (header, rows)))
            continue

        m = re.match(r"^[*\-+]\s+(.*)$", stripped)
        if m:
            flush()
            items = []
            while i < len(lines):
                mm = re.match(r"^[*\-+]\s+(.*)$", lines[i].strip())
                if not mm:
                    # A wrapped continuation line belongs to the last bullet.
                    if items and lines[i].startswith(("    ", "\t")) and lines[i].strip():
                        items[-1] += " " + strip_inline(lines[i].strip())
                        i += 1
                        continue
                    break
                items.append(strip_inline(mm.group(1)))
                i += 1
            blocks.append(("ul", items))
            continue

        m = re.match(r"^(\d+)[.)]\s+(.*)$", stripped)
        if m:
            flush()
            items = []
            while i < len(lines):
                mm = re.match(r"^(\d+)[.)]\s+(.*)$", lines[i].strip())
                if not mm:
                    break
                items.append(strip_inline(mm.group(2)))
                i += 1
            blocks.append(("ol", items))
            continue

        para.append(strip_inline(stripped))
        i += 1

    flush()
    return blocks


# ── Layout ──────────────────────────────────────────────────────────────────
def draw_table(sheet, header, rows, accent):
    """Two- and three-column tables, sized to content, split across pages with
    the header repeated."""
    c = sheet.c
    ncols = max(len(header), max((len(r) for r in rows), default=0)) or 1
    if ncols == 2:
        widths = [USABLE_W * 0.30, USABLE_W * 0.70]
    elif ncols == 3:
        widths = [USABLE_W * 0.24, USABLE_W * 0.38, USABLE_W * 0.38]
    else:
        widths = [USABLE_W / ncols] * ncols
    pad = 7
    size = 9.0
    leading = 12.4

    def row_height(cells):
        h = 0
        for idx, cell in enumerate(cells[:ncols]):
            lines = wrap(c, cell, SANS, size, widths[idx] - 2 * pad)
            h = max(h, len(lines) * leading)
        return h + 2 * pad

    def draw_row(cells, y, bold=False, fill=None):
        h = row_height(cells)
        if fill:
            c.setFillColor(fill)
            c.rect(ML, y - h, USABLE_W, h, stroke=0, fill=1)
        x = ML
        for idx in range(ncols):
            cell = cells[idx] if idx < len(cells) else ""
            lines = wrap(c, cell, SANS_B if bold else SANS, size, widths[idx] - 2 * pad)
            ty = y - pad - size
            for line in lines:
                c.setFillColor(NAVY if bold else INK)
                c.setFont(SANS_B if bold else SANS, size)
                c.drawString(x + pad, ty, line)
                ty -= leading
            x += widths[idx]
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.line(ML, y - h, ML + USABLE_W, y - h)
        return h

    sheet.need(row_height(header) + 40)
    top = sheet.y
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(ML, top, ML + USABLE_W, top)
    sheet.y -= draw_row(header, sheet.y, bold=True, fill=WARM)
    for row in rows:
        if sheet.y - row_height(row) < MB:
            # column rules for the part already drawn
            sheet.new_page()
            top = sheet.y
            c.setStrokeColor(BORDER)
            c.line(ML, top, ML + USABLE_W, top)
            sheet.y -= draw_row(header, sheet.y, bold=True, fill=WARM)
        sheet.y -= draw_row(row, sheet.y)
    sheet.y -= 12


def render_report(md_path, out_path, module_number, module_title, accent):
    with open(md_path, "r", encoding="utf-8") as fh:
        blocks = parse_markdown(fh.read())

    # The first h1 is the document title; the first paragraph is its standfirst.
    title = None
    standfirst = None
    body = []
    for kind, value in blocks:
        if title is None and kind == "h1":
            title = value
            continue
        if title is not None and standfirst is None and kind == "p":
            standfirst = value
            continue
        body.append((kind, value))
    title = title or os.path.basename(md_path).replace("-", " ").replace(".md", "").title()

    c = canvas.Canvas(out_path, pagesize=(W, H), pageCompression=1)
    c.setTitle(f"{title} — {COURSE_NAME}")
    c.setAuthor(MINISTRY)
    c.setSubject(f"Module {module_number}: {module_title} — study report")

    footer = f"{COURSE_NAME} · Module {module_number} · {MINISTRY}"
    sheet = Sheet(c, footer, accent=accent)
    cover(
        sheet,
        f"Module {module_number} · {module_title} · Study report",
        title,
        standfirst,
        accent,
        meta_lines=[
            "Optional study aid generated with Notebook by Gemini from thematically related research.",
            "It reflects the source material, not U.S.M.C. Ministries doctrine — read it against the module.",
        ],
    )

    for kind, value in body:
        if kind == "h1":
            sheet.heading(value, size=18, color=NAVY, space_before=8)
        elif kind == "h2":
            sheet.rule(color=HexColor(accent), width=1.2, gap_before=6, gap_after=10)
            sheet.heading(value, size=14.5, color=NAVY, space_before=0, space_after=6)
        elif kind == "h3":
            sheet.subheading(value, size=11.5)
        elif kind in ("h4", "h5", "h6"):
            sheet.kicker(value, color=HexColor(accent))
        elif kind == "p":
            sheet.body(value, size=9.8, leading=13.8, gap=9)
        elif kind == "ul":
            for item in value:
                sheet.bullet(item)
            sheet.space(4)
        elif kind == "ol":
            for idx, item in enumerate(value, 1):
                sheet.bullet(item, glyph=f"{idx}.")
            sheet.space(4)
        elif kind == "quote":
            sheet.quote(value)
        elif kind == "table":
            draw_table(sheet, value[0], value[1], accent)
        elif kind == "hr":
            sheet.space(4)

    sheet.finish()
    c.save()
    return out_path


def main():
    import json
    export = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "course-export.json")))
    by_number = {m["number"]: m for m in export["modules"]}

    built = 0
    for number in sorted(by_number):
        module = by_number[number]
        accent = MODULE_ACCENTS[number]
        reports_dir = os.path.join(MEDIA, f"m{number:02d}", "reports")
        if not os.path.isdir(reports_dir):
            continue
        for name in sorted(os.listdir(reports_dir)):
            if not name.endswith(".md"):
                continue
            md_path = os.path.join(reports_dir, name)
            out_path = md_path[:-3] + ".pdf"
            render_report(md_path, out_path, number, module["title"], accent)
            built += 1
            print(f"  m{number:02d}  {os.path.basename(out_path)}  ({os.path.getsize(out_path) // 1024} KB)")
    print(f"{built} report PDFs written.")


if __name__ == "__main__":
    main()

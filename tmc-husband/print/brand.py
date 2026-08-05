#!/usr/bin/env python3
"""
brand.py — the print brand kit for The Husband Course, in The Marriage Academy.

Everything printable in this course (the field workbook, the seven module
inserts, and the twenty-one reading PDFs) is drawn with these helpers, so the
whole pack looks like one product and like usmcmin.com.

Type:      Playfair Display for display and headings (same face the site uses,
           OFL-licensed so it embeds cleanly), Helvetica for form text and
           small print.
Color:     the module accents are the SAME light-theme values the site uses in
           tmc-husband/generate.js MODULE_ACCENTS, so a printed module and the
           web module carry one identity.
Rules:     muted, no neon, WCAG-grade contrast, no meaning in hue alone —
           every colored band also carries its module number in words.

Run nothing here directly; import it.
"""

import os

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
FONT_DIR = os.path.join(HERE, "fonts")

# ── Type ────────────────────────────────────────────────────────────────────
# Static instances cut from the variable Playfair Display (see README in this
# folder). Registration is idempotent so multiple builders can import freely.
SERIF = "Playfair"
SERIF_B = "Playfair-Bold"
SERIF_I = "Playfair-Italic"
SANS = "Helvetica"
SANS_B = "Helvetica-Bold"
SANS_I = "Helvetica-Oblique"


def register_fonts():
    if SERIF in pdfmetrics.getRegisteredFontNames():
        return
    pdfmetrics.registerFont(TTFont(SERIF, os.path.join(FONT_DIR, "PlayfairDisplay-Regular.ttf")))
    pdfmetrics.registerFont(TTFont(SERIF_B, os.path.join(FONT_DIR, "PlayfairDisplay-Bold.ttf")))
    pdfmetrics.registerFont(TTFont(SERIF_I, os.path.join(FONT_DIR, "PlayfairDisplay-Italic.ttf")))
    pdfmetrics.registerFontFamily(SERIF, normal=SERIF, bold=SERIF_B, italic=SERIF_I, boldItalic=SERIF_B)


register_fonts()

# ── Palette ─────────────────────────────────────────────────────────────────
NAVY = HexColor("#1E3A5F")     # USMC navy — headings and rules
INK = HexColor("#1A1A1A")
GRAY = HexColor("#4B5563")
GRAY_LT = HexColor("#6B7280")
PAPER = HexColor("#FFFFFF")
WARM = HexColor("#F4F5F7")     # panel fill (site --bg-card)
BORDER = HexColor("#D1D5DB")   # site --border
RULE = HexColor("#E6E8EC")     # faint notebook rules inside a field
FIELD_BG = HexColor("#FBFAF7")  # pale fill so a field reads as "type here"
FIELD_EDGE = HexColor("#C9C4B8")
ALERT = HexColor("#A03127")

# Module accents — light-theme values from tmc-husband/generate.js.
MODULE_ACCENTS = {
    1: "#8C5A1F",  # Foundation — bronze
    2: "#2C6E8A",  # Communication — harbor
    3: "#4C6B2F",  # Conflict — olive
    4: "#9B4A3F",  # Repair — clay
    5: "#5B5A8C",  # Family roots — slate violet
    6: "#8A3F62",  # Intimacy — deep rose
    7: "#1E4E6B",  # Love in action — navy blue
}
NEUTRAL_ACCENT = "#4A5568"

WORDED_NUMBER = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
}

# ── Page geometry ───────────────────────────────────────────────────────────
W, H = LETTER
ML = 0.85 * inch
MR = 0.85 * inch
MT = 0.82 * inch
MB = 0.72 * inch
USABLE_W = W - ML - MR

COURSE_NAME = "The Husband Course · The Marriage Academy"
MINISTRY = "U.S.M.C. Ministries"

def ascii_safe(s):
    """Playfair covers the smart punctuation we use, but form-field text and
    Helvetica fall back to WinAnsi — normalize so nothing prints as a box."""
    if not s:
        return ""
    repl = {
        "—": "—", "–": "–",  # keep real dashes (Playfair has them)
        "&mdash;": "—", "&ndash;": "–", "&rsquo;": "’",
        "&lsquo;": "‘", "&ldquo;": "“", "&rdquo;": "”",
        "&amp;": "&", "&middot;": "·", "&hellip;": "…",
        "&uarr;": "", "&darr;": "", "&check;": "", "&nbsp;": " ",
        "→": "->", "↑": "", " ": " ",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    return s


def wrap(c, text, font, size, max_w):
    """Greedy word wrap against real string widths."""
    text = ascii_safe(text)
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if c.stringWidth(trial, font, size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            # A single word longer than the column (a URL) gets hard-split.
            while c.stringWidth(word, font, size) > max_w and len(word) > 1:
                cut = len(word)
                while cut > 1 and c.stringWidth(word[:cut], font, size) > max_w:
                    cut -= 1
                lines.append(word[:cut])
                word = word[cut:]
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


class Sheet:
    """A page the builders draw down. Owns the cursor, page breaks, footer."""

    def __init__(self, canvas_obj, footer_text, accent=NEUTRAL_ACCENT, start_page=1):
        self.c = canvas_obj
        self.y = H - MT
        self.page = start_page
        self.footer_text = footer_text
        self.accent = HexColor(accent) if isinstance(accent, str) else accent

    # ── page plumbing ──
    def footer(self):
        c = self.c
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.line(ML, 0.62 * inch, ML + USABLE_W, 0.62 * inch)
        c.setFont(SANS, 7.6)
        c.setFillColor(GRAY_LT)
        c.drawString(ML, 0.45 * inch, ascii_safe(self.footer_text))
        c.drawRightString(ML + USABLE_W, 0.45 * inch, str(self.page))

    def new_page(self):
        self.footer()
        self.c.showPage()
        self.page += 1
        self.y = H - MT

    def need(self, height):
        """Break to a new page unless `height` still fits."""
        if self.y - height < MB:
            self.new_page()
            return True
        return False

    def finish(self):
        self.footer()
        self.c.showPage()

    def space(self, amount):
        self.y -= amount

    # ── text ──
    def kicker(self, text, color=None):
        self.need(24)
        self.c.setFont(SANS_B, 7.8)
        self.c.setFillColor(color or self.accent)
        self.c.drawString(ML, self.y - 8, ascii_safe(text).upper())
        self.y -= 20

    def heading(self, text, size=17, color=NAVY, space_before=6, space_after=10):
        self.y -= space_before
        lines = wrap(self.c, text, SERIF_B, size, USABLE_W)
        self.need(len(lines) * (size + 4) + space_after)
        self.c.setFillColor(color)
        self.c.setFont(SERIF_B, size)
        for line in lines:
            self.c.drawString(ML, self.y - size, line)
            self.y -= size + 4
        self.y -= space_after

    def subheading(self, text, size=11.5):
        lines = wrap(self.c, text, SERIF_B, size, USABLE_W)
        self.need(len(lines) * (size + 3) + 6)
        self.c.setFillColor(NAVY)
        self.c.setFont(SERIF_B, size)
        for line in lines:
            self.c.drawString(ML, self.y - size, line)
            self.y -= size + 3
        self.y -= 5

    def body(self, text, size=9.8, color=INK, font=SANS, indent=0, leading=13.6, gap=8):
        lines = wrap(self.c, text, font, size, USABLE_W - indent)
        for line in lines:
            self.need(leading)
            self.c.setFillColor(color)
            self.c.setFont(font, size)
            self.c.drawString(ML + indent, self.y - size, line)
            self.y -= leading
        self.y -= gap

    def bullet(self, text, size=9.8, glyph="•"):
        indent = 14
        lines = wrap(self.c, text, SANS, size, USABLE_W - indent)
        for i, line in enumerate(lines):
            self.need(13.4)
            self.c.setFillColor(self.accent if i == 0 else INK)
            self.c.setFont(SANS_B if i == 0 else SANS, size)
            if i == 0:
                self.c.drawString(ML + 2, self.y - size, glyph)
            self.c.setFillColor(INK)
            self.c.setFont(SANS, size)
            self.c.drawString(ML + indent, self.y - size, line)
            self.y -= 13.4
        self.y -= 3

    def quote(self, text, size=10):
        lines = wrap(self.c, text, SERIF_I, size, USABLE_W - 28)
        self.need(len(lines) * 14 + 14)
        top = self.y
        self.c.setFillColor(INK)
        for line in lines:
            self.c.setFont(SERIF_I, size)
            self.c.drawString(ML + 20, self.y - size, line)
            self.y -= 14
        self.c.setStrokeColor(self.accent)
        self.c.setLineWidth(2)
        self.c.line(ML + 6, top - 1, ML + 6, self.y + 3)
        self.y -= 10

    # ── structure ──
    def band(self, kicker_text, title, accent=None):
        """The module band: a solid accent bar carrying module number + name."""
        accent = HexColor(accent) if isinstance(accent, str) else (accent or self.accent)
        h = 46
        self.need(h + 18)
        self.c.setFillColor(accent)
        self.c.roundRect(ML, self.y - h, USABLE_W, h, 5, stroke=0, fill=1)
        self.c.setFillColor(HexColor("#FFFFFF"))
        self.c.setFont(SANS_B, 7.6)
        self.c.drawString(ML + 14, self.y - 17, ascii_safe(kicker_text).upper())
        self.c.setFont(SERIF_B, 16)
        self.c.drawString(ML + 14, self.y - 36, ascii_safe(title))
        self.y -= h + 16

    def rule(self, color=None, width=1.0, gap_before=2, gap_after=12):
        self.y -= gap_before
        self.need(gap_after + 2)
        self.c.setStrokeColor(color or BORDER)
        self.c.setLineWidth(width)
        self.c.line(ML, self.y, ML + USABLE_W, self.y)
        self.y -= gap_after

    def panel(self, title, lines, fill=WARM, accent=None):
        """A bordered note panel — used for 'how to use' and safety notes."""
        accent = HexColor(accent) if isinstance(accent, str) else (accent or self.accent)
        wrapped = []
        for line in lines:
            wrapped.extend(wrap(self.c, line, SANS, 9.4, USABLE_W - 28) if line else [""])
        h = 18 + (20 if title else 0) + len(wrapped) * 13 + 12
        self.need(h + 10)
        self.c.setFillColor(fill)
        self.c.setStrokeColor(BORDER)
        self.c.setLineWidth(0.75)
        self.c.roundRect(ML, self.y - h, USABLE_W, h, 5, stroke=1, fill=1)
        self.c.setStrokeColor(accent)
        self.c.setLineWidth(2.5)
        self.c.line(ML + 1, self.y - h + 4, ML + 1, self.y - 4)
        ty = self.y - 20
        if title:
            self.c.setFillColor(NAVY)
            self.c.setFont(SERIF_B, 11.5)
            self.c.drawString(ML + 16, ty, ascii_safe(title))
            ty -= 20
        self.c.setFont(SANS, 9.4)
        self.c.setFillColor(INK)
        for line in wrapped:
            if line:
                self.c.drawString(ML + 16, ty, line)
            ty -= 13
        self.y -= h + 14

    # ── fillable fields ──
    def field(self, label, name, rows=3, hint=None, indent=0):
        """A real AcroForm multiline field over ruled paper, so the same sheet
        works typed (Preview/Acrobat/GoodNotes) or handwritten (printed)."""
        line_h = 16
        box_h = rows * line_h + 8
        width = USABLE_W - indent
        self.need(box_h + 30)
        if label:
            self.c.setFont(SANS_B, 8.6)
            self.c.setFillColor(NAVY)
            self.c.drawString(ML + indent, self.y - 9, ascii_safe(label))
            if hint:
                lw = self.c.stringWidth(ascii_safe(label), SANS_B, 8.6)
                self.c.setFont(SANS_I, 8.2)
                self.c.setFillColor(GRAY_LT)
                self.c.drawString(ML + indent + lw + 8, self.y - 9, ascii_safe(hint))
            self.y -= 17
        top = self.y
        bottom = top - box_h
        self.c.setStrokeColor(BORDER)
        self.c.setLineWidth(0.75)
        self.c.roundRect(ML + indent, bottom, width, box_h, 4, stroke=1, fill=0)
        self.c.setStrokeColor(RULE)
        self.c.setLineWidth(0.4)
        ly = top - line_h
        while ly > bottom + 5:
            self.c.line(ML + indent + 7, ly, ML + indent + width - 7, ly)
            ly -= line_h
        self.c.acroForm.textfield(
            name=name, x=ML + indent + 3, y=bottom + 2,
            width=width - 6, height=box_h - 4,
            fontName=SANS, fontSize=9.5,
            fieldFlags="multiline",
            fillColor=FIELD_BG, borderColor=FIELD_EDGE, borderWidth=0.75,
            forceBorder=True, textColor=INK,
            tooltip="Tap and type — or print it and write",
        )
        self.y = bottom - 14

    def line_field(self, label, name, width=None, label_w=None):
        """A single-line field on one row — score boxes, dates, names."""
        h = 20
        self.need(h + 12)
        label = ascii_safe(label)
        label_w = label_w or (self.c.stringWidth(label, SANS_B, 8.6) + 10)
        width = width or (USABLE_W - label_w)
        self.c.setFont(SANS_B, 8.6)
        self.c.setFillColor(NAVY)
        self.c.drawString(ML, self.y - 14, label)
        self.c.acroForm.textfield(
            name=name, x=ML + label_w, y=self.y - h,
            width=width, height=h - 2,
            fontName=SANS, fontSize=9.5,
            fillColor=FIELD_BG, borderColor=FIELD_EDGE, borderWidth=0.75,
            forceBorder=True, textColor=INK,
        )
        self.y -= h + 10

    def checkbox_row(self, name, text, size=9.8):
        """A tickable checkbox with its label — for task and drill tracking."""
        h = 14
        self.need(h + 8)
        self.c.acroForm.checkbox(
            name=name, x=ML + 1, y=self.y - h + 1, size=11,
            fillColor=FIELD_BG, borderColor=FIELD_EDGE, borderWidth=0.75,
            checked=False, buttonStyle="check",
            tooltip="Tick when done",
        )
        lines = wrap(self.c, text, SANS, size, USABLE_W - 22)
        self.c.setFillColor(INK)
        self.c.setFont(SANS, size)
        for i, line in enumerate(lines):
            if i:
                self.need(13)
            self.c.drawString(ML + 20, self.y - 11 - (i * 13), line)
        self.y -= h + 4 + (len(lines) - 1) * 13


def cover(sheet, kicker_text, title, subtitle, accent, meta_lines=None):
    """A consistent cover block for every document in the pack."""
    c = sheet.c
    accent_c = HexColor(accent) if isinstance(accent, str) else accent
    y = sheet.y
    c.setFillColor(accent_c)
    c.setFont(SANS_B, 8.6)
    c.drawString(ML, y - 8, ascii_safe(kicker_text).upper())
    y -= 44
    c.setFillColor(NAVY)
    for line in wrap(c, title, SERIF_B, 27, USABLE_W):
        c.setFont(SERIF_B, 27)
        c.drawString(ML, y - 20, line)
        y -= 34
    y -= 4
    if subtitle:
        c.setFillColor(GRAY)
        for line in wrap(c, subtitle, SERIF_I, 13, USABLE_W - 40):
            c.setFont(SERIF_I, 13)
            c.drawString(ML, y - 8, line)
            y -= 19
    y -= 14
    c.setStrokeColor(accent_c)
    c.setLineWidth(1.6)
    c.line(ML, y, ML + USABLE_W, y)
    y -= 20
    if meta_lines:
        c.setFont(SANS, 8.8)
        c.setFillColor(GRAY)
        for line in meta_lines:
            c.drawString(ML, y - 8, ascii_safe(line))
            y -= 14
        y -= 8
    sheet.y = y


SAFETY_LINES = [
    "This course assumes a basically safe marriage. It is formation and practice — not counseling,",
    "crisis care, clinical treatment, addiction recovery, or trauma therapy.",
    "",
    "Abuse, coercion, threats, violence, active addiction, serious betrayal, or fear of retaliation call for",
    "confidential individual help first — not a joint exercise. Never use Scripture, forgiveness, headship,",
    "money, children, or course completion to demand access or to silence a concern.",
    "",
    "Immediate danger: call or text 911. Abuse or coercive control: National Domestic Violence Hotline,",
    "1-800-799-7233, or text START to 88788 — confidential, 24/7.",
]

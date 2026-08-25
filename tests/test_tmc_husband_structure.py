from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "tmc-husband"
PAGES = [COURSE / "index.html", COURSE / "progress.html"] + [
    COURSE / f"module-{number:02d}.html" for number in range(1, 8)
]
FORBIDDEN = re.compile(r"\b(?:TODO|TBD|FIXME|Lorem ipsum|PLACEHOLDER)\b", re.I)


class DocumentScan(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.start_tags: list[tuple[str, dict[str, str]]] = []
        self.ids: set[str] = set()
        self.heading_levels: list[int] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        self.start_tags.append((tag, values))
        if values.get("id"):
            self.ids.add(values["id"])
        if re.fullmatch(r"h[1-6]", tag):
            self.heading_levels.append(int(tag[1]))

    def handle_data(self, data: str) -> None:
        self.text_parts.append(data)


class TmcHusbandStructureTests(unittest.TestCase):
    def scan(self, page: Path) -> tuple[str, DocumentScan]:
        html = page.read_text(encoding="utf-8")
        parser = DocumentScan()
        parser.feed(html)
        return html, parser

    def test_all_pages_have_semantic_shell_safe_links_and_valid_local_references(self) -> None:
        for page in PAGES:
            with self.subTest(page=page.name):
                html, scan = self.scan(page)
                tags = [tag for tag, _ in scan.start_tags]
                self.assertIn("main", tags)
                self.assertIn("nav", tags)
                self.assertIn("footer", tags)
                self.assertEqual(scan.heading_levels.count(1), 1)
                self.assertFalse(any(b - a > 1 for a, b in zip(scan.heading_levels, scan.heading_levels[1:])), scan.heading_levels)
                self.assertIn("main-content", scan.ids)
                self.assertIsNone(FORBIDDEN.search(html))
                self.assertIn("../assets/css/tmc-husband.v1.css", html)
                self.assertIn("../assets/js/tmc-husband.v1.js", html)

                for tag, attrs in scan.start_tags:
                    if tag == "a" and attrs.get("target") == "_blank":
                        rel = set(attrs.get("rel", "").split())
                        self.assertTrue({"noopener", "noreferrer"}.issubset(rel))
                    if tag == "a" and attrs.get("href", "").endswith(".html"):
                        target = (page.parent / attrs["href"]).resolve()
                        self.assertTrue(target.exists(), f"broken link {attrs['href']} in {page.name}")

    def test_module_pages_have_complete_standard_structure_and_keyboard_control(self) -> None:
        required = {
            "mission-brief", "scripture-frame", "fair-insight", "caution-boundary",
            "self-check", "field-action", "conversation-guide", "support-boundary",
            "resources", "completion"
        }
        for number, page in enumerate(PAGES[2:], start=1):
            with self.subTest(page=page.name):
                html, scan = self.scan(page)
                self.assertTrue(required.issubset(scan.ids))
                controls = [attrs for tag, attrs in scan.start_tags if tag == "button" and attrs.get("data-complete-module")]
                self.assertEqual(len(controls), 1)
                self.assertEqual(controls[0].get("type"), "button")
                self.assertEqual(controls[0].get("aria-pressed"), "false")
                text = " ".join(scan.text_parts)
                self.assertIn("Observable finish line", text)
                self.assertIn("Support and safety boundary", text)
                self.assertIn("Draft pending Adam, doctrinal, editorial, and rights review.", text)

    def test_css_enforces_mobile_overflow_focus_and_reduced_motion_boundaries(self) -> None:
        css = (ROOT / "assets/css/tmc-husband.v1.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"html\s*\{[^}]*overflow-x:\s*hidden")
        self.assertIn(":focus-visible", css)
        self.assertRegex(css, r"@media\s*\(prefers-reduced-motion:\s*reduce\)")
        self.assertRegex(css, r"max-width:\s*100%")
        self.assertRegex(css, r"@media\s*\(min-width:")


if __name__ == "__main__":
    unittest.main(verbosity=2)

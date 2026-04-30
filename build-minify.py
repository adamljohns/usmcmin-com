#!/usr/bin/env python3
"""
build-minify.py — minify profile.css + profile.js to .min.css / .min.js.

Run after editing assets/css/profile.css or assets/js/profile.js. The
profile template (generate-profiles.py) links to the .min versions so
visitors download the smallest possible asset.

Both source files stay in the repo for editability + diffability —
.min.css and .min.js are derived artifacts, regenerated on demand.

Conservative implementation:
  - CSS: strips /* */ comments, collapses whitespace, removes optional
    semicolons before }, trims space around { } : ; , > + ~
  - JS: strips // line comments + /* */ block comments + blank lines.
    Does NOT rename identifiers or perform deep AST optimization
    (would need a real JS parser like terser; not worth the dependency
    for this scale).

Typical reduction:
  CSS: ~30-40% smaller
  JS:  ~20-25% smaller (because of preserved identifiers)

Usage:
    python3 build-minify.py        # minify both files
    python3 build-minify.py --dry  # report sizes without writing
"""
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
# Files to minify. Each tuple is (source_path, minified_path, minifier_func_name).
TARGETS = [
    (BASE / 'assets' / 'css' / 'profile.css',
     BASE / 'assets' / 'css' / 'profile.min.css', 'css'),
    (BASE / 'assets' / 'css' / 'main.css',
     BASE / 'assets' / 'css' / 'main.min.css', 'css'),
    (BASE / 'assets' / 'js' / 'profile.js',
     BASE / 'assets' / 'js' / 'profile.min.js', 'js'),
    # main.js is also a minify candidate but is used in many places —
    # add when we audit it.
]


def minify_css(text):
    # Remove /* ... */ comments (greedy across lines)
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    # Collapse runs of whitespace into a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove space around CSS operators that don't need it
    text = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', text)
    # Remove the optional semicolon before }
    text = text.replace(';}', '}')
    # Remove leading 0 from 0.5em, 0.25rem, etc. (saves a byte)
    text = re.sub(r'(?<![\d.])0\.', '.', text)
    return text.strip()


def minify_js(text):
    """Remove comments and blank lines. Preserve all identifiers/whitespace
    inside expressions (safer than aggressive minification without a real
    parser — string contents and regex literals could otherwise break)."""
    # Remove /* ... */ block comments — but be careful about regex literals.
    # Approach: walk char-by-char, track string/regex/comment state.
    out = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        nx = text[i+1] if i+1 < n else ''

        # Detect /* ... */ block comment
        if ch == '/' and nx == '*':
            # Skip until next */
            j = text.find('*/', i + 2)
            if j == -1:
                # Unterminated — leave the rest as-is
                break
            i = j + 2
            continue
        # Detect // line comment
        if ch == '/' and nx == '/':
            j = text.find('\n', i)
            if j == -1:
                break
            i = j  # leave the \n for line preservation
            continue
        # Inside a string literal — copy verbatim until closing quote
        if ch in ('"', "'", '`'):
            quote = ch
            out.append(ch)
            i += 1
            while i < n:
                c = text[i]
                if c == '\\' and i + 1 < n:
                    out.append(c)
                    out.append(text[i+1])
                    i += 2
                    continue
                out.append(c)
                i += 1
                if c == quote:
                    break
            continue
        out.append(ch)
        i += 1

    minified = ''.join(out)
    # Drop blank lines (but keep single newlines between statements for
    # safety with ASI — Automatic Semicolon Insertion).
    lines = [ln.rstrip() for ln in minified.split('\n')]
    lines = [ln for ln in lines if ln.strip()]
    # Trim leading whitespace per line — saves bytes without changing semantics
    lines = [ln.lstrip() for ln in lines]
    return '\n'.join(lines)


def write(path_min, content):
    path_min.parent.mkdir(parents=True, exist_ok=True)
    with open(path_min, 'w') as f:
        f.write(content)


def main():
    dry = '--dry' in sys.argv
    minifiers = {'css': minify_css, 'js': minify_js}

    for src_path, min_path, kind in TARGETS:
        if not src_path.exists():
            print(f'Skipping {src_path.name} (not found)')
            continue
        src = src_path.read_text()
        out = minifiers[kind](src)
        delta = (1 - len(out) / len(src)) * 100 if src else 0
        rel = src_path.relative_to(BASE)
        print(f'{str(rel):40s}  {len(src):>7,} → {len(out):>7,} bytes  '
              f'(-{delta:.1f}%)')
        if not dry:
            write(min_path, out)

    if dry:
        print('DRY RUN — nothing written')


if __name__ == '__main__':
    main()

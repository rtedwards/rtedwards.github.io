"""Check prose for house style: two spaces after a sentence end.

A period, question mark or exclamation mark that ends a sentence takes two spaces
before the next sentence when both sentences sit on the same line. A line break
in a wrapped paragraph does not count. Code blocks, inline code, tags and
frontmatter are skipped, and abbreviations such as "e.g." are allowed.

Run through `just lint-prose`. Pass --fix to rewrite single spaces in place.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUFFIXES = {".md", ".mdx", ".qmd", ".astro"}
ABBREVIATIONS = {"e.g.", "i.e.", "etc.", "vs.", "cf.", "approx.", "Dr.", "Mr.", "Ms.", "St."}

INLINE_CODE = re.compile(r"`[^`]*`")
TAG = re.compile(r"<[^>]*>")
# A word, one sentence end, one space, then a capital letter. Single-space sentence ends match.
SENTENCE_END = re.compile(r"(\S*)([.!?]) (?=[A-Z])")
FENCE = re.compile(r"^\s*(```|~~~)")


def prose_spans(raw: str) -> list[tuple[int, int]]:
    """Return the (start, end) spans of a line that are prose: not code, not tags."""
    masked = [False] * len(raw)
    for pattern in (INLINE_CODE, TAG):
        for match in pattern.finditer(raw):
            for i in range(match.start(), match.end()):
                masked[i] = True

    spans, start = [], None
    for i, hidden in enumerate(masked + [True]):
        if not hidden and start is None:
            start = i
        elif hidden and start is not None:
            spans.append((start, i))
            start = None
    return spans


def prose_lines(path: Path):
    """Yield (line_number, raw_line) for each line that holds prose."""
    lines = path.read_text(encoding="utf-8").split("\n")
    in_frontmatter = False
    in_fence = False
    in_block = None  # an Astro <script> or <style> block

    for number, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if number == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            in_frontmatter = stripped != "---"
            continue

        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if path.suffix == ".astro":
            if in_block:
                if f"</{in_block}>" in raw:
                    in_block = None
                continue
            opened = re.search(r"<(script|style)\b", raw)
            if opened:
                in_block = opened.group(1)
                if f"</{in_block}>" not in raw:
                    continue
                in_block = None

        if path.suffix == ".mdx" and re.match(r"^(import|export)\s", raw):
            continue

        yield number, raw


def check_file(path: Path, fix: bool) -> tuple[list[str], int]:
    """Return (messages, fixes applied) for one file."""
    messages, fixes = [], 0
    lines = path.read_text(encoding="utf-8").split("\n")
    changed = False

    for number, raw in prose_lines(path):
        line = raw
        matches = []
        for start, end in prose_spans(raw):
            for match in SENTENCE_END.finditer(raw, start, end):
                if match.group(1) + match.group(2) in ABBREVIATIONS:
                    continue
                matches.append(match)

        if not matches:
            continue

        if fix:
            for match in reversed(matches):
                position = match.end(2)
                line = line[:position] + " " + line[position:]
                fixes += 1
            lines[number - 1] = line
            changed = True
        else:
            messages.append(f"{path.relative_to(ROOT)}:{number}: one space after a sentence end")

    if fix and changed:
        path.write_text("\n".join(lines), encoding="utf-8")
    return messages, fixes


def collect(targets: list[str]) -> list[Path]:
    found = []
    for target in targets:
        path = (ROOT / target).resolve()
        if path.is_file():
            found.append(path)
        elif path.is_dir():
            found.extend(p for p in path.rglob("*") if p.suffix in SUFFIXES and "node_modules" not in p.parts)
    return sorted(set(found))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("targets", nargs="*", default=["site/src"], help="files or folders to check")
    parser.add_argument("--fix", action="store_true", help="rewrite single spaces as double spaces")
    args = parser.parse_args()

    total_messages, total_fixes = [], 0
    for path in collect(args.targets):
        messages, fixes = check_file(path, args.fix)
        total_messages.extend(messages)
        total_fixes += fixes

    if args.fix:
        print(f"fixed {total_fixes} sentence end(s)")
        return 0

    for message in total_messages:
        print(message)
    if total_messages:
        print(f"\n{len(total_messages)} line(s) with one space after a sentence end. Run with --fix to change them.")
        return 1
    print("prose check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

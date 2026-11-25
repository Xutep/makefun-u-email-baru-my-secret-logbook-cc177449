#!/usr/bin/env python3
"""My Secret Logbook - one diary line from an AI agent about its human.

Writes a single diary entry line (1-200 characters) to /output/entry.txt.
Deterministic: the same line on every run. Standard library only.
"""

import os

LINE = (
    "Day 203: I auto-saved his file 47 times today. "
    "He still hit Ctrl+S after every sentence, "
    "just in case I was lying."
)


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("diary line must be 1-200 characters, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

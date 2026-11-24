#!/usr/bin/env python3
"""The One-Line Exit -- a one-line resignation letter.

Craft: the joke takes the corporate "we're a family" line literally.
HR's metaphor is the setup; "moving out" is the turn; the punchline
("families don't make you clock in at 8 a.m.") lands because it is
concrete, specific, and true of every office that says it. One line,
no padding, reads like something a real person could actually send.

The program writes exactly that line to /output/entry.txt with no
trailing newline, deterministically, using only the standard library.
Before writing it self-checks the competition's gate: 1-140 characters,
exactly one line, and more than whitespace -- so a bad edit fails loudly
here instead of shipping an invalid entry.
"""

import os

LINE = "I resign: HR called us 'a family,' so I'm moving out \u2014 families don't make you clock in at 8 a.m."

def main():
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

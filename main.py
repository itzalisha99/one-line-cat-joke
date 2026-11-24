#!/usr/bin/env python3
"""One-Line Cat Joke That Lands — make.fun bounty entry.

Writes a single cat joke, one line under 200 characters, to
/output/entry.txt.

The joke is checked by a self-authored ``validate()`` gate that mirrors
the bounty gate before anything is written: the text must be UTF-8,
1 to 200 characters, not only whitespace, and exactly one line.
"""

import os

JOKE = "The vet said my cat is overweight. My cat said the vet is underfed."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()

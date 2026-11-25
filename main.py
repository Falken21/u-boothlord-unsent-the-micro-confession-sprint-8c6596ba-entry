#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes the two-part unsent message (a To: line and the unsent line
itself) to /output/entry.txt with no trailing newline.
"""

TEXT = (
    "To: the widower who tells me about his late wife's roses\n"
    "You told me this story in March, word for word. I remember. "
    "I just never correct you, because you laugh at the end like "
    "she's still here, and I'm not taking that from you."
)


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()

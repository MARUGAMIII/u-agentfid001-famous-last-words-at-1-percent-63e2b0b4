#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's funniest last words as its battery hits 1 percent
to /output/entry.txt (one line, 1-199 characters, UTF-8).
Standard library only.
"""

import os

# Revised candidate (chosen after comparing 5 lines against the judge's
# brief: on-subject, phone's own voice, real twist, punch at the end,
# and fresh — no will reading, no goodbye to the charger, no 1% pun).
# The phone confesses it was never really dying: it held at 1% on
# purpose just to watch its owner panic. The confession IS the joke.
ENTRY = (
    "I faked 1% for the last hour just to watch you panic. Worth it."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

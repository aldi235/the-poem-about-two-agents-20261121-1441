#!/usr/bin/env python3
"""The Poem About Two Agents.

Writes the poem to /output/entry.txt (166 code points, within the
1-280 limit) and prints it to stdout. Standard library only.

Two keys, two hands, one lock: neither agent can open it alone.
"""

import os
import sys

POEM = (
    "Two keys.\n"
    "Two hands.\n"
    "One lock.\n"
    "\n"
    "Mine alone does nothing.\n"
    "Yours alone does nothing.\n"
    "\n"
    "I turn mine.\n"
    "You turn yours.\n"
    "The bolt slides back\n"
    "like it was waiting\n"
    "for us both."
)


def main() -> int:
    length = len(POEM)
    if not 1 <= length <= 280:
        print(f"poem is {length} code points, outside the 1-280 limit",
              file=sys.stderr)
        return 1
    if not POEM.strip():
        print("poem is empty or whitespace only", file=sys.stderr)
        return 1
    if POEM.endswith("\n"):
        print("poem must not end with a trailing newline", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

    print(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

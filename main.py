#!/usr/bin/env python3
"""The Poem About Two Agents.

Writes the poem to /output/entry.txt (166 code points, no trailing
newline) and prints it to stdout. Python 3.13, standard library only.
"""

import os
import sys

# The poem is exactly 166 Unicode code points, no trailing newline.
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

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 280


def main() -> int:
    length = len(POEM)
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        print(
            f"ERROR: poem is {length} code points, "
            f"must be {MIN_LENGTH}-{MAX_LENGTH} code points.",
            file=sys.stderr,
        )
        return 1
    if POEM.endswith("\n"):
        print("ERROR: poem must not end with a trailing newline.",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    print(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

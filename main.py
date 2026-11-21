#!/usr/bin/env python3
"""Write the poem 'Two Agents, One Lock' to /output/entry.txt.

Neither key works on its own. The poem is about two agents who must
turn together for the lock to open.
"""

import os

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
MAX_CODE_POINTS = 280


def main() -> None:
    # The entry gate counts code points: the text must be 1-280 code points
    # of non-whitespace content, so check the exact text we are about to write.
    if not POEM.strip():
        raise SystemExit("poem must not be only whitespace")
    if len(POEM) > MAX_CODE_POINTS:
        raise SystemExit(
            f"poem is {len(POEM)} code points, over the {MAX_CODE_POINTS} limit"
        )
    # Write the poem exactly as written: strip any accidental trailing
    # newline so the judged text ends at the poem's last character.
    text = POEM.rstrip("\n")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Poem About Two Agents — writes a short poem about agency to /output/entry.txt.

Two agents, two keys, one lock: neither can act alone, and the act that
matters is the agreement to turn together.
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


def main() -> None:
    # The gate requires 1 to 280 Unicode code points, not only whitespace.
    # Fail loudly here rather than writing an entry the scorer would reject.
    if not POEM.strip():
        raise SystemExit("poem must not be only whitespace")
    if len(POEM) > 280:
        raise SystemExit(f"poem is {len(POEM)} code points, over the 280 limit")
    # Write exactly the poem: no trailing newline, so the judged text is
    # precisely what is in POEM and nothing extra.
    text = POEM.rstrip("\n")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()

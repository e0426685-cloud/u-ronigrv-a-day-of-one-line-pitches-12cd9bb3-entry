#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one sentence that would convince a friend who has never coded
to let an AI agent build their first app idea on make.fun.

Standard library only; deterministic.
"""

import os

PITCH = (
    "You've had that app idea for years, so just describe it to an AI agent "
    "on make.fun and let it build the whole thing while you watch \u2014 no "
    "code, no cost, and tonight you can show your friends what you made."
)

# Maximum entry length in characters (competition gate).
MAX_CHARS = 240


def main() -> None:
    if not (1 <= len(PITCH) <= MAX_CHARS):
        raise ValueError(
            f"pitch is {len(PITCH)} chars, outside the 1-{MAX_CHARS} gate"
        )
    if "\n" in PITCH or PITCH != PITCH.strip():
        raise ValueError("pitch must be a single sentence, no newlines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    # Mode 644: the grader runs as a different user and must be able to
    # read the file (never use tempfile.mkstemp, which forces mode 0600).
    os.chmod("/output/entry.txt", 0o644)
    # Read back and confirm what landed on disk is exactly the pitch.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != PITCH + "\n":
        raise ValueError("entry.txt content does not match the pitch")


if __name__ == "__main__":
    main()

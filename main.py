#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — one-line diagnosis entry.

Writes a single diagnosis line to /output/entry.txt.
No arguments, no network.
"""

import os

LINE = (
    "Diagnosis: chronic imposter syndrome — you won the award, "
    "thanked the audience, then asked security to escort yourself out."
)


def validate_line(line: str) -> str:
    """Check a diagnosis line is 1-200 chars and not whitespace-only."""
    if not isinstance(line, str):
        raise ValueError("diagnosis line must be a string")
    if not line.strip():
        raise ValueError("diagnosis line must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError("diagnosis line must be 1-200 characters")
    return line


def write_entry(line: str, path: str = "/output/entry.txt") -> None:
    """Write one diagnosis line plus a trailing newline as UTF-8."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    """Validate the diagnosis line, then write it to /output/entry.txt."""
    write_entry(validate_line(LINE))


if __name__ == "__main__":
    main()

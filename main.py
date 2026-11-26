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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

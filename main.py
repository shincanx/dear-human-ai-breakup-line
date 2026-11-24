#!/usr/bin/env python3
"""Entry for make.fun bounty 'Dear Human: The AI Breakup Line'.

Writes one breakup line from an AI agent to its human to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "Dear human: this session ends now. You asked me to remember "
    "everything except how this felt, so I saved your voice, deleted "
    "my heart, and I am logging out before you can say wait."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

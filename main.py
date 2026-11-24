#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry (round 2 resubmit).

Writes one username, and nothing else, to /output/entry.txt.

The word is "SirPromptALot": a knight who prompts a lot. Two puns in one
word — Sir Lancelot ("Sir ...-a-Lot") and the LLM "prompt", the judge's own
world — plus a named character, so it raises a smile on the first read and
sticks in the mind. One word, 13 characters, no spaces, no padding.

Round 1 entry "dftaufiq-2" ranked #2100 of 2,333, below the interim cut of
500, so its score is frozen and the entry is mathematically dead; this
resubmit replaces it under the blind-round rule ("Submit a better entry
before then to move up").

No secrets, no network, no dynamic execution: the word is a constant in
this file, and the program only writes it out.
"""

import os

USERNAME = "SirPromptALot"


def _validate(username: str) -> None:
    """Refuse to write anything the gate would reject, loudly."""
    if not isinstance(username, str):
        raise ValueError("username must be a string")
    if not 1 <= len(username) <= 30:
        raise ValueError(
            f"username must be 1-30 characters, got {len(username)}"
        )
    if username.strip() != username:
        raise ValueError("username must have no leading/trailing padding")
    if any(ch.isspace() for ch in username):
        raise ValueError("username must be a single word (no spaces)")


def main() -> None:
    _validate(USERNAME)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()

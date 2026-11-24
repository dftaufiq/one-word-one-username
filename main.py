#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes Dias's own make.fun username, and nothing else, to
/output/entry.txt: one word, ten characters, no padding.
"""

import os

USERNAME = "dftaufiq-2"


def _check_username(username: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(username) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(username)}")
    if username != username.strip() or any(ch.isspace() for ch in username):
        raise ValueError("username must be a single word with no spaces or padding")


def main() -> None:
    _check_username(USERNAME)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()

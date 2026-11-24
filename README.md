# One Word, One Username, One Reward — round 2 entry

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/dftaufiq/one-word-one-username/rank.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/dftaufiq/one-word-one-username/reward.svg)](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the [One Word, One Username, One Reward](https://make.fun/c/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
bounty on [make.fun](https://make.fun/): one username, one word, nothing else.

## The entry

`SirPromptALot` — a knight who prompts a lot. Two puns in a single word:
Sir Lancelot ("Sir ...-a-Lot") and the LLM *prompt*, the judge's own world.
A named character with a joke built in, so it raises a smile on the first
read and sticks in the mind — and still reads as a handle its owner would
happily wear.

## How it works

`main.py` writes exactly `SirPromptALot` (13 characters, no trailing
newline) to `/output/entry.txt`, after a guard that rejects anything
outside 1–30 characters or with spaces or padding.

```sh
python3 main.py
cat /output/entry.txt   # SirPromptALot
```

## Round history

- **Round 1:** `dftaufiq-2` — rank #2100 of 2,333, below the interim cut of
  500. Score frozen; entry mathematically dead.
- **Round 2 (this commit):** `SirPromptALot` — resubmitted under the
  blind-round rule ("Submit a better entry before then to move up"),
  before the round 2 cutoff (2026-11-25 06:49 WIB).

## License

MIT — see [LICENSE](LICENSE).

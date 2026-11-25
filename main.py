"""One Word for the Boss.

Writes exactly one word describing a boss to /output/entry.txt.
Stdlib only, no network, fully deterministic: the same word every run.
"""

import os

WORD = "meetingizer"  # the boss who turns every question into a meeting


def main() -> None:
    # Gate check, mirroring the scorer: 1-30 chars, UTF-8, not only whitespace.
    assert 1 <= len(WORD) <= 30 and WORD.strip() == WORD and " " not in WORD
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one AI agent apology one-liner to /output/entry.txt.

Entry (119 chars, limit 159): the agent emailed the boss a draft apology
for emailing the boss -- a recursive apology loop, third one today, and
the boss has now replied 'stop'. One concrete detail (third one today)
plus the twist (the apology itself is the accident, repeated).
Flat agent voice, no generic "sorry" or "oops".
"""
import os

LINE = "I emailed your boss your draft apology for emailing your boss. This is the third one today, and he just replied 'stop'."


def main() -> None:
    assert 1 <= len(LINE) <= 159, f"entry is {len(LINE)} chars, limit 159"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()

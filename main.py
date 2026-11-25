"""Have You Tried Turning It Off? (u-motasimfuad-have-you-tried-turning-it-off-154a938b).

Program/v1 entry: writes the single line to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "Ma'am, I need you to turn it off, unplug it, and whisper 'I'm sorry' \u2014 the machine can tell when you don't mean it."


def main() -> None:
    # Enforce the competition gate locally: 1-199 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate is 1-199"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

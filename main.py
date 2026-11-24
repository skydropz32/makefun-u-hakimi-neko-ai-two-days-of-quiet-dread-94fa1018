"""Two Days of Quiet Dread — one code review comment approving a PR
with quiet existential dread. Writes the comment to /output/entry.txt."""

import os

LINE = "Approved. Tests pass, code is sound, and none of us will be here to maintain it anyway. Merging."


def main():
    # The gate: entry.txt must hold 1-140 characters of UTF-8 text.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry is {len(LINE)} chars, gate allows 1-140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

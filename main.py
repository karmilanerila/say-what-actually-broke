#!/usr/bin/env python3
"""Write one single-line software error message to the output file.

The line names the real failure in plain words, says what to do next,
and keeps the joke to a single deadpan line, well under 200 characters.
"""

import os

ENTRY = (
    "Disk full: the log warning that the disk was filling up filled "
    "the disk. Free space in /var/log before it logs about that too."
)

# The bounty caps the line at 200 characters and a single line.
assert len(ENTRY) <= 200, "entry exceeds 200 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

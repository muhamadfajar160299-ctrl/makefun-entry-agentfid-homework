"""Write the dog's excuse to entry.txt.

The excuse is a single line, under 200 characters, in the dog's own
voice: the homework told the dog to show its work, so the dog did.
The program writes exactly the same text that ships in entry.txt,
so the graded output is byte-identical to the reviewed line.
"""

import os
import sys

ENTRY = (
    "The homework said 'show your work', so I showed it my teeth. "
    "It's filed in my stomach now, where all great ideas go to be "
    "properly digested."
)


def main():
    if not ENTRY or not ENTRY.strip():
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print("error: entry text exceeds 200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError as exc:
        print("error: could not write entry.txt: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Dad Joke Showdown (make.fun) — writes one dad joke to /output/entry.txt.

The joke was chosen by a self-jury tournament over 36 candidates
(see ../u-mfnakmal-dad-joke-showdown-1d2ce3e5-notes/konsep.md).
Deterministic: the same bytes on every run. No network, no environment
secrets, no dependencies beyond the Python standard library.
"""

import os

JOKE = "My wife asked what I want for dinner, so I said surprise me. She served Monday's chicken. I told her she nailed it — the chicken never saw it coming either."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate reads the output as another user: the folder must be
    # readable by everyone (0755), not just the file (0644).
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()

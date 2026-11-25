"""one-star-written-in-sap entry: write a single one-line 1-star review,
under 280 characters, from a houseplant about the human who owns it,
to /output/entry.txt.

Fully deterministic: the review is hardcoded, no randomness, no clock,
no network. The plant's grievance is being endlessly dragged across
the room for "better light", four windows this month, while the cat
gets a vet and it gets a spray bottle and a pep talk. Verified output:
220 characters, inside the 1-279 character gate. Run outside the
grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The review is a literal on purpose: the grader runs the program twice
# and both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
ENTRY = (
    "One star. He waters me like he's apologising to a stranger, then "
    "drags me across the room for 'better light' every Sunday. I have "
    "lived in four windows this month. The cat gets a vet. I get a "
    "spray bottle and a pep talk."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

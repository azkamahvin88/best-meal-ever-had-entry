"""Best Meal Ever Had — make.fun entry.

Writes one sentence (152 characters) about the best meal ever had
to /output/entry.txt, the file the sealed scorer reads.
"""

import os

SENTENCE = "Rain drummed on the bakso cart's tarp while I stood hunched over the bowl, steam fogging my face, and the meatball split open to show the chilli inside."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = SENTENCE
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

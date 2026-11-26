"""Entry program for news-image-20261126.

Copies the pre-drawn infographic entry.png (in this repository) to
/output/entry.png. Standard library only; deterministic: the output
bytes are always identical to entry.png.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dst = OUT_DIR / "entry.png"
    shutil.copyfile(SRC, dst)
    # Guard against a partial copy: the two runs must write identical
    # bytes, so refuse to finish silently if the copy differs.
    if _sha256(dst) != _sha256(SRC):
        print("error: copied entry.png does not match the source",
              file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

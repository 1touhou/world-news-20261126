"""World News 20261126 — entry point.

The newspaper image (entry.png) is pre-rendered and checked into this
repository. The scoring environment runs Python 3 with the standard
library only, so this program does nothing but copy the finished image
to the output directory. It is deterministic: same input, same output.
"""

import os
import shutil
import sys


def output_dir():
    """Directory the grader expects the entry in."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if raw.strip():
        return raw
    return "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(source) != os.path.getsize(target):
        sys.stderr.write("entry.png copy mismatch\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

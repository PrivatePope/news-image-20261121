"""Copy the rendered front page to the grader's output directory.

Standard library only. The image is already rendered and shipped in this
repository as entry.png next to this program; this program just places a
copy at $MAKEFUN_OUTPUT_DIR/entry.png, which is what the grader reads.
No network, no clock, no third-party packages: it runs the same way every
time, from any working directory.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        raise SystemExit("entry.png missing next to main.py: %s" % source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()

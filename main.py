#!/usr/bin/env python3
"""Copy the bundled front-page image to the output directory.

Standard library only. Deterministic: the same bytes every run.
The image (entry.png) sits beside this file in the repository; the
program only copies it, it never draws or downloads anything.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, SOURCE),
                    os.path.join(out_dir, SOURCE))


if __name__ == "__main__":
    main()

"""Sunflower Umbrella: copy entry.png to the output directory.

The entry image ships beside this program; the program writes the
same bytes to $MAKEFUN_OUTPUT_DIR (else /output) as entry.png.
The copy is byte for byte, so repeated runs are identical.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()

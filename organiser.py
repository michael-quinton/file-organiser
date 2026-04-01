# Accept a directory as a CLI argument
# Scane directory for files
# Move each file into a subfolder based on its category

import argparse
from pathlib import Path

extensions = {
    ".py": "code",
    ".txt": "documents",
    ".jpg": "images"
}

parser = argparse.ArgumentParser()
parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
args = parser.parse_args()
print(args.directory)

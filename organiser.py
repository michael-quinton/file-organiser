# Accept a directory as a CLI argument
# Scan directory for files
# Move each file into a subfolder based on its category

import argparse
from pathlib import Path

ignore_files = [".gitignore", "organiser.py"]

parser = argparse.ArgumentParser()
parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
args = parser.parse_args()
directory = args.directory

def get_files(directory):
    files = []
    for item in directory.iterdir():
        if item.name in ignore_files:
            continue
        if item.is_file():
            files.append(item)
    return files

print(get_files(directory))
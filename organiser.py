# Accept a directory as a CLI argument
# Scan directory for files
# Move each file into a subfolder based on its category

import argparse
from pathlib import Path

extensions = {
    # Code
    ".py": "code",
    ".js": "code",
    ".html": "code",
    ".css": "code",
    ".cpp": "code",
    ".java": "code",

    # Documents
    ".txt": "documents",
    ".pdf": "documents",
    ".docx": "documents",
    ".doc": "documents",
    ".xlsx": "documents",
    ".pptx": "documents",

    # Images
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".svg": "images",

    # Audio
    ".mp3": "audio",
    ".wav": "audio",
    ".flac": "audio",

    # Video
    ".mp4": "video",
    ".mkv": "video",
    ".avi": "video",

    # Archives
    ".zip": "archives",
    ".tar": "archives",
    ".gz": "archives",
    ".rar": "archives"
}

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

def get_category(file):
    return extensions.get(file.suffix.lower(), "misc")

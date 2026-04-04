"""
CLI tool to organise files into category-based folders.
"""

import argparse
import shutil
from pathlib import Path

import yaml


# File extensions mapped to destination categories.
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
    ".rar": "archives",
}

# Files that should not be moved during organisation.
ignore_files = [
    ".gitignore",
    "organiser.py",
    "config.yaml",
]


def load_extensions():
    """Load extension categories from config.yaml if it exists."""
    config = Path("./config.yaml")

    if config.is_file():
        extensions.clear()

        with open("./config.yaml", "r") as file:
            data = yaml.safe_load(file)

        for key, values in data.items():
            for value in values:
                extensions[value.lower()] = key


def parse_directory():
    """Parse CLI arguments and validate the target directory."""
    parser = argparse.ArgumentParser(
        description="Organise files in a directory by category"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path.cwd(),
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--undo", action="store_true")

    args = parser.parse_args()
    directory = args.directory
    dry_run = args.dry_run
    undo = args.undo

    if not directory.exists() or not directory.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        raise SystemExit(1)

    return directory, dry_run, undo


def get_files(directory):
    """Return files in the directory that are not ignored."""
    return [
        item
        for item in directory.iterdir()
        if item.is_file() and item.name not in ignore_files
    ]


def get_category(file):
    """Return the category for a file based on its extension."""
    return extensions.get(file.suffix.lower(), "misc")


def get_unique_name(destination):
    """Return a unique destination path if the file already exists."""
    if not destination.exists():
        return destination

    increment = 1

    while True:
        new_name = f"{destination.stem}({increment}){destination.suffix}"
        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        increment += 1


def organise_files(directory, dry_run):
    """Move files into category folders, or print actions in dry-run mode."""
    files = get_files(directory)

    for file in files:
        category = get_category(file)
        folder = directory / category

        if not dry_run:
            folder.mkdir(exist_ok=True)

        destination = folder / file.name
        destination = get_unique_name(destination)

        if not dry_run:
            shutil.move(src=file, dst=destination)

        relative_path = destination.relative_to(directory)

        if not dry_run:
            print(f"Moved {file.name} -> {relative_path}")
        else:
            print(f"Would move {file.name} -> {relative_path}")


def main():
    """Run the file organiser."""
    directory, dry_run, undo = parse_directory()
    if not undo:
        load_extensions()
        organise_files(directory, dry_run)
    

if __name__ == "__main__":
    main()
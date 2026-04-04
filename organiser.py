# Accept a directory as a CLI argument
# Scan directory for files
# Move each file into a subfolder based on its category

import argparse, shutil, yaml
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

def load_extensions():
    config = Path("./config.yaml")
    if config.is_file():
        extensions.clear()

        with open("./config.yaml", "r") as file:
            data = yaml.safe_load(file)

        for key, values in data.items():
            for value in values:
                extensions[value.lower()] = key

ignore_files = [".gitignore", "organiser.py", "config.yaml"]

def parse_directory():
    parser = argparse.ArgumentParser(description="Organise files in a directory by category")
    parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    directory = args.directory
    dry_run = args.dry_run
    if not directory.exists() or not directory.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        raise SystemExit(1)
    return directory, dry_run
    
def get_files(directory):
    return [item for item in directory.iterdir() if item.is_file() and item.name not in ignore_files]

def get_category(file):
    return extensions.get(file.suffix.lower(), "misc")

def get_unique_name(destination):
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
    directory, dry_run = parse_directory()
    load_extensions()
    organise_files(directory, dry_run)

if __name__ == "__main__":
    main()
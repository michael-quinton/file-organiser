# File Organiser

A command-line tool that tidies up a directory by sorting files into subfolders based on their file type.

## Usage

```bash
# Organise the current directory
python organiser.py

# Organise a specific directory
python organiser.py ~/Downloads
```

## How It Works

The tool scans the target directory and moves files into categorised subfolders:

| Category    | Extensions                          |
|-------------|-------------------------------------|
| code        | .py, .js, .html, .css, .cpp, .java |
| documents   | .txt, .pdf, .docx, .doc, .xlsx, .pptx |
| images      | .jpg, .jpeg, .png, .gif, .svg      |
| audio       | .mp3, .wav, .flac                   |
| video       | .mp4, .mkv, .avi                    |
| archives    | .zip, .tar, .gz, .rar              |
| misc        | everything else                     |

If a file with the same name already exists in the destination folder, it is automatically renamed (e.g. `photo(1).jpg`).

## Requirements

Python 3.6+

No external dependencies.

## Roadmap

- [x] `--dry-run` flag to preview changes without moving files
- [ ] `--watch` mode for continuous monitoring
- [x] Configurable rules via YAML
- [ ] `--undo` to reverse the last run
- [ ] Logging
- [ ] Tests

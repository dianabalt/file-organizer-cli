# File Organizer CLI

A simple Python command-line tool that organizes files into folders based on their file type (Images, Documents, Audio, etc.).

---

##  Features

* Organize files by extension
* Dry-run mode (preview changes before applying)
* Duplicate protection (prevents overwriting existing files)
* Summary output (processed, moved, skipped)

---

## Project Structure

```
file-organizer-cli/
├── main.py
├── organizer.py
├── utils.py
├── test_files/
└── README.md
```

---

##  How to Run

### 1. Navigate to the project folder

```bash
cd file-organizer-cli
```

### 2. Dry Run (Recommended First)

Preview what will happen without moving files:

```bash
python main.py organize <folder_path> --dry-run
```

Example:

```bash
python main.py organize test_files --dry-run
```

---

### 3. Actual File Organization

Run without `--dry-run` to move files:

```bash
python main.py organize <folder_path>
```

Example:

```bash
python main.py organize test_files
```

---

##  How It Works

The program:

1. Scans the specified folder
2. Detects each file’s extension
3. Maps it to a category (Images, Documents, etc.)
4. Moves the file into the appropriate folder

Example result:

```
test_files/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
```

---

## Safety Features

### Dry Run Mode

Preview changes before applying them.

### Duplicate Protection

If a file already exists in the destination:

```
Skipping photo.jpg (already exists)
```

### Summary Output

```
Summary:
Processed: 10
Moved: 8
Skipped: 2
```

---

## Testing on Real Files

Before running on important folders:

1. Always run with `--dry-run` first
2. Verify output carefully
3. Then run without `--dry-run`

Example for real use:

```bash
python main.py organize C:\Users\YourName\Downloads --dry-run
```

Then:

```bash
python main.py organize C:\Users\YourName\Downloads
```

---

## Tech Used

* Python
* pathlib
* argparse
* shutil

---
📝 Notes

This project includes extensive line-by-line comments as part of my learning process to document my understanding of Python and CLI development concepts.

---

## Author

Diana Balteanu

# 🗂️ Python File Organizer

A simple, beginner-friendly command-line tool that automatically sorts messy files into categorized folders based on their file extension — created as a **practice/learning project** to explore file handling, modular Python design, and the `os`/`shutil` standard libraries.

> 🧪 **Status:** Practice Project — built for learning purposes, not a production-grade file management tool.

---

## 📸 Preview

```
Enter folder path: C:\Users\vineet\Downloads

Scanning folder...

Moved photo1.jpg -> Images
Moved report.pdf -> Documents
Moved movie.mp4 -> Videos
Moved archive.zip -> Archives
Moved notes.txt -> Documents
Moved random.xyz -> Others
```

*(Each file gets moved into a neatly labeled subfolder inside the folder you specify — no more messy Downloads folder!)*

---

## ✨ Features

| Feature | Description |
|---|---|
| 📁 **Automatic Sorting** | Scans any folder you specify and moves files into categorized subfolders |
| 🧩 **Extension-Based Mapping** | Uses a simple, editable dictionary (`EXTENSION_MAP`) to decide where each file type belongs |
| 🖼️ **Built-in Categories** | Comes preconfigured with `Images`, `Videos`, `Documents`, and `Archives` |
| 🗑️ **Catch-All Bucket** | Any unrecognized extension is safely moved to an `Others` folder instead of being skipped |
| ✅ **Path Validation** | Checks that the folder path exists before attempting to organize anything |
| 🧱 **Modular Structure** | Code is split across `main.py`, `organizer.py`, `config.py`, and `utlis.py` for clarity and separation of concerns |
| 📦 **Zero Dependencies** | Built entirely with Python's standard library (`os`, `shutil`) — nothing extra to install |

---

## 🛠️ How It Works

The program flows through three main stages:

```
┌───────────────────┐     ┌────────────────────┐     ┌──────────────────────┐
│  Get Folder Path   │ ──▶ │  Validate Folder    │ ──▶ │  Organize & Move     │
│    (main.py)       │     │   (utlis.py)        │     │   (organizer.py)     │
└───────────────────┘     └────────────────────┘     └──────────────────────┘
```

### 1. `main.py`
- Prompts the user to enter a folder path.
- Calls `folder_exists()` to validate the path before doing anything else.
- If the folder exists, kicks off the organizing process via `organize_folder()`.

### 2. `utlis.py`
- Contains a single helper function, `folder_exists(path)`, which wraps `os.path.exists()` to confirm the target folder is real before the program tries to scan it.

### 3. `config.py`
- Stores the `EXTENSION_MAP` dictionary — a simple lookup table mapping file extensions (like `jpg`, `pdf`, `mp4`, `zip`) to human-readable category names (`Images`, `Documents`, `Videos`, `Archives`).
- This is the easiest place to extend the tool: just add a new `"extension": "Category"` entry.

### 4. `organizer.py`
- Lists every item in the target folder with `os.listdir()`.
- Skips anything that isn't a file (like existing subfolders).
- Extracts each file's extension with `os.path.splitext()` and looks it up in `EXTENSION_MAP`, defaulting to `"Others"` if the extension isn't recognized.
- Creates the destination category folder if it doesn't already exist (`os.makedirs(..., exist_ok=True)`).
- Moves the file into place using `shutil.move()`.
- Prints a confirmation line for every file moved, so you can watch the folder get cleaned up in real time.

---

## 📦 Requirements

- Python 3.6+
- No external dependencies — the project relies entirely on Python's built-in `os` and `shutil` modules.

---

## 🚀 Usage

```bash
python main.py
```

Then just follow the prompt:
1. Enter the full path to the folder you want to organize
2. Sit back and watch each file get sorted into `Images`, `Videos`, `Documents`, `Archives`, or `Others`

---

## 🔧 Customizing Categories

Want to sort more file types? Just open `config.py` and add new entries to `EXTENSION_MAP`:

```python
EXTENSION_MAP = {
    "jpg": "Images",
    "mp3": "Music",      # 👈 add your own mappings like this
    "py": "Code",
}
```

No other code changes needed — `organizer.py` automatically picks up new entries.

---

## 🧠 What This Project Demonstrates (Learning Goals)

This project was built to practice:
- ✅ Working with the `os` and `shutil` standard libraries for file system operations
- ✅ Splitting a small program into logical modules (`main`, `organizer`, `config`, `utils`)
- ✅ Using dictionaries as lightweight, extensible configuration/lookup tables
- ✅ Basic input validation before performing file system operations
- ✅ Safe folder creation with `exist_ok=True` to avoid errors on repeated runs
- ✅ Writing simple, readable feedback output for a CLI tool

---

## ⚠️ Disclaimer

This is a **practice/educational project**. It moves real files on your system, so always double-check the folder path you enter and consider testing on a sample/dummy folder first. It hasn't been hardened with extensive error handling (e.g. permission errors, duplicate filenames) — a great next step for further learning!

---

## 📄 License

Free to use for learning and practice purposes.

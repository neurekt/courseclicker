# CourseClicker

Lightweight tool that clicks anywhere on your screen at regular intervals.
---

## Quick Start

[Download the latest release](https://github.com/neurekt/courseclicker/releases)

### How to Use (Windows)

1. Extract the ZIP file
2. Double-click `courseclicker.exe`
3. Set your click position
4. Let it run while you do something else 

> No Python or install required.

## Developer Setup (Optional)

If you want to run or modify the Python code:

### Install Locally

```bash
git clone https://github.com/yourusername/courseclicker.git
cd courseclicker
```

(Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## How to Use

### Run with GUI (Default)

```bash
python src/courseclicker/main.py
```

Or, if installed:
```bash
courseclicker
```

In the GUI:
- Set the click interval (seconds)
- Click “Set Position” and hover over the target
- Click “Start Clicking”
- Stop or exit anytime

---

### Run with CLI

```bash
courseclicker --cli --interval 180
```

#### CLI Options

| Flag         | Description                             |
|--------------|-----------------------------------------|
| `--cli`      | Run without the GUI                     |
| `--interval` | Set interval in seconds (default: 180)  |
| `--reset`    | Reset and reselect the button position  |
| `--version`  | Show current version                    |

---

## Build Executable (Windows)

Build a standalone `.exe` (no Python needed to run):

Install PyInstaller:

```bash
pip install pyinstaller
```

Then build the app:

```bash
python build.py
```

This creates `courseclicker.exe` inside the `dist/` folder. You can now share or run this without Python installed.

---

## Development

Run the app in dev mode:
```bash
make run
```

Run tests:
```bash
make test
```

Clean build artifacts:
```bash
make clean
```

Or manually:
```bash
rm -rf build dist *.spec
```

---

## Project Structure

```
courseclicker/
├── src/
│   └── courseclicker/
│       ├── main.py
│       ├── __init__.py
├── tests/
│   └── test_basic.py
├── build.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE.txt
├── Makefile
├── .gitignore
```

---

## License

See `LICENSE.txt` for terms.

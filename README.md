## CourseClicker

This project clicks anywhere on your screen with configurable options and is currently run locally. I definitely did not build this to get me through my real estate course while sleeping. It supports both a GUI and command-line interface.

---

## Installation (Local)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/courseclicker.git
   cd courseclicker
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # On macOS/Linux
   .venv\Scripts\activate           # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Use

### Run with GUI (default)

```bash
python src/courseclicker/main.py
```

Or if installed as a CLI tool:
```bash
courseclicker
```

This opens a window where you can:
- Set the interval (in seconds)
- Click “Set Position” and hover over your target
- Click “Start Clicking” to begin
- Use “Stop Clicking” or “Exit” to stop

---

### Run from CLI

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

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build script:
   ```bash
   python build.py
   ```

This creates a standalone `.exe` in the `dist/` folder with your icon included.

---

## Development

### Run the app in dev mode

```bash
make run
```

### Run tests

```bash
make test
```

### Clean build artifacts

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

See `LICENSE.txt` for details.

# build.py
import shutil
import subprocess
from pathlib import Path

# Clean old folders and files
for target in ["build", "dist", "courseclicker.spec"]:
    path = Path(target)
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()

# Build a fresh .exe
subprocess.run([
    "pyinstaller",
    "--noconfirm",
    "--onefile",
    "--windowed",
    "--icon=courseclicker.ico",
    "--name=courseclicker",
    "--add-data=courseclicker.ico;.",  # <== Add this line exactly like this (Windows uses semicolon!)
    "src/courseclicker/main.py"
])
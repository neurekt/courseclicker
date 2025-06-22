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
    "--noconfirm",          # Don't ask questions
    "--onefile",            # Just one .exe file
    "--windowed",           # No terminal pop-up
    "--icon=courseclicker.ico",  # Your custom icon
    "src/courseclicker/main.py"  # Your app
])
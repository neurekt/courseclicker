import time, json, platform, sys, threading
from pathlib import Path
import pyautogui
from wakepy import keep
from courseclicker import __version__
import logging
import argparse
import tkinter as tk
from tkinter import messagebox
import os

# --- Setup logging ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
log = logging.getLogger("courseclicker")
CONFIG = Path.home() / ".courseclicker.json"

# --- OS Warnings ---
system = platform.system()
if system not in ("Windows", "Darwin", "Linux"):
    log.error(f"❌ Unsupported OS: {system}")
    sys.exit(1)
if system == "Darwin":
    log.info("🍎 macOS detected. Enable Accessibility permissions.")
elif system == "Linux":
    log.info("🐧 Linux detected. PyAutoGUI may not work under Wayland.")

# --- Helpers ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- CLI Arguments ---
def parse_args():
    parser = argparse.ArgumentParser(description="Courseclicker automation")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--interval", type=int, default=180, help="Seconds between clicks")
    parser.add_argument("--reset", action="store_true", help="Reset click position")
    parser.add_argument("--cli", action="store_true", help="Use command-line interface")
    return parser.parse_args()

# --- Position Setup ---
def setup_position():
    log.info("👉 Hover over your chosen target in 5 seconds…")
    time.sleep(5)
    p = pyautogui.position()
    CONFIG.write_text(json.dumps({"x": p.x, "y": p.y}))
    log.info(f"✅ Saved: {p}")
    return p

def load_position():
    if CONFIG.exists():
        try:
            d = json.loads(CONFIG.read_text())
            return pyautogui.Point(d["x"], d["y"])
        except (json.JSONDecodeError, KeyError) as e:
            log.warning(f"⚠️ Failed to load config, resetting: {e}")
    return setup_position()

# --- Clicker Loop ---
def run_click_loop(interval: int):
    pos = load_position()
    log.info("🛡️  Clicking every %s seconds. Ctrl+C to stop.", interval)
    with keep.running():
        try:
            while True:
                pyautogui.click(pos.x, pos.y)
                log.info(f"Clicked at {time.strftime('%H:%M:%S')}")
                time.sleep(interval)
        except KeyboardInterrupt:
            log.info("🛑 Stopped.")

# --- GUI Setup ---
def launch_gui():
    root = tk.Tk()
    root.iconbitmap(resource_path("courseclicker.ico"))
    root.title(f"CourseClicker v{__version__}")
    root.minsize(360, 320)
    root.configure(padx=20, pady=20)

    running = tk.BooleanVar(value=False)
    interval_var = tk.StringVar(value="180")

    # --- GUI functions ---
    def set_position():
        messagebox.showinfo("Set Position", "Hover over your chosen target in 5 seconds.")
        time.sleep(5)
        pos = pyautogui.position()
        CONFIG.write_text(json.dumps({"x": pos.x, "y": pos.y}))
        messagebox.showinfo("Saved", f"Position saved at: {pos}")

    def click_loop(interval):
        pos = load_position()
        with keep.running():
            while running.get():
                pyautogui.click(pos.x, pos.y)
                log.info(f"Clicked at {time.strftime('%H:%M:%S')}")
                time.sleep(interval)

    def start_clicking():
        try:
            interval = int(interval_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for interval.")
            return

        running.set(True)
        start_btn.config(state=tk.DISABLED)
        stop_btn.config(state=tk.NORMAL)
        thread = threading.Thread(target=click_loop, args=(interval,), daemon=True)
        thread.start()

    def stop_clicking():
        running.set(False)
        start_btn.config(state=tk.NORMAL)
        stop_btn.config(state=tk.DISABLED)

    # --- Layout ---
    tk.Label(root, text="CourseClicker", font=("Segoe UI", 18, "bold")).pack(pady=(0, 15))

    interval_frame = tk.Frame(root)
    interval_frame.pack(pady=(0, 10))
    tk.Label(interval_frame, text="Interval (seconds):", font=("Segoe UI", 11)).pack(side="left", padx=5)
    tk.Entry(interval_frame, textvariable=interval_var, font=("Segoe UI", 11), width=10, justify="center").pack(side="left", padx=5)

    tk.Button(root, text="Set Click Position", font=("Segoe UI", 10), command=set_position, width=30).pack(pady=5)
    start_btn = tk.Button(root, text="▶ Start", font=("Segoe UI", 10), command=start_clicking, width=30)
    start_btn.pack(pady=5)
    stop_btn = tk.Button(root, text="⏹ Stop", font=("Segoe UI", 10), command=stop_clicking, width=30, state=tk.DISABLED)
    stop_btn.pack(pady=5)
    tk.Button(root, text="❌ Exit", font=("Segoe UI", 10), command=root.destroy, width=30).pack(pady=(20, 0))

    root.mainloop()

# --- Entry Point ---
def main():
    args = parse_args()
    if len(sys.argv) == 1 or not args.cli:
        launch_gui()
    else:
        if args.reset:
            setup_position()
        run_click_loop(args.interval)

if __name__ == "__main__":
    main()
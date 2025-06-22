import time, json
from pathlib import Path
import pyautogui
from wakepy import keep

CONFIG = Path.home() / ".nextclick.json"
INTERVAL = 180  # seconds

def setup_position():
    print("👉 Hover over the 'Next' button in 5 seconds…")
    time.sleep(5)
    p = pyautogui.position()
    CONFIG.write_text(json.dumps({"x": p.x, "y": p.y}))
    print(f"✅ Saved: {p}")
    return p

def load_position():
    if CONFIG.exists():
        d = json.loads(CONFIG.read_text())
        return pyautogui.Point(d["x"], d["y"])
    return setup_position()

def main():
    pos = load_position()
    print("🛡️  Running with wake lock. Ctrl+C to stop.")
    with keep.running():
        try:
            while True:
                pyautogui.click(pos.x, pos.y)
                print(f"Clicked at {time.strftime('%H:%M:%S')}")
                time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print("\n🛑 Stopped.")
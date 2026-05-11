from pathlib import Path
from chrono_marco2.player.eye import Eye
import pyautogui
import time

if __name__ == "__main__":
    path = Path(__file__).parent / "data" / "tmp"
    path.mkdir(parents=True, exist_ok=True)
    screenshot_path = path / "tmp_screenshot.png"
    mini_map_title_path = path / "tmp_mini_map_title.png"
    mini_map_path = path / "tmp_mini_map.png"
    e = Eye(mini_map_title_path,  (59, 67, 165, 105), (8, 124, 205, 271))

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    e.save_screenshot(screenshot_path)
    e.save_current_frame_mini_map_title()
    e.save_current_frame_mini_map(mini_map_path)
    pyautogui.hotkey("alt", "tab")


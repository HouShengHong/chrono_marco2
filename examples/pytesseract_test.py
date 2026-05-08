from chrono_marco2.player.eye import Eye
import pytesseract
from PIL import Image
import time
from pathlib import Path
import pyautogui


if __name__ == "__main__":
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    path = Path(__file__).parent / "data" / "tmp"
    path.mkdir(parents=True, exist_ok=True)
    mini_map_title_path = path / "tmp_mini_map_title.png"
    mini_map_path = path / "tmp_mini_map.png"
    eye = Eye(mini_map_title_path, (60, 67, 161, 105), (8, 124, 248, 271))

    last_frame = eye.update_current_frame()

    custom_config = r"-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6"

    region = (8, 124, 248, 271)
    left, upper, right, lower = region

    roi_frame = last_frame[upper:lower, left:right] if last_frame is not None else None
    roi_img = Image.fromarray(roi_frame) if roi_frame is not None else None
    roi_text = pytesseract.image_to_string(roi_img, config=custom_config).strip()
    print(roi_text)

    pyautogui.hotkey("alt", "tab")

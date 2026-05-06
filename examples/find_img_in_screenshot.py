import pyautogui
import cv2
from pathlib import Path
import time

# 只在程式開始時讀取一次磁碟
path = Path().cwd() / "data" / "lie_detector" / "0.png"
print(path)

img = cv2.imread(path)

while 1:
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    t1 = time.time()
    pyautogui.useImageNotFoundException(False)
    location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
    t2 = time.time()

    print(t2 - t1)
    pyautogui.hotkey("alt", "tab")
    print(location)
    time.sleep(1)
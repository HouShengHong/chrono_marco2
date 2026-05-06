import dxcam
import time
import pyautogui

camera = dxcam.create()
camera.start(target_fps=60)

while 1:
    camera.get_latest_frame()
    time.sleep(1)

import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin
import alpha_setting
from chrono_marco2.common.action import KeyBinds


if __name__ == "__main__":
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    for i in range(5):
        KeyHolderWin("5",(0.1,0.1),(0.2,0.2)).hold()
    
    time.sleep(1)

    pyautogui.hotkey("alt", "tab")


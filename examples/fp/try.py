import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin
import alpha_setting
from chrono_marco2.common.action import KeyBinds




if __name__ == "__main__":
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)


    for i in range(1):
        KeyHolderWin(
            [
                alpha_setting.AttackKeys.explosion, 
                KeyBinds.left,
            ],
            (0.03, 0.06),
        ).hold()
    
    time.sleep(1)

    pyautogui.hotkey("alt", "tab")

    
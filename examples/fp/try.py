import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin
import alpha_setting
from chrono_marco2.common.action import KeyBinds


if __name__ == "__main__":
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    with pyautogui.hold(["k", "d", "space"]):
        for i in range(100):
            KeyHolderWin(
                [alpha_setting.AttackKeys.rush],
                (0.03, 0.06),
                (0.03, 0.06),
            ).hold()

    time.sleep(1)

    pyautogui.hotkey("alt", "tab")


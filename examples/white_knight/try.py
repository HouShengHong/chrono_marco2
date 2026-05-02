import alpha_setting
import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin

if __name__ == "__main__":
    a: KeyHolderWin = KeyHolderWin("7", (0.1, 0.1), (1.6, 1.6))
    b: KeyHolderWin = KeyHolderWin("8", (0.1, 0.1), (0.6, 0.6))
    c: KeyHolderWin = KeyHolderWin("9", (0.1, 0.1), (0.4, 0.4))
    d: KeyHolderWin = KeyHolderWin("0", (0.1, 0.1), (1.1, 1.1))
    att: KeyHolderWin = alpha_setting.normal_attack(["k"], hold_time=(0.03, 0.03))

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    for _ in range(5):
        d.hold()
        # b.hold()
        # b.hold()
        # att.hold()
    time.sleep(1)
    pyautogui.hotkey("alt", "tab")



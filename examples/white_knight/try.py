import alpha_setting
import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds

if __name__ == "__main__":
    hold_time = (0.08, 0.08)

    left_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.left], hold_time=hold_time
    )

    right_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.right], hold_time=hold_time
    )

    left_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
        direction_keys=[KeyBinds.left, KeyBinds.jump]
    )

    right_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
        direction_keys=[KeyBinds.right, KeyBinds.jump]
    )

    lightning_attack = alpha_setting.lightning_attack(
        [alpha_setting.AttackKeys.charged_blow]
    )

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    i = 5
    for _ in range(i):
        left_mid_jump.hold()
        left_lightning_rush.hold()
        lightning_attack.hold()
        lightning_attack.hold()

    for _ in range(i):
        right_mid_jump.hold()
        right_lightning_rush.hold()
        lightning_attack.hold()
        lightning_attack.hold()

    time.sleep(1)
    pyautogui.hotkey("alt", "tab")

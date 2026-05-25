import alpha_setting
import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds

if __name__ == "__main__":
    hold_time = (0.14, 0.14)

    left_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.left], hold_time=hold_time
    )

    right_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.right], hold_time=hold_time
    )

    left_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
        direction_keys=[KeyBinds.left, KeyBinds.jump],
        hold_time=(0.03, 0.03),
        end_sleep_time=(0.38, 0.38),
    )

    right_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
        direction_keys=[KeyBinds.right, KeyBinds.jump],
        hold_time=(0.03, 0.03),
        end_sleep_time=(0.38, 0.38),
    )

    lightning_attack = alpha_setting.lightning_attack(
        [alpha_setting.AttackKeys.charged_blow],
        hold_time=(0.03, 0.03),
        end_sleep_time=(0.48, 0.48),
    )

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    i = 5
    for _ in range(i):
        right_lightning_rush.hold()

    for _ in range(i):
        left_lightning_rush.hold()

    for _ in range(i * 4):
        lightning_attack.hold()

    time.sleep(1)
    pyautogui.hotkey("alt", "tab")

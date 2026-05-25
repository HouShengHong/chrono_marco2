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
        direction_keys=[KeyBinds.left],
        hold_time=(0.03, 0.03),
        end_sleep_time=(0.36, 0.36),
    )

    right_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
        direction_keys=[KeyBinds.right],
        hold_time=(0.03, 0.03),
        end_sleep_time=(0.365, 0.365),
    )

    lightning_attack = alpha_setting.lightning_attack(
        [alpha_setting.AttackKeys.charged_blow],
        hold_time=(0.03, 0.03),
        end_sleep_time=(0.48, 0.48),
    )

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    i = 20
    for _ in range(i):
        lightning_attack.hold()

    time.sleep(1)
    pyautogui.hotkey("alt", "tab")

import alpha_setting
import pyautogui
import time
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds

if __name__ == "__main__":
    hold_time = (0.27, 0.27)
    right_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.right]
    )

    left_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.left]
    )

    right_little_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.right], hold_time = hold_time
    )

    left_little_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.left], hold_time = hold_time
    )

    left_fire_rush: KeyHolderWin = alpha_setting.normal_rush(
        direction_keys=[KeyBinds.left, KeyBinds.jump]
    )
    right_fire_rush: KeyHolderWin = alpha_setting.normal_rush(
        direction_keys=[KeyBinds.right, KeyBinds.jump]
    )
    


    left_down_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.left, KeyBinds.down],
        hold_time = hold_time
    )

    right_down_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
        direction_keys=[KeyBinds.right, KeyBinds.down],
        hold_time = hold_time
    )


    normal_attack = alpha_setting.normal_attack([alpha_setting.AttackKeys.charged_blow])
    
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    i = 8
    for _ in range(i):
        left_little_jump.hold()
        left_fire_rush.hold()

        # right_little_jump.hold()
        # right_fire_rush.hold()


        # normal_attack.hold()
        # normal_attack.hold()
    for _ in range(i):
        # left_little_jump.hold()
        # left_fire_rush.hold()

        right_little_jump.hold()
        right_fire_rush.hold()


        # normal_attack.hold()
        # normal_attack.hold()
    time.sleep(1)
    pyautogui.hotkey("alt", "tab")



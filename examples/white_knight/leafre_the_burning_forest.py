from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds
from chrono_marco2.keeper import CountdownTimer

import alpha_setting

from pathlib import Path
import time
import random
import pyautogui


little_left: KeyHolderWin = KeyHolderWin([KeyBinds.left], (0.2, 0.2))
little_right: KeyHolderWin = KeyHolderWin([KeyBinds.right], (0.2, 0.2))
little_up: KeyHolderWin = KeyHolderWin([KeyBinds.up], (0.03, 0.06), (0.3, 0.3))

lightning_charge: KeyHolderWin = KeyHolderWin([alpha_setting.BuffKeys.lightning_charge], (0.03, 0.06), (0.1, 0.1))

right_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(direction_keys = [KeyBinds.right])
left_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(direction_keys = [KeyBinds.left])

right_down_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(direction_keys = [KeyBinds.right, KeyBinds.down])
left_down_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(direction_keys = [KeyBinds.left, KeyBinds.down])

left_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(direction_keys=[KeyBinds.left, KeyBinds.jump])
right_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(direction_keys=[KeyBinds.right, KeyBinds.jump])

left_lightning_rush_then_ice: KeyHolderWin = alpha_setting.lightning_rush(direction_keys=[KeyBinds.left], end_sleep_time=(0, 0))
right_lightning_rush_then_ice: KeyHolderWin = alpha_setting.lightning_rush(direction_keys=[KeyBinds.right], end_sleep_time=(0, 0))
then_ice: KeyHolderWin = KeyHolderWin([alpha_setting.BuffKeys.ice_charge], (0.19, 0.19), (0.19, 0.19))


normal_attack = alpha_setting.normal_attack([alpha_setting.AttackKeys.charged_blow])
normal_attack_then_lightning = alpha_setting.normal_attack([alpha_setting.AttackKeys.charged_blow], change_element_keys=[alpha_setting.BuffKeys.lightning_charge])

def how_to_play(player: Player):
        for keeper in player.keepers:
            keeper.do_on_finish()
        match player.eye.status.current_yellow_point_position_in_mini_map:
            # teleport point
            case (x, y) if 90 <= x <= 94 and 99 <= y <= 108:
                little_up.hold()

            # teleport point left
            case (x, y) if 86 <= x <= 89 and 99 <= y <= 108:
                little_right.hold()
                # normal_attack.hold()

            # teleport point right
            case (x, y) if 95 <= x <= 98 and 99 <= y <= 108:
                little_left.hold()
                # normal_attack.hold()
            
            # teleport point far left
            case (x, y) if 78 <= x <= 89 and 99 <= y <= 108:
                right_prev_jump.hold()
                normal_attack.hold()
            
            # teleport point far right
            case (x, y) if 95 <= x <= 106 and 99 <= y <= 108:
                left_prev_jump.hold()
                normal_attack.hold()

            # platform 3 left
            case (x, y) if 23 <= x <= 89 and 99 <= y <= 108:
                right_lightning_rush_then_ice.hold()
                then_ice.hold()
                normal_attack_then_lightning.hold()

            # platform 3 right
            case (x, y) if 95 <= x <= 180 and 99 <= y <= 108:
                left_lightning_rush_then_ice.hold()
                then_ice.hold()
                normal_attack_then_lightning.hold()

            # platform 0
            case (x, y) if 47 <= x <= 135 and 18 <= y <= 33:
                right_lightning_rush_then_ice.hold()
                then_ice.hold()
                normal_attack.hold()
                normal_attack.hold()
                right_down_prev_jump.hold()
                normal_attack_then_lightning.hold()

            # platform 1
            case (x, y) if 69 <= x <= 150 and 44 <= y <= 57:
                right_lightning_rush_then_ice.hold()
                then_ice.hold()
                normal_attack.hold()
                normal_attack.hold()
                right_down_prev_jump.hold()
                normal_attack_then_lightning.hold()

            # platform 2
            case (x, y) if 92 <= x <= 165 and 65 <= y <= 69:
                right_lightning_rush.hold()
                right_lightning_rush_then_ice.hold()
                then_ice.hold()
                normal_attack.hold()
                normal_attack.hold()
                right_down_prev_jump.hold()
                normal_attack_then_lightning.hold()
            
            case (x, y):
                right_down_prev_jump.hold()
                normal_attack.hold()

            case _:
                if random.random() < 0.5:
                    left_lightning_rush.hold()
                else: 
                    right_lightning_rush.hold()

if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "leafre_the_burning_forest.png"
    eye: Eye = Eye(path,MiniMapData.leafre_the_burning_forest["title"],MiniMapData.leafre_the_burning_forest["region"])
    keepers:CountdownTimer = [
        alpha_setting.BuffKeepers.booster, 
        alpha_setting.BuffKeepers.power_guard, 
        alpha_setting.BuffKeepers.nimble_feet,
        alpha_setting.BuffKeepers.pills
    ]
    player = Player(eye=eye, keepers=keepers)
    
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play)

    
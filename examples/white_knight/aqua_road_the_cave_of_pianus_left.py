from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds
from chrono_marco2.keeper import CountdownTimer, FreeMarketKeeper, BuffKeeper

import alpha_setting

from pathlib import Path
import time
import random
import pyautogui


little_left: KeyHolderWin = KeyHolderWin([KeyBinds.left], (0.2, 0.2))
little_right: KeyHolderWin = KeyHolderWin([KeyBinds.right], (0.2, 0.2))
little_up: KeyHolderWin = KeyHolderWin([KeyBinds.up], (0.03, 0.06), (0.3, 0.3))

left_big_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.left], hold_time=(0.24, 0.27)
)

right_big_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.right], hold_time=(0.24, 0.27)
)

right_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.right]
)
left_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.left]
)

right_down_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.right, KeyBinds.down]
)
left_down_prev_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.left, KeyBinds.down]
)

left_fire_rush: KeyHolderWin = alpha_setting.normal_rush(
    direction_keys=[KeyBinds.left, KeyBinds.jump]
)

right_fire_rush: KeyHolderWin = alpha_setting.normal_rush(
    direction_keys=[KeyBinds.right, KeyBinds.jump]
)

left_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
    direction_keys=[KeyBinds.left, KeyBinds.jump]
)

right_lightning_rush: KeyHolderWin = alpha_setting.lightning_rush(
    direction_keys=[KeyBinds.right, KeyBinds.jump]
)

normal_attack = alpha_setting.normal_attack([alpha_setting.AttackKeys.power_strike])
lightning_attack = alpha_setting.lightning_attack(
    [alpha_setting.AttackKeys.charged_blow]
)

right_power_strike: KeyHolderWin = KeyHolderWin(
    [KeyBinds.right, alpha_setting.AttackKeys.power_strike], (1, 1.2), (0, 0)
)

left_power_strike: KeyHolderWin = KeyHolderWin(
    [KeyBinds.left, alpha_setting.AttackKeys.power_strike], (1, 1.2), (0, 0)
)

threaten: BuffKeeper = BuffKeeper(
    80,
    None,
    [KeyHolderWin([alpha_setting.AttackKeys.threaten], (1, 1.2), (0.03, 0.03))],
)

left_threaten: BuffKeeper = BuffKeeper(
    80,
    None,
    [KeyHolderWin([KeyBinds.left, alpha_setting.AttackKeys.threaten], (1, 1.2), (0.03, 0.03))],
)

right_threaten: BuffKeeper = BuffKeeper(
    80,
    None,
    [KeyHolderWin([KeyBinds.right, alpha_setting.AttackKeys.threaten], (1, 1.2), (0.03, 0.03))],
)


def how_to_play(player: Player):
    for keeper in player.keepers:
        keeper.do_on_finish()

    match player.eye.status.current_yellow_point_position_in_mini_map:
        case (x, y) if 36 <= x <= 51 and 67 <= y <= 81:
            threaten.do_on_finish()
            right_power_strike.hold()

        case (x, y) if 52 <= x <= 70 and 67 <= y <= 81:
            threaten.do_on_finish()
            left_power_strike.hold()
        
        case (x, y):
            left_fire_rush.hold()
        
        case _:
            if random.random() < 0.5:
                right_prev_jump.hold()
            else:
                left_prev_jump.hold()
            normal_attack.hold()
            

if __name__ == "__main__":
    path = (
        Path().cwd() / "data" / "mini_map_titles" / "aqua_road_the_cave_of_pianus.png"
    )
    eye: Eye = Eye(
        path,
        MiniMapData.aqua_road_the_cave_of_pianus["title"],
        MiniMapData.aqua_road_the_cave_of_pianus["region"],
    )
    
    fire_charge_buff: BuffKeeper = BuffKeeper(
        850,
        None,
        [KeyHolderWin([alpha_setting.BuffKeys.fire_charge], (0.03, 0.06), (0.03, 0.03))],
    )

    skill_buffs: BuffKeeper = BuffKeeper(
        850,
        None,
        [
            KeyHolderWin([alpha_setting.BuffKeys.power_guard], (0.2, 0.3), (0.6, 0.6)),
            KeyHolderWin([alpha_setting.BuffKeys.booster], (0.2, 0.3), (0.4, 0.4)),
        ],
        True,
        1,
    )

    pills_buff: BuffKeeper = BuffKeeper(
        580,
        None,
        [
            KeyHolderWin([KeyBinds.buff_ins],  (0.03, 0.03), (0.03, 0.03)),
            KeyHolderWin([KeyBinds.buff_home], (0.03, 0.03), (0.03, 0.03)),
            KeyHolderWin([KeyBinds.buff_pgup], (0.03, 0.03), (0.03, 0.03)),
        ],
    )

    keepers: list[CountdownTimer] = [
        fire_charge_buff,
        skill_buffs,
        pills_buff,
    ]
    # keepers = []
    player = Player(eye=eye, keepers=keepers,alert_monitors=[])

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

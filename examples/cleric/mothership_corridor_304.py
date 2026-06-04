from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds
from chrono_marco2.keeper import CountdownTimer, FreeMarketKeeper
from mothership_corridor_104 import how_to_play

import alpha_setting

from pathlib import Path
import time
import random
import pyautogui

shining_ray_time: tuple[float, float] = (0.24, 0.27)

little_left: KeyHolderWin = KeyHolderWin([KeyBinds.left], (0.2, 0.2))
little_right: KeyHolderWin = KeyHolderWin([KeyBinds.right], (0.2, 0.2))
little_up: KeyHolderWin = KeyHolderWin([KeyBinds.up], (0.03, 0.06), (0.3, 0.3))

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

shining_ray_left: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.left,
    ],
    shining_ray_time,
)

shining_ray_right: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.right,
    ],
    shining_ray_time,
)

shining_ray_left_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.left,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_right_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.right,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_down_left_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.down,
        KeyBinds.left,
        KeyBinds.jump,
    ],
    shining_ray_time,
)

shining_ray_down_right_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.down,
        KeyBinds.right,
        KeyBinds.jump,
    ],
    shining_ray_time,
)

shining_ray_down_left_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.down,
        KeyBinds.left,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_down_right_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.down,
        KeyBinds.right,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_left_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.left,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_right_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.right,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_left_up_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.left,
        KeyBinds.up,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_right_up_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.right,
        KeyBinds.up,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    shining_ray_time,
)

shining_ray_little_up: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.up,
    ],
    (0.03, 0.06),
    (0.53, 0.5),
)

shining_ray_little_left: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.left,
    ],
    (0.03, 0.06),
)

shining_ray_little_right: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.shining_ray,
        KeyBinds.right,
    ],
    (0.03, 0.06),
)


if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "mothership_corridor_304.png"
    eye: Eye = Eye(
        path,
        MiniMapData.mothership_corridor_304["title"],
        MiniMapData.mothership_corridor_304["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 1200
    take_a_break_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.take_a_break
    take_a_break_keeper.refresh()
    take_a_break_keeper.refresh_other_free_market_keepers = [free_market_keeper]

    keepers: list[CountdownTimer] = [
        take_a_break_keeper,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        # alpha_setting.BuffKeepers.sugar_rush_candy,
        alpha_setting.BuffKeepers.summon_dragon,
        free_market_keeper,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)
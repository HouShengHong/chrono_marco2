from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds
from chrono_marco2.keeper import CountdownTimer, FreeMarketKeeper

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


def how_to_play(player: Player):

    if player.hand.status is None:
        player.hand.status = "l"
    elif player.eye.status.current_yellow_point_position_in_mini_map is None:
        player.hand.status = "l"
    elif 0 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 22:
        # 10 <= x
        player.hand.status = "r"
    elif 150 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 200:
        # x <= 187
        player.hand.status = "l"

    match player.eye.status.current_yellow_point_position_in_mini_map:
        # rope 0, 1
        case (x, y) if 40 <= x <= 42 or 152 <= x <= 155:
            if player.hand.status == "r":
                shining_ray_right_jump_rush.hold()
            else:
                shining_ray_left_jump_rush.hold()
        # platform 0
        case (x, y) if 48 <= y <= 62:
            if player.hand.status == "r":
                shining_ray_right_rush.hold()
            else:
                shining_ray_left_rush.hold()

        # platform 1
        case (x, y) if 0 <= x <= 40 and 65 <= y <= 83:
            shining_ray_left_up_jump_rush.hold()

        case (x, y) if 65 <= y <= 83:
            shining_ray_left_rush.hold()

        case (x, y):
            if random.random() < 0.5:
                shining_ray_right_jump_rush.hold()
            else:
                shining_ray_left_jump_rush.hold()
            print(f"where am i ? ,({x}, {y})")

        case _:
            shining_ray_left_jump_rush.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = (
        Path().cwd() / "data" / "mini_map_titles" / "hidden_street_bone_fish_cave.png"
    )
    eye: Eye = Eye(
        path,
        MiniMapData.hidden_street_bone_fish_cave["title"],
        MiniMapData.hidden_street_bone_fish_cave["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 600
    take_a_break_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.take_a_break
    take_a_break_keeper.refresh()
    take_a_break_keeper.refresh_other_free_market_keepers = [free_market_keeper]

    keepers: list[CountdownTimer] = [
        take_a_break_keeper,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        free_market_keeper,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

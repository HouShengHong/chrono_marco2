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

explosion_hold_time: tuple[float, float] = (0.24, 0.27)

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

explosion_right: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.right,
    ],
    explosion_hold_time,
)

explosion_left: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.left,
    ],
    explosion_hold_time,
)

explosion_right_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.right,
        KeyBinds.rush,
    ],
    explosion_hold_time,
)

explosion_left_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.left,
        KeyBinds.rush,
    ],
    explosion_hold_time,
)

explosion_down_right_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.down,
        KeyBinds.right,
        KeyBinds.jump,
    ],
    explosion_hold_time,
)

explosion_down_left_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.down,
        KeyBinds.left,
        KeyBinds.jump,
    ],
    explosion_hold_time,
)

explosion_down_right_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.down,
        KeyBinds.right,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    explosion_hold_time,
)

explosion_down_left_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.down,
        KeyBinds.left,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    explosion_hold_time,
)

explosion_right_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.right,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    explosion_hold_time,
)

explosion_left_jump_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.left,
        KeyBinds.jump,
        KeyBinds.rush,
    ],
    explosion_hold_time,
)

explosion_little_up: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.up,
    ],
    (0.03, 0.06),
    (0.3, 0.3),
)

explosion_little_left: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.left,
    ],
    (0.03, 0.06),
)

explosion_little_right: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.explosion,
        KeyBinds.right,
    ],
    (0.03, 0.06),
)


def how_to_play(player: Player):

    # if player.hand.status is None:
    #     player.hand.status = "r"
    # elif player.eye.status.current_yellow_point_position_in_mini_map is None:
    #     player.hand.status = "r"
    # elif 0 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 44:
    #     # 10 <= x
    #     player.hand.status = "r"
    # elif 165 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 200:
    #     # x <= 187
    #     player.hand.status = "l"
    #     lightning_attack.hold()

    match player.eye.status.current_yellow_point_position_in_mini_map:
        # platform 0
        case (x, y) if 139 <= x <= 160 and 12 <= y <= 47:
            explosion_down_left_jump.hold()

        case (x, y) if 63 <= x <= 160 and 12 <= y <= 37:
            if random.random() < 0.9:
                explosion_right_rush.hold()
            else:
                explosion_right_jump_rush.hold()

        # platform 1
        case (x, y) if 47 <= x <= 66 and 62 <= y <= 76:
            explosion_down_right_jump.hold()

        case (x, y) if 47 <= x <= 160 and 62 <= y <= 76:
            if random.random() < 0.9:
                explosion_left_rush.hold()
            else:
                explosion_left_jump_rush.hold()

        # platform 2
        # tp
        case (x, y) if 118 <= x <= 122 and 100 <= y <= 116:
            explosion_little_up.hold()
        # tp left
        case (x, y) if 107 <= x <= 117 and 100 <= y <= 116:
            explosion_little_right.hold()
        # tp right
        case (x, y) if 123 <= x <= 133 and 100 <= y <= 116:
            explosion_little_left.hold()
        # left
        case (x, y) if 46 <= x <= 106 and 100 <= y <= 116:
            if random.random() < 0.9:
                explosion_right_rush.hold()
            else:
                explosion_right_jump_rush.hold()
        # right
        case (x, y) if 123 <= x <= 158 and 100 <= y <= 116:
            if random.random() < 0.9:
                explosion_left_rush.hold()
            else:
                explosion_left_jump_rush.hold()

        case (x, y) if x <= 100:
            explosion_right_jump_rush.hold()

        case (x, y) if 100 <= x:
            explosion_left_jump_rush.hold()

        case (x, y):
            if random.random() < 0.5:
                explosion_right_jump_rush.hold()
            else:
                explosion_left_jump_rush.hold()

        case _:
            if random.random() < 0.5:
                explosion_right_jump_rush.hold()
            else:
                explosion_left_jump_rush.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "leafre_entrance_to_sky_nest.png"
    eye: Eye = Eye(
        path,
        MiniMapData.leafre_entrance_to_sky_nest["title"],
        MiniMapData.leafre_entrance_to_sky_nest["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 900
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

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

list_explosion_left_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.left,
    KeyBinds.jump,
]
list_explosion_right_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.right,
    KeyBinds.jump,
]

list_explosion_up_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.up,
    KeyBinds.jump,
]
list_explosion_left_up_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.left,
    KeyBinds.up,
    KeyBinds.jump,
]
list_explosion_right_up_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.right,
    KeyBinds.up,
    KeyBinds.jump,
]

list_explosion_down_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.down,
    KeyBinds.jump,
]
list_explosion_left_down_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.left,
    KeyBinds.down,
    KeyBinds.jump,
]
list_explosion_right_down_jump: list[str] = [
    alpha_setting.AttackKeys.explosion,
    KeyBinds.right,
    KeyBinds.down,
    KeyBinds.jump,
]

little_rush: KeyHolderWin = KeyHolderWin(
    [alpha_setting.AttackKeys.rush],
    (0.03, 0.06),
    (0.03, 0.06),
)

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
    if player.hand.status is None:
        player.hand.status = "r"
    elif player.eye.status.current_yellow_point_position_in_mini_map is None:
        player.hand.status = "r"
    elif 0 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 25:
        player.hand.status = "r"
    elif 225 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 248:
        player.hand.status = "l"

    match player.eye.status.current_yellow_point_position_in_mini_map:
        # # rope 0
        # case (x, y) if (41 <= x <= 44 and 35 <= y <= 88):
        #     random_holding_keys(player)
        #     alpha_setting.Actions.jump.hold()
        #     alpha_setting.Actions.frostbolt.hold()

        # # rope 1
        # case (x, y) if (124 <= x <= 127 and 35 <= y <= 88):
        #     random_holding_keys(player)
        #     alpha_setting.Actions.jump.hold()
        #     alpha_setting.Actions.frostbolt.hold()

        # # rope 2

        # case (x, y) if (206 <= x <= 209 and 35 <= y <= 88):
        #     random_holding_keys(player)
        #     alpha_setting.Actions.jump.hold()
        #     alpha_setting.Actions.frostbolt.hold()

        # platform -1
        case (x, y) if 35 <= y <= 48:
            if player.hand.status == "r":
                with pyautogui.hold(list_explosion_right_down_jump):
                    for _ in range(2):
                        little_rush.hold()
            else:
                with pyautogui.hold(list_explosion_left_down_jump):
                    for _ in range(2):
                        little_rush.hold()

        # platform 0
        case (x, y) if 49 <= y <= 54:
            if player.hand.status == "r":
                with pyautogui.hold(list_explosion_right_down_jump):
                    for _ in range(2):
                        little_rush.hold()
            else:
                with pyautogui.hold(list_explosion_left_down_jump):
                    for _ in range(2):
                        little_rush.hold()

        # platform 1
        case (x, y) if 58 <= y <= 71:
            if player.hand.status == "r":
                with pyautogui.hold(list_explosion_right_jump):
                    for _ in range(5):
                        little_rush.hold()
            else:
                with pyautogui.hold(list_explosion_left_jump):
                    for _ in range(5):
                        little_rush.hold()

        # platform 2 left
        case (x, y) if 0 <= x <= 41 and 73 <= y <= 90:
            with pyautogui.hold(list_explosion_right_jump):
                player.hand.status = "r"
                for _ in range(2):
                    little_rush.hold()

        # platform 2
        case (x, y) if 73 <= y <= 90:
            if player.hand.status == "r":
                with pyautogui.hold(list_explosion_right_up_jump):
                    for _ in range(2):
                        little_rush.hold()
            else:
                with pyautogui.hold(list_explosion_left_up_jump):
                    for _ in range(2):
                        little_rush.hold()

        case (x, y):
            if random.random() < 0.5:
                with pyautogui.hold(list_explosion_right_jump):
                    for _ in range(2):
                        little_rush.hold()
            else:
                with pyautogui.hold(list_explosion_left_jump):
                    for _ in range(2):
                        little_rush.hold()

        case _:
            if random.random() < 0.7:
                explosion_right_jump_rush.hold()
            else:
                explosion_left_jump_rush.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "mothership_corridor_104.png"
    eye: Eye = Eye(
        path,
        MiniMapData.mothership_corridor_104["title"],
        MiniMapData.mothership_corridor_104["region"],
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
        alpha_setting.BuffKeepers.sugar_rush_candy,
        free_market_keeper,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

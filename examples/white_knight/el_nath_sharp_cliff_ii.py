from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds
from chrono_marco2.keeper import BuffKeeper, CountdownTimer, FreeMarketKeeper

import alpha_setting

from pathlib import Path
import time
import random
import pyautogui


little_left: KeyHolderWin = KeyHolderWin([KeyBinds.left], (0.2, 0.2))
little_right: KeyHolderWin = KeyHolderWin([KeyBinds.right], (0.2, 0.2))
little_up: KeyHolderWin = KeyHolderWin([KeyBinds.up], (0.03, 0.06), (0.3, 0.3))
little_left_up: KeyHolderWin = KeyHolderWin([KeyBinds.left, KeyBinds.up], (0.2, 0.2))

left_big_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.left], hold_time=(0.24, 0.27)
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

normal_attack = alpha_setting.normal_attack([alpha_setting.AttackKeys.charged_blow])


def how_to_play(player: Player):
    match player.eye.status.current_yellow_point_position_in_mini_map:
        # teleport point
        case (x, y) if 69 <= x <= 73 and 72 <= y <= 83:
            little_up.hold()

        # teleport point left
        case (x, y) if 62 <= x <= 68 and 72 <= y <= 83:
            little_right.hold()

        # teleport point right
        case (x, y) if 74 <= x <= 76 and 72 <= y <= 83:
            little_left.hold()

        # teleport point far right
        case (x, y) if 77 <= x <= 80 and 72 <= y <= 83:
            little_left_up.hold()
            # if random.random() < 0.85:
            #     little_left.hold()
            # else:
            #     left_prev_jump.hold()

        # teleport point far left
        case (x, y) if 55 <= x <= 61 and 72 <= y <= 83:
            right_fire_rush.hold()

        # platform 3 left
        case (x, y) if 55 <= x <= 100 and 90 <= y <= 97:
            left_big_jump.hold()
            left_fire_rush.hold()

        # platform 3 right
        case (x, y) if 101 <= x <= 137 and 90 <= y <= 97:
            left_fire_rush.hold()
            left_fire_rush.hold()
            normal_attack.hold()

        # platform 0, 1, 2 left
        case (x, y) if 55 <= x <= 96 and 64 <= y <= 70:
            right_fire_rush.hold()
            right_fire_rush.hold()
            right_fire_rush.hold()
            right_down_prev_jump.hold()
            normal_attack.hold()

        # platform 0, 1, 2 right
        case (x, y) if 97 <= x <= 137 and 64 <= y <= 70:
            left_fire_rush.hold()
            left_fire_rush.hold()
            left_fire_rush.hold()
            left_down_prev_jump.hold()
            normal_attack.hold()

        case (x, y):
            if random.random() < 0.5:
                right_down_prev_jump.hold()
            else:
                left_down_prev_jump.hold()
            normal_attack.hold()

        case _:
            if random.random() < 0.5:
                left_fire_rush.hold()
            else:
                left_fire_rush.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "el_nath_sharp_cliff_ii.png"
    eye: Eye = Eye(
        path,
        MiniMapData.el_nath_sharp_cliff_ii["title"],
        MiniMapData.el_nath_sharp_cliff_ii["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 500
    take_a_break_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.take_a_break
    take_a_break_keeper.refresh()
    take_a_break_keeper.refresh_other_free_market_keepers = [free_market_keeper]

    keepers: list[CountdownTimer] = [
        take_a_break_keeper,
        alpha_setting.BuffKeepers.fire_charge,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        BuffKeeper(
            880,
            Path(__file__).parent / "keepers" / "red_bean_porridge.txt",
            [
                KeyHolderWin([KeyBinds.buff_end], (0.1, 0.3), (0.1, 0.3)),
            ],
        ),
        free_market_keeper,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

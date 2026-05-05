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

normal_attack = alpha_setting.normal_attack([alpha_setting.AttackKeys.charged_blow])
lightning_attack = alpha_setting.lightning_attack(
    [alpha_setting.AttackKeys.charged_blow]
)


def how_to_play(player: Player):

    # if player.hand.status is None:
    #     player.hand.status = "l"

    match player.eye.status.current_yellow_point_position_in_mini_map:
        # platform 0 left
        case (x, y) if 4 <= x <= 63 and 29 <= y <= 49:
            player.hand.status = "r"
            right_lightning_rush.hold()
            right_lightning_rush.hold()
            lightning_attack.hold()
            right_down_prev_jump.hold()
            lightning_attack.hold()

        # platform 0 right
        case (x, y) if 145 <= x <= 204 and 29 <= y <= 49:
            player.hand.status = "l"
            left_lightning_rush.hold()
            left_lightning_rush.hold()
            lightning_attack.hold()
            left_down_prev_jump.hold()
            lightning_attack.hold()

        # platform 1 left
        case (x, y) if 4 <= x <= 85 and 63 <= y <= 74:
            left_lightning_rush.hold()
            left_lightning_rush.hold()
            lightning_attack.hold()
            left_down_prev_jump.hold()
            lightning_attack.hold()

        # platform 1 right
        case (x, y) if 123 <= x <= 204 and 63 <= y <= 74:
            right_lightning_rush.hold()
            right_lightning_rush.hold()
            lightning_attack.hold()
            right_down_prev_jump.hold()
            lightning_attack.hold()

        # platform 2 left telepoint
        case (x, y) if 15 <= x <= 19 and 90 <= y <= 114:
            if player.hand.status == "r":
                right_lightning_rush.hold()
                lightning_attack.hold()
            else:
                little_up.hold()

        # platform 2 left telepoint left
        case (x, y) if 0 <= x <= 14 and 90 <= y <= 114:
            if player.hand.status == "r":
                right_lightning_rush.hold()
                lightning_attack.hold()
            else:
                little_right.hold()

        # platform 2 left telepoint right
        case (x, y) if 20 <= x <= 25 and 90 <= y <= 114:
            if player.hand.status == "r":
                right_lightning_rush.hold()
                lightning_attack.hold()
            else:
                little_left.hold()

        # platform 2 right telepoint
        case (x, y) if 190 <= x <= 194 and 90 <= y <= 114:
            if player.hand.status == "l":
                left_lightning_rush.hold()
                lightning_attack.hold()
            else:
                little_up.hold()

        # platform 2 right telepoint left
        case (x, y) if 184 <= x <= 189 and 90 <= y <= 114:
            if player.hand.status == "l":
                left_lightning_rush.hold()
                lightning_attack.hold()
            else:
                little_right.hold()

        # platform 2 right telepoint right
        case (x, y) if 195 <= x <= 207 and 90 <= y <= 114:
            if player.hand.status == "l":
                left_lightning_rush.hold()
                lightning_attack.hold()
            else:
                little_left.hold()

        # platform 2
        case (x, y) if 0 <= x <= 207 and 90 <= y <= 114:
            if player.hand.status == "r":
                right_lightning_rush.hold()
            else:
                left_lightning_rush.hold()

            lightning_attack.hold()

        case (x, y):
            if random.random() < 0.5:
                left_down_prev_jump.hold()
            else:
                right_down_prev_jump.hold()
            lightning_attack.hold()

        case _:
            player.hand.status = "l"
            if random.random() < 0.3:
                left_lightning_rush.hold()
            else:
                right_lightning_rush.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = (
        Path().cwd()
        / "data"
        / "mini_map_titles"
        / "leafre_battlefield_of_fire_and_darkness.png"
    )
    eye: Eye = Eye(
        path,
        MiniMapData.leafre_battlefield_of_fire_and_darkness["title"],
        MiniMapData.leafre_battlefield_of_fire_and_darkness["region"],
    )
    keepers: list[CountdownTimer] = [
        alpha_setting.BuffKeepers.lightning_charge,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        alpha_setting.BuffKeepers.free_market,
        alpha_setting.BuffKeepers.take_a_break,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

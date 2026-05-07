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

    match player.eye.status.current_yellow_point_position_in_mini_map:
        # platform 0 right
        case (x, y) if (59 <= x <= 65 and 6 <= y <= 18) or (
            0 <= x <= 41 and 10 <= y <= 22
        ):
            right_down_prev_jump.hold()

        # platform 1 left
        case (x, y) if 0 <= x <= 33 and 67 <= y <= 87:
            left_fire_rush.hold()
            left_down_prev_jump.hold()
            normal_attack.hold()

        # platform 1
        case (x, y) if 0 <= x <= 118 and 67 <= y <= 87:
            left_fire_rush.hold()
            # left_prev_jump.hold()
            normal_attack.hold()

        # platform 2 teleport point
        case (x, y) if 188 <= x <= 192 and 93 <= y <= 113:
            little_up.hold()

        # platform 2 teleport point left
        case (x, y) if 181 <= x <= 187 and 93 <= y <= 113:
            little_right.hold()

        # platform 2 teleport point right
        case (x, y) if 193 <= x <= 199 and 93 <= y <= 113:
            little_left.hold()

        # platform 2 teleport point far left
        case (x, y) if 174 <= x <= 180 and 93 <= y <= 113:
            right_prev_jump.hold()
            normal_attack.hold()

        # platform 2 teleport point far right
        case (x, y) if 200 <= x <= 206 and 93 <= y <= 113:
            left_prev_jump.hold()
            normal_attack.hold()

        # platform 2 regular platform left
        case (x, y) if 0 <= x <= 190 and 93 <= y <= 113:
            right_fire_rush.hold()
            # right_prev_jump.hold()
            normal_attack.hold()

        # platform 2 regular platform right
        case (x, y) if 190 <= x <= 255 and 93 <= y <= 113:
            left_fire_rush.hold()
            # left_prev_jump.hold()
            normal_attack.hold()

        # other platforms 0
        case (x, y) if 36 <= x <= 110 and 37 <= y <= 57:
            right_fire_rush.hold()
            right_down_prev_jump.hold()
            normal_attack.hold()

        # other platforms 1
        case (x, y) if 110 <= x <= 199 and 20 <= y <= 42:
            right_fire_rush.hold()
            right_down_prev_jump.hold()
            normal_attack.hold()

        # other platforms 2
        case (x, y) if 155 <= x <= 242 and 58 <= y <= 77:
            right_fire_rush.hold()
            right_down_prev_jump.hold()
            normal_attack.hold()

        # any platforms
        case (x, y):
            if random.random() < 0.5:
                left_down_prev_jump.hold()
            else:
                right_down_prev_jump.hold()
            normal_attack.hold()

        # other
        case _:
            if random.random() < 0.8:
                left_fire_rush.hold()
            else:
                right_fire_rush.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "leafre_dragon_forest_ii.png"
    eye: Eye = Eye(
        path,
        MiniMapData.leafre_dragon_forest_ii["title"],
        MiniMapData.leafre_dragon_forest_ii["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 2000
    take_a_break_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.take_a_break
    take_a_break_keeper.refresh()
    take_a_break_keeper.refresh_other_free_market_keepers = [free_market_keeper]

    keepers: list[CountdownTimer] = [
        take_a_break_keeper,
        alpha_setting.BuffKeepers.fire_charge,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        free_market_keeper,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

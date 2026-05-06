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
        # platform teleport 
        case (x, y) if 92 <= x <= 96 and 108 <= y <= 124:
            little_up.hold()
        
        # platform teleport left
        case (x, y) if 87 <= x <= 91 and 108 <= y <= 124:
            little_right.hold()
        
        # platform teleport left
        case (x, y) if 68 <= x <= 86 and 108 <= y <= 124:
            right_prev_jump.hold()
            normal_attack.hold()
        
        # platform teleport right
        case (x, y) if 97 <= x <= 101 and 108 <= y <= 124:
            little_left.hold()
        
        # platform teleport far right
        case (x, y) if 102 <= x <= 110 and 108 <= y <= 124:
            left_prev_jump.hold()
            normal_attack.hold()

        # platform most bottom left
        case (x, y) if 0 <= x <= 55 and 108 <= y <= 124:
            player.hand.status = "r"
            right_fire_rush.hold()
            right_prev_jump.hold()
            normal_attack.hold()
        
        # platform most bottom right
        case (x, y) if 141 <= x <= 200 and 108 <= y <= 124:
            player.hand.status = "l"
            left_fire_rush.hold()
            left_prev_jump.hold()
            normal_attack.hold()

        # platform most bottom 
        case (x, y) if 0 <= x <= 200 and 108 <= y <= 124:
            if player.hand.status == "l":
                left_fire_rush.hold()
                left_prev_jump.hold()
                normal_attack.hold()
            else:
                right_fire_rush.hold()
                right_prev_jump.hold()
                normal_attack.hold()
        
        # other platform left
        case (x, y) if 0 <= x <= 55:
            player.hand.status = "r"
            right_fire_rush.hold()
            right_down_prev_jump.hold()
            normal_attack.hold()
        
        # other platform right
        case (x, y) if 141 <= x <= 200:
            player.hand.status = "l"
            left_fire_rush.hold()
            left_down_prev_jump.hold()
            normal_attack.hold()

        # other platform
        case (x, y):
            if player.hand.status == "l":
                left_fire_rush.hold()
                left_down_prev_jump.hold()
                normal_attack.hold()
            else:
                right_fire_rush.hold()
                right_down_prev_jump.hold()
                normal_attack.hold()

        case _:
            player.hand.status = "r"
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
        / "hidden_street_the_hidden_dragon_tomb_ii.png"
    )
    eye: Eye = Eye(
        path,
        MiniMapData.hidden_street_the_hidden_dragon_tomb_ii["title"],
        MiniMapData.hidden_street_the_hidden_dragon_tomb_ii["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    take_a_break_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.take_a_break
    take_a_break_keeper.refresh()
    take_a_break_keeper.refresh_other_free_market_keepers = [free_market_keeper]

    keepers: list[CountdownTimer] = [
        alpha_setting.BuffKeepers.take_a_break,
        alpha_setting.BuffKeepers.fire_charge,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        alpha_setting.BuffKeepers.free_market,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

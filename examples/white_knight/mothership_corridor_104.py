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
    direction_keys=[KeyBinds.left], hold_time=(0.25, 0.30)
)

right_big_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.right], hold_time=(0.25, 0.30)
)

left_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.left], hold_time=(0.16, 0.2)
)

right_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.right], hold_time=(0.16, 0.2)
)

left_down_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.left, KeyBinds.down], hold_time=(0.35, 0.40)
)

right_down_mid_jump: KeyHolderWin = alpha_setting.attack_prev_jump(
    direction_keys=[KeyBinds.right, KeyBinds.down], hold_time=(0.35, 0.40)
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

r_list = [
    right_big_jump,
    right_mid_jump,
    right_down_mid_jump,
    right_down_prev_jump,
    right_lightning_rush,
]
l_list = [
    left_big_jump,
    left_mid_jump,
    left_down_mid_jump,
    left_down_prev_jump,
    left_lightning_rush,
]

normal_attack = alpha_setting.normal_attack([alpha_setting.AttackKeys.charged_blow])
lightning_attack = alpha_setting.lightning_attack(
    [alpha_setting.AttackKeys.charged_blow]
)


def how_to_play(player: Player):
    if player.hand.status is None:
        player.hand.status = r_list
    elif player.eye.status.current_yellow_point_position_in_mini_map is None:
        player.hand.status = r_list
    elif 0 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 35:
        player.hand.status = r_list
    elif 215 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 248:
        player.hand.status = l_list

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
            player.hand.status[3].hold()
            # player.hand.status[4].hold()
            lightning_attack.hold()
            # normal_attack.hold()

        # platform 0
        case (x, y) if 49 <= y <= 54:
            player.hand.status[3].hold()
            # player.hand.status[4].hold()
            lightning_attack.hold()
            # normal_attack.hold()

        # platform 1
        case (x, y) if 58 <= y <= 71:
            if random.random() < 0.55:
                player.hand.status[1].hold()
                player.hand.status[4].hold()
                player.hand.status[2].hold()
                player.hand.status[4].hold()

            else:
                player.hand.status[2].hold()
                player.hand.status[4].hold()
                player.hand.status[1].hold()
                player.hand.status[4].hold()

            lightning_attack.hold()
            # lightning_attack.hold()

        # platform 2
        case (x, y) if 73 <= y <= 90:
            player.hand.status[0].hold()
            player.hand.status[4].hold()
            lightning_attack.hold()
            # lightning_attack.hold()

        case (x, y):
            if random.random() < 0.5:
                right_prev_jump.hold()
            else:
                left_prev_jump.hold()
            lightning_attack.hold()

        case _:
            if random.random() < 0.7:
                right_lightning_rush.hold()
            else:
                right_lightning_rush.hold()

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
        alpha_setting.BuffKeepers.lightning_charge,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        free_market_keeper,
    ]

    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

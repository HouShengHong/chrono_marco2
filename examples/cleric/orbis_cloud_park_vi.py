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

heal_left: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.left,
        "f",
    ],
    explosion_hold_time,
)

heal_right: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.right,
        "f",
    ],
    explosion_hold_time,
)

heal_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.jump,
        "f",
    ],
    explosion_hold_time,
)

heal_down_left_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.down,
        KeyBinds.left,
        KeyBinds.jump,
        "f",
    ],
    (0.03, 0.06),
)

heal_right_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.right,
        KeyBinds.jump,
        "f",
    ],
    explosion_hold_time,
)

heal_left_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.left,
        KeyBinds.jump,
        "f",
    ],
    explosion_hold_time,
)

heal_down_right_jump: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.down,
        KeyBinds.right,
        KeyBinds.jump,
        "f",
    ],
    (0.03, 0.06),
)

heal_up_rush: KeyHolderWin = KeyHolderWin(
    [
        alpha_setting.AttackKeys.heal,
        KeyBinds.up,
        KeyBinds.rush,
        "f",
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
        # platform teleport
        # teleport
        case (x, y) if 33 <= x <= 37 and 90 <= y <= 104:
            little_up.hold()
        
        case (x, y) if 25 <= x <= 32 and 90 <= y <= 104:
            little_right.hold()

        case (x, y) if 38 <= x <= 53 and 90 <= y <= 104:
            little_left.hold()

        # platform 0
        case (x, y) if 150 <= x <= 161 and 20 <= y <= 53:
            heal_down_right_jump.hold()

        case (x, y) if 54 <= x <= 161 and 22 <= y <= 51:
            if random.random() < 0.9:
                heal_right.hold()
            else:
                heal_right_jump.hold()

        # platform 1
        case (x, y) if 54 <= x <= 65 and 54 <= y <= 80:
            heal_down_left_jump.hold()

        case (x, y) if 54 <= x <= 161 and 54 <= y <= 80:
            if random.random() < 0.9:
                heal_left.hold()
            else:
                heal_left_jump.hold()
        
        # platform 2
        case (x, y) if 113 <= x <= 124 and 88 <= y <= 104:
            heal_down_right_jump.hold()

        case (x, y) if 54 <= x <= 124 and 88 <= y <= 104:
            if random.random() < 0.9:
                heal_right.hold()
            else:
                heal_right_jump.hold()

        # platform 3
        # tp
        case (x, y) if 31 <= x <= 39 and 110 <= y <= 124:
            heal_right_jump.hold()
            heal_up_rush.hold()
        
        case (x, y) if 35 <= x <= 185 and 110 <= y <= 124:
            if random.random() < 0.9:
                heal_left.hold()
            else:
                heal_left_jump.hold()
        
        case (x, y) if 10 <= x <= 35 and 110 <= y <= 124:
            if random.random() < 0.9:
                heal_right.hold()
            else:
                heal_right_jump.hold()
        
        # other
        case (x, y):
            if random.random() < 0.5:
                heal_down_left_jump.hold()
            else:
                heal_down_right_jump.hold()

        case _:
            if random.random() < 0.5:
                heal_down_left_jump.hold()
            else:
                heal_down_right_jump.hold()

    for keeper in player.keepers:
        keeper.do_on_finish()


if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "orbis_cloud_park_vi.png"
    eye: Eye = Eye(
        path,
        MiniMapData.orbis_cloud_park_vi["title"],
        MiniMapData.orbis_cloud_park_vi["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 600
    take_a_break_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.take_a_break
    take_a_break_keeper.refresh()
    take_a_break_keeper.refresh_other_free_market_keepers = [free_market_keeper]

    keepers: list[CountdownTimer] = [
        take_a_break_keeper,
        alpha_setting.BuffKeepers.skill_buffs,
        # alpha_setting.BuffKeepers.pills,
        # alpha_setting.BuffKeepers.sugar_rush_candy,
        free_market_keeper,
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

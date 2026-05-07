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

fire_charge: KeyHolderWin = KeyHolderWin(
    [alpha_setting.BuffKeys.fire_charge], (0.03, 0.06), (0.1, 0.1)
)

lightning_charge: KeyHolderWin = KeyHolderWin(
    [alpha_setting.BuffKeys.lightning_charge], (0.03, 0.06), (0.1, 0.1)
)

r_list = [right_big_jump, right_lightning_rush]
l_list = [left_lightning_rush, lightning_attack]

# r_list = [right_big_jump, right_lightning_rush]
# l_list = [left_lightning_rush, lightning_attack]


def how_to_play(player: Player):

    if player.hand.status is None:
        player.hand.status = "r"
    elif player.eye.status.current_yellow_point_position_in_mini_map is None:
        player.hand.status = "r"
    elif 0 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 44:
        # 10 <= x
        player.hand.status = "r"
    elif 165 <= player.eye.status.current_yellow_point_position_in_mini_map[0] <= 200:
        # x <= 187
        player.hand.status = "l"

    match player.eye.status.current_yellow_point_position_in_mini_map:
        # platform 0
        case (x, y) if 48 <= y <= 62:
            if random.random() < 0.5:
                left_down_prev_jump.hold()
            else:
                right_down_prev_jump.hold()
            lightning_attack.hold()

        # platform 1
        case (x, y) if 65 <= y <= 83:
            if player.hand.status == "l":
                left_big_jump.hold()
                left_lightning_rush.hold()
                lightning_attack.hold()
                lightning_attack.hold()
            else:
                left_lightning_rush.hold()
                lightning_attack.hold()

        case (x, y):
            if random.random() < 0.5:
                left_down_prev_jump.hold()
            else:
                right_down_prev_jump.hold()
            lightning_attack.hold()
            print(f"where am i ? ,({x}, {y})")

        case _:
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
        / "hidden_street_risell_spuid_cave.png"
    )
    eye: Eye = Eye(
        path,
        MiniMapData.hidden_street_risell_spuid_cave["title"],
        MiniMapData.hidden_street_risell_spuid_cave["region"],
    )

    free_market_keeper: FreeMarketKeeper = alpha_setting.BuffKeepers.free_market
    free_market_keeper.duration = 600
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

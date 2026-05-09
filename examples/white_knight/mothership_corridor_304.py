from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.keeper import CountdownTimer, FreeMarketKeeper

import alpha_setting

from pathlib import Path
import time
import pyautogui

from mothership_corridor_104 import how_to_play

if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "mothership_corridor_304.png"
    eye: Eye = Eye(
        path,
        MiniMapData.mothership_corridor_304["title"],
        MiniMapData.mothership_corridor_304["region"],
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

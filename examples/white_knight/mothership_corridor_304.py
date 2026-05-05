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
    keepers: list[CountdownTimer] = [
        alpha_setting.BuffKeepers.fire_charge,
        alpha_setting.BuffKeepers.skill_buffs,
        alpha_setting.BuffKeepers.pills,
        alpha_setting.BuffKeepers.sugar_rush_candy,
        FreeMarketKeeper(1700, Path(__file__).parent / "keepers" / "fm.txt"),
    ]
    player = Player(eye=eye, keepers=keepers)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play, pre_do_keepers=True)

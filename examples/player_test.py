from chrono_marco2.player import Player
from chrono_marco2.player.eye import Eye
from chrono_marco2.common.mini_map_data import MiniMapData
from pathlib import Path
import time
import pyautogui

if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "leafre_the_burning_forest.png"
    eye: Eye = Eye(path,MiniMapData.leafre_the_burning_forest["title"],MiniMapData.leafre_the_burning_forest["region"])
    player = Player(eye=eye)
    def how_to_play(player: Player):
        # print("Playing the game...")
        pyautogui.press("x")
        time.sleep(1)
    
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    player.run(how_to_play)

from pathlib import Path
import pyautogui
import time
import datetime
from chrono_marco2.player.eye import Eye
from chrono_marco2.player.ear import Ear
from chrono_marco2.common.mini_map_data import MiniMapData

if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "hidden_street_cold_shark_cave.png"
    eye: Eye = Eye(
        path,
        MiniMapData.hidden_street_cold_shark_cave["title"],
        MiniMapData.hidden_street_cold_shark_cave["region"],
    )
    ear = Ear()

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    # eye.save_current_frame_mini_map_title()
    temp_set = set()
    while ear.is_running:
        eye.update_status()
        s = eye.status.current_is_same_map
        # print(f"Same map: {s}", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"))
        p = eye.status.current_yellow_point_position_in_mini_map
        p = (int(p[0]), int(p[1])) if p else None
        match (s, p,):
            case (True, p):
                if p is not None:
                    temp_set.add(p)
            case _:
                print(None)

    pyautogui.hotkey("alt", "tab")
    
    temp_list = list(temp_set)
    sorted_0 = sorted(temp_list, key=lambda x: (x[0], x[1]))
    sorted_1 = sorted(temp_list, key=lambda x: (x[1], x[0]))
    print(sorted_0)
    print("---------------------------")
    print(sorted_1)
    print("---------------------------")
    if len(temp_list) > 0:
        print(sorted_0[0], sorted_0[-1])
        print(sorted_1[0], sorted_1[-1])


    


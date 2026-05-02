from chrono_marco2.player.eye import Eye
from pathlib import Path
import time

if __name__ == "__main__":
    path = Path(__file__).parent / "data" / "tmp"
    path.mkdir(parents=True, exist_ok=True)
    mini_map_title_path = path / "tmp_mini_map_title.png"
    mini_map_path = path / "tmp_mini_map.png"
    eye = Eye(mini_map_title_path,(60, 67, 161, 105),(8, 124, 248, 271))

    time.sleep(1)

    for i in range(5):
        time1 = time.time()
        eye.update_status()
        time2 = time.time()
        print(f"update_status took {time2 - time1} seconds")
        print(eye.status.current_is_same_map)
        print(eye.status.current_yellow_point_position_in_mini_map)
        print(eye.status.current_red_point_position_in_mini_map)
        print("----")
        time.sleep(1)


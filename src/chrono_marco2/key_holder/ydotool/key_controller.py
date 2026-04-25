from .key_codes import KeyCodes
import subprocess
import random
import time


class KeyController:
    def key_down(self, key: int):
        subprocess.run(["ydotool", "key", f"{key}:1"])

    def keys_down(self, keys: list[int]):
        tmp_l: list[str] = ["ydotool", "key"]
        for key in keys:
            tmp_l.append(f"{key}:1")
        subprocess.run(tmp_l)

    def key_up(self, key: int):
        subprocess.run(["ydotool", "key", f"{key}:0"])

    def keys_up(self, keys: list[int]):
        tmp_l: list[str] = ["ydotool", "key"]
        for key in keys[::-1]:
            tmp_l.append(f"{key}:0")
        subprocess.run(tmp_l)

    def key_tap(self, key: int):
        subprocess.run(["ydotool", "key", f"{key}:1", f"{key}:0"])

    def keys_tap(self, keys: list[int]):
        self.keys_down(keys)
        self.keys_up(keys)

    def keys_hold(
        self,
        keys: list[int],
        hold_time: tuple[float, float],
        end_sleep_time: tuple[float, float],
    ):
        self.keys_down(keys)
        time.sleep(random.uniform(hold_time[0], hold_time[1]))
        self.keys_up(keys)
        time.sleep(random.uniform(end_sleep_time[0], end_sleep_time[1]))

    def key_reset(self):
        for _ in range(2):
            for key in KeyCodes:
                self.key_tap(key)

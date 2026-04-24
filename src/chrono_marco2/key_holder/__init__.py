import time
import pyautogui
import random

__all__ = ["KeyHolder"]

class KeyHolder:
    def __init__(
        self,
        hold_keys: list[str],
        hold_time:tuple[float, float],
        end_sleep_time:tuple[float, float] = (0,0),
        tap_key_holders: list["KeyHolder"] | None = None,
    ):
        self.hold_keys = hold_keys
        self.hold_time = hold_time
        self.end_sleep_time = end_sleep_time
        self.tap_key_holders = tap_key_holders
    
    def hold(self):
        with pyautogui.hold(self.hold_keys):
            if self.tap_key_holders is None:
                time.sleep(random.uniform(*self.hold_time))
            else:
                end_time = time.time() + random.uniform(*self.hold_time)
                while time.time() <= end_time:
                    for tap_key_holder in self.tap_key_holders:
                        tap_key_holder.hold()
        time.sleep(random.uniform(*self.end_sleep_time))
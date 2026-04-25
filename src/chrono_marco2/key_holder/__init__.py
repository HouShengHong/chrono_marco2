import time
import random
import platform

if platform.system() == "Windows":
    import pyautogui

from .ydotool import KeyController

__all__ = [
    "KeyHolder",
    "KeyHolderWin",
    "KeyHolderLinux",
    "KeyHolderByTime",
    "KeyHolderByTimeWin",
    "KeyHolderByTimeLinux",
]


class KeyHolder:
    def hold(self):
        pass


class KeyHolderWin(KeyHolder):
    def __init__(
        self,
        hold_keys: list[str],
        hold_time: tuple[float, float],
        end_sleep_time: tuple[float, float] = (0, 0),
        tap_key_holders: list["KeyHolderWin"] | None = None,
    ):
        self.hold_keys = hold_keys
        self.hold_time = hold_time
        self.end_sleep_time = end_sleep_time
        self.tap_key_holders = tap_key_holders

    def hold(self):
        with pyautogui.hold(self.hold_keys):  # type: ignore
            if self.tap_key_holders is None:
                time.sleep(random.uniform(*self.hold_time))
            else:
                end_time = time.time() + random.uniform(*self.hold_time)
                while time.time() <= end_time:
                    for tap_key_holder in self.tap_key_holders:
                        tap_key_holder.hold()
        time.sleep(random.uniform(*self.end_sleep_time))


class KeyHolderLinux(KeyHolder):
    def __init__(
        self,
        hold_keys: list[int],
        hold_time: tuple[float, float],
        end_sleep_time: tuple[float, float] = (0, 0),
        tap_key_holders: list[KeyHolderLinux] | None = None,
    ):
        self.hold_keys = hold_keys
        self.tap_key_holders = tap_key_holders
        self.hold_time = hold_time
        self.end_sleep_time = end_sleep_time

    def hold(self):
        if self.tap_key_holders is None:
            KeyController().keys_hold(
                self.hold_keys,
                self.hold_time,
                self.end_sleep_time,
            )
        else:
            end_time = time.time() + random.uniform(
                self.hold_time[0], self.hold_time[1]
            )
            KeyController().keys_down(self.hold_keys)
            while end_time >= time.time():
                for tap_key_holder in self.tap_key_holders:
                    tap_key_holder.hold()
            KeyController().keys_up(self.hold_keys)
            time.sleep(random.uniform(self.end_sleep_time[0], self.end_sleep_time[1]))


class KeyHolderByTime:
    def hold(self):
        pass


class KeyHolderByTimeWin(KeyHolderByTime):
    def __init__(
        self,
        end_sleep_time: tuple[float, float],
        *keys: tuple[list[str], tuple[float, float]],
    ) -> None:
        self.keys = keys
        self.end_sleep_time = end_sleep_time

    def hold(self):
        key_iter = iter(self.keys)

        def do():
            try:
                keys, hold_time = next(key_iter)
                with pyautogui.hold(keys):  # type: ignore
                    time.sleep(random.uniform(*hold_time))
                    do()
            except StopIteration as _:
                pass

        do()
        time.sleep(random.uniform(*self.end_sleep_time))


class KeyHolderByTimeLinux(KeyHolderByTime):
    def __init__(
        self,
        end_sleep_time: tuple[float, float],
        *holdkey_and_times: tuple[list[int], tuple[float, float]],
    ) -> None:
        self.holdkey_and_times = holdkey_and_times
        self.end_sleep_time = end_sleep_time

    def hold(self):
        key_iter = iter(self.holdkey_and_times)

        def do():
            try:
                t1 = time.time()
                keys, hold_time = next(key_iter)
                KeyController().keys_down(keys)
                time.sleep(random.uniform(*hold_time))
                t2 = time.time()
                print("\n", t2 - t1)
                do()
            except StopIteration as _:
                t1 = time.time()
                for keys, _ in self.holdkey_and_times[::-1]:
                    KeyController().keys_up(keys)
                time.sleep(random.uniform(*self.end_sleep_time))
                t2 = time.time()
                print("\n", t2 - t1)

        do()

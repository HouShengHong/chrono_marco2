import time
from pathlib import Path
import pyautogui
from chrono_marco2.key_holder import KeyHolderLinux, KeyHolderWin, KeyHolder
from chrono_marco2.common import KeyBinds
from chrono_marco2.common.action import auto_fm_go_into_and_sell_equips_and_leave

__all__ = ["CountdownTimer", "BuffKeeper", "FreeMarketKeeper"]


class CountdownTimer:
    def __init__(
        self,
        duration: float,
        refresh_file: Path | None = None,
    ):
        self.duration = duration
        self.refresh_file = refresh_file
        self.refresh_time: float = 0.0
        if self.refresh_file:
            self.refresh_file.parent.mkdir(parents=True, exist_ok=True)
            if self.refresh_file.exists():
                self.refresh_time = float(self.refresh_file.read_text())
            else:
                self.refresh_file.write_text(str(self.refresh_time))
        else:
            self.refresh_time: float = 0.0

    def is_time_up(self) -> bool:
        return time.time() >= self.refresh_time

    def refresh(self, delay_time: float | None = None):
        delay_time = delay_time if delay_time is not None else self.duration
        self.refresh_time = time.time() + delay_time
        if self.refresh_file:
            self.refresh_file.write_text(str(self.refresh_time))

    def do_something(self):
        print("You should do something!")

    def do_on_finish(self):
        if self.is_time_up():
            self.do_something()
            self.refresh()


class BuffKeeper(CountdownTimer):
    def __init__(
        self,
        duration: float,
        refresh_file: Path | None,
        buff_key_holders: list[KeyHolder] | list[KeyHolderWin] | list[KeyHolderLinux],
        double_buff: bool = False,
        pre_buff_sleep_time: float = 0,
    ):
        super().__init__(duration, refresh_file)
        self.buff_key_holders = buff_key_holders
        self.double_buff = double_buff
        self.pre_buff_sleep_time = pre_buff_sleep_time

    def rebuff(self):
        time.sleep(self.pre_buff_sleep_time)
        for key_holder in self.buff_key_holders:
            if self.double_buff:
                origin_hold_time = key_holder.hold_time
                origin_end_sleep_time = key_holder.end_sleep_time

                key_holder.hold_time = (0.03, 0.06)
                key_holder.end_sleep_time = (0.1, 0.2)
                key_holder.hold()

                key_holder.hold_time = origin_hold_time
                key_holder.end_sleep_time = origin_end_sleep_time

            key_holder.hold()

    def do_something(self):
        self.rebuff()


class FreeMarketKeeper(CountdownTimer):
    def __init__(
        self,
        duration: float,
        refresh_file: Path | None = None,
        # self
        refresh_other_free_market_keepers: list[FreeMarketKeeper] | None = None,
        left_key: str = KeyBinds.left,
        right_key: str = KeyBinds.right,
        item_key: str = KeyBinds.item,
        trade_button_position: tuple[int, int] = (876, 715),
        sell_equips_button_position: tuple[int, int] = (867, 193),
        ok_button_position: tuple[int, int] = (689, 408),
        npc_chat_key_holder: KeyHolder | None = None,
        up_key_holder: KeyHolder | None = None,
        sell_equips_walk_repeat_time: int = 30,
        leave_walk_repeat_time: int = 40,
        after_go_into_fm_sleep_time: float = 10,
        after_sell_equips_sleep_time: float = 1,
        after_leave_fm_sleep_time: float = 5,
    ):
        super().__init__(duration, refresh_file)
        self.left_key = left_key
        self.right_key = right_key
        self.refresh_other_free_market_keepers = refresh_other_free_market_keepers
        self.item_key = item_key
        self.trade_button_position = trade_button_position
        self.sell_equips_button_position = sell_equips_button_position
        self.ok_button_position = ok_button_position
        self.npc_chat_key_holder = npc_chat_key_holder
        self.up_key_holder = up_key_holder
        self.sell_equips_walk_repeat_time = sell_equips_walk_repeat_time
        self.leave_walk_repeat_time = leave_walk_repeat_time
        self.after_go_into_fm_sleep_time = after_go_into_fm_sleep_time
        self.after_sell_equips_sleep_time = after_sell_equips_sleep_time
        self.after_leave_fm_sleep_time = after_leave_fm_sleep_time

    def do_something(self):
        auto_fm_go_into_and_sell_equips_and_leave(
            self.left_key,
            self.right_key,
            self.item_key,
            self.trade_button_position,
            self.sell_equips_button_position,
            self.ok_button_position,
            self.npc_chat_key_holder,
            self.up_key_holder,
            self.sell_equips_walk_repeat_time,
            self.leave_walk_repeat_time,
            self.after_go_into_fm_sleep_time,
            self.after_sell_equips_sleep_time,
            self.after_leave_fm_sleep_time,
        )

        if self.refresh_other_free_market_keepers is not None:
            for keeper in self.refresh_other_free_market_keepers:
                keeper.refresh()

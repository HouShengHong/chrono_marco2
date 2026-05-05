import pyautogui
import time
from chrono_marco2.common import KeyBinds
from chrono_marco2.key_holder import KeyHolderWin, KeyHolder


def go_into_fm(trade_button_position: tuple[int, int] = (876, 715)):
    pyautogui.click(*trade_button_position)


def sell_equips(
    left_key: str = KeyBinds.left,
    right_key: str = KeyBinds.right,
    item_key: str = KeyBinds.item,
    sell_equips_button_position: tuple[int, int] = (867, 193),
    ok_button_position: tuple[int, int] = (689, 408),
    npc_chat_key_holder: KeyHolder | None = None,
    sell_equips_walk_repeat_time: int = 30,
):
    npc_chat_key_holder = (
        npc_chat_key_holder
        if npc_chat_key_holder is not None
        else KeyHolderWin([KeyBinds.chat_npc], (0.05, 0.05), (0.05, 0.05))
    )

    with pyautogui.hold(left_key):
        for _ in range(sell_equips_walk_repeat_time):
            npc_chat_key_holder.hold()

    with pyautogui.hold(right_key):
        for _ in range(sell_equips_walk_repeat_time):
            npc_chat_key_holder.hold()

    pyautogui.click(*sell_equips_button_position)
    time.sleep(1)
    pyautogui.click(*ok_button_position)
    time.sleep(1)
    KeyHolderWin([KeyBinds.esc], (0.05, 0.05), (0.05, 0.05)).hold()
    KeyHolderWin([item_key], (0.05, 0.05), (0.05, 0.05)).hold()


def leave_fm(
    right_key: str = KeyBinds.right,
    up_key_holder: KeyHolder | None = None,
    leave_walk_repeat_time: int = 40,
):
    up_key_holder = (
        up_key_holder
        if up_key_holder is not None
        else KeyHolderWin([KeyBinds.up], (0.05, 0.05), (0.05, 0.05))
    )

    with pyautogui.hold(right_key):
        for _ in range(leave_walk_repeat_time):
            up_key_holder.hold()


def auto_fm_go_into_and_sell_equips_and_leave(
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
    go_into_fm(trade_button_position)
    time.sleep(after_go_into_fm_sleep_time)
    sell_equips(
        left_key,
        right_key,
        item_key,
        sell_equips_button_position,
        ok_button_position,
        npc_chat_key_holder,
        sell_equips_walk_repeat_time,
    )
    time.sleep(after_sell_equips_sleep_time)
    leave_fm(right_key, up_key_holder, leave_walk_repeat_time)
    time.sleep(after_leave_fm_sleep_time)

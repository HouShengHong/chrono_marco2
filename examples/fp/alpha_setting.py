from chrono_marco2.key_holder import KeyHolderWin
from chrono_marco2.common import KeyBinds
from chrono_marco2.keeper import BuffKeeper, FreeMarketKeeper
from pathlib import Path


attack_hold_time: tuple[float, float] = (0.03, 0.06)
attack_end_sleep_time: tuple[float, float] = (0.59, 0.59)

attack_end_sleep_time_20off: tuple[float, float] = (0.52, 0.52)
attack_end_sleep_time_40off: tuple[float, float] = (0.38, 0.38)

attack_prev_jump_hold_time: tuple[float, float] = (0.02, 0.02)


class AttackKeys:
    rush: str = KeyBinds.rush
    fire_arrow: str = KeyBinds.att_j
    explosion: str = KeyBinds.att_k
    poison_mist: str = KeyBinds.att_l


class BuffKeys:
    spell_booster: str = KeyBinds.buff_7
    meditation: str = KeyBinds.buff_8
    magic_guard: str = KeyBinds.buff_9
    nimble_feet: str = KeyBinds.buff_0


class BuffKeepers:
    skill_buffs: BuffKeeper = BuffKeeper(
        430,
        Path(__file__).parent / "keepers" / "skill_buffs.txt",
        [
            KeyHolderWin([BuffKeys.spell_booster], (0.2, 0.3), (1.5, 1.5)),
            KeyHolderWin([BuffKeys.meditation], (0.2, 0.3), (0.8, 0.8)),
            KeyHolderWin([BuffKeys.magic_guard], (0.2, 0.3), (1.3, 1.3)),
            KeyHolderWin([BuffKeys.nimble_feet], (0.2, 0.3), (1.1, 1.1)),
        ],
        True,
        1,
    )
    spell_booster: BuffKeeper = BuffKeeper(
        430,
        Path(__file__).parent / "keepers" / "spell_booster.txt",
        [KeyHolderWin([BuffKeys.spell_booster], (0.2, 0.3), (1.5, 1.5))],
        True,
        1,
    )
    meditation: BuffKeeper = BuffKeeper(
        430,
        Path(__file__).parent / "keepers" / "meditation.txt",
        [KeyHolderWin([BuffKeys.meditation], (0.2, 0.3), (0.8, 0.8))],
        True,
        1,
    )
    magic_guard: BuffKeeper = BuffKeeper(
        430,
        Path(__file__).parent / "keepers" / "magic_guard.txt",
        [KeyHolderWin([BuffKeys.magic_guard], (0.2, 0.3), (1.3, 1.3))],
        True,
        1,
    )
    nimble_feet: BuffKeeper = BuffKeeper(
        430,
        Path(__file__).parent / "keepers" / "nimble_feet.txt",
        [KeyHolderWin([BuffKeys.nimble_feet], (0.2, 0.3), (1.1, 1.1))],
        True,
        1,
    )

    pills: BuffKeeper = BuffKeeper(
        580,
        Path(__file__).parent / "keepers" / "pills.txt",
        [
            # KeyHolderWin([KeyBinds.buff_ins], (0.1, 0.3), (0.1, 0.3)),
            KeyHolderWin([KeyBinds.buff_home], (0.1, 0.3), (0.1, 0.3)),
            # KeyHolderWin([KeyBinds.buff_pgup], (0.1, 0.3), (0.1, 0.3)),
        ],
    )

    sugar_rush_candy: BuffKeeper = BuffKeeper(
        880,
        Path(__file__).parent / "keepers" / "sugar_rush_candy.txt",
        [
            KeyHolderWin([KeyBinds.buff_pgdn], (0.1, 0.3), (0.1, 0.3)),
        ],
    )

    free_market: FreeMarketKeeper = FreeMarketKeeper(
        600, Path(__file__).parent / "keepers" / "fm.txt"
    )

    take_a_break: FreeMarketKeeper = FreeMarketKeeper(
        3600,
        Path(__file__).parent / "keepers" / "take_a_break.txt",
        after_sell_equips_sleep_time=300,
    )


def action_template(
    main_keys: list[str],
    direction_keys: list[str] | None = None,
    change_element_keys: list[str] | None = None,
    hold_time: tuple[float, float] = (0, 0),
    end_sleep_time: tuple[float, float] = (0, 0),
) -> KeyHolderWin:
    direction_keys = direction_keys if direction_keys is not None else []
    change_element_keys = change_element_keys if change_element_keys is not None else []
    action: KeyHolderWin = KeyHolderWin(
        direction_keys + main_keys + change_element_keys, hold_time, end_sleep_time
    )
    return action


def attack_prev_jump(
    jump_keys: list[str] | None = None,
    direction_keys: list[str] | None = None,
    change_element_keys: list[str] | None = None,
    hold_time: tuple[float, float] = attack_prev_jump_hold_time,
    end_sleep_time: tuple[float, float] = (0, 0),
) -> KeyHolderWin:
    jump_keys = jump_keys if jump_keys is not None else [KeyBinds.jump]
    return action_template(
        jump_keys, direction_keys, change_element_keys, hold_time, end_sleep_time
    )


def normal_attack(
    main_keys: list[str],
    direction_keys: list[str] | None = None,
    change_element_keys: list[str] | None = None,
    hold_time: tuple[float, float] = attack_hold_time,
    end_sleep_time: tuple[float, float] = attack_end_sleep_time,
) -> KeyHolderWin:
    return action_template(
        main_keys, direction_keys, change_element_keys, hold_time, end_sleep_time
    )


def lightning_attack(
    main_keys: list[str],
    direction_keys: list[str] | None = None,
    change_element_keys: list[str] | None = None,
    hold_time: tuple[float, float] = attack_hold_time,
    end_sleep_time: tuple[float, float] = attack_end_sleep_time_20off,
) -> KeyHolderWin:
    return action_template(
        main_keys, direction_keys, change_element_keys, hold_time, end_sleep_time
    )


def normal_rush(
    rush_keys: list[str] | None = None,
    direction_keys: list[str] | None = None,
    # change_element_keys: list[str] | None = None,
    hold_time: tuple[float, float] = attack_hold_time,
    end_sleep_time: tuple[float, float] = attack_end_sleep_time_20off,
) -> KeyHolderWin:
    rush_keys = rush_keys if rush_keys is not None else [KeyBinds.rush]
    return action_template(rush_keys, direction_keys, None, hold_time, end_sleep_time)


def lightning_rush(
    rush_keys: list[str] | None = None,
    direction_keys: list[str] | None = None,
    # change_element_keys: list[str] | None = None,
    hold_time: tuple[float, float] = attack_hold_time,
    end_sleep_time: tuple[float, float] = attack_end_sleep_time_40off,
) -> KeyHolderWin:
    rush_keys = rush_keys if rush_keys is not None else [KeyBinds.rush]
    return action_template(rush_keys, direction_keys, None, hold_time, end_sleep_time)

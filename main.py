from chrono_marco2.key_holder import KeyHolder
from chrono_marco2.common import KeyBinds


if __name__ == "__main__":
    k = KeyHolder(["a"],(5,5),tap_key_holders=[KeyHolder([KeyBinds.att_4],(0.1,0.1),(0.1,0.1)), KeyHolder([KeyBinds.buff_0],(0.1,0.1),(0.1,0.1))])
    k.hold()
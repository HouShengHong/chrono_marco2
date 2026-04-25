import time
import platform
from chrono_marco2.key_holder import (
    KeyHolderByTimeLinux,
    KeyHolderByTimeWin,
    KeyHolderByTime,
)
from chrono_marco2.key_holder.ydotool.key_controller import KeyController, KeyCodes


if __name__ == "__main__":
    system_name = platform.system()
    print(system_name)
    time.sleep(5)

    # k: KeyHolderByTime = KeyHolderByTimeLinux(
    #     (4, 4),
    #     ([KeyCodes.d, KeyCodes.space], (3, 3)),
    #     ([KeyCodes.j], (2, 2)),
    # )
    # k.hold()

    k: KeyHolderByTime = KeyHolderByTimeWin(
        (4, 4),
        (["d", "space"], (3, 3)),
        (["j"], (2, 2)),
    )
    k.hold()

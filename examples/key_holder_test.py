from chrono_marco2.key_holder import KeyHolderWin
import time
import pyautogui

if __name__ == "__main__":
    pyautogui.hotkey("alt", "tab")


    time.sleep(1)
    
    key_holder = KeyHolderWin(
        hold_keys=["d","space"],
        # hold_keys=[],
        hold_time=(6.9, 6.9),
        end_sleep_time=(0, 0),
        hold_then_tap_sleep_time=(0.01, 0.01),
        tap_key_holders=[
            KeyHolderWin(
                hold_keys=["j"],
                hold_time=(0.04, 0.04),
                end_sleep_time=(0.66, 0.66),
            ),
        ],
    )
    key_holder1 = KeyHolderWin(
        hold_keys=["j"],
        hold_time=(0.5, 0.5),
        end_sleep_time=(0.18, 0.18),
    )
    time0 = time.time()
    with pyautogui.hold(["a", "space"]): 
        time.sleep(0.02)
        for i in range(20):
            key_holder1.hold()
    time1 = time.time()
    print(f"Total time taken to hold keys: {time1 - time0}")

    time.sleep(1)
    pyautogui.hotkey("alt", "tab")
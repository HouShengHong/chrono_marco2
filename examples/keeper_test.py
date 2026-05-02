from chrono_marco2.keeper import BuffKeeper, FreeMarketKeeper
from chrono_marco2.key_holder import KeyHolderWin
import time
from pathlib import Path
import pyautogui

if __name__ == "__main__":
    path = Path(__file__).parent / "data" / "keeper_test" / "tmp.txt"
    key_holder0 = KeyHolderWin(["home"],(0.5,0.5),(0.5,0.5))
    k = FreeMarketKeeper(30,path)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    for i in range(100):
        k.do_on_finish()
        time.sleep(1)
    
    time.sleep(1)
    print("i stopped")
    pyautogui.hotkey("alt", "tab")

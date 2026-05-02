from chrono_marco2.key_holder import KeyHolderWin
import pyautogui
import time

if __name__ == "__main__":
    # e = Ear()
    # while e.is_running:
    #     if e.is_paused:
    #         print("i am pausing")
    #         time.sleep(1)
    #     else:
    #         print("i am running")
    #         time.sleep(1)
    
    # print("i stopped")
    kh: KeyHolderWin = KeyHolderWin(["a", "k", "p"], (0.03, 0.03), (0.64, 0.64))
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    for i in range(1):
        kh.hold()
        # with pyautogui.hold(["s", "space"]):
        #     time.sleep(0.02)
        # with pyautogui.hold(["k"]):
        #     time.sleep(0.03)
        # time.sleep(1)
    time.sleep(1)
    pyautogui.hotkey("alt", "tab")


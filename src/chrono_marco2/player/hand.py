from typing import Any
import pyautogui

class Hand:
    def __init__(self,
        # holding_keys: list[str] | None = None, 
        status: Any = None,
    ):
        self.holding_keys: list[str] =  []
        self.status = status

    def reset_holding_keys(self):
        for key in self.holding_keys:
            pyautogui.press(key)
        self.holding_keys = []
    
    def update_holding_keys(self, keys: list[str]):
        self.reset_holding_keys()
        self.holding_keys = keys
        for key in self.holding_keys:
            pyautogui.keyDown(key)
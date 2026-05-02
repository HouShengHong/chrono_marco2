from pynput import keyboard

class Ear:
    def __init__(self,
        pause_key: keyboard.Key = keyboard.Key.f8,
        stop_key: keyboard.Key = keyboard.Key.f9,
        keyboard_listener: keyboard.Listener | None = None,

    ):
        self.pause_key = pause_key
        self.stop_key = stop_key
        self.keyboard_listener = (
            keyboard_listener
            if keyboard_listener is not None
            else keyboard.Listener(on_press=self.on_press)  # type: ignore
        )
        self.keyboard_listener.start()
        self.is_paused = False

    def on_press(self, key):
        if key == self.pause_key:
            self.is_paused = not self.is_paused

        # if self.is_paused:
        #     return

        if key == self.stop_key:
            return False
    
    @property
    def is_running(self):
        return self.keyboard_listener.running

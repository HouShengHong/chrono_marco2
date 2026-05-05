from .eye import Eye
from .ear import Ear
from .hand import Hand
from chrono_marco2.keeper import CountdownTimer
from chrono_marco2.alert import AlertMonitor
from typing import Callable
import time
from chrono_marco2.my_telegram_bot import run_my_tg_bot
from chrono_marco2.common.alert import (
    red_alert_monitor,
    different_map_alert_monitor,
    lie_detector_alert_monitor,
)


class Player:
    def __init__(
        self,
        eye: Eye,
        ear: Ear | None = None,
        hand: Hand | None = None,
        keepers: list[CountdownTimer] | None = None,
        alert_monitors: list[AlertMonitor] | None = None,
    ):
        self.eye = eye
        self.ear = ear if ear is not None else Ear()
        self.hand = hand if hand is not None else Hand()
        self.keepers = keepers if keepers is not None else []
        self.alert_monitors = (
            alert_monitors
            if alert_monitors is not None
            else [
                red_alert_monitor(self.eye),
                different_map_alert_monitor(self.eye),
                lie_detector_alert_monitor(),
            ]
        )

    def run(self, how_to_play: Callable[[Player], None], pre_do_keepers: bool = False):
        self.eye.update_status()
        run_my_tg_bot()
        time.sleep(1)
        for alert_monitor in self.alert_monitors:
            alert_monitor.start()

        if pre_do_keepers is True:
            self.eye.update_status()
            if self.eye.status.current_is_same_map is True:
                for keeper in self.keepers:
                    keeper.do_on_finish()

        while self.ear.keyboard_listener.running:
            if self.ear.is_paused:
                self.hand.reset_holding_keys()
                for alert_monitor in self.alert_monitors:
                    alert_monitor.stop()
                print(f"Paused. Press {self.ear.pause_key} to resume.")
                time.sleep(1)
                continue

            # for alert_monitor in self.alert_monitors:
            #     if alert_monitor._thread is not None:
            #         if not alert_monitor._thread.is_alive():
            #             alert_monitor.start()

            self.eye.update_status()
            if self.eye.status.current_is_same_map:
                how_to_play(self)

            else:
                self.hand.reset_holding_keys()
                print(self.eye.status.current_same_map_score, "Different map detected!")
                time.sleep(1)

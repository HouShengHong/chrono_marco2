from chrono_marco2.alert import AlertMonitor
from chrono_marco2 import my_telegram_bot
from chrono_marco2.my_telegram_bot.my_tg_setting import MyTelegramSetting
from chrono_marco2.player.eye import Eye
from pathlib import Path
import pyautogui
import cv2
from datetime import datetime


def red_alert_monitor(eye: Eye) -> AlertMonitor:
    def check_red_alert(eye: Eye = eye) -> bool:
        if eye.status.current_red_point_position_in_mini_map:
            return True
        return False

    def on_red_alert():
        print("Red alert!")
        my_telegram_bot.notify_user_image_array_external_trigger(
            MyTelegramSetting.chat_id,
            f"Red alert! {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            eye.status.current_frame,
        )

    return AlertMonitor(
        check_red_alert, on_red_alert, check_args=(eye,), name="Red_Alert_Monitor"
    )


def different_map_alert_monitor(eye: Eye) -> AlertMonitor:
    def check_different_map_alert(eye: Eye = eye) -> bool:
        if eye.status.current_is_same_map is False:
            return True
        return False

    def on_different_map_alert():
        print("Different map alert!")
        my_telegram_bot.notify_user_image_array_external_trigger(
            MyTelegramSetting.chat_id,
            f"Different map alert! {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            eye.status.current_frame,
        )

    return AlertMonitor(
        check_different_map_alert,
        on_different_map_alert,
        check_args=(eye,),
        name="Different_Map_Alert_Monitor",
    )


def lie_detector_alert_monitor(
    path: Path = Path().cwd() / "data" / "lie_detector" / "0.png",
) -> AlertMonitor:
    img = cv2.imread(path)

    def lie_detector_alert() -> bool:
        pyautogui.useImageNotFoundException(False)
        location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
        if location is not None:
            return True
        return False

    def on_lie_detector_alert():
        print("Different map alert!")
        my_telegram_bot.notify_user_screenshot_external_trigger(
            MyTelegramSetting.chat_id,
            f"Lie Detector alert! {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        )

    return AlertMonitor(
        lie_detector_alert,
        on_lie_detector_alert,
        name="Lie_Detector_Alert_Monitor",
    )

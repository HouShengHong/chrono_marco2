from chrono_marco2.alert import AlertMonitor
from chrono_marco2 import my_telegram_bot
from chrono_marco2.my_telegram_bot.my_tg_setting import MyTelegramSetting
from chrono_marco2.player.eye import Eye


def red_alert_monitor(eye: Eye) -> AlertMonitor:
    def check_red_alert(eye: Eye = eye) -> bool:
        if eye.status.current_red_point_position_in_mini_map:
            return True
        return False

    def on_red_alert():
        print("Red alert!")
        my_telegram_bot.notify_user_screenshot_external_trigger(
            MyTelegramSetting.chat_id, "Red alert!"
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
        my_telegram_bot.notify_user_screenshot_external_trigger(
            MyTelegramSetting.chat_id, "Different map alert!"
        )

    return AlertMonitor(
        check_different_map_alert,
        on_different_map_alert,
        check_args=(eye,),
        name="Different_Map_Alert_Monitor",
    )


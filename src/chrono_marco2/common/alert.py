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


lie_detector_png_path: Path = Path().cwd() / "data" / "lie_detector" / "0.png"
lie_detector_img = cv2.imread(lie_detector_png_path)
if lie_detector_img is None:
    print("lie_detector_img is None")
else:
    print("lie_detector_img is exist")

# template_h, template_w = lie_detector_img.shape[:2]


def lie_detector_alert_monitor(
    eye: Eye,
) -> AlertMonitor:
    def lie_detector_alert(eye: Eye = eye) -> bool:
        frame = eye.status.current_frame
        if frame is None:
            return False
        if lie_detector_img is None:
            return False

        template_h, template_w = lie_detector_img.shape[:2]

        # dxcam 是 RGB，OpenCV 讀圖預設是 BGR，需統一格式
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # 3. 模板匹配
        # res 是一個矩陣，代表每個位置的匹配分數
        res = cv2.matchTemplate(frame_bgr, lie_detector_img, cv2.TM_CCOEFF_NORMED)

        # 4. 找出分數最高的位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # 如果最高分數大於門檻值 (例如 0.8)，視為找到
        if max_val >= 0.8:
            top_left = max_loc
            bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
            center = (top_left[0] + template_w // 2, top_left[1] + template_h // 2)

            print(f"找到目標！信心指數: {max_val:.2f}, 中心座標: {center}")
            return True
        else:
            print(f"未找到目標，最高信心指數僅: {max_val:.2f}")
            return False

    def on_lie_detector_alert():
        print("Lie Detector alert!")
        my_telegram_bot.notify_user_image_array_external_trigger(
            MyTelegramSetting.chat_id,
            f"Lie Detector alert! {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            eye.status.current_frame,
        )

    return AlertMonitor(
        lie_detector_alert,
        on_lie_detector_alert,
        check_args=(eye,),
        name="Lie_Detector_Alert_Monitor",
    )

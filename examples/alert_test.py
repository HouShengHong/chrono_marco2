# from chrono_marco2.alert import AlertMonitor
from chrono_marco2.my_telegram_bot import *
from chrono_marco2.my_telegram_bot.my_tg_setting import MyTelegramSetting
from chrono_marco2.player.eye import Eye
from pathlib import Path
from chrono_marco2.common.mini_map_data import MiniMapData
from chrono_marco2.common.alert import red_alert_monitor, different_map_alert_monitor
import time


# def simple_check():
#     return 1

# def on_alert():
#     print("Alert triggered!")

# if __name__ == "__main__":
#     simple_monitor = AlertMonitor(simple_check,on_alert)
#     simple_monitor.start()

#     while 1:
#         input("按 Enter 鍵退出...")
#         if simple_monitor._thread.is_alive():
#             simple_monitor.stop()
#         else:
#             simple_monitor.start()

if __name__ == "__main__":
    path = Path().cwd() / "data" / "mini_map_titles" / "leafre_the_burning_forest.png"
    eye: Eye = Eye(path,MiniMapData.leafre_the_burning_forest["title"],MiniMapData.leafre_the_burning_forest["region"])
    run_my_tg_bot()
    red_alert_monitor = red_alert_monitor(eye)
    different_map_alert_monitor = different_map_alert_monitor(eye)
    eye.update_status()
    red_alert_monitor.start()
    different_map_alert_monitor.start()


    time.sleep(1)
    t1 = time.time()
    if not red_alert_monitor._thread.is_alive():
        red_alert_monitor.start()
        print("Red alert monitor restarted.")
    if not different_map_alert_monitor._thread.is_alive():
        different_map_alert_monitor.start()
        print("Different map alert monitor restarted.")
    t2 = time.time()
    print(f"Alert monitors restarted in {t2-t1:.10f} seconds.")
    print()
    while 1:
        time.sleep(1)
        eye.update_status()


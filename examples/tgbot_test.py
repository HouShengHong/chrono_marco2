from chrono_marco2.my_telegram_bot import *
from chrono_marco2.my_telegram_bot.my_tg_setting import MyTelegramSetting

print("Async 機器人運行中...")
run_my_tg_bot()
print("...")


while 1:
    notify_user_screenshot_external_trigger(MyTelegramSetting.chat_id, "這是來自外部執行緒的訊息！")
    input("按 Enter 鍵退出...")
    


import asyncio
import time
from PIL import Image
import numpy as np
from telebot.async_telebot import AsyncTeleBot
from .my_tg_setting import MyTelegramSetting
import threading
import pyautogui
import io
from functools import wraps
from chrono_marco2.key_holder import KeyHolderWin


__all__ = [
    "run_my_tg_bot",
    "notify_user_external_trigger",
    "notify_user_screenshot_external_trigger",
]

API_TOKEN = MyTelegramSetting.token
CHAT_ID = MyTelegramSetting.chat_id
ADMIN_IDS = [
    int(MyTelegramSetting.chat_id),
]  # 也可以允許多個 ID

bot = AsyncTeleBot(API_TOKEN)
loop = asyncio.new_event_loop()
_running = False


async def _start_bot():
    print("Async Bot 執行緒啟動...")
    await bot.polling()


def _bot_worker():
    # loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(_start_bot())


def run_my_tg_bot():
    global _running
    if not _running:
        threading.Thread(target=_bot_worker, daemon=True).start()
        _running = True


def admin_only(func):
    @wraps(func)
    async def wrapped(message, *args, **kwargs):
        if message.from_user.id not in ADMIN_IDS:
            await bot.reply_to(message, "⚠️ 你沒有執行此指令的權限。")
            return
        return await func(message, *args, **kwargs)

    return wrapped


# 定義你的主動發送邏輯
async def notify_user(chat_id: int, msg_content: str):
    await bot.send_message(chat_id, f"【系統通知】: {msg_content}")


# 如果你在另一個執行緒，想主動發送：
def notify_user_external_trigger(chat_id: int, msg_content: str):
    asyncio.run_coroutine_threadsafe(notify_user(chat_id, msg_content), loop)


# 定義你的主動發送邏輯
async def notify_user_screenshot(chat_id: int, msg_content: str):
    screen = pyautogui.screenshot()

    # 3. 將圖片轉換為二進位流（BytesIO），不必存檔到硬碟
    buf = io.BytesIO()
    screen.save(buf, format="PNG")
    buf.seek(0)  # 將指針移回開頭，方便讀取

    # 4. 發送圖片
    # 注意：使用非同步版一定要 await
    await bot.send_photo(chat_id, buf, caption=f"【系統通知】: {msg_content}")


# 如果你在另一個執行緒，想主動發送：
def notify_user_screenshot_external_trigger(chat_id: int, msg_content: str):
    asyncio.run_coroutine_threadsafe(notify_user_screenshot(chat_id, msg_content), loop)


# 定義你的主動發送邏輯
async def notify_user_image_array(
    chat_id: int, msg_content: str, image_array: np.ndarray | None
):
    if image_array is None:
        await bot.send_message(chat_id, f"【系統通知】: {msg_content} (沒有圖片可顯示)")
    else:
        img = Image.fromarray(image_array.astype("uint8"))
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        # 4. 發送圖片
        # 注意：使用非同步版一定要 await
        await bot.send_photo(chat_id, buf, caption=f"【系統通知】: {msg_content}")


# 如果你在另一個執行緒，想主動發送：
def notify_user_image_array_external_trigger(
    chat_id: int, msg_content: str, image_array: np.ndarray | None
):
    asyncio.run_coroutine_threadsafe(
        notify_user_image_array(chat_id, msg_content, image_array), loop
    )


@bot.message_handler(commands=["help"])
@admin_only
async def help_info(message):
    await bot.reply_to(message, "help, set, send, action, lie, screenshot")


@bot.message_handler(commands=["screenshot"])
@admin_only
async def take_screenshot(message):
    try:
        # 1. 告知使用者正在處理（增加互動感）
        # await bot.send_chat_action(message.chat.id, "upload_photo")

        # 2. 執行截圖
        # screenshot() 會回傳一個 PIL Image 物件
        screen = pyautogui.screenshot()

        # 3. 將圖片轉換為二進位流（BytesIO），不必存檔到硬碟
        buf = io.BytesIO()
        screen.save(buf, format="PNG")
        buf.seek(0)  # 將指針移回開頭，方便讀取

        # 4. 發送圖片
        # 注意：使用非同步版一定要 await
        await bot.send_photo(message.chat.id, buf, caption="這是當下的電腦螢幕截圖！")

    except Exception as e:
        await bot.reply_to(message, f"截圖失敗：{str(e)}")


@bot.message_handler(commands=["set"])
@admin_only
async def handle_set(message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await bot.reply_to(message, "請提供參數")
    else:
        value = args[1]
        await bot.reply_to(message, f"你輸入的是: {value}, len: {len(value)}")


@bot.message_handler(commands=["send"])
@admin_only
async def send_message_in_game(message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await bot.reply_to(message, "請提供參數")
    else:
        value = args[1]
        KeyHolderWin(["f8"], (0.1, 0.1)).hold()
        time.sleep(3)
        KeyHolderWin(["enter"], (0.1, 0.1)).hold()
        pyautogui.write(value)
        time.sleep(1)
        KeyHolderWin(["enter"], (0.1, 0.1)).hold()
        KeyHolderWin(["f8"], (0.1, 0.1)).hold()

        await bot.reply_to(message, f"你輸入的是: {value}, len: {len(value)}")


@bot.message_handler(commands=["action"])
@admin_only
async def make_action(message):

    args = message.text.split()

    if len(args) < 3:
        await bot.reply_to(message, "請提供參數, 須要至少2個")
    else:
        try:
            hold_key = args[1:-1]
            hold_time = abs(float(args[-1]))
            hold_time = min(hold_time, 5)
            KeyHolderWin(hold_key, (hold_time, hold_time)).hold()

            await bot.reply_to(message, f"hold_key: {hold_key}, hold_time: {hold_time}")
        except:
            await bot.reply_to(message, "Something error, cannot key hold")


@bot.message_handler(commands=["lie"])
@admin_only
async def input_lie_detecter(message):
    """
    lie detecter soft keyboard
     --------------------------------------
    |      1     |      2     |      3     |
    | (897, 330) | (948, 330) | (999, 330) |
    |--------------------------------------|
    |      4     |      5     |      6     |
    | (897, 375) | (948, 375) | (999, 375) |
    |--------------------------------------|
    |      7     |      8     |      9     |
    | (897, 419) | (948, 419) | (999, 419) |
    |--------------------------------------|
    |     <-     |      0     |            |
    | (897, 464) | (948, 464) |            |
    |--------------------------------------|
    |       cancel      |        ok        |
    |     (910, 514)    |    (987, 514)    |
     --------------------------------------
    """
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await bot.reply_to(message, "請提供參數")
    else:
        value = args[1]
        if len(value) < 6:
            await bot.reply_to(message, "arg len should be 6")
        else:
            pyautogui.click(910, 514)
            time.sleep(1)
            for i in range(6):
                match value[i]:
                    case "1":
                        pyautogui.click(897, 330)
                        time.sleep(1)
                    case "2":
                        pyautogui.click(948, 330)
                        time.sleep(1)
                    case "3":
                        pyautogui.click(999, 330)
                        time.sleep(1)
                    case "4":
                        pyautogui.click(897, 375)
                        time.sleep(1)
                    case "5":
                        pyautogui.click(948, 375)
                        time.sleep(1)
                    case "6":
                        pyautogui.click(999, 375)
                        time.sleep(1)
                    case "7":
                        pyautogui.click(897, 419)
                        time.sleep(1)
                    case "8":
                        pyautogui.click(948, 419)
                        time.sleep(1)
                    case "9":
                        pyautogui.click(999, 419)
                        time.sleep(1)
                    case "0":
                        pyautogui.click(948, 464)
                        time.sleep(1)
                    case _:
                        pass
            pyautogui.click(987, 514)
            time.sleep(1)

            await bot.reply_to(message, f"你輸入的是: {value}, len: {len(value)}")


"""
# 使用 async def 定義處理器
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('點我測試非同步')
    markup.add(btn)
    
    # 必須使用 await
    await bot.reply_to(message, "這是非同步模式的機器人！", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '點我測試非同步')
async def handle_async_test(message):
    await bot.send_chat_action(message.chat.id, 'typing')
    # 模擬非同步耗時操作，這不會卡住其他使用者的請求
    await asyncio.sleep(2) 
    await bot.send_message(message.chat.id, "這是在不阻塞的情況下完成的回覆！")

# 處理所有其他文字
@bot.message_handler(func=lambda message: True)
async def echo_all(message):
    await bot.reply_to(message, f"Async 回覆：{message.chat.id} - {message.text}")
"""

# 啟動非同步循環
if __name__ == "__main__":
    pass

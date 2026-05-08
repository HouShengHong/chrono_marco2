import asyncio
from PIL import Image
import numpy as np
from telebot.async_telebot import AsyncTeleBot
from .my_tg_setting import MyTelegramSetting
import threading
import pyautogui
import io
from functools import wraps


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


@bot.message_handler(commands=["screenshot"])
@admin_only
async def take_screenshot(message):
    try:
        # 1. 告知使用者正在處理（增加互動感）
        await bot.send_chat_action(message.chat.id, "upload_photo")

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

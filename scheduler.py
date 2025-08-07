from telegram import Bot
from apscheduler.schedulers.background import BackgroundScheduler
from config import BOT_TOKEN
import os

def start_scheduler():
    if not BOT_TOKEN or not BOT_TOKEN.startswith(""):
        print("❌ BOT_TOKEN не найден или некорректен. Получи токен от https://t.me/BotFather.")
        return

    bot = Bot(token=BOT_TOKEN)
    scheduler = BackgroundScheduler()

    def send_reminder():
        # Замените chat_id на ID пользователя или группы
        chat_id = os.getenv("CHAT_ID")
        if chat_id:
            bot.send_message(chat_id=chat_id, text="⏰ Напоминание!")
        else:
            print("⚠️ CHAT_ID не указан. Напоминание не отправлено.")

    # Пример: отправлять напоминание каждый час
    scheduler.add_job(send_reminder, 'interval', hours=1)
    scheduler.start()
    print("📅 Планировщик запущен.")

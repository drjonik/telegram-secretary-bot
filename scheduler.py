from apscheduler.schedulers.background import BackgroundScheduler
from database import get_reminders
from datetime import datetime
from telegram import Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
scheduler = BackgroundScheduler()

def send_reminder(chat_id, text):
    bot.send_message(chat_id=chat_id, text=f"🔔 Напоминание: {text}")

def schedule_reminders():
    reminders = get_reminders()
    for r in reminders:
        chat_id, text, time_str, interval = r[1], r[2], r[3], r[4]
        time = datetime.fromisoformat(time_str)
        if interval:
            scheduler.add_job(send_reminder, 'interval', days=int(interval), args=[chat_id, text], next_run_time=time)
        else:
            scheduler.add_job(send_reminder, 'date', run_date=time, args=[chat_id, text])

def start_scheduler():
    schedule_reminders()
    scheduler.start()

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from dateparser import parse
from database import add_reminder, delete_reminder_by_text, get_reminders

menu_keyboard = ReplyKeyboardMarkup(
    [["Добавить напоминание", "Список задач"],
     ["Удалить напоминание", "Настройки"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я ваш секретарь 🤖", reply_markup=menu_keyboard)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    chat_id = update.message.chat_id

    if "напомни" in text:
        time = parse(text, languages=['ru'])
        if time:
            add_reminder(chat_id, text, time.isoformat())
            await update.message.reply_text(f"✅ Напоминание добавлено на {time.strftime('%d.%m.%Y %H:%M')}")
        else:
            await update.message.reply_text("❌ Не удалось распознать время.")
    elif "удалить" in text:
        delete_reminder_by_text(chat_id, text)
        await update.message.reply_text("🗑 Напоминание удалено.")
    elif "список" in text:
        reminders = get_reminders()
        user_reminders = [r for r in reminders if r[1] == chat_id]
        if user_reminders:
            msg = "\n".join([f"• {r[2]} — {r[3]}" for r in user_reminders])
            await update.message.reply_text(f"📋 Ваши задачи:\n{msg}")
        else:
            await update.message.reply_text("📭 У вас нет задач.")
    else:
        await update.message.reply_text("🤔 Не понял команду. Попробуйте ещё раз.")

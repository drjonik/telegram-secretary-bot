from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from config import BOT_TOKEN
from handlers import start, handle_message
from scheduler import start_scheduler
from database import init_db

def main():
    init_db()
    start_scheduler()

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

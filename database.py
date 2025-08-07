import sqlite3

def init_db():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER,
            text TEXT,
            time TEXT,
            repeat_interval TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_reminder(chat_id, text, time, repeat_interval=None):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (chat_id, text, time, repeat_interval) VALUES (?, ?, ?, ?)",
                   (chat_id, text, time, repeat_interval))
    conn.commit()
    conn.close()

def get_reminders():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reminders")
    reminders = cursor.fetchall()
    conn.close()
    return reminders

def delete_reminder_by_text(chat_id, text):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reminders WHERE chat_id = ? AND text LIKE ?", (chat_id, f"%{text}%"))
    conn.commit()
    conn.close()

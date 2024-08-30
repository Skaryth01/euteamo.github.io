import sqlite3

def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_message(message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (content) VALUES (?)', (message,))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT content FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return [msg[0] for msg in messages]

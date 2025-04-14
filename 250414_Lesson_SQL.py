import sqlite3 as sq

with sq.connect('250414_prodile.db') as con:
    cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
summa REAL,
data TEXT
)
'''

)
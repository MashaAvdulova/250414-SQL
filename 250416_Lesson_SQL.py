import sqlite3 as sq

with sq.connect('250416_users.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone BLOB NOT NULL DEFAULT '+79001234567',
    age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    email TEXT UNIQUE
    )
    '''
    )
# Переименовать таблицу
    # cur.execute('''
    # ALTER TABLE person
    # RENAME TO person_table;
    # '''
    # )

# Добавить столбец
    # cur.execute('''
    # ALTER TABLE person_table
    # ADD COLUMN adress TEXT NOT NULL''')

# Переименовать столбец
    # cur.execute('''
    # ALTER TABLE person_table
    # RENAME COLUMN adress TO home_adress''')

# # Удалить таблицу
#     cur.execute('''
#     DROP TABLE person_table
#     ''')

#  Добавление информации в базу данных
#     cur.execute('''
#             INSERT INTO person
#             VALUES (1, 'Антон', '+79001234567', 22, 'anton@gmail.com')
#     ''')
#
#     cur.execute('''
#             INSERT INTO person(name, age, email)
#             VALUES ('Яна', 33, 'yyn@gmail.com')
#     ''')


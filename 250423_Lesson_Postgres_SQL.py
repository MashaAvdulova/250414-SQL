import psycopg2
from psycopg2 import Error

# Создаем объект подключения к базе данных
def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname='Airport',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
        print('Соединение с БД установлено')
        return conn
    except Exception as err:
        print(f'Ошибка при подключении в БД\n {err}')
        return conn

def close_connection():
    if conn:
        conn.close()
        print('Соединение с БД закрыто')

def create_tables(conn):
    table_1 = '''CREATE TABLE IF NOT EXISTS Airports(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL)
    '''
    try:
        cur = conn.cursor()
        cur.execute(table_1)
        conn.commit()
        cur.close()
        print(f'Таблица успешно создана')
    except Error as err:
        print(f'Ошибка при создании таблицы \n{err}')


conn = create_connection()
create_tables(conn)


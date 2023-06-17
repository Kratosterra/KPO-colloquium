import logging
import sqlite3


def create_database() -> None:
    """
    Функция создания базы данных. Создаёт таблицы, если их нет.
    :return:
    """
    # Создание подключения к базе данных
    logging.debug("Создание базы данных.")
    conn = sqlite3.connect(r'database/database.db')
    try:
        cursor = conn.cursor()
        # Создание таблицы "project/workouts"
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS project (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    description TEXT UNIQUE NOT NULL,
                    duration TEXT NOT NULL,
                    coach TEXT NOT NULL
                )
            ''')
        # Сохранение изменений и закрытие соединения
        conn.commit()
    except Exception as error:
        logging.debug(f"Создание базы данных произошло с ошибкой: {error}.")
    finally:
        conn.close()


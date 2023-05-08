import sqlite3

"""Создание базы данных"""

db = sqlite3.connect("TestDB.db")
print("Подключильсь к базе данных")
cur = db.cursor()

"""Создание таблицы"""
cur.execute("""CREATE TABLE IF NOT EXISTS Students(
    StudentID INTEGER PRIMARY KEY,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);
""")
db.commit()

"""Заполнение таблицы"""
for i in range(100):
    cur.execute("""INSERT INTO Students( First_name, Last_name)
        VALUES('IVAN', 'IVANOV');
    """)
    db.commit()

cur.execute("""SELECT * FROM Students""")
a = cur.fetchall()
print(a)

db.close()
print("Закрыли подключение")
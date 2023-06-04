import sqlite3

"""Создание базы данных"""

db = sqlite3.connect("TestDB.db")
print("Подключильсь к базе данных")
cur = db.cursor()

# """Создание таблицы"""
# cur.execute("""CREATE TABLE IF NOT EXISTS Students(
#     StudentID INTEGER PRIMARY KEY,
#     First_name TEXT NOT NULL,
#     Last_name TEXT NOT NULL);
# """)
# db.commit()

"""Заполнение таблицы"""

# data = [('alex', 'aleksandrov'), ('olga', 'olgova')]
#
# cur.executemany("""INSERT INTO Students( First_name, Last_name)
#     VALUES(?, ?);""", data)
# db.commit()

data_update=('1111', 4)

cur.execute("""UPDATE Students SET Last_name = ? WHERE StudentID = ?""", data_update)
db.commit()

cur.execute("""SELECT * FROM Students""")
a = cur.fetchone()
print(a[1])

db.close()
print("Закрыли подключение")






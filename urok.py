import sqlite3

"""Подключение к базе данных"""

db = sqlite3.connect(r"/Users/aleksandr.gorelov/Documents/QATesting.db")
print("Подключильсь к базе данных")
cur = db.cursor()

cur.execute("""SELECT * FROM Student;""")
print("Выполнили запрос")

result = cur.fetchall()
print(result)

db.close()
print("Закрыли подключение")
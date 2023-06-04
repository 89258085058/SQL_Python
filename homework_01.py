import sqlite3

# 1. Создать базу данных registration.db
db = sqlite3.connect("registration.db")
cur = db.cursor()
print("Создали и подключильсь к базе данных")


# 2. Создать таблицу users_data
cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
    UserID INTEGER PRIMARY KEY,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Code INTEGER
    );
""")
db.commit()
print("Таблица создана")



# 3. Добавить пользователя с данными
data_user = ('Ivan', 'qwer1234', 1234)
cur.execute("""INSERT INTO users_data( Login, Password, Code)
    VALUES(?, ?, ?);""", data_user)
db.commit()
print("Данные добавлены")


cur.execute("""SELECT * FROM users_data""")
a = cur.fetchall()
print(a)
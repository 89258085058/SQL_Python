import sqlite3

#
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


# Функция добавления пользователя
def add_user(login, Password, Code):
    data = login, Password, Code
    cur.execute("""INSERT INTO users_data(Login, Password, Code)
             VALUES(?, ?, ?);""", data)
    db.commit()
    print("Вы зарегистрированны")


# Функция получения пользователя по логину
def get_user_login(login):
    cur.execute(f"""SELECT * FROM users_data WHERE Login= {"'" + login + "'"}""")
    return cur.fetchall()


# Функция добавления авторизованного пользователя
def get_auth_user(login, Password):
    cur.execute(f"""SELECT * FROM users_data WHERE Login= {"'" + login + "'"} AND Password= {"'" + Password + "'"}""")
    return cur.fetchall()


# Функция получения пользователя с кодом доступа
def password_recovery(login, code):
    cur.execute(f"""SELECT * FROM users_data WHERE Login= {"'" + login + "'"} AND Code= {"'" + code + "'"}""")
    return cur.fetchall()


# Функция изменения пароля
def new_password(new_pass, login):
    cur.execute(f"""UPDATE users_data SET Password = {"'" + new_pass + "'"} WHERE Login = {"'" + login + "'"}""")
    db.commit()
    print('Пароль успешно обновлен')


# 4. Основной функционал
var = str(input(
    'Выберете один из 3х пунктов: \n- 1.Регистрация нового пользователя\n- 2.Авторизация в системе\n- 3.Восстановление пароля по кодовому слову\n\n'))
if var == '1':
    login = input('Введите логин: ')
    all_login = get_user_login(login)
    if len(all_login) > 0:
        login = input('Логин уже существует Введите новый логин: ')
        Password = input('Введите Пароль: ')
        Code = input('Введите Код доступа: ')
        add_user(login, Password, Code)
    else:
        Password = input('Введите Пароль: ')
        Code = input('Введите Код доступа: ')
        add_user(login, Password, Code)

elif var == '2':
    login = input('Введите логин: ')
    Password = input('Введите Пароль: ')
    auth_user = get_auth_user(login, Password)
    if len(auth_user) > 0:
        print("Вы авторизованы")
    else:
        print('Пользователя с указанными данными не существует')

elif var == '3':
    login = input('Введите логин: ')
    code = input('Введите скретный код: ')
    recovery = password_recovery(login, code)
    if len(recovery) > 0:
        password = input('Введите новый пароль: ')
        new_password(password, login)
    else:
        print('Пользователя с указанными данными не существует')

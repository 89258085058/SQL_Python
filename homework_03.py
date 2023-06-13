import sqlite3

# 1. Создать базу данных exchanger.db
db = sqlite3.connect("exchanger.db")
cur = db.cursor()
print("Создали и подключильсь к базе данных")

# 2. Создать таблицу users_balance
cur.execute("""CREATE TABLE IF NOT EXISTS users_balance(
    UserID INTEGER PRIMARY KEY,
    Balance_RUB INTEGER,
    Balance_USD INTEGER,
    Balance_EUR INTEGER
    );
""")
db.commit()
print("Таблица создана")

# 3. Добавить пользователя с данными
data_user = ('100000', '1000', 1000)
cur.execute("""INSERT INTO users_balance(Balance_RUB, Balance_USD, Balance_EUR)
    VALUES(?, ?, ?);""", data_user)
db.commit()
print("Данные добавлены")


# получение рублей
def get_rubels():
    cur.execute(f"""SELECT Balance_RUB FROM users_balance""")
    return cur.fetchone()[0]


# получение долларов
def get_usd():
    cur.execute(f"""SELECT Balance_USD FROM users_balance""")
    return cur.fetchone()[0]


# получение евро
def get_eur():
    cur.execute(f"""SELECT Balance_EUR FROM users_balance""")
    return cur.fetchone()[0]


# основной расет
def account_verification(result, currency, val, sum, val2):
    if result <= currency:
        input(f"Вам понадобится: {result} {val} На счету достаточно средств!"
              f"\nНажмите Enter для подтверждения операции")
        set_new_sum_plus(sum, val2)
        set_new_sum_minus(result)
        new_sum()
    else:
        print("У вас недостаточно средств")


# Прибавление суммы
def set_new_sum_plus(sum, val):
    if val == 'rub':
        cur.execute(f"""SELECT * FROM users_balance""")
        many = cur.fetchone()[1]
        cur.execute(f"""UPDATE users_balance SET Balance_RUB = {int(sum + many)} WHERE UserID = 1""")
        db.commit()
    elif val == 'usd':
        cur.execute(f"""SELECT * FROM users_balance""")
        many = cur.fetchone()[2]
        cur.execute(f"""UPDATE users_balance SET Balance_USD = {int(sum + many)} WHERE UserID = 1""")
        db.commit()
    elif val == 'eur':
        cur.execute(f"""SELECT * FROM users_balance""")
        many = cur.fetchone()[3]
        cur.execute(f"""UPDATE users_balance SET Balance_EUR = {int(sum + many)} WHERE UserID = 1""")
        db.commit()


# Вычитание суммы
def set_new_sum_minus(results):
    if val == 'rub':
        cur.execute(f"""SELECT * FROM users_balance""")
        many = cur.fetchone()[1]
        cur.execute(f"""UPDATE users_balance SET Balance_RUB = {float(many - results)} WHERE UserID = 1""")
        db.commit()
    elif val == 'usd':
        cur.execute(f"""SELECT * FROM users_balance""")
        many = cur.fetchone()[2]
        cur.execute(f"""UPDATE users_balance SET Balance_USD = {float(many - results)} WHERE UserID = 1""")
        db.commit()
    elif val == 'eur':
        cur.execute(f"""SELECT * FROM users_balance""")
        many = cur.fetchone()[3]
        cur.execute(f"""UPDATE users_balance SET Balance_EUR = {float(many - results)} WHERE UserID = 1""")
        db.commit()


# Информация для пользователя
def new_sum():
    cur.execute(f"""SELECT * FROM users_balance""")
    rub = cur.fetchone()
    print("\nВаш текущий баланс"
          f"\nRUB:{rub[1]}"
          f"\nUSD:{rub[2]}"
          f"\nEUR:{rub[3]}"
          )


# Основной функционал
var = int(input("Добро пожаловать в наш обменный пункт, курс валют следующий:"
                "\n1 USD = 70 RUB"
                "\n1 EUR = 80 RUB"
                "\n1 USD = 0,87 EUR"
                "\n1 EUR = 1,15 USD"
                "\n"
                "\nВведите какую валюты желаете получить:"
                "\n1. RUB"
                "\n2. USD"
                "\n3. EUR"
                "\n"
                ))

if var == 1:
    rubels = get_rubels()
    try:
        sum = int(input("Какая сумма Вас интересует?"))
    except:
        sum = int(input("Вы ввели неверное значение попоробуйте еще раз\nКакая сумма Вас интересует?"))

    val = int(input("Какую валюту готовы предложить взамен?"
                    "\n1. USD"
                    "\n2. EUR"
                    "\n"
                    ))
    if val == 1:
        val = 'usd'
        res = sum / 70
        account_verification(round(res, 2), get_usd(), val, sum, 'rub')
    if val == 2:
        val = 'eur'
        res = sum / 80
        account_verification(round(res, 2), get_eur(), val, sum, 'rub')

if var == 2:
    rubels = get_rubels()
    try:
        sum = int(input("Какая сумма Вас интересует?"))
    except:
        sum = int(input("Вы ввели неверное значение попоробуйте еще раз\nКакая сумма Вас интересует?"))

    val = int(input("Какую валюту готовы предложить взамен?"
                    "\n1. RUB"
                    "\n2. EUR"
                    "\n"
                    ))
    if val == 1:
        val = 'rub'
        res = sum * 70
        account_verification(round(res, 2), get_rubels(), val, sum, 'usd')
    if val == 2:
        val = 'eur'
        res = sum * 0.87
        account_verification(round(res, 2), get_eur(), val, sum, 'usd')

if var == 3:
    rubels = get_rubels()
    try:
        sum = int(input("Какая сумма Вас интересует?"))
    except:
        sum = int(input("Вы ввели неверное значение попоробуйте еще раз\nКакая сумма Вас интересует?"))

    val = int(input("Какую валюту готовы предложить взамен?"
                    "\n1. RUB"
                    "\n2. USD"
                    "\n"
                    ))
    if val == 1:
        val = 'rub'
        res = sum * 80
        account_verification(round(res, 2), get_rubels(), val, sum, 'eur')
    if val == 2:
        val = 'usd'
        res = sum * 1.15
        account_verification(round(res, 2), get_usd(), val, sum, 'eur')

import pymysql

pymysql.install_as_MySQLdb()
# import database_conn as dbc                                                #uncomment for debug
import configparser
from datetime import datetime, timedelta, timezone

# stream_id = 163
start_time = datetime.now()
end_time = '2018-08-08'
st_time = str(start_time.strftime("%Y%m%d%H%M%S"))
# print(st_time)
tarif = 4.96


def read(name):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    # # исполняем SQL-запрос
    # sql="""SELECT building_number FROM clients;"""
    sqlr = f"""SELECT * FROM {name};"""
    # sqlw = f"""INSERT test (id, firstname, lastname, building_number, address, phone ) VALUES (1, "NULL", "NULL", 99, "NULL", "NULL");"""

    cursor.execute(sqlr)
    DATA = cursor.fetchall()
    print(DATA)
    # применяем изменения к базе данных
    db.commit()
    db.close()


def create_user_table(name="clients"):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    sql = f"""create TABLE {name} (id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATE,counter_end_val INT UNSIGNED, PRIMARY KEY (id));"""
    # sql1 = """create TABLE clients (user_id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATE,counter_end_val INT UNSIGNED, contact_id INT UNSIGNED NOT NULL, PRIMARY KEY (entry_id, contact_id));"""
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        print(f"таблица {name} создана успешно")
    except:
        print("что то пошло не так...")
        db.close()


def write_clients():
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    # # исполняем SQL-запрос
    # sql="""SELECT building_number FROM clients;"""
    # sqlr =  """SELECT * FROM clients;"""
    sqlw = f"""INSERT clients (id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATE,counter_end_val INT UNSIGNED, PRIMARY KEY (id));"""

    cursor.execute(sqlw)
    # DATA = cursor.fetchall()
    # print(DATA)
    # применяем изменения к базе данных
    db.commit()
    db.close()


def create_table_test(name):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    sql = f"""create TABLE {name} (id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATETIME,counter_end_val INT UNSIGNED, PRIMARY KEY (id));"""
    # sql1 = """create TABLE clients (user_id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATE,counter_end_val INT UNSIGNED, contact_id INT UNSIGNED NOT NULL, PRIMARY KEY (entry_id, contact_id));"""

    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        print(f"таблица {name} создана успешно")
    except:
        print("что то пошло не так...")
        db.close()


def create_payment_table(name="payments"):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    sql = f"""create TABLE {name} (id INT UNSIGNED AUTO_INCREMENT NOT NULL, building_number INT UNSIGNED, old_data INT UNSIGNED, current_data INT UNSIGNED, tarif FLOAT, rashod_za_period INT UNSIGNED, money_for_pay FLOAT, date DATETIME, PRIMARY KEY (id));"""

    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        print(f"таблица {name} создана успешно")
    except:
        print("что то пошло не так...")
        db.close()


def write_payments(build_number, old_data, current_data, tarif, rashod_za_period, money_for_pay, datap):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    # # исполняем SQL-запрос
    # sql="""SELECT building_number FROM clients;"""
    # sqlr =  """SELECT * FROM clients;"""
    sqlw = f"""INSERT payments (building_number, old_data, current_data, tarif, rashod_za_period, money_for_pay, date) VALUES ({build_number}, {old_data}, {current_data}, {tarif}, {rashod_za_period}, {money_for_pay}, {datap});"""

    cursor.execute(sqlw)
    # DATA = cursor.fetchall()
    # print(DATA)
    # применяем изменения к базе данных
    db.commit()
    db.close()


# read(clients)
# write()
# create_table_test("dick")
# create_payment_table()
# create_user_table()
# read("clients")
# read("payments")
# write_clients()
# write_payments(99, 0, 100, tarif, 100, 498, st_time)

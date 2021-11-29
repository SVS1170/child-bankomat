import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("config.ini")  # читаем конфиг
con = psycopg2.connect(
    database=config["database"]["db"],
    user=config["database"]["user"],
    password=config["database"]["passwd"],
    host=config["database"]["host"],
    port=int(config["database"]["port"])


def create_table(name):
  cur = con.cursor()
  cur.execute(f'''CREATE TABLE {name}  
       (ADMISSION INT PRIMARY KEY NOT NULL,
       NAME TEXT NOT NULL,
       AGE INT NOT NULL,
       COURSE CHAR(50),
       DEPARTMENT CHAR(50));''')
  commit()


def insert_data(name):
  cur = con.cursor()
  cur.execute(
    f"INSERT INTO {name} (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"
  )
  commit()


def read_data(name):
  cur = con.cursor()
  cur.execute(f"SELECT admission, name, age, course, department from {name}")
  rows = cur.fetchall()
  for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")
  close()


def update_data(name):
  cur = con.cursor()
  cur.execute(f"UPDATE {name} set AGE = 20 where ADMISSION = 3420")
  commit()


def close():
  con.close()


def commit():
  con.commit()
  con.close()
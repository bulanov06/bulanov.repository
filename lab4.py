import requests
from requests.structures import CaseInsensitiveDict
import sqlite3
url_post = "https://ptsv2.com/t/lab4/post"
headers_post = {'content-type' : 'application/json'}
data_post = '{"title": "apple", "color": "red", "count": 23}'
response_post = requests.request("POST", url_post, params=data_post, headers=headers_post)
try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite\n")

    cursor.execute("""DROP TABLE requests""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS requests(
        response TEXT);
        """)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""

    data_tuple = (url_post.text,)
    cursor.execute(sqlite_insert_with_param, data_tuple)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""




    cursor.execute(sqlite_insert_with_param, data_tuple)

    cursor.execute("SELECT * FROM requests;")
    result = cursor.fetchmany(999)
    print(result)

    sqlite_connection.commit()
    print("\nЗапись успешно вставлена в таблицу requests ")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
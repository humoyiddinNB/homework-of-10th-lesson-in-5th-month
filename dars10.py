import psycopg2
from prettytable import PrettyTable
import json

my_db_info = {
    'dbname' : "cars_db",
    "password" : "571632571632",
    "user" : "defendereviver71",
    "host" : "localhost",
    "port" : "5432"
}





##### 1-topshiriq
class MyContexM:
    def __init__(self, db_info):
        self.db_info = db_info

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_info)
        self.conn.autocommit = True
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        if exc_type:
            print(exc_val)


# with MyContexM(my_db_info) as conn:
#     with conn.cursor() as cur:
#         table = input("table name: ")
#         column = input("yangi qiymatni kiriting\n")
#         value = input(f"{column} = ")
#         column1  = input("qaysi columni ozgartirmoqchisiz?\n")
#         value1 = input(f"{column1} = ")
#         a = f"update {table} set {column} = %s where {column1} = %s"
#         cur.execute(a, (value, value1))
#         print("qiymat ozgartirildi!")









##### 2- topshiriq
# my_table = PrettyTable()
# my_table.field_names = ["id", "Name", "age", "date_of_birth", "gender"]
# my_table.add_rows([
#     [1, "Ali", 25, "05/12/2000", "Male"],
#     [2, "Vali", 30, "08/23/1995", "Male"],
#     [3, "Hasan", 22, "11/03/2003", "Male"],
#     [4, "Husan", 28, "07/14/1997", "Male"],
#     [5, "Sardor", 35, "02/27/1990", "Male"],
#     [6, "Bekzod", 29, "09/11/1994", "Male"],
#     [7, "Javohir", 26, "04/05/1999", "Male"],
#     [8, "Diyor", 24, "06/30/2001", "Male"],
#     [9, "Ulug'bek", 27, "01/15/1998", "Male"],
#     [10, "Shahzod", 32, "03/21/1993", "Male"],
#     [11, "Madina", 23, "07/18/2002", "Female"],
#     [12, "Zarina", 31, "09/09/1994", "Female"],
#     [13, "Laylo", 29, "10/25/1996", "Female"],
#     [14, "Malika", 26, "02/14/1999", "Female"],
#     [15, "Sabina", 24, "12/05/2000", "Female"],
#     [16, "Gulnoza", 28, "11/11/1997", "Female"],
#     [17, "Dildora", 30, "08/08/1995", "Female"],
#     [18, "Aziza", 25, "04/07/2000", "Female"],
#     [19, "Shoxrux", 27, "05/20/1998", "Male"],
#     [20, "Miron", 22, "06/15/2003", "Male"]
# ])

# print(my_table.get_string())
# print(my_table.get_html_string())








#### 3-topshiriq
# with psycopg2.connect(**my_db_info) as conn:
#     with conn.cursor() as cur:
        # cur.execute("""CREATE TABLE products (
        #     id SERIAL PRIMARY KEY,
        #     name TEXT NOT NULL,
        #     details JSONB );
        # """)
        # cur.execute("""
        # insert into products (name, details) values
        #     ('Smartphone', '{"brand": "Apple", "model": "iPhone 14", "price": 1200}'),
        #     ('Laptop', '{"brand": "Dell", "model": "XPS 15", "price": 1800}'),
        #     ('Tablet', '{"brand": "Samsung", "model": "Galaxy Tab S8", "price": 900}'),
        #     ('Smartwatch', '{"brand": "Apple", "model": "Watch Series 8", "price": 500}'),
        #     ('Headphones', '{"brand": "Sony", "model": "WH-1000XM5", "price": 400}'),
        #     ('Gaming Console', '{"brand": "Sony", "model": "PlayStation 5", "price": 500}'),
        #     ('Smartphone', '{"brand": "Samsung", "model": "Galaxy S23", "price": 1100}'),
        #     ('Laptop', '{"brand": "Apple", "model": "MacBook Pro 16", "price": 2500}'),
        #     ('Tablet', '{"brand": "Apple", "model": "iPad Pro", "price": 1200}'),
        #     ('Camera', '{"brand": "Canon", "model": "EOS R5", "price": 3500}');
        # """)

        # cur.execute("""
        # --select details->'brand' from products
        # --select details ->> 'brand', details ->> 'model' from products
        # select name, details ->> 'brand', details ->> 'model' from products where (details ->> 'price')::int > 900
        # """)
        # for i in cur.fetchall():
        #     print(i)







######## 4-topshiriq
with psycopg2.connect(**my_db_info) as conn:
    with conn.cursor() as cur:
        cur.execute("select * from cars_info where model !~*'[aeiouy]$' ;")

        columns = [i[0] for i in cur.description]

        result = [dict(zip(columns, row)) for row in cur.fetchall()]


        if result:
            with open("undosh.json", "w") as file:
                json.dump(result, file, indent=4, default=str)

            print("Barcha ma'lumotlar fayliga yozildi.")
        else:
            print("Hech qanday malumot topilmadi.")
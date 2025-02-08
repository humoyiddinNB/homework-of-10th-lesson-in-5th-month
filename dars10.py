import psycopg2

db_info = {
    "dbname" : "cars_db",
    "user" : "defendereviver71",
    "password" : "571632571632",
    "host" : "localhost",
    "port" : "5432"
}


class ContexManagerDB:
    def __init__(self, db_infos):
        self.db_infos  = db_infos

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_infos)
        self.conn.autocommit = True
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        if exc_type:
            print(exc_val)
        if exc_tb:
            print("Xatolik manzili: ", exc_tb)




with ContexManagerDB(db_info) as conn:
    with conn.cursor() as cur:
        cur.execute("select * from cars_info")
        for i in cur.fetchall():
            print(i)
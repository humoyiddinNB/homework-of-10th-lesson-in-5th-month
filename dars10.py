import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname =  dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.conn = psycopg2.connect(dbname = self.dbname, user = self.user, password = self.password,
                                    host = self.host, port = self.port)

        self.cur = self.conn.cursor()

    def get_data(self, table):
        self.cur.execute(f"select *from {table}")
        for i in self.cur.fetchall():
            print(i)
        self.conn.close()

my_db = DBManager("cars_db", "defendereviver71", "571632571632", "localhost", "5432")
my_db.get_data('cars_info')


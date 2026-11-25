import psycopg2


class ConnectDB:
    def __init__(self):
        self.con = psycopg2.connect(
            database="airline",
            user="postgres",
            password="Mmd22901mmd",
            host="localhost",
            port="5432"
        )
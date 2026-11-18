import psycopg2


def connect_db():
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Mmd22901mmd",
        host="localhost",
        port="5432"
    )

    return connection
from connect_db import ConnectDB
import psycopg2
import bcrypt


class User(ConnectDB):

    def register(self, first_name, last_name, username, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        query = """
            INSERT INTO users (first_name, last_name, username, password)
            VALUES (%s, %s, %s, %s)
        """
        try:
            with self.con.cursor() as cursor:
                cursor.execute(query, (first_name, last_name, username, hashed_password))
            self.con.commit()
        except psycopg2.errors:
            return "Registration failed"


    def login(self, username, password):
        query = """
            SELECT * FROM users
            WHERE username = %s
        """
        with self.con.cursor() as cursor:
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            
        if user and bcrypt.checkpw(password.encode(), user[4].encode()):
            return user
        return None

from database import connect_db

connection = connect_db()
print("Database connected successfully!")
connection.close()
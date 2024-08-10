import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="8624",
        database="ehs"
    )
    return connection

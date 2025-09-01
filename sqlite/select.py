import sqlite3
from sqlite.configuracao import DB_FILE, TABLE_NAME

def open_connection():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    return cursor, connection

def close_connection(cursor, connection):
    cursor.close()
    connection.close()

def lista_select():
    cursor, connection = open_connection()
    cursor.execute(f"select * from {TABLE_NAME}")
    list_all = cursor.fetchall()

    if list_all:
        return list_all
    close_connection(cursor, connection)

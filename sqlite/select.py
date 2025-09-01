import sqlite3
from configuracao import DB_FILE, TABLE_NAME


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

    # buscar ID's
    # for _list in list_all:
    #     print(_list[0])
    # print(list_all[0])
    # print(list_all[1])
    # print(list_all[2])

    if list_all:
        return list_all
    close_connection(cursor, connection)


def lista_select_vazia():
    lista_vazia = lista_select()
    return len(lista_vazia) == 0


# lista_select()

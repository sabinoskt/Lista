import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "veiculos"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL - INSERT SELECT UPDATE DELETE
# CRUD - Create Read Update Delete


# CUIDADO: fazendo delete sem where
# cursor.execute(
#     f"DELETE FROM {TABLE_NAME}"
# )


# DELETE mais cuidadoso
# cursor.execute(
#     f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")

# connection.commit()
#
# cursor.close()
# connection.close()


if __name__ == "__main__":
    pass
    # cursor.execute(
    #     f"DELETE FROM {TABLE_NAME} "
    #     "WHERE id = '2'"
    # )
    #
    # connection.commit()

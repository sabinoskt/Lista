from configuracao import cursor, connection, TABLE_NAME


# CRIA TABELA

cursor.execute(
    f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Modelo TEXT,
            Cor TEXT,
            Ano TEXT
        )
    """
)

connection.commit()
cursor.close()



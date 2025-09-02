from sqlite.configuracao import cursor, connection, TABLE_NAME

# CRIA TABELA
cursor.execute(
    f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Modelo VARCHAR(50),
            Cor VARCHAR(50),
            Ano INTEGER
        )
    """
)

connection.commit()
cursor.close()

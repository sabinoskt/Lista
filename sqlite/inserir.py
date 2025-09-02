from sqlite.configuracao import TABLE_NAME, cursor, connection


# Registrar valores nas colunas da tabela
# CUIDADE: sql injection


# cursor.execute(f"select * from {TABLE_NAME}")
# colunhas = cursor.description


insert1 = (
    f"""
    INSERT INTO {TABLE_NAME} (Modelo, Cor, Ano)
    VALUES (?, ?, ?)
    """
)

def inserir(modelo, cor, ano):
    cursor.execute(insert1, [modelo, cor, ano])
    connection.commit()

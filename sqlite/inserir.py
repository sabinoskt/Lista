from sqlite.configuracao import TABLE_NAME, cursor, connection


# Registrar valores nas colunas da tabela
# CUIDADE: sql injection

insert1 = (
    f"""
    INSERT INTO {TABLE_NAME} (Modelo, Cor, Ano) 
    VALUES (?, ?, ?)
    """
)

def inserir(modelo, cor, ano):
    dados = list(zip(modelo, cor, ano))
    # cursor.execute(insert1, (modelo, cor, ano))
    cursor.executemany(insert1, dados)
    connection.commit()

from configuracao import TABLE_NAME, cursor, connection


# Registrar valores nas colunas da tabela
# CUIDADE: sql injection


cursor.execute(f"select * from {TABLE_NAME}")
colunhas = cursor.description

for linha in range(len(colunhas[0])):
    for column in colunhas:
        print(column)






















# insert1 = (
#     f"""
#     INSERT INTO {TABLE_NAME} (Modelo, Cor, Ano)
#     VALUES (?, ?, ?)
#     """
# )
#
# nova_valor = input().split(' ')
# modelo, cor, ano = nova_valor[0], nova_valor[1], nova_valor[2]
# cursor.execute(insert1, [modelo, cor, ano])
# connection.commit()


# def inserir(modelo, cor, ano):
#     dados = list(zip(modelo, cor, ano))
#     # cursor.execute(insert1, (modelo, cor, ano))
#     cursor.executemany(insert1, dados)
#     connection.commit()

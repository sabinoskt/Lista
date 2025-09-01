from sqlite.configuracao import cursor, TABLE_NAME, connection


def update(var_modelo: str, var_cor: str, var_ano: int, id: int):
    cursor.execute(
        f"""
        UPDATE {TABLE_NAME}
        SET modelo= ?, cor= ?, ano= ?
        WHERE id = ?
        """,
        (var_modelo, var_cor, var_ano, id)
    )
    connection.commit()

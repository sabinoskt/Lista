from sqlite.configuracao import cursor, TABLE_NAME, connection

def update(var_modelo, var_cor, var_ano, id):
    cursor.execute(
        f"""
        UPDATE {TABLE_NAME}
        SET modelo={var_modelo}, cor={var_cor}, ano={var_ano}
        WHERE id = {id}
        """
    )
    connection.commit()

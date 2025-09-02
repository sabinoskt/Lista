from sqlite.configuracao import cursor, TABLE_NAME, connection

# cursor.execute(
#     f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")
#
# cursor.execute(
#         f"DELETE FROM {TABLE_NAME}"
#     )
#
# connection.commit()


def delete(id: int):
    # CUIDADO: fazendo delete sem where
    # cursor.execute(
    #     f"DELETE FROM {TABLE_NAME}"
    # )

    # DELETE mais cuidadoso
    # cursor.execute(
    #     f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")

    cursor.execute(
        f"""
        select * from {TABLE_NAME}
        where id = ?
        """,
        [id]
    )
    linha_removida = cursor.fetchone()

    if linha_removida:
        cursor.execute(
            f"""
            DELETE FROM {TABLE_NAME}
            WHERE id = ?
            """,
            [id]
        )
        connection.commit()
        return linha_removida
    else:
        return None

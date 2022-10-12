
def get_transactions_ignored(cursor, day):
    """
    Cuenta el número de registros de la tabla “ignored_transactions” del día anterior.
    """

    query = (
        f"""
        SELECT 
            COUNT(transaction_date) as counted
        FROM 
            ignored_transactions
        WHERE 
            transaction_date = '{day}';
        """ 
    )
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print(f"total transactions ignored: {result}")

    return result


def get_users_transactions_ignored(cursor, day):
    """
    Cuenta el número único de usuarios en la tabla ignored_transactions del día correspondiente.
    """

    query = (
        f"""
        SELECT
            COUNT(DISTINCT user_id) as counted
        FROM
            ignored_transactions
        WHERE
            transaction_date = '{day}';
        """
    )
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print(f"total users transactions ignored: {result}")

    return result
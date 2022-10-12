
def get_recategorized_by_users(cursor, day):
    """
    Cuenta el número de registros de la tabla 'reclassified_transactions' del día anterior.
    """

    query = (
        f"""
        SELECT
            COUNT(transaction_date) as counted
        FROM
            reclassified_transactions
        WHERE
            transaction_date = '{day}';
        """
    )
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print(f"total recategorized by users: {result}")

    return result


def get_users_transactions_categorized(cursor, day):
    """
    Cuenta el número de usuarios únicos en los registros de la tabla “reclassified_transactions” del día anterior.
    """

    query = (
        f"""
        SELECT
            COUNT(DISTINCT user_id) as counted
        FROM
            reclassified_transactions
        WHERE
            transaction_date = '{day}';
        """
    )
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print(f"total users transactions categorized: {result}")

    return result

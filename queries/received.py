
def get_transactions_received(cursor, day):
    """
    Cuenta las transacciones insertadas del día anterior a la ejecución del proceso.
    """

    query = (
        f"""
        SELECT 
            COUNT(transaction_date) as counted
        FROM 
            transactions
        WHERE 
            transaction_date = '{day}';
        """ 
    )
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print(f"total transactions received: {result}")

    return result

def get_users_transactions_received(cursor, day):
    """
    Cuenta los usuarios únicos de las transacciones del día anterior a la ejecución del proceso.
    """

    query = (
        f"""
        SELECT
            COUNT(DISTINCT user_id) as counted
        FROM
            transactions
        WHERE
            transaction_date = '{day}';
        """
    )
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    print(f"total users transactions received: {result}")

    return result

from db_connection import connect_to_db


def transactions_report():
    cursor = connect_to_db().cursor()
    query = (
        "SELECT COUNT(*) FROM transactions;",
        "SELECT SUM(amount) FROM transactions;",
        "SELECT AVG(amount) FROM transactions;",
    )
    average_transaction_query = """
        SELECT 
            a.account_number,
            a.account_holder_name,
            AVG(t.amount) AS avg_transaction_amount
        FROM 
            transactions t
        JOIN 
            accounts a
            ON t.account_id = a.account_number
        GROUP BY 
            a.account_number, a.account_holder_name
        ORDER BY 
            avg_transaction_amount DESC
        LIMIT 10;
    """

    cursor.execute(average_transaction_query)
    results = cursor.fetchall()
    cursor.execute(query[0])
    total_transactions = cursor.fetchone()[0]
    cursor.execute(query[1])
    total_amount = cursor.fetchone()[0]
    cursor.execute(query[2])
    average_amount = cursor.fetchone()[0]

    print(f"Total transactions: {total_transactions}")
    print(f"Total amount: {total_amount}")
    print(f"Average amount: {average_amount} \n")
    print("Top 10 customers by transaction amount: Account")

    for account in results:
        print(f"{account[0]} \t{account[1]} \t{account[2]}")

    return True

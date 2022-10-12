from queries import categorized
from queries import ignored
from queries import received
from queries.load_metrics import insert

from database import get_connector
from constants import YESTERDAY


def main():
    conn = get_connector()
    cursor = conn.cursor()

    # received
    transactions_received = received.get_transactions_received(cursor, YESTERDAY)
    users_transactions_received = received.get_users_transactions_received(cursor, YESTERDAY)

    # categorized
    recategorized_by_users = categorized.get_recategorized_by_users(cursor, YESTERDAY)
    users_transactions_categorized = categorized.get_users_transactions_categorized(cursor, YESTERDAY)

    # ignored
    transactions_ignored = ignored.get_transactions_ignored(cursor, YESTERDAY)
    users_transactions_ignored = ignored.get_users_transactions_ignored(cursor, YESTERDAY)

    # inserting metrics
    insert(
        cursor=cursor,
        metrics=dict(
            metrics_date=YESTERDAY,
            transactions_received=transactions_received,
            users_transactions_received=users_transactions_received,
            recategorized_by_users=recategorized_by_users,
            users_transactions_categorized=users_transactions_categorized,
            transactions_ignored=transactions_ignored,
            users_transactions_ignored=users_transactions_ignored,
        ),
    ) 

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

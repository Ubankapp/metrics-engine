from json import dumps

from typing import Dict
from uuid import uuid4


def insert(cursor, metrics: Dict):
    query = (
    f"""
        INSERT INTO spendings_daily
            (
                id,
                metrics_date,
                transactions_received,
                users_transactions_received,
                recategorized_by_users,
                users_transactions_categorized,
                transactions_ignored,
                users_transactions_ignored,
                transactions_categorized
            )
        VALUES 
            (
                '{uuid4()}',
                '{metrics["metrics_date"]}',
                {metrics["transactions_received"]},
                {metrics["users_transactions_received"]},
                {metrics["recategorized_by_users"]},
                {metrics["users_transactions_categorized"]},
                {metrics["transactions_ignored"]},
                {metrics["users_transactions_ignored"]},
                0
            );
    """
    )
    cursor.execute(query)
    print(f"inserted metric: {dumps(metrics, indent=4)}")

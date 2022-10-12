from os import environ

from dotenv import load_dotenv

import psycopg2


load_dotenv()


connectors = {
    "name": environ["DB_NAME"],
    "user": environ["DB_USER"],
    "password": environ["DB_PASSWORD"],
    "port": environ["DB_PORT"],
    "host": environ["DB_HOST"],
}

def get_connector():
    connection = psycopg2.connect(
        user=connectors["user"],
        password=connectors["password"],
        host=connectors["host"],
        port=connectors["port"],
        database=connectors["name"],
    )
    return connection

"""
Connect to Postgres
"""
import os

from dotenv import load_dotenv

import psycopg2 as ps

load_dotenv()

POSTGRES_ADDRESS = os.getenv("POSTGRES_ADDRESS")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME")
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


def connect_to_postgres():
    """ Returns connection object"""
    conn = ps.connect(host=POSTGRES_ADDRESS,
                      user=POSTGRES_USERNAME,
                      password=POSTGRES_PASSWORD,
                      port=POSTGRES_PORT,
                      database=POSTGRES_DBNAME)
    return conn

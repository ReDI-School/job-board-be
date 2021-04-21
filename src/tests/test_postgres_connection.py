"""
Test the connection to the postgresql db
"""
import logging

from src.db.connect import connect_to_postgres


def test_postgres():
    """
    Test connection to postgres
    """
    conn = connect_to_postgres()
    cur = conn.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'public'""")
    tables = cur.fetchall()
    assert tables



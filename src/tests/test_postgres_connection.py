"""
Test the connection to the postgresql db
"""
import logging

from src.db.connect import connect_to_postgres
from src.db.jobs import get_jobs


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


def test_jobs():
    conn = connect_to_postgres()
    jobs = get_jobs(conn, limit=2, skip=0, employment_type="Full-Time", experience_level="Entry-level")
    assert jobs


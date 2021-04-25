"""Sets up the jobs table"""

from typing import List, Dict

import psycopg2.extras


def get_jobs(conn) -> List[Dict]:
    """
    Check if the jobs table exists. If not, create it.
    Returns:
        [{"timestamp: "", poster:"",..}, {}]
    """
    query_string = """
        SELECT * FROM jobs LIMIT 20;
    """
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query_string)
    jobs_tuples = cursor.fetchall()
    jobs = []
    for job in jobs_tuples:
        jobs.append(dict(job))

    return jobs

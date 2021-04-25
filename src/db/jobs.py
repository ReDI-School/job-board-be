"""Sets up the jobs table"""

import psycopg2.extras


def get_jobs(conn):
    """
    Check if the jobs table exists. If not, create it.

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

"""Sets up the jobs table"""


def get_jobs(conn):
    """
    Check if the jobs table exists. If not, create it.

    """
    query_string = """
        SELECT * FROM jobs LIMIT 20;
    """
    cursor = conn.cursor()
    cursor.execute(query_string)
    return cursor.fetchall()

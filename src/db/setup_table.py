"""Sets up the jobs table"""


def create_jobs_table(conn):
    """
    Check if the jobs table exists. If not, create it.

    """
    query_string = """
        CREATE TABLE IF NOT EXISTS jobs(
            id integer PRIMARY KEY,
            timestamp text,
            source text,
            header text,
            content text,
            language text,
            experience text,
            employment_time text,
            poster text,
            application_link text,
            company_name text,
            location text,
            deadline text,
            community_only text,
            contact_name text
        );
    """
    cursor = conn.cursor()
    cursor.execute(query_string)
    conn.commit()

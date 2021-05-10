"""Sets up the jobs table"""

from typing import List, Dict, Optional

import psycopg2.extras


def get_jobs(conn, limit=20, skip=0, language: Optional[str] = None, employment_type: Optional[str] = None, experience_level: Optional[str] = None) -> List[Dict]:
    """
    Check if the jobs table exists. If not, create it.
    Returns:
        [{"timestamp: "", poster:"",..}, {}]
    """
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        query_string = f"SELECT * FROM jobs WHERE ID > 0 "
        if language:
            query_string += f"AND language = '{language}' "
        if employment_type:
            query_string += f"AND employment_type = '{employment_type}' "
        if experience_level:
            query_string += f"AND experience_level = '{experience_level}' "

        query_string += f"LIMIT {limit} OFFSET {skip};"

        cursor.execute(query_string)
        jobs_tuples = cursor.fetchall()

        if len(jobs_tuples)<1:
            raise Exception("no items found")

        jobs = []
        for job in jobs_tuples:
            jobs.append(dict(job))

        return jobs
    except:
        cursor.execute("ROLLBACK")
        raise 

    


def get_job_by_id(conn, jobId: int) -> Dict:
    """
    try to return the job with the provided jobId
    """
    if not jobId or jobId == "":
        return {}
    
    query_string = f'SELECT * FROM jobs WHERE id = {jobId};'
        
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query_string)
    job = cursor.fetchone()
    
    if job:
        return dict(job)

    return {}

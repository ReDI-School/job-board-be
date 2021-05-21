"""Sets up the jobs table"""

from typing import List, Dict, Optional

import psycopg2.extras


def get_jobs(conn, limit=20, skip=0, language: Optional[str] = None, employment_type: Optional[str] = None, experience_level: Optional[str] = None) :
    """
    Check if the jobs table exists. If not, create it.
    Returns:
        [{"timestamp: "", poster:"",..}, {}]
    """
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        # query_string = f"SELECT *, count(*) OVER() as full_count FROM jobs WHERE ID > 0 "
        query_string = f"SELECT * FROM jobs WHERE ID > 0 "

        query_string_filters="" # create a new string only for filters since we want to reuse them later
        if language:
            query_string_filters += f"AND language = '{language}' "
        if employment_type:
            query_string_filters += f"AND employment_type = '{employment_type}' "
        if experience_level:
            query_string_filters += f"AND experience_level = '{experience_level}' "

        query_string+=query_string_filters 

        query_string += f"LIMIT {limit} OFFSET {skip};"

        cursor.execute(query_string)
        jobs_tuples = cursor.fetchall()

        if len(jobs_tuples)<1:
            raise Exception("no items found")

        jobs = []
        for job in jobs_tuples:
            jobs.append(dict(job))

        # count all the jobs for the provided filters. Doing this in a seperate query is horrible but it should be fine for now
        count_jobs_query_string="SELECT COUNT(*) FROM jobs WHERE ID > 0 "
        count_jobs_query_string+=query_string_filters
        
        cursor.execute(count_jobs_query_string)
        count=cursor.fetchone()

        data={}
        data["count"]=count[0]
        data["jobs"]=jobs

        return data
    except:
        cursor.execute("ROLLBACK")
        raise 

    


def get_job_by_id(conn, jobId: int) -> Dict:
    """
    try to return the job with the provided jobId
    """
    try:
        #if not jobId or jobId == "":
        #    raise ValueError("no valid job id provided")
        
        query_string = f'SELECT * FROM jobs WHERE id = {jobId};'
            
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(query_string)
        job = cursor.fetchone()
        
        if not job:
            raise Exception(f"Could not find job for the provided id: {jobId}")
        
        return dict(job)
                
    except:
        # maybe rollback here not sure if needed tho
        raise
    

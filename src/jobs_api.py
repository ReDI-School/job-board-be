"""
Jobs API
"""

import logging
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.db import connect, setup_table, jobs
from src.request_models import JobsRequestPayload

conn = connect.connect_to_postgres()
setup_table.create_jobs_table(conn)

app = FastAPI()

origins = ["http://localhost:8080","https://localhost:8080", "https://redi-school.github.io", "https://jobs.communityredi.school"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.post("/")
def post_jobs(payload: JobsRequestPayload):
    """
    #TODO: Implement connection to DB and query
    """
    #logging.warning(payload)
    #jobs = {"job1": "Data Scientist"}
    #return jobs
    return


@app.get("/{jobId}")
def get_jobs(jobId: int):
    """
    Return all jobs from DB
    """
    try:
        queried_jobs = jobs.get_job_by_id(conn, jobId)
        return queried_jobs
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

@app.get("/")
def get_jobs(skip: int = 0, limit: int = 20, language: Optional[str] = None, employment_type: Optional[str] = None, experience_level: Optional[str] = None, order_by: Optional[str]="id", order_direction: Optional[str]="DESC"):
    """
    Return all jobs from DB
    """
    
    try:
        queried_jobs = jobs.get_jobs(conn, limit, skip, language, employment_type, experience_level, order_by, order_direction)
        queried_jobs["loaded"]=len(queried_jobs["jobs"]) or 0
        queried_jobs["start"]=skip

        return queried_jobs
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

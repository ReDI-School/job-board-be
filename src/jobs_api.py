"""
Jobs API
"""

import logging

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.db import connect, setup_table, jobs
from src.request_models import JobsRequestPayload

conn = connect.connect_to_postgres()
setup_table.create_jobs_table(conn)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

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


@app.get("/")
def get_jobs():
    """
    Return all jobs from DB
    """
    queried_jobs = jobs.get_jobs(conn)
    return queried_jobs


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

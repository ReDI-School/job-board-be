"""
Jobs API
"""

import logging

from fastapi import FastAPI
from fastapi.requests import Request
import uvicorn

from src.db import connect, setup_table
from src.request_models import JobsRequestPayload

conn = connect.connect_to_postgres()
setup_table.create_jobs_table(conn)

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/")
def post_jobs(payload: JobsRequestPayload):
    """
    #TODO: Implement connection to DB and query
    """
    logging.warning(payload)
    jobs = {"job1": "Data Scientist"}
    return jobs


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

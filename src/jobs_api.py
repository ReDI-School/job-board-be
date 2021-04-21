"""
Jobs API
"""

import logging

from fastapi import FastAPI
from fastapi.requests import Request
import uvicorn

from src.request_models import JobsRequestPayload

app = FastAPI()


@app.post("/")
def request_jobs(payload: JobsRequestPayload):
    """
    #TODO: Implement connection to DB and query
    """
    logging.warning(payload)
    jobs = {"job1": "Data Scientist"}
    return jobs


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

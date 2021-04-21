from typing import Optional
from pydantic import BaseModel


class JobsRequestPayload(BaseModel):
    """ request payload model for jobs
    TODO: add parameters for API request
    """
    language: Optional[str] = "de"
    request_all: Optional[bool] = True

"""
Test the Jobs API
"""

from fastapi.testclient import TestClient

from src.jobs_api import app

client = TestClient(app)


def test_request():
    """
    Test sending simple request to jobs api
    """
    request_dict = {
        "language": "de",
        "request_all": True,
    }

    response = client.post(
        "/", headers={"X-Token": "coneofsilence"}, json=request_dict
    )
    assert response.status_code == 200
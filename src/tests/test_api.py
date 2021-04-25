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
    response = client.get(
        "/", headers={"X-Token": "coneofsilence"}
    )
    assert response.status_code == 200
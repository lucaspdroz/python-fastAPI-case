from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.routers.tiny_url import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_tiny_url_post_success():
    response = client.post("/tiny_url", json={"input_url": "https://www.google.com"})
    assert response.status_code == 200
    data = response.json()
    assert "tiny_url" in data
    assert data["old_url"] == "https://www.google.com"

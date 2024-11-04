from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.routers.hello import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_hello_with_name():
    response = client.get("/hello?name=Lucas")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Lucas!"


def test_hello_missing_name():
    response = client.get("/hello")
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Query parameter 'name' is required."


def test_hello_invalid_name():
    response = client.get("/hello?name=123")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, 123!"

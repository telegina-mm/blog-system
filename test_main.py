from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/api/users/",
        json={
            "email": "test@example.com",
            "login": "testuser",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["login"] == "testuser"


def test_create_post():
    response = client.post(
        "/api/posts/",
        json={"title": "Test Post", "content": "This is a test post content"},
        params={"author_id": 1},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Post"

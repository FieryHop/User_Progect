def test_create_user(client):
    response = client.post("/users/", json={"username": "testuser", "role": "manager"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert "id" in data


def test_get_user(client):
    user = client.post(
        "/users/", json={"username": "stutterer", "role": "manager"}
    ).json()

    response = client.get(f"/users/{user['id']}")
    assert response.status_code == 200
    assert response.json()["username"] == "stutterer"


def test_delete_user(client):
    user = client.post("/users/", json={"username": "ronin", "role": "manager"}).json()

    response = client.delete(f"/users/{user['id']}", params={"user_id": user["id"]})

    assert response.status_code == 200
    assert response.json()["message"] == "Пользователь удален"

    response = client.get(f"/users/{user['id']}")
    assert response.status_code == 404

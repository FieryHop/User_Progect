def test_create_project(client):
    manager = client.post(
        "/users/", json={"username": "manager1", "role": "manager"}
    ).json()

    response = client.post(
        "/projects/", json={"name": "Проект X", "manager_id": manager["id"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Проект X"
    assert data["manager_id"] == manager["id"]


def test_create_project_with_invalid_manager(client):
    response = client.post("/projects/", json={"name": "Проект X", "manager_id": 999})
    assert response.status_code == 400

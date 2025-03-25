def test_get_report(client):
    manager = client.post("/users/", json={"username": "Nul", "role": "manager"}).json()
    project = client.post(
        "/projects/", json={"name": "Проект", "manager_id": manager["id"]}
    ).json()
    timelog = client.post(
        "/timelogs/",
        json={
            "user_id": manager["id"],
            "project_id": project["id"],
            "hours": 8.0,
            "date_field": "2025-01-15",
        },
    ).json()

    response = client.get(
        f"/reports/reports/project/{project['id']}",
        params={
            "start_date": "2025-01-01",
            "end_date": "2025-02-01",
            "manager_id": manager["id"],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 1
    assert data["items"][0]["hours"] == 8.0

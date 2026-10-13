from fastapi.testclient import TestClient

from robot_knowledge_engine.api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_sources_are_exposed_without_local_paths() -> None:
    response = client.get("/api/v1/sources")
    payload = response.json()
    assert response.status_code == 200
    assert payload["count"] >= 8
    assert all("location" not in source for source in payload["sources"])

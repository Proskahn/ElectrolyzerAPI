from fastapi.testclient import TestClient
from electrolyzer.main import app

client = TestClient(app)


def test_choose_membrane():
    response = client.post(
        "/api/v1/compile/choose-membrane", json={"membrane": "Nafion115"}
    )
    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "Selected membrane: Nafion115"
    assert "details" in data
    assert isinstance(data["details"], dict)


def test_choose_catalyst():
    response = client.post(
        "/api/v1/compile/choose-catalyst", json={"catalyst": "Combination1"}
    )
    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "Selected catalyst: Combination1"
    assert "details" in data
    assert isinstance(data["details"], dict)

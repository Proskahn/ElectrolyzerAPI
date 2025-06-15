from fastapi.testclient import TestClient
from electrolyzer.main import app

client = TestClient(app)

def test_choose_membrane():
    response = client.post("/api/v1/compile/choose-membrane", json={"membrane": "Nafion115"})
    assert response.status_code == 200
    assert response.json() == {"message": "Selected membrane: Nafion115"}
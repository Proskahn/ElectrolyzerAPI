from fastapi.testclient import TestClient
from electrolyzer.api.endpoints.compile import router  # adjust path based on your structure
from fastapi import FastAPI
from electrolyzer.config.electrolyzer import ElectrolyzerConfig
from electrolyzer.service.electrolyzer import ElectrolyzerService
# Create a test app and include the router
app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_configure_electrolyzer():
    response = client.post("/compile/configure_electrolyzer", json={"temperature": 310.0})
    assert response.status_code == 200
    data = response.json()
    assert data["configured_parameters"]["temperature"] == 310.0
    assert data["configured_parameters"]["pressure"] == 1.0  # default

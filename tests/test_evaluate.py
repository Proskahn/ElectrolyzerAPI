from fastapi.testclient import TestClient
from electrolyzer.api.endpoints.evaluate import router  # adjust path based on your structure
from fastapi import FastAPI
from electrolyzer.config.electrolyzer import ElectrolyzerConfig
from electrolyzer.service.electrolyzer import ElectrolyzerService
# Create a test app and include the router
app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_open_circuit_voltage():
    response = client.post("/evaluate/compute-open-circuit-voltage", json={"temperature": 310.0})
    assert response.status_code == 200
    data = response.json()
    expected_voltage = 1.229 -9.0*1e-4*(310.0 - 298.15)
    assert abs(data["open_circuit_voltage"]-expected_voltage) <1e-5

def test_ohm_potential():
    response = client.post("/evaluate/compute-ohm-potential", json={"R_membrane": 0.1})
    assert response.status_code == 200
    data = response.json()
    expected_value = 0.0
    assert abs(data["ohmic_potential"]-expected_value)<1e-5

def test_life_prediction():
    response = client.post("/evaluate/life-prediction")
    assert response.status_code == 200
    data = response.json()
    expoected_value = 1.0
    assert abs(data["lifespan"]-expoected_value)<1e-5
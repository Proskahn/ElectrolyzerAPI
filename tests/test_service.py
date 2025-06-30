import pytest
from casadi import MX
from electrolyzer.service.electrolyzer import ElectrolyzerService
from electrolyzer.config.electrolyzer import ElectrolyzerConfig


@pytest.fixture
def sample_config():
    return ElectrolyzerConfig(
        waterflow=1.0,
        temperature=298.15,
        pressure=1.0,
        R_membrane=0.1,
        i0_anode=1e-4,
        i0_cathode=1e-4,
        alpha_anode=0.5,
        alpha_cathode=0.5,
        A=0.01,
        GDL_thickness=0.0001,
        channel_width=0.001,
        channel_depth=0.001
    )


def test_configure_and_get_config(sample_config):
    service = ElectrolyzerService()
    service.configure(sample_config)
    retrieved = service.get_config()
    assert isinstance(retrieved, ElectrolyzerConfig)
    assert retrieved.temperature == sample_config.temperature


def test_life_prediction_returns_none(sample_config):
    service = ElectrolyzerService()
    service.configure(sample_config)
    prediction = service.life_prediction()
    print("Prediction: ", prediction)
    assert prediction == 1.0


def test_compute_OHM_potential_returns_zero(sample_config):
    service = ElectrolyzerService()
    service.configure(sample_config)
    ohmic = service.compute_OHM_potential(sample_config)
    assert ohmic == 0.0


def test_compute_open_circuit_voltage(sample_config):
    service = ElectrolyzerService()
    service.configure(sample_config)
    voltage = service.compute_open_circuit_voltage(sample_config)
    expected_voltage = 1.229 - 900.0 * (sample_config.temperature - 298.15)
    assert isinstance(voltage, float)
    assert abs(voltage - expected_voltage) < 1e-5

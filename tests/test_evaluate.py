import pytest
from api.evaluate.temperature_optimizer import TemperatureOptimizer


def test_default_temperature():
    optimizer = TemperatureOptimizer()
    temp = optimizer.compute_best_temperature()
    assert temp == 70.0


def test_temperature_with_current_density():
    optimizer = TemperatureOptimizer()
    temp = optimizer.compute_best_temperature(current_density=3.0)
    assert optimizer.min_temp <= temp <= optimizer.max_temp

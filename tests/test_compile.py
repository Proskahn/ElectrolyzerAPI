import pytest
from api.compile.membrane_selector import MembraneSelector


def test_list_membranes():
    selector = MembraneSelector()
    membranes = selector.list_membranes()
    assert "Nafion 115" in membranes
    assert "Nafion 117" in membranes
    assert isinstance(membranes, list)


def test_select_membrane_valid():
    selector = MembraneSelector()
    response = selector.select_membrane("Nafion 117")
    assert "selected" in response


def test_select_membrane_invalid():
    selector = MembraneSelector()
    response = selector.select_membrane("Unknown Membrane")
    assert "not supported" in response

from ..Config.condition import Condition
import casadi as ca
from pydantic import BaseModel, Field, ConfigDict


class Membrane(Condition):
    def __init__(self, membrane_name: str):
        self.name = membrane_name

    def compute_ionic_conductivity(self) -> casadi.MX:
        # The equation can be found on Jingxian Chen, Hong Lv, Xiaojun Shen, Cunman Zhang,
        # Multi-objective optimization design and sensitivity analysis of proton exchange membrane electrolytic cell,
        # Journal of Cleaner Production,
        # Volume 434,
        # 2024,
        # 140045,
        # ISSN 0959-6526,
        # https://doi.org/10.1016/j.jclepro.2023.140045.
        # I am not sure what parameter the membrane should provide
        # as I have not saw any isolated test of membrane.
        # Most of them were tested in an electrolyzer, where the only
        # parameter the membrane should provide is its name.
        if self.name == "Nafion117":
            water_content = 16.0
            return (0.5139 * water_content - 0.326) * ca.exp(
                1268 / 303 - 1268 / self.temperature
            )
        else:
            return None

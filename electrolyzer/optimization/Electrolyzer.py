from electrolyzer.optimization.interface.controlcomponent import ControlComponent
from electrolyzer.optimization.interface.costcomponent import CostComponent
from electrolyzer.optimization.interface.statecomponent import StateComponent
from electrolyzer.optimization.interface.constraintcomponent import ConstraintComponent
from electrolyzer.optimization.constant import GAS_CONSTANT_IN_JOULE_PER_MOL_KELVIN as R
from electrolyzer.optimization.constant import FARADY_CONSTANT_in_COULOMB_PER_MOL as F
import casadi as ca


class ElectrolyzerDigitalTwin(
    CostComponent, ControlComponent, StateComponent, ConstraintComponent
):
    "Formulate the optimization problem"

    def __init__(self):
        super().__init__()

    def set_state(self):
        self.add_state("current_density")
        self.add_state("hydrogen_production_rate")

    def set_control(self):
        self.add_control("water_temperature")
        self.add_control("actual_voltage")

    def set_cost(self):
        self.add_cost(
            "energy_cost",
            self.control["actual_voltage"] * self.state["current_density"],
        )

    def set_constraint(self):
        reversible_voltage = 1.229 - 9.0 * 1e-4 * (
            self.control["water_temperature"] - 298.0
        )
        # going to be corrected, this is wrong
        alpha_wrong = 1.0
        i_0_wrong = 1e-2
        open_circuit_voltage = (
            R
            * self.control["water_temperature"]
            / (alpha_wrong * F)
            * ca.log(self.state["current_density"] / i_0_wrong)
        )
        # suppose 0.1 is the overall Ohm resistance
        ohm_law = self.state["current_density"] * 0.1
        """The relations are not correct yet, just a place_holder to show how it works"""
        self.add_constraint(
            "overall_voltage",
            self.control["actual_voltage"]
            - reversible_voltage
            - open_circuit_voltage
            - ohm_law,
        )

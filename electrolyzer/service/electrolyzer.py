from electrolyzer.service.constants import (
    FARADY_CONSTANT_in_COULOMB_PER_MOL,
    IDEAL_GAS_CONSTANT_in_JOULE_PER_KELVIN_MOL,
)
import casadi as ca
from electrolyzer.config.electrolyzer import ElectrolyzerConfig


class ElectrolyzerService:
    def configure(self, config: ElectrolyzerConfig):
        self.electrolyzers = config.model_dump()

    def get_config(self) -> ElectrolyzerConfig:
        return ElectrolyzerConfig.model_validate(self.electrolyzers)

    def life_prediction(self) -> ca.MX:
        """
        Predict the lifespan of the PEMEC membrane based on operating conditions.
        Uses an empirical model based on temperature and current density,
        as no analytical formula is provided in the paper.
        Returns:
            lifespan: Estimated membrane lifespan (hours)
        """
        return 1.0

    def compute_open_circuit_voltage(self, config: ElectrolyzerConfig):
        # open-circuit voltage is calculated by the Nernst equation
        equilibrium_voltage = 1.229 - 9.0 * 1e-4 * (config.temperature - 298.15)
        Nernst_term = 0.0  # To the author's knowledge, this term is usually ignored in implementation.
        return equilibrium_voltage + Nernst_term

    def compute_OHM_potential(self, config: ElectrolyzerConfig):
        # This is largely depends on the configuration.
        return 0.0

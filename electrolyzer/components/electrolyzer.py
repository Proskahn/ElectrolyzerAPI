from .condition import Condition
from constants import (
    FARADAY_CONSTANT_in_COULOMB_PER_MOL,
    IDEAL_GAS_CONSTANT_in_JOULE_PER_KELVIN_MOL,
)
import casadi as ca


class Electrolyzer(Condition):
    def __init__(self, membrane: str, condition: dict):
        super().__init__(condition)
        self.membrane = membrane
        # Define typical PEMEC parameters (based on literature and paper)
        self.R_membrane = 0.0001  # Membrane resistance (ohm m^2), typical for Nafion
        self.i0_anode = 1e-6  # Exchange current density for OER (A/m^2)
        self.i0_cathode = 1e-3  # Exchange current density for HER (A/m^2)
        self.alpha_anode = 0.5  # Charge transfer coefficient for anode
        self.alpha_cathode = 0.5  # Charge transfer coefficient for cathode
        self.A = 0.01  # Electrode area (m^2), assumed for a small cell
        self.GDL_thickness = 0.0003  # GDL thickness (m), typical value
        self.channel_width = 0.002  # Channel width (m), from paper's recommendation
        self.channel_depth = 0.002  # Channel depth (m), from paper's recommendation

    def compute_actual_voltage(self, current_density: ca.MX) -> ca.MX:
        """
        Compute the actual voltage of the PEMEC, consisting of:
        - Open circuit voltage (OCV)
        - Activation overvoltage (Butler-Volmer)
        - Ohmic overvoltage
        - Diffusion overvoltage
        Parameters:
            current_density: Symbolic variable for current density (A/m^2)
        Returns:
            V_total: Total cell voltage (V)
        """
        # 1. Open Circuit Voltage (OCV)
        # Using Nernst equation for water electrolysis, adjusted for temperature and pressure
        T = self.temperature  # Temperature in Kelvin
        P = self.pressure  # Pressure in Pa
        R = IDEAL_GAS_CONSTANT_in_JOULE_PER_KELVIN_MOL
        F = FARADAY_CONSTANT_in_COULOMB_PER_MOL
        E0 = 1.229 - 0.000845 * (
            T - 298.15
        )  # Standard potential at 25°C, adjusted for temperature
        # Nernst correction for pressure (assuming ideal gas behavior for O2 and H2)
        P0 = 101325  # Standard pressure (Pa)
        V_ocv = E0 + (R * T) / (2 * F) * ca.log(P / P0)

        # 2. Activation Overvoltage (Butler-Volmer equation)
        # Anode (OER) overpotential
        eta_act_anode = (
            (R * T)
            / (self.alpha_anode * 2 * F)
            * ca.asinh(current_density / (2 * self.i0_anode))
        )
        # Cathode (HER) overpotential
        eta_act_cathode = (
            (R * T)
            / (self.alpha_cathode * 2 * F)
            * ca.asinh(current_density / (2 * self.i0_cathode))
        )
        eta_act = eta_act_anode + eta_act_cathode

        # 3. Ohmic Overvoltage
        # Ohmic loss = I * R, where I = current_density * area, R is membrane resistance
        eta_ohmic = current_density * self.R_membrane

        # 4. Diffusion Overvoltage
        # Simplified model based on mass transfer limitations (empirical, as per paper)
        # Assume diffusion losses increase with current density and are affected by flow rate
        # Paper suggests low flow rate hinders water diffusion (page 3)
        flow_factor = 1.0 / (
            1.0 + ca.exp(-self.waterflow / 0.001)
        )  # Normalize flow effect
        eta_diff = (
            0.1 * current_density / (10000 + current_density) * flow_factor
        )  # Empirical term

        # Total voltage
        V_total = V_ocv + eta_act + eta_ohmic + eta_diff
        return V_total

    def life_prediction(self) -> ca.MX:
        """
        Predict the lifespan of the PEMEC membrane based on operating conditions.
        Uses an empirical model based on temperature and current density,
        as no analytical formula is provided in the paper.
        Returns:
            lifespan: Estimated membrane lifespan (hours)
        """
        # Paper indicates temperature has significant impact (page 1)
        # Assume exponential degradation with temperature and current density
        T = self.temperature
        P = self.pressure
        i = ca.MX.sym("i", 1)  # Current density as a symbolic variable
        T_ref = 353.15  # Reference temperature (80°C)
        i_ref = 10000  # Reference current density (A/m^2)
        # Empirical degradation rate: increases with higher T and i
        degradation_rate = ca.exp((T - T_ref) / 50) * (i / i_ref) ** 0.5
        # Base lifespan (hours) adjusted by degradation
        base_lifespan = 50000  # Typical Nafion membrane lifespan
        lifespan = base_lifespan / degradation_rate
        return lifespan

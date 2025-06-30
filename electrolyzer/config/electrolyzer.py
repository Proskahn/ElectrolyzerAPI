from pydantic import BaseModel


class ElectrolyzerConfig(BaseModel):
    # Following data is default value which could be changed.
    waterflow: float = 1.0
    temperature: float = 298.15
    pressure: float = 1.0
    R_membrane: float = 0.1
    i0_anode: float = 1e-4
    i0_cathode: float = 1e-4
    alpha_anode: float = 0.5
    alpha_cathode: float = 0.5
    A: float = 0.01
    GDL_thickness: float = 0.0001
    channel_width: float = 0.001
    channel_depth: float = 0.001

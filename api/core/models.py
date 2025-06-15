from pydantic import BaseModel
from typing import Optional


class Membrane(BaseModel):
    """
    Represents a membrane with basic metadata.
    """

    name: str
    thickness_microns: Optional[float] = None
    conductivity_s: Optional[float] = None


class OperationParameters(BaseModel):
    """
    Represents operating parameters for the electrolyzer.
    """

    temperature_celsius: Optional[float] = None
    pressure_bar: Optional[float] = None
    current_density_a_per_cm2: Optional[float] = None

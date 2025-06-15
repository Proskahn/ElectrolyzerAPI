from pydantic import BaseModel


class MembraneRequest(BaseModel):
    membrane: str  # e.g., Nafion 115, Nafion 117


class TemperatureResponse(BaseModel):
    temperature: float  # Placeholder for computed temperature
    message: str  # Optional message or status

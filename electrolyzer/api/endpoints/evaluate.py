from fastapi import APIRouter
from electrolyzer.config.electrolyzer import ElectrolyzerConfig
from electrolyzer.service.electrolyzer import ElectrolyzerService

router = APIRouter(prefix="/evaluate", tags=["evalute"])


@router.post("/compute-open-circuit-voltage")
async def compute_open_circuit_voltage(config: ElectrolyzerConfig):
    service = ElectrolyzerService()
    result = service.compute_open_circuit_voltage(config)
    return {"open_circuit_voltage": result}


@router.post("/compute-ohm-potential")
async def compute_ohm_potential(config: ElectrolyzerConfig):
    service = ElectrolyzerService()
    result = service.compute_OHM_potential(config)
    return {"ohmic_potential": result}


@router.post("/life-prediction")
async def predict_life():
    service = ElectrolyzerService()
    result = service.life_prediction()
    return {"lifespan": result}

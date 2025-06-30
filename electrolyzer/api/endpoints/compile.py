from fastapi import APIRouter
from electrolyzer.config.electrolyzer import ElectrolyzerConfig

router = APIRouter(prefix="/compile", tags=["compile"])


@router.post("/configure_electrolyzer")
async def configure_electrolyzer(config: ElectrolyzerConfig):
    return {"configured_parameters": config.model_dump()}

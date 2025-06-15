from fastapi import APIRouter
from electrolyzer.core.models import MembraneRequest, CatalystRequest
from electrolyzer.core.calculations import choose_membrane, choose_catalyst

router = APIRouter(prefix="/compile", tags=["compile"])


@router.post("/choose-membrane")
async def choose_membrane_endpoint(request: MembraneRequest):
    result = choose_membrane(request.membrane)
    return {"message": f"Selected membrane: {request.membrane}", "details": result}


@router.post("/choose-catalyst")
async def choose_catalyst_endpoint(request: CatalystRequest):
    result = choose_catalyst(request.catalyst)
    return {"message": f"Selected catalyst: {request.catalyst}", "details": result}

from fastapi import APIRouter

router = APIRouter(prefix="/compile", tags=["compile"])


@router.post("/choose-membrane")
async def choose_membrane(membrane: str):
    # Placeholder for membrane selection logic (e.g., Nafion 115, 117)
    return {"message": f"Selected membrane: {membrane}"}

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from electrolyzer.api.v1.compile import router as compile_router
from electrolyzer.api.v1.evaluate import router as evaluate_router
from electrolyzer.core.config import settings

app = FastAPI(title=settings.api_name, version=settings.api_version)

app.include_router(compile_router, prefix=f"/api/{settings.api_version}")
app.include_router(evaluate_router, prefix=f"/api/{settings.api_version}")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

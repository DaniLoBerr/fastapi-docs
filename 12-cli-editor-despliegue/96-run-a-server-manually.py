"""96/112 - Run a Server Manually
https://fastapi.tiangolo.com/deployment/manually/
"""

from fastapi import APIRouter

router = APIRouter(prefix="/cli-editor-deployment/run-a-server-manually", tags=["CLI, editor y despliegue"])

# Agrega aquí el código de la lección de FastAPI

@router.get("/")
async def read_lesson():
    return {
        "section": "CLI, editor y despliegue",
        "lesson": "Run a Server Manually",
        "path": "/cli-editor-deployment/run-a-server-manually",
        "reference_url": "https://fastapi.tiangolo.com/deployment/manually/",
    }
